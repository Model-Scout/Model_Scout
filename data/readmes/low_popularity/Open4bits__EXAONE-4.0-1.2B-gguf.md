---
license: other
license_name: exaone
license_link: LICENSE
language:
- en
- ko
- es
tags:
- lg-ai
- exaone
- exaone-4.0
- open4bits
pipeline_tag: text-generation
library_name: transformers
base_model:
- LGAI-EXAONE/EXAONE-4.0-1.2B
---

![EXAONE](https://huggingface.co/Open4bits/EXAONE-4.0-1.2B-gguf/resolve/main/assets/EXAONE_Symbol%252BBI_3d.png)
# Open4bits / EXAONE-4.0-1.2B-GGUF

This repository provides the **EXAONE-4.0-1.2B model converted to GGUF format**, published by Open4bits to enable efficient local inference with reduced memory usage and broad CPU compatibility.

The underlying EXAONE model and architecture are **developed and owned by LG AI Research**.
This repository contains **only a quantized GGUF conversion** of the original model weights.

The model is designed for lightweight text generation and instruction-following tasks, making it suitable for local and resource-constrained environments.

---

## Model Overview

EXAONE 4.0 is a large language model family developed by LG AI Research, focusing on strong reasoning, instruction understanding, and multilingual capabilities.
This release uses the **1.2B parameter variant**, optimized for efficiency while retaining the original architecture.

The GGUF format allows seamless use with popular local inference engines and CPU-based runtimes.

---

## Model Details

* **Architecture:** EXAONE 4.0
* **Parameters:** 1.2 billion
* **Format:** GGUF (quantized)
* **Task:** Text generation, instruction following
* **Languages:** English, Korean, Spanish
* **Weight tying:** Preserved
* **Compatibility:** GGUF-compatible runtimes (CPU-focused inference)

Compared to larger EXAONE variants, this model prioritizes lower memory usage and faster inference, with some trade-off in reasoning depth.

---

## Intended Use

This model is intended for:

* Local text generation and chat applications
* CPU-based or low-resource deployments
* Research, experimentation, and prototyping
* Offline or self-hosted AI systems

---

## Limitations

* Reduced performance compared to larger EXAONE models
* Output quality depends on prompt design and inference settings
* Not fine-tuned for highly specialized or domain-specific tasks

---

## License

This repository follows the **original EXAONE license terms** as defined by LG AI Research.
Users must comply with the licensing conditions of the base EXAONE-4.0-1.2B model.

---

## Support

If you find this model useful, consider supporting the project.
Your support helps Open4bits continue converting and releasing high-quality, efficient models for the community.
