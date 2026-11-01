---
license: mit
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
- it
library_name: transformers
tags:
- DAC
- M.INC.
- dac6
- DAC6.5
- vl
- dac6_vl
pipeline_tag: image-text-to-text
---
# DAC6.5 — M.INC. Architecture Series

<p align="center">
  <img src="DAC6.5_Logo/DAC6.5_Logo.jpg" alt="DAC6 Logo" width="800px"/>
</p>

**M.INC.** is proud to present **DAC6.5**, the flagship release introducing our custom, proprietary multimodal architecture. Designed to bring high-performance vision-language capabilities to small-footprint and edge compute environments, DAC6.5 seamlessly unifies perception and reasoning into a single cohesive ecosystem.

DAC6.5 couples the **LFM2.5-230M** language backbone with the high-resolution **SigLIP2** vision encoder through a custom-trained projection module, delivering strong zero-shot image understanding, rapid inference, and minimal memory overhead.

---

## Model Architecture & Technical Overview

Unlike fragmented pipelines requiring complex multi-stage orchestration, DAC6.5 is engineered as an integrated, end-to-end multimodal system:

* **Language Backbone (`LFM2.5-230M`):** Ultra-lightweight text engine fine-tuned for high throughput and low-latency response generation.
* **Vision Encoder (`SigLIP2`):** State-of-the-art visual feature extraction, capturing deep spatial and semantic details from input images.
* **Proprietary Projector:** A dedicated cross-modal projection layer trained from scratch by M.INC. to map visual representation spaces directly into the language model's embedding space.

---

## Repository Structure & Core Artifacts

This repository contains the complete unified weights, configuration schemas, and quantization variants required for deployment:

### Weights & Configurations
* `model.safetensors` — Unified model weights stored with isolated, clean namespaces (`language_model.*`, `vision_encoder.*`, and `projector.*`).
* `config.json` — Core DAC6.5 architecture specifications and inter-component routing.
* `tokenizer.json`, `tokenizer_config.json`, `chat_template.jinja` — Complete tokenizer configuration and standard chat templates for the LFM engine.
* `vision_config.json`, `processor_config.json` — Preprocessing pipelines and parameter definitions for the SigLIP2 vision encoder.

---

## ☕ Support my research

[![Buy Me a Coffee](https://img.shields.io/badge/Support-Buy%20Me%20a%20Coffee-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=black)](https://www.buymeacoffee.com/marzomattye)

---

## About M.INC.

**M.INC.** focuses on research and development of custom neural architectures, efficient language models, and accessible multimodal systems. DAC6.5 represents the first milestone in our custom architecture series, establishing a new baseline for compact, locally deployable artificial intelligence.