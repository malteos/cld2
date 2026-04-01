SHELL := /bin/bash
VENV := .venv
PYTHON := $(VENV)/bin/python3
CXX := g++
CXXFLAGS := -O2 -std=c++11 -Wno-narrowing

WARC := data/crawl-data/CC-MAIN-2026-12/segments/1772687277079.88/warc/CC-MAIN-20260305070756-20260305100756-00076.warc.gz
CACHE := data/benchmark/test-data/10k.jsonl
NUM_PAGES := 10000
ITERATIONS := 5
EXPERIMENT := baseline
RESULTS := data/benchmark/results.csv

# CLD2 source files
CLD2_SRC := internal
CLD2_SOURCES := \
	$(CLD2_SRC)/cldutil.cc \
	$(CLD2_SRC)/cldutil_shared.cc \
	$(CLD2_SRC)/compact_lang_det.cc \
	$(CLD2_SRC)/compact_lang_det_hint_code.cc \
	$(CLD2_SRC)/compact_lang_det_impl.cc \
	$(CLD2_SRC)/debug.cc \
	$(CLD2_SRC)/fixunicodevalue.cc \
	$(CLD2_SRC)/generated_entities.cc \
	$(CLD2_SRC)/generated_language.cc \
	$(CLD2_SRC)/generated_ulscript.cc \
	$(CLD2_SRC)/getonescriptspan.cc \
	$(CLD2_SRC)/lang_script.cc \
	$(CLD2_SRC)/offsetmap.cc \
	$(CLD2_SRC)/scoreonescriptspan.cc \
	$(CLD2_SRC)/tote.cc \
	$(CLD2_SRC)/utf8statetable.cc \
	$(CLD2_SRC)/cld_generated_cjk_uni_prop_80.cc \
	$(CLD2_SRC)/cld2_generated_cjk_compatible.cc \
	$(CLD2_SRC)/cld_generated_cjk_delta_bi_4.cc \
	$(CLD2_SRC)/generated_distinct_bi_0.cc \
	$(CLD2_SRC)/cld2_generated_quadchrome_2.cc \
	$(CLD2_SRC)/cld2_generated_deltaoctachrome.cc \
	$(CLD2_SRC)/cld2_generated_distinctoctachrome.cc \
	$(CLD2_SRC)/cld_generated_score_quad_octa_2.cc

.PHONY: setup extract benchmark run evaluate clean

# Python venv (for WARC extraction only)
setup: $(VENV)/bin/activate

$(VENV)/bin/activate:
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip -q
	$(VENV)/bin/pip install warcio -q

# Extract HTML pages from WARC into single JSONL cache
extract: setup
	$(PYTHON) tools/extract_warc.py \
		--warc $(WARC) \
		--num-pages $(NUM_PAGES) \
		--output $(CACHE)

# Compile C++ benchmark binary
tools/benchmark_bin: tools/benchmark.cc $(CLD2_SOURCES)
	$(CXX) $(CXXFLAGS) -I$(CLD2_SRC) -Ipublic \
		tools/benchmark.cc $(CLD2_SOURCES) \
		-o tools/benchmark_bin

# Run benchmark (extract if needed, compile, then run)
benchmark: extract tools/benchmark_bin
	./tools/benchmark_bin \
		--experiment $(EXPERIMENT) \
		--iterations $(ITERATIONS) \
		--results-file $(RESULTS)

# Recompile and run benchmark (no extraction, no extra args)
run: clean tools/benchmark_bin
	./tools/benchmark_bin

# Compile CLD2 line-level detection CLI
tools/cld2_detect: tools/cld2_detect.cc $(CLD2_SOURCES)
	$(CXX) $(CXXFLAGS) -I$(CLD2_SRC) -Ipublic \
		tools/cld2_detect.cc $(CLD2_SOURCES) \
		-o tools/cld2_detect

# Run CommonLID evaluation (recompiles cld2_detect first)
evaluate: tools/cld2_detect
	$(PYTHON) tools/evaluate_lid.py

clean:
	rm -f tools/benchmark_bin tools/cld2_detect
