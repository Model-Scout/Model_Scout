---
license: other
license_name: mixed-open-licenses
language:
  - ko
task_categories:
  - text-generation
tags:
  - sft
  - instruction-tuning
  - chatml
  - korean
size_categories:
  - 1M<n<10M
pretty_name: Keural SFT ChatML (Korean)
---

# Keural SFT ChatML — Korean

Korean supervised fine-tuning (SFT) dataset in fully-rendered **ChatML** format, produced by the
Keural SFT data pipeline (collect → structure → clean → quality-filter → safety-filter → dedup →
format → tokenize → package → audit). Intended for instruction-tuning of the Keural model family.

- **Language**: Korean (ko)
- **Total samples**: 2,018,250 (~499M tokens; see `manifest.json` for per-shard counts and sha256 checksums)
- **Format**: one JSON object per line (JSONL), sharded per source dataset
- **Version**: v3 — same source composition as v2, fully reprocessed with a fixed cleaning stage.
  **v1/v2 had corrupted code indentation** (a whitespace-collapse rule flattened all code-block
  indents to one space, breaking Python syntax); v3 preserves indentation. **Do not train on
  v1/v2 if code ability matters.** Also includes the full OpenOrca-gugugo-ko (~80% of rows);
  use `source_name` to reweight if a smaller machine-translation share is desired.

## Row schema

```json
{
  "text": "<|im_start|>user\n...<|im_end|>\n<|im_start|>assistant\n...<|im_end|>",
  "n_tokens": 342,
  "source_name": "kocommercial",
  "license": "mit"
}
```

| Field | Description |
|---|---|
| `text` | Fully-rendered ChatML conversation (may include a `system` turn and multiple user/assistant turns; always ends on an assistant turn) |
| `n_tokens` | Token count measured with the Keural SentencePiece tokenizer (max 8,192; longer samples truncated) |
| `source_name` | Which source dataset this row came from (see table below) — filter on this for selective training |
| `license` | License of the source dataset, recorded per row |

### ChatML format

```
<|im_start|>system
{system_message}
<|im_end|>
<|im_start|>user
{user_message}
<|im_end|>
<|im_start|>assistant
{response}
<|im_end|>
```

If there is no system turn, `text` starts directly with the user turn.

> ⚠️ **Tokenizer requirement**: `<|im_start|>` and `<|im_end|>` must be registered as special
> tokens in your tokenizer before training/serving, otherwise they get split into sub-tokens and
> the chat format breaks. For HF tokenizers:
> `tokenizer.add_special_tokens({"additional_special_tokens": ["<|im_start|>", "<|im_end|>"]})`
> followed by `model.resize_token_embeddings(len(tokenizer))`.

## Sources

All sources are public Hugging Face datasets with permissive licenses, verified 2026-07-08.
No AI Hub or non-commercial data is included.

Rows for `openorca_gugugo_ko` were collected in two passes (v1: first 400K; v2: the remaining
~1.84M, with rows already in v1 excluded). Both passes share the same `source_name`; the shard
files are named `openorca_gugugo_ko_shard_*` and `openorca_gugugo_ko_p2_shard_*`.

| source_name | Origin | Raw rows collected | Final rows | License | Task | Provenance |
|---|---|---:|---:|---|---|---|
| openorca_gugugo_ko | [squarelike/OpenOrca-gugugo-ko](https://huggingface.co/datasets/squarelike/OpenOrca-gugugo-ko) | 2,236,144 (of 2.24M) | 1,624,399 | MIT | general | machine-translated OpenOrca (Gugugo) |
| kocommercial | [MarkrAI/KoCommercial-Dataset](https://huggingface.co/datasets/MarkrAI/KoCommercial-Dataset) | 175,454 | 171,462 | MIT | general | mixed (commercial-safe aggregate) |
| kullm_v2 | [nlpai-lab/kullm-v2](https://huggingface.co/datasets/nlpai-lab/kullm-v2) | 152,630 | 127,894 | Apache-2.0 | general | GPT-translated alpaca/dolly/vicuna |
| korean_safe_conversation | [jojo0217/korean_safe_conversation](https://huggingface.co/datasets/jojo0217/korean_safe_conversation) | 26,979 | 26,803 | Apache-2.0 | safety | safe-response / refusal behavior |
| medical_reasoning_ko | [ChuGyouk/medical-o1-reasoning-SFT-Ko](https://huggingface.co/datasets/ChuGyouk/medical-o1-reasoning-SFT-Ko) | 25,682 | 24,207 | Apache-2.0 | reasoning | medical QA (final answers only, CoT traces excluded) |
| kopen_platypus | [kyujinpy/KOpen-platypus](https://huggingface.co/datasets/kyujinpy/KOpen-platypus) | 24,926 | 17,585 | CC-BY-4.0 | reasoning | translated Open-Platypus (STEM/logic) |
| openorca_ko | [kyujinpy/OpenOrca-KO](https://huggingface.co/datasets/kyujinpy/OpenOrca-KO) | 21,632 | 14,853 | MIT | general | curated OpenOrca translation |
| claude_reasoning_ko | [Jongsim/claude-opus-4.6-reasoning-12k-ko-filtered-v2](https://huggingface.co/datasets/Jongsim/claude-opus-4.6-reasoning-12k-ko-filtered-v2) | 12,126 | 11,047 | Apache-2.0 | reasoning | Claude Opus teacher, Korean reasoning (7 rows with literal `<think>` traces removed) |

## Processing

Each source went through the following per-dataset pipeline (independent per source; statistics in
the shipped `manifest.json` and the pipeline audit report):

1. **Structure** — normalized to `{messages: [{role, content}]}`; rows failing conversion dropped
2. **Clean** — removed empty turns, broken role ordering, conversations not ending on an assistant turn, encoding damage
3. **Quality filter** — rule-based scoring (instruction clarity, response relevance, length, repetition, refusals); score < 0.6 dropped
4. **Safety filter** — tagged and removed toxic / sexual / PII / harmful content
5. **Dedup** — exact SHA-256 dedup + MinHash-LSH near-dedup (Jaccard ≥ 0.8), *within each source*
6. **Format** — rendered to ChatML
7. **Tokenize** — token counts with the Keural tokenizer; samples > 8,192 tokens truncated

## Usage

```python
from datasets import load_dataset

ds = load_dataset("Mkd-Yonas/keural-SFT-chatml-ko-v3", split="train")

# e.g. exclude the large machine-translated subset (~80% of the data)
ds_curated = ds.filter(lambda r: r["source_name"] != "openorca_gugugo_ko")
```

## Integrity

`manifest.json` lists every shard with row count and sha256. Verify after download:

```bash
sha256sum *_shard_*.jsonl   # compare against manifest.json
```
