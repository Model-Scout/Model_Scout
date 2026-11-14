---
license: apache-2.0
base_model:
- FINAL-Bench/Darwin-35B-A3B-Opus
pipeline_tag: image-text-to-text
language:
- en
- zh
- ru
- es
- fr
- it
- ja
- ko
- af
- de
- ar
- tr
- is
- pl
- sw
- sv
- nl
- he
- id
- uk
- fa
- pa
- pt
- ms
- fi
- el
library_name: mlx
tags:
- 8bit
- mxfp8
---
# Darwin-35B-A3B-Opus

**Quality**: quantized (***mxfp8**, 8.349 bpw*)

### Model Specifications
| | |
|---|---|
| Architecture | Qwen3.5 MoE (Gated DeltaNet + MoE) |
| Total Parameters | 35B |
| Active Parameters | 3B per forward pass |
| Layers | 40 |
| Layout | 10 x (3 x GDN-MoE + 1 x Attention-MoE) |
| Experts | 256 (8 routed + 1 shared active) |
| Context Length | 262,144 native |
| Languages | 201 |
| Multimodal | Image and Video |
| License | Apache 2.0 |

### Parent Models

Both parents share the identical Qwen3.5-35B-A3B architecture (40 layers, 256 experts, GDN+MoE hybrid). The Mother is a LoRA SFT on the same base — not a different architecture. "Text-only" refers to the training data (Claude 4.6 Opus reasoning chains), not the model structure.

| Role | Model | Architecture | Training |
|---|---|---|---|
| Father | [Qwen/Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B) | Qwen3.5-35B-A3B | Original pre-training + RLHF |
| Mother | [Jackrong/Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled) | Qwen3.5-35B-A3B (same) | LoRA SFT with text-only Claude reasoning chains |

-----
### Source
This model was converted to MLX format from [`FINAL-Bench/Darwin-35B-A3B-Opus`](https://huggingface.co/FINAL-Bench/Darwin-35B-A3B-Opus) using mlx-vlm version **0.4.4**.