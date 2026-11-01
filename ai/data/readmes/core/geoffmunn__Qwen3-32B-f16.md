---
license: apache-2.0
tags:
  - gguf
  - qwen
  - qwen3
  - qwen3-32b
  - qwen3-32b-gguf
  - llama.cpp
  - quantized
  - text-generation
  - reasoning
  - agent
  - multilingual
  - imatrix
  - q3_hifi
  - q4_hifi
  - q5_hifi
base_model: Qwen/Qwen3-32B
author: geoffmunn
pipeline_tag: text-generation
language:
  - en
  - zh
  - es
  - fr
  - de
  - ru
  - ar
  - ja
  - ko
  - hi
---

# Qwen3-32B-f16-GGUF

This is a **GGUF-quantized version** of the **[Qwen/Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B)** language model — a **32-billion-parameter** LLM with state-of-the-art reasoning, research capabilities, and enterprise-grade performance. Converted for use with `llama.cpp`, [LM Studio](https://lmstudio.ai), [OpenWebUI](https://openwebui.com), [GPT4All](https://gpt4all.io), and more.


## Why Use a 32B Model?

The **Qwen3-32B** model represents the **pinnacle of locally runnable intelligence**, delivering near-flagship reasoning and generation capabilities while remaining feasible to deploy on dual consumer GPUs or single professional accelerators. It's the definitive choice when you demand maximum fidelity—where every percentage point of precision matters for complex reasoning, nuanced language tasks, and production-grade code generation—without surrendering to cloud dependency or vendor lock-in.

### Highlights:
- **Best-in-class open 32B performance**, excelling in multi-step reasoning, advanced mathematics, professional-grade coding, and nuanced multilingual understanding  
- **Unprecedented quantization resilience**: achieves *statistically F16-equivalent quality* with Q5_K_M/HIFI + imatrix (within ±0.056 measurement noise) while using only **36% of F16's memory** and running **2.5× faster**  
- **Production-ready even at aggressive compression**: Q4_K variants maintain near-lossless fidelity (+0.5–0.7% loss with imatrix); even Q3_K_HIFI delivers exceptional 3-bit quality (+2.2% loss)  
- **Fully open weights with commercial rights**, enabling complete control over deployment, fine-tuning, and integration into sensitive workflows  

### It's ideal for:
- **Quality-critical production systems** where output precision directly impacts user trust—medical, legal, financial, or engineering applications  
- **Research and development environments** requiring near-F16 fidelity at dramatically reduced infrastructure costs (64% memory savings with zero quality penalty)  
- **Enterprise RAG and agentic workflows** demanding maximum comprehension of complex documents, precise tool use, and reliable multi-hop reasoning  
- **Developers pushing quantization boundaries**, leveraging 32B's unique resilience to deploy massive models on constrained hardware without perceptible degradation  

Choose **Qwen3-32B** when smaller models consistently miss subtle nuances, hallucinate on complex tasks, or fail to maintain coherence across extended reasoning chains—delivering flagship-grade intelligence with the sovereignty, privacy, and cost control of local deployment. With intelligent quantization, you gain 99.9% of F16's capability at one-third the resource footprint: the ultimate balance of quality, efficiency, and independence.

# Qwen3 32B Quantization Guide: Cross-Bit Summary & Recommendations

## Executive Summary

At 32B scale, **quantization achieves near-miraculous fidelity**—Q5_K_HIFI and Q5_K_M with imatrix deliver **statistically F16-equivalent quality** (within ±0.056 measurement noise) while using only **36% of F16's memory** and running **2.5× faster**. Even Q4_K variants achieve near-lossless quality (+0.5–0.7% loss with imatrix), and Q3_K_HIFI reaches production-ready fidelity (+2.2% loss). However, **Q3_K_S and Q2_K are catastrophically broken** at this scale, making variant selection critically important:

| Bit Width | Best Variant (+ imatrix) | Quality vs F16 | File Size | Speed | Memory | Viability |
|-----------|--------------------------|----------------|-----------|-------|--------|-----------|
| **Q5_K** | Q5_K_HIFI + imatrix | **-0.073%** ✅✅✅ | 21.84 GiB | 28.22 TPS | 22,364 MiB | Exceptional |
| **Q4_K** | Q4_K_S + imatrix | **+0.7%** ✅✅ | 17.48 GiB | **35.00 TPS** (fastest) | 17,900 MiB | Excellent |
| **Q3_K** | Q3_K_HIFI + imatrix | **+2.2%** ✅ | ~17.0 GiB* | 32.00 TPS | 17,807 MiB | Good |
| **Q2_K** | Q2_K + imatrix | **+121.1%** ❌ | 11.49 GiB | 48.94 TPS | 12,871 MiB | **Unusable** |

💡 **Critical insight**: 32B models exhibit **unprecedented quantization resilience** at Q5_K/Q4_K/Q3_K levels, but **Q3_K_S fails catastrophically** (+120–155% precision loss) and **Q2_K is unusable** (>121% loss). This represents the pinnacle of quantization resilience across the Qwen3 family—with critical failure modes at extreme compression.

\* *Q3_K_HIFI file size estimated from memory footprint; actual size ~16.8–17.2 GiB*

---

## Bit-Width Recommendations by Use Case

### ✅ Quality-Critical Applications (Research, Content Generation)
**→ Q5_K_HIFI + imatrix**  
- **Statistically indistinguishable from F16** (7.8975 PPL vs 7.9033, difference within ±0.056 measurement noise)  
- 64.2% memory reduction (22.4 GiB vs 62.5 GiB)  
- 157% faster than F16 (28.22 TPS vs 10.96 TPS)  
- ⚠️ Requires custom llama.cpp build (8037+) with `Q6_K_HIFI_RES8` support

**→ Q5_K_M + imatrix (standard alternative)**  
- Also F16-equivalent quality (7.8995 PPL, -0.048% vs F16)  
- Standard GGUF compatibility — works with all recent llama.cpp builds  
- Only 0.025 PPL points worse than HIFI (within measurement noise)  
- **Recommended default for quality-critical work requiring standard tooling**

### ⚖️ Best Overall Balance (Recommended Default)
**→ Q4_K_M + imatrix**  
- Excellent +0.6% precision loss vs F16 (PPL 7.9488) — imperceptible in practice  
- Strong 33.36 TPS speed (+193% vs F16)  
- Compact 18.40 GiB file size (70% smaller than F16)  
- **Standard llama.cpp compatibility** — no custom builds needed  
- Ideal for most development and production scenarios where 5-bit overhead isn't justified

### 🚀 Maximum Speed / Minimum Size
**→ Q4_K_S + imatrix**  
- **Fastest variant at 35.00 TPS** (+208% vs F16)  
- Smallest viable footprint at **17.48 GiB** (71.4% memory reduction)  
- Surprisingly good quality at +0.7% loss — only 0.2% worse than Q4_K_HIFI with imatrix  
- ⚠️ **Never use without imatrix** — quality degrades to +3.5% loss

### 💎 Near-Lossless 3-Bit Option
**→ Q3_K_HIFI + imatrix**  
- **Remarkable +2.2% precision loss** — exceptional for 3-bit quantization  
- 71.5% memory reduction (17,807 MiB vs 62,495 MiB)  
- Unique value: When you need maximum compression but cannot accept Q3_K_S's catastrophic failure  
- ⚠️ **22% slower than Q3_K_M** and requires careful validation for quality-sensitive tasks

### ⛔ Avoid Entirely
**→ Q3_K_S (any configuration)**  
- Minimum +120% precision loss even with imatrix (PPL 17.40)  
- Output quality severely compromised — incoherent generations expected  
- **NEVER use for 32B models** — failure mode does not occur at smaller scales

**→ Q2_K variants (any configuration)**  
- Minimum +121.1% precision loss even with imatrix (PPL 17.48)  
- Quality equivalent to a **4B model**, not a 32B model  
- **Unusable for any practical application** — only for pipeline verification

---

## Critical Warnings for 32B Scale

⚠️ **Q3_K_S is catastrophically broken at 32B scale**:  
- Without imatrix: **+155% precision loss** (PPL 20.19 vs F16 7.90) — completely unusable  
- With imatrix: **+120% precision loss** (PPL 17.40) — still unusable despite imatrix guidance  
- **NEVER use Q3_K_S for 32B models** — this failure mode does not occur at smaller scales (8B/14B)  
- Minimum safe Q3 variant: **Q3_K_M + imatrix** (+3.7% loss, production-ready)

⚠️ **Q2_K is unusable at 32B scale**:  
- Even Q2_K + imatrix suffers +121.1% precision loss (PPL 17.48)  
- Quality is **worse than 4B Q2_K + imatrix** (17.48 vs 17.02 PPL)  
- **Only use for pipeline verification** — not for actual inference

⚠️ **Q2_K pattern reversal at 32B**:  
- Unlike 4B/8B/14B where Q2_K beats Q2_K_HIFI, at 32B:  
  - **Without imatrix**: Q2_K_HIFI is better (19.87 vs 20.67 PPL)  
  - **With imatrix**: Q2_K is better (17.48 vs 17.54 PPL)  
- This is the **only scale** where this reversal occurs

⚠️ **Q5_K_HIFI provides negligible advantage over Q5_K_M**:  
- Quality difference: 0.025 PPL points (within ±0.056 measurement noise)  
- Costs +235 MiB memory (+1.1% overhead) and requires custom build  
- **Prefer Q5_K_M + imatrix** for standard compatibility unless you specifically need HIFI tensor types

⚠️ **imatrix effectiveness plateaus at 32B**:  
- Q5_K variants: Already near-F16 quality without imatrix (+0.06% loss); imatrix provides marginal gains  
- Q4_K_S: Most dramatic imatrix benefit — closes 2.8% quality gap (from +3.5% → +0.7%)  
- Q3_K_HIFI: Minimal imatrix benefit (+0.18 PPL improvement) — already excellent without it  
- Q2_K: Weak imatrix recovery (~25% vs ~58% at 14B) — cannot save unusable quality

⚠️ **VRAM requirements are substantial**:  
- Minimum viable: **~18 GiB** (Q4_K_S)  
- Comfortable deployment: **24+ GiB** (RTX 3090/4090) for context headroom  
- Dual-GPU recommended for production workloads (tested on 2× L40S)

---

## Memory Budget Guide

| Available VRAM | Recommended Variant | Expected Quality | Why |
|----------------|---------------------|------------------|-----|
| **< 13 GiB** | Neither Q2_K variant | — | Both require ~12.9–13.1 GiB minimum; quality unusable anyway |
| **13 – 18 GiB** | Q3_K_M + imatrix | PPL 8.20, +3.7% loss ⚠️ | Only option that fits; quality acceptable for non-critical tasks |
| **18 – 20 GiB** | Q4_K_S + imatrix | PPL 7.9627, +0.7% loss ✅ | Tight fit; leaves minimal headroom for KV cache at longer contexts |
| **20 – 24 GiB** | Q4_K_M + imatrix | PPL 7.9488, +0.6% loss ✅ | Comfortable fit on RTX 3090/4090 (24 GiB) with context headroom |
| **24 – 48 GiB** | Q5_K_M + imatrix | PPL 7.8995, F16-equivalent ✅ | Room for larger context windows; near-perfect quality |
| **> 48 GiB** | Q5_K_HIFI + imatrix or F16 | PPL 7.8975, F16-equivalent ✅ | Maximum quality with standard tooling (M) or absolute precision (F16) |

---

## Cross-Bit Performance Comparison

| Priority | Q3_K Best | Q4_K Best | Q5_K Best | Winner |
|----------|-----------|-----------|-----------|--------|
| **Quality (with imat)** | Q3_K_HIFI (+2.2%) | Q4_K_HIFI (+0.5%) | **Q5_K_HIFI (-0.073%)** ✅✅✅ | **Q5_K_HIFI/M** |
| **Speed** | Q3_K_S (40 TPS)* | **Q4_K_S (35.00 TPS)** ✅ | Q5_K_S (29.62 TPS) | **Q4_K_S** |
| **Smallest Size** | **Q3_K_S (13.40 GiB)** ✅ | Q4_K_S (17.48 GiB) | Q5_K_S (21.08 GiB) | **Q3_K_S** ⚠️ |
| **Best Balance** | Q3_K_M + imat | **Q4_K_M + imat** ✅ | Q5_K_M + imat | **Q4_K_M** |

✅ = Recommended for general use  
✅✅ = Near-lossless quality  
✅✅✅ = Statistically F16-equivalent  
⚠️ = Q3_K_S is broken despite small size — **never use**  
\* *Q3_K_S speed is misleading — quality is catastrophically degraded*

---

## Scale-Specific Insights: Why 32B Quantizes So Well (and Fails So Hard)

### 1. Parameter Redundancy Threshold
32B represents the point where model architecture provides **sufficient weight redundancy** that quantization errors effectively cancel out rather than accumulating. This creates a "quantization sweet spot" where aggressive compression meets robust architecture—but only up to a point. Beyond Q3_K_M, the redundancy breaks down catastrophically.

### 2. imatrix Saturation Effect
At 32B scale, imatrix effectiveness **plateaus** — Q5_K variants already achieve near-F16 quality *without* imatrix (+0.06% loss), unlike smaller models where imatrix recovers 40–78% of lost precision. The model's inherent robustness reduces dependence on importance weighting.

### 3. Q3_K_S Catastrophic Failure Mode
While Q3_K_HIFI achieves remarkable +2.2% loss (exceptional for 3-bit), Q3_K_S fails catastrophically (+120–155% loss). This demonstrates that **intelligent tensor selection becomes critical at extreme compression levels** on large models — uniform quantization strategies break down where mixed-precision approaches succeed.

### 4. Q2_K Quality Collapse
Q2_K at 32B produces output quality **equivalent to a 4B model** (17.48 PPL vs 4B Q2_K's 17.02 PPL). You would receive better quality running a **4B F16 model** (14.34 PPL) than a **32B Q2_K model**. This demonstrates the severity of extreme quantization at massive scales.

### 5. Diminishing Returns of Residual Quantization
Q5_K_HIFI's residual correction tensors (`Q6_K_HIFI_RES8`) provide **negligible benefit** at 32B scale (0.025 PPL improvement over Q5_K_M) because the base quantization is already near-optimal. This contrasts with 4B–8B scales where residual correction delivers measurable gains.

### 6. Q4_K_S imatrix Synergy
Q4_K_S uniquely benefits from imatrix at 32B scale — the 2.8% quality gap vs Q4_K_HIFI collapses to just 0.2% with imatrix, making Q4_K_S + imatrix the **standout value proposition** (fastest + smallest + near-HIFI quality).

---

## Why Use a 32B Model?

The **Qwen3-32B** model represents the **pinnacle of locally runnable intelligence**, delivering near-flagship reasoning and generation capabilities while remaining feasible to deploy on dual consumer GPUs or single professional accelerators. It's the definitive choice when you demand maximum fidelity—where every percentage point of precision matters for complex reasoning, nuanced language tasks, and production-grade code generation—without surrendering to cloud dependency or vendor lock-in.

### Highlights:
- **Best-in-class open 32B performance**, excelling in multi-step reasoning, advanced mathematics, professional-grade coding, and nuanced multilingual understanding  
- **Unprecedented quantization resilience**: achieves *statistically F16-equivalent quality* with Q5_K_M/HIFI + imatrix (within ±0.056 measurement noise) while using only **36% of F16's memory** and running **2.5× faster**  
- **Production-ready even at aggressive compression**: Q4_K variants maintain near-lossless fidelity (+0.5–0.7% loss with imatrix); even Q3_K_HIFI delivers exceptional 3-bit quality (+2.2% loss)  
- **Fully open weights with commercial rights**, enabling complete control over deployment, fine-tuning, and integration into sensitive workflows  

### It's ideal for:
- **Quality-critical production systems** where output precision directly impacts user trust—medical, legal, financial, or engineering applications  
- **Research and development environments** requiring near-F16 fidelity at dramatically reduced infrastructure costs (64% memory savings with zero quality penalty)  
- **Enterprise RAG and agentic workflows** demanding maximum comprehension of complex documents, precise tool use, and reliable multi-hop reasoning  
- **Developers pushing quantization boundaries**, leveraging 32B's unique resilience to deploy massive models on constrained hardware without perceptible degradation  

Choose **Qwen3-32B** when smaller models consistently miss subtle nuances, hallucinate on complex tasks, or fail to maintain coherence across extended reasoning chains—delivering flagship-grade intelligence with the sovereignty, privacy, and cost control of local deployment. With intelligent quantization, you gain 99.9% of F16's capability at one-third the resource footprint: the ultimate balance of quality, efficiency, and independence.

---

## Practical Deployment Recommendations

### For Most Users
**→ Q4_K_M + imatrix**  
Delivers excellent quality (+0.6% vs F16), strong speed (33.36 TPS), compact size (18.40 GiB), and universal llama.cpp compatibility. The safe, practical choice for 95% of deployments where absolute F16-equivalence isn't required.

### For Quality-Critical Work
**→ Q5_K_M + imatrix**  
Achieves statistical F16-equivalence (-0.048% vs F16) with 64.5% memory reduction and 159% speedup. Standard compatibility makes it preferable to Q5_K_HIFI for most users requiring maximum fidelity.

### For High-Throughput Serving
**→ Q4_K_S + imatrix**  
Fastest variant (35.00 TPS, +208% vs F16) with surprisingly good quality (+0.7% loss) and smallest viable footprint (17.48 GiB). Ideal when throughput matters more than marginal quality differences.

### For Maximum Compression
**→ Q3_K_HIFI + imatrix**  
Demonstrates that 3-bit quantization can achieve production-ready quality (+2.2% loss) on sufficiently large models. Valuable for characterizing lower bounds of viable quantization — but **never use Q3_K_S**.

### For Pipeline Verification Only
**→ Q2_K + imatrix**  
Only use to verify that 32B inference pipeline works on constrained hardware. Quality is unusable for actual applications.

---

## Decision Flowchart

```mermaid
Need absolute best quality?
├─ Yes → VRAM ≥ 24 GiB?
│        ├─ Yes → Q5_K_M + imatrix (F16-equivalent, standard build) ✅
│        └─ No  → Q4_K_M + imatrix (+0.6% loss, fits 20 GiB) ✅
└─ No → Need max throughput?
     ├─ Yes → Q4_K_S + imatrix (35 TPS, +0.7% loss) ✅
     └─ No → Need max compression?
              ├─ Yes → Q3_K_HIFI + imatrix (+2.2% loss) ✅
              └─ No  → Q4_K_M + imatrix (best balance) ✅
```

⚠️ **Critical path exclusions**: 
- Q3_K_S is **never** on the optimal path — quality degradation is catastrophic regardless of constraints
- Q2_K variants are **never** on the optimal path — quality is unusable for any practical application

---

## Bottom Line Recommendations

| Scenario | Recommended Variant | Rationale |
|----------|---------------------|-----------|
| **Default / General Purpose** | Q4_K_M + imatrix | Best balance of quality (+0.6%), speed (33.36 TPS), size (18.40 GiB), and compatibility |
| **Maximum Quality** | Q5_K_M + imatrix | Statistically F16-equivalent (-0.048%) with standard toolchain; skip HIFI (no meaningful advantage) |
| **Maximum Throughput** | Q4_K_S + imatrix | Fastest (35.00 TPS) with excellent quality (+0.7%); imatrix essential |
| **Maximum Compression** | Q3_K_HIFI + imatrix | Best Q3 quality (+2.2%); **never use Q3_K_S** (catastrophic failure) |
| **Standard Tooling Required** | Q5_K_M or Q4_K_M + imatrix | Both achieve excellent quality with universal llama.cpp compatibility |
| **Pipeline Verification Only** | Q2_K + imatrix | Only to confirm 32B inference works; quality unusable for actual applications |

✅ **32B is the quantization resilience milestone**: Large enough for near-lossless compression even at 3-bit levels (with intelligent quantization), yet small enough for dramatic efficiency gains. This scale demonstrates that quantization can deliver **F16-equivalent quality at 1/3 the memory with 2.5–3.5× speed** — a compelling value proposition for nearly all deployments.

⚠️ **Golden rules for 32B**:  
1. **NEVER use Q3_K_S** — catastrophic failure mode unique to this scale  
2. **NEVER use Q2_K variants** — quality equivalent to 4B model, not 32B  
3. **Prefer Q5_K_M over Q5_K_HIFI** — identical quality with standard compatibility  
4. **Always use imatrix with Q4_K_S** — closes 2.8% quality gap for free  
5. **Q4_K_M + imatrix is the pragmatic default** — excellent quality with minimal constraints

## Non-technical model anaysis and rankings

**NOTE:** This analysis does not include the HIFI models.

There are two very, very good candidates: **Qwen3-32B-f16:Q3_K_M** and **Qwen3-32B-f16:Q4_K_M**. These cover the full range of temperatures and were in the top 3 in nearly all question types.
**Qwen3-32B-f16:Q4_K_M** has a slightly better coverage across the temperature types.

**Qwen3-32B-f16:Q5_K_S** also did well, but because it's a larger model, it's not as highly recommended.

Despite being a larger parameter model, the Q2_K and Q3_K_S models are still such low quality that you should never use them.

You can read the results here: [Qwen3-32b-analysis.md](Qwen3-32b-analysis.md)

If you find this useful, please give the project a ❤️ like.

## Non-HIFI recommentation table based on output

| Level     | Speed     | Size       | Recommendation                                                                                                |
|-----------|-----------|------------|---------------------------------------------------------------------------------------------------------------|
| Q2_K      | ⚡ Fastest | 12.3 GB    | 🚨 **DO NOT USE.** Produced garbage results and is not reliable.                                              |
| Q3_K_S    | ⚡ Fast    | 14.4 GB    | 🚨 **DO NOT USE.** Not recommended, almost as bad as Q2_K.                                                    |
| 🥈 Q3_K_M  | ⚡ Fast    | 16.0 GB    | 🥈 Got top 3 results across nearly all questions. Basically the same as K4_K_M.                               |
| Q4_K_S    | 🚀 Fast   | 18.8 GB     | Not recommended. Got 2 2nd place results, one of which was the hello question.                                |
| 🥇 Q4_K_M  | 🚀 Fast   | 19.8 GB    | 🥇 **Recommended model** Slightly better than Q3_K_M, and also got top 3 results across nearly all questions. |
| 🥉 Q5_K_S  | 🐢 Medium | 22.6 GB    | 🥉 Got good results across the temperature range.                                                             |
| Q5_K_M    | 🐢 Medium | 23.2 GB    | Not recommended. Got 2 top-3 placements, but nothing special.                                                  |
| Q6_K      | 🐌 Slow   | 26.9 GB    | Not recommended. Got 2 top-3 placements, but also nothing special.                                             |
| Q8_0      | 🐌 Slow   | 34.8 GB    | Not recommended - no top 3 placements.                                                                         |

## Build notes

You can read the guide for building llama.cpp here: [HIFI_BUILD_GUIDE.md](https://github.com/geoffmunn/llama.cpp/blob/master/HIFI_BUILD_GUIDE.md).

The HIFI quantization also used a very large 4697 chunk imatrix file for extra precision. You can re-use it here: [Qwen3-32B-f16-imatrix-4697-generic.gguf](https://huggingface.co/geoffmunn/Qwen3-32B-f16/blob/main/Qwen3-32B-f16-imatrix-4697-generic.gguf)

The imatrix was created as a generic mix of Wikipedia, mathmatics, and coding examples.

### Source code

You can use the HIFI GitHub repository to build it from source if you're interested: [https://github.com/geoffmunn/llama.cpp](https://github.com/geoffmunn/llama.cpp).

Build notes: [HIFI_BUILD_GUIDE.md](https://github.com/geoffmunn/llama.cpp/blob/master/HIFI_BUILD_GUIDE.md)

Improvements and feedback are welcome.

## Usage

Load this model using:
- [OpenWebUI](https://openwebui.com) – self-hosted AI interface with RAG & tools
- [LM Studio](https://lmstudio.ai) – desktop app with GPU support and chat templates
- [GPT4All](https://gpt4all.io) – private, local AI chatbot (offline-first)
- Or directly via `llama.cpp`

Each quantized model includes its own `README.md` and shares a common `MODELFILE` for optimal configuration.

Importing directly into Ollama should work, but you might encounter this error: `Error: invalid character '<' looking for beginning of value`.
In this case try these steps:

1. `wget https://huggingface.co/geoffmunn/Qwen3-32B/resolve/main/Qwen3-32B-f16%3AQ4_K_M.gguf` (replace the quantised version with the one you want)
2. `nano Modelfile` and enter these details (again, replacing Q4_K_M with the version you want):
```text
FROM ./Qwen3-32B-f16:Q4_K_M.gguf

# Chat template using ChatML (used by Qwen)
SYSTEM You are a helpful assistant

TEMPLATE "{{ if .System }}<|im_start|>system
{{ .System }}<|im_end|>{{ end }}<|im_start|>user
{{ .Prompt }}<|im_end|>
<|im_start|>assistant
"
PARAMETER stop <|im_start|>
PARAMETER stop <|im_end|>

# Default sampling
PARAMETER temperature 0.6
PARAMETER top_p 0.95
PARAMETER top_k 20
PARAMETER min_p 0.0
PARAMETER repeat_penalty 1.1
PARAMETER num_ctx 4096
```

The `num_ctx` value has been dropped to increase speed significantly.

3. Then run this command: `ollama create Qwen3-32B-f16:Q4_K_M -f Modelfile`

You will now see "Qwen3-32B-f16:Q4_K_M" in your Ollama model list.

These import steps are also useful if you want to customise the default parameters or system prompt.

## Author

👤 Geoff Munn (@geoffmunn)  
🔗 [Hugging Face Profile](https://huggingface.co/geoffmunn)

## Disclaimer

This is a community conversion for local inference. Not affiliated with Alibaba Cloud or the Qwen team.
