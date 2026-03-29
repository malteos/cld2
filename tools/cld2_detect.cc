// CLD2 Line-Level Language Detection CLI
//
// Reads UTF-8 text lines from stdin, detects language for each line.
// Output per line (tab-separated): lang_code\tlang_name\tis_reliable\tpercent
//
// Usage:
//   echo "This is English text" | ./cld2_detect
//   cat samples.txt | ./cld2_detect

#include <cstdio>
#include <cstring>
#include <string>

#include "../public/compact_lang_det.h"
#include "../public/encodings.h"

int main(int argc, char** argv) {
  std::string line;
  char buf[65536];

  while (fgets(buf, sizeof(buf), stdin)) {
    // Strip trailing newline
    size_t len = strlen(buf);
    while (len > 0 && (buf[len - 1] == '\n' || buf[len - 1] == '\r')) {
      buf[--len] = '\0';
    }

    if (len == 0) {
      printf("un\tUnknown\tfalse\t0\n");
      continue;
    }

    CLD2::Language language3[3];
    int percent3[3];
    double normalized_score3[3];
    int text_bytes;
    bool is_reliable;

    CLD2::CLDHints cldhints = {nullptr, nullptr, CLD2::UNKNOWN_ENCODING,
                                CLD2::UNKNOWN_LANGUAGE};
    int valid_prefix_bytes;

    CLD2::Language lang = CLD2::ExtDetectLanguageSummaryCheckUTF8(
        buf, (int)len,
        true,   // is_plain_text
        &cldhints,
        0,      // flags
        language3, percent3, normalized_score3,
        nullptr,  // resultchunkvector
        &text_bytes, &is_reliable,
        &valid_prefix_bytes);

    printf("%s\t%s\t%s\t%d\n",
           CLD2::LanguageCode(lang),
           CLD2::LanguageName(lang),
           is_reliable ? "true" : "false",
           percent3[0]);
  }

  return 0;
}
