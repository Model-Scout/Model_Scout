---
base_model: mistralai/Devstral-Small-2-24B-Instruct-2512
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
language:
  - en
  - fr
  - de
  - es
  - pt
  - it
  - ja
  - ko
  - ru
  - zh
tags:
  - devstral
  - mistral3
  - ministral3
  - fp8
  - quantized
  - vllm
  - DGX-Spark
  - GB10
  - coding
  - swe-agent
  - mirror
---

# gdubicki/Devstral-Small-2-24B-Instruct-2512-FP8

**Public mirror of [`mistralai/Devstral-Small-2-24B-Instruct-2512`](https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512)** — Mistral's official FP8 checkpoint.

This mirror exists to provide a pinned, stable reference for deployment on DGX Spark (GB10). Use the upstream repo if you want to track author updates.

## Credits

- Base model: [`mistralai/Devstral-Small-2-24B-Instruct-2512`](https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512) by Mistral AI
- FP8 quantization: by Mistral AI (official release; `quant_method: fp8` in config.json)
- License: **Apache-2.0** (inherited)

## Why FP8 (not NVFP4) on GB10

- GB10 Blackwell (SM12.1) has **native FP8 tensor cores** — FP8 GEMM is compute-native
- NVFP4 on GB10 runs as W4A16 via Marlin (no CUTLASS FP4 kernel)
- Mistral ships official FP8 in this repo → no custom quantization needed
- Trade-off vs NVFP4: ~25 GB vs ~12 GB weights; decode ~30% slower (memory-bound)

## Model details

- Architecture: `Mistral3ForConditionalGeneration` (multimodal: text + Pixtral vision)
- Text backbone: `ministral3`, 40 layers dense, 24B params
- Vision: Pixtral ViT, 24 layers (image-aware; ignored for pure-text usage)
- Quantization: FP8 (per-tensor, static activation scheme)
- Kept in BF16: `vision_tower`, `multi_modal_projector`, `lm_head`
- Max context: 393,216 tokens (YaRN scaling)
- SWE-bench Verified: ~55-58% (state-of-art for 24B open-weights SWE agents at release)

## Usage

```bash
docker run --rm --runtime=nvidia --gpus all \
  -p 8000:8000 \
  -v ~/.cache/huggingface:/root/.cache/huggingface \
  vllm/vllm-openai:cu130-nightly \
  gdubicki/Devstral-Small-2-24B-Instruct-2512-FP8 \
  --dtype auto \
  --kv-cache-dtype fp8 \
  --gpu-memory-utilization 0.30 \
  --max-model-len 131072 \
  --tool-call-parser mistral \
  --enable-auto-tool-choice \
  --enable-chunked-prefill \
  --enable-prefix-caching
```

## Agentic / SWE use case

Devstral is tuned for **agentic coding workflows** (multi-file edits, tool use, long SWE trajectories) — not raw code-gen from prompt. Pair with Cline / aider / OpenHands.
