---
pretty_name: Korean JEV Benchmark
language:
- ko
license: other
license_name: source-dependent
license_link: LICENSE
task_categories:
- text-classification
- question-answering
size_categories:
- 10K<n<100K
tags:
- korean
- evaluation
- multiple-choice
- natural-language-inference
- tool-selection
- decision-making
configs:
- config_name: default
  default: true
  data_files:
  - split: test
    path: data/evaluation.parquet
---

# Korean JEV Benchmark

**25,418 Korean text-only evaluation items from 9 public datasets and 22 subsets**, normalized to finite-choice decisions such as `A`, `B`, or `C`.

<!-- baseline-comparison:start -->
## Baseline results · 9 October 2026

All ten measured baseline configurations, including Vega and hosted JEV, appear in both the table and radar.

![Baseline comparison](results/20261008_baselines/model_overview_highlight.png)

Farther outward is better on every radar axis. Throughput is normalized across these ten models; accuracy and order agreement are raw percentages. HTTP p50 uses a reversed linear millisecond axis: 3,000 ms at the center, 0 ms at the rim, with 500 ms ticks. Farther outward means lower latency.

| Model | Precision / service | C* | Decisions/s ↑ | HTTP p50 ms ↓ | Korean accuracy ↑ | English accuracy ↑ | Order KO ↑ | Order EN ↑ | Order macro ↑ |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Gemma 4 31B | FP8 | 64 | 45.2 | 1343.3 | 94.40% | 57.64% | 97.68% | 55.00% | 76.34% |
| Qwen3.8 27B | FP8 | 64 | 52.9 | 1162.4 | 89.02% | 60.40% | 95.29% | 61.38% | 78.34% |
| Gemma 4 26B-A4B | FP8 | 128 | 200.4 | 614.6 | 90.37% | 45.36% | 95.63% | 41.75% | 68.69% |
| Gemma 4 12B | FP8 | 64 | 114.4 | 533.4 | 89.58% | 39.69% | 92.72% | 36.46% | 64.59% |
| Cygnet · Gemma 12B | BF16 | 64 | 49.9 | 1244.7 | 89.18% | 54.84% | 95.47% | 58.73% | 77.10% |
| Mica v0.1 4B | BF16 | 64 | 152.0 | 432.7 | 81.47% | 52.96% | 89.83% | 61.25% | 75.54% |
| K-Decision 4B | BF16 | 256 | 102.7 | 2451.4 | 85.41% | 48.94% | 93.44% | 53.12% | 73.28% |
| Qwen3.5 4B | BF16 | 64 | 185.6 | 332.5 | 78.77% | 46.24% | 77.49% | 44.75% | 61.12% |
| Decision 2.0 Vega 27B | BF16 / FP32 head · official max_speed | 1 | 11.1 | 71.3 | 92.38% | 64.59% | 96.84% | 73.78% | 85.31% |
| JEV 1.13 · hosted API | Hosted API | 64 | 88.4 | 543.7 | 88.93% | 82.50% | 96.39% | 89.28% | 92.83% |

Local models use one RTX PRO 6000 Blackwell Server 96GB GPU, with 256 warmup requests per timed pass. JEV is hosted through OpenRouter; its hardware is undisclosed. C* maximizes observed throughput across concurrency 1/8/32/64/128/256/512 on the same 2,048-item workload. HTTP p50 is measured at that C* and includes server/API queueing and transport after submission; it excludes local caller-slot wait.

Accuracy uses 25,418 Korean items and 12,032 English MMLU-Pro items (zero-shot direct decisions, without reasoning). Order agreement compares original and exact-reverse choices after semantic alignment; Order macro gives the two languages equal weight. Agreement can include consistently wrong answers.

[Measurement details](detail.md) · [Complete baseline metrics](results/20261008_baselines/summary.json).
<!-- baseline-comparison:end -->

## Earlier results

[4 October local-model and hosted JEV API results](results/README.md#original-baseline-results--4-october-2026) use queue-inclusive timing and remain archived as earlier measurements.

## Load and evaluate

```python
import json
from datasets import load_dataset

ds = load_dataset("DaehanKim/korean-jev-benchmark", split="test")
row = ds[0]
model_input = {
    "task": row["instruction"],
    "item": json.loads(row["item_json"]),
    "choices": row["choices"],
}
gold = row["answer_id"]  # Evaluation only; never include in the prompt.
```

Use the released choice order and score exact-match choice accuracy. There is **one evaluation split**, with 2–11 choices per item (supported scope: up to 26). There is no training or calibration split. Source and subset provenance are retained for breakdowns; keep answers, provenance and audit judgments out of model prompts.

## About the data

Sources: KLUE, KoBEST, Belebele, FunctionChat-Bench, APEACH, Korean Hate Speech/BEEP, SIB-200, EnterpriseOps-KO Policy, and KD-Lawset-KO. Tasks cover inference, comprehension, commonsense, classification, policy decisions, tool selection and questions about supplied statutes. Evaluation compares choice IDs; it does not use a reward model or LLM judge.

Labels were audited with GPT-6 Luna and Codex text adjudication; original gold labels were preserved and unresolved cases excluded. This is a curated derivative of public datasets, **not an independent human annotation study or a guaranteed uncontaminated test set**.

**[Dataset sources, construction, full review process, schema and limitations → detail.md](detail.md)**

Licenses remain source-dependent: CC BY-SA 4.0, CC BY 4.0 and Apache-2.0. **No CC BY-NC 4.0 data is included.** See [LICENSE](LICENSE), [source attributions](benchmark/v1/attribution), and the [citation](detail.md#attribution-and-licensing).
