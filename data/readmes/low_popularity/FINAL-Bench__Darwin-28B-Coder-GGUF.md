---
license: apache-2.0
base_model: FINAL-Bench/Darwin-28B-Coder
base_model_relation: quantized
library_name: gguf
pipeline_tag: text-generation
tags:
- gguf
- llama.cpp
- mtp
- multi-token-prediction
- speculative-decoding
- code
language:
- en
- ko
---

> ### 📱 Run it on your phone or a GPU-less PC → **POCKET**  ·  🚀 **[Try it live (CPU chat)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU)**
> VIDRAFT's on-device family: a 35B model that runs on **iPhone** and on **CPU with no GPU** — stock `llama.cpp`, no fork.
>
> [![Live demo](https://img.shields.io/badge/🤗_Space-POCKET_CPU_chat-ffce3a)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU) [![Collection](https://img.shields.io/badge/📚-POCKET_collection-5dbf9a)](https://huggingface.co/collections/FINAL-Bench/pocket-models-6a618ee5d23eafb7e185a5c6) [![35B](https://img.shields.io/badge/POCKET--35B-GGUF-243456)](https://huggingface.co/FINAL-Bench/POCKET-35B-GGUF) [![KR MLX](https://img.shields.io/badge/POCKET--KR-iPhone-0f6e56)](https://huggingface.co/FINAL-Bench/POCKET-KR-MLX) [![EN](https://img.shields.io/badge/POCKET--EN-GGUF-185fa5)](https://huggingface.co/FINAL-Bench/POCKET-EN-GGUF)

>


# Darwin-28B-Coder — GGUF (MTP-enabled)

GGUF builds of [**FINAL-Bench/Darwin-28B-Coder**](https://huggingface.co/FINAL-Bench/Darwin-28B-Coder) with the native **Multi-Token Prediction (MTP)** head preserved, for **self-speculative decoding in llama.cpp**.

Requested in the [base model discussion](https://huggingface.co/FINAL-Bench/Darwin-28B-Coder/discussions/1).

## Files

| File | Quant | Size | Notes |
|------|-------|------|-------|
| `Darwin-28B-Coder-Q4_K_M.gguf` | Q4_K_M | 16.8 GB | recommended for most GPUs |
| `Darwin-28B-Coder-Q8_0.gguf` | Q8_0 | 29.0 GB | near-lossless |
| `Darwin-28B-Coder-F16.gguf` | F16 | 54.7 GB | full precision |

All files include the MTP layer — verified in metadata:
`general.architecture = qwen35`, `qwen35.nextn_predict_layers = 1`, tensors `blk.64.nextn.*`.

## Multi-Token Prediction (MTP)

This model ships with a trained MTP head (1 prediction layer). With a recent **llama.cpp** build that includes MTP support (merged in [PR #22673](https://github.com/ggml-org/llama.cpp/pull/22673)), the `nextn` layer is used for **self-speculative decoding** — typically **~1.5–2× faster generation with identical output** (the main model verifies every drafted token, so quality is unchanged).

> A standard (non-MTP) GGUF does **not** contain the prediction head — you need these MTP-enabled files to benefit from the speedup.

## Usage

```bash
# 1) Build a recent llama.cpp (MTP support is in mainline since PR #22673)
git clone https://github.com/ggml-org/llama.cpp && cd llama.cpp
cmake -B build -DGGML_CUDA=ON && cmake --build build -j --config Release

# 2) Run — the nextn (MTP) layer enables self-speculative decoding
./build/bin/llama-cli \
  -m Darwin-28B-Coder-Q4_K_M.gguf \
  -ngl 99 -c 8192 \
  -p "Write a quicksort in Python."
```

For the exact MTP/speculative flags and the latest behaviour, see the llama.cpp MTP documentation / PR #22673. Works with `llama-cli` and `llama-server`.

## Model spec (public)

| | |
|---|---|
| Architecture | `qwen35` (hybrid attention) |
| Layers | 64 + 1 MTP |
| Hidden size | 5120 |
| Attention heads | 24 (KV 4) |
| Context length | 262,144 |
| Vocab | 248,320 |
| Precision (source) | bfloat16 |

## License & attribution

License and usage follow the base model [FINAL-Bench/Darwin-28B-Coder](https://huggingface.co/FINAL-Bench/Darwin-28B-Coder). These are GGUF conversions only; refer to the base model card for model details, intended use, and limitations.

GGUF conversion + quantization by the FINAL-Bench team using `llama.cpp/convert_hf_to_gguf.py`.

## Learn more
- Running large coding models on-device without a GPU: [Can you run a large LLM without a GPU?](https://vidraft.net/insights/on-device-llm-without-gpu.html)
- What model quantization is: [What is model quantization?](https://vidraft.net/insights/what-is-quantization-llm.html)
