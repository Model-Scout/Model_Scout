---
license: other
task_categories:
- text-generation
language:
- en
- ko
- ja
- zh
pretty_name: DeepSeek-V4 Flash REAM Healing Mix 2048
size_categories:
- 1K<n<10K
configs:
- config_name: seq1024
  default: true
  data_files:
  - split: train
    path: data/train-*.parquet
- config_name: seq4096
  data_files:
  - split: train
    path: data-4096/train-*.parquet
- config_name: seq8192
  data_files:
  - split: train
    path: data-8192/train-*.parquet
- config_name: seq16384
  data_files:
  - split: train
    path: data-16384/train-*.parquet
- config_name: needle8192
  data_files:
  - split: train
    path: data-needle8192/train-*.parquet
- config_name: needle16384
  data_files:
  - split: train
    path: data-needle16384/train-*.parquet
---

# DeepSeek-V4 Flash REAM Healing Mix 2048

Private, deterministic healing mixtures for the 104-expert REAM-pruned
`DeepSeek-V4-Flash-0731-120B` checkpoint. It was prepared after direct A/B
generation tests found post-pruning degradation in factual accuracy, language
control, thinking delimiters, and long-code repetition.

## `seq1024` base config

- Rows: **2,048**
- Maximum sequence length: **1,024** DeepSeek-V4 tokens
- Non-padding tokens: **1,581,071**
- Supervised assistant tokens: **1,092,037**
- Length range / median: **15 / 1024 / 1024**
- Thinking-mode examples: **1,215**
- Seed: `20260804`
- Tensor SHA-256: `c1860cd7a5e395ed49bf9bd9921dac5901c722101c4df3ab0c8ae46d3282327e`

## `seq4096` long-context extension

- Rows: **2,048**, all identity-disjoint from `seq1024`
- Maximum sequence length: **4,096** DeepSeek-V4 tokens
- Non-padding tokens: **4,352,397**
- Supervised assistant tokens: **3,662,259**
- Length range / median: **13 / 1,709–1,713 / 4,096**
- Rows longer than 1,024 tokens: **1,240**
- Rows in the 3,073–4,096 range: **793**
- Thinking-mode examples: **1,235**
- Seed: `20260805`
- Tensor SHA-256: `746e918a89c177eb17ab9c543dcb5f974df7ce9dc0b8c546ef6678c9e3c178dc`

The extension was sampled from different byte ranges and local row identities
while excluding every `(source, identity)` pair in the base manifest. Its audit
reports **2,048 unique rows, zero overlap with `seq1024`, and no masking,
padding, label, shape, or checksum errors**.

## `seq8192` long-context extension

- Rows: **2,048**, identity-disjoint from both earlier configs
- Maximum sequence length: **8,192** DeepSeek-V4 tokens
- Non-padding tokens: **6,875,189**
- Supervised assistant tokens: **6,017,620**
- Length range / median: **19 / 1,805–1,806 / 8,192**
- Rows longer than 4,096 tokens: **724**
- Rows in the 6,145–8,192 range: **575**
- Thinking-mode examples: **1,239**
- Seed: `20260806`
- Tensor SHA-256: `4381ab63178054c1fdde4b4f2fd403f039004b91355931b9b98c197a38165336`

The 8K audit reports **2,048 unique rows, zero overlap with both `seq1024`
and `seq4096`, and no masking, padding, label, metadata, shape, or checksum
errors**. This config deliberately retains a substantial 8K-capped tail for
later selective healing; it is prepared data, not evidence that 8K training
was used in the current checkpoint.

## `seq16384` long-context extension

- Rows: **2,048**, identity-disjoint from all three earlier configs
- Maximum sequence length: **16,384** DeepSeek-V4 tokens
- Non-padding tokens: **8,122,959**
- Supervised assistant tokens: **7,120,731**
- Length range / median: **23 / 1,638 / 16,384**
- Rows longer than 8,192 tokens: **361**
- Rows in the 12,289–16,384 range: **235**
- Thinking-mode examples: **1,232**
- Seed: `20260807`
- Tensor SHA-256: `2cd538586b4c2577932bd2ecd4c574c132f462b3144a5e815cbea798f7a3a764`

The 16K audit reports **2,048 unique rows, zero overlap with all 6,144 rows
from `seq1024`, `seq4096`, and `seq8192`, and no masking, padding, label,
metadata, shape, or checksum errors**. Like `seq8192`, this is a prepared
extension for selective future healing and is not automatically mixed into a
checkpoint unless that training report names it.

## Near-limit needle configs

The procedural `needle8192` and `needle16384` configs contain **192 rows each**.
Unlike the organic SFT configs, every prompt is deliberately near its context
limit and has a short, exactly checkable assistant-only target.

| Config | Total-token range | Median pair | Non-padding tokens | Supervised tokens | SHA-256 |
|---|---:|---:|---:|---:|---|
| `needle8192` | 7,357–7,874 | 7,595–7,596 | 1,459,790 | 3,754 | `271aa96bd521f29d79c74a3d1b8d9dab9b8b4c0a7a4dcc879d5c99afce9ee16b` |
| `needle16384` | 14,737–15,726 | 15,227–15,228 | 2,923,540 | 3,732 | `d05eeba0f46b9647b2e77be1c118daeb7ca177da609f4ad59de4b931a5358473` |

Each config balances four task types (single exact lookup, two-hop join,
latest-version selection, and paired-value arithmetic) across front, middle,
and back needle positions: **12 combinations × 16 rows**. Training identities,
seeds, exact targets, prompt/total token counts, and generation script are
recorded in the manifests. The held-out evaluation identifiers `LANTERN`,
`Mina Park`, `7319`, and `eu-north-1` are excluded from these configs, and the
evaluation prompt template is not reused.

These are training/healing records, not benchmark examples. A model report
must explicitly name the config and row count before claiming that a checkpoint
was trained on them.

The `labels` column uses `-100` for all prompt tokens, so loss is computed only
on assistant reasoning/content tokens. Rows are already encoded with the
official DeepSeek-V4 `encoding/encoding_dsv4.py` format and the tokenizer from
the pruned BF16 checkpoint. No generic Jinja chat template was substituted.

## Source composition

| Source bucket | Rows | Pinned source |
|---|---:|---|
| `nemotron_if_chat` | 384 | `https://huggingface.co/datasets/nvidia/Nemotron-SFT-Instruction-Following-Chat-v2/resolve/1a9454ed054b8544503ab8d8c0a519d141a44c5b/data/reasoning_off.jsonl` |
| `nemotron_if_reasoning` | 256 | `https://huggingface.co/datasets/nvidia/Nemotron-SFT-Instruction-Following-Chat-v2/resolve/1a9454ed054b8544503ab8d8c0a519d141a44c5b/data/reasoning_on.jsonl` |
| `nemotron_swe_agentless` | 192 | `https://huggingface.co/datasets/nvidia/Nemotron-SFT-SWE-v2/resolve/bd151f3f2d89c4804dda0083d912bd9f6a0a9fb7/data/agentless.jsonl` |
| `nemotron_competitive_python` | 256 | `https://huggingface.co/datasets/nvidia/Nemotron-SFT-Competitive-Programming-v2/resolve/778afc98a9e027e10b3cd78020c120e93e142ef2/data/competitive_programming_python_00.jsonl` |
| `nemotron_multilingual_ja` | 128 | `https://huggingface.co/datasets/nvidia/Nemotron-SFT-Multilingual-v1/resolve/22c86505762a7c595abee309d720084351c9f4ba/data/super-v3_math_ja_translated_final.jsonl` |
| `nemotron_multilingual_zh` | 128 | `https://huggingface.co/datasets/nvidia/Nemotron-SFT-Multilingual-v1/resolve/22c86505762a7c595abee309d720084351c9f4ba/data/super-v3_math_zh_translated_final.jsonl` |
| `k_exaone_ko_instr` | 320 | `/workspace/data/K-EXAONE-236B-REAP-calibration-mix/mix.jsonl` |
| `k_exaone_ko_tool` | 128 | `/workspace/data/K-EXAONE-236B-REAP-calibration-mix/mix.jsonl` |
| `k_exaone_code_en` | 64 | `/workspace/data/K-EXAONE-236B-REAP-calibration-mix/mix.jsonl` |
| `k_exaone_tool_en` | 64 | `/workspace/data/K-EXAONE-236B-REAP-calibration-mix/mix.jsonl` |
| `k_exaone_mot_math` | 64 | `/workspace/data/K-EXAONE-236B-REAP-calibration-mix/mix.jsonl` |
| `k_exaone_agentic_swe` | 64 | `/workspace/data/K-EXAONE-236B-REAP-calibration-mix/mix.jsonl` |

The NVIDIA inputs are pinned to exact Hub revisions. The K-EXAONE records come
from `Baekpica/K-EXAONE-236B-REAP-calibration-mix` and were sampled from the
local revision used for the REAM calibration run.

## Files

- `data/train-00000-of-00001.parquet`: variable-length rows for Datasets/Arrow.
- `data-4096/train-00000-of-00001.parquet`: identity-disjoint long-context rows.
- `data-8192/train-00000-of-00001.parquet`: identity-disjoint 8K-context rows.
- `data-16384/train-00000-of-00001.parquet`: identity-disjoint 16K-context rows.
- `data-needle8192/train-00000-of-00001.parquet`: near-limit 8K needle rows.
- `data-needle16384/train-00000-of-00001.parquet`: near-limit 16K needle rows.
- `healing_mix_2048x1024.safetensors`: fixed `[2048, 1024]` tensors for low-overhead local training.
- `healing_mix_2048x4096.safetensors`: fixed `[2048, 4096]` long-context tensors.
- `healing_mix_2048x8192.safetensors`: fixed `[2048, 8192]` long-context tensors.
- `healing_mix_2048x16384.safetensors`: fixed `[2048, 16384]` long-context tensors.
- `healing_needle_192x8192.safetensors`: fixed `[192, 8192]` near-limit needle tensors.
- `healing_needle_192x16384.safetensors`: fixed `[192, 16384]` near-limit needle tensors.
- `healing_mix_2048x1024_manifest.json`: exact quotas, revisions, identities, statistics, and checksum.
- `healing_mix_2048x4096_manifest.json`: long-context provenance and identities.
- `healing_mix_2048x8192_manifest.json`: 8K provenance and exclusion identities.
- `healing_mix_2048x16384_manifest.json`: 16K provenance and exclusion identities.
- `healing_needle_192x8192_manifest.json`: procedural 8K needle provenance and exact targets.
- `healing_needle_192x16384_manifest.json`: procedural 16K needle provenance and exact targets.
- `healing_mix_2048x4096_audit.json`: full masking, uniqueness, overlap, and length-distribution audit.
- `healing_mix_2048x8192_audit.json`: full 8K masking, uniqueness, overlap, metadata, and length audit.
- `healing_mix_2048x16384_audit.json`: full 16K masking, uniqueness, overlap, metadata, and length audit.
- `healing_needle_192x8192_audit.json`: full 8K needle mask, identity, metadata, and length audit.
- `healing_needle_192x16384_audit.json`: full 16K needle mask, identity, metadata, and length audit.

```python
from datasets import load_dataset

dataset = load_dataset(
    "Baekpica/DeepSeek-V4-Flash-0731-REAM-Healing-Mix-2048",
    "seq8192",
    split="train",
)
print(dataset[0].keys())
```

## Licenses and attribution

This is a mixed-license derived dataset. Preserve the source-level attribution
and terms when using or redistributing rows:

- Nemotron Instruction-Following Chat v2: ODC-By.
- Nemotron Multilingual v1: CC BY 4.0; some upstream rows are CC BY-SA 4.0.
- Nemotron SWE v2: CC BY 4.0 with Apache-2.0/MIT/BSD upstream components.
- Nemotron Competitive Programming v2: CC BY 4.0, ODC-By, and MIT components.
- K-EXAONE calibration mix: follow its private repository card and each recorded
  upstream source license.

This repository is private and is intended for the specific model-healing run.
It is not an evaluation set and should not be used to claim benchmark results.

## Reproducibility

The fixed revisions, per-source quotas, byte-range sampling seeds, row identities,
assistant-only masking statistics, exclusion provenance, and artifact hashes are
recorded in the manifests.
The preparation script is `scripts/prepare_healing_mix.py` in the associated
model-build workspace.
