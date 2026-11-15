---
license: other
license_name: lfm1.0
license_link: LICENSE
base_model: LiquidAI/LFM3-1.7B
library_name: mlx
pipeline_tag: text-generation
language:
- fr
- en
- de
- es
- it
- nl
- pt
- ar
- zh
- ja
- ko
tags:
- mlx
- lora
- on-device
- tool-use
---

# Valet · LFM3-1.7B

The on-device model of **Valet**, an iPhone app that files your paperwork, tracks deadlines and sets reminders, entirely on the phone. It is a fine-tune of [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B) for Valet's agent: its tool calls, its prompt and its 11 languages.

## What is in this repo

- `model.safetensors`: LFM3-1.7B fine-tuned for Valet, then quantized for MLX with mixed precision. The bits per unit range from 3 to 8, averaging 4.0, and are chosen by measured sensitivity.
- `adapter/`: a PEFT LoRA (rank 16, last 12 blocks) trained against those exact quantized weights. Load it **unmerged** on top of the quantized model: merging and re-quantizing loses part of the gain.

Valet loads both with mlx-swift-lm (`QLoRALinear` on the quantized layers).

## Results

The scores come from Valet's own bench, run greedily as the app runs. "base" is the same model without the adapter.

| | base | with adapter |
|---|---|---|
| dev (185 tasks) | 93.0 | 95.4 |
| dev, multilingual (60) | 85.1 | 90.4 |
| hard (125) | 95.6 | 96.5 |
| quick (38) | 85.5 | 88.9 |

Long multi-request conversations (the "marathon" suite) are unchanged, at about 63 out of 100. That is the known weak spot.

## Modifications

This model is a Derivative Work of LFM3-1.7B by Liquid AI. Valet changed it in three ways:
1. supervised fine-tuning on synthetic Valet agent traces;
2. mixed-precision quantization;
3. a LoRA trained by rejection-sampling fine-tuning on the model's own verified answers.

No user data was used.

## License

The model is distributed under the LFM Open License v1.0, the base model's license, included as `LICENSE`. Commercial use is licensed only below the threshold the license sets: an annual revenue of 10 million US dollars.
