# autoresearch

This is an experiment to have coding agents do its own research.

## Setup

To set up a new experiment, work with the user to:

1. **Agree on a run tag**: propose a tag based on today's date (e.g. `mar5`). The branch `autoresearch/<tag>` must not already exist — this is a fresh run.
2. **Create the branch**: `git checkout -b autoresearch/<tag>` from current master.
3. **Read the in-scope files**
4. **Verify data exists**: Check that `./data/benchmark/` exists and contains baseline predictions and test-data. If not, tell the human to prepare benchmark data.
5. **Initialize results.tsv**: Create `results.tsv` with just the header row. The baseline will be recorded after the first run.
6. **Confirm and go**: Confirm setup looks good.

Once you get confirmation, kick off the experimentation.

## Experimentation

Each experiment runs on a single machine. The benchmark script runs predictions on a fixed number of HTML pages and reports metrics on prediction time (in ms) and prediction accuracy (compared to baseline). You launch it with: `make run`

**What you CAN do:**
- Modify the CLD2 source code in `./internal` and `./public` — these are only directories you edit. 

**What you CANNOT do:**
- Modify `tools`. It is read-only. It contains the fixed evaluation code.
- Install new packages or add dependencies. You can only use what's already available.
- Modify the evaluation harness or test data. 

**The goal is simple: get the lowest `total_ms` while maintaining prediction accuracy.** The input data is fixed and the output predictions are compared against the baseline. Everything in the CLD2 code base can be changed to reduce the prediction time.


**Simplicity criterion**: All else being equal, simpler is better. A small improvement that adds ugly complexity is not worth it. Conversely, removing something and getting equal or better results is a great outcome — that's a simplification win. When evaluating whether to keep a change, weigh the complexity cost against the improvement magnitude. A 0.01 ms improvement that adds 20 lines of hacky code? Probably not worth it. A 0.01 ms improvement from deleting code? Definitely keep. An improvement of ~0 but much simpler code? Keep.

**The first run**: Your very first run should always be to establish the baseline, so you will run the training script as is.

## Output format

Once the script finishes it prints a summary like this:

```
---
pages: 10000
iterations: 1
total_ms: 3548.950
mean_ms: 0.3549
median_ms: 0.2275
p95_ms: 0.9658
p99_ms: 2.1745
stddev_ms: 0.0000
accuracy: 1.0000
```

Note that the script is configured to predict the language for exactly 1000 HTML pages. You can extract the key metric from the log file:

```
grep "^total_ms:" run.log
```

## Logging results

When an experiment is done, log it to `results.tsv` (tab-separated, NOT comma-separated — commas break in descriptions).

The TSV has a header row and 5 columns:

```
commit	total_ms	accuracy	status	description
```

1. git commit hash (short, 7 chars)
2. total_ms prediction time
3. accuracy: correct predictions compared to baseline
4. status: `keep`, `discard`, or `crash`
5. short text description of what this experiment tried

Example:

```
commit	total_ms	accuracy	status	description
a1b2c3d	3548.950	1.0000	keep	baseline
b2c3d4e	3518.221	1.0000	keep	increase cache
c3d4e5f	548.153	0.5400	discard	look up table
d4e5f6g	0.000000	0.0	crash	double model width (OOM)
```

## The experiment loop

The experiment runs on a dedicated branch (e.g. `autoresearch/mar5` or `autoresearch/mar5-gpu0`).

LOOP FOREVER:

1. Look at the git state: the current branch/commit we're on
2. Tune CDL2 source code in `./internal` and `./public` with an experimental idea by directly hacking the code.
3. git commit
4. Run the experiment: `make run > run.log 2>&1` (redirect everything — do NOT use tee or let output flood your context)
5. Read out the results: `grep "^total_ms:\|^accuracy:" run.log`
6. If the grep output is empty, the run crashed. Run `tail -n 50 run.log` to read the stack trace and attempt a fix. If you can't get things to work after more than a few attempts, give up.
7. Record the results in the tsv (NOTE: do not commit the results.tsv file, leave it untracked by git)
8. If total_ms improved (lower), you "advance" the branch, keeping the git commit
9. If total_ms is equal or worse, you git reset back to where you started

The idea is that you are a completely autonomous researcher trying things out. If they work, keep. If they don't, discard. And you're advancing the branch so that you can iterate. If you feel like you're getting stuck in some way, you can rewind but you should probably do this very very sparingly (if ever).

**Timeout**: Each experiment should take ~5 minutes total (+ a few seconds for startup and eval overhead). If a run exceeds 10 minutes, kill it and treat it as a failure (discard and revert).

**Crashes**: If a run crashes (OOM, or a bug, or etc.), use your judgment: If it's something dumb and easy to fix (e.g. a typo, a missing import), fix it and re-run. If the idea itself is fundamentally broken, just skip it, log "crash" as the status in the tsv, and move on.

**NEVER STOP**: Once the experiment loop has begun (after the initial setup), do NOT pause to ask the human if you should continue. Do NOT ask "should I keep going?" or "is this a good stopping point?". The human might be asleep, or gone from a computer and expects you to continue working *indefinitely* until you are manually stopped. You are autonomous. If you run out of ideas, think harder — read papers referenced in the code, re-read the in-scope files for new angles, try combining previous near-misses, try more radical architectural changes. The loop runs until the human interrupts you, period.

As an example use case, a user might leave you running while they sleep. If each experiment takes you ~5 minutes then you can run approx 12/hour, for a total of about 100 over the duration of the average human sleep. The user then wakes up to experimental results, all completed by you while they slept!