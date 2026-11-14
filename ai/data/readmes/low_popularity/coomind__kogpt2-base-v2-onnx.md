---
language: ko
license: cc-by-nc-sa-4.0
library_name: transformers.js
base_model: skt/kogpt2-base-v2
pipeline_tag: text-generation
tags:
- gpt2
- onnx
---

# KoGPT2 (skt/kogpt2-base-v2) — ONNX q8 for Transformers.js

This is an ONNX export of **[skt/kogpt2-base-v2](https://huggingface.co/skt/kogpt2-base-v2)** by **SK Telecom**
([SKT-AI/KoGPT2](https://github.com/SKT-AI/KoGPT2)), dynamically quantized to 8 bits so it can run in a web browser
with [Transformers.js](https://github.com/huggingface/transformers.js).

- Changes: ONNX export (with past key values) via Hugging Face Optimum, 8-bit dynamic quantization (ONNX Runtime),
  added `tokenizer_config.json` (special tokens as documented in the original README), removed the sampling default
  from `config.json` (`generation_config.json` uses greedy decoding). Weights are otherwise unchanged.
- License: **CC BY-NC-SA 4.0**, same as the original model. Non-commercial use only. Attribution: SK Telecom, KoGPT2.
- Used by the browser game “아니 그거 말고 / Not What I Asked” (https://notwhatiasked.pages.dev).

원본: SK텔레콤 KoGPT2(skt/kogpt2-base-v2). 라이선스 CC BY-NC-SA 4.0(비상업). 이 저장소는 브라우저에서 돌리기 위해
ONNX로 바꾸고 8비트 양자화한 것 외에는 원본과 같습니다.
