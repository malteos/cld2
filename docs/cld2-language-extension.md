Extending CLD2's language coverage to all 109 CommonLID benchmark languages.

- CommonLID evaluation data: https://huggingface.co/datasets/commoncrawl/CommonLID
- GlotLID training data: https://huggingface.co/datasets/cis-lmu/glotlid-corpus

Task: Extend CLD2 to all languages covered by the CommonLID benchmark. Research missing languages (characteristics, grammar, vocabulary) and create MD doc with key findings for each new language in the docs folder. Modify all the CLD2 source code, reverse engineer its training algorithm, extend data tables. Generate new training data based on the language md docs or use training data from GlotLID. Make sure to use only training data from GlotLID for training and CommonLID only for evaluation. Do not forget to recompile CLD2 before doing the evaluation.

Run experiments as described in `program.md` but with `macro_f1` and `micro_f1` as evaluation metric. Results should be tracked in `run_lid.log` and `results_lid.tsv`. Also list failed experiments (discarded status).

Goal: High macro/micro F1 across all samples. At least all language with F1 > 0.20

Tools:

- cld2_detect.cc: Detect languages from stdin
- evaluate_lid.py: Evaluate against CommonLID benchmark (metric output: samples, languages, coverage, macro_f1, micro_f1)
- download_data.py Download training and evaluation data

Run experiments as infinite loop. Keep going until I stop you.