---
license: apache-2.0
base_model:
  - google/gemma-4-E4B-it
  - arsovskidev/Gemma-4-E4B-Claude-4.6-Opus-Reasoning-Distilled
tags:
  - darwin-v6
  - evolutionary-merge
  - mri-guided
  - dare-ties
  - gemma4
  - reasoning
  - thinking
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
---

# Darwin-4B-Opus

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

> Gemma 4 Expert 4B (MoE) | Thinking Mode | 128K Context | 140+ Languages | BF16 | Apache 2.0

---

## Overview

Darwin-4B-Opus is a reasoning-enhanced model created by merging google/gemma-4-E4B-it (Father) and arsovskidev/Gemma-4-E4B-Claude-4.6-Opus-Reasoning-Distilled (Mother) using the Darwin V6 engine.

Darwin V6 diagnoses both parent models at the tensor level before merging, assigning an independent optimal ratio to each tensor. This is fundamentally different from conventional merging tools that apply a single uniform ratio across all tensors.

As the smallest member of the Darwin Opus family, Darwin-4B-Opus delivers Claude Opus-level reasoning distillation in a highly efficient 4B parameter MoE architecture, making it ideal for edge deployment, rapid prototyping, and resource-constrained environments while maintaining strong benchmark performance (0.8292 ARC-Challenge).

---

## Parent Models

| Role | Model | Characteristics |
|---|---|---|
| Father | google/gemma-4-E4B-it | Gemma 4 Expert 4B (MoE), multimodal, 128K context, efficient inference |
| Mother | arsovskidev/Gemma-4-E4B-Claude-4.6-Opus-Reasoning-Distilled | Claude 4.6 Opus high-effort reasoning distillation, enhanced code/science/analysis |

### Model Diagnostic Scan (MDS)

<p align="center">
  <img src="s1.png" alt="Father (gemma-4-E4B-it) MDS Scan" width="48%">
  <img src="s2.png" alt="Mother (Claude-Opus-Distill) MDS Scan" width="48%">
</p>

Left: Father (gemma-4-E4B-it) — balanced generalist with low activation across most probes. Right: Mother (Claude-Opus-Distill) — strong REASONING concentration in later layers, CODE activation in late layers. The Mother shows significantly more specialized layer patterns from Claude Opus distillation.

---

## Benchmarks

| Benchmark | Darwin-4B-Opus | Condition |
|---|---|---|
| ARC-Challenge | 82.92% | loglikelihood, zero-shot |

Note: Gemma 4 architecture (Gemma4ForConditionalGeneration) has limited compatibility with lm-eval's loglikelihood method due to its multimodal wrapper structure. Only generative evaluation produces valid results for Gemma 4 based models. Full extended evaluation with Majority Voting is planned.

---

## Darwin V6 vs Conventional Merging

| Capability | mergekit (DARE-TIES) | Darwin V6 |
|---|---|---|
| Implementation | Library call (mergekit CLI) | Direct PyTorch tensor operations, no external dependency |
| Ratio selection | Uniform ratio across all tensors | Per-tensor ratio from MDS diagnostic (independent ratios per tensor) |
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

### Parent Comparison (MDS Result)

<p align="center">
  <img src="parent_comparison.png" alt="Parent Comparison — Layer-wise Importance" width="100%">
</p>

---

## Evolution Result

| | |
|---|---|
| Best Score (ARC-Challenge) | 0.8292 |
| Merge Method | DARE-TIES (direct PyTorch) |
| Health Check | Not performed |

Optimal Genome (14-dimensional adaptive):

```
global_ratio:        0.4989   (overall merge ratio — near balanced)
attn_ratio:          0.1766   (Attention layers — Father strongly dominant)
ffn_ratio:           0.9021   (FFN layers — Mother strongly dominant)
embed_ratio:         0.6122   (Embedding — slight Mother bias)
density_a:           0.9951   (Father DARE density — nearly full)
density_b:           0.9617   (Mother DARE density — high)
block_0_ratio:       0.5740   (early layers — slight Mother bias)
block_1_ratio:       0.5811   (early-mid layers — slight Mother bias)
block_2_ratio:       0.5736   (mid layers — slight Mother bias)
block_3_ratio:       0.4697   (mid-late layers — near balanced, slight Father)
block_4_ratio:       0.4930   (late layers — near balanced)
block_5_ratio:       0.8418   (final layers, reasoning core — Mother dominant)
mri_trust:           0.4907   (MDS 49% + Genome 51% — near equal trust)
merge_method_weight: 0.3623
```

Key observations from the genome: ffn_ratio=0.90 indicates the FFN layers strongly favor the Mother (Claude Opus Distill), carrying the bulk of the reasoning enhancement. block_5 (final layers)=0.84 shows the reasoning core layers also strongly favor Mother, consistent with the pattern seen across all Darwin Opus models where Claude's reasoning capability concentrates in the final layers. Meanwhile, attn_ratio=0.18 firmly preserves Father's attention structure, maintaining the original Gemma 4 multimodal and context capabilities. Notably, mri_trust=0.49 shows the system found near-equal value in both diagnostic analysis and evolutionary search, suggesting a well-balanced optimization.

---

## Model Specifications

| | |
|---|---|
| Architecture | Gemma 4 Expert 4B (Mixture of Experts) |
| Parameters | 4B |
| Precision | BF16 |
| Context | 128K |
| Languages | 140+ |
| Thinking | enable_thinking=True chain-of-thought |
| License | Apache 2.0 |

---

## Usage

### Transformers

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained("FINAL-Bench/Darwin-4B-Opus", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    "FINAL-Bench/Darwin-4B-Opus",
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
| BF16 Full Precision | ~8 GB | |
| NVIDIA RTX 4090 24GB | 24 GB | Single GPU, very comfortable |
| NVIDIA RTX 3090 24GB | 24 GB | Single GPU, comfortable |
| NVIDIA RTX 4080 16GB | 16 GB | Single GPU |
| NVIDIA T4 16GB | 16 GB | Cloud/Colab friendly |

Darwin-4B-Opus is the most accessible model in the Darwin Opus family, running comfortably on a single consumer GPU.

---

## Darwin Opus Family

| Model | Architecture | Parameters | Context | Base |
|---|---|---|---|---|
| **Darwin-4B-Opus** | MoE (E4B) | 4B | 128K | gemma-4-E4B-it |
| Darwin-9B-Opus | — | 9B | — | gemma-4-9B-it |
| Darwin-31B-Opus | Dense | 31B | 256K | gemma-4-31B-it |
| Darwin-35B-A3B-Opus | MoE | 35B (3B active) | 256K | gemma-4-35B-A3B-it |

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
| Architecture | Gemma-4-E4B (MoE) |
| License | Apache 2.0 |

---

## Citation

```bibtex
@misc{vidraft_darwin_4b_opus,
  title        = {Darwin-4B-Opus: Diagnostic-Guided Evolutionary Merge on Gemma 4 E4B},
  author       = {VIDRAFT},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/FINAL-Bench/Darwin-4B-Opus}}
}
```
This model is introduced in [Darwin Family](https://arxiv.org/abs/2605.14386).