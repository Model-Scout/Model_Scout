---
license: apache-2.0
base_model:
- FINAL-Bench/Darwin-31B-Opus
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
---
# Darwin-31B-Opus

**Quality**: quantized (***8 bit**, group size: 32, 8.643 bpw*)

## Overview

**Darwin-31B-Opus** is a reasoning-enhanced model created by merging **google/gemma-4-31B-it** (Father) and **TeichAI/gemma-4-31B-it-Claude-Opus-Distill** (Mother) using the Darwin V6 engine.

Darwin V6 diagnoses both parent models at the tensor level before merging, assigning an independent optimal ratio to each of the 1,188 tensors. This is fundamentally different from conventional merging tools that apply a single uniform ratio across all tensors.

### Model Specifications
| | |
|---|---|
| Architecture | **Gemma 4 Dense** (Hybrid Attention: Sliding Window + Global) |
| Parameters | 31B |
| Precision | BF16 |
| Context | 256,072 |
| Languages | 140+ |
| Thinking | enable_thinking=True chain-of-thought |
| License | Apache 2.0 |

### Parent Models

| Role | Model | Characteristics |
|---|---|---|
| Father | google/gemma-4-31B-it | Gemma 4 Dense 31B, multimodal, 256K context, LMArena 1452 (open model #3) |
| Mother | TeichAI/gemma-4-31B-it-Claude-Opus-Distill | Claude 4.6 Opus high-effort reasoning distillation, code/science/analysis |

-----
### Source
This model was converted to MLX format from [`FINAL-Bench/Darwin-31B-Opus`](https://huggingface.co/FINAL-Bench/Darwin-31B-Opus) using mlx-vlm version **0.4.4**.