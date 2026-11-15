---
language:
- bn
- en
- zh
- ko
- ar
- hi
pipeline_tag: text-generation
tags:
- cinematic
- movie-explainer
- qwen
- gguf
thumbnail: null
base_model: Qwen/Qwen2.5-1.5B-Instruct
license: apache-2.0
---


# Axion v1.0 (Movie Explainer AI)

![Axion Logo](https://cdn-uploads.huggingface.co/production/uploads/69cfec4600af2a889e527125/l6emcNJcDOZsszEhuBffK.png)


Axion is a fine-tuned cinematic AI model based on **Qwen 2.5 1.5B**. It is specifically trained to analyze movies, explain complex plots, and provide real-time frame descriptions for streaming applications.

## Model Details
- **Developed by:** AeonCoreX-Lab
- **Base Model:** Qwen 2.5 1.5B Instruct
- **Format:** GGUF (Quantized)
- **Quantization:** Q4_K_M (4-bit)
- **Training Data:** 685 steps of specialized cinematic datasets.

## Features
- Specialized in movie plot analysis.
- Optimized for mobile devices (works great on RedMagic & high-end Android).
- Small footprint (~986MB), making it ideal for on-device inference.

## Usage
This model is designed to be integrated into the **StreamX-Ultra** media player for real-time movie explanation.