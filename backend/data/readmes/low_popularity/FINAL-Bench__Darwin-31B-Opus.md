---
license: apache-2.0

tags:
  - darwin
  - darwin-v6
  - evolutionary-merge
  - mri-guided
  - dare-ties
  - gemma4
  - reasoning
  - thinking
  - darwin-delphi
  - gpqa
  - benchmark
  - eval-results
  - apache-2.0
  - proto-agi
  - vidraft
language:
  - en
  - ko
  - ja
  - zh
  - multilingual
pipeline_tag: text-generation
library_name: transformers
model-index:
- name: Darwin-31B-Opus
  results:
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: GPQA Diamond
      type: Idavidrein/gpqa
      config: gpqa_diamond
    metrics:
    - type: accuracy
      value: 85.9
      name: Accuracy
---

> ### 📱 Run it on your phone or a GPU-less PC → **POCKET**  ·  🚀 **[Try it live (CPU chat)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU)**
> VIDRAFT's on-device family: a 35B model that runs on **iPhone** and on **CPU with no GPU** — stock `llama.cpp`, no fork.
>
> [![Live demo](https://img.shields.io/badge/🤗_Space-POCKET_CPU_chat-ffce3a)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU) [![Collection](https://img.shields.io/badge/📚-POCKET_collection-5dbf9a)](https://huggingface.co/collections/FINAL-Bench/pocket-models-6a618ee5d23eafb7e185a5c6) [![35B](https://img.shields.io/badge/POCKET--35B-GGUF-243456)](https://huggingface.co/FINAL-Bench/POCKET-35B-GGUF) [![KR MLX](https://img.shields.io/badge/POCKET--KR-iPhone-0f6e56)](https://huggingface.co/FINAL-Bench/POCKET-KR-MLX) [![EN](https://img.shields.io/badge/POCKET--EN-GGUF-185fa5)](https://huggingface.co/FINAL-Bench/POCKET-EN-GGUF)

>


# Darwin-31B-Opus

<p align="center">
  <a href="https://huggingface.co/FINAL-Bench/Darwin-31B-Opus"><img src="https://img.shields.io/badge/⭐_GPQA_Diamond-85.9%25_with_Darwin--DELPHI-gold?style=for-the-badge" alt="GPQA"></a>
</p>

<p align="center">
  <a href="https://huggingface.co/FINAL-Bench/Darwin-4B-Opus"><img src="https://img.shields.io/badge/🧬_Gen1-Darwin--4B--Opus-blue?style=for-the-badge" alt="Gen1"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-4B-David"><img src="https://img.shields.io/badge/🧬_Gen2-Darwin--4B--David-blue?style=for-the-badge" alt="Gen2"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-4B-Genesis"><img src="https://img.shields.io/badge/⭐_Gen3-Darwin--4B--Genesis-gold?style=for-the-badge" alt="Gen3"></a>
</p>

<p align="center">
  <a href="https://huggingface.co/FINAL-Bench/Darwin-9B-Opus"><img src="https://img.shields.io/badge/🧬_Model-Darwin--9B--Opus-blue?style=for-the-badge" alt="9B"></a>
  <a href="https://huggingface.co/spaces/FINAL-Bench/Darwin-9B-Opus"><img src="https://img.shields.io/badge/🚀_Space-9B_Demo-purple?style=for-the-badge" alt="9B Space"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-31B-Opus"><img src="https://img.shields.io/badge/🧬_Model-Darwin--31B--Opus-blue?style=for-the-badge" alt="31B"></a>
  <a href="https://huggingface.co/spaces/FINAL-Bench/Darwin-31B-Opus"><img src="https://img.shields.io/badge/🚀_Space-31B_Demo-purple?style=for-the-badge" alt="31B Space"></a>
</p>

<p align="center">
  <a href="https://huggingface.co/FINAL-Bench/Darwin-35B-A3B-Opus"><img src="https://img.shields.io/badge/🧬_Model-Darwin--35B--A3B--Opus-blue?style=for-the-badge" alt="35B"></a>
  <a href="https://huggingface.co/spaces/FINAL-Bench/Darwin-35B-A3B-Opus"><img src="https://img.shields.io/badge/🚀_Space-35B_Demo-purple?style=for-the-badge" alt="35B Space"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-35B-A3B-Opus-Q8-GGUF"><img src="https://img.shields.io/badge/📦_GGUF-Q8--Official-yellow?style=for-the-badge" alt="Q8 GGUF"></a>
  <a href="https://huggingface.co/bartowski/FINAL-Bench_Darwin-35B-A3B-Opus-GGUF"><img src="https://img.shields.io/badge/📦_GGUF-bartowski-yellow?style=for-the-badge" alt="bartowski GGUF"></a>
</p>

<p align="center">
  <a href="https://huggingface.co/spaces/FINAL-Bench/Leaderboard"><img src="https://img.shields.io/badge/🏆_FINAL_Bench-Leaderboard-green?style=for-the-badge" alt="FINAL Bench"></a>
  <a href="https://huggingface.co/spaces/FINAL-Bench/all-bench-leaderboard"><img src="https://img.shields.io/badge/📊_ALL_Bench-Leaderboard-orange?style=for-the-badge" alt="ALL Bench"></a>
</p>

> Gemma 4 Dense 31B | Thinking Mode | 256K Context | 140+ Languages | BF16 | Apache 2.0

---

## Overview

Darwin-31B-Opus is a reasoning-enhanced model created by merging google/gemma-4-31B-it (Father) and TeichAI/gemma-4-31B-it-Claude-Opus-Distill (Mother) using the Darwin V6 engine.

Darwin V6 diagnoses both parent models at the tensor level before merging, assigning an independent optimal ratio to each of the 1,188 tensors. This is fundamentally different from conventional merging tools that apply a single uniform ratio across all tensors.

---

## Parent Models

| Role | Model | Characteristics |
|---|---|---|
| Father | google/gemma-4-31B-it | Gemma 4 Dense 31B, multimodal, 256K context, LMArena 1452 (open model #3) |
| Mother | TeichAI/gemma-4-31B-it-Claude-Opus-Distill | Claude 4.6 Opus high-effort reasoning distillation, code/science/analysis |

### Model Diagnostic Scan (MDS)

<p align="center">
  <img src="s1.png" alt="Father (gemma-4-31B-it) MDS Scan" width="48%">
  <img src="s2.png" alt="Mother (Claude-Opus-Distill) MDS Scan" width="48%">
</p>

Left: Father (gemma-4-31B-it) — balanced generalist with low activation across most probes. Right: Mother (Claude-Opus-Distill) — strong REASONING concentration in L50-L60, CODE activation in late layers, KOREAN at start and end. The Mother shows significantly more specialized layer patterns from Claude Opus distillation.

---

## 🏆 Benchmark — GPQA Diamond (198 questions)

GPQA Diamond is a 198-question, PhD-level graduate science reasoning benchmark.

| Benchmark | Darwin-31B-Opus | Engine |
|---|---|---|
| **GPQA Diamond** | **🥇 85.9%** | Darwin-DELPHI test-time engine |
| ARC-Challenge | 82.89% | evolutionary-selection metric (loglikelihood, 0-shot, 200Q) |

The 85.9 % GPQA Diamond result is produced with the **Darwin-DELPHI** test-time reasoning engine applied on top of this model. The evaluation methodology is **protected**; sample counts, staging, and thresholds are a **trade secret**. ARC-Challenge 82.89 % is the internal evolutionary-selection score used during the Darwin V6 merge search.

> Note: the Gemma 4 architecture (`Gemma4ForConditionalGeneration`) has a multimodal wrapper that limits `lm-eval` loglikelihood compatibility; generative evaluation is the valid path for Gemma 4 based models, and Darwin-DELPHI evaluates generatively accordingly.

---

## Darwin V6 vs Conventional Merging

| Capability | mergekit (DARE-TIES) | Darwin V6 |
|---|---|---|
| Implementation | Library call (mergekit CLI) | Direct PyTorch tensor operations, no external dependency |
| Ratio selection | Uniform ratio across all tensors | Per-tensor ratio from MDS diagnostic (1,188 independent ratios) |
| Pre-merge analysis | None | Static tensor profiling (entropy, std, norm) + probe-based functional importance (5 probes) |
| Ratio formula | Human-set or grid search | combined = static × 0.4 + probe × 0.6, then evolutionary optimization |
| Transplant | Not supported | ratio < 0.15 → Father 100%, ratio > 0.85 → Mother 100% (zero interpolation noise) |
| Post-merge validation | Benchmark score only | Layer-by-layer Health Check: child vs both parents, interference and function loss detection |
| Search method | Manual tuning | CMA-ES evolution with adaptive 14-dimensional genome |
| Reproducibility | Config file | genome_hash seed guarantees identical output for identical genome |
| GPU efficiency | Single merge per run | Phase 1 proxy (200 steps, seconds) → Phase 2 real merge (top-k only evaluated) |

---

## How Darwin V6 Works

Darwin V6 does not use mergekit or any external merge library. It re-implements DARE-TIES (Yadav et al., 2023) directly via PyTorch tensor operations with per-tensor diagnostic ratios.

Before merging, Darwin performs a Model Diagnostic Scan (MDS) on both parents. For every tensor, it measures Shannon entropy (information density), standard deviation (activation spread), and L2 norm (energy). Additionally, 5 diagnostic probes (REASONING, CODE, MATH, KNOWLEDGE, LANGUAGE) are passed through the model, measuring cosine distance when each layer is skipped to determine functional importance.

The final merge ratio for each tensor:

```
static_score = entropy × 0.3 + std × 0.2 + clamp(norm, 100) × 0.002
probe_score  = Σ(cosine_distance[probe_i] × weight_i)
combined     = static × 0.4 + probe × 0.6
mri_ratio    = combined_b / (combined_a + combined_b)
final_ratio  = mri_ratio × mri_trust + genome_ratio × (1 - mri_trust)
```

The mri_trust parameter itself is optimized by the CMA-ES evolutionary algorithm, allowing the system to automatically determine the optimal balance between diagnostic prescription and evolutionary search for each model pair.

After merging, a Health Check compares the child model against both parents layer-by-layer, detecting interference (child importance >> parent max) or function loss (parent importance high but child dropped).

### Parent Comparison (MDS Result)

<p align="center">
  <img src="parent_comparison.png" alt="Parent Comparison — Layer-wise Importance" width="100%">
</p>

---

## Evolution Result

| | |
|---|---|
| Best Score (ARC-Challenge) | 0.8289 |
| Merge Method | DARE-TIES (direct PyTorch) |
| Tensors Merged | 1,188 |
| Health Check | healthy |
| Phase 2 Steps | 4 (early stop, patience=5) |
| Total Time | 134 min |
| Infrastructure | 4 x NVIDIA H100 NVL (100GB) |

Optimal Genome (14-dimensional adaptive):

```
global_ratio:        0.5147   (overall merge ratio)
attn_ratio:          0.3169   (Attention layers — Father dominant)
ffn_ratio:           0.9316   (FFN layers — Mother dominant)
embed_ratio:         0.7748   (Embedding)
density_a:           0.8997   (Father DARE density)
density_b:           0.9539   (Mother DARE density)
block_0_ratio:       0.6628   (L0-L9)
block_1_ratio:       0.6431   (L10-L19)
block_2_ratio:       0.5146   (L20-L29, balanced)
block_3_ratio:       0.5971   (L30-L39)
block_4_ratio:       0.6339   (L40-L49)
block_5_ratio:       0.8583   (L50-L59, reasoning core — Mother dominant)
mri_trust:           0.3631   (MDS 36% + Genome 64%)
merge_method_weight: 0.6897
```

Key observations from the genome: ffn_ratio=0.93 indicates the FFN layers strongly favor the Mother (Claude Opus Distill), and block_5 (L50-L59)=0.86 shows the reasoning core layers also favor Mother. This aligns with the MDS heatmap pattern where Mother's reasoning capability concentrated in the final layers. Meanwhile, attn_ratio=0.32 preserves Father's attention structure, maintaining the original Gemma 4 multimodal and long-context capabilities.

---

## Model Specifications

| | |
|---|---|
| Architecture | Gemma 4 Dense (Hybrid Attention: Sliding Window + Global) |
| Parameters | 31B |
| Precision | BF16 |
| Context | 256,072 |
| Languages | 140+ |
| Thinking | enable_thinking=True chain-of-thought |
| License | Apache 2.0 |

---

## Usage

### Transformers

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained("FINAL-Bench/Darwin-31B-Opus", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    "FINAL-Bench/Darwin-31B-Opus",
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)

messages = [{"role": "user", "content": "Prove that sqrt(2) is irrational."}]
text = tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True, enable_thinking=True
)
inputs = tokenizer(text, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=4096, do_sample=False)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

---

## VRAM Requirements

| Setup | VRAM | Status |
|---|---|---|
| BF16 Full Precision | ~62 GB | |
| NVIDIA H100 80GB | 80 GB | Single GPU |
| NVIDIA A100 80GB x 2 | 160 GB | Comfortable |
| NVIDIA RTX 4090 24GB x 4 | 96 GB | device_map=auto |

---

## References

- DARE-TIES: Yadav et al., 2023 (https://arxiv.org/abs/2311.03099) — re-implemented, not library-dependent
- Darwin V6 Engine: https://huggingface.co/spaces/ginigen-ai/DARWIN-V5-BACKUP
- FINAL Bench: https://huggingface.co/spaces/FINAL-Bench/Leaderboard

---

## Built By

| | |
|---|---|
| Developer | VIDRAFT |
| Engine | Darwin V6 (Diagnostic-Guided Evolutionary Merge) |
| Architecture | Gemma-4-31B |
| License | Apache 2.0 |

---

## Citation

```bibtex
@misc{vidraft_darwin_31b_opus,
  title        = {Darwin-31B-Opus: Diagnostic-Guided Evolutionary Merge on Gemma 4},
  author       = {VIDRAFT},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/FINAL-Bench/Darwin-31B-Opus}}
}
```
This model is introduced in [Darwin Family](https://arxiv.org/abs/2605.14386).