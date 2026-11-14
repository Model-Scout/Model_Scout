---
base_model: tencent/Hy-MT2-30B-A3B
pipeline_tag: text-generation
library_name: llama.cpp
tags:
  - gguf
  - llama.cpp
  - quantized
  - translation
  - hy-mt2
  - hy-v3
  - moe
language:
  - zh
  - en
  - fr
  - pt
  - es
  - ja
  - tr
  - ru
  - ar
  - ko
  - th
  - it
  - de
  - vi
  - ms
  - id
  - tl
  - hi
  - pl
  - cs
  - nl
  - km
  - my
  - fa
  - gu
  - ur
  - te
  - mr
  - he
  - bn
  - ta
  - uk
  - bo
  - kk
  - mn
  - ug
---

# Hy-MT2-30B-A3B 4bit GGUF

GGUF quantizations of `tencent/Hy-MT2-30B-A3B`, with `Q4_K_M` as the
recommended 4bit deployment file.

## Files

| File | Size | Notes |
|---|---:|---|
| `Hy-MT2-30B-A3B-Q2_K.gguf` | 10.30 GiB | smallest test build |
| `Hy-MT2-30B-A3B-Q3_K_M.gguf` | 13.45 GiB | lower VRAM option |
| `Hy-MT2-30B-A3B-Q4_K_M.gguf` | 16.98 GiB | recommended default |
| `Hy-MT2-30B-A3B-BF16.gguf` | 56.03 GiB | conversion source |
| `patches/llama-cpp-hyv3.patch` | 17 KiB | required when upstream llama.cpp has no HYV3 support |

## Important

Current upstream `llama.cpp` may not support `HYV3ForCausalLM` / `model_type=hy_v3`
directly. This repository includes the required patch at:

```text
patches/llama-cpp-hyv3.patch
```

Clone this model repository first, then prepare a patched `llama.cpp` checkout:

```bash
git lfs install
git clone https://huggingface.co/GrahLnn/Hy-MT2-30B-A3B-4bit-GGUF
cd Hy-MT2-30B-A3B-4bit-GGUF
bash scripts/prepare_llama_cpp.sh ./llama.cpp
```

For CUDA 13.1 builds:

```bash
CUDA_HOME=/usr/local/cuda-13.1 bash scripts/prepare_llama_cpp.sh ./llama.cpp
```

## Run Q4 Server

```bash
cd Hy-MT2-30B-A3B-4bit-GGUF
CUDA_VISIBLE_DEVICES=0 bash scripts/run_q4_server.sh
```

The script runs:

```bash
./llama.cpp/build-hyv3-cuda/bin/llama-server \
  -m Hy-MT2-30B-A3B-Q4_K_M.gguf \
  -ngl all \
  --host 127.0.0.1 \
  --port 8080
```

## Test Translation

```bash
bash scripts/test_translation.sh
```

Expected style:

```text
The weather is really nice today.
```

Use stop strings when serving through the OpenAI-compatible endpoint:

```json
["<eos:6124c78e>", "<｜hy_User｜>", "<｜hy_Assistant｜>"]
```

## Measured Local Runtime

Test machine: RTX 4090, WSL CUDA, patched `llama.cpp`.

| Quant | GPU model buffer | Notes |
|---|---:|---|
| Q2_K | 10465.90 MiB | 49/49 layers offloaded |
| Q3_K_M | 13670.82 MiB | 49/49 layers offloaded |
| Q4_K_M | 17254.26 MiB | 49/49 layers offloaded |

For Q4 server translation tests after warmup, generation was typically around
`195-206 tok/s` on the local 4090 setup. Actual speed depends on prompt length,
context size, batch settings, and build options.

## Tested Cases

The Q4 server path was tested with:

- normal Chinese to English translation
- mixed Chinese/English/Japanese text
- code and function names
- Markdown lists and tables
- XML tags
- JSON-like text
- logs, shell commands, and Windows/WSL paths

Structure-heavy prompts should explicitly ask the model to preserve structure,
keys, tags, and newlines.

## License

This repository contains quantized derivatives of `tencent/Hy-MT2-30B-A3B`.
Follow the upstream model license and usage terms.
