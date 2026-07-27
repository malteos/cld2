#!/usr/bin/env python3
"""Register a new language in CLD2's generated language tables.

CLD2 reserves unused Language enum slots (X_183 .. X_505) and unused
per-script language numbers. This script claims one of each and rewrites
the parallel arrays in internal/generated_language.cc (and the enum
comment in internal/generated_language.h) so the rest of CLD2 -- and the
table trainer -- can use the new language.

Updated arrays:
  kLanguageToName[]      "X_183"  -> "CHUVASH"
  kLanguageToCName[]     "X_183"  -> "Chuvash"
  kLanguageToCode[]      ""       -> "cv"
  kLanguageToScripts[]   {None,..}-> {ULScript_Cyrillic, ...}
  kLanguageToPLang[]     0        -> free per-script number
  kPLangToLanguageLatn[] or kPLangToLanguageOthr[]  UNKNOWN_LANGUAGE -> X_183
  kNameToLanguage[]      sorted insert (size constant bumped)
  kCodeToLanguage[]      sorted insert (size constant bumped)

Usage:
  register_language.py --code cv --name CHUVASH --script Cyrillic
  register_language.py --code szl --name SILESIAN --script Latin

The script is idempotent: re-registering an existing code is a no-op.
"""

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CC = REPO / "internal" / "generated_language.cc"
H = REPO / "internal" / "generated_language.h"

# Scripts whose spans are scored with the quadgram/octagram tables and can
# therefore actually be trained. Others are listed for completeness.
RTYPE_MANY = {"Latin", "Cyrillic", "Arabic", "Hebrew", "Devanagari",
              "Bengali", "Tibetan", "Ethiopic"}


def find_array(lines, header_re):
    """Return (start, end) line indexes of an array body: header .. '};'."""
    start = None
    for i, line in enumerate(lines):
        if re.search(header_re, line):
            start = i
            break
    if start is None:
        sys.exit(f"error: cannot find array {header_re} in {CC}")
    for j in range(start + 1, len(lines)):
        if lines[j].startswith("};"):
            return start, j
    sys.exit(f"error: unterminated array {header_re}")


def row_with_index(lines, start, end, idx):
    """Find the row inside [start,end] whose trailing comment is '// idx ...'."""
    pat = re.compile(r"//\s*" + str(idx) + r"(\s|$)")
    for i in range(start + 1, end):
        if pat.search(lines[i]):
            return i
    sys.exit(f"error: cannot find row // {idx} in array at line {start + 1}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--code", required=True,
                    help="language code to register, e.g. cv or szl")
    ap.add_argument("--name", required=True,
                    help="UPPERCASE_NAME for the language, e.g. CHUVASH")
    ap.add_argument("--script", required=True,
                    help="primary script, e.g. Latin or Cyrillic")
    ap.add_argument("--cname", default=None,
                    help="CamelCase display name (default: from --name)")
    args = ap.parse_args()

    code = args.code
    name = args.name.upper()
    cname = args.cname or name.capitalize()
    script = args.script

    if script not in RTYPE_MANY:
        print(f"warning: script {script} is not RTypeMany; CLD2 will not "
              f"consult the trained tables for it", file=sys.stderr)

    text = CC.read_text()
    lines = text.split("\n")

    # Idempotency: is the code already present?
    m = re.search(r'\{"' + re.escape(code) + r'",\s*(\d+)\},', text)
    if m:
        print(f"{code} already registered as language {m.group(1)}")
        return

    # ---- claim a free Language slot ----
    # Free slots have a bare number as their name: `"183",  // 183`
    n_start, n_end = find_array(lines, r"kLanguageToName\[kLanguageToNameSize\]")
    slot = None
    for i in range(n_start + 1, n_end):
        m = re.match(r'\s*"(\d+)",\s*//\s*\1\s*$', lines[i])
        if m:
            slot = int(m.group(1))
            name_row = i
            break
    if slot is None:
        sys.exit("error: no free X_NNN language slots left")

    # ---- claim a free per-script number ----
    if script == "Latin":
        p_hdr = r"kPLangToLanguageLatn\[256\]"
    else:
        p_hdr = r"kPLangToLanguageOthr\[256\]"
    p_start, p_end = find_array(lines, p_hdr)
    plang = None
    for i in range(p_end - 1, p_start, -1):   # highest free first
        m = re.match(r"\s*UNKNOWN_LANGUAGE,\s*//\s*(\d+)\s*$", lines[i])
        if m and 100 <= int(m.group(1)) <= 249:
            plang = int(m.group(1))
            plang_row = i
            break
    if plang is None:
        sys.exit(f"error: no free per-script numbers in {p_hdr}")

    print(f"registering {code} = {name}: Language slot {slot} (X_{slot}), "
          f"per-script number {plang} ({script} space)")

    # ---- kLanguageToName ----
    lines[name_row] = f'  "{name}",  // {slot} {code}'

    # ---- kLanguageToCName ----
    c_start, c_end = find_array(
        lines, r"kLanguageToCName\[kLanguageToCNameSize\]")
    r = row_with_index(lines, c_start, c_end, slot)
    lines[r] = f'  "{cname}",  // {slot} {code}'

    # ---- kLanguageToCode ----
    co_start, co_end = find_array(
        lines, r"kLanguageToCode\[kLanguageToCodeSize\]")
    r = row_with_index(lines, co_start, co_end, slot)
    lines[r] = f'  "{code}",  // {slot} {name}'

    # ---- kLanguageToScripts ----
    s_start, s_end = find_array(
        lines, r"kLanguageToScripts\[kLanguageToScriptsSize\]")
    r = row_with_index(lines, s_start, s_end, slot)
    lines[r] = f'  {{ULScript_{script}, None, None, None, }},  // {slot} {code}'

    # ---- kLanguageToPLang ----
    pl_start, pl_end = find_array(
        lines, r"kLanguageToPLang\[kLanguageToPLangSize\]")
    r = row_with_index(lines, pl_start, pl_end, slot)
    lines[r] = f'  {plang:3d},  // {slot} {code}'

    # ---- kPLangToLanguageLatn / Othr ----
    lines[plang_row] = f'  X_{slot},                 // {plang} {name} {code}'

    # ---- sorted insert into kNameToLanguage ----
    def insert_sorted(header_re, key, value_line):
        a_start, a_end = find_array(lines, header_re)
        entries = []
        for i in range(a_start + 1, a_end):
            m = re.match(r'\s*\{"([^"]+)",', lines[i])
            if m:
                entries.append((i, m.group(1)))
        pos = a_end   # default: append at end
        for i, k in entries:
            if k > key:
                pos = i
                break
        lines.insert(pos, value_line)

    insert_sorted(r"kNameToLanguage\[kNameToLanguageSize\]", name,
                  f'  {{"{name}", {slot}}},  // {code}')
    insert_sorted(r"kCodeToLanguage\[kCodeToLanguageSize\]", code,
                  f'  {{"{code}", {slot}}},  // {code}')

    # ---- bump the lookup-array size constants ----
    out = "\n".join(lines)
    for const in ("kNameToLanguageSize", "kCodeToLanguageSize"):
        m = re.search(r"extern const int " + const + r" = (\d+);", out)
        if not m:
            sys.exit(f"error: cannot find {const}")
        out = out.replace(m.group(0),
                          f"extern const int {const} = {int(m.group(1)) + 1};")

    CC.write_text(out)

    # ---- annotate the enum in the header (cosmetic but helpful) ----
    htext = H.read_text()
    htext, n = re.subn(
        r"(  X_" + str(slot) + r"\s+= " + str(slot) + r",)\s*//.*",
        rf"\1  // {name} {code} (registered by register_language.py)",
        htext, count=1)
    if n:
        H.write_text(htext)

    print(f"done: edit {CC.relative_to(REPO)} committed to disk")


if __name__ == "__main__":
    main()
