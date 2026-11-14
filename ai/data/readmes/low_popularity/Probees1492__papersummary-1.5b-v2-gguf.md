---
license: apache-2.0
base_model: Qwen/Qwen2.5-1.5B-Instruct
library_name: gguf
pipeline_tag: summarization
tags:
  - gguf
  - llama.cpp
  - qwen2.5
  - summarization
  - on-device
  - document
language:
  - ko
  - en
  - ja
  - zh
  - es
---

# PaperSummary 1.5B (fine-tuned, Q4_K_M GGUF)

On-device document-summarization engine for the **PaperSummary** app. A supervised
fine-tune (LoRA) of **Qwen2.5-1.5B-Instruct**, distilled from Qwen2.5-72B-Instruct,
aligned to the app output contract: structured `Title / Description / Summary`
markers, faithful markdown, level/format control, 29 languages, and map-reduce
merge for long documents.

- **Format**: GGUF, **Q4_K_M** (runs via llama.cpp / llama.rn, Metal/GPU), n_ctx 4096
- **File**: `papersummary-1.5b-v2-q4_k_m.gguf` (986,048,000 bytes)
- **Improvements over stock Qwen2.5-1.5B** (measured): output-marker compliance
  71%→100%, cross-lingual output language obeyed, map-reduce merge without
  hallucinated figures.
- **License**: Apache-2.0 (inherits Qwen2.5). Fine-tune data generated synthetically.

Intended as a drop-in engine download for the app; not a general chat model.
