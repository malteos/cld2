SHELL := /bin/bash
VENV := .venv
PYTHON := $(VENV)/bin/python3
TOOLS := tools
WARC := data/crawl-data/CC-MAIN-2026-12/segments/1772687277079.88/warc/CC-MAIN-20260305070756-20260305100756-00076.warc.gz

.PHONY: setup benchmark

setup: $(VENV)/bin/activate

$(VENV)/bin/activate:
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip -q
	$(VENV)/bin/pip install pycld2 warcio -q

benchmark: setup
	$(PYTHON) $(TOOLS)/benchmark_cld2.py \
		--warc $(WARC) \
		--num-pages 1000 \
		--experiment pycld2-baseline \
		--results-file data/benchmark/results.csv \
		--cache-dir data/benchmark/cache/
