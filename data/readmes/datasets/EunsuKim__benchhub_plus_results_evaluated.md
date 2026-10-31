---
license: mit
task_categories:
  - text-generation
language:
  - en
  - ko
tags:
  - benchmark
  - evaluation
  - llm
pretty_name: BenchHub Plus Results (Evaluated)
---

# BenchHub Plus Results (Evaluated)

LLM inference results on the BenchHub Plus benchmark, with per-sample accuracy scores.

## Folder Structure

```
├── vllm_inference_results_en/       # English benchmark results (19 models)
│   ├── {model_name}_{date}.jsonl
│   └── ...
└── vllm_inference_results_ko/       # Korean benchmark results (16 models)
    ├── {model_name}_{date}.jsonl
    └── ...
```

## Column Description

Each `.jsonl` file contains one JSON object per line with the following fields:

| Column | Type | Description |
|---|---|---|
| `index` | int | Question index |
| `original_prompt` | str | Original question text |
| `problem_type` | str | One of: `Binary`, `MCQA`, `Short-form`, `Free-form` |
| `formatted_prompt` | str | Prompt formatted with instructions and answer format |
| `model_response` | str | Raw model output |
| `reference` | str | Reference answer (if available) |
| `answer_str` | str | Ground-truth answer string |
| `options` | str | Answer options (list as string, empty `[]` for non-MCQA) |
| `model_name` | str | Model name |
| `accuracy` | int | Per-sample correctness: `1` (correct) or `0` (incorrect) |
| `time` | str | Evaluation timestamp |



## Models

### English (19 models)

| Model | Samples |
|---|---:|
| gemma-3-4b-it | 32,954 |
| gemma-3-12b-it | 32,954 |
| gemma-3-27b-it | 30,592 |
| Llama-3.3-70B-Instruct | 3,000 |
| Magistral-Sm | 32,954 |
| Meta-Llama-3-70B-Instruct | 32,954 |
| Ministral-8B-Instruct-2410 | 32,954 |
| Mistral-Small-3.2-24B-Instruct-2506 | 32,954 |
| Mixtral-8x7B-Instruct-v0.1 | 32,954 |
| Mixtral-8x22B-Instruct-v0.1 | 32,954 |
| Olmo-3-1025-7B | 32,954 |
| Olmo-3-1125-32B | 32,954 |
| Olmo-3.1-32B-Instruct | 32,954 |
| Qwen3-4B | 32,954 |
| Qwen3-8B | 32,954 |
| Qwen3-14B | 32,954 |
| Qwen3-30B-A3B-Instruct-2507 | 32,954 |
| Qwen3-32B | 32,954 |
| Qwen3-Next-80B-A3B-Instruct | 32,954 |

### Korean (16 models)

| Model | Samples |
|---|---:|
| gemma-3-4b-it | 21,543 |
| gemma-3-12b-it | 21,543 |
| Llama-3.3-70B-Instruct | 21,541 |
| Meta-Llama-3-70B-Instruct | 21,541 |
| Ministral-8B-Instruct-2410 | 21,543 |
| Mistral-Small-3.2-24B-Instruct-2506 | 21,543 |
| Mixtral-8x7B-Instruct-v0.1 | 21,391 |
| Olmo-3-1025-7B | 21,456 |
| Olmo-3-1125-32B | 21,456 |
| Olmo-3.1-32B-Instruct | 21,456 |
| Qwen3-4B | 21,541 |
| Qwen3-8B | 21,541 |
| Qwen3-14B | 21,541 |
| Qwen3-30B-A3B-Instruct-2507 | 21,541 |
| Qwen3-32B | 21,541 |
| Qwen3-Next-80B-A3B-Instruct | 21,541 |

## Problem Types

| Type | Description | Scoring Method |
|---|---|---|
| `Binary` | True/False questions | Extract `\boxed{}` → match A/true or B/false |
| `MCQA` | Multiple-choice (A/B/C/D...) | Extract `\boxed{}` → letter index or direct text match against options |
| `Short-form` | Short answer | Extract `\boxed{}` → substring match with pipe-separated alternatives in `answer_str` |
| `Free-form` | Open-ended generation | Keyword overlap heuristic (≥50% word overlap with `answer_str`) |

## Problem Type Distribution

### English (`vllm_inference_results_en`)

| Type | Count | Ratio |
|---|---:|---:|
| MCQA | 20,596 | 62.5% |
| Binary | 5,164 | 15.7% |
| Short-form | 3,829 | 11.6% |
| Free-form | 3,365 | 10.2% |
| **Total** | **32,954** | |

### Korean (`vllm_inference_results_ko`)

| Type | Count | Ratio |
|---|---:|---:|
| MCQA | ~18,424 | 85.5% |
| Short-form | 2,980 | 13.8% |
| Binary | 137 | 0.6% |
| **Total** | **~21,541** | |

