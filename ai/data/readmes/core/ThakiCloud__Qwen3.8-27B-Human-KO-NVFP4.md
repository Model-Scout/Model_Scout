---
license: apache-2.0
base_model: ThakiCloud/Qwen3.8-27B-Human-KO
language:
- ko
pipeline_tag: text-generation
tags:
- korean
- style-alignment
- nvfp4
- quantized
- compressed-tensors
- qwen
base_model_relation: quantized
library_name: transformers
---

# Qwen3.8-27B-Human-KO-NVFP4

This is the **NVFP4 (W4A4) quantized version** of
[ThakiCloud/Qwen3.8-27B-Human-KO](https://huggingface.co/ThakiCloud/Qwen3.8-27B-Human-KO).
Quantized with llm-compressor GPTQ, in compressed-tensors format so vLLM recognizes it
automatically. Targets Blackwell's (SM100+) native FP4 kernels; weights shrink to about
15GB, serving **256k context on a single B200** (native window 262,144) with generous KV
headroom.

## What this checkpoint preserves (measured 2026-09-02, paired comparison against the bf16 original)

| Axis | bf16 original | NVFP4 (this model) | Verdict |
|---|---|---|---|
| T=0 anchor response | short polite-register short answers | **identical output** | style survives |
| Free-generation bullet-list rate (n=200) | 2.0% | **2.0%** | Same |
| Free-generation median length | 220 characters | 249 characters | Similar |
| KMMLU (same items, n=500) | — | Δ−2.4pp, z=1.09 | **not distinguishable** |
| HAE-RAE (same items, n=199) | — | Δ+4.9pp, z=0.41 | **not distinguishable** |

Measured serving (1x B200, vLLM 0.28, gpu-mem-util 0.90): KV cache **2,143,277 tokens**,
maximum concurrency **8.18x** at a 262,144-token request size.

Honest caveats:

- "Not distinguishable" is not "no loss." With this sample (n=500/199), a fine-grained
  loss on the order of 1-2pp is below the detection limit.
- The median-length shift 220→249 characters is a directional observation and has not
  gone through a sample-spread significance test.
- Quantization rebuild spread (the difference between running the same recipe twice) has
  not been separately measured.
- All of the original model's caveats (judge uncalibrated, safety inherited as-is from
  base, etc.) are inherited in full.

## Usage

```python
from vllm import LLM
llm = LLM(model="ThakiCloud/Qwen3.8-27B-Human-KO-NVFP4",
          max_model_len=262144, trust_remote_code=True)
```

NVFP4 kernels run on SM100+ (B200, etc.). On architectures below that, the model may
fail to load or run much slower on a fallback kernel. If you need the bf16 original, use
the base_model repo.

## License

Apache-2.0 (same as the original). NOTICE and DATA_PROVENANCE.md carry the same content
as the original repo.

## Paper

Off-Target Effects of Response-Style Alignment in a Korean 27B Language Model — [arXiv:2609.11291](https://arxiv.org/abs/2609.11291)

The style alignment behind this line also moved two behaviors nobody trained for: abstention on ambiguous social questions (KoBBQ) and unprompted disclosure in securities guidance. Both moved through the **emission policy** — how often the model answers and how much it says — rather than through what it says when it does answer. Holding prompts, recipe, data volume and serving fixed and changing only the training target, three style seeds moved answer rate one way and three neutral seeds moved it the other (observed ranges do not overlap). Read this card's numbers with that in mind.
