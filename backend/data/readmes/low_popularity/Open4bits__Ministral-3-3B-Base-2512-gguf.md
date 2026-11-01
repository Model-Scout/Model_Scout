---
library_name: vllm
language:
- en
- fr
- es
- de
- it
- pt
- nl
- zh
- ja
- ko
- ar
license: apache-2.0
tags:
- mistral-common
- llama-cpp
- open4bits
base_model: mistralai/Ministral-3-3B-Base-2512
pipeline_tag: image-text-to-text
---
# Open4bits / Ministral-3-3B-Base-2512-GGUF

This repository provides the **Ministral 3 3B Base model converted to GGUF format**, published by Open4bits to enable efficient local inference with reduced memory usage and broad CPU compatibility.

The underlying Ministral 3 model and architecture are **developed and owned by Ministral**. This repository contains only a quantized GGUF conversion of the original model weights.

The model is designed for lightweight, high-performance text generation and instruction-following tasks, making it well suited for local and resource-constrained environments.

---

## Model Overview

Ministral 3 is a next-generation transformer-based large language model developed for strong generalization and robust natural language understanding.
This release uses the **3B parameter Base variant**, optimized for general-purpose text generation, reasoning, and instruction compliance.

The GGUF format enables broad compatibility with popular local inference engines and efficient CPU-based runtimes.

---

## Model Details

* **Architecture:** Ministral 3 Base
* **Parameters:** ~3 billion
* **Format:** GGUF (quantized)
* **Task:** Text generation, instruction following
* **Weight tying:** Preserved
* **Compatibility:** GGUF-compatible inference runtimes (CPU-focused)

Compared to larger models in the same family, this variant offers a favorable balance of performance and resource efficiency.

---

## Intended Use

This model is intended for:

* Local text generation and conversational applications
* CPU-based or low-resource deployments
* Research, experimentation, and prototyping
* Self-hosted or offline AI systems

---

## Limitations

* Reduced performance compared to larger or non-quantized variants
* Output quality depends on prompt engineering and inference settings
* Not specifically tuned for domain-specific or specialized tasks

---

## License

This model is released under the **original licensing terms** of the base Ministral 3 model.
Users must comply with the licensing conditions defined by the original model creators.

---

## Support

If you find this model useful, please consider supporting the project.
Your support enables Open4bits to continue releasing and maintaining high-quality, efficient open models for the community.