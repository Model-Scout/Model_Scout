---
base_model: openbmb/MiniCPM-V-4.7-35B-A3B
base_model_relation: quantized
quantized_by: IsValorum
library_name: gguf
pipeline_tag: image-text-to-text
license: apache-2.0
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
tags:
- gguf
- llama.cpp
- quantized
- quantization
- apex
- apex-quant
- apex-i-miniplus
- v2.1
- custom-quantization
- minicpm-v
- minicpm
- openbmb
- moe
- multimodal
- vision
- image-text-to-text
- video
- on-device
- imatrix
- atomic-chat
---

## <a id="quick-navigation"></a>Quick Navigation Index

<a href="https://ko-fi.com/isvalorum"><img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="Support on Ko-fi" height="38"></a>

**Independently computed using dedicated cloud compute clusters, funded 100% out-of-pocket.**

If you consider these releases to be of high quality and they help you in your day-to-day workflow, consider [supporting on Ko-fi](https://ko-fi.com/isvalorum). Every contribution directly sustains future cloud compute hours and helps support my university studies.

---

### MiniCPM-V 4.7 35B-A3B APEX-I MiniPlus V2.1 GGUF

Official APEX-I MiniPlus V2.1 canonical release for **OpenBMB MiniCPM-V 4.7 35B-A3B**, the first Mixture-of-Experts (MoE) multimodal model in the MiniCPM series.

#### Key Architectural Features:
- **Canonical 733-Tensor Allocation:**
  - `output.weight` protected in **Q6_K** (1 tensor).
  - `token_embd.weight` protected in **Q4_K** (1 tensor).
  - Normalizations and MoE Expert Routers (`ffn_gate_inp`) in **F32** (zero routing drift).
  - Shared foundation experts (`shexp`) in **Q5_K** (100% active pathway).
  - Periodic full-attention anchors (layers 3, 7, 11, ..., 39) in **Q4_K** (Q/K/V) and **Q6_K** (output).
  - Recurrent Gated DeltaNet protected states in **F32** (`ssm_a`, `ssm_conv1d`, `ssm_dt`, `ssm_norm`).
  - Edge routed experts (layers 0-9 and 30-39) in **Q3_K**; core routed experts (layers 10-29) in **IQ3_XXS**.
- **Multimodal Projector:**
  - Includes companion `mmproj-Q8_0.gguf` for high-fidelity visual reasoning without token degradation.

#### CLI Usage Example:
```bash
llama-minicpmv-cli \
  -m MiniCPM-V-4.7-35B-A3B.APEX-I-MiniPlus-V2.1.gguf \
  --mmproj mmproj-Q8_0.gguf \
  --image test.jpg \
  -p "Describe what you see in this image in detail." \
  -c 4096 --temp 0.7
```
