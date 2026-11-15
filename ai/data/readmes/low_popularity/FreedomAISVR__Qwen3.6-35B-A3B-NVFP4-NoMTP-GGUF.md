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
  - uk
  - cs
  - sv
  - da
  - fi
  - no
  - hu
  - ro
  - bg
  - hr
  - sk
  - sl
  - et
  - lv
  - lt
  - el
  - he
  - fa
  - ms
  - bn
  - ta
  - te
  - ur
  - sw
  - am
  - yo
  - ig
  - zu
  - af
  - sq
  - hy
  - az
  - eu
  - be
  - bs
  - ca
  - cy
  - eo
  - gl
  - ka
  - gu
  - ha
  - is
  - ga
  - jv
  - kn
  - kk
  - km
  - ky
  - lo
  - la
  - mk
  - mt
  - mi
  - mr
  - mn
  - ne
  - my
  - ps
  - pa
  - sq
  - sr
  - su
  - tl
  - tg
  - tt
  - tk
  - uz
  - wo
  - xh
  - yi
  - yo
  - zh
tags:
  - gguf
  - nvfp4
  - moe
  - qwen3.6
  - 35b
  - no-mtp
  - quantized
inference: false
pipeline_tag: text-generation
base_model: Qwen/Qwen3.6-35B-A3B
---

# Qwen3.6-35B-A3B NVFP4 No-MTP GGUF

## Base Model

**[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)** by Alibaba Qwen Team — a 35B-parameter Mixture-of-Experts (MoE) model with only 3B active parameters per token. Apache 2.0 licensed. Supports 131K+ context, tool use, and multilingual tasks across 100+ languages.

## Why No MTP?

Qwen3.6-35B-A3B ships with Multi-Token Prediction (MTP) heads for speculative decoding. However, on MoE models like this one, MTP heads waste ~1-2 GB of VRAM with no measurable speed benefit — the bottleneck is expert routing through system RAM (when using `--cpu-moe`), not draft token verification. This build strips the MTP heads with `--no-mtp` to reclaim that VRAM for the KV cache and expert weights, resulting in better performance on 16GB cards.

## Quantization

- **Format:** NVIDIA FP4 (NVFP4) — 4-bit E2M1 values with E4M3 scaling per 16 values + FP32 tensor scale
- **BPW:** 4.55 bits per weight
- **Size:** 19.7 GB
- **Target hardware:** NVIDIA Blackwell GPUs (RTX 50 series) — requires CUDA kernels at inference

## Tested Settings (llama.cpp build 1324+, RTX 5060 Ti 16GB)

```
llama-cli -m qwen3.6-35b-a3b-nvfp4-nomtp.gguf \
  -ngl 99 --cpu-moe \
  --ctx-size 131072 \
  --flash-attn on \
  --cache-type-k q8_0 --cache-type-v q8_0 \
  -t 8 --temp 0.7 --top-k 20 --top-p 0.95
```

### Performance Results

| Metric | Result |
|--------|--------|
| Prompt processing | 22.9 t/s |
| Token generation | 29.1 t/s |
| Context | 128K |
| KV Cache | Q8_0 |
| Test prompt | "Tell me about superposition and quantum computing" |
| Output quality | Coherent, thorough, no hallucination, no repetition |

## Usage

### llama.cpp CLI (text generation)
```bash
llama-cli -m qwen3.6-35b-a3b-nvfp4-nomtp.gguf   -ngl 99 --cpu-moe   -c 131072   --flash-attn on   --cache-type-k q8_0 --cache-type-v q8_0   -p "Your prompt here"
```

### llama.cpp Server (API)
```bash
llama-server -m qwen3.6-35b-a3b-nvfp4-nomtp.gguf   -ngl 99 --cpu-moe   -c 131072   --flash-attn on   --cache-type-k q8_0 --cache-type-v q8_0   --host 0.0.0.0 --port 8080
```

## Requirements

- llama.cpp build 700+ with CUDA support
- NVIDIA GPU with 16GB+ VRAM (tested on RTX 5060 Ti 16GB)
- `--cpu-moe` flag required — routes MoE expert weights to system RAM while keeping attention on GPU
- `--flash-attn on` recommended for memory efficiency at long context

## Notes

- Q8_0 KV cache recommended for quality — Q4_0 saves ~3 GB VRAM but loses precision
- Model uses `--cpu-moe` because NVFP4 weights (~19.7 GB) exceed 16GB VRAM; experts stream from RAM at ~611 MB per token
- For MXFP4_MoE variant (expert weights MXFP4, non-expert Q8_0), see [MXFP4_MoE repo](https://huggingface.co/FreedomAISVR/Qwen3.6-35B-A3B-MXFP4-MOE-NoMTP-GGUF)

## License

Apache 2.0 (inherited from base model)
