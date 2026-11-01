---
language:
- en
- ja
- ko
library_name: llama.cpp
tags:
- gguf
- sentence-transformers
- sentence-similarity
- feature-extraction
- embedding
- bge-m3
- quantized
base_model: KGESH/nsfw-bge-m3-v5
---

# NSFW BGE-M3 v5 — GGUF quantisations

This repository contains derived GGUF distribution artefacts for [KGESH/nsfw-bge-m3-v5](https://huggingface.co/KGESH/nsfw-bge-m3-v5), a 1,024-dimensional BGE-M3 fine-tune. These files are quantisations and conversions of the original model; they are not independently trained models.

## Relationship to the original model

The source model is [KGESH/nsfw-bge-m3-v5](https://huggingface.co/KGESH/nsfw-bge-m3-v5), evaluated at revision `eaaf46c3b340d880d298ba7a03158fbe9b6e780b`. No additional training was performed during conversion or quantisation. The F16 file is an unquantised GGUF conversion. Q8_0, Q6_K and Q5_K_M are lower-bit GGUF quantisations derived from that conversion. Please cite and follow the original model's licence, intended-use statement and limitations.

## Files

| File | Size | SHA-256 |
|---|---:|---|
| `nsfw-bge-m3-v5-f16.gguf` | 1,157,676,992 bytes | `d7579f0c22023eba0c4280f9ba52310710bba8677aaf868c7a625a0a7be50640` |
| `nsfw-bge-m3-v5-q8_0.gguf` | 634,559,552 bytes | `ccc1d8dcfbf92330714acc73a86375c6a9e25d6d5effbe398fb9bda4496d766e` |
| `nsfw-bge-m3-v5-q6_k.gguf` | 499,420,896 bytes | `c67cc93fae5eb0e92e3ff9cc88666fbcd59c4b79a150a13431675f3aa0d60dfb` |
| `nsfw-bge-m3-v5-q5_k_m.gguf` | 467,668,704 bytes | `23d90c5c2311a4b95145f713e0b6260e273f9220a4db99df4c51534e143b4ce0` |

All files expose 1,024-dimensional embeddings in the tested `llama-server` configuration.

## Use with llama.cpp

```bash
llama-server \
  --model nsfw-bge-m3-v5-q6_k.gguf \
  --host 127.0.0.1 \
  --port 8084 \
  --embedding \
  --embd-normalize 2
```

Send embedding requests to `/v1/embeddings`. The benchmark used the raw BGE-M3 serializer and cosine-compatible normalised embeddings; it did not use a Qwen instruction template.

## Evaluation protocol

The four candidates were evaluated as a paired, within-query multi-group experiment: the same 90-query retrieval fixture was run against F16, Q8_0, Q6_K and Q5_K_M. Each candidate was loaded in an isolated `llama-server` process, with an isolated SQLite store and no production retrieval path. The retrieval configuration was top-k 8, 30 lexical candidates, 30 dense candidates, and reciprocal-rank fusion `k=60`.

The supplied error-bar figure is shown below and is also available at [`figures/quantisation_metrics_with_95ci.png`](figures/quantisation_metrics_with_95ci.png).

![Quantisation metrics with 95% confidence intervals](figures/quantisation_metrics_with_95ci.png)

Error bars represent 95% confidence intervals: Wilson intervals for Recall@8 and paired bootstrap intervals for MRR@8 and end-to-end latency. The raw paired query results, summary statistics, group breakdowns, omnibus tests and post-hoc tests are provided alongside the figure.

## Overall summary

| Candidate | Recall@8 mean | Recall variance | Recall SD | Recall 95% CI | MRR@8 mean | MRR variance | MRR SD | MRR 95% CI | Mean latency (ms) | Latency variance | Latency SD | Median (ms) | p95 (ms) |
|---|---:|---:|---:|---|---:|---:|---:|---|---:|---:|---:|---:|---:|
| F16 | 0.6667 | 0.2247 | 0.4740 | [0.5642, 0.7555] | 0.6036 | 0.2165 | 0.4652 | [0.5078, 0.7000] | 126.23 | 472.43 | 21.74 | 124.36 | 156.18 |
| Q8_0 | 0.6667 | 0.2247 | 0.4740 | [0.5642, 0.7555] | 0.6090 | 0.2182 | 0.4671 | [0.5127, 0.7053] | 104.11 | 153.82 | 12.40 | 102.25 | 124.05 |
| Q6_K | 0.6667 | 0.2247 | 0.4740 | [0.5642, 0.7555] | 0.6030 | 0.2170 | 0.4658 | [0.5071, 0.6990] | 144.35 | 588.89 | 24.27 | 144.59 | 176.10 |
| Q5_K_M | 0.6667 | 0.2247 | 0.4740 | [0.5642, 0.7555] | 0.6038 | 0.2163 | 0.4650 | [0.5078, 0.6989] | 94.67 | 126.99 | 11.27 | 91.34 | 114.61 |

The latency values above are end-to-end benchmark measurements and can vary with hardware, process state and server configuration. The exact machine-readable values are in `quantisation_summary.csv`.

## Paired multi-group statistical tests

The primary analysis used all four candidates together, rather than treating the comparison as a sequence of independent two-group tests. The significance threshold was alpha = 0.05.

| Metric | Omnibus test | Statistic | df | p-value | Effect size |
|---|---|---:|---:|---:|---|
| Recall@8 | Cochran's Q | 0.0000 | 3 | 1.000000 | Q/(n(k−1)) = 0.0000 |
| MRR@8 | Friedman chi-square | 4.0435 | 3 | 0.256807 | Kendall's W = 0.0150 |
| End-to-end latency | Friedman chi-square | 178.5467 | 3 | 1.8168e-38 | Kendall's W = 0.6613 |

The latency omnibus result indicates a statistically detectable difference in measured latency across candidates. It does not establish that one candidate is universally best, nor does it remove hardware and process-state confounding.

All six post-hoc candidate pairs were tested with paired methods and Holm correction within each metric. The complete results, including raw p-values, Holm-adjusted p-values and effect sizes, are in `posthoc_tests.csv`. Adjusted p-values for Recall@8 were 1.000000 for every pair. For MRR@8, no Holm-adjusted comparison was significant: the adjusted p-values were 1.000000, 1.000000, 1.000000, 0.652857, 1.000000 and 0.898562 in the file's pair order. For latency, all six Holm-adjusted comparisons were significant; the adjusted p-values ranged from `1.46e-15` to `5.31e-12`.

## Interpretation and limitations

On this 90-query fixture, all four candidates achieved the same Recall@8 (0.6667), and the omnibus MRR test was not significant. Q6_K was retained as a practical candidate for its size–quality trade-off, not because it was statistically superior to every other candidate. Q5_K_M had the lowest measured mean latency and smallest file, while Q6_K had the largest measured latency of the four in this run; these operational measurements should be repeated on the intended deployment hardware before selection.

The negative-query fixture returned a result for every negative query: `negative_false_recall_rate = 1.0` and `negative_no_result_precision = 0.0`. This is a known evaluation limitation and must not be interpreted as reliable rejection, abstention or safety behaviour. The model is not a safety classifier, and users must apply appropriate access controls, content policies and human review.

The source data and training claims belong to the original model card. This derived repository does not make a new claim about the legality, completeness or representativeness of any source dataset. Review the original model's licence and intended-use restrictions before redistribution or deployment.

## Reproduction

From the project workspace:

```bash
uv run python scripts/collect_quantization_evaluation.py
uv run --with 'numpy~=1.26.4' --with 'scipy>=1.11,<2' --with 'matplotlib>=3.8,<4' \
  python scripts/analyse_quantisation_results.py \
  --input C:/Users/downl/AppData/Local/Temp/nsfw-bge-m3-v5-quantisation-query-results.json \
  --output artifacts/nsfw-bge-m3-v5-quantisation
```

The analysis is paired and deterministic apart from server timing and the explicitly seeded bootstrap (`20,000` resamples; seed `20260810`). The benchmark code revision and source-model revision are recorded in `analysis_metadata.json`.

## Files in this repository

`README.md` is this model card. `figures/quantisation_metrics_with_95ci.png` is the error-bar figure. `quantisation_summary.csv` contains overall summary statistics; `group_summary.csv` contains per-query-group summaries; `omnibus_tests.csv` contains the four-group tests; `posthoc_tests.csv` contains all paired post-hoc tests with Holm correction; `raw_query_results.json` contains the paired observations; and `analysis_metadata.json` records provenance and analysis settings.
