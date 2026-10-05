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
  - model-level-rsi
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
  - structured-output
  - document-extraction
  - extractbench
  - evasionbench
  - ztc
  - zero-token-confidence
  - eval-results
  - korean
  - english
  - vllm
  - openai-compatible
---

# Darwin-180B-RSI-R3

### 180B Mixture-of-Experts · vision-language · **#1 on ExtractBench (90.29)** · the Darwin-180B-RSI line now holds **nine Hugging Face official #1s**: eight by [Darwin-180B-RSI](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI) (R1) and ExtractBench by R3 · **self-improving**

> 🥇 **R3 is #1 on the [ExtractBench](https://huggingface.co/datasets/llamaindex/ExtractBench) leaderboard (90.29)**, ahead of its own parent Qwen3.8-Flash-Next (89.88), and #3 on [EvasionBench](https://huggingface.co/datasets/FutureMa/EvasionBench) (77.83).

> 💻 **Run it on your own machine: [POCKET-Darwin-180B-GGUF](https://huggingface.co/FINAL-Bench/POCKET-Darwin-180B-GGUF)**, the 4-bit GGUF of R3 (111 GB), runs on a **laptop with an 8 GB GPU and 32 GB RAM**, **CPU only at 18–21 tok/s**, a 128 GB mini PC or one DGX Spark. MMLU-Pro is **identical to BF16 (87.65%)**.

`reasoning` · `MoE 512 experts` · `262K long context` · `image + text` · `Korean + English` · `self-improvement` · `structured output` · `ZTC`

<p align="center">
<a href="https://vidraft.net"><img src="https://img.shields.io/badge/🌐_VIDRAFT-vidraft.net-111827?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/llamaindex/ExtractBench"><img src="https://img.shields.io/badge/ExtractBench_(R3)-90.29_%231-059669?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/FutureMa/EvasionBench"><img src="https://img.shields.io/badge/EvasionBench_(R3)-77.83_%233-0d9488?style=for-the-badge"></a>
</p>
<p align="center">
<a href="https://huggingface.co/datasets/Idavidrein/gpqa"><img src="https://img.shields.io/badge/GPQA_Diamond_(R1)-94.44%25_%231-gold?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro"><img src="https://img.shields.io/badge/MMLU--Pro_(R1)-88.12%25_%231-2563eb?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/MMMU/MMMU_Pro"><img src="https://img.shields.io/badge/MMMU--Pro_(R1)-79.48%25_%231-0891b2?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/MathArena/aime_2026"><img src="https://img.shields.io/badge/AIME_2026_(R1)-100%25_%231-dc2626?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/MathArena/hmmt_feb_2026"><img src="https://img.shields.io/badge/HMMT_Feb_2026_(R1)-100%25_%231-ea580c?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/LEXam-Benchmark/LEXam"><img src="https://img.shields.io/badge/LEXam_(R1)-68.94%25_%231-4f46e5?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/joelniklaus/LEXam-hard"><img src="https://img.shields.io/badge/LEXam--hard_(R1)-45.72_%231-6d28d9?style=for-the-badge"></a>
<a href="https://huggingface.co/datasets/LiquidAI/ifstruct-v1.0"><img src="https://img.shields.io/badge/IFStruct_(R1)-98.95%25_%231-b45309?style=for-the-badge"></a>
</p>
<p align="center">
<a href="https://huggingface.co/FINAL-Bench/Darwin-180B-RSI"><img src="https://img.shields.io/badge/Round_1-Darwin--180B--RSI-e11d48?style=for-the-badge"></a>
<a href="https://arxiv.org/abs/2605.14386"><img src="https://img.shields.io/badge/arXiv-2605.14386_Darwin_Family-b31b1b?style=for-the-badge"></a>
<a href="https://huggingface.co/papers/2609.20269"><img src="https://img.shields.io/badge/Paper-2609.20269_Latin_Square-b31b1b?style=for-the-badge"></a>
<a href="https://huggingface.co/collections/FINAL-Bench/darwin-family"><img src="https://img.shields.io/badge/🧬_Collection-Darwin_Family-16a34a?style=for-the-badge"></a>
<a href="https://huggingface.co/FINAL-Bench/POCKET-Darwin-180B-GGUF"><img src="https://img.shields.io/badge/💻_POCKET_4--bit-Laptop_·_CPU_only_·_DGX_Spark-0f766e?style=for-the-badge"></a>
</p>

**The second round of model-level self-improvement on top of [Darwin-180B-RSI](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI).**
R3 continues training from R1 with the same recipe: the model solves verifiable problems, keeps only its own solutions that check out as correct, and trains on them. No human-written solutions or reasoning traces are used.
R3 is released so anyone can download it, run it, and check the numbers below.

---

## 🏆 Nine #1s in the Darwin-180B-RSI line

Hugging Face **official** benchmark leaderboards. Each score is listed under the model that produced it.

| Benchmark | Score | Model | Leaderboard |
|:---|:---:|:---|:---|
| **ExtractBench** (370 documents) | **90.29** | **R3 (this model)** | [**#1**](https://huggingface.co/datasets/llamaindex/ExtractBench) |
| **GPQA Diamond** (198) | **94.44** | R1 ([Darwin-180B-RSI](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI)) | [**#1**](https://huggingface.co/datasets/Idavidrein/gpqa) |
| **MMLU-Pro** (12,032) | **88.12** | R1 | [**#1**](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro) |
| **AIME 2026** (30) | **100.0** | R1 | [**#1**](https://huggingface.co/datasets/MathArena/aime_2026) |
| **HMMT Feb 2026** (33) | **100.0** | R1 | [**#1**](https://huggingface.co/datasets/MathArena/hmmt_feb_2026) |
| **MMMU-Pro** (vision, 1,730) | **79.48** | R1 | [**#1**](https://huggingface.co/datasets/MMMU/MMMU_Pro) |
| **LEXam** (law, MCQ 4-choice, 1,655) | **68.94** | R1 | [**#1**](https://huggingface.co/datasets/LEXam-Benchmark/LEXam) |
| **LEXam-hard** (law, open-ended, 518) | **45.72** | R1 | [**#1**](https://huggingface.co/datasets/joelniklaus/LEXam-hard) |
| **IFStruct** (structured output, 2,000 prompts) | **98.95** | R1 | [**#1**](https://huggingface.co/datasets/LiquidAI/ifstruct-v1.0) |

R3's own leaderboard entries:

| Benchmark | R3 | Leaderboard | Setting |
|:---|:---:|:---|:---|
| **ExtractBench** (370 documents) | **90.29, #1** | [llamaindex/ExtractBench](https://huggingface.co/datasets/llamaindex/ExtractBench) | official harness, 32,768 max tokens (same as the parent), temperature 0, thinking off, single run |
| **EvasionBench** (16,726 questions) | **77.83, #3** | [FutureMa/EvasionBench](https://huggingface.co/datasets/FutureMa/EvasionBench) | inspect-ai task from the dataset eval.yaml, temperature 1.0, top_p 0.95, 8,192 max tokens, thinking on, single run |

Full settings are recorded in [`.eval_results/`](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI-R3/tree/main/.eval_results).

### R1 head-to-head with Chinese frontier models

![Darwin-180B-RSI vs Chinese frontier models](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI/resolve/main/assets/bench_vs_china.png)

| Model | AIME 2026 | GPQA Diamond | MMLU-Pro | MMMU-Pro | HMMT Feb 2026 | LEXam | LEXam-hard |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **🧬 Darwin-180B-RSI, R1 (ours · 🇰🇷)** | **100** 🥇 | **94.44** 🥇 | **88.12** 🥇 | **79.48** 🥇 | **100** 🥇 | **68.94** 🥇 | **45.72** 🥇 |
| Inkling (Thinking Machines) | · | · | · | · | · | · | 40.82 |
| Kimi-K3 (Moonshot AI) | · | 93.5 | · | · | · | · | 29.54 |
| Kimi-K2.6 (Moonshot AI) | 96.4 | 90.5 | · | 79.4 | 92.7 | · | 36.18 |
| DeepSeek-V4-Pro (DeepSeek) | · | 90.1 | 87.5 | · | · | · | 38.93 |
| Qwen3.5-397B-A17B (Alibaba) | 93.33 | 88.4 | 87.8 | · | 87.88 | · | · |
| MiniMax-M2.1 (MiniMax) | · | 80.81 | 88 | · | · | · | · |
| GLM-5 (Zhipu AI) | 95.83 | 86 | 86 | · | 86.36 | · | · |
| Intern-S2-Preview (Shanghai AI Lab) | · | · | 88 | 76.88 | 87.31 | · | · |
| Step-3.5-Flash (StepFun) | 96.67 | 83.5 | 84.4 | · | 86.36 | · | · |
| DeepSeek-R1 (DeepSeek) | · | · | · | · | · | 52.41 | · |
| Qwen3-235B-A22B-Thinking-2507 (Alibaba) | · | · | · | · | · | 48.19 | · |

<sub>Scores as listed on the Hugging Face official benchmark leaderboards (self-reported by each model's publisher). "·" = not reported. Open-weight models only; closed API models are not included. Settings (samples, voting, thinking budget) differ across models. R1 settings are in the evaluation protocol below.</sub>

---

## 🧬 What changed from R1

- **Starting point:** R1 weights (not the parent). R3 is a true second round.
- **Practice problems:** 3,000 SuperGPQA questions (middle and hard difficulty) that were never used in R1 training. R1 solved each one 8 times.
- **What it learned from:** only the "boundary" problems, where R1 was right on 2 to 6 of 8 attempts (462 problems). From those, up to 2 of R1's own correct, untruncated solutions per problem (714 solutions in total).
- **What was trained:** the same components as R1 (attention paths and shared experts) via LoRA, then merged. All 512 routed experts, the router and the vision encoder are unchanged.
- **No benchmark data:** GPQA Diamond and the held-out set below were never used for training or selection.

### Held-out SuperGPQA, 1,000 questions never used in training or selection
4 samples per question, 16K thinking budget, temperature 1.0.

| Model | Single sample | Mean of 4 | Majority of 4 |
|---|---:|---:|---:|
| R1 (Darwin-180B-RSI) | 65.30 | 65.67 | 68.30 |
| **R3 (this model)** | **66.30** | **66.70** | **69.00** |

Paired per-question difference, R1 → R3 (mean of 4): **+1.03 points, 95% CI [+0.05, +2.00]**. The second round of self-improvement produced a measurable gain over R1.

### GPQA Diamond, 198 questions
8 samples per question, 32K thinking budget, temperature 1.0.

| Model | Single sample | Mean of 8 | Majority of 8 |
|---|---:|---:|---:|
| R0 (parent, Qwen3.8-Flash-Next) | 84.85 | 85.35 | 90.91 |
| R1 (Darwin-180B-RSI) | 84.85 | 85.80 | 89.90 |
| **R3 (this model)** | **85.86** | **86.05** | 90.40 |

---

## 🧬 The Darwin Family

<p align="center">
<a href="https://huggingface.co/FINAL-Bench/Darwin-180B-RSI"><img src="https://img.shields.io/badge/Darwin--180B--RSI-8×_%231-e11d48"></a>
<a href="https://huggingface.co/FINAL-Bench/Darwin-397B-ZTC"><img src="https://img.shields.io/badge/Darwin--397B--ZTC-GPQA_93.43-16a34a"></a>
<a href="https://huggingface.co/FINAL-Bench/Darwin-28B-REASON"><img src="https://img.shields.io/badge/Darwin--28B--REASON-GPQA_89.39-16a34a"></a>
<a href="https://huggingface.co/FINAL-Bench/Darwin-35B-A3B-Opus"><img src="https://img.shields.io/badge/Darwin--35B--A3B--Opus-♥98-e11d48"></a>
<a href="https://huggingface.co/FINAL-Bench/Darwin-36B-Opus"><img src="https://img.shields.io/badge/Darwin--36B--Opus-♥97-e11d48"></a>
</p>
<p align="center">
<a href="https://huggingface.co/FINAL-Bench/Darwin-4B-Genesis"><img src="https://img.shields.io/badge/Darwin--4B--Genesis-♥63-e11d48"></a>
<a href="https://huggingface.co/FINAL-Bench/Darwin-9B-NEG"><img src="https://img.shields.io/badge/Darwin--9B--NEG-♥57-e11d48"></a>
<a href="https://huggingface.co/FINAL-Bench/POCKET-35B-GGUF"><img src="https://img.shields.io/badge/POCKET--35B-824K_↓-1f6feb"></a>
<a href="https://huggingface.co/FINAL-Bench/POCKET-26B-GGUF"><img src="https://img.shields.io/badge/POCKET--26B-365K_↓-1f6feb"></a>
<a href="https://huggingface.co/FINAL-Bench/POCKET-Darwin-180B-GGUF"><img src="https://img.shields.io/badge/POCKET--Darwin--180B-4--bit_R3_·_laptop-1f6feb"></a>
</p>

**Darwin** is [VIDRAFT](https://vidraft.net)'s measurement-driven reasoning model family: **50+ official models**, **400+ community derivatives**, and two places in the GPQA Diamond top 3 (Darwin-180B-RSI #1 · Darwin-397B-ZTC #3).

### Darwin: evolve the parent, keep what works

Darwin treats a strong open model as a **parent**. It measures where the parent is weak and strengthens exactly those parts, instead of re-training everything and risking what already works.

- **Diagnose before you change.** Every Darwin generation starts from a measured weakness map of the parent.
- **Change little, precisely.** Darwin modifies a small, targeted fraction of the network. Knowledge stored in the experts is preserved.
- **Proven capability over new guesses.** Earlier Darwin generations grafted the best-performing expert/FFN blocks from other strong models onto a base backbone; the RSI line adds a new ingredient: **the model's own verified work**.
- **Measured, not claimed.** Every change must beat its predecessor on held-out tests before it ships.

### Lineage

| Role | | |
|:---|:---|:---|
| **R0, parent** | `Qwen/Qwen3.8-Flash-Next` | 180B MoE vision-language backbone · Qwen Community License 1.0 |
| **R1** | [Darwin-180B-RSI](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI) | first RSI round: the parent's own verified solutions fed back as training signal · eight #1s |
| **R3 (this model)** | Darwin-180B-RSI-R3 | second RSI round, trained from R1 on R1's own verified solutions · ExtractBench #1 |
| **Preserved** | 512 routed experts · router · vision encoder | untouched in every round |

---

## 🔁 RSI: a model that improves from its own work

**Recursive self-improvement (RSI)** is the core of this line. Instead of distilling a bigger teacher, the model improves by learning from itself:

1. **Solve:** the model works through practice problems it has never seen in evaluation.
2. **Verify:** its answers are checked against verifiable references (answer keys, executable checks). Nothing unverified is learned.
3. **Learn:** it is re-trained on the reasoning that turned out to be correct.
4. **Repeat:** the improved model becomes the next solver. R1 was round one; R3 is the next round.

Practice sets are deduplicated against every evaluation set we report (8-gram overlap filter).

### Model-level RSI vs. harness-level RSI

Darwin-180B-RSI-R3 is **Model-level RSI**: the model itself (its weights) improves by learning only from its own solutions. No human-written solutions or reasoning traces are used; correctness is checked automatically. **Harness-level RSI** (e.g., Google's RRSI) improves the prompts, tools and workflow around a fixed model. It is like rewriting an employee's manual, while Model-level RSI is the employee getting smarter. The two are complementary.

---

## 🏛️ ZTC: it knows before it answers

**Zero-Token Confidence (ZTC)** reads the model's own internal state **once, before generation**, and returns the probability that the answer it is about to give is correct, with **no extra tokens and no second model.**

```json
{"answer": "...", "confidence": 0.93, "ztc_score": 1.84, "truncated": false}
```

The ZTC probe published with [Darwin-180B-RSI](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI) was fitted on R1's hidden states. A probe fitted on R3 will be added to this repository; until then, use R1's probe only as a rough signal.

---

## 📐 Evaluation protocol

**R3 entries (ExtractBench, EvasionBench):** see the settings column in the table above and [`.eval_results/`](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI-R3/tree/main/.eval_results). ExtractBench was run with thinking turned off (`chat_template_kwargs: {"enable_thinking": false}`), which suits schema-guided extraction.

**R1 entries (its #1s):**

| Setting | Value |
|:---|:---|
| Thinking budget | **131,072 tokens** (32,768 for LEXam and LEXam-hard) |
| Sampling | temperature 1.0 · top_p 0.95 · top_k 20 |
| Precision | bf16 |
| Engine | vLLM, tensor parallel 8 (or 4), expert parallel |

| Benchmark | Samples per question | Reported score |
|:---|:---:|:---|
| AIME 2026 | 16 | majority vote (maj@16); mean over 16 = 98.75 |
| HMMT Feb 2026 | 16 | majority vote (maj@16); mean over 16 = 96.59 |
| GPQA Diamond | up to 16 | majority vote |
| MMLU-Pro | 1 | single sample (no voting) |
| MMMU-Pro (vision) | 3 | majority vote (maj@3) |
| LEXam | 4 | majority vote (single sample 60.54 · mean 61.42) |
| LEXam-hard | 1 | single sample, judged by DeepSeek-R1-0528 per the official eval.yaml |
| IFStruct | 1 | single run, temperature 0, 16,000 max tokens (official harness defaults) |

All numbers are self-measured and reproducible with the settings above. Majority-vote scores are system scores (several samples per question) and are labeled as such.

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
vllm serve FINAL-Bench/Darwin-180B-RSI-R3 \
  --tensor-parallel-size 8 --enable-expert-parallel \
  --max-model-len 139264 --trust-remote-code
```

### Chat Completions (OpenAI-compatible)

```python
from openai import OpenAI
c = OpenAI(base_url="http://localhost:8000/v1", api_key="-")
r = c.chat.completions.create(model="FINAL-Bench/Darwin-180B-RSI-R3",
    messages=[{"role": "user", "content": "Explain why the sky is blue in two sentences."}],
    temperature=1.0, top_p=0.95, extra_body={"top_k": 20})
print(r.choices[0].message.content)
```

For structured extraction (JSON to a schema), turn thinking off, as in the ExtractBench run:

```python
r = c.chat.completions.create(model="FINAL-Bench/Darwin-180B-RSI-R3", messages=msgs, temperature=0,
    response_format={"type": "json_object"},
    extra_body={"chat_template_kwargs": {"enable_thinking": False}})
```

### Transformers

```python
from transformers import AutoProcessor, AutoModelForImageTextToText
model_id = "FINAL-Bench/Darwin-180B-RSI-R3"
processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForImageTextToText.from_pretrained(model_id, torch_dtype="auto", device_map="auto")
```

**Tip:** for hard reasoning, keep thinking on and give it room (a thinking budget of 32K to 131K tokens). For document extraction, thinking off was faster and scored higher in our ExtractBench runs.

---

## ⚠️ Limitations and disclosure

- Scores are self-measured with the settings stated above; majority-vote numbers use several samples per question.
- Very long reasoning is normal for hard problems; a short thinking budget will truncate answers and lower accuracy.
- Like every LLM, the model can be confidently wrong. Use a confidence readout such as ZTC to gate high-stakes actions.

---

## 🔗 Related Darwin Models

- **[Darwin-180B-RSI](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI)**: R1, the model R3 was trained from, #1 on eight Hugging Face official leaderboards
- **[POCKET-Darwin-180B-GGUF](https://huggingface.co/FINAL-Bench/POCKET-Darwin-180B-GGUF)**: 4-bit GGUF of R3 for laptops, CPU-only machines and DGX Spark
- **[Darwin-397B-ZTC](https://huggingface.co/FINAL-Bench/Darwin-397B-ZTC)**: 397B MoE (FP8), GPQA Diamond 93.43 %, ZTC on board
- **[Darwin-28B-REASON](https://huggingface.co/FINAL-Bench/Darwin-28B-REASON)**: 28B, GPQA Diamond 89.39 %
- **[Darwin-27B-RSI](https://huggingface.co/FINAL-Bench/Darwin-27B-RSI)**: 27B, the first Darwin RSI model
- **[ZTC-Judge-27B](https://huggingface.co/FINAL-Bench/ZTC-Judge-27B)**: standalone ZTC judge

---

## 📚 Citation

```bibtex
@misc{darwin180b_rsi_r3_2026,
  title  = {Darwin-180B-RSI-R3: A Second Round of Model-Level Self-Improvement for a 180B Mixture-of-Experts Reasoning Model},
  author = {FINAL-Bench / Darwin Research Team},
  year   = {2026},
  howpublished = {\url{https://huggingface.co/FINAL-Bench/Darwin-180B-RSI-R3}},
  note   = {ExtractBench 90.29}
}

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
```

---

## 📜 License

Darwin-180B-RSI-R3 is a derivative of **Qwen3.8-Flash-Next** (through Darwin-180B-RSI) and is distributed under the **Qwen Community License 1.0** (see [LICENSE](LICENSE)).

## 🏢 About

Built by **[VIDRAFT](https://vidraft.net)** · evaluated with **FINAL-Bench**. Part of the [Darwin Family](https://arxiv.org/abs/2605.14386).
