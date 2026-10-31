---
license: other
license_name: mixed-apache2-and-aihub-terms
license_link: https://github.com/sylvanus4/kodialectbench/blob/main/LICENSE
language:
- ko
tags:
- korean
- dialect
- benchmark
- evaluation
- gyeongsang
- jeolla
- jeju
- chungcheong
- gangwon
pretty_name: KoDialectBench
size_categories:
- 1K<n<10K
configs:
- config_name: default
  data_files: eval/bench/kodialectbench-v0/items.jsonl
---

> **Code repository**: https://github.com/sylvanus4/kodialectbench
> **English card**: [`README.en.md`](eval/bench/kodialectbench-v0/README.en.md)
>
> ⛔ This repository contains **no AI Hub text, no marker lexicon and no original item identifiers.**
> `items.jsonl` holds only one-way hashes, region labels and counts. They are computed from AI Hub
> data and follow the AI Hub terms of use. You regenerate the text and the lexicon yourself from
> your own AI Hub account's data.

# KoDialectBench v0.1.0

A benchmark that measures Korean **regional dialects (사투리/방언)**. It covers five regions —
Gangwon, Gyeongsang, Jeolla, Chungcheong, and Jeju — with 200 items per region, 1,000 items
in total.

No Korean dialect benchmark existed in the world. So this project, which set out to build a
dialect model, built the ruler before the model. Even if training fails, the ruler survives.

## Getting started

The code and the item list live in `eval/bench/kodialectbench-v0/` of the `satoori-ko`
repository. All commands below are run **from the repository root (`satoori-ko/`)**.

The only requirement is Python 3.10 or later (verified on 3.12.8). **No external packages are
used at all** — the scorer, the item builder, and the dialectness scorer run entirely on the
standard library. There is nothing to install.

To download AI Hub data you need an account and an API key. After signing up on AI Hub,
**apply for usage of datasets 118·119·120·121·122 and 71517·71558 and get approved.** After
approval, issue an API key from your account page and set it as an environment variable.

```bash
export AIHUB_APIKEY=your-issued-key
```

## Why item text is not included

This repository contains **no item text.** It holds only item numbers, a passage digest, and
scoring code. The source is AI Hub data, and AI Hub's usage policy prohibits handing the data
to unapproved third parties. So the text was removed, and the repository is built so that you
download the original with your own account and fill in the same items yourself.

In other words, everyone ends up with **the exact same 1,000 items** from data pulled through
their own account. Item selection is fixed by a random seed and document-level splitting, and
the passage digest lets you confirm you and someone else landed on the same items.

```bash
# 1) Download the AI Hub 118·119·120·121·122 (+ 71517·71558) labeled data to your own account
python corpus/aihub_fetch.py --elder      # ⛔ without --elder, 71517·71558 are not downloaded
                                          #    and parse_elder below dies immediately
python corpus/aihub_parse.py
python corpus/aihub_parse_elder.py --holdout-frac 0.2

# 2) Regenerate the marker lexicon (⛔ this lexicon is also not distributed — see below)
python kit/mine_markers.py --min-n 10 --min-purity 0.70 --min-spec 0.30 --top 20000

# 3) Fill in the same items on your own machine
python eval/build_bench.py --per-region 200 --materialize
```

To check whether your regenerated marker lexicon matches ours, compare the sha256 in
`eval/bench/MARKERS.sha256.json`. Mining is deterministic, so the same input produces
byte-identical output.

## Three tasks

**T1 Comprehension** asks the model to translate a dialect sentence into standard Korean. It
directly checks whether the meaning was understood, measured by chrF and exact-match rate.

**T2 Region identification** asks the model to pick which of the five regions a sentence's
dialect belongs to.

**T3 Generation** asks the model to convert a standard-Korean sentence into a specific
region's dialect. It jointly reports dialectness, whether the region is correct
(region_match), the product of the two (ADI2), and whether the meaning survived.
⛔ Do not combine dialectness and meaning preservation into a single score. If the output
looks like dialect but the meaning has collapsed, that is a failure, not a success.

## Running the evaluation

The scorer calls your model through an **OpenAI-compatible endpoint.** Rather than you
producing an output file and handing it over, you just give it a server address and model
name, and it sends the items and scores them itself.

```bash
python eval/run_bench.py \
    --base http://127.0.0.1:8000 \   # replace with your serving server's address
    --model my-model-name \
    --per-region 200 \
    --label my-experiment-name \
    --out results.json
```

The result JSON carries both the per-task total score and the per-region scores. If you want
to compare against someone else's numbers, don't report the score alone — also state **what
serving configuration you measured it under.** You need the engine and precision (bf16/fp8,
etc.), the context length, and how many runs you averaged and how you combined them. Our
baseline is the median of three runs on the same engine, because even with `temperature=0`
set, the same value does not come out every time.

## Evidence that this ruler actually measures something

Before using the ruler, we first checked whether it has any graduations at all. We fed in
dialect sentences and standard-Korean sentences of the same meaning side by side and checked
whether it could separate the two. 400 pairs per region.

| Region | Dialect·standard separation | Region margin |
|---|---|---|
| Jeolla | 96.5% | +0.622 |
| Gangwon | 92.5% | +0.705 |
| Chungcheong | 90.5% | +0.560 |
| Gyeongsang | 86.8% | +0.587 |
| Jeju | 86.5% | +0.784 |

You can reproduce this table yourself.

```bash
python eval/marker_calibration.py -n 400
```

All five regions passed, and the region margin is positive across the board. Markers were
mined from the training-split conversations, and scoring used only the test-split
conversations, so the same speaker never appears on both sides.

There is one thing we learned here. At first Gyeongsang and Jeolla did not separate well, and
we explained it away as a linguistic fact — "Gyeongsang's dialect difference lives in
intonation, so less of it survives in text." **We were wrong.** It was simply an insufficient
sample; once we merged in the middle-aged/elderly data, Jeolla rose from 76.8% to 96.5%. When
a metric fails to separate two things, check the sample size before you say "they were just
similar to begin with."

## Baseline (Qwen3.8-27B)

We measured three times on the same engine, changing only the weights, and reported the
median.

| Metric | Base model | Synthetic-data training | Real-data training |
|---|---|---|---|
| T1 chrF | 50.7 | 70.1 | 80.1 |
| T1 exact-match % | 2.2 | 10.6 | 24.7 |
| T2 region-ID % | 24.7 | 63.1 | 79.4 |
| T3 dialectness | 0.034 | 0.102 | 0.141 |
| (reference) real-speaker dialectness | 0.232 | 0.232 | 0.232 |
| T3 ADI2 | 0.012 | 0.065 | 0.107 |

The base model can barely produce dialect at all. Real speakers' sentences for the same items
score 0.232 dialectness, while the base model scores 0.034 — reproducing roughly 1.4 out of
every 10 people's worth. Even giving three examples in the prompt was inconsistent across
regions, and Gangwon actually dropped. **Dialect is not something instructions can produce —
it is something training produces.**

## What not to trust

Items are transcribed text. Intonation and sound are not captured here. Sound accounts for a
large share of what makes a dialect a dialect, but this ruler measures only what survives in
writing.

The amount of source data is uneven across regions. Jeolla in particular has especially little
main-corpus data, so it leans heavily on the middle-aged/elderly data.

The dialectness score depends on the marker lexicon, and that lexicon was mined from AI Hub
labels. A word that is dialect but absent from the lexicon is scored as 0. So read this score
as a lower bound, not an upper bound.

## Provenance

The original source of the items is AI Hub's "Korean Dialect Speech" data
(118·119·120·121·122) and "Middle-aged/Elderly Korean Dialect Speech" data (71517·71558). This
repository contains no item text.

**The marker lexicon used for scoring (`kit/markers/*.json`) is also not distributed,** since
it too is a derivative mined from AI Hub labels. Exactly as with the item text, you build it
yourself by running `kit/mine_markers.py` on your own account's data. Mining is deterministic,
so the same input yields the same lexicon, which you can verify against the hash in
`eval/bench/MARKERS.sha256.json`.

⇒ As a result **this repository contains no AI Hub text and no original item identifiers** —
only code, plus one-way hashes and counts (`items.jsonl`) for verifying the items you regenerate.
Those hashes and counts are computed from AI Hub data, so they follow the AI Hub terms of use (see License).

## License

**The code is Apache-2.0** (`LICENSE`). The authoritative list of what counts as code is
`eval/bench/PUBLISH.json`.

**The item numbers and digests (`items.jsonl`) are AI Hub derivatives,** so they follow **AI
Hub's usage policy,** not Apache-2.0. The marker lexicon is not distributed at all (you
regenerate it). Model weights trained on AI Hub data are not released either.

## Citation

Please cite the benchmark version (`KoDialectBench v0.1.0`) together with **the serving
configuration you measured under.** Without the engine, precision, context length, and the
number of repeats and how they were combined, that number cannot be compared against anyone
else's.

## Contact / reporting

Please file item errors, scoring anomalies, or reproduction failures as issues in this
repository.

## Paper

Metric-Construction Coupling Inflates Measured Synthetic Dialect Recovery — [arXiv:2610.00164](https://arxiv.org/abs/2610.00164)

This benchmark is introduced in that paper, together with the held-out-marker protocol it uses to separate real recovery from metric-construction coupling. If you score a synthetic dialect pipeline on this set, withhold the marker types the builder relies on and report both numbers — a single coupled number overstated recovery by an order of magnitude in our own runs (91.8% → 8.1% on dialectness). Arms measured in the paper: [real data](https://huggingface.co/ThakiCloud/Qwen3.8-27B-Satoori-KO) · [synthetic](https://huggingface.co/ThakiCloud/Qwen3.8-27B-Satoori-KO-Synth).
