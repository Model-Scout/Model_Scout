---
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
language: [en, de, es, fr, ja, pt, ar, cs, it, ko, nl, zh]
tags: [granite, granite-4.2, reasoning, thinking, tool-calling, ibm]
base_model: ibm-granite/granite-4.2-3b
base_model_relation: quantized
---

# Jeethu/granite-4.2-3b-PARO

**Pairwise Rotation Quantization for Efficient Reasoning LLM Inference**

<p>
  <a href="https://arxiv.org/abs/2511.10645"><img src="https://img.shields.io/badge/arXiv-2511.10645-b31b1b.svg" alt="Paper"></a>
  <a href="https://paroquant.z-lab.ai"><img src="https://img.shields.io/badge/Blog-ParoQuant-blue" alt="Blog"></a>
  <a href="https://huggingface.co/collections/z-lab/paroquant"><img src="https://img.shields.io/badge/%F0%9F%A4%97-Models-yellow" alt="Models"></a>
  <a href="https://pypi.org/project/paroquant/"><img src="https://img.shields.io/pypi/v/paroquant" alt="PyPI"></a>
</p>

ParoQuant is the state-of-the-art INT4 quantization for LLMs. It closes the accuracy gap with FP16 while running at near-AWQ speed. Supports NVIDIA GPUs (vLLM, Transformers) and Apple Silicon (MLX). For more information, see https://github.com/z-lab/paroquant.

Jeethu/granite-4.2-3b-PARO is a 4-bit [ibm-granite/granite-4.2-3b](https://huggingface.co/ibm-granite/granite-4.2-3b) quantized with ParoQuant.
