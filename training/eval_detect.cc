// Evaluation harness for trained CLD2 tables.
//
// Reads a TSV of <language-code> TAB <utf8 text> on --in (or stdin) and
// reports per-language detection accuracy plus the most common confusions.
// Link this against the CLD2 sources with either the stock generated
// tables or a trained replacement (see training/train.py).

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <map>
#include <string>
#include <utility>

#include "compact_lang_det.h"
#include "encodings.h"

int main(int argc, char** argv) {
  const char* in_file = NULL;
  bool show_errors = false;
  for (int i = 1; i < argc; ++i) {
    if (strcmp(argv[i], "--in") == 0 && i + 1 < argc) {in_file = argv[++i];}
    else if (strcmp(argv[i], "--show_errors") == 0) {show_errors = true;}
    else {
      fprintf(stderr, "usage: %s [--in eval.tsv] [--show_errors]\n", argv[0]);
      return 1;
    }
  }
  FILE* fp = in_file ? fopen(in_file, "rb") : stdin;
  if (fp == NULL) {
    fprintf(stderr, "error: cannot open %s\n", in_file);
    return 1;
  }

  std::map<std::string, std::pair<long, long> > per_lang;  // code -> (ok, n)
  std::map<std::pair<std::string, std::string>, long> confusions;
  long total = 0, correct = 0;

  char* buf = NULL;
  size_t cap = 0;
  ssize_t n;
  while ((n = getline(&buf, &cap, fp)) >= 0) {
    if (n > 0 && buf[n - 1] == '\n') {buf[--n] = '\0';}
    char* tab = strchr(buf, '\t');
    if (tab == NULL) {continue;}
    *tab = '\0';
    const char* truth = buf;
    const char* text = tab + 1;
    int text_len = n - (tab + 1 - buf);
    if (text_len <= 0) {continue;}

    bool is_reliable;
    CLD2::Language language3[3];
    int percent3[3];
    double normalized_score3[3];
    int text_bytes;
    CLD2::CLDHints hints = {NULL, NULL, CLD2::UNKNOWN_ENCODING,
                            CLD2::UNKNOWN_LANGUAGE};
    CLD2::Language lang = CLD2::ExtDetectLanguageSummary(
        text, text_len, /*is_plain_text=*/true, &hints, /*flags=*/0,
        language3, percent3, normalized_score3, NULL, &text_bytes,
        &is_reliable);

    std::string got = CLD2::LanguageCode(lang);
    // Truth codes may carry region/script suffixes; compare base code
    std::string want(truth);
    bool ok = (got == want);
    ++total;
    per_lang[want].second++;
    if (ok) {++correct; per_lang[want].first++;}
    else {
      ++confusions[std::make_pair(want, got)];
      if (show_errors) {
        printf("MISS want=%s got=%s reliable=%d text=%.60s\n", want.c_str(),
               got.c_str(), is_reliable ? 1 : 0, text);
      }
    }
  }
  free(buf);
  if (in_file) {fclose(fp);}

  printf("\nOverall: %ld/%ld = %.2f%%\n", correct, total,
         total ? 100.0 * correct / total : 0.0);
  printf("%-10s %8s %8s %8s\n", "lang", "correct", "total", "acc%");
  for (std::map<std::string, std::pair<long, long> >::iterator it =
           per_lang.begin(); it != per_lang.end(); ++it) {
    printf("%-10s %8ld %8ld %7.2f%%\n", it->first.c_str(), it->second.first,
           it->second.second,
           it->second.second ? 100.0 * it->second.first / it->second.second
                             : 0.0);
  }
  if (!confusions.empty()) {
    printf("\nTop confusions (want -> got):\n");
    std::multimap<long, std::pair<std::string, std::string> > by_count;
    for (auto& kv : confusions) {by_count.insert({kv.second, kv.first});}
    int shown = 0;
    for (std::multimap<long, std::pair<std::string, std::string> >::
             reverse_iterator it = by_count.rbegin();
         it != by_count.rend() && shown < 20; ++it, ++shown) {
      printf("  %-6s -> %-6s %ld\n", it->second.first.c_str(),
             it->second.second.c_str(), it->first);
    }
  }
  return 0;
}
