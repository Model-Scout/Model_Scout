---
license: cc-by-4.0
language:
- ko
task_categories:
- question-answering
- multiple-choice
pretty_name: heritage-ko-bench
configs:
- config_name: architecture
  data_files:
  - split: test
    path: architecture/test.jsonl
  - split: dev
    path: architecture/dev.jsonl
- config_name: conservation
  data_files:
  - split: test
    path: conservation/test.jsonl
  - split: dev
    path: conservation/dev.jsonl
- config_name: excavation
  data_files:
  - split: test
    path: excavation/test.jsonl
  - split: dev
    path: excavation/dev.jsonl
- config_name: history_context
  data_files:
  - split: test
    path: history_context/test.jsonl
  - split: dev
    path: history_context/dev.jsonl
- config_name: intangible_folk
  data_files:
  - split: test
    path: intangible_folk/test.jsonl
  - split: dev
    path: intangible_folk/dev.jsonl
- config_name: natural_heritage
  data_files:
  - split: test
    path: natural_heritage/test.jsonl
  - split: dev
    path: natural_heritage/dev.jsonl
- config_name: short_answer
  data_files:
  - split: test
    path: short_answer/test.jsonl
  - split: dev
    path: short_answer/dev.jsonl
---

# heritage-ko-bench

**Korean cultural-heritage knowledge benchmark v1.3** — 6 four-choice MCQ subsets (1,317 items) + 1 short-answer subset (270 items) = **1,587 items** (test 1,552 · dev 35 for few-shot).

> ⚠️ **Evaluation only. Do not train on this data.**

## Why this benchmark

- **Decontamination by design**: items are minted exclusively from **474 documents held out before** the companion training suites were generated — document-level separation, empirically verified.
- **Triple full-pass review**: grounding verification → distractor back-verification → choices-only shortcut removal → answer-position balancing (per-subset A/B/C/D max−min ≤ 1) → three full manual-style audits → human review.
- **Measured integrity**: a 27B-class open model scores **61.2% zero-shot** (subsets 57–67%), while **choices-only accuracy is 29.8% ≈ random 25%** (shortcut delta +31.4p) — items cannot be solved without reading the question.
- MMLU-style schema: `choices` list + 0-indexed integer `answer` — natively compatible with lm-evaluation-harness.

## Subsets

| subset | test | dev | topic |
|---|--:|--:|---|
| `architecture` | 258 | 5 | traditional architecture, palaces, temples |
| `conservation` | 233 | 5 | conservation science, restoration |
| `excavation` | 240 | 5 | archaeological excavation, artifacts |
| `history_context` | 212 | 5 | historical context, documents |
| `intangible_folk` | 194 | 5 | intangible heritage, folklore |
| `natural_heritage` | 150 | 5 | natural monuments, scenic sites |
| `short_answer` | 265 | 5 | all topics, short verifiable answers |

## Data Fields

MCQ subsets:
- `question` (string) — self-contained Korean question
- `choices` (list[string], 4) — options
- `answer` (int, **0-indexed**: 0=A … 3=D)
- `category` (string) — subset name
- `source_doc_id` (string) — internal unit reference

`short_answer`: no `choices`; `answer` (string) is a short verifiable answer scored by exact match (case/punctuation-insensitive).

## Running the benchmark (lm-evaluation-harness)

The `lm_eval/` directory ships drop-in task configs (group `heritage_ko` + 7 tasks):

```bash
pip install "lm_eval[vllm]==0.4.8"   # pinned; newer versions have an --include_path regression (issue #3435)

# HF backend
lm_eval --model hf --model_args pretrained=<model>,dtype=bfloat16 \
  --tasks heritage_ko --include_path ./lm_eval \
  --num_fewshot 0 --batch_size auto --output_path results/ --log_samples

# vLLM backend (recommended)
lm_eval --model vllm --model_args pretrained=<model>,tensor_parallel_size=1,gpu_memory_utilization=0.8 \
  --tasks heritage_ko --include_path ./lm_eval --num_fewshot 0 --output_path results/

# Against a running OpenAI-compatible server (chat models)
OPENAI_API_KEY=EMPTY lm_eval --model local-chat-completions \
  --model_args model=<served-name>,base_url=http://<host>:8000/v1/chat/completions,num_concurrent=32 \
  --tasks heritage_ko --include_path ./lm_eval --apply_chat_template
```

**Scoring**: the 6 MCQ tasks use log-likelihood `multiple_choice` (`acc`/`acc_norm`) — suitable for base-model comparison. `short_answer` uses `generate_until` + `exact_match` (greedy, stop at newline). Run a single subset with e.g. `--tasks heritage_ko_architecture`.

**Reproducibility anchors** (fix these when comparing scores):

| item | value |
|---|---|
| few-shot | report 0-shot by default; for 5-shot use `fewshot_split: dev` and say so |
| aggregation | group `heritage_ko` acc is size-weighted (micro) over the 6 MCQ tasks; report `short_answer` (exact_match) separately |
| generation scoring | short_answer: greedy (temperature 0), `until: ["\n"]` |
| harness version | report the lm-eval version alongside scores |

## How it was built

Held-out source units → teacher-LLM minting of MCQ/short items (source-grounded) → grounding verification, distractor back-verification, shortcut testing, dedup, convention cleanup, answer-position rebalancing → three full-pass item surgeries + human review.

## License & Attribution

**License**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to share and adapt with attribution.

**Source material**: The benchmark items were minted from Korean public-institution
cultural-heritage reports published by the **Korea Heritage Service (국가유산청)** and the
**National Research Institute of Cultural Heritage (국립문화재연구원)**, distributed under the
**Korea Open Government License (KOGL, 공공누리)**.

> KOGL type verification is complete for the Korea Heritage Service portion and **still in
> progress for the NRICH-derived portion**. Items are derived works (newly written questions and
> answer options), not redistributions of the source documents. If you are a rights holder and
> believe any item requires correction or removal, please open a discussion on this dataset page.

**Attribution example**

```
heritage-ko-bench (PoSTMEDIA AI Lab, 2026), CC BY 4.0.
Derived from Korean public-institution cultural-heritage reports (Korea Heritage Service /
National Research Institute of Cultural Heritage), Korea Open Government License.
```

**Citation**

```bibtex
@misc{heritage_ko_bench_2026,
  title     = {heritage-ko-bench: A Korean Cultural-Heritage Knowledge Benchmark},
  author    = {{PoSTMEDIA AI Lab}},
  year      = {2026},
  publisher = {Hugging Face},
  url       = {https://huggingface.co/datasets/PoSTMEDIA/heritage-ko-bench}
}
```
