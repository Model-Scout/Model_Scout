---
license: other
license_name: lfm1.0
license_link: LICENSE
base_model: LiquidAI/LFM2.5-ColBERT-350M
pipeline_tag: feature-extraction
library_name: litert
language:
- en
- es
- de
- fr
- it
- pt
- ar
- sv
- 'no'
- ja
- ko
tags:
- litert
- tflite
- on-device
- edge
- colbert
- late-interaction
- retrieval
- multi-vector
- liquid
- lfm2
- lfm2.5
base_model_relation: quantized
---

# LFM2.5-ColBERT-350M — LiteRT

[LiquidAI/LFM2.5-ColBERT-350M](https://huggingface.co/LiquidAI/LFM2.5-ColBERT-350M) converted to **LiteRT** (`.tflite`) for on-device retrieval. A multilingual late-interaction retriever: it emits **one 128-d vector per token**, and documents are ranked by MaxSim rather than by a single-vector cosine. Higher accuracy and better generalization than a dense bi-encoder, at the cost of index size.

If you want one vector per text, use [LFM2.5-Embedding-350M](https://huggingface.co/litert-community/LFM2.5-Embedding-350M) instead — it is the same backbone with a dense head.

| File | Recipe | Size | |
|---|---|---|---|
| `LFM2.5-ColBERT-350M_wi8fc.tflite` | int8 dynamic-range (linears + embedding, convs float) | 370 MB | mobile + desktop (iPhone-verified bit-exact, 1.2 GiB peak) |
| `LFM2.5-ColBERT-350M_fp16.tflite` | fp16 weights, float compute | 710 MB | desktop; loads on a 12 GB iPhone but needs **5.8 GiB** peak |

## Signatures

Batch-1, right-padded static shapes: `input_ids` int32 `[1, S]`, `attention_mask` int32 `[1, S]`.

| Signature | Output |
|---|---|
| `encode_32` / `encode_128` / `encode_256` / `encode_512` | `output_0` float32 `[1, S, 128]` — one L2-normalized vector per position |

There is **no separate query and document signature**: the graph is identical for both. What differs is entirely host-side — which prefix token you insert, how you pad, and which positions you keep. Queries use `encode_32`.

**Pick a signature for speed and memory, not for quality.** The same document routed through `encode_128`, `encode_256` or `encode_512` returns *bitwise identical* vectors at every position you keep. (The short-convolution kernel is 3, so a token reads exactly one neighbour on each side; once there is one pad to the right, more pads change nothing.)

## Host contract — this model does not work without it

Late interaction puts real work on the host. All of the following comes from `pylate` 1.6.0 and this repo's `config_sentence_transformers.json`.

**Queries** — `encode_32`:
1. Tokenize to **31** tokens with `padding="max_length"`, padding with the **EOS token, id 7**.
2. Insert `[Q] ` (id **64400**) at **position 1**, right after BOS → 32 tokens. Insert a `1` at position 1 of the attention mask too.
3. Leave the attention mask **0** on the padded positions.
4. **Keep all 32 vectors for scoring**, expansion positions included. That is what query expansion is; those positions carry query signal even though nothing attends to them. No skiplist on queries.

**Documents** — the smallest signature that fits:
1. Tokenize to **511**, insert `[D] ` (id **64401**) at position 1 → up to 512.
2. Keep positions where `attention_mask == 1` **and** the token id is not in the 32-entry punctuation skiplist from `config_sentence_transformers.json`.

**Scoring** — MaxSim: for each kept query vector take the maximum dot product over the kept document vectors, then sum over query vectors. Vectors are already unit length, so a dot product is a cosine.

> **The pad token id is part of the contract.** This model deliberately does *not* zero its padding states — that is what keeps query-expansion vectors alive — so padding with 0 instead of 7 changes the output (measured 0.34 max abs). Note `config.json` says `pad_token_id: 0`; pylate does not use it, and neither should you.

## Quality

Measured against the PyTorch reference at the same padded shape, so the numbers isolate the export.

| Variant | per-token cos vs PyTorch | NanoSciFact nDCG@10 | recall@5 | hit@1 |
|---|---|---|---|---|
| PyTorch fp32 (padded reference) | — | 0.8625 | 0.900 | 0.760 |
| fp16 | 1.000000 | 0.8625 | 0.900 | 0.760 |
| int8 (wi8fc) | 0.9986 | 0.8626 | 0.920 | 0.760 |

Conversion is lossless and int8 costs nothing measurable (+0.0001 nDCG@10, well inside noise). 600 documents, 50 queries, 165 778 document vectors (276 per document).

**One honest caveat about fixed shapes.** pylate encodes documents unpadded; a `.tflite` signature is a fixed shape and always pads. The resulting document vectors differ from an unpadded PyTorch run by cosine 0.9957 per token, and the same 50-query set scores 0.8777 unpadded versus 0.8625 padded. That 0.0152 gap is *inside one standard error at 50 queries*, so this set cannot tell you whether the shift costs any real retrieval quality — but the vectors do move, and you should know that before comparing an on-device index against a server-side one built with pylate.

## Speed

Apple-silicon Mac, XNNPACK, 16 threads, 20 iterations after warmup:

| Variant | encode_32 | encode_128 | encode_256 | encode_512 |
|---|---|---|---|---|
| int8 (wi8fc) | 24.8 ms | 44.1 ms | 68.0 ms | 118.8 ms |
| fp16 | 30.2 ms | 66.3 ms | 101.9 ms | 181.2 ms |
| fp32 | 24.5 ms | 53.1 ms | 88.9 ms | 178.2 ms |

iPhone 17 Pro, XNNPACK, 6 threads:

| Variant | load+delegate | peak footprint | encode_32 | encode_128 | encode_512 | vs Mac |
|---|---|---|---|---|---|---|
| int8 (wi8fc) | 0.77 s | **1254 MiB** | 30 ms | 40–64 ms | 180 ms | cosine 1.000000, **max diff 0.0** |
| fp16 | 1.42 s | **5786 MiB** | 136 ms | 87–248 ms | 447 ms | cosine 1.000000, max diff 3e-07 |

The int8 model reproduces the Mac outputs **bit-exactly** on device across all tested cases, including a real 32-token query with 23 expansion positions and the same document at two signature lengths. fp16 runs on an iPhone 17 Pro but its 5.8 GiB peak is a function of that device's memory — treat fp16 as the desktop artifact. fp16 is also slower than fp32 on CPU: XNNPACK unpacks fp16 weights to fp32 at run time.

### GPU (2026-08-13 re-export)

The re-export respells the one idiom mobile GPU delegates refuse — transformers' rank-5 `repeat_kv` expand — into an equivalent rank-4 matmul (outputs bitwise-identical on CPU), and the int8 file now fully delegates on mobile GPUs. Measured with the LiteRT CompiledModel API (fp32 GPU precision, real inputs, best of 3 warm runs): Pixel 8a OpenCL `encode_512` **14.3 ms**, cosine **0.9999** vs the fp32 desktop reference; iPhone 17 Pro Metal `encode_512` 173 ms (all six fixture cases ≥ 0.9999). Set the GPU precision to **fp32** — at fp16 GPU precision this family's norm reductions overflow and every output is NaN; CompiledModel timings are not comparable to classic-delegate `benchmark_model` timings.

## Snapdragon NPU (Hexagon)

- `LFM2.5-ColBERT-350M_fp16.tflite` — the NPU runs it at 177.7 ms. The GPU does not — `LiteRtException: Failed to compile model`.
- `LFM2.5-ColBERT-350M_wi8fc.tflite` — the GPU runs it at 83.20 ms. The NPU does not — `LiteRtException: Failed to compile model`.

| file | backend | compiled | inference (median / min) | load |
|---|---|---|---:|---:|
| `LFM2.5-ColBERT-350M_fp16.tflite` | NPU (Hexagon v81) | AOT (SM8850) | 177.7 ms / 174.3 ms | 1539 ms |
| `LFM2.5-ColBERT-350M_wi8fc.tflite` | GPU (Adreno) | — | 83.20 ms / 79.95 ms | 13004 ms |

Measured on a **Samsung Galaxy S26** (Snapdragon 8 Elite Gen 5 / SM8850, Hexagon v81, Android 16) with LiteRT `CompiledModel` 2.2.0, one accelerator per process, 5 warm-up runs then N=50 timed runs, median reported. Every run held thermal status `NONE` throughout. Headroom 0.75–0.78, where 1.0 is the throttling threshold.

The NPU row marked *AOT* ran an artifact compiled ahead of time for SM8850 (ai-edge-litert 2.2.0 + QAIRT 2.47.0), not the published file. That artifact is not distributed here; the compile is one command in the [NPU guide](https://github.com/john-rocky/hf-to-litertlm/blob/main/docs/android-npu.md).

GPU wiring: [GPU guide](https://github.com/john-rocky/hf-to-litertlm/blob/main/docs/android-gpu.md).

## Usage (Python)

```python
import json
import numpy as np
from ai_edge_litert.interpreter import Interpreter
from tokenizers import Tokenizer

PAD, Q_ID, D_ID = 7, 64400, 64401
tok = Tokenizer.from_file("tokenizer.json")
it = Interpreter(model_path="LFM2.5-ColBERT-350M_wi8fc.tflite")
CFG = json.load(open("config_sentence_transformers.json"))
skiplist = {tok.token_to_id(w) for w in CFG["skiplist_words"]}

def _run(sig, ids, mask):
    x = np.full((1, sig), PAD, np.int32)
    m = np.zeros((1, sig), np.int32)
    x[0, :len(ids)] = ids
    m[0, :len(mask)] = mask
    r = it.get_signature_runner(f"encode_{sig}")
    return list(r(input_ids=x, attention_mask=m).values())[0][0]

def encode_query(text):                      # -> [32, 128], ALL kept
    ids = tok.encode(text).ids[:31]
    ids = [ids[0], Q_ID] + ids[1:]
    mask = [1] * len(ids)
    return _run(32, ids, mask)               # padded positions are scored too

def encode_document(text):                   # -> [n_kept, 128]
    ids = tok.encode(text).ids[:511]
    ids = [ids[0], D_ID] + ids[1:]
    sig = next(s for s in (128, 256, 512) if len(ids) <= s)
    v = _run(sig, ids, [1] * len(ids))[:len(ids)]
    keep = [i for i, t in enumerate(ids) if t not in skiplist]
    return v[keep]

def maxsim(q, d):                            # ColBERT late interaction
    return float((q @ d.T).max(axis=1).sum())

q = encode_query("What is the capital of France?")
docs = [encode_document(t) for t in ["Paris is the capital of France.",
                                     "Tokyo is the capital of Japan."]]
print([round(maxsim(q, d), 3) for d in docs])
```

On Android/iOS use the LiteRT runtime's SignatureRunner APIs with the same signature names; the tokenizer is the standard Hugging Face `tokenizer.json`.

## License

LFM Open License v1.0 (see `LICENSE`, unchanged from the base model). Note the license's commercial-use threshold (Section 5). This repository redistributes converted **Derivative Works** of LiquidAI/LFM2.5-ColBERT-350M with modification notices per Section 4; all credit for the model to [Liquid AI](https://www.liquid.ai/).
