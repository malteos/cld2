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
  bool matches_baseline;  // true if matches baseline or no baseline provided
};

// Load baseline predictions from TSV (sample_id \t lang \t lang_code ...)
// Returns vector of language codes indexed by sample_id
std::vector<std::string> load_baseline(const char* path) {
  std::vector<std::string> codes;
  std::ifstream ifs(path);
  if (!ifs) {
    fprintf(stderr, "Error: cannot open baseline file: %s\n", path);
    exit(1);
  }
  std::string line;
  std::getline(ifs, line);  // skip header
  while (std::getline(ifs, line)) {
    // Fields: sample_id \t detected_language \t language_code \t ...
    // We want the 3rd field (language_code)
    int tab_count = 0;
    size_t start = 0, end = 0;
    for (size_t i = 0; i < line.size(); i++) {
      if (line[i] == '\t') {
        tab_count++;
        if (tab_count == 2) start = i + 1;
        if (tab_count == 3) { end = i; break; }
      }
    }
    if (tab_count >= 3) {
      codes.push_back(line.substr(start, end - start));
    }
  }
  return codes;
}

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
// If baseline is non-empty, compare each result's lang_code against it
std::vector<PageResult> benchmark_pages(
    const std::vector<PageData>& pages,
    const std::vector<std::string>& baseline = {}) {
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
    r.matches_baseline = baseline.empty() ||
        (i < (int)baseline.size() && baseline[i] == r.lang_code);
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
  int baseline_matches;   // -1 if no baseline
  double accuracy;        // 0.0-1.0, or -1 if no baseline
};

AggregateStats compute_stats(const std::vector<PageResult>& results,
                             bool has_baseline) {
  AggregateStats stats = {};
  stats.num_pages = (int)results.size();

  std::vector<double> times;
  times.reserve(results.size());
  int matches = 0;
  for (const auto& r : results) {
    times.push_back(r.time_us / 1000.0);  // convert to ms
    stats.total_bytes += r.content_length;
    if (r.matches_baseline) matches++;
  }

  if (has_baseline) {
    stats.baseline_matches = matches;
    stats.accuracy = (double)matches / results.size();
  } else {
    stats.baseline_matches = -1;
    stats.accuracy = -1;
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
            "num_pages\ttotal_bytes\taccuracy\ttimestamp\n");
  }

  fprintf(f, "%s\t%d\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%d\t%lld\t%s\t%s\n",
          experiment, iteration, stats.total_ms, stats.mean_ms,
          stats.median_ms, stats.p95_ms, stats.p99_ms, stats.stddev_ms,
          stats.num_pages, stats.total_bytes,
          stats.accuracy >= 0 ? std::to_string(stats.accuracy).substr(0, 6).c_str() : "n/a",
          utc_timestamp().c_str());
  fclose(f);
}

void write_predictions_tsv(const std::vector<PageResult>& results,
                           const char* experiment) {
  std::string exp_dir =
      std::string("data/benchmark/") + experiment;
  mkdirs(exp_dir);
  std::string path = exp_dir + "/predictions.tsv";

  FILE* f = fopen(path.c_str(), "w");
  if (!f) {
    fprintf(stderr, "Error: cannot open %s for writing\n", path.c_str());
    return;
  }

  fprintf(f, "sample_id\tdetected_language\tlanguage_code\tis_reliable\tpercent\tmatches_baseline\n");
  for (const auto& r : results) {
    fprintf(f, "%d\t%s\t%s\t%s\t%d\t%s\n", r.sample_id, r.lang_name, r.lang_code,
            r.is_reliable ? "true" : "false", r.percent,
            r.matches_baseline ? "y" : "n");
  }
  fclose(f);
  fprintf(stderr, "Predictions written to %s\n", path.c_str());
}

// Fixed benchmark parameters
static const char* const kCacheFile = "data/benchmark/test-data/10k.jsonl";
static const int kNumPages = 10000;
static const char* const kBaselinePredictions = "data/benchmark/baseline/predictions.tsv";

void print_usage(const char* prog) {
  fprintf(stderr,
          "Usage: %s [--experiment NAME] [--iterations N] [--results-file PATH]\n",
          prog);
}

int main(int argc, char** argv) {
  // Defaults
  const char* experiment = nullptr;
  const char* results_file = nullptr;
  int iterations = 1;

  // Parse args
  for (int i = 1; i < argc; i++) {
    if (strcmp(argv[i], "--experiment") == 0 && i + 1 < argc) {
      experiment = argv[++i];
    } else if (strcmp(argv[i], "--results-file") == 0 && i + 1 < argc) {
      results_file = argv[++i];
    } else if (strcmp(argv[i], "--iterations") == 0 && i + 1 < argc) {
      iterations = atoi(argv[++i]);
    } else {
      print_usage(argv[0]);
      return 1;
    }
  }

  // Load pages
  fprintf(stderr, "Loading pages from %s...\n", kCacheFile);
  std::vector<PageData> pages = load_pages(kCacheFile, kNumPages);
  fprintf(stderr, "Loaded %d pages\n", (int)pages.size());

  if (pages.empty()) {
    fprintf(stderr, "Error: no pages found\n");
    return 1;
  }

  // Load baseline if available
  std::vector<std::string> baseline;
  bool has_baseline = false;
  {
    struct stat st;
    if (stat(kBaselinePredictions, &st) == 0 && st.st_size > 0) {
      baseline = load_baseline(kBaselinePredictions);
      has_baseline = true;
      fprintf(stderr, "Loaded baseline with %d predictions from %s\n",
              (int)baseline.size(), kBaselinePredictions);
    }
  }

  // Warmup run (discard)
  fprintf(stderr, "Warmup run...\n");
  benchmark_pages(pages);

  // Benchmark iterations
  std::vector<AggregateStats> all_stats;
  std::vector<PageResult> last_results;

  for (int iter = 0; iter < iterations; iter++) {
    fprintf(stderr, "Iteration %d/%d...\n", iter + 1, iterations);
    last_results = benchmark_pages(pages, baseline);
    AggregateStats stats = compute_stats(last_results, has_baseline);
    all_stats.push_back(stats);
    if (results_file && experiment) {
      write_results_tsv(stats, experiment, iter + 1, results_file);
    }

    fprintf(stderr,
            "  total=%.3fms  mean=%.3fms  median=%.3fms  "
            "p95=%.3fms  p99=%.3fms  stddev=%.3fms",
            stats.total_ms, stats.mean_ms, stats.median_ms, stats.p95_ms,
            stats.p99_ms, stats.stddev_ms);
    if (has_baseline) {
      fprintf(stderr, "  accuracy=%.2f%% (%d/%d)",
              stats.accuracy * 100, stats.baseline_matches, stats.num_pages);
    }
    fprintf(stderr, "\n");
  }

  // Write predictions from last iteration
  if (experiment) {
    write_predictions_tsv(last_results, experiment);
  }

  // Print summary across iterations
  fprintf(stderr, "\n");

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

  // Compute p95/p99 averages across iterations
  std::vector<double> p95s, p99s, totals;
  for (const auto& s : all_stats) {
    p95s.push_back(s.p95_ms);
    p99s.push_back(s.p99_ms);
    totals.push_back(s.total_ms);
  }
  double mean_p95 = std::accumulate(p95s.begin(), p95s.end(), 0.0) / p95s.size();
  double mean_p99 = std::accumulate(p99s.begin(), p99s.end(), 0.0) / p99s.size();
  double mean_total = std::accumulate(totals.begin(), totals.end(), 0.0) / totals.size();

  // Summary table to stdout
  printf("\n---\n");
  if (experiment) {
    printf("experiment: %s\n", experiment);
  }
  printf("pages: %d\n", (int)pages.size());
  printf("iterations: %d\n", iterations);
  printf("total_ms: %.3f\n", mean_total);
  printf("mean_ms: %.4f\n", mean_of_means);
  printf("median_ms: %.4f\n", mean_of_medians);
  printf("p95_ms: %.4f\n", mean_p95);
  printf("p99_ms: %.4f\n", mean_p99);
  printf("stddev_ms: %.4f\n", stddev_of_means);
  if (has_baseline) {
    printf("accuracy: %.4f\n", all_stats.back().accuracy);
  }

  return 0;
}
