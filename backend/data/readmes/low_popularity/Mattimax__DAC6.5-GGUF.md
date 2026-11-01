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
base_model:
- Mattimax/DAC6.5
tags:
- edge
- DAC
- M.INC.
- dac6
- DAC6.5
- vl
- dac6_vl
pipeline_tag: image-text-to-text
---
# Mattimax/DAC6.5-GGUF

<p align="center">
  <img src="DAC6.5_Logo/DAC6.5_Logo.jpg" alt="DAC6 Logo" width="800px"/>
</p>

This repository contains the official GGUF quantized variants of **DAC6.5**, the flagship multimodal model by **M.INC.** built on our custom neural architecture series. 

These quantized builds are optimized for lightweight, low-latency, and memory-efficient local deployment using GGUF-compatible inference runtimes (such as llama.cpp and Ollama).

---

## Base Model & Architecture Overview

DAC6.5 unifies vision perception and language understanding in a compact, single-pipeline system:

* **Base Model Repository:** [Mattimax/DAC6.5](https://huggingface.co/Mattimax/DAC6.5)
* **Language Backbone:** `LFM2.5-230M`
* **Vision Encoder:** `SigLIP2`
* **Projector Layer:** Proprietary cross-modal projection layer trained by M.INC.

---

## Provided Quantization Formats

This repository provides two high-efficiency GGUF quantization formats:

* **`dac6.5-q4_k_m.gguf`**: 4-bit K-quantized weights balancing fast execution, minimal memory usage, and high retention of multimodal performance. Ideal for edge devices, single-board computers, and low-VRAM environments.
* **`dac6.5-q8_0.gguf`**: 8-bit quantized weights offering maximum precision, near-lossless accuracy relative to the FP16 base model, and robust stability for critical evaluation workloads.

---

## ☕ Support my research

[![Buy Me a Coffee](https://img.shields.io/badge/Support-Buy%20Me%20a%20Coffee-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=black)](https://www.buymeacoffee.com/marzomattye)

---

## About M.INC.

**M.INC.** focuses on research and development of custom neural architectures, efficient language models, and accessible multimodal systems. DAC6.5 represents the first milestone in our custom architecture series, establishing a new baseline for compact, locally deployable artificial intelligence.