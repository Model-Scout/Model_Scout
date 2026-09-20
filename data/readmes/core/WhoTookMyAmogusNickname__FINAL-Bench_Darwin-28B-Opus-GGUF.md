---
quantized_by: bartowski
pipeline_tag: text-generation
base_model: FINAL-Bench/Darwin-28B-Opus
tags:
  - darwin
  - darwin-v7
  - evolutionary-merge
  - merge
  - mergekit
  - reasoning
  - advanced-reasoning
  - chain-of-thought
  - thinking
  - qwen3.6
  - qwen
  - claude-opus
  - distillation
  - multilingual
  - gpqa
  - benchmark
  - open-source
  - apache-2.0
  - hybrid-vigor
  - proto-agi
  - vidraft
  - eval-results
language:
  - en
  - zh
  - ko
  - ja
  - multilingual
license: apache-2.0
base_model_relation: quantized
model-index:
  - name: Darwin-28B-Opus
    results:
      - task:
          type: text-generation
          name: Graduate-Level Reasoning
        dataset:
          type: Idavidrein/gpqa
          name: GPQA Diamond
          config: gpqa_diamond
          split: train
        metrics:
          - type: accuracy
            value: 88.89
            name: Accuracy
            verified: false
---

GGUF quantizations of [FINAL-Bench/Darwin-28B-Opus](https://huggingface.co/FINAL-Bench/Darwin-28B-Opus)

llama.cpp commit used for conversion: [27aef3d](https://github.com/ggml-org/llama.cpp/commit/27aef3dd91e7cde049e7c242dbf6c8fe86574d01)\
llama.cpp build used for quantization: [b8983](https://github.com/ggml-org/llama.cpp/releases/tag/b8983)

Current quants are static(non-imatrix), if you want imatrix quants, please open a discussion.

# Original model card below:

---

# Darwin-28B-Opus — Qwen3.6-27B × Opus-Distilled Evolutionary Merge

<p align="center">
  <a href="https://huggingface.co/FINAL-Bench/Darwin-28B-Opus"><img src="https://img.shields.io/badge/⭐_GPQA_Diamond-88.89%25_Darwin--28B--Opus-gold?style=for-the-badge" alt="GPQA"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-36B-Opus"><img src="https://img.shields.io/badge/🧬_Sibling-Darwin--36B--Opus_(88.4%25)-blue?style=for-the-badge" alt="36B"></a>
</p>

<p align="center">
  <a href="https://huggingface.co/FINAL-Bench/Darwin-4B-Genesis"><img src="https://img.shields.io/badge/🧬_Model-Darwin--4B--Genesis-blue?style=for-the-badge" alt="Genesis"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-9B-Opus"><img src="https://img.shields.io/badge/🧬_Model-Darwin--9B--Opus-blue?style=for-the-badge" alt="9B"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-9B-NEG"><img src="https://img.shields.io/badge/⚡_Model-Darwin--9B--NEG_(84.3%25)-purple?style=for-the-badge" alt="NEG"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-27B-Opus"><img src="https://img.shields.io/badge/🧬_Model-Darwin--27B--Opus_(86.9%25)-blue?style=for-the-badge" alt="27B"></a>
</p>

<p align="center">
  <a href="https://huggingface.co/FINAL-Bench/Darwin-31B-Opus"><img src="https://img.shields.io/badge/🧬_Model-Darwin--31B--Opus_(85.9%25)-blue?style=for-the-badge" alt="31B"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-36B-Opus"><img src="https://img.shields.io/badge/⭐_Model-Darwin--36B--Opus_(88.4%25)-blue?style=for-the-badge" alt="36B"></a>
</p>

<p align="center">
  <a href="https://huggingface.co/collections/FINAL-Bench/darwin-family"><img src="https://img.shields.io/badge/🏠_Darwin_Family-Collection-green?style=for-the-badge" alt="Family"></a>
  <a href="https://huggingface.co/spaces/FINAL-Bench/Leaderboard"><img src="https://img.shields.io/badge/🏆_FINAL_Bench-Leaderboard-green?style=for-the-badge" alt="FINAL Bench"></a>
</p>

> Qwen3.6-27B dense · 27.6B parameters · Hybrid Linear/Full Attention · BF16 · Thinking Mode · Apache 2.0
> **Darwin V7 evolutionary merge: Father × Opus-distilled Mother → 88.89% on GPQA Diamond (3-stage adaptive evaluation)**

---

## Abstract

**Darwin-28B-Opus** is the first reasoning model of the Darwin series built on the **Qwen3.6 generation** backbone. Produced by the Darwin V7 evolutionary breeding engine from two publicly available parents, it combines the strong bilingual reasoning of Qwen3.6-27B with Claude Opus 4-style chain-of-thought distilled behaviour.

On the **GPQA Diamond** graduate-level reasoning benchmark (198 PhD-level questions), Darwin-28B-Opus scores **88.89 %** under the standard 3-stage adaptive evaluation, slightly edging out its larger MoE sibling Darwin-36B-Opus (88.4 %) and clearly surpassing its Qwen3.5-generation counterpart Darwin-27B-Opus (86.9 %).

---

## 🧬 Model Lineage

| Role | Model | Role in the Merge |
|:---:|:---|:---|
| **Father (父)** | [`Qwen/Qwen3.6-27B`](https://huggingface.co/Qwen/Qwen3.6-27B) | Qwen3.6 generation dense backbone with hybrid linear/full attention. |
| **Mother (母)** | [`rico03/Qwen3.6-27B-Claude-Opus-Reasoning-Distilled`](https://huggingface.co/rico03/Qwen3.6-27B-Claude-Opus-Reasoning-Distilled) | Claude Opus reasoning-distilled variant of the same backbone (Jackrong-style distillation, 14 k traces). |
| **Offspring** | **`Darwin-28B-Opus`** (this model) | Darwin V7 evolutionary merge; Qwen3.6 architecture retained, Opus reasoning style inherited. |

> **Why 28B?** The `28B` label denotes the Qwen3.6-generation member of the Darwin lineup (`+1` over the Qwen3.5-era `Darwin-27B-Opus`).
> The actual parameter count is **27.6 B**, and the architecture exactly follows Qwen3.6-27B.

---

## ⚙️ Technical Specifications

| Component | Value |
|:---|:---|
| Architecture | `Qwen3_5ForConditionalGeneration` (Qwen3.6 generation, hybrid linear + full attention) |
| Parameters | **27.6 B** (BF16) |
| Hidden size | 5 120 |
| Intermediate size | 17 408 |
| Head dim | 256 |
| Layers | 64 (3 linear : 1 full attention, `full_attention_interval = 4`) |
| Precision | bfloat16 |
| Context length | Inherited from base (long-chain reasoning supported) |
| License | Apache 2.0 |

---

## 🏆 Benchmark — GPQA Diamond (198 questions)

Darwin-28B-Opus is evaluated under our standard **3-stage adaptive evaluation** protocol, identical to the protocol used across the Darwin series.

| Stage | Decoding Protocol | Cost | **Accuracy** |
|:---:|:---|:---:|:---:|
| **Stage 1** | Single-shot greedy baseline | 1× | **74.75 %** (148 / 198) |
| **Stage 2** | Majority vote ×8 at temperature 0.7 on Stage-1 wrongs | 8× | **83.84 %** (166 / 198) |
| **Stage 3** | Adaptive ensemble refinement (close-tie tiebreaker + iterative MTI on residual hard questions) | ≈ 20× | **🥇 88.89 %** (176 / 198) |

**Key performance indicators**:
- Stage 1 → Stage 3: **+14.14 %p** through adaptive protocol
- vs Darwin-27B-Opus (86.9 %): **+1.99 %p**
- vs Darwin-36B-Opus (88.4 %): **+0.49 %p**
- vs Darwin-31B-Opus (85.9 %): **+2.99 %p**

---

## 🚀 Usage

### Standard inference (Stage 1 baseline)

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tok = AutoTokenizer.from_pretrained(
    "FINAL-Bench/Darwin-28B-Opus",
    trust_remote_code=True,
)
model = AutoModelForCausalLM.from_pretrained(
    "FINAL-Bench/Darwin-28B-Opus",
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)

messages = [
    {"role": "user",
     "content": "Solve: If f(x) = x³ − 3x + 2, find all critical points and classify them."}
]
text = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tok(text, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=2048, do_sample=False)
print(tok.decode(outputs[0][inputs.input_ids.shape[-1]:], skip_special_tokens=True))
```

### Enhanced accuracy (Stage 2-3 adaptive)

For leaderboard-grade accuracy, combine:
1. Stage 1 greedy baseline,
2. Stage 2 maj@8 temperature sampling on low-confidence answers,
3. Stage 3 adaptive refinement on still-disputed answers.

Reference implementation is provided in the Darwin-series evaluation harness.

---

## 🎯 Recommended Use-Cases

- **Graduate-level STEM reasoning** (GPQA / science qualifying exams)
- **Mathematical problem solving** (MATH, AIME-style problems)
- **Code generation and debugging** (HumanEval, MBPP)
- **Complex multi-step chain-of-thought tasks**
- **Bilingual reasoning** (strong English + Korean; also Chinese / Japanese)

## ⚠️ Limitations

- At 27.6 B parameters in bfloat16, full inference requires ≈ 55 GB of VRAM (e.g., a single A100-80GB or B200).
- Optimised for English first, with secondary support for Korean, Chinese, and Japanese.
- Deep Opus-style reasoning traces tend to be verbose — control with `max_new_tokens` as needed.

---

## 📚 Citation

```bibtex
@misc{darwin28b_opus_2026,
  title  = {Darwin-28B-Opus: Evolutionary Merging of Qwen3.6-27B with Claude-Opus-Distilled Reasoning},
  author = {FINAL-Bench / Darwin Research Team},
  year   = {2026},
  howpublished = {\url{https://huggingface.co/FINAL-Bench/Darwin-28B-Opus}},
  note   = {Darwin V7 · Mother-centric Ratio Interpolation merge · 88.89 % GPQA Diamond (3-stage)}
}
```

---

## 🔗 Related Darwin Models

- **Darwin-36B-Opus** — MoE 36B, Qwen3.6-35B-A3B × Opus distilled, GPQA 88.4 %
- **Darwin-31B-Opus** — 31B dense, multilingual-strong reasoning, GPQA 85.9 %
- **Darwin-27B-Opus** — 27B dense (Qwen3.5 generation), GPQA 86.9 %
- **Darwin-9B-NEG** — 9B with Native Entropy Gating, GPQA 84.3 %
- **Darwin-9B-Opus** — the Qwen3.5-9B Darwin member
- **Darwin-4B-Genesis** — smallest Darwin member

---

*Darwin V7 · Qwen3.6 generation flagship · Sealed 2026-04-25 · FINAL-Bench*
