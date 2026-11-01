---
license: apache-2.0
language:
- en
- zh
- it
- de
- fr
- es
- ja
- ko
base_model:
- Jackrong/Qwopus3.5-9B-v3.5
- Jackrong/Qwen3.5-9B-GLM5.1-Distill-v1
pipeline_tag: text-generation
library_name: transformers
tags:
- merge
- dare-ties
- qwen3.5
- reasoning
- agentic
- tool-use
- chain-of-thought
- distilled
- gguf
datasets:
- Jackrong/GLM-5.1-Reasoning-1M-Cleaned
- openai/gsm8k
- cais/mmlu
- allenai/ai2_arc
- openai/openai_humaneval
- google/IFEval
---

# Qwopus-GLM-9B-DualReason-Distilled

**A DARE-TIES weight merge of two specialized Qwen3.5-9B fine-tunes**, combining Opus-style agentic reasoning with GLM-5.1 structured chain-of-thought into a single 9B model.

> This model is the result of an extensive research process that explored ANN-based layer routing before converging on DARE-TIES as the optimal merging strategy. The full methodology and findings are documented below.

---

## Benchmark Results

> ⏳ **Evaluation in progress** — Results will be updated shortly.

| Benchmark | Score |
|-----------|-------|
| HumanEval pass@1 | ⏳ |
| MMLU-Pro | ⏳ |
| GSM8K | ⏳ |
| ARC-Challenge | ⏳ |

---

## Model Details

| Property | Value |
|---|---|
| **Base architecture** | Qwen3.5-9B |
| **Parameters** | ~9B |
| **Merge method** | DARE-TIES (weight=0.5, density=0.5) |
| **Context length** | 262,144 tokens |
| **License** | Apache 2.0 |
| **Training hardware** | H100 80GB (Vast.ai) |

---

## Available Quantizations

| Quantization | Size | Use case |
|---|---|---|
| F16 | 17.9 GB | Full precision / re-quantization |
| Q8_0 | 9.5 GB | Near-lossless |
| Q6_K | 7.4 GB | High quality |
| Q5_K_M | 6.5 GB | Recommended for quality |
| Q4_K_M | 5.6 GB | **Best balance** ← start here |
| Q4_0 | 5.3 GB | Fast inference |
| IQ4_XS | 5.2 GB | Efficient 4-bit |
| Q3_K_S | 4.3 GB | Small footprint |
| IQ3_M | 4.4 GB | Small + imatrix |
| Q2_K | 3.8 GB | Minimum quality |

---

## Usage

### With llama.cpp (recommended)

```bash
llama-server \
    -m Qwopus-GLM-9B-DualReason-Distilled-Q4_K_M.gguf \
    --ctx-size 32768 \
    --flash-attn on \
    --n-gpu-layers 99
```

### With Transformers

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model = AutoModelForCausalLM.from_pretrained(
    "rico03/Qwopus-GLM-9B-DualReason-Distilled",
    dtype=torch.bfloat16,
    device_map="cuda",
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained(
    "rico03/Qwopus-GLM-9B-DualReason-Distilled",
    trust_remote_code=True,
)

messages = [{"role": "user", "content": "Solve step by step: 2x + 5 = 13"}]
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to("cuda")

with torch.no_grad():
    output = model.generate(**inputs, max_new_tokens=512, do_sample=False)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

---

## Source Models

All credit for the source models goes to **[Jackrong](https://huggingface.co/Jackrong)**.

### [Jackrong/Qwopus3.5-9B-v3.5](https://huggingface.co/Jackrong/Qwopus3.5-9B-v3.5)
A reasoning-enhanced fine-tune of Qwen3.5-9B trained with ~2x more SFT data than v3, focused on structured reasoning, tool-augmented workflows, and multi-step agentic tasks.
- **HumanEval pass@1**: 87.80%
- **MMLU-Pro**: 90.36%
- **Training guide**: [GitHub](https://github.com/R6410418/Jackrong-llm-finetuning-guide)

### [Jackrong/Qwen3.5-9B-GLM5.1-Distill-v1](https://huggingface.co/Jackrong/Qwen3.5-9B-GLM5.1-Distill-v1)
A distilled variant of Qwen3.5-9B trained on high-quality reasoning data from a GLM-5.1 teacher model (~700x scale). Focused on structured reasoning, instruction-following, and problem decomposition.
- **Training data**: `Jackrong/GLM-5.1-Reasoning-1M-Cleaned`

---

## Why DARE-TIES and Not a Frankenmerge

This model went through an extensive research process before arriving at DARE-TIES.

### Step 1 — ANN Router (abandoned)

We designed a lightweight ANN router (~1M parameters) to learn optimal layer selection between the two models:

```
Input hidden states (both models)
         ↓
LayerRouter MLP: Linear(8320,1024) → SiLU → LayerNorm → Dropout → Linear(1024,256) → SiLU → LayerNorm → Linear(256,1)
         ↓
α ∈ [0,1] per layer → mixed = α × h_qwopus + (1-α) × h_glm
```

Trained on 12,297 examples from GSM8K, MMLU, ARC-Challenge, HumanEval, and IFEval with entropy regularization. **Result:** the router consistently collapsed to always selecting one model regardless of training objective — entropy loss or cross-entropy.

### Step 2 — Cosine Similarity Analysis

To understand why, we computed cosine similarity between hidden states of both models across all 32 layers on 12,297 examples:

| Layer | CosSim | Layer | CosSim | Layer | CosSim | Layer | CosSim |
|-------|--------|-------|--------|-------|--------|-------|--------|
| 00 | 1.000 | 08 | 0.994 | 16 | 0.994 | 24 | 0.996 |
| 01 | 1.000 | 09 | 0.996 | 17 | 0.994 | 25 | 0.996 |
| 02 | 0.999 | 10 | 0.996 | 18 | 0.996 | 26 | 0.996 |
| 03 | 0.999 | 11 | 0.997 | 19 | 0.996 | 27 | 0.995 |
| 04 | 0.998 | 12 | 0.996 | 20 | 0.996 | 28 | 0.994 |
| 05 | 0.998 | 13 | 0.996 | 21 | 0.996 | 29 | 0.993 |
| 06 | 0.996 | 14 | 0.994 | 22 | 0.997 | 30 | 0.993 |
| 07 | 0.995 | 15 | 0.993 | 23 | 0.996 | 31 | 0.992 |

**Conclusion:** Cosine similarity of 0.992–1.000 across all layers means the two models produce nearly identical hidden states. They differ in their **weights**, not in the structure of their internal representations. Layer-by-layer selection adds no value — the optimal combination must happen at the weight level.

### Step 3 — DARE-TIES (adopted)

DARE-TIES operates directly on model weights, interpolating the specialized knowledge of both models continuously:

```python
tv_g   = weights_glm - weights_qwopus      # task vector
mask   = torch.rand_like(tv_g) < 0.5       # DARE dropout
tv_g   = tv_g * mask / 0.5
sign   = tv_g.sign()                        # TIES sign resolution
tv_g   = tv_g * (tv_g.sign() == sign).float()
merged = weights_qwopus + 0.5 * tv_g       # final merge
```

Unlike Jackrong's frankenmerge which makes a **binary** choice per layer, DARE-TIES produces a **continuous interpolation** of both models' knowledge at every weight.

---

## Why No DPO/SFT

We explored DPO post-training but abandoned it after careful analysis. The primary dataset (GLM-5.1-Reasoning-1M-Cleaned) has a median chosen length of **3,225 tokens**. With max_length=512, 95.8% of examples get truncated — the chosen response (with full thinking) gets cut short while the rejected (without thinking) remains intact, **inverting the DPO signal**. This was confirmed empirically: loss dropped from 0.51 to 0.069 in 20 steps (false convergence from corrupted signal).

Correct DPO for this class of model requires max_length ≥ 4,096 and complete long-CoT pairs — addressed in a future version.

---

## References

- **Rethinking Generalization in Reasoning SFT** (Ren et al., 2026) — [arXiv:2604.06628](https://arxiv.org/abs/2604.06628)
- **DARE** — Language Model Merging by Uncertainty-Based Model Pruning
- **TIES** — Resolving Interference When Merging Models
- **Jackrong's fine-tuning guide** — [GitHub](https://github.com/R6410418/Jackrong-llm-finetuning-guide)

---

## Acknowledgements

- **[Jackrong](https://huggingface.co/Jackrong)** — both source models, training pipelines, datasets, and documentation
- **[Qwen team](https://huggingface.co/Qwen)** — Qwen3.5-9B base model
- **GLM-5.1 team** — teacher model used in distillation
- **[Kassadin88](https://huggingface.co/Kassadin88)** — original GLM-5.1-1000000x dataset
- **[KyleHessling1](https://huggingface.co/KyleHessling1)** — Qwopus-GLM-18B-Merged reference benchmark

---

## Citation

```bibtex
@misc{rico03_qwopus_glm_dualreason,
  title     = {Qwopus-GLM-9B-DualReason-Distilled},
  author    = {rico03},
  year      = {2026},
  publisher = {Hugging Face},
  url       = {https://huggingface.co/rico03/Qwopus-GLM-9B-DualReason-Distilled}
}