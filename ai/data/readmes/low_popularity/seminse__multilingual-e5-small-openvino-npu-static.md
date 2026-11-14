---
license: mit
base_model: intfloat/multilingual-e5-small
tags:
  - sentence-transformers
  - feature-extraction
  - sentence-similarity
  - openvino
  - intel-npu
  - intel-gpu
  - intel-cpu
  - multilingual
  - korean
language:
  - multilingual
pipeline_tag: feature-extraction
library_name: openvino
---

# multilingual-e5-small — OpenVINO IR (static `[1, 512]`)

Pre-exported [`intfloat/multilingual-e5-small`](https://huggingface.co/intfloat/multilingual-e5-small)
in OpenVINO IR format with **static input shape `[1, 512]`**.

A single `.xml` / `.bin` pair, **measured to compile and run on every
OpenVINO device a Core Ultra laptop exposes** — CPU, integrated GPU (Arc),
secondary GPU, and NPU (3720). The static reshape unlocks the NPU path,
but the same IR drops into CPU and GPU pipelines unchanged.

## TL;DR — full local agent on a single laptop

This embedder is one piece of a working all-local LLM-agent stack on a
**single consumer laptop** (Intel Core Ultra 9 + RTX 5070 Ti, 64 GB RAM):

| Silicon | Workload | Measured |
|---|---|---|
| **dGPU** (RTX 5070 Ti, 12 GB) | **Gemma 4 31B Q8_0 LLM** via `llama.cpp -ngl 18` | **20–27 s / tool call, 2.29 tok/s, 18.7 GB RAM free** |
| **NPU** (Intel 3720) | Embeddings (this model) — always-on agent memory | **29 ms / text @ ~1 W** |
| **iGPU** (Intel Arc) | Available — fastest raw embed (19 ms/text) if CPU/GPU are free | 19 ms / text |
| **CPU** | Orchestrator + FastAPI memory server + FAISS index + user's IDE/browser | (works) |

The headline isn't any single number — it's that **a 31-billion-parameter
LLM, an always-on multilingual embedder, persistent vector memory, and the
user's normal desktop work all run simultaneously on one laptop**, none of
them blocking each other, all entirely offline.

## Multi-device benchmark on a real laptop

Same `openvino_model.xml`, same input, mean of 50 runs after one warm-up.
Hardware: **Intel® Core™ Ultra 9** (NPU 3720 + Intel® Arc™ iGPU), Windows
11, **OpenVINO 2026.1.0**:

| Device | Latency / text | Throughput | Compile time | Best for |
|---|---:|---:|---:|---|
| **GPU.0** (Intel Arc iGPU) | **19.4 ms** | 51.6 /s | 4.2 s | Fastest raw speed; uses iGPU power. |
| **NPU** (Intel NPU 3720) | **29.1 ms** | 34.3 /s | 0.5 s | Best perf/watt (~1 W); leaves CPU + iGPU + dGPU free for the LLM and user work. |
| **CPU** | **49.0 ms** | 20.4 /s | 0.4 s | Universal fallback; no special hardware. |
| GPU.1 (secondary GPU) | 150.3 ms | 6.7 /s | 1.6 s | Available but slowest of the four. |

**You don't need an NPU to use this model.** A regular CPU-only PC runs
the same file at ~20 embeds/s — fast enough for most retrieval workloads.
NPU is the right pick when you want the embedder to **stay always-on
without contending with the GPU or CPU** (which, in the agent setup
above, are busy serving a 31 B LLM).

## Why this exists

The Intel NPU compiler (NPU 3720 and newer) **rejects dynamic input dims**
(`-1` in the shape). The default `optimum-intel` export keeps shapes
dynamic, which works fine on CPU and GPU but fails on NPU with `Got
negative shape dim bound: '-1'`. This repository is the same model already
reshaped to `[batch=1, seq_len=512]`, so a single IR is loadable on **NPU,
GPU, and CPU**.

## Files

- `openvino_model.xml` / `openvino_model.bin` — IR with static shape
- `tokenizer.json`, `tokenizer_config.json`, `special_tokens_map.json` — tokenizer
- `config.json` — model config

## Usage

The same code runs unchanged on NPU / GPU / CPU. The snippet auto-picks
the best device the laptop exposes:

```python
import numpy as np
import openvino as ov
from huggingface_hub import snapshot_download
from transformers import AutoTokenizer

REPO = "seminse/multilingual-e5-small-openvino-npu-static"
local_dir = snapshot_download(REPO)

tokenizer = AutoTokenizer.from_pretrained(local_dir)
core = ov.Core()
available = core.available_devices
device = "NPU" if "NPU" in available else ("GPU" if "GPU" in available else "CPU")
print(f"Using device: {device}")

ov_config = {"PERFORMANCE_HINT": "LATENCY"}
if device == "NPU":
    ov_config["NPU_TURBO"] = "YES"

model = core.read_model(f"{local_dir}/openvino_model.xml")
compiled = core.compile_model(model, device, ov_config)

def embed(text: str, prefix: str = "passage: ") -> np.ndarray:
    batch = tokenizer(prefix + text, padding="max_length", truncation=True,
                      max_length=512, return_tensors="np")
    feed = {k: v.astype(np.int64) for k, v in batch.items()
            if k in {"input_ids", "attention_mask", "token_type_ids"}}
    out = compiled(feed)
    last_hidden = next(iter(out.values()))
    mask = batch["attention_mask"][..., None].astype(np.float32)
    pooled = (last_hidden * mask).sum(1) / mask.sum(1).clip(1e-9)
    pooled /= np.linalg.norm(pooled, axis=-1, keepdims=True).clip(1e-9)
    return pooled[0].astype(np.float32)

vec = embed("Edge AI runs on the NPU.")
print(vec.shape)  # (384,)
```

## Why the NPU number matters even though the iGPU is faster

On a consumer laptop the silicon is *not* idle:

- **dGPU** is busy serving the LLM (31 B Q8 at 2.29 tok/s — that workload
  saturates VRAM and most of the GPU's compute).
- **iGPU** is doing rendering, video decode, Studio Effects, sometimes
  Stable-Diffusion-class workloads.
- **CPU** is running the orchestrator, FAISS, the IDE, the browser.

The **NPU is the only piece of silicon that is otherwise idle.** Putting
the embedder on it at ~1 W means the memory layer **does not contend**
with the LLM or the user's work. The price for that is +10 ms / embed vs
the iGPU — a fair trade when the alternative is the embedder fighting the
LLM for GPU time.

## Properties preserved from base model

- 117 M parameters
- 384-dim output
- 100+ languages (Korean, Japanese, Chinese, German, French, ...)
- L2-normalized embeddings (after mean pooling)
- Use `passage: ` prefix for documents and `query: ` for queries

## Where this is useful

- **Always-on agent memory** (the original motivation): NPU runs the
  embedder at ~1 W while the dGPU runs a local 31 B LLM, with measured
  zero contention between them.
- **Plain on-device search on a regular PC**: no NPU required. CPU →
  20 embeds/s, Intel iGPU → 50+ embeds/s. Same file, same code.
- **Foundation for local retrieval-augmented LLM agents** running entirely
  on-device with no cloud round-trip.

## Companion notebook

A full walkthrough — export, static reshape, compile across CPU / GPU /
NPU, latency benchmark, multilingual FAISS demo — is being submitted to
the official OpenVINO Notebooks repo:
[`openvinotoolkit/openvino_notebooks#3425`](https://github.com/openvinotoolkit/openvino_notebooks/pull/3425).

## License

MIT (inherited from the base model).
