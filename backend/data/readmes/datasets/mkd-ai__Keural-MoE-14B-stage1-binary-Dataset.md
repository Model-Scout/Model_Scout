---
license: other
task_categories:
- text-generation
language:
- ko
- en
tags:
- keural
- moe
- pretraining
- binary-dataset
- korean
- multilingual
- 69.5B-tokens
size_categories:
- 10B<n<100B
---

# Keural Stage 1 — 69.5 Billion Tokens Binary Dataset

Pre-tokenized binary dataset for the **Keural MoE Foundation Model**.
Ready to use directly for training — no tokenization step needed.

## Dataset Overview

| Property | Value |
|---|---|
| **Total Tokens** | **69.5 billion** (69,496,921,399) |
| **Format** | Binary (.bin) + Index (.idx) + Metadata (.meta) |
| **Total Sequences** | 15,761,448 |
| **Sequence Length** | 4,096 tokens |
| **Shards** | 158 shards |
| **Archive Size** | ~242GB (binary_69B_tokens.tar) |
| **Tokenizer** | Keural SentencePiece Unigram, vocab=131,072 |
| **Last Updated** | 2026-04-03 |

## Data Sources

| Source | Language | Tokens (approx) |
|---|---|---|
| FineWeb | English | ~20B |
| WanJuan Korean | Korean | ~5B |
| Korean WebText | Korean | ~4B |
| ArXiv | English Science | ~4B |
| CC100 Korean | Korean | ~3B |
| PubMed | English Medical | ~3B |
| The Stack v1 | Code | ~8B |
| Wikipedia Korean | Korean | ~1B |
| PG19 Literature | English | ~1B |
| Other sources | Mixed | ~20.5B |

## Archive Contents

The tar file contains a `binary/` folder with:
- **158 .bin files**: Pre-tokenized binary data (keural_000.bin to keural_157.bin)
- **158 .idx files**: Index files for fast random access
- **158 .meta files**: Metadata JSON for each shard
- **build_stats.json**: Complete build statistics

## Binary Format Specification

```
File: keural_NNN.bin
─────────────────────────────────────────
HEADER (36 bytes):
  [0:8]   magic   = b"KEURAL\x00\x00"   (8 bytes)
  [8:12]  version = 1                    (uint32 LE)
  [12:20] num_seq                        (uint64 LE)
  [20:28] seq_len = 4096                 (uint64 LE)
  [28:36] padding = 0                    (uint64 LE)

BODY:
  num_seq × 4096 × 4 bytes (uint32 LE tokens)

File: keural_NNN.idx
─────────────────────────────────────────
  [0:4]  num_seq  (uint32)
  [4:8]  seq_len  (uint32)
  per sequence: 8-byte offset + 4-byte length

File: keural_NNN.meta (JSON)
─────────────────────────────────────────
  {"num_sequences": N, "seq_length": 4096, "source": "keural_NNN"}
```

## How to Extract

```bash
# Download the tar file, then extract:
tar -xf binary_69B_tokens.tar

# This creates: binary/ directory with 158 shards
```

## How to Use

```python
import struct, mmap, torch

HEADER_FMT  = "<8sIQQQ"
HEADER_SIZE = struct.calcsize(HEADER_FMT)  # 36 bytes

with open("binary/keural_001.bin", "rb") as f:
    raw = f.read(HEADER_SIZE)
    magic, ver, num_seqs, seq_len, _ = struct.unpack(HEADER_FMT, raw)
    print(f"Sequences: {num_seqs}, Length: {seq_len}")

# Or use directly with training scripts:
# torchrun --nproc_per_node=2 train_keural_v2.py --data_dir ./binary
```

## Build Statistics

```json
{
  "documents_processed": 553,711,744,
  "tokens_processed": 69,496,921,399,
  "sequences_written": 15,761,448,
  "padding_added": 3,143,055,066,
  "shards_created": 158,
  "sequence_utilization": "95.13%"
}
```

## Related Resources

- Model Training: [github.com/mkd-hossain/Keural-Model-Training](https://github.com/mkd-hossain/Keural-Model-Training)
- Tokenizer: [huggingface.co/mkd-ai/keural-tokenizer](https://huggingface.co/mkd-ai/keural-tokenizer)
- Organization: [huggingface.co/mkd-ai](https://huggingface.co/mkd-ai)

## Author

MKD CO., LTD.  
Keural Foundation Model — Stage 1 pretraining dataset, 2026

## License
[![License](https://img.shields.io/github/license/MKD-CORP/Keural-MoE-14B-Training)](https://github.com/MKD-CORP/Keural-MoE-14B-Training/blob/main/LICENSE)

