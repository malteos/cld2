#!/usr/bin/env python3
"""End-to-end CLD2 training pipeline.

Steps:
  1. (optional) register new languages in the generated language tables
  2. build the table trainer (generate_cld2_tables)
  3. run it over the training TSV -> training/output/cld2_generated_trained.cc
  4. build the evaluation binary against the trained tables
  5. evaluate on the held-out TSV

Usage (after fetching data with fetch_leipzig.py):
  python3 training/train.py \
      --train training/data/train.tsv --eval training/data/eval.tsv \
      --register cv:CHUVASH:Cyrillic --register szl:SILESIAN:Latin

Any extra trainer options can be passed through with --trainer_arg.
"""

import argparse
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TRAINING = REPO / "training"
INTERNAL = REPO / "internal"

CXX = "g++"
CXXFLAGS = ["-O2", "-std=c++11", "-Wno-narrowing",
            f"-I{INTERNAL}", f"-I{REPO / 'public'}"]

# Sources for the trainer binary (no scoring tables linked in).
TRAINER_SOURCES = [
    "getonescriptspan.cc", "utf8statetable.cc", "fixunicodevalue.cc",
    "generated_entities.cc", "offsetmap.cc", "generated_ulscript.cc",
    "generated_language.cc", "lang_script.cc", "cldutil_shared.cc",
    "cldutil_offline.cc", "tote.cc",
]

# Sources for the runtime/eval binary, minus the four table files that the
# trainer regenerates (quadchrome_2, deltaoctachrome, distinctoctachrome,
# score_quad_octa_2) which are replaced by the trained output file.
RUNTIME_SOURCES = [
    "cldutil.cc", "cldutil_shared.cc", "compact_lang_det.cc",
    "compact_lang_det_hint_code.cc", "compact_lang_det_impl.cc", "debug.cc",
    "fixunicodevalue.cc", "generated_entities.cc", "generated_language.cc",
    "generated_ulscript.cc", "getonescriptspan.cc", "lang_script.cc",
    "offsetmap.cc", "scoreonescriptspan.cc", "tote.cc", "utf8statetable.cc",
    "cld_generated_cjk_uni_prop_80.cc", "cld2_generated_cjk_compatible.cc",
    "cld_generated_cjk_delta_bi_4.cc", "generated_distinct_bi_0.cc",
]


def run(cmd, **kw):
    print("+ " + " ".join(str(c) for c in cmd), file=sys.stderr)
    subprocess.run([str(c) for c in cmd], check=True, **kw)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--train", required=True, help="training TSV")
    ap.add_argument("--eval", default=None, help="held-out eval TSV")
    ap.add_argument("--register", action="append", default=[],
                    metavar="code:NAME:Script",
                    help="register a new language first (repeatable)")
    ap.add_argument("--out", default=str(TRAINING / "output"),
                    help="output directory for generated tables")
    ap.add_argument("--trainer_arg", action="append", default=[],
                    help="extra argument passed to generate_cld2_tables")
    ap.add_argument("--show_errors", action="store_true",
                    help="print each misclassified eval document")
    args = ap.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    trained_cc = out_dir / "cld2_generated_trained.cc"

    # 1. Register languages (idempotent)
    for spec in args.register:
        try:
            code, name, script = spec.split(":")
        except ValueError:
            sys.exit(f"error: bad --register {spec}, want code:NAME:Script")
        run([sys.executable, TRAINING / "register_language.py",
             "--code", code, "--name", name, "--script", script])

    # 2. Build trainer
    trainer_bin = out_dir / "generate_cld2_tables"
    run([CXX] + CXXFLAGS + [TRAINING / "generate_cld2_tables.cc"] +
        [INTERNAL / s for s in TRAINER_SOURCES] + ["-o", trainer_bin])

    # 3. Train
    run([trainer_bin, "--in", args.train, "--out", trained_cc] +
        args.trainer_arg)

    # 4. Build eval binary against the trained tables
    eval_bin = out_dir / "eval_detect"
    run([CXX] + CXXFLAGS + [TRAINING / "eval_detect.cc"] +
        [INTERNAL / s for s in RUNTIME_SOURCES] + [trained_cc] +
        ["-o", eval_bin])

    # 5. Evaluate
    if args.eval:
        cmd = [eval_bin, "--in", args.eval]
        if args.show_errors:
            cmd.append("--show_errors")
        run(cmd)
    else:
        print(f"no --eval given; trained tables at {trained_cc}",
              file=sys.stderr)
    print(f"\nDone. To use the trained tables in a build, compile the\n"
          f"runtime sources with {trained_cc}\n"
          f"instead of cld2_generated_quadchrome_2.cc, "
          f"cld2_generated_deltaoctachrome.cc,\n"
          f"cld2_generated_distinctoctachrome.cc and "
          f"cld_generated_score_quad_octa_2.cc", file=sys.stderr)


if __name__ == "__main__":
    main()
