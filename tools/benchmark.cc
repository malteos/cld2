// CLD2 Benchmark
//
// Measures language detection speed on cached HTML pages stored in JSONL.
// Each JSONL line: {"id": N, "html": "<base64>", "size": N}
//
// Usage:
//   ./benchmark --cache data/benchmark/cache.jsonl --experiment <name>
//               [--num-pages N] [--iterations N] [--results-file PATH]

#include <algorithm>
#include <chrono>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <numeric>
#include <string>
#include <sys/stat.h>
#include <vector>

#include "../public/compact_lang_det.h"
#include "../public/encodings.h"

struct PageData {
  std::string content;
};

struct PageResult {
  int sample_id;
  int content_length;
  double time_us;  // microseconds
  const char* lang_name;
  const char* lang_code;
  bool is_reliable;
  int percent;
};

// Minimal base64 decoder
static const unsigned char b64_table[256] = {
    64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,
    64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,
    64,64,64,64,64,64,64,64,64,64,64,62,64,64,64,63,
    52,53,54,55,56,57,58,59,60,61,64,64,64,65,64,64,
    64, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,
    15,16,17,18,19,20,21,22,23,24,25,64,64,64,64,64,
    64,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,
    41,42,43,44,45,46,47,48,49,50,51,64,64,64,64,64,
    64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,
    64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,
    64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,
    64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,
    64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,
    64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,
    64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,
    64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,
};

std::string base64_decode(const char* src, size_t len) {
  std::string out;
  out.reserve(len * 3 / 4);
  unsigned int buf = 0;
  int bits = 0;
  for (size_t i = 0; i < len; i++) {
    unsigned char c = b64_table[(unsigned char)src[i]];
    if (c >= 64) continue;  // skip padding/invalid
    buf = (buf << 6) | c;
    bits += 6;
    if (bits >= 8) {
      bits -= 8;
      out.push_back((char)(buf >> bits));
      buf &= (1 << bits) - 1;
    }
  }
  return out;
}

// Extract a JSON string value for a given key (minimal parser)
// Returns pointer to start of value and sets len
const char* json_string_value(const char* json, const char* key,
                              size_t* value_len) {
  // Find "key": (with optional space after colon)
  std::string needle = std::string("\"") + key + "\":";
  const char* pos = strstr(json, needle.c_str());
  if (!pos) return nullptr;
  pos += needle.size();
  // Skip whitespace
  while (*pos == ' ') pos++;
  if (*pos != '"') return nullptr;
  pos++;  // skip opening quote
  // Find closing quote (base64 has no escapes)
  const char* end = strchr(pos, '"');
  if (!end) return nullptr;
  *value_len = end - pos;
  return pos;
}

// Load pages from JSONL cache file
std::vector<PageData> load_pages(const char* cache_file, int max_pages) {
  std::ifstream ifs(cache_file);
  if (!ifs) {
    fprintf(stderr, "Error: cannot open cache file: %s\n", cache_file);
    exit(1);
  }

  std::vector<PageData> pages;
  pages.reserve(max_pages);
  std::string line;

  while ((int)pages.size() < max_pages && std::getline(ifs, line)) {
    size_t b64_len = 0;
    const char* b64 = json_string_value(line.c_str(), "html", &b64_len);
    if (!b64) continue;

    PageData page;
    page.content = base64_decode(b64, b64_len);
    pages.push_back(std::move(page));
  }
  return pages;
}

// Run CLD2 detection on all pages, return per-page results
std::vector<PageResult> benchmark_pages(const std::vector<PageData>& pages) {
  std::vector<PageResult> results;
  results.reserve(pages.size());

  for (int i = 0; i < (int)pages.size(); i++) {
    const auto& page = pages[i];

    CLD2::Language language3[3];
    int percent3[3];
    double normalized_score3[3];
    CLD2::ResultChunkVector resultchunkvector;
    int text_bytes;
    bool is_reliable;

    CLD2::CLDHints cldhints = {nullptr, nullptr, CLD2::UNKNOWN_ENCODING,
                               CLD2::UNKNOWN_LANGUAGE};
    int valid_prefix_bytes;

    auto t0 = std::chrono::high_resolution_clock::now();

    CLD2::Language lang = CLD2::ExtDetectLanguageSummaryCheckUTF8(
        page.content.data(), (int)page.content.size(),
        false,  // is_plain_text (HTML input)
        &cldhints,
        0,  // flags
        language3, percent3, normalized_score3,
        nullptr,  // resultchunkvector
        &text_bytes, &is_reliable,
        &valid_prefix_bytes);

    auto t1 = std::chrono::high_resolution_clock::now();
    double time_us =
        std::chrono::duration<double, std::micro>(t1 - t0).count();

    PageResult r;
    r.sample_id = i;
    r.content_length = (int)page.content.size();
    r.time_us = time_us;
    r.lang_name = CLD2::LanguageName(lang);
    r.lang_code = CLD2::LanguageCode(lang);
    r.is_reliable = is_reliable;
    r.percent = percent3[0];
    results.push_back(r);
  }
  return results;
}

struct AggregateStats {
  double total_ms;
  double mean_ms;
  double median_ms;
  double p95_ms;
  double p99_ms;
  double stddev_ms;
  int num_pages;
  long long total_bytes;
};

AggregateStats compute_stats(const std::vector<PageResult>& results) {
  AggregateStats stats = {};
  stats.num_pages = (int)results.size();

  std::vector<double> times;
  times.reserve(results.size());
  for (const auto& r : results) {
    times.push_back(r.time_us / 1000.0);  // convert to ms
    stats.total_bytes += r.content_length;
  }

  std::sort(times.begin(), times.end());
  double sum = std::accumulate(times.begin(), times.end(), 0.0);

  stats.total_ms = sum;
  stats.mean_ms = sum / times.size();
  stats.median_ms = times[times.size() / 2];
  stats.p95_ms = times[(int)(times.size() * 0.95)];
  stats.p99_ms = times[(int)(times.size() * 0.99)];

  // stddev
  double sq_sum = 0;
  for (double t : times) {
    sq_sum += (t - stats.mean_ms) * (t - stats.mean_ms);
  }
  stats.stddev_ms = sqrt(sq_sum / times.size());

  return stats;
}

// Ensure directory exists (recursive mkdir)
void mkdirs(const std::string& path) {
  std::string cmd = "mkdir -p " + path;
  system(cmd.c_str());
}

// Get parent directory of a file path
std::string dirname(const std::string& path) {
  size_t pos = path.rfind('/');
  if (pos == std::string::npos) return ".";
  return path.substr(0, pos);
}

// Get current UTC timestamp as ISO 8601
std::string utc_timestamp() {
  time_t now = time(nullptr);
  struct tm tm;
  gmtime_r(&now, &tm);
  char buf[32];
  strftime(buf, sizeof(buf), "%Y-%m-%dT%H:%M:%SZ", &tm);
  return std::string(buf);
}

void write_results_tsv(const AggregateStats& stats, const char* experiment,
                       int iteration, const char* results_file) {
  mkdirs(dirname(results_file));

  bool file_exists = false;
  {
    struct stat st;
    file_exists = (stat(results_file, &st) == 0 && st.st_size > 0);
  }

  FILE* f = fopen(results_file, "a");
  if (!f) {
    fprintf(stderr, "Error: cannot open %s for writing\n", results_file);
    return;
  }

  if (!file_exists) {
    fprintf(f,
            "experiment_name\titeration\ttotal_time_ms\tmean_time_ms\t"
            "median_time_ms\tp95_time_ms\tp99_time_ms\tstddev_time_ms\t"
            "num_pages\ttotal_bytes\ttimestamp\n");
  }

  fprintf(f, "%s\t%d\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%d\t%lld\t%s\n",
          experiment, iteration, stats.total_ms, stats.mean_ms,
          stats.median_ms, stats.p95_ms, stats.p99_ms, stats.stddev_ms,
          stats.num_pages, stats.total_bytes, utc_timestamp().c_str());
  fclose(f);
}

void write_predictions_tsv(const std::vector<PageResult>& results,
                           const char* experiment,
                           const char* results_dir) {
  std::string exp_dir =
      std::string(results_dir) + "/experiments/" + experiment;
  mkdirs(exp_dir);
  std::string path = exp_dir + "/predictions.tsv";

  FILE* f = fopen(path.c_str(), "w");
  if (!f) {
    fprintf(stderr, "Error: cannot open %s for writing\n", path.c_str());
    return;
  }

  fprintf(f, "sample_id\tdetected_language\tlanguage_code\tis_reliable\tpercent\n");
  for (const auto& r : results) {
    fprintf(f, "%d\t%s\t%s\t%s\t%d\n", r.sample_id, r.lang_name, r.lang_code,
            r.is_reliable ? "true" : "false", r.percent);
  }
  fclose(f);
  fprintf(stderr, "Predictions written to %s\n", path.c_str());
}

void print_usage(const char* prog) {
  fprintf(stderr,
          "Usage: %s --cache FILE --experiment NAME\n"
          "       [--num-pages N] [--iterations N] [--results-file PATH]\n",
          prog);
}

int main(int argc, char** argv) {
  // Defaults
  const char* cache_file = "data/benchmark/cache.jsonl";
  const char* experiment = nullptr;
  const char* results_file = "data/benchmark/results.csv";
  int num_pages = 10000;
  int iterations = 5;

  // Parse args
  for (int i = 1; i < argc; i++) {
    if (strcmp(argv[i], "--cache") == 0 && i + 1 < argc) {
      cache_file = argv[++i];
    } else if (strcmp(argv[i], "--experiment") == 0 && i + 1 < argc) {
      experiment = argv[++i];
    } else if (strcmp(argv[i], "--results-file") == 0 && i + 1 < argc) {
      results_file = argv[++i];
    } else if (strcmp(argv[i], "--num-pages") == 0 && i + 1 < argc) {
      num_pages = atoi(argv[++i]);
    } else if (strcmp(argv[i], "--iterations") == 0 && i + 1 < argc) {
      iterations = atoi(argv[++i]);
    } else {
      print_usage(argv[0]);
      return 1;
    }
  }

  if (!experiment) {
    fprintf(stderr, "Error: --experiment is required\n");
    print_usage(argv[0]);
    return 1;
  }

  // Load pages
  fprintf(stderr, "Loading pages from %s...\n", cache_file);
  std::vector<PageData> pages = load_pages(cache_file, num_pages);
  fprintf(stderr, "Loaded %d pages\n", (int)pages.size());

  if (pages.empty()) {
    fprintf(stderr, "Error: no pages found\n");
    return 1;
  }

  // Warmup run (discard)
  fprintf(stderr, "Warmup run...\n");
  benchmark_pages(pages);

  // Results dir for predictions (dirname of results_file)
  std::string results_dir = dirname(results_file);

  // Benchmark iterations
  std::vector<AggregateStats> all_stats;
  std::vector<PageResult> last_results;

  for (int iter = 0; iter < iterations; iter++) {
    fprintf(stderr, "Iteration %d/%d...\n", iter + 1, iterations);
    last_results = benchmark_pages(pages);
    AggregateStats stats = compute_stats(last_results);
    all_stats.push_back(stats);
    write_results_tsv(stats, experiment, iter + 1, results_file);

    fprintf(stderr,
            "  total=%.3fms  mean=%.3fms  median=%.3fms  "
            "p95=%.3fms  p99=%.3fms  stddev=%.3fms\n",
            stats.total_ms, stats.mean_ms, stats.median_ms, stats.p95_ms,
            stats.p99_ms, stats.stddev_ms);
  }

  // Write predictions from last iteration
  write_predictions_tsv(last_results, experiment, results_dir.c_str());

  // Print summary across iterations
  fprintf(stderr, "\n--- Summary: %s (%d iterations x %d pages) ---\n",
          experiment, iterations, (int)pages.size());

  std::vector<double> means, medians;
  for (const auto& s : all_stats) {
    means.push_back(s.mean_ms);
    medians.push_back(s.median_ms);
  }
  std::sort(means.begin(), means.end());
  std::sort(medians.begin(), medians.end());

  double mean_of_means =
      std::accumulate(means.begin(), means.end(), 0.0) / means.size();
  double mean_of_medians =
      std::accumulate(medians.begin(), medians.end(), 0.0) / medians.size();

  // Stddev of means across iterations
  double sq_sum = 0;
  for (double m : means) sq_sum += (m - mean_of_means) * (m - mean_of_means);
  double stddev_of_means = sqrt(sq_sum / means.size());

  fprintf(stderr, "  mean(mean):   %.4f ms  (+/- %.4f ms)\n", mean_of_means,
          stddev_of_means);
  fprintf(stderr, "  mean(median): %.4f ms\n", mean_of_medians);
  fprintf(stderr, "  best mean:    %.4f ms\n", means.front());
  fprintf(stderr, "  worst mean:   %.4f ms\n", means.back());

  return 0;
}
