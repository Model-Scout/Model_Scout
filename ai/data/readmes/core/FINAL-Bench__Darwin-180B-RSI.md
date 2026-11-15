---
license: other
license_name: qwen-community-1.0
license_link: LICENSE
language: [en, ko, zh, ja, multilingual]
library_name: transformers
pipeline_tag: image-text-to-text
tags:
  - darwin
  - darwin-rsi
  - recursive-self-improvement
  - self-improvement
  - vidraft
  - final-bench
  - qwen
  - qwen3.8
  - moe
  - mixture-of-experts
  - sparse-moe
  - 180b
  - hybrid-attention
  - linear-attention
  - long-context
  - 262k-context
  - vision-language
  - multimodal
  - reasoning
  - reasoning-model
  - thinking
  - chain-of-thought
  - math
  - science
  - stem
  - ztc
  - model-level-rsi
  - zero-token-confidence
  - confidence-estimation
  - hallucination-detection
  - gpqa
  - gpqa-diamond
  - mmlu-pro
  - mmmu-pro
  - lexam
  - lexam-hard
  - ifstruct
  - mdpbench
  - document-parsing
  - ocr
  - structured-output
  - eval-results
  - korean
  - english
  - vllm
  - openai-compatible
  - b200
model-index:
  - name: Darwin-180B-RSI
    results:
      - task: {type: text-generation, name: Graduate-Level Reasoning}
        dataset: {type: Idavidrein/gpqa, name: GPQA Diamond, config: gpqa_diamond, split: train}
        metrics:
          - {type: accuracy, value: 94.44, name: "Accuracy (majority vote, up to 16 samples, 131K thinking)", verified: false}
      - task: {type: text-generation, name: Multi-discipline Knowledge & Reasoning}
        dataset: {type: TIGER-Lab/MMLU-Pro, name: MMLU-Pro, split: test}
        metrics:
          - {type: accuracy, value: 88.12, name: "Accuracy (single sample, 131K thinking)", verified: false}
      - task: {type: image-text-to-text, name: Multimodal Expert Reasoning}
        dataset: {type: MMMU/MMMU_Pro, name: MMMU-Pro (vision), config: vision, split: test}
        metrics:
          - {type: accuracy, value: 79.48, name: "Accuracy (majority vote, 3 samples, 131K thinking)", verified: false}
      - task: {type: text-generation, name: Legal Reasoning}
        dataset: {type: LEXam-Benchmark/LEXam, name: LEXam (MCQ, 4 choices), config: mcq_4_choices, split: test}
        metrics:
          - {type: accuracy, value: 68.94, name: "Accuracy (majority vote, 4 samples, 32K thinking)", verified: false}
      - task: {type: text-generation, name: Legal Reasoning (open-ended)}
        dataset: {type: joelniklaus/LEXam-hard, name: LEXam-hard, split: test}
        metrics:
          - {type: score, value: 45.72, name: "Judge score (DeepSeek-R1-0528, single sample)", verified: false}
      - task: {type: image-text-to-text, name: Multilingual Document Parsing}
        dataset: {type: Delores-Lin/MDPBench, name: MDPBench (public), split: overall}
        metrics:
          - {type: score, value: 83.65, name: "Overall (official scoring, thinking on)", verified: false}
      - task: {type: text-generation, name: Structured Output Compliance}
        dataset: {type: LiquidAI/ifstruct-v1.0, name: IFStruct v1.0, split: test}
        metrics:
          - {type: accuracy, value: 98.95, name: "Pass rate (official harness, temperature 0, thinking on)", verified: false}
      - task: {type: text-generation, name: Competition Mathematics}
        dataset: {type: MathArena/aime_2026, name: AIME 2026, split: train}
        metrics:
          - {type: accuracy, value: 100.0, name: "Accuracy (majority vote, 16 samples, 131K thinking)", verified: false}
          - {type: accuracy, value: 98.75, name: "Mean accuracy over 16 samples", verified: false}
      - task: {type: text-generation, name: Competition Mathematics}
        dataset: {type: MathArena/hmmt_feb_2026, name: HMMT Feb 2026, split: train}
        metrics:
          - {type: accuracy, value: 100.0, name: "Accuracy (majority vote, 16 samples, 131K thinking)", verified: false}
          - {type: accuracy, value: 96.59, name: "Mean accuracy over 16 samples", verified: false}
---
<!-- SUPERCLUE-2026-11:START -->
## 🏆 SuperCLUE November 2026: #1 open-weight model in math and science reasoning

[![SuperCLUE Nov 2026: Darwin-180B-RSI #1 open-weight, #2 overall in math and science reasoning](https://huggingface.co/datasets/VIDraft/press-assets/resolve/main/press/superclue_banner_darwin_2026-11.png)](https://www.superclueai.com/homepage)

**This model line was evaluated by [SuperCLUE](https://www.superclueai.com/homepage), China's most widely cited LLM benchmark, on its private November 2026 test set.** Darwin-180B-RSI-R3 scored **73.68 in mathematical and scientific reasoning: #1 among open-weight models and #2 overall** among 19 models, right behind OpenAI's GPT-6.1-Sol (76.32) and ahead of Google Gemini-4-Argon (71.05), DeepSeek-V4.1-Flash (71.05), xAI Grok-4.7 (68.42) and Qwen3.8-Max (68.42). On the overall intelligence index it placed 9th of 19 and 5th among open-weight models. It is the only Korean model on the board.

| Model | Developer | Open weights | Math & science reasoning |
|---|---|---|---|
| GPT-6.1-Sol | OpenAI | No | 76.32 |
| **Darwin-180B-RSI-R3** | **VIDRAFT** | **Yes** | **73.68** |
| Gemini-4-Argon | Google | No | 71.05 |
| DeepSeek-V4.1-Flash | DeepSeek | Yes | 71.05 |
| Grok-4.7 | xAI | No | 68.42 |
| Qwen3.8-Max-0902 | Alibaba | No | 68.42 |
| GLM-5.3 | Zhipu AI | Yes | 65.79 |
| Kimi-K3.1-Pro | Moonshot | Yes | 63.16 |
| Qwen3.8-Flash (parent of Darwin-180B) | Alibaba | Yes | 57.89 |

Darwin-180B-RSI inherited its expert layers from Qwen3.8-Flash-Next and rebuilt only the attention and shared-expert layers through recursive self-improvement. On the same board the parent, Qwen3.8-Flash, placed 15th overall (39.81) with 57.89 in math and science reasoning; Darwin placed 9th (43.08) with 73.68.

<details><summary>Overall intelligence index, November 2026 (screenshot)</summary>

![SuperCLUE Nov 2026 intelligence index](https://huggingface.co/datasets/VIDraft/press-assets/resolve/main/press/superclue_intelligence_index_2026-11.png)

</details>

Source: [SuperCLUE general leaderboard, November 2026](https://www.superclueai.com/homepage) (screenshots taken November 5, 2026). Scores are SuperCLUE's, not VIDRAFT's.
<!-- SUPERCLUE-2026-11:END -->


# Darwin-180B-RSI

### 180B Mixture-of-Experts · vision-language · **#1 on ten Hugging Face official leaderboards**: nine by this model (MDPBench 83.65 · IFStruct 98.95 · AIME 2026 100 · HMMT Feb 2026 100 · GPQA Diamond 94.44 · MMLU-Pro 88.12 · MMMU-Pro 79.48 · LEXam 68.94 · LEXam-hard 45.72) and ExtractBench 90.29 by its next round R3 · **self-improving**

> 💻 **Run it on your own machine — [POCKET-Darwin-180B-GGUF](https://huggingface.co/FINAL-Bench/POCKET-Darwin-180B-GGUF)**: the 4-bit GGUF of R3 (111 GB) runs on a **laptop with an 8 GB GPU and 32 GB RAM**, **CPU only at 18–21 tok/s**, a 128 GB mini PC or one DGX Spark — MMLU-Pro **identical to BF16 (87.65%)**.

> 🥇 **NEW: #1 on [MDPBench](https://huggingface.co/datasets/Delores-Lin/MDPBench) (83.65)**, multilingual document parsing across 17 languages, digital and photographed pages, ahead of Kimi-K3 (83.6) and the dedicated OCR models.

> 🥇 **NEW: #1 on [IFStruct](https://huggingface.co/datasets/LiquidAI/ifstruct-v1.0) (98.95)**, the structured-output compliance benchmark (valid JSON/YAML that follows a requested schema), ahead of Agents-A1 (93.25) and gpt-oss-20b (91.95).

> 🥇 **NEW: [Darwin-180B-RSI-R3](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI-R3), the next self-improvement round of this model, is #1 on the [ExtractBench](https://huggingface.co/datasets/llamaindex/ExtractBench) leaderboard (90.29)** and #3 on [EvasionBench](https://huggingface.co/datasets/FutureMa/EvasionBench) (77.83).

`reasoning` · `MoE 512 experts` · `262K long context` · `image + text` · `Korean + English` · `self-improvement` · `ZTC`

<p align="center">
<a href="https://vidraft.net"><img src="https://img.shields.io/badge/🌐_VIDRAFT-vidraft.net-111827?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/Idavidrein/gpqa"><img src="https://img.shields.io/badge/GPQA_Diamond-94.44%25_%231-gold?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro"><img src="https://img.shields.io/badge/MMLU--Pro-88.12%25_%231-2563eb?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/MMMU/MMMU_Pro"><img src="https://img.shields.io/badge/MMMU--Pro-79.48%25_%231-0891b2?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/MathArena/aime_2026"><img src="https://img.shields.io/badge/AIME_2026-100%25_%231-dc2626?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/MathArena/hmmt_feb_2026"><img src="https://img.shields.io/badge/HMMT_Feb_2026-100%25_%231-ea580c?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/LEXam-Benchmark/LEXam"><img src="https://img.shields.io/badge/LEXam_(Law)-68.94%25_%231-4f46e5?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/joelniklaus/LEXam-hard"><img src="https://img.shields.io/badge/LEXam--hard_(Law)-45.72_%231-6d28d9?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/LiquidAI/ifstruct-v1.0"><img src="https://img.shields.io/badge/IFStruct-98.95%25_%231-b45309?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/Delores-Lin/MDPBench"><img src="https://img.shields.io/badge/MDPBench-83.65_%231-0f766e?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/llamaindex/ExtractBench"><img src="https://img.shields.io/badge/ExtractBench_(R3)-90.29_%231-059669?style=for-the-badge"></a>
<a href="https://huggingface.co/FINAL-Bench/Darwin-27B-RSI"><img src="https://img.shields.io/badge/Self--Improving-RSI-e11d48?style=for-the-badge"></a>
<a href="https://huggingface.co/collections/FINAL-Bench/ztc-models-jev-ecosystems"><img src="https://img.shields.io/badge/ZTC-Zero--Token_Confidence-7c3aed?style=for-the-badge"></a>
</p>
<p align="center">
<a href="https://huggingface.co/papers/2605.14386"><img src="https://img.shields.io/badge/arXiv-2605.14386_Darwin_Family-b31b1b?style=for-the-badge"></a>
<a href="https://huggingface.co/papers/2609.20269"><img src="https://img.shields.io/badge/Paper-2609.20269_Latin_Square-b31b1b?style=for-the-badge"></a>
<a href="https://huggingface.co/collections/FINAL-Bench/darwin-family"><img src="https://img.shields.io/badge/🧬_Collection-Darwin_Family-16a34a?style=for-the-badge"></a>
<a href="https://huggingface.co/collections/FINAL-Bench/ztc-models-jev-ecosystems"><img src="https://img.shields.io/badge/🏛️_Collection-ZTC_Models-7c3aed?style=for-the-badge"></a>
<a href="https://huggingface.co/FINAL-Bench/POCKET-Darwin-180B-GGUF"><img src="https://img.shields.io/badge/💻_POCKET_4--bit-Laptop_·_CPU_only_·_DGX_Spark-0f766e?style=for-the-badge"></a>
</p>

**The newest flagship of the Darwin family: #1 on MDPBench, IFStruct, AIME 2026, HMMT Feb 2026, GPQA Diamond, MMLU-Pro, MMMU-Pro, LEXam and LEXam-hard,
and a model that gets better by learning from its own verified work.**

---

## 🏆 Head-to-head with Chinese frontier models

![Darwin-180B-RSI vs Chinese frontier models](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI/resolve/main/assets/bench_vs_china.png)

![Five leaderboards — full field](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI/resolve/main/assets/bench_field.png)

Scores as listed on the Hugging Face **official** benchmark leaderboards (self-reported by each model's publisher).
🥇 = #1 on that leaderboard. "—" = not reported.

| Model | AIME 2026 | GPQA Diamond | MMLU-Pro | MMMU-Pro | HMMT Feb 2026 | LEXam | LEXam-hard |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **🧬 Darwin-180B-RSI (ours · 🇰🇷)** | **100** 🥇 | **94.44** 🥇 | **88.12** 🥇 | **79.48** 🥇 | **100** 🥇 | **68.94** 🥇 | **45.72** 🥇 |
| Inkling (Thinking Machines) | — | — | — | — | — | — | 40.82 |
| Kimi-K3 (Moonshot AI) | — | 93.5 | — | — | — | — | 29.54 |
| Kimi-K2.6 (Moonshot AI) | 96.4 | 90.5 | — | 79.4 | 92.7 | — | 36.18 |
| DeepSeek-V4-Pro (DeepSeek) | — | 90.1 | 87.5 | — | — | — | 38.93 |
| Qwen3.5-397B-A17B (Alibaba) | 93.33 | 88.4 | 87.8 | — | 87.88 | — | — |
| MiniMax-M2.1 (MiniMax) | — | 80.81 | 88 | — | — | — | — |
| GLM-5 (Zhipu AI) | 95.83 | 86 | 86 | — | 86.36 | — | — |
| Intern-S2-Preview (Shanghai AI Lab) | — | — | 88 | 76.88 | 87.31 | — | — |
| Step-3.5-Flash (StepFun) | 96.67 | 83.5 | 84.4 | — | 86.36 | — | — |
| DeepSeek-R1 (DeepSeek) | — | — | — | — | — | 52.41 | — |
| Qwen3-235B-A22B-Thinking-2507 (Alibaba) | — | — | — | — | — | 48.19 | — |

<sub>This comparison covers open-weight models listed on the Hugging Face official benchmark leaderboards; closed API models are not included. Leaderboard values are each publisher's own reported numbers; settings (samples, voting, thinking budget) differ across models. Darwin-180B-RSI settings are listed in the evaluation protocol below.</sub>

---

## 🧬 The Darwin Family

<p align="center">
<a href="https://huggingface.co/FINAL-Bench/Darwin-397B-ZTC"><img src="https://img.shields.io/badge/Darwin--397B--ZTC-GPQA_93.43-16a34a"></a>
<a href="https://huggingface.co/FINAL-Bench/Darwin-28B-REASON"><img src="https://img.shields.io/badge/Darwin--28B--REASON-GPQA_89.39-16a34a"></a>
<a href="https://huggingface.co/FINAL-Bench/Darwin-35B-A3B-Opus"><img src="https://img.shields.io/badge/Darwin--35B--A3B--Opus-♥98-e11d48"></a>
<a href="https://huggingface.co/FINAL-Bench/Darwin-36B-Opus"><img src="https://img.shields.io/badge/Darwin--36B--Opus-♥97-e11d48"></a>
<a href="https://huggingface.co/FINAL-Bench/Darwin-4B-Genesis"><img src="https://img.shields.io/badge/Darwin--4B--Genesis-♥63-e11d48"></a>
</p>
<p align="center">
<a href="https://huggingface.co/FINAL-Bench/Darwin-9B-NEG"><img src="https://img.shields.io/badge/Darwin--9B--NEG-♥57-e11d48"></a>
<a href="https://huggingface.co/FINAL-Bench/POCKET-35B-GGUF"><img src="https://img.shields.io/badge/POCKET--35B-824K_↓-1f6feb"></a>
<a href="https://huggingface.co/FINAL-Bench/POCKET-26B-GGUF"><img src="https://img.shields.io/badge/POCKET--26B-365K_↓-1f6feb"></a>
<a href="https://huggingface.co/FINAL-Bench/POCKET-EN-GGUF"><img src="https://img.shields.io/badge/POCKET--EN-♥43-1f6feb"></a>
<a href="https://huggingface.co/FINAL-Bench/POCKET-KR-GGUF"><img src="https://img.shields.io/badge/POCKET--KR-♥36-1f6feb"></a>
<a href="https://huggingface.co/FINAL-Bench/POCKET-Darwin-180B-GGUF"><img src="https://img.shields.io/badge/POCKET--Darwin--180B-NEW_·_4--bit_·_laptop-1f6feb"></a>
</p>

**Darwin** is [VIDRAFT](https://vidraft.net)'s measurement-driven reasoning model family —
**50+ official models**, **400+ community derivatives**, and now **two places in the GPQA Diamond top 3**
(Darwin-180B-RSI #1 · Darwin-397B-ZTC #3).

---

## 🧬 Darwin — evolve the parent, keep what works

Darwin treats a strong open model as a **parent**. It measures where the parent is weak,
and strengthens exactly those parts — instead of re-training everything and risking what already works.

- **Diagnose before you change.** Every Darwin generation starts from a measured weakness map of the parent.
- **Change little, precisely.** Darwin modifies a small, targeted fraction of the network. Knowledge stored in the experts is preserved.
- **Proven capability over new guesses.** Earlier Darwin generations grafted the best-performing expert/FFN blocks from other strong models onto a base backbone; Darwin-180B-RSI adds a new ingredient — **the model's own verified work**.
- **Measured, not claimed.** Every change must beat the parent on held-out tests before it ships.

| Model | Scale | GPQA Diamond |
|:---|:---|:---:|
| Darwin-9B-NEG | 9B | 84.3 |
| Darwin-27B-Opus | 27B dense | 86.9 |
| Darwin-36B-Opus | 36B MoE | 88.4 |
| Darwin-28B-REASON | 28B + DELPHI | 89.39 |
| Darwin-397B-ZTC | 397B MoE (FP8) | 93.43 |
| **Darwin-180B-RSI** | **180B MoE** | **94.44** |

### Lineage

| Role | | |
|:---|:---|:---|
| **Parent** | `Qwen/Qwen3.8-Flash-Next` | 180B MoE vision-language backbone · Qwen Community License 1.0 |
| **Darwin RSI** | self-improvement on verified answers | the parent's own solutions, checked against verifiable answer keys, fed back as training signal |
| **Preserved** | 512 routed experts · router · vision encoder | untouched — the parent's knowledge stays intact |
| **ZTC** | zero-token confidence readout | see below |

---

## 📄 Darwin Platform & Research

- **Darwin Family** — MRI trust-weighted evolutionary merging for training-free scaling of language-model reasoning ([arXiv:2605.14386](https://huggingface.co/papers/2605.14386))
- **Placement Is Free, Composition Is Not** — the Latin square as a provably-balanced construction for heterogeneous sequence-mixer stacks ([2609.20269](https://huggingface.co/papers/2609.20269)) — the AETHER architecture line
- **FINAL Bench** — VIDRAFT's measurement-driven evaluation framework (SSRN)
- **Four-layer Pre-AGI roadmap** — Darwin → AETHER → PROMETHEUS → HEPHAESTUS
- Collections: [Darwin Family](https://huggingface.co/collections/FINAL-Bench/darwin-family) · [ZTC Models — JEV ecosystems](https://huggingface.co/collections/FINAL-Bench/ztc-models-jev-ecosystems)

---

## 🔁 RSI — a model that improves from its own work

**Recursive self-improvement (RSI)** is the core of this generation.
Instead of distilling a bigger teacher, the model improves by learning from itself:

1. **Solve** — the model works through practice problems it has never seen in evaluation.
2. **Verify** — its answers are checked against verifiable references (answer keys, executable checks). Nothing unverified is learned.
3. **Learn** — it is re-trained on the reasoning that turned out to be correct.
4. **Repeat** — the improved model becomes the next solver.

What it bought in this release:

| | Parent (Qwen3.8-Flash-Next) | **Darwin-180B-RSI** |
|:---|:---:|:---:|
| Average reasoning length (MMLU-Pro) | 4,320 tokens | **3,833 tokens (−11 %)** |
| MMLU-Pro accuracy | 88.04 % | **88.12 %** |

**Same or better accuracy with shorter reasoning** — cheaper and faster to serve.
Practice sets are deduplicated against every evaluation set we report (8-gram overlap filter).

### Next round: Darwin-180B-RSI-R3

[Darwin-180B-RSI-R3](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI-R3) is the next RSI round, trained from this model with the same recipe. Its own leaderboard entries (submitted 2026-10-05):

| Benchmark | R3 | Leaderboard |
|:---|:---:|:---|
| **ExtractBench** (370 documents) | **90.29, #1** | [llamaindex/ExtractBench](https://huggingface.co/datasets/llamaindex/ExtractBench) |
| **EvasionBench** (16,726 questions) | **77.83, #3** | [FutureMa/EvasionBench](https://huggingface.co/datasets/FutureMa/EvasionBench) |

### Model-level RSI vs. harness-level RSI

Darwin-180B-RSI is **Model-level RSI**: the model itself (its weights) improves by learning only from its own solutions. No human-written solutions or reasoning traces are used; correctness is checked automatically. **Harness-level RSI** (e.g., Google's RRSI) improves the prompts, tools and workflow around a fixed model. It's like rewriting an employee's manual, while Model-level RSI is the employee getting smarter. The two are complementary.

---

## 🏛️ ZTC — it knows before it answers

**Zero-Token Confidence (ZTC)** reads the model's own internal state **once, before generation**,
and returns the probability that the answer it is about to give is correct — **no extra tokens, no second model.**

```json
{"answer": "...", "confidence": 0.93, "ztc_score": 1.84, "truncated": false}
```

Use it to gate actions: when confidence is low, do not call the tool, escalate, or answer "I don't know".

**What ships with this model**

| File | Role |
|:---|:---|
| `handler.py` | one call returns the answer **and** its confidence as JSON |
| `ztc/ztc_probe_darwin180rsi.npz` | the ZTC readout for this model (final layer, last prompt token) |
| `ztc/usage.py` | minimal example |

```python
from handler import EndpointHandler
h = EndpointHandler("FINAL-Bench/Darwin-180B-RSI")   # local snapshot path
print(h({"inputs": "What is 17 * 23?"}))
# [{"answer": "...391...", "confidence": 0.97, "ztc_score": 2.1, "truncated": false}]
```

Same format as [Darwin-397B-ZTC](https://huggingface.co/FINAL-Bench/Darwin-397B-ZTC). The readout is fitted only on practice data that is disjoint from every benchmark reported here.

**Status: early release.** This probe reaches an AUROC of 0.64 on our held-out validation split: a coarse signal for routing and review, not a correctness guarantee. A retrained probe with more data will replace it. Details in [`ztc/README.md`](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI/blob/main/ztc/README.md).

---

## 🏆 Results

| Benchmark | Score | Setting | Leaderboard |
|:---|:---:|:---|:---|
| **GPQA Diamond** (198) | **94.44** | majority vote over up to 16 samples · 131,072-token thinking budget | [**#1**](https://huggingface.co/datasets/Idavidrein/gpqa) |
| **MMLU-Pro** (12,032) | **88.12** | single sample · 131,072-token thinking budget | [**#1**](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro) |
| **AIME 2026** (30) | **100.0** | majority vote over 16 samples (mean accuracy 98.75) · 131,072-token thinking budget | [**#1**](https://huggingface.co/datasets/MathArena/aime_2026) |
| **HMMT Feb 2026** (33) | **100.0** | majority vote over 16 samples (mean accuracy 96.59) · 131,072-token thinking budget | [**#1**](https://huggingface.co/datasets/MathArena/hmmt_feb_2026) |
| **MMMU-Pro** (vision, 1,730) | **79.48** | majority vote over 3 samples · 131,072-token thinking budget | [**#1**](https://huggingface.co/datasets/MMMU/MMMU_Pro) |
| **LEXam** (law, MCQ 4-choice, 1,655) | **68.94** | majority vote over 4 samples (single sample 60.54 · mean 61.42) · 32,768-token thinking budget | [**#1**](https://huggingface.co/datasets/LEXam-Benchmark/LEXam) |
| **LEXam-hard** (law, open-ended, 518) | **45.72** | single sample · 32,768-token thinking budget (60 truncated answers regenerated at 120K) · judged by DeepSeek-R1-0528 per the official eval.yaml | [**#1**](https://huggingface.co/datasets/joelniklaus/LEXam-hard) |
| **IFStruct** (structured output, 2,000 prompts) | **98.95** | single run · official harness defaults (temperature 0, 16,000 max tokens) · thinking on | [**#1**](https://huggingface.co/datasets/LiquidAI/ifstruct-v1.0) |
| **MDPBench** (multilingual document parsing, 2,720 pages) | **83.65** | single run · official prompt and scoring (text, formula CDM, table TEDS) · temperature 0 · thinking on | [**#1**](https://huggingface.co/datasets/Delores-Lin/MDPBench) |

### Evaluation protocol

**Common to every benchmark**

| Setting | Value |
|:---|:---|
| Thinking budget | **131,072 tokens** (max generated tokens per sample) |
| Sampling | temperature 1.0 · top_p 0.95 · top_k 20 |
| Precision | bf16 |
| Engine | vLLM, tensor parallel 8 (or 4), expert parallel |

**Per benchmark**

| Benchmark | Samples per question | Reported score |
|:---|:---:|:---|
| AIME 2026 | 16 | majority vote (maj@16); mean over 16 = 98.75 |
| HMMT Feb 2026 | 16 | majority vote (maj@16); mean over 16 = 96.59 |
| GPQA Diamond | up to 16 | majority vote |
| MMLU-Pro | 1 | single sample (no voting) |
| MMMU-Pro (vision) | 3 | majority vote (maj@3) |
| IFStruct | 1 | single run, temperature 0, 16,000 max tokens (official harness defaults) |
| MDPBench | 1 | single run, temperature 0, 32,768 max tokens, thinking on (pages with no transcription re-read with thinking off) |

All numbers are self-measured and reproducible with the settings above. Majority-vote scores are system scores (several samples per question) and are labeled as such.

**MMLU-Pro by category (single sample)** — strongest in math 95.0 · biology 94.6 · physics 92.5; room to grow in law and history.

---

## ⚙️ Specifications

| | |
|:---|:---|
| Architecture | Mixture-of-Experts, hybrid attention (36 linear-attention + 12 full-attention layers) |
| Layers / hidden | 48 / 2,560 |
| Experts | 512 routed (10 active per token) + shared expert |
| Context | 262,144 tokens |
| Vocabulary | 248,320 |
| Modalities | image + text → text |
| Precision | bf16 (~336 GB) |

---

## 🚀 Quickstart

### Serving with vLLM (8 × B200 or equivalent)

```bash
vllm serve FINAL-Bench/Darwin-180B-RSI \
  --tensor-parallel-size 8 --enable-expert-parallel \
  --max-model-len 135168 --trust-remote-code
```

### Chat Completions (OpenAI-compatible)

```python
from openai import OpenAI
c = OpenAI(base_url="http://localhost:8000/v1", api_key="-")
r = c.chat.completions.create(model="FINAL-Bench/Darwin-180B-RSI",
    messages=[{"role": "user", "content": "Explain why the sky is blue in two sentences."}],
    temperature=1.0, top_p=0.95, extra_body={"top_k": 20})
print(r.choices[0].message.content)
```

### Transformers

```python
from transformers import AutoProcessor, AutoModelForImageTextToText
model_id = "FINAL-Bench/Darwin-180B-RSI"
processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForImageTextToText.from_pretrained(model_id, torch_dtype="auto", device_map="auto")
```

**Tip:** this is a thinking model. Give it room — a thinking budget of 32K–131K tokens is recommended for hard reasoning.
Short budgets truncate the reasoning and cost accuracy.

---

## ⚠️ Limitations and disclosure

- Scores are self-measured with the settings stated in the Results table; majority-vote numbers use several samples per question.
- Very long reasoning is normal for hard problems; a short thinking budget will truncate answers and lower accuracy.
- Like every LLM, the model can be confidently wrong — use the ZTC confidence readout to gate high-stakes actions.

---

## 🔗 Related Darwin Models

- **[Darwin-180B-RSI-R3](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI-R3)**: the next RSI round of this model, ExtractBench #1 and EvasionBench #3
- **[Darwin-397B-ZTC](https://huggingface.co/FINAL-Bench/Darwin-397B-ZTC)** — 397B MoE (FP8), GPQA Diamond 93.43 %, ZTC on board
- **[Darwin-28B-REASON](https://huggingface.co/FINAL-Bench/Darwin-28B-REASON)** — 28B, GPQA Diamond 89.39 %
- **[Darwin-36B-Opus](https://huggingface.co/FINAL-Bench/Darwin-36B-Opus)** — 36B MoE, GPQA Diamond 88.4 %
- **[Darwin-27B-RSI](https://huggingface.co/FINAL-Bench/Darwin-27B-RSI)** — 27B, the first Darwin RSI model
- **[Darwin-9B-NEG](https://huggingface.co/FINAL-Bench/Darwin-9B-NEG)** — 9B with Negentropy distillation, GPQA Diamond 84.3 %
- **[ZTC-Judge-27B](https://huggingface.co/FINAL-Bench/ZTC-Judge-27B)** — standalone ZTC judge

---

## 📚 Citation

```bibtex
@misc{darwin180b_rsi_2026,
  title  = {Darwin-180B-RSI: Recursive Self-Improvement on Verified Answers for a 180B Mixture-of-Experts Reasoning Model},
  author = {FINAL-Bench / Darwin Research Team},
  year   = {2026},
  howpublished = {\url{https://huggingface.co/FINAL-Bench/Darwin-180B-RSI}},
  note   = {GPQA Diamond 94.44 \% · MMLU-Pro 88.12 \%}
}

@misc{darwin_family_2026,
  title  = {Darwin Family: MRI-Trust-Weighted Evolutionary Merging for Training-Free Scaling of Language-Model Reasoning},
  author = {Kim, Taebong and Hong, Youngsik and Kim, Minsik and Choi, Sunyoung and Jang, Jaewon and Shin, Junghoon},
  year   = {2026},
  eprint = {2605.14386},
  archivePrefix = {arXiv}
}

@misc{latin_square_2026,
  title  = {Placement Is Free, Composition Is Not: The Latin Square as a Provably-Balanced Construction for Heterogeneous Sequence-Mixer Stacks},
  author = {Kim, Taebong and Hong, Youngsik and Kim, Minsik and Choi, Sunyoung and Jang, Jaewon and Kim, Minseo},
  year   = {2026},
  eprint = {2609.20269},
  archivePrefix = {arXiv}
}
```

---

## 📜 License

Darwin-180B-RSI is a derivative of **Qwen3.8-Flash-Next** and is distributed under the **Qwen Community License 1.0** (see `LICENSE`).

## 🏢 About

Built by **[VIDRAFT](https://vidraft.net)** · evaluated with **FINAL-Bench**.

This model is part of the [Darwin Family](https://huggingface.co/papers/2605.14386).
