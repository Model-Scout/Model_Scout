---
license: other
language:
- ko
- en
tags:
- sft
- instruction-tuning
- chatml
- korean
- math
- code
size_categories:
- 1M<n<10M
---

# Keural SFT Dataset

Bilingual (Korean/English) instruction-tuning dataset for the Keural LLM project.
Built from 14 curated sources and formatted in ChatML after multi-stage filtering.

---

## Dataset Summary

| Field | Value |
|-------|-------|
| Total samples | 1,144,119 |
| Total tokens | 710,280,675 (~710M) |
| Average tokens/sample | 621.0 |
| Max sequence length | 8,192 tokens |
| Language ratio | Korean 45.3% / English 54.7% |
| Format | ChatML |
| Number of shards | 115 (10,000 samples/shard) |
| Tokenizer | Keural SentencePiece |

---

## Format

Each sample contains a `text` field in ChatML format.

```
<|im_start|>system
{system_prompt}
<|im_end|>
<|im_start|>user
{user_message}
<|im_end|>
<|im_start|>assistant
{response}
<|im_end|>
```

The `system` turn is included only when present in the source data.

### Record Schema

```jsonl
{
  "text": "<|im_start|>user\n...<|im_end|>\n<|im_start|>assistant\n...<|im_end|>",
  "source_name": "alpaca",
  "license": "cc-by-4.0",
  "n_tokens": 312
}
```

### Special Tokens

The Keural tokenizer includes the following reserved tokens:

| Token | ID | Description |
|-------|----|-------------|
| `<pad>` | 0 | Padding |
| `<bos>` | 1 | Beginning of sequence |
| `<eos>` | 2 | End of sequence |
| `<unk>` | 3 | Unknown token |
| `<\|im_start\|>` | — | Turn start marker (**must be added before training/serving**) |
| `<\|im_end\|>` | — | Turn end marker (**must be added before training/serving**) |

`<|im_start|>` and `<|im_end|>` are not in the base vocabulary and must be added as user-defined tokens prior to fine-tuning.

---

## Dataset Composition

### Per-Source Statistics

| Dataset | Samples | Total Tokens | Avg Tokens | Task | Language | License |
|---------|--------:|-------------:|----------:|------|----------|---------|
| ultrachat | 193,212 | 257,127,675 | 1,330.8 | general | en | MIT |
| orca_math_korean | 185,362 | 71,152,470 | 383.9 | math | ko | MIT |
| openorca | 138,639 | 57,813,277 | 417.0 | general | en | MIT |
| aihub_multisession_sci | 127,868 | 92,753,664 | 725.4 | general | ko | AI Hub Terms |
| mathinstruct | 153,921 | 48,697,451 | 316.4 | math | en | MIT |
| aihub_multisession_social | 85,346 | 69,374,613 | 812.9 | general | ko | AI Hub Terms |
| magicoder | 71,953 | 43,425,338 | 603.5 | code | en | MIT |
| koinstruct_qa | 45,299 | 20,179,572 | 445.5 | general | ko | Apache 2.0 |
| koinstruct_base | 42,276 | 22,795,596 | 539.2 | general | ko | Apache 2.0 |
| alpaca | 46,303 | 5,390,721 | 116.4 | general | en | CC BY 4.0 |
| koalpaca | 21,091 | 4,278,003 | 202.8 | general | ko | CC BY-SA 4.0 |
| competition_math | 12,040 | 4,042,968 | 335.8 | math | en | MIT |
| aihub_expert_qa | 10,778 | 10,921,351 | 1,013.3 | general | ko | AI Hub Terms |
| gsm8k | 10,031 | 2,327,976 | 232.1 | math | en | MIT |
| **Total** | **1,144,119** | **710,280,675** | **621.0** | | | |

### Domain Distribution

| Domain | Samples | Share | Total Tokens | Avg Tokens |
|--------|--------:|------:|-------------:|-----------:|
| general/en | 378,154 | 33.1% | 320,331,673 | 847.1 |
| general/ko | 332,658 | 29.1% | 220,302,799 | 662.3 |
| math/ko | 185,362 | 16.2% | 71,152,470 | 383.9 |
| math/en | 175,992 | 15.4% | 55,068,395 | 312.9 |
| code/en | 71,953 | 6.3% | 43,425,338 | 603.5 |

### Language Split

| Language | Samples | Share |
|----------|--------:|------:|
| English | 626,099 | 54.7% |
| Korean | 518,020 | 45.3% |

### Token Length Distribution

| Range | Samples | Share |
|-------|--------:|------:|
| 0–512 | 563,375 | 49.2% |
| 512–1,024 | 425,489 | 37.2% |
| 1,024–2,048 | 129,878 | 11.3% |
| 2,048–4,096 | 24,942 | 2.2% |
| 4,096+ | 435 | 0.04% |

---

## Processing Pipeline

```
A. collect   → Download from HuggingFace Hub / AI Hub
B. structure → Normalize to standard messages schema
C. clean     → Remove empty responses, role errors, control characters
D. quality   → Quality score filter (min threshold: 0.6)
E. safety    → Tag and remove harmful content
F. dedup     → Exact hash + MinHash LSH deduplication (similarity threshold: 0.8)
G. format    → Apply ChatML template
H. tokenize  → Measure token length, truncate at 8,192
I. package   → Split into 10,000-sample shards with SHA256 checksums
```

### Filter Funnel (Overall)

| Stage | Output | Removed | Retention |
|-------|-------:|--------:|----------:|
| B. Structure | 1,427,282 | 60 | 100.0% |
| C. Clean | 1,364,734 | 62,548 | 95.6% |
| D. Quality | 1,296,048 | 68,686 | 94.9% |
| E. Safety | 1,292,731 | 3,317 | 99.7% |
| F. Dedup | 1,144,119 | 148,612 | 88.5% |
| **Final** | **1,144,119** | **283,283 total** | **80.1%** |

> Note: OpenOrca raw corpus contains 4.2M samples; 200,000 were sampled before entering the pipeline.

### Filter Breakdown by Stage

**C. Clean** — 62,548 removed

| Filter | Count |
|--------|------:|
| Response too short | 59,079 |
| Invalid role order | 3,138 |
| Placeholder response | 329 |
| Response too long | 2 |

**D. Quality** — 68,686 removed (score < 0.6)

| Score Range | Samples | Action |
|-------------|--------:|--------|
| 0.8 – 1.0 | 766,973 | kept |
| 0.6 – 0.8 | 529,075 | kept |
| 0.4 – 0.6 | 68,680 | removed |
| 0.2 – 0.4 | 6 | removed |

**E. Safety** — 3,317 removed

| Tag | Count | Action |
|-----|------:|--------|
| safe | 1,288,616 | kept |
| refusal | 4,115 | kept |
| pii | 1,761 | removed |
| toxic | 824 | removed |
| sexual | 583 | removed |
| harmful | 102 | removed |
| flagged | 47 | removed |

**F. Dedup** — 148,612 removed

| Type | Count |
|------|------:|
| Near-duplicate (MinHash LSH, threshold 0.8) | 132,540 |
| Exact duplicate (hash) | 16,072 |

### Per-Dataset Filter Progression

| Dataset | Structured | → Clean | → Quality | → Safety | → Final | Retention |
|---------|----------:|--------:|----------:|---------:|--------:|----------:|
| openorca | 200,000 | 184,306 | 153,630 | 153,368 | 138,639 | 69.3% |
| koalpaca | 21,155 | 21,146 | 21,140 | 21,091 | 21,091 | 99.7% |
| magicoder | 75,197 | 75,197 | 74,537 | 74,386 | 71,953 | 95.7% |
| mathinstruct | 262,038 | 261,549 | 253,729 | 253,603 | 153,921 | 58.7% |
| koinstruct_base | 50,169 | 50,137 | 48,220 | 48,022 | 42,276 | 84.3% |
| koinstruct_qa | 50,276 | 50,252 | 48,874 | 48,687 | 45,299 | 90.1% |
| competition_math | 12,500 | 12,500 | 12,402 | 12,396 | 12,040 | 96.3% |
| gsm8k | 14,946 | 14,946 | 14,946 | 14,946 | 10,031 | 67.1% |
| alpaca | 51,974 | 47,431 | 46,338 | 46,316 | 46,303 | 89.1% |
| orca_math_korean | 193,789 | 193,684 | 193,578 | 192,249 | 185,362 | 95.6% |
| ultrachat | 207,834 | 207,627 | 199,342 | 199,015 | 193,212 | 93.0% |
| aihub_multisession_sci | 135,105 | 130,284 | 128,948 | 128,669 | 127,868 | 94.6% |
| aihub_multisession_social | 135,851 | 104,250 | 89,508 | 89,205 | 85,346 | 62.8% |
| aihub_expert_qa | 16,448 | 11,425 | 10,856 | 10,778 | 10,778 | 65.5% |
| **Total** | **1,427,282** | **1,364,734** | **1,296,048** | **1,292,731** | **1,144,119** | **80.2%** |

> mathinstruct and gsm8k show high near-duplicate removal (~40%) due to overlapping math problem templates across splits.
> aihub_multisession_social has significant clean-stage drop (23%) due to short or malformed response turns.

---

## Licenses

This dataset is a mixture of multiple sources with different licenses.
Please verify individual source licenses before any commercial use.

| License | Sources |
|---------|---------|
| MIT | OpenOrca, UltraChat, Magicoder, MathInstruct, competition_math, GSM8K, orca_math_korean |
| CC BY 4.0 | Stanford Alpaca |
| CC BY-SA 4.0 | KoAlpaca |
| Apache 2.0 | KoInstruct (base, qa) |
| AI Hub Terms (non-commercial research only) | AI Hub 71304, 71674, 71675 |
