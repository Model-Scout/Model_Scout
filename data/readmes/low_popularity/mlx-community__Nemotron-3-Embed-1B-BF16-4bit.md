---
license: openmdw-1.1
language:
- en
- ar
- as
- bn
- bg
- zh
- da
- nl
- fi
- fr
- de
- hi
- id
- it
- ja
- ko
- ms
- mr
- ne
- 'no'
- fa
- pt
- ro
- ru
- es
- sw
- sv
- ta
- te
- th
- uk
- ur
- vi
- multilingual
library_name: mlx
pipeline_tag: sentence-similarity
tags:
- mlx
- sentence-similarity
- feature-extraction
- retrieval
- embeddings
base_model: nvidia/Nemotron-3-Embed-1B-BF16
base_model_relation: quantized
---

# Nemotron-3-Embed-1B-BF16-4bit

An **MLX conversion** of [`nvidia/Nemotron-3-Embed-1B-BF16`](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16) that runs
natively on Apple Silicon. Weights are quantized to MLX affine 4-bit (group_size=64).

This is an **independent community conversion**. It is **not affiliated with or
endorsed by NVIDIA**. The original model ships vLLM (CUDA) and PyTorch paths
only; this repository fills the MLX gap and bundles a self-contained
implementation.

The repository name keeps the upstream `-BF16` suffix on purpose: NVIDIA
publishes both a BF16 and an NVFP4 checkpoint, and this conversion is derived
from the **BF16** one.

Mirrored from [`choipilkyu/Nemotron-3-Embed-1B-BF16-MLX-4bit`](https://huggingface.co/choipilkyu/Nemotron-3-Embed-1B-BF16-MLX-4bit),
where these weights were first published.

## Changes from the original

The original architecture `Ministral3Model` is a bidirectional-attention encoder,
which `mlx-lm` / `mlx-embeddings` do not support out of the box. The following
changes were made, and the implementation is bundled as a single self-contained
file, [`nemotron3_embed_mlx.py`](nemotron3_embed_mlx.py):

1. Reused attention, yarn RoPE and llama_4_scaling from the `ministral3` causal-LM
   implementation in `mlx-lm`.
2. Removed the causal mask and replaced it with a key-padding mask, turning the
   stack into a **bidirectional encoder**.
3. Applied mean pooling + L2 normalization. Pooling and normalization run in fp32
   to avoid bf16 accumulation error perturbing the embedding norm.
4. Applied MLX affine 4-bit quantization (`group_size=64`).

No weights were retrained. Numerics are unchanged apart from the quantization
noted above.

## Verification

Checked against the original PyTorch implementation (fp32, identical token ids):
worst-case cosine similarity of the pooled embedding **> 0.999**.

| Check | This build |
|---|---|
| Source revision converted | [`a5e0f804b9e9`](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16/tree/a5e0f804b9e90a1ca6784ecbf6e41595774fc834) |
| `model.safetensors` sha256 | `73b06890e9d44ac792c98d38cd1d624ad4c45b5e0a4106bae6bef1ae356dd62f` |
| Embedding L2 norm (min–max) | 1.000000 – 1.000000 |

Embeddings are L2-normalized exactly, not approximately: pooling and
normalization run in fp32 so bf16 accumulation cannot drift the norm.

## Quantization impact

This repository is a **format conversion**, not a new model. Absolute retrieval
quality belongs to the upstream model — see
[`nvidia/Nemotron-3-Embed-1B-BF16`](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16) and NVIDIA's published benchmark
figures. This card therefore does not restate absolute quality; it measures the
two things the conversion itself can change: **fidelity to the original**
(above) and **what quantization costs**.

Measured on an Apple M4 (32GB). Every variant saw identical task data on the same
machine, which is what makes the comparison valid:

| Variant | Size | NDCG@10 retention | Recall@10 retention |
|---|---|---|---|
| [`Nemotron-3-Embed-1B-BF16`](https://huggingface.co/mlx-community/Nemotron-3-Embed-1B-BF16) | 2.28 GB | 100.0% | 100.0% |
| [`Nemotron-3-Embed-1B-BF16-8bit`](https://huggingface.co/mlx-community/Nemotron-3-Embed-1B-BF16-8bit) | 1.21 GB | 100.0% | 100.0% |
| [`Nemotron-3-Embed-1B-BF16-4bit`](https://huggingface.co/mlx-community/Nemotron-3-Embed-1B-BF16-4bit) | 0.64 GB | 99.3% | 98.7% |

Retention is the per-dataset ratio to bf16, averaged over the nine tasks below.

**NanoBEIR** — 4 of the 13 tasks, each on its full corpus, so these per-task
figures are directly comparable to other published NanoBEIR per-task numbers.
The 4-task average is not comparable to a published 13-task mean, so none is
given.

NDCG@10 per dataset:

| Dataset | bf16 | 8bit | 4bit |
|---|---|---|---|
| NanoNQ · en | 0.7482 | 0.7418 | 0.7565 |
| NanoFiQA2018 · en | 0.6355 | 0.6387 | 0.6017 |
| NanoSciFact · en | 0.7821 | 0.7818 | 0.7894 |
| NanoNFCorpus · en | 0.3653 | 0.3666 | 0.3608 |

Recall@10 per dataset:

| Dataset | bf16 | 8bit | 4bit |
|---|---|---|---|
| NanoNQ · en | 0.8800 | 0.8800 | 0.8900 |
| NanoFiQA2018 · en | 0.7407 | 0.7407 | 0.7069 |
| NanoSciFact · en | 0.8700 | 0.8700 | 0.8700 |
| NanoNFCorpus · en | 0.1492 | 0.1498 | 0.1384 |

**MIRACL** — dev-split hard-negatives corpus **subsampled to ~6k passages per
language** (every judged document kept; distractors drawn with a fixed seed, so
all variants face the identical task). Subsampling inflates the absolute
numbers, so **these are for relative comparison between variants only** and must
not be read against published full-corpus MIRACL results. A second reason not to
read them as quality figures: NVIDIA lists `MIRACLRetrieval` among the upstream
model's [training datasets](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16), so MIRACL is
in-domain for this model, not a zero-shot benchmark. Neither caveat affects the
retention comparison, which is what these rows are here for.

NDCG@10 per dataset:

| Dataset | bf16 | 8bit | 4bit |
|---|---|---|---|
| MIRACL · ar | 0.8920 | 0.8918 | 0.8895 |
| MIRACL · de | 0.8067 | 0.8074 | 0.8009 |
| MIRACL · es | 0.8582 | 0.8593 | 0.8584 |
| MIRACL · ja | 0.8658 | 0.8663 | 0.8637 |
| MIRACL · ko | 0.8143 | 0.8157 | 0.8086 |

Recall@10 per dataset:

| Dataset | bf16 | 8bit | 4bit |
|---|---|---|---|
| MIRACL · ar | 0.9873 | 0.9870 | 0.9884 |
| MIRACL · de | 0.9614 | 0.9614 | 0.9597 |
| MIRACL · es | 0.9788 | 0.9788 | 0.9790 |
| MIRACL · ja | 0.9851 | 0.9851 | 0.9839 |
| MIRACL · ko | 0.9185 | 0.9185 | 0.9146 |

Reproduce with the bundled [`benchmark_mteb.py`](benchmark_mteb.py):
`pip install mteb datasets` then `python benchmark_mteb.py . results.json`.

## Usage

```bash
pip install mlx mlx-lm transformers numpy huggingface_hub
```

```python
import sys
from huggingface_hub import snapshot_download

path = snapshot_download("mlx-community/Nemotron-3-Embed-1B-BF16-4bit")
sys.path.insert(0, path)
from nemotron3_embed_mlx import load, encode

model, tokenizer = load(path)
q = encode(model, tokenizer, ["What is the refund policy?"], input_type="query")
d = encode(model, tokenizer,
           ["Full refunds are available within 14 days of purchase."],
           input_type="passage")
print(float(q[0] @ d[0]))   # embeddings are L2-normalized, so dot == cosine
```

**Prefixes matter.** Queries need `query: ` and documents need `passage: `.
The `input_type` argument applies them for you; pass `input_type=None` if you
have already added the prefix yourself.

## Repository contents

The sentence-transformers scaffolding files (`modules.json`, `1_Pooling/`,
`sentence_bert_config.json`, `config_sentence_transformers.json`) are carried
over from the upstream repository as configuration reference. **These weights
load only via the bundled MLX implementation** — not via `sentence-transformers`
or `transformers`.

## Choosing a variant

Measured on an M1 Pro (16GB) over 200 documents averaging 1,014 characters,
batch size 8:

| Backend | Throughput | Weights |
|---|---|---|
| upstream via PyTorch/MPS (sentence-transformers) | 1.53 docs/s | 2.28 GB |
| this port, bf16 | **2.71 docs/s** | 2.28 GB |
| this port, 8-bit | 1.66 docs/s | 1.21 GB |
| this port, 4-bit | 1.65 docs/s | 0.64 GB |

Two things follow. At identical precision the MLX path is **1.8x faster** than
the upstream PyTorch/MPS path. But the quantized variants are **~1.6x slower
than bf16, not faster**: at 1.1B parameters the dequantization cost outweighs
the reduced memory traffic. The same ordering shows up in the Apple M4 runs
above (bf16 2.5 docs/s, 8-bit and 4-bit 2.2 docs/s).

**Pick bf16 for throughput. Pick 8-bit or 4-bit for footprint** — 0.64 GB fits
alongside other work on a small machine, and keeps 99.3% NDCG retention.

Reproduce on your own machine with the bundled
[`compare_backends.py`](compare_backends.py).

## Limitations

- Default `max_length` is 4096. The original supports 32k, but bidirectional
  attention is O(L²) and memory becomes the binding constraint well before that.
- Throughput on Apple Silicon is modest: 2.5 docs/s on long Korean
  documents (avg 1,014 chars, batch 8) measured on an Apple M4 (32GB). Use a server for
  bulk indexing and this for development and interactive querying, where
  single-query latency is not a problem.
- Embeddings from different variants are not interchangeable. Do not mix
  outputs of different variants in one index.

## License

The original model is licensed by NVIDIA under **OpenMDW-1.1**, and its base
model `mistralai/Ministral-3-3B-Instruct-2512` under Apache-2.0. Both texts are
bundled here as [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE).

Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
