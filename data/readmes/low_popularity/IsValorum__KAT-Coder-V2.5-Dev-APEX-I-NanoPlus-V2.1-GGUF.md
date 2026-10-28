---
base_model: Kwaipilot/KAT-Coder-V2.5-Dev
quantized_by: IsValorum
library_name: gguf
language:
- en
- zh
- es
- fr
- de
- pt
- it
- ru
- ja
- ko
- vi
- th
- ar
tags:
- gguf
- quantized
- quantization
- apex
- apex-quant
- apex-i-nanoplus
- v2.1
- custom-quantization
- unsloth-studio
- moe
- reasoning
- coding
- llama.cpp
- qwen35moe
license: apache-2.0
pipeline_tag: text-generation
---

<div align="center">

# KAT-Coder-V2.5-Dev-APEX-I-NanoPlus-V2.1

**APEX Quantization Series by IsValorum**

[![Ko-fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/isvalorum)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/IsValorum)

</div>

---

### Family Cross-Links

| Precision Tier | Standard Alignment (Base) |
|---|---|
| **MiniPlus** (14.75 GB) | [KAT-Coder-V2.5-Dev-APEX-I-MiniPlus-V2.1-GGUF](https://huggingface.co/IsValorum/KAT-Coder-V2.5-Dev-APEX-I-MiniPlus-V2.1-GGUF) |
| **NanoPlus** (12.55 GB) | [KAT-Coder-V2.5-Dev-APEX-I-NanoPlus-V2.1-GGUF](https://huggingface.co/IsValorum/KAT-Coder-V2.5-Dev-APEX-I-NanoPlus-V2.1-GGUF) |

---

### Architecture & Precision Highlights

- **Base Model:** `Kwaipilot/KAT-Coder-V2.5-Dev`
- **Architecture Type:** Sparse Mixture-of-Experts (Qwen 35B / 40 Layers / DeltaNet Hybrid)
- **Total Parameters:** 34.5 Billion (approx. 3.4 Billion active per token)
- **Quantization Profile:** APEX-I NanoPlus V2.1 (approx. 11.69 GiB / approx. 12.55 GB on web)
- **Audited Tensors:** Exactly 733 verified tensors
- **Integrated Speculative Decoding:** Bundled with standalone MTP adapter `mtp-KAT-Coder-V2.5-Dev-Q4_0.gguf`

| Structural Group | Precision Tier | Technical Rationale |
|---|---|---|
| **Recurrent Core & Norms** | `F32` | Shielded from quantization noise; protects continuous-state memory dynamics. |
| **MoE Routers** | `F32` | `ffn_gate_inp` and shared gates locked to 32-bit floats to prevent expert collapse. |
| **Shared Experts** | `Q4_K` | Preserves fundamental token representations across all 40 layers. |
| **Boundary Routed Experts** | `Q3_K` / `IQ3_XXS` | First 10 and last 10 layers protected with higher precision codebooks. |
| **Core Routed Experts** | `IQ2_S` / `IQ2_XXS` | Central layers (10 to 29) compressed via importance matrix guidance. |
| **Attention Projections** | `Q4_K` | Unified attention projection fidelity. |
| **Output Head** | `Q6_K` | Highest-precision linear projection for vocabulary generation. |

---

### Recommended Generation Parameters

```bash
llama-server \
  -m KAT-Coder-V2.5-Dev.APEX-I-NanoPlus-V2.1.gguf \
  --draft-model mtp-KAT-Coder-V2.5-Dev-Q4_0.gguf \
  --draft-max 2 \
  --host 0.0.0.0 \
  --port 8080 \
  -c 32768 \
  -ngl 99 \
  --temp 0.6 \
  --top-p 0.95 \
  --top-k 40
```

---

### Support & Community Compute Fund

All APEX-I quantizations are independently computed on private cloud clusters funded 100% out-of-pocket. If this release helps your workflow, consider [supporting on Ko-fi](https://ko-fi.com/isvalorum). Every contribution directly sustains future cloud compute hours and supports my university studies.
