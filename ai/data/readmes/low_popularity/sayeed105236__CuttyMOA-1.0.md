---
license: apache-2.0
datasets:
- sayeed105236/cuteadmoa-204-datasets
language:
- en
- bn
- hi
- ar
- zh
- ja
- ko
- fr
- de
- es
pipeline_tag: text-generation
tags:
- gguf
- moa
- self-trained
- cuteadmoa
- quantized
- q4_k_m
---

# 🚀 CuttyMOA-1.0 Pro (24K)

**Self-trained language model** built on Qwen2.5-14B-Instruct, combining **two independent LoRA training phases** (4K + 20K) via **TIES delta merge** into a single 24K-step model.

## What's New — 20K Merge Update

This release merges **both training adapters** into one coherent model:

| Phase | Platform | Steps | Method | Status |
|-------|----------|-------|--------|--------|
| Phase 1 | HuggingFace Spaces (L40S 48GB) | ~4,000 | QLoRA 4-bit nf4, r=128, α=256 | ✅ Completed |
| Phase 2 | RunPod A40 (48GB VRAM) | ~20,000 | QLoRA 4-bit nf4, r=128, α=256 | ✅ Completed |
| **TIES Merge** | VPS (12 cores, 47GB RAM) | — | Sign-resolve + magnitude delta combine | ✅ **Completed** |
| GGUF Q4_K_M | VPS (llama.cpp) | — | 4.87 BPW | ✅ **Completed** |
| Deploy + HF Upload | VPS + HuggingFace | — | llama-server :5401 + this repo | ✅ **Live** |

### Why TIES Merge?
- The 20K RunPod phase was a **fresh training** (not a continuation of 4K)
- Both adapters trained independent learning trajectories on the same base
- **TIES** (Trim, Elect Sign, Merge) resolves cases where the two adapters modified weights in opposite directions, keeping the larger-magnitude delta — preventing destructive interference
- Result: a combined model that captures knowledge from **both** phases

## Training Data

- **204 verified datasets** (24 categories) → **4.5M training pairs**
- Categories: core LLM, code, security/cyber, Q&A, multilingual (10 lang), reasoning/math, agentic-tools, finance, medical, legal, RAG, enterprise, image, video, audio, presentation, science, sentiment, dialogue, docs/PDF, news, SQL, dialogue systems, translation
- **RAG corpus**: 857K domain pairs captured from live CUTEADMOA platform usage (MOA fleet, OpenAI-compatible API, security scanning)
- **Historical sessions**: 2,323 logged interactions

## Files

| File | Purpose |
|------|---------|
| `cuttymoa-1.0-pro-Q4_K_M.gguf` | **Pro model (24K TIES-merged) — recommended** |
| `cuttymoa-1.0-Q4_K_M.gguf` | Original 4K Phase-1 model (legacy) |

## Deployment

- **Self-hosted**: llama-server on port 5401 (Q4_K_M, 8.99 GB, 32K context)
- **API**: via CUTEADMOA-5.6 MOA fleet (`cuttymoa_pro` model id)
- **Inference**: ~30-50 tokens/sec on CPU (12-core VPS)

## Capabilities

- General chat & instruction following
- Code generation (Python, JS, SQL, shell)
- **Cybersecurity** (17 security intents): vulnerability analysis, code audit, threat intel
- Multilingual (10 languages)
- Agentic / tool use
- RAG-augmented domain knowledge

## Limitations

- 14B parameters, domain-specialized (not frontier-scale)
- Trained on ~50M tokens (far less than commercial models' trillions)
- Best used within the CUTEADMOA Mixture-of-Agents fleet as a specialized engine

## 📄 Publication

This model is part of the **CUTEADMOA** platform presented in:

> Md Abu Sayeed. *CUTEADMOA: A Unified Mixture-of-Agents Platform with Continuous Self-Training for Autonomous Enterprise AI Automation.* **Advances in Artificial Intelligence and Robotics Research**, Vol. 2, No. 3, pp. 190–208, September 2026.

- 📰 Paper page: <https://www.scirp.org/journal/paperinformation?paperid=154162>
- 📄 Full-text PDF: <https://www.scirp.net/pdf/airr_2970152.pdf>
- 🔗 DOI: <https://doi.org/10.4236/airr.2026.23011>

```bibtex
@article{sayeed2026cuteadmoa,
  author  = {Md Abu Sayeed},
  title   = {CUTEADMOA: A Unified Mixture-of-Agents Platform with Continuous Self-Training for Autonomous Enterprise AI Automation},
  journal = {Advances in Artificial Intelligence and Robotics Research},
  volume  = {2},
  number  = {3},
  pages   = {190--208},
  year    = {2026},
  issn    = {3143-3987},
  doi     = {10.4236/airr.2026.23011},
  url     = {https://www.scirp.org/journal/paperinformation?paperid=154162}
}
```

## Citation

```bibtex
@misc{cuttymoa2026,
  title={CuttyMOA-1.0: Self-Trained 14B Model with TIES Multi-Adapter Merge},
  author={Sayeed},
  year={2026},
  url={https://huggingface.co/sayeed105236/CuttyMOA-1.0}
}
```
