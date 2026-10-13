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
- apex-i-nanoplus
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

### MiniCPM-V 4.7 35B-A3B APEX-I NanoPlus V2.1 GGUF

Official APEX-I NanoPlus V2.1 canonical release for **OpenBMB MiniCPM-V 4.7 35B-A3B**, engineered for ultra-compact on-device memory footprints while preserving recurrent DeltaNet dynamics and visual fidelity.

#### Key Architectural Features:
- **Canonical 733-Tensor Allocation:**
  - `output.weight` in **Q6_K** and `token_embd.weight` in **Q4_K**.
  - MoE Expert Routers (`ffn_gate_inp`) in **F32**.
  - Shared foundation experts (`shexp`) in **Q4_K**.
  - Recurrent SSM continuous states in **F32** (`ssm_a`, `ssm_conv1d`, `ssm_dt`, `ssm_norm`).
  - Border down projections in **Q3_K** and border gate/up in **IQ3_XXS**.
  - Core down projections (layers 2-37) in **IQ3_XXS**, gate in **IQ2_S**, protected up (layers 2-15) in **IQ2_S**, compact up (layers 16-37) in **IQ2_XXS**.
- **Multimodal Projector:**
  - Includes companion `mmproj-Q8_0.gguf` for on-device visual inference.

#### CLI Usage Example:
```bash
llama-minicpmv-cli \
  -m MiniCPM-V-4.7-35B-A3B.APEX-I-NanoPlus-V2.1.gguf \
  --mmproj mmproj-Q8_0.gguf \
  --image test.jpg \
  -p "Describe what you see in this image in detail." \
  -c 4096 --temp 0.7
```
