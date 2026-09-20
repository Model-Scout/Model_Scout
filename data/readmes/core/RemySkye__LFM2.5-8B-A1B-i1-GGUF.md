---
license: other
license_name: lfm1.0
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
- pt
pipeline_tag: text-generation
tags:
- liquid
- lfm2.5
- edge
- gguf
- llama
- text-generation
base_model:
- LiquidAI/LFM2.5-8B-A1B
---

# LFM2.5-8B-A1B-i1-GGUF

This repository contains GGUF format quantizations of the model LiquidAI/LFM2.5-8B-A1B. These models were generated using llama.cpp with an importance matrix (imatrix) - https://gist.github.com/bartowski1182/82ae9b520227f57d79ba04add13d0d0d

Used this pull request to be able to quantize: https://github.com/ggml-org/llama.cpp/pull/23826/
Should work with the latest llama.cpp

# NOTE
Quantization below 4 bits may result in unacceptably low quality.