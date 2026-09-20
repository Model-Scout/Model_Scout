---
license: other
license_name: lfm1.0
license_link: LICENSE
base_model: LiquidAI/LFM2.5-Embedding-350M
pipeline_tag: sentence-similarity
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
- embeddings
- feature-extraction
- sentence-similarity
- retrieval
- liquid
- lfm2
- lfm2.5
base_model_relation: quantized
---

LiteRT is Google's on-device runtime, the new name for TensorFlow Lite (Android: `com.google.ai.edge.litert:litert`), and `litert-torch`, the renamed `ai-edge-torch`, is its PyTorch converter: a PyTorch model converted unmodified with `litert_torch.convert` matched the original to 4e-7 on a Galaxy S26 ([measured](https://github.com/john-rocky/apple-silicon-llm-bench/blob/main/results/android/tinyhybridnet-three-runtimes.md), LiteRT 2.2.0, Android 16, 2026-09-05).

# LFM2.5-Embedding-350M — LiteRT

[LiquidAI/LFM2.5-Embedding-350M](https://huggingface.co/LiquidAI/LFM2.5-Embedding-350M) converted to **LiteRT** (`.tflite`) for on-device inference. A multilingual (11 languages) dense bi-encoder on the LFM2 hybrid backbone (gated short-convolutions + grouped-query attention) — one 1024-d vector per text, for retrieval, semantic search and RAG, fully offline on CPU.

| File | Recipe | Size | |
|---|---|---|---|
| `LFM2.5-Embedding-350M_wi8fc.tflite` | int8 dynamic-range (linears + embedding, convs float) | 371 MB | mobile + desktop (iPhone-verified bit-exact, 1.2 GiB peak) |
| `LFM2.5-Embedding-350M_fp16.tflite` | fp16 weights, float compute | 712 MB | desktop; loads on a 12 GB iPhone but needs **5.8 GiB** peak — see Speed |

Since litert-lm 0.17.0 the same weights are also published as **LiteRT-LM EmbeddingEngine bundles** (`.litertlm`) that the runtime loads without any host-side tokenization or pooling code — see the section below.

## Signatures

All signatures take batch-1, right-padded static shapes: `input_ids` int32 `[1, S]`, `attention_mask` int32 `[1, S]` (1 = real token, 0 = pad).

| Signature | Output |
|---|---|
| `embed_64` / `embed_128` / `embed_256` / `embed_512` | `output_0` float32 `[1, 1024]` — CLS token, L2-normalized |

Pick the smallest signature that fits your token count. **The vector does not depend on which one you pick**: padding is zeroed inside the graph before the short-convolution and masked in attention, so the same text through `embed_64` and through `embed_512` returns a *bitwise identical* vector — verified on Mac and again on-device. Model max length is 512 tokens.

## Contract

Two things must match the upstream model or results silently degrade:

- **Asymmetric prompts, with the trailing space.** Prefix queries with `query: ` and passages with `document: `, exactly as stored in the base repo's `config_sentence_transformers.json`.
- **CLS pooling and normalization are already in the graph.** The output is the position-0 token vector, L2-normalized, so a plain dot product is cosine similarity. Do not pool or normalize again.

## LiteRT-LM EmbeddingEngine bundles (`.litertlm`, litert-lm ≥ 0.17.0)

Since litert-lm 0.17.0 the runtime hosts embedding models directly through `EmbeddingEngine` (Python, C and Kotlin), so the same weights are also published as bundles that the engine loads without any host-side tokenization or pooling code:

| file | contents | size |
|---|---|---|
| `LFM2.5-Embedding-350M_wi8fc.litertlm` | int8 embedding table + int8 (dynamic-range) encoder, signatures for 64/128/256/512 tokens | 370 MB |
| `LFM2.5-Embedding-350M_fp16.litertlm` | int8 embedding table + fp16 encoder | 647 MB |

The vectors are identical to the `.tflite` path (cosine 1.000000 on the check set below; CLS pooling and L2 normalization are inside the graph). Keep `insert_special_tokens` at its default (`True`): the bundle declares `<|startoftext|>` as the token the CLS position reads, and the engine inserts it — the runtime's tokenizer does not run the tokenizer's own post-processor, so turning the option off silently returns wrong vectors.

Python (`pip install litert-lm>=0.17.0`):

```python
import litert_lm
from litert_lm.embedding_engine import EmbeddingEngine, EmbeddingOptions

engine = EmbeddingEngine("LFM2.5-Embedding-350M_wi8fc.litertlm", backend=litert_lm.Backend.CPU())
vec = engine.compute_embedding("query: What is the tallest mountain in Japan?").embedding   # 1024 floats, L2-normalized
batch = engine.compute_embedding_batch(["document: first text", "document: second text"])                  # list of responses
```

Use the model's prefixes as plain text (`query: ` for queries, `document: ` for passages). Inputs longer than 512 tokens are an error by default; pass `EmbeddingOptions(input_overflow_strategy=InputOverflowStrategy.TRUNCATE)` or `CHUNK_AND_AVERAGE` to choose. `EmbeddingOptions(output_size=256)` keeps the first 256 dimensions.

Kotlin (`com.google.ai.edge.litertlm:litertlm-android:0.17.0`, needs a Kotlin 2.4 project):

```kotlin
val engine = EmbeddingEngine(EmbeddingEngineConfig(modelPath = "/data/local/tmp/LFM2.5-Embedding-350M_wi8fc.litertlm", backend = Backend.CPU()))
engine.initialize()
val vec = engine.computeEmbedding(listOf(InputData.Text("query: What is the tallest mountain in Japan?"))).embedding
engine.close()
```

Measured (CPU, single text, 10-text check set of 6–70 tokens, median):

| device | runtime | init | per text |
|---|---|---|---|
| Galaxy S26 (SM-S942Q, Android 16) | litertlm-android 0.17.0, Kotlin `EmbeddingEngine` | 1.86 s | 22–33 ms |
| Mac (M4 Max) | litert-lm 0.17.0, Python | 0.3 s | 19 ms (wi8fc) / 28 ms (fp16) |

## Quality

Measured against the PyTorch fp32 reference (`Lfm2BidirectionalModel` + CLS + normalize) on the same inputs. fp16 is bitwise identical to the reference on every task metric below.

| Variant | STS17 Spearman (11 pairs) | NanoSciFact nDCG@10 | recall@5 | hit@1 |
|---|---|---|---|---|
| PyTorch fp32 (reference) | 0.6720 | 0.8540 | 0.920 | 0.780 |
| fp16 | 0.6720 | 0.8540 | 0.920 | 0.780 |
| int8 (wi8fc) | 0.6721 | 0.8494 | 0.900 | 0.780 |

int8 costs 0.005 nDCG@10 and is a rounding difference on STS17. Per-vector agreement with the reference is cosine 0.9945–0.9955 for int8 and ≥0.9999999 for fp16.

Graph mechanics on the shipped artifacts, all three variants: cross-signature max\|diff\| **0.0** at 64/128/256/512, pad-content invariance **0.0** (garbage in the padded region cannot move the vector), and a live `attention_mask` (shortening it moves the output by 4.8e-02).

## Speed

Apple-silicon Mac, XNNPACK, 16 threads, 20 iterations after warmup:

| Variant | embed_64 | embed_128 | embed_256 | embed_512 |
|---|---|---|---|---|
| int8 (wi8fc) | 31.7 ms | 45.7 ms | 73.6 ms | 123.0 ms (4164 tok/s) |
| fp16 | 55.5 ms | 74.1 ms | 108.2 ms | 200.8 ms |
| fp32 | 37.9 ms | 53.1 ms | 88.2 ms | 168.8 ms |

fp16 is *slower* than fp32 on CPU: XNNPACK unpacks fp16 weights to fp32 at run time, so the smaller file buys disk, not latency.

iPhone 17 Pro, XNNPACK, 6 threads (warm, after the first call on each signature):

| Variant | load+delegate | peak footprint | embed_128 | embed_512 | vs Mac |
|---|---|---|---|---|---|
| int8 (wi8fc) | 1.02 s | **1245 MiB** | 40–44 ms | 137–142 ms | cosine 1.000000, **max diff 0.0** |
| fp16 | 1.50 s | **5799 MiB** | 73–98 ms | 256–409 ms | cosine 1.000000, max diff 2e-07 |

The int8 model reproduces the Mac outputs **bit-exactly** on device across all tested cases (en/ja/de/ar/hi, short and long, both prompt forms). The fp16 model does run on an iPhone 17 Pro, but its 5.8 GiB peak is a function of that device's memory — treat fp16 as the desktop artifact. Its first invocation on each signature costs 355–538 ms of one-time XNNPACK fp16→fp32 unpacking, excluded from the warm figures above.

### GPU (2026-08-13 re-export)

The re-export respells the one idiom mobile GPU delegates refuse — transformers' rank-5 `repeat_kv` expand — into an equivalent rank-4 matmul (outputs bitwise-identical on CPU), and the int8 file now fully delegates on mobile GPUs. Measured with the LiteRT CompiledModel API (fp32 GPU precision, real inputs, best of 3 warm runs): Pixel 8a OpenCL `embed_512` **20.1 ms**, cosine **0.9992** vs the fp32 desktop reference; iPhone 17 Pro Metal `embed_512` 171–194 ms (eight fixture cases, cosine ≥ 0.9995). Set the GPU precision to **fp32** — at fp16 GPU precision this family's norm reductions overflow and every output is NaN; CompiledModel timings are not comparable to classic-delegate `benchmark_model` timings.

## Snapdragon NPU (Hexagon)

- `LFM2.5-Embedding-350M_fp16.tflite` — the NPU runs it at 182.6 ms. The GPU does not — `LiteRtException: Failed to compile model`.
- `LFM2.5-Embedding-350M_wi8fc.tflite` — the GPU runs it at 81.10 ms. The NPU does not — `LiteRtException: Failed to compile model`.

| file | backend | compiled | inference (median / min) | load |
|---|---|---|---:|---:|
| `LFM2.5-Embedding-350M_fp16.tflite` | NPU (Hexagon v81) | AOT (SM8850) | 182.6 ms / 175.9 ms | 923 ms |
| `LFM2.5-Embedding-350M_wi8fc.tflite` | GPU (Adreno) | — | 81.10 ms / 80.12 ms | 16097 ms |

Measured on a **Samsung Galaxy S26** (Snapdragon 8 Elite Gen 5 / SM8850, Hexagon v81, Android 16) with LiteRT `CompiledModel` 2.2.0, one accelerator per process, 5 warm-up runs then N=50 timed runs, median reported. Every run held thermal status `NONE` throughout. Headroom 0.75–0.78, where 1.0 is the throttling threshold.

The NPU row marked *AOT* ran an artifact compiled ahead of time for SM8850 (ai-edge-litert 2.2.0 + QAIRT 2.47.0), not the published file. That artifact is not distributed here; the compile is one command in the [NPU guide](https://github.com/john-rocky/hf-to-litertlm/blob/main/docs/android-npu.md).

GPU wiring: [GPU guide](https://github.com/john-rocky/hf-to-litertlm/blob/main/docs/android-gpu.md).

## Usage (Python)

```python
import numpy as np
from ai_edge_litert.interpreter import Interpreter
from tokenizers import Tokenizer

tok = Tokenizer.from_file("tokenizer.json")
it = Interpreter(model_path="LFM2.5-Embedding-350M_wi8fc.tflite")
embed = it.get_signature_runner("embed_128")

def encode(text, prompt):           # prompt = "query: " or "document: "
    ids = tok.encode(prompt + text).ids[:128]
    x = np.zeros((1, 128), np.int32)
    m = np.zeros((1, 128), np.int32)
    x[0, :len(ids)] = ids
    m[0, :len(ids)] = 1
    return list(embed(input_ids=x, attention_mask=m).values())[0][0]  # [1024]

q = encode("What is the capital of France?", "query: ")
d = encode("Paris is the capital and largest city of France.", "document: ")
print(float(q @ d))                 # already normalized -> dot product is cosine
```

On Android/iOS use the LiteRT runtime's SignatureRunner APIs with the same signature names; the tokenizer is the standard Hugging Face `tokenizer.json` (works with the `tokenizers` libraries for Rust/Swift/Kotlin).

## License

LFM Open License v1.0 (see `LICENSE`, unchanged from the base model). Note the license's commercial-use threshold (Section 5). This repository redistributes converted **Derivative Works** of LiquidAI/LFM2.5-Embedding-350M with modification notices per Section 4; all credit for the model to [Liquid AI](https://www.liquid.ai/).
