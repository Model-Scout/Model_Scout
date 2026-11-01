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

# RWKV7-G1G 7.2B - GGUF Quantizations

GGUF conversions of [BlinkDL/rwkv7-g1g-7.2b](https://huggingface.co/BlinkDL/rwkv7-g1) (Apache 2.0)  
for use with [llama.cpp](https://github.com/ggml-org/llama.cpp), LM Studio, and other GGUF-compatible runtimes.

All quants converted from **BF16 base** for maximum lossless quality.
Used imatrix generated with https://gist.github.com/bartowski1182/82ae9b520227f57d79ba04add13d0d0d

See [UncheatableEval](https://huggingface.co/spaces/Jellyfish042/UncheatableEval) for benchmarks.