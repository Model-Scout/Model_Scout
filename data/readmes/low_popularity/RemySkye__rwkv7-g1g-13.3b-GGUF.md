---
license: apache-2.0
language:
  - en
  - zh
  - fr
  - es
  - de
  - pt
  - ru
  - it
  - ja
  - ko
  - vi
  - ar
tags:
- text-generation
- causal-lm
- rwkv
- gguf
- llama.cpp
- lmstudio
base_model: BlinkDL/rwkv7-g1
pipeline_tag: text-generation
---

# RWKV7-G1G 13.3B - GGUF Quantizations

GGUF conversions of [BlinkDL/rwkv7-g1g-13.3b](https://huggingface.co/BlinkDL/rwkv7-g1) (Apache 2.0)  
for use with [llama.cpp](https://github.com/ggml-org/llama.cpp), LM Studio, and other GGUF-compatible runtimes.

All quants converted from **BF16 base** for maximum lossless quality.  
**Static quantizations** — no importance matrix (imatrix) was used.
Check out this for imatrix quantizations: [RemySkye/rwkv7-g1g-13.3b-i1-GGUF](https://huggingface.co/RemySkye/rwkv7-g1g-13.3b-i1-GGUF)

*S/M/L K-quant variants had **no effect on size** for RWKV architecture — only `_M` variants are included.*

See [UncheatableEval](https://huggingface.co/spaces/Jellyfish042/UncheatableEval) for benchmarks.

> **Note:** Q3_K_M, and Q2_K were tested but produced completely unintelligible / broken output without an importance matrix. For lower BPW quantizations (below ~4.5 BPW), an imatrix would be required — these quants currently use **no imatrix** at all. Stick to Q4_K_M or higher for usable results.