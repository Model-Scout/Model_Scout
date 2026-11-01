---
language:
  - en
  - zh
  - de
  - fr
  - ja
  - ko
  - ar
  - es
  - pt
  - ru
  - it
  - nl
  - pl
  - tr
  - vi
  - th
  - id
  - hi
tags:
  - gguf
  - mxfp4
  - moe
  - qwen3.6
  - 35b
  - no-mtp
  - quantized
inference: false
pipeline_tag: text-generation
base_model: Qwen/Qwen3.6-35B-A3B
---

# Qwen3.6-35B-A3B MXFP4_MoE No-MTP GGUF

## Base Model

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)** by Alibaba Qwen Team — a 35B-parameter Mixture-of-Experts (MoE) model with only 3B active parameters per token. Apache 2.0 licensed. Supports 131K+ context, tool use, and multilingual tasks across 100+ languages.

## Why No MTP?

Qwen3.6-35B-A3B ships with Multi-Token Prediction (MTP) heads for speculative decoding. On MoE models, MTP heads waste ~1-2 GB of VRAM with no measurable speed benefit — the bottleneck is expert routing through system RAM (when using `--cpu-moe`), not draft token verification. This build strips the MTP heads with `--no-mtp` to reclaim that VRAM for expert weights and KV cache, resulting in better performance on 16GB cards.

## Quantization

- **Format:** MXFP4_MoE — OCP microscaled FP4 (E2M1 values with E8M0 power-of-two scaling per 32 values) for routed expert weights; Q8_0 for all non-expert tensors (attention, embeddings, shared FFN, norms)
- **BPW:** 4.57 bits per weight
- **Size:** 19.8 GB
- **Portable:** MXFP4 works on any hardware with FP4 support (not Blackwell-only like NVFP4)

## Tested Settings (llama.cpp build 1324+, RTX 5060 Ti 16GB)

```
llama-cli -m qwen3.6-35b-a3b-mxfp4-moe-nomtp.gguf \
  -ngl 99 --cpu-moe \
  --ctx-size 131072 \
  --flash-attn on \
  --cache-type-k q8_0 --cache-type-v q8_0 \
  -t 8 --temp 0.7 --top-k 20 --top-p 0.95
```

### Performance Results

| Metric | Result |
|--------|--------|
| Prompt processing | 23.7 t/s |
| Token generation | 30.3 t/s |
| Context | 128K |
| KV Cache | Q8_0 |
| Test prompt | "Tell me about superposition and quantum computing" |
| Output quality | Coherent, thorough, no hallucination, no repetition |

## Usage

### llama.cpp CLI (text generation)
```bash
llama-cli -m qwen3.6-35b-a3b-mxfp4-moe-nomtp.gguf   -ngl 99 --cpu-moe   -c 131072   --flash-attn on   --cache-type-k q8_0 --cache-type-v q8_0   -p "Your prompt here"
```

### llama.cpp Server (API)
```bash
llama-server -m qwen3.6-35b-a3b-mxfp4-moe-nomtp.gguf   -ngl 99 --cpu-moe   -c 131072   --flash-attn on   --cache-type-k q8_0 --cache-type-v q8_0   --host 0.0.0.0 --port 8080
```

## Requirements

- llama.cpp build 700+ with CUDA support
- NVIDIA GPU with 16GB+ VRAM (tested on RTX 5060 Ti 16GB)
- `--cpu-moe` flag required — routes MoE expert weights to system RAM while keeping attention on GPU
- `--allow-requantize` used during quantization for mixed-precision output
- `--flash-attn on` recommended for memory efficiency at long context

## Notes

- MXFP4_MoE keeps expert weights at MXFP4 while non-expert tensors (attention, shared FFN, embeddings) stay at higher Q8_0 precision — better quality on always-active parameters
- Model uses `--cpu-moe` because total weights (~19.8 GB) exceed 16GB VRAM; experts stream from RAM
- Slightly faster than NVFP4 variant (30.3 vs 29.1 t/s gen) due to better MXFP4 decode paths on Blackwell
- For NVFP4 variant (all weights NVFP4, Blackwell-only), see [NVFP4 repo](https://huggingface.co/FreedomAISVR/Qwen3.6-35B-A3B-NVFP4-NoMTP-GGUF)

## License

Apache 2.0 (inherited from base model)
