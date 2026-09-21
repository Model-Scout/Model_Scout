---
language:
- en
- zh
- ja
- ko
- fr
- de
- es
- pt
- it
- ru
license: apache-2.0
base_model:
- Qwen/Qwen3-VL-235B-A22B-Instruct
tags:
- text-generation
- vision
- multimodal
- zenlm
- zen
- gguf
- abliterated
- moe
- ocr
- document-understanding
- hanzo
pipeline_tag: text-generation
library_name: gguf
---

# Zen Designer GGUF: 235B Vision-Language Model (Abliterated)

**235B MoE | Vision-Language | GGUF Quantized | Abliterated**

Fine-tuned from [Qwen3-VL-235B-A22B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-235B-A22B-Instruct) (Apache-2.0) with Hanzo identity + agentic-data training + abliteration, then GGUF-quantized. A 235B-total / 22B-active Mixture-of-Experts vision-language model supporting images, video, documents, charts, GUIs, and spatial reasoning with 256K context.

---

## Model Specifications

| Attribute | Value |
|-----------|-------|
| Base Model | [Qwen3-VL-235B-A22B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-235B-A22B-Instruct) (Apache-2.0) |
| Parameters | 235B total / 22B active (MoE) |
| Architecture | Vision-language transformer (Mixture of Experts) |
| Context Window | 256K tokens |
| Modalities | Text, Images, Video, Documents |
| OCR Languages | 32 scripts |
| License | Apache 2.0 |

---

## Available Formats

| Format | Size | Description | Recommended Use |
|--------|------|-------------|-----------------|
| Q2_K (split) | ~60 GB | 2-bit quantization, 15-part split | Servers with 64+ GB RAM, maximum scale |
| Q4_K_M | ~142 GB | 4-bit quantization, single or split | Best quality/size tradeoff for local inference |

---

## Quick Start

### llama.cpp

```bash
# Download a split (Q2_K example — replace with Q4_K_M filename as appropriate)
# Then run:
llama-cli \
  --model zen-designer-235b-a22b-instruct-abliterated-Q2_K-00001-of-00015.gguf \
  --mmproj mmproj-zen-designer-235b-a22b-instruct-abliterated-f16.gguf \
  --image your_image.jpg \
  --prompt "Describe this image in detail." \
  -n 1024 \
  --ctx-size 8192 \
  --temp 0.7
```

For multi-part files, place all split parts in the same directory and point `--model` to part `00001`.

### Vision Tasks

Zen Designer handles a broad range of visual inputs:
- Image analysis and description
- Document and PDF parsing
- Chart and table extraction
- GUI navigation and screen understanding
- Video understanding with temporal reasoning
- Bounding box and spatial grounding

---

## Abliteration

This model has been abliterated — a technique that removes refusal behaviors encoded in the model weights without fine-tuning. The process works by identifying the refusal direction in the model's residual stream and projecting it out of the weight matrices.

**What abliteration does:**
- Removes hardcoded refusal responses
- Preserves all other capabilities and knowledge
- Does not alter factual knowledge or reasoning ability

**What abliteration does not do:**
- Add harmful knowledge the base model lacked
- Guarantee any specific behavior
- Replace a system prompt or application-level safety policy

Users are responsible for appropriate deployment and use of abliterated models. Apply system prompts and application-layer controls to define model behavior for your use case.

---

## Attribution

Built on [Qwen3-VL-235B-A22B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-235B-A22B-Instruct) by the Qwen team, Alibaba Group, released under the Apache License 2.0. Hanzo's contribution is identity training, agentic-data fine-tuning, and abliteration on top of that base, distributed here in GGUF format. The base model is used under the terms of the Apache License, Version 2.0.

---

## Model Family

| Model | Format | Parameters | Context |
|-------|--------|-----------|---------|
| [zen-designer-235b-a22b-instruct](https://huggingface.co/zenlm/zen-designer-235b-a22b-instruct) | SafeTensors | 235B / 22B active | 256K |
| [zen-designer-gguf](https://huggingface.co/zenlm/zen-designer-gguf) | GGUF | 235B / 22B active | 256K |

---

## Links

[Zen LM](https://zenlm.org) | [Hanzo AI](https://hanzo.ai) | [GitHub](https://github.com/zenlm) | [All Models](https://huggingface.co/zenlm)

---

Part of the Zen model family ([zenlm.org](https://zenlm.org)) by [Hanzo AI](https://hanzo.ai) (Techstars '17) and [Zoo Labs Foundation](https://zoo.ngo) (zoo.ngo).
