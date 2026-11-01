---
language:
- ko
- en
- ja
license: gemma
library_name: gguf
pipeline_tag: translation
base_model: xiaomi-research/MiLMMT-46-1B-v0.1
base_model_relation: quantized
tags:
- gguf
- llama.cpp
- quantized
- translation
- korean
- japanese
---

# Model Description

This repository provides an unofficial GGUF derivative of
[`xiaomi-research/MiLMMT-46-1B-v0.1`](https://huggingface.co/xiaomi-research/MiLMMT-46-1B-v0.1)
for local Korean, English, and Japanese translation.

The model was not fine-tuned. It was produced by retaining a 130k-token
ko/en/ja-focused vocabulary, applying importance-matrix calibration, and using
a mixed quantization policy: `Q4_K_M` by default, with `Q8_0` retained for
`ffn_gate` and `ffn_up` tensors in transformer blocks 16–25.

- **File:** `milmmt-pruned-130k-bf16-imatrix-mix-late16-25-ffngateupq8-Q4_K_M.gguf`
- **Size:** 803,547,328 bytes (766.3 MiB / 0.748 GiB)
- **SHA-256:** `5f781fdc9a685212dba3244b7cf2df39625776066043408f769549195f018b0d`
- **Target languages:** Korean, English, Japanese
- **Intended runtime:** llama.cpp-compatible runtimes, including LLamaSharp

Against the local MiLMMT `Q8_0` baseline, this model achieved a 0.995182
average chrF++ ratio and a 0.991064 worst-direction ratio on the full
FLORES+ `dev` ko/en/ja evaluation. It also passed an independent 100-row
`devtest` check.

This is the current recommended low-VRAM balanced variant from this
experiment. It is not the absolute smallest evaluated GGUF, nor the
absolute highest-scoring variant; smaller candidates failed the held-out
quality gate, while the Q8_0 baseline is substantially larger.

Use the MiLMMT raw translation prompt format:

```text
Translate this from <source language> to <target language>:
<source language>: <text>
<target language>:
```
This model is intended for translation, not general chat or reliable use in
languages outside Korean, English, and Japanese. It is an independent
derivative and is not affiliated with or endorsed by Xiaomi or Google.

# Notice
Gemma is provided under and subject to the Gemma Terms of Use found at ai.google.dev/gemma/terms
