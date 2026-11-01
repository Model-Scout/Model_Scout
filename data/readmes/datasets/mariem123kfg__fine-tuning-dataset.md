---
language:
- en
- ko
tags:
- json-extraction
- json-correction
- fine-tuning
- carebench
- sob
---

# SOB Fine-Tuning Dataset (Extraction + Correction)

Internal fine-tuning corpus for JSON extraction and JSON repair tasks, built to fine-tune our best-performing model from the CAREBench benchmark on both scenarios it's evaluated on.

## What this is

**100,405 rows** split into two paired tasks:

| Split | Rows | Task | What the model sees | What it should produce |
|-------|-----:|------|---------------------|------------------------|
| `extraction` | 50,204 | JSON extraction | `context`, `question`, `json_schema` | A valid JSON object matching the schema (`validated_output`) |
| `correction` | 50,201 | JSON repair | Same inputs, plus a corrupted JSON (`errored_json`) | The corrected JSON (`validated_output`), same target as extraction |

`train` (**100,405 rows**) is the two splits combined, for training a single model on both tasks together.

```python
from datasets import load_dataset

REPO = "mariem123kfg/fine-tuning-dataset"

extract = load_dataset(REPO, split="extraction")
correct = load_dataset(REPO, split="correction")
all_rows = load_dataset(REPO, split="train")
```

## How it was built

**1. Merge.** 12 upstream sources (hotpotqa, scrapegraph web-scrape extraction, STAGE-Eval, ToolACE, Hermes function-calling, DeepJSONEval, paraloq, and others) were mapped onto a shared schema (`context` / `question` / `json_schema` / `ground_truth`) and combined.

**2. Quality filter.** Every row was validated with a Draft-7 JSON Schema checker against its own `ground_truth`. Rows that failed (schema-noncompliant labels, e.g. missing required fields, wrong types) were dropped rather than kept as "correct" training examples, since training on invalid ground truth would teach the model the wrong thing about what compliant output looks like. This removed sources/rows with low compliance rates outright (an entire low-quality source at ~24–29% compliance, a tool-calling variant at ~49%) and trimmed the largest remaining source down to its schema-valid subset only.

**3. Deduplication.** The two largest sources (both derived from the same underlying scrapegraph web-scrape pipeline) had substantial internal near-duplication, over 20% within each individually. These were deduplicated in a single combined MinHash/LSH pass (similarity threshold 0.85, first-seen-wins) so the corpus doesn't overweight one generation pipeline's idiosyncrasies.

**4. Volume additions.** Two datasets originally built as held-out evaluation sets (`paraloq-json-extraction-eval`, STAGE-eval) were deliberately repurposed into training data after review, since they were schema-compliant and added useful volume/diversity. **Important:** those standalone eval repos should no longer be treated as clean/unseen benchmarks for any model trained on this corpus.

**5. Error injection (correction split only).** For the correction task, a copy of each clean, schema-valid `validated_output` was algorithmically corrupted (`errored_json`) to create repair training pairs. Errors are injected with controlled type, count, and difficulty per row:

- **Error types:** e.g. `string_truncation`, `number_as_string`, `case_corruption`, `type_break`, `array_duplicate`, `drop_required_field`, `sibling_value_swap`, `numeric_off_by_one`, `word_typo`. Multiple error types can be combined in a single row (`error_type` records them concatenated, `error_types` as a list).
- **Error count:** 0–3 injected errors per row, tracked in `error_count`.
- **Error difficulty:** each individual injected error is tagged easy/medium/hard (`error_difficulty` / `error_difficulties`), letting training and eval slice by how subtle the corruption is.
- **Error location:** the exact JSON path(s) affected are recorded (`error_location` / `error_locations`), along with a human-readable description of what changed (`error_description` / `error_descriptions`) and a structured combined record (`errors_json`).
- **`error_source`** marks all injected errors as `algorithmic` (rule-based corruption, not model-generated), for reproducibility.

Extraction-split rows carry `error_count == 0` by construction (`errored_json == validated_output`, i.e. no corruption applied), so the same schema works across both splits without special-casing.

## Columns

| Column | Extraction | Correction |
|--------|:----------:|:----------:|
| `record_id` | ✓ | ✓ |
| `context`, `question`, `json_schema` | ✓ | ✓ |
| `validated_output` | ✓ (target) | ✓ (repair target) |
| `errored_json` | ✓ (= target, no corruption) | ✓ (corrupted input) |
| `error_count`, `error_difficulty`, `error_type(s)` | ✓ (zero/none) | ✓ |
| `error_location(s)`, `error_description(s)`, `errors_json` | optional | ✓ |
| `source_dataset`, `schema_complexity`, `question_type` | ✓ | ✓ |

## Source mix

| Rows | `source_dataset` |
|-----:|------------------|
| 35,025 | `scrapegraphai_full` |
| 19,257 | `boradorish/STAGE-eval` |
| 16,597 | `hotpotqa` |
| 13,303 | `ChristianAzinn/json-training` |
| 10,630 | `scrapegraphai_finetuning_subset` |
| 2,052 | `GTSAIInfraLabSOTAS/DeepJSONEval` |
| 1,340 | `hermes-function-calling-v1/json_mode_agentic` |
| 1,237 | `hermes-function-calling-v1/json_mode_singleturn` |
| 484 | `paraloq` |
| 472 | `suneeldk/text-json` |
| 8 | `Team-ACE/ToolACE` |

## Eval firewall

| Holdout | Overlap with this dataset |
|---------|---------------------------|
| `interfaze-ai/sob` test split (~5k rows) | **0** shared `record_id`s |
| `MoetezF/SOB-with-errors-injection` test split (~5k rows) | **0** shared `record_id`s |

Both held-out sets were checked for `record_id` overlap before publishing and confirmed clean. Do **not** merge either eval set into this training corpus — doing so would invalidate any CAREBench numbers reported against them going forward.

## Regenerate / republish

```bash
python publish_ft_finetuning_dataset.py --target-repo mariem123kfg/fine-tuning-dataset
```
