---
license: apache-2.0
language:
- ko
tags:
- korean
- rlhf
- sft
- preprocessing
task_categories:
- text-generation
pretty_name: Korean RLHF Content Filtered
size_categories:
- 100K<n<1M
---

# Korean RLHF Content Filtered

## Dataset Summary

This dataset is a cleaned, content-only derivative of:
- Source dataset: `jojo0217/korean_rlhf_dataset`
- Source URL: https://huggingface.co/datasets/jojo0217/korean_rlhf_dataset

Each row has a single `content` field suitable for LM pretraining/SFT-style text modeling.

## Construction

### Content construction rule

For each source row:
- If `input` is empty: `content = instruction + "\n" + output`
- If `input` is not empty: `content = instruction + "\n" + input + "\n" + output`

### Filtering methods

The following filters were applied in this order:
1. Remove rows missing required core fields (`instruction` or `output`).
2. Normalize text and remove invisible control/zero-width characters.
3. Remove rows shorter than 20 characters.
4. Remove broken rows (`\x00`, replacement char `�`, `<unk>`, abnormal control-character ratio).
5. Tokenize with `Qwen/Qwen3.5-4B-Base` and keep rows with token length in `[1, 4096]`.
6. Remove exact duplicates by SHA1 hash of `content`.

## Final Statistics

From `filtering_stats.json`:
- Raw rows: 107,172
- Kept rows: 107,008
- Dropped missing core: 52
- Dropped too short: 60
- Dropped broken: 3
- Dropped duplicates: 41
- Dropped token too long (>4096): 8
- Dropped zero-token rows: 0
- Rows with NUL (`\x00`) in final data: 0
- Rows with invisible chars in final data: 0

## Data Fields

- `content` (`string`): filtered text content
- `source_dataset` (`string`): source dataset id
- `source_split` (`string`): source split name
- `row_index` (`int`): original row index in source split
- `token_count` (`int`): token count with `Qwen/Qwen3.5-4B-Base`

## Files

- `train.jsonl`: main filtered dataset
- `filtering_stats.json`: preprocessing/filtering summary

## Intended Use

- Korean language modeling pretraining
- Continued pretraining / domain adaptation
- SFT-style text-only preparation

## Caveats

This is a transformed derivative dataset. Please also review and comply with the source dataset card and upstream source licenses/terms referenced by the original dataset author.
