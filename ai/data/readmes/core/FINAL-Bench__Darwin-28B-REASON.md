---
license: apache-2.0
language:
  - en
  - zh
  - ko
  - ja
  - multilingual
library_name: transformers
pipeline_tag: text-generation
tags:
  - darwin
  - darwin-reason
  - reasoning
  - advanced-reasoning
  - chain-of-thought
  - thinking
  - reasoning-trace-distillation
  - rtd
  - darwin-delphi
  - test-time-compute
  - qwen3.6
  - qwen
  - gpqa
  - benchmark
  - open-source
  - apache-2.0
  - proto-agi
  - vidraft
  - eval-results

base_model_relation: merge
model-index:
- name: Darwin-28B-REASON
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
      value: 89.39
      name: Accuracy
---

> ### 📱 Run it on your phone or a GPU-less PC → **POCKET**  ·  🚀 **[Try it live (CPU chat)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU)**
> VIDRAFT's on-device family: a 35B model that runs on **iPhone** and on **CPU with no GPU** — stock `llama.cpp`, no fork.
>
> [![Live demo](https://img.shields.io/badge/🤗_Space-POCKET_CPU_chat-ffce3a)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU) [![Collection](https://img.shields.io/badge/📚-POCKET_collection-5dbf9a)](https://huggingface.co/collections/FINAL-Bench/pocket-models-6a618ee5d23eafb7e185a5c6) [![35B](https://img.shields.io/badge/POCKET--35B-GGUF-243456)](https://huggingface.co/FINAL-Bench/POCKET-35B-GGUF) [![KR MLX](https://img.shields.io/badge/POCKET--KR-iPhone-0f6e56)](https://huggingface.co/FINAL-Bench/POCKET-KR-MLX) [![EN](https://img.shields.io/badge/POCKET--EN-GGUF-185fa5)](https://huggingface.co/FINAL-Bench/POCKET-EN-GGUF)

>


# Darwin-28B-REASON — Reasoning-Trace Distilled, Darwin-DELPHI Enhanced

<p align="center">
  <a href="https://huggingface.co/FINAL-Bench/Darwin-28B-REASON"><img src="https://img.shields.io/badge/⭐_GPQA_Diamond-89.39%25_Darwin--28B--REASON-gold?style=for-the-badge" alt="GPQA"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-28B-Opus"><img src="https://img.shields.io/badge/🧬_Base-Darwin--28B--Opus_(88.89%25)-blue?style=for-the-badge" alt="Opus"></a>
</p>

<p align="center">
  <a href="https://huggingface.co/FINAL-Bench/Darwin-36B-Opus"><img src="https://img.shields.io/badge/🧬_Model-Darwin--36B--Opus_(88.4%25)-blue?style=for-the-badge" alt="36B"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-27B-Opus"><img src="https://img.shields.io/badge/🧬_Model-Darwin--27B--Opus_(86.9%25)-blue?style=for-the-badge" alt="27B"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-9B-NEG"><img src="https://img.shields.io/badge/⚡_Model-Darwin--9B--NEG_(84.3%25)-purple?style=for-the-badge" alt="NEG"></a>
</p>

<p align="center">
  <a href="https://huggingface.co/collections/FINAL-Bench/darwin-family"><img src="https://img.shields.io/badge/🏠_Darwin_Family-Collection-green?style=for-the-badge" alt="Family"></a>
  <a href="https://huggingface.co/spaces/FINAL-Bench/Leaderboard"><img src="https://img.shields.io/badge/🏆_FINAL_Bench-Leaderboard-green?style=for-the-badge" alt="FINAL Bench"></a>
</p>

> Full standalone reasoning model derived from Darwin-28B-Opus · Reasoning-Trace Distillation (RTD) · Darwin-DELPHI test-time engine · 27.6 B · BF16 · Apache 2.0
> **GPQA Diamond: 89.39 % with Darwin-DELPHI**

---

## Overview

**Darwin-28B-REASON** is a reasoning-enhanced **standalone model** derived from **[Darwin-28B-Opus](https://huggingface.co/FINAL-Bench/Darwin-28B-Opus)**. It combines two components:

1. **Reasoning-Trace Distillation (RTD)** — a reasoning-trace distillation stage applied on top of the Darwin-28B-Opus base, producing this fully self-contained model (full weights, no external adapter required).
2. **Darwin-DELPHI** — a proprietary test-time reasoning engine.

Together they push graduate-level scientific reasoning to the top tier of the Darwin family: **89.39 %** on GPQA Diamond with Darwin-DELPHI. The model is released under **Apache-2.0**.

---

## 🧬 Darwin Platform & Research

**Darwin** is VIDRAFT's measuring-result-driven Korean reasoning model family — approximately **20 official models** plus **400+ community derivatives**, ranking **#3 globally on GPQA** among open models. The base model, **Darwin-28B-Opus**, is the HuggingFace-official **GPQA #3 (88.89 %)** model.

- **Platform technique** — MRI trust-weighted Evolutionary Merge ([arXiv:2605.14386](https://huggingface.co/papers/2605.14386)).
- **FINAL Bench** — VIDRAFT's evaluation framework (SSRN): MetaCognition **+14.05**, MA-ER Gap **0.392**.
- **4-layer Pre-AGI roadmap** — Darwin → AETHER → PROMETHEUS → HEPHAESTUS.

---

## 🧬 Model Lineage

| Role | Model | Contribution |
|:---:|:---|:---|
| **Base** | [`FINAL-Bench/Darwin-28B-Opus`](https://huggingface.co/FINAL-Bench/Darwin-28B-Opus) | GPQA #3 (88.89 %) Qwen3.6-generation reasoning backbone. |
| **RTD training** | reasoning-trace distillation | Distills complete reasoning chains into the model on top of the Opus base. |
| **Test-time engine** | Darwin-DELPHI | Proprietary inference-time consensus engine (not stored in weights). |
| **Result** | **`Darwin-28B-REASON`** (this model) | Full standalone RTD model + Darwin-DELPHI → **89.39 %** GPQA Diamond. |

---

## ⚙️ Technical Specifications

| Component | Value |
|:---|:---|
| Architecture | `Qwen3_5ForConditionalGeneration` (Qwen3.6 generation, hybrid linear + full attention; text path, `language_model_only`) |
| Parameters | **27.6 B** (BF16) — full standalone weights |
| Layers | 64 (3 linear : 1 full attention, `full_attention_interval = 4`) |
| Vocab size | 248 320 |
| Context length | 262 144 (long-chain reasoning supported) |
| Delivery | Full self-contained model — no external base or adapter required |
| Precision | bfloat16 |
| License | Apache 2.0 |

---

## 🔬 Core Techniques

### ① RTD — Reasoning-Trace Distillation

RTD distills **complete reasoning chains** from a publicly available mathematical corpus (Apache-2.0 source) on top of the Darwin-28B-Opus base, producing this standalone model. It strengthens long-form, multi-step scientific reasoning while preserving the base model's bilingual capability.

> The full RTD recipe (curation, trace selection, training schedule) is **proprietary** and is not disclosed.

### ② Darwin-DELPHI — Test-Time Reasoning Engine

**Darwin-DELPHI** is a proprietary test-time engine applied at inference. It performs **multi-sample cross-validation**, **re-examination of uncertain responses**, and **iterative self-critique**, converging to a **consensus** answer through a single-agent Delphi-method procedure.

> Darwin-DELPHI is **not stored in the model weights**. Its internal parameters — sampling counts, stage transitions, and decision thresholds — are a **trade secret** and are not published.

---

## 🏆 Benchmark — GPQA Diamond (198 questions)

GPQA Diamond is a 198-question, PhD-level graduate science reasoning benchmark.

| Model | Engine | **Accuracy** |
|:---|:---|:---:|
| Darwin-28B-Opus (base) | Standard | 88.89 % (176 / 198) |
| **Darwin-28B-REASON** | **Darwin-DELPHI** | **🥇 89.39 % (177 / 198)** |

The evaluation methodology for the Darwin-DELPHI result is **protected**; sample counts, staging, and thresholds are a **trade secret**.

---

## 🚀 Usage

Darwin-28B-REASON is a **full standalone model** — load it directly, no base model or adapter merge required.

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

MODEL = "FINAL-Bench/Darwin-28B-REASON"

tok = AutoTokenizer.from_pretrained(MODEL, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    MODEL,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)
model.eval()

messages = [
    {"role": "user",
     "content": "A particle moves along x(t) = t³ − 6t² + 9t. Find when it is at rest and classify the motion."}
]
text = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tok(text, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=2048)
print(tok.decode(outputs[0][inputs.input_ids.shape[-1]:], skip_special_tokens=True))
```

> The 89.39 % GPQA Diamond result is produced with the Darwin-DELPHI test-time engine applied on top of this model. Darwin-DELPHI is provided through the Darwin-series evaluation harness.

---

## 🎯 Recommended Use-Cases

- **Graduate-level STEM reasoning** (GPQA / science qualifying exams)
- **Mathematical problem solving** (MATH, AIME-style problems)
- **Complex multi-step chain-of-thought tasks**
- **Code generation and debugging**
- **Bilingual reasoning** (strong English + Korean; also Chinese / Japanese)

## ⚠️ Limitations

- The 27.6 B model in bfloat16 requires ≈ 55 GB of VRAM (a single A100-80GB or B200 is sufficient).
- The 89.39 % result depends on the Darwin-DELPHI test-time engine; the model on its own delivers strong but lower single-model accuracy.
- Optimised for English first, with secondary support for Korean, Chinese, and Japanese.
- Reasoning traces tend to be verbose — control with `max_new_tokens` as needed.

---

## 📚 Citation

```bibtex
@misc{darwin28b_reason_2026,
  title  = {Darwin-28B-REASON: Reasoning-Trace Distillation and Darwin-DELPHI Test-Time Reasoning on Darwin-28B-Opus},
  author = {FINAL-Bench / Darwin Research Team},
  year   = {2026},
  howpublished = {\url{https://huggingface.co/FINAL-Bench/Darwin-28B-REASON}},
  note   = {RTD + Darwin-DELPHI · 89.39 % GPQA Diamond}
}

@misc{darwin_family_2026,
  title  = {Darwin Family: MRI Trust-Weighted Evolutionary Merging for Reasoning Models},
  author = {VIDRAFT / FINAL-Bench},
  year   = {2026},
  howpublished = {\url{https://huggingface.co/papers/2605.14386}}
}

@misc{final_bench_2026,
  title  = {FINAL Bench: A Measuring-Result-Driven Evaluation Framework for Reasoning Models},
  author = {VIDRAFT / FINAL-Bench},
  year   = {2026},
  howpublished = {SSRN}
}
```

---

## 🔗 Related Darwin Models

- **Darwin-28B-Opus** — base model, Qwen3.6-27B × Opus distilled, GPQA 88.89 %
- **Darwin-36B-Opus** — MoE 36B, GPQA 88.4 %
- **Darwin-27B-Opus** — 27B dense (Qwen3.5 generation), GPQA 86.9 %
- **Darwin-9B-NEG** — 9B with Negentropy distillation, GPQA 84.3 %
- **Darwin-4B-Genesis** — smallest Darwin member

---

This model is introduced in [Darwin Family](https://huggingface.co/papers/2605.14386).

*Darwin-28B-REASON · RTD + Darwin-DELPHI · 89.39 % GPQA Diamond · FINAL-Bench*
