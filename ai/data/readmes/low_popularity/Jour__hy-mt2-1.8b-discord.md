---
license: apache-2.0
base_model: tencent/Hy-MT2-1.8B
language: [en, fr, es, de, pt, it, ru, ja, ko, zh, tr, ar, pl, nl]
pipeline_tag: translation
tags: [translation, discord, lora, formatting-preservation]
---
# Hy-MT2-1.8B Discord (merged)

[tencent/Hy-MT2-1.8B](https://huggingface.co/tencent/Hy-MT2-1.8B) (Apache-2.0, license included) merged with the Discord LoRA: bf16 safetensors plus `hy-mt2-1.8b-discord-bf16.gguf`. Modified from the original (fine-tuned). Details, benchmark and limits: [Jour/hy-mt2-1.8b-discord-lora](https://huggingface.co/Jour/hy-mt2-1.8b-discord-lora) (formatting preserved 94.4 % → 97.2 %, chrF 63.5 → 70.6 on 143 unseen pairs).

Note: re-quantizing this merged model to 1.25 bit (STQ1_0) with plain post-training quantization degrades quality (the official 1.25-bit model uses quantization-aware training). For 1.25 bit use [Jour/hy-mt2-1.8b-discord-1.25bit-lora](https://huggingface.co/Jour/hy-mt2-1.8b-discord-1.25bit-lora) on top of Tencent's official GGUF.
