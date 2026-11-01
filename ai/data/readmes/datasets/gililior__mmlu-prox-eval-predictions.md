---
license: cc-by-4.0
language:
- af
- ar
- bn
- cs
- de
- en
- es
- fr
- hi
- hu
- id
- it
- ja
- ko
- mr
- ne
- pt
- ru
- sr
- sw
- te
- th
- uk
- ur
- vi
- wo
- yo
- zh
- zu
task_categories:
- question-answering
- multiple-choice
tags:
- mmlu-prox
- evaluation
- lm-eval-harness
- multilingual
- model-predictions
- irt
pretty_name: MMLU-ProX Multilingual Model Predictions
size_categories:
- 1M<n<10M
configs:
- config_name: default
  data_files:
  - split: predictions
    path: "*/*/samples_*.jsonl"
---

# MMLU-ProX Multilingual Model Predictions

Raw per-sample model predictions on **[MMLU-ProX](https://huggingface.co/datasets/li-lab/MMLU-ProX)**
across **29 languages** and **25 open-weight LLMs**, produced with
[lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness).

This dataset releases the **full prediction logs** (not just aggregate scores) so that
item-level responses can be re-analysed — e.g. for Item Response Theory (IRT) modelling
of multilingual benchmarks, error analysis, or per-item difficulty estimation.

## Repository structure

```
mmlu_prox_<lang>/
└── <org>__<model>/
    ├── samples_mmlu_prox_<lang>_<subject>_<timestamp>.jsonl   # per-item predictions
    └── results_<timestamp>.json                               # aggregate scores + run config
```

- **Languages (29):** af, ar, bn, cs, de, en, es, fr, hi, hu, id, it, ja, ko, mr, ne, pt, ru, sr, sw, te, th, uk, ur, vi, wo, yo, zh, zu
- **Subjects (14):** biology, business, chemistry, computer_science, economics, engineering, health, history, law, math, other, philosophy, physics, psychology
- **Models (25):** CohereLabs aya-expanse (8b/32b) & tiny-aya-global; Qwen3.5 (2B/4B/9B/27B + 35B-A3B/122B-A10B MoE); allenai Olmo-3-7B & Olmo-3.1-32B (Instruct/Think); google gemma-3 (4b/12b/27b)-it; meta-llama Llama-3.1-8B / 3.2-3B / 3.3-70B-Instruct; microsoft Phi-4-mini (instruct/reasoning) & Phi-4-reasoning(-plus); openai gpt-oss (20b/120b)

## File schemas

### `samples_*.jsonl` — one JSON object per evaluated item

| Field | Description |
|-------|-------------|
| `doc_id` | Index of the item within the subject split |
| `doc` | The source MMLU-ProX item: `question_id`, `question`, `option_0`…`option_9`, `answer`, `answer_index`, `cot_content`, `category`, `src`, `question_id_src` |
| `target` | Gold answer letter |
| `arguments` | Prompt(s) sent to the model |
| `resps` / `filtered_resps` | Raw and post-filter model responses |
| `filter` | Name of the answer-extraction filter applied |
| `metrics` | Metric names scored for this item (`exact_match`) |
| `exact_match` | 1.0 if correct, 0.0 otherwise |
| `doc_hash` / `prompt_hash` / `target_hash` | Reproducibility hashes |

### `results_*.json` — per (language, model, run)

Standard lm-eval-harness results: aggregate `results`/`groups` scores, full `config`
(model args, gen kwargs, seeds), `n-shot`, `n-samples`, library/transformers versions,
chat-template hashes, and total evaluation time.

## Usage

Load all predictions via the default config:

```python
from datasets import load_dataset

ds = load_dataset("gililior/mmlu-prox-eval-predictions", split="predictions")
```

Or pull specific files directly:

```python
from huggingface_hub import hf_hub_download

path = hf_hub_download(
    repo_id="gililior/mmlu-prox-eval-predictions",
    repo_type="dataset",
    filename="mmlu_prox_en/google__gemma-3-27b-it/results_<timestamp>.json",
)
```

## Generation details

- Backend: `vllm` (bfloat16), `max_model_len` 8192, `max_gen_toks` 512
- Seeds: `random_seed=0`, `numpy_seed=1234`, `torch_seed=1234`, `fewshot_seed=1234`
- Scored with `exact_match` after answer-extraction filtering

Exact decoding/prompt settings per run are recorded in each `results_*.json` `config` block.

## License

Released under **CC-BY-4.0**. The underlying MMLU-ProX questions retain their original
license — see the [MMLU-ProX dataset](https://huggingface.co/datasets/li-lab/MMLU-ProX).

## Citation

If you use these predictions, please cite this repository and the MMLU-ProX benchmark.
(Citation for the accompanying IRT-for-multilingual-benchmarks work to be added.)
