---
license: apache-2.0
base_model:
  - Qwen/Qwen3.5-35B-A3B
  - Jackrong/Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled
tags:
  - merge
  - evolutionary-merge
  - darwin
  - darwin-v5
  - model-mri
  - reasoning
  - advanced-reasoning
  - chain-of-thought
  - thinking
  - qwen3.5
  - qwen
  - moe
  - mixture-of-experts
  - claude-opus
  - distillation
  - multimodal
  - vision-language
  - multilingual
  - 201-languages
  - gpqa
  - benchmark
  - open-source
  - apache-2.0
  - natural-selection
  - layer-wise-merge
  - moe-merge
  - dead-expert-revival
  - neural-anatomy
  - coding-agent
  - tool-calling
  - long-context
  - 262k-context
language:
  - en
  - zh
  - ko
  - ja
  - de
  - fr
  - es
  - ru
  - ar
  - multilingual
pipeline_tag: text-generation
library_name: transformers
model-index:
  - name: Darwin-35B-A3B-Opus
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
            value: 90.0
            name: Accuracy
            verified: false
      - task:
          type: text-generation
          name: Multilingual Knowledge
        dataset:
          type: openai/MMMLU
          name: MMMLU
        metrics:
          - type: accuracy
            value: 85.0
            name: Accuracy
            verified: false
---

# Darwin-35B-A3B-Opus

<p align="center">
  <img src="info.png" alt="Darwin-35B-A3B-Opus" width="100%">
</p>

<p align="center">
  <a href="https://huggingface.co/FINAL-Bench/Darwin-35B-A3B-Opus"><img src="https://img.shields.io/badge/🤗_Model-Darwin--35B--A3B--Opus-blue" alt="Model"></a>
  <a href="https://huggingface.co/spaces/FINAL-Bench/Darwin-35B-A3B-Opus"><img src="https://img.shields.io/badge/🚀_Space-Live_Demo-purple" alt="Space"></a>
  <a href="https://huggingface.co/spaces/FINAL-Bench/Leaderboard"><img src="https://img.shields.io/badge/🏆_FINAL_Bench-Leaderboard-green" alt="FINAL Bench"></a>
  <a href="https://huggingface.co/spaces/FINAL-Bench/all-bench-leaderboard"><img src="https://img.shields.io/badge/📊_ALL_Bench-Leaderboard-orange" alt="ALL Bench"></a>
</p>

<p align="center">
  <em>"The child surpassed both parents — that is evolution."</em>
</p>

<!-- SEO: Structured Summary for Search Engines & AI Answer Engines -->
<!-- 
Darwin-35B-A3B-Opus is a 35B parameter Mixture-of-Experts (MoE) language model with 3B active parameters, 
created by VIDRAFT using the Darwin V5 evolutionary merge engine with Model MRI integration.
It achieves 90.0% on GPQA Diamond (vs Father Qwen3.5-35B-A3B at 84.2%) and 85.0% on MMMLU,
while preserving multimodal capabilities (image/video), 201 language support, and 262K context length.
Licensed under Apache 2.0.
-->

> **TL;DR**: 35B MoE (3B active) | **GPQA Diamond 90.0%** (beats Father 84.2% & Mother 85.0%) | **MMMLU 85.0%** | Multimodal ✅ | 201 Languages | 262K Context | 147.8 tok/s | Apache 2.0
>
> `#Darwin` `#EvolutionaryMerge` `#ModelMRI` `#Qwen3.5` `#MoE` `#Reasoning` `#GPQA90` `#Multimodal` `#OpenSource` `#Apache2` `#DarwinV5` `#VIDRAFT`

---

## Why Darwin? — The Child That Surpassed Both Parents

The fundamental question of AI model merging: **If parent models already exist, why crossbreed?**

This model is the answer.

### Benchmark Results

**GPQA Diamond (198 Questions, Graduate-Level Reasoning)**

| Model | Accuracy | Multimodal | Benchmark Published |
|---|---|---|---|
| 🧬 **Darwin-35B-A3B-Opus (Child)** | **90.0%** | ✅ Image/Video | ✅ Fully Open |
| 👩 Mother — Jackrong Claude 4.6 Opus Distilled | 85.0% | ❌ Text-only | ❌ Not Published |
| 👨 Father — Qwen3.5-35B-A3B (Official) | 84.2% | ✅ Image/Video | ✅ Official |

> *Evaluation: SGLang, context 32768, temperature 0, greedy decoding, official GPQA prompt format ("ANSWER: LETTER")*

**MMMLU (Multilingual Knowledge, 29 Languages)**

| Model | Accuracy |
|---|---|
| 🧬 **Darwin-35B-A3B-Opus (Child)** | **85.0%** |
| 👨 Father — Qwen3.5-35B-A3B (Official) | 85.2% |

> *Darwin maintains Father-level multilingual knowledge while gaining superior reasoning.*

**The child surpassed both parents in reasoning, and matched the Father in multilingual knowledge.**

- GPQA vs Father: **+6.9% relative improvement** ((90.0−84.2)/84.2)
- GPQA vs Mother: **+5.9% relative improvement** ((90.0−85.0)/85.0)
- MMMLU: **85.0%** — Father-level (85.2%) multilingual knowledge preserved

### Why Not Just Use the Mother?

| | Mother (Claude Distilled) | Darwin (Child) |
|---|---|---|
| Reasoning | Strong (85.0%) | **Stronger (90.0%)** |
| Image/Video | ❌ Lost (text-only fine-tune) | ✅ Inherited from Father |
| 201 Languages | ❌ Potentially degraded | ✅ Inherited from Father |
| 262K Context | Unverified | ✅ Father's architecture preserved |
| Benchmark Transparency | ❌ No scores published | ✅ Fully open |

### Why Not Just Use the Father?

The Father (Qwen3.5-35B-A3B) excels in versatility but scores 84.2% on hard reasoning. Darwin **pushes reasoning to 90.0%** while maintaining Father-level multilingual knowledge (MMMLU 85.0% vs 85.2%) and all general capabilities.

**Conclusion: The only model that surpasses the Mother's reasoning, preserves the Father's multilingual knowledge, and retains full multimodal capabilities.**

---

## Model Overview

**Darwin-35B-A3B-Opus** is a next-generation reasoning-enhanced language model created by VIDRAFT's **Darwin V5** evolution engine.

Darwin V5 combines two innovations:
1. **Evolutionary Merge** — Applies natural selection to automatically find optimal weight combinations
2. **Model MRI Integration** — CT-scans parent models layer by layer before merging, guiding evolution with structural insight

If conventional merging is "mixing recipes blindfolded," Darwin V5 is **"precision surgery with X-ray guidance."**

---

## Parent Models

| Role | Model | Strengths |
|---|---|---|
| 👨 Father | [Qwen/Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B) | General knowledge, multimodal (image/video), coding, agents, 201 languages, 262K context |
| 👩 Mother | [Jackrong/Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/Jackrong/Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled) | Claude 4.6 Opus CoT distillation, structured step-by-step reasoning, coding agent compatibility |

---

## Darwin V5 — Beyond Simple Merge

### Limitations of Conventional Merging

Traditional model merging relies on humans setting hyperparameters like ratio and density **by intuition**. Set ratio=0.5, density=0.9, run once, and hope for the best. The result depends on luck, and applying the same ratio uniformly across billions of parameters ignores each layer's unique role.

### Darwin V4's Advance

Darwin V4 solved this with **evolutionary algorithms** — automatically searching hundreds of parameter combinations and selecting survivors by real benchmark scores. But V4 was still **blind evolution**: it didn't know what each layer does.

### Darwin V5: Model MRI Opens the Eyes

V5 integrates **Model MRI** (neural anatomy analyzer) to give evolution "sight":

```
[Phase 0] Model MRI — CT-scan both parents layer by layer
    ↓  "Father's layers 15-25 concentrate multilingual knowledge"
    ↓  "Mother's layers 30-40 concentrate reasoning patterns"
    ↓
[Phase 1] MRI-Guided Evolution — Start from scan-informed initial genome
    ↓  Not random, but "informed by CT results"
    ↓
[Phase 2] mergekit real merge + benchmark fitness selection
    ↓  Faster convergence in MRI-narrowed search space
    ↓
[Phase 3] MRI Health Check — CT-scan the child model
    ↓  Detect interference, function loss
    ↓  Prescribe layer-specific ratio adjustments
    ↓
[Final] Darwin-35B-A3B-Opus
```

### V4 vs V5

| | Darwin V4 | Darwin V5 |
|---|---|---|
| Analogy | Mixing recipes blindfolded | **Precision surgery with X-ray** |
| Initial genome | Random | **MRI-guided** |
| Layer control | 2 ratios (attn/ffn) | **40 layers independently** |
| Pre-diagnosis | ❌ None | ✅ Phase 0 MRI scan |
| Post-verification | Benchmark only | ✅ Phase 3 health check |
| Search efficiency | Wide space | **Narrowed, guided search** |
| Failure diagnosis | Unknown "why" | **Pinpoint which layer failed** |

---

### Darwin V4: Discovered Optimal Parameters (Blind Evolution)

| Parameter | Value | Meaning |
|---|---|---|
| ratio | 0.481 | Father 52% : Mother 48% asymmetric blend |
| density_a | 0.855 | Selected 85.5% of Father's weights |
| density_b | 0.971 | Adopted 97.1% of Mother's weights |
| attn | 0.168 | Only 16.8% change in attention layers |
| ffn | 0.841 | 84.1% change in FFN layers |

**Interpretation:** Attention patterns (what to focus on) are **almost entirely preserved** from the Father, while FFN layers (knowledge storage) are **largely replaced** with the Mother's reasoning patterns.

Discovering attn=0.168 and ffn=0.841 — this extreme asymmetry — is **virtually impossible by human intuition**.

### Darwin V5: MRI-Guided Merge Recipe

After scanning both parents, Model MRI generated a fundamentally different prescription:

<p align="center"><img src="a2.png" width="500" alt="MRI-Guided Genome"></p>

| Parameter | V4 (Blind) | V5 (MRI) | Change |
|---|---|---|---|
| global_ratio | 0.481 | **0.800** | Mother weight ↑↑ |
| attn_ratio | 0.168 | **0.320** | Attention also shifts to Mother |
| ffn_ratio | 0.841 | **0.590** | FFN becomes more conservative |
| density_a | 0.855 | **0.799** | Similar |
| density_b | 0.971 | **0.799** | Mother density ↓ (Dead Expert compensation) |

**Key insight:** MRI prescribed "use more of the Mother (ratio 0.8), but reduce density (0.799) because 50-65% of her experts are dead." V4 found ratio=0.481 blindly — the **opposite direction**.

### Layer-Wise Merge Strategy (3 Blocks)

MRI didn't apply uniform ratios. It split 40 layers into 3 blocks:

<p align="center"><img src="a1.png" width="700" alt="Merge Ratio + Parent Importance + MoE Health per Layer"></p>

| Block | Layers | t (Mother %) | Router Source | Rationale |
|---|---|---|---|---|
| Block 1 | L0~L37 | **59.9%** | Mother | Reasoning pattern injection across most layers |
| Block 2 | L38 | **90.0%** | Mother | **Golden Layer — Mother's reasoning engine core** |
| Block 3 | L39 | **53.4%** | Father | Output layer — Father's router preserves multimodal routing |

**L38 is the "Golden Layer"**: Mother's MRI showed peak cosine distance at L34~L38 (see Mother MRI below). Darwin V5 responded by assigning t=0.9 to L38 — transplanting the Mother's reasoning engine almost entirely.

---

## Model MRI Scans — Parent Neural Anatomy

### Mother MRI: Claude 4.6 Opus Distilled

<p align="center"><img src="m3.png" width="600" alt="Mother Probe Cosine Distance"></p>

**Probe-wise Layer Importance:** L34~L38 shows intense red (high cosine distance) across REASONING, CODE, LOGIC probes — this is the Mother's reasoning engine.

<p align="center"><img src="m1.png" width="500" alt="Mother MoE Health"></p>

| Metric | Status | Interpretation |
|---|---|---|
| Router Entropy | ✅ ~1.0 across all layers | Healthy — experts evenly distributed |
| **Dead Expert %** | 🔴 **50~65%** | **Critical — Claude distillation killed half the experts** |
| Expert Similarity | ✅ 0.001~0.008 | Healthy — surviving experts remain diverse |

**Dead Expert 50~65% is the fingerprint of Claude text-only distillation.** The fine-tuning killed multimodal and multilingual experts that were no longer activated during text-only training.

<p align="center"><img src="m2.png" width="600" alt="Mother Expert Utilization"></p>

**Expert Utilization Heatmap:** Mostly dark (inactive) with sparse bright activations — the Claude reasoning pattern is concentrated in a small number of specialized experts.

### Father MRI: Healthy Generalist (Organ Donor)

<p align="center"><img src="f1.png" width="500" alt="Father MoE Health"></p>

<p align="center"><img src="f2.png" width="600" alt="Father Expert Utilization"></p>

<p align="center"><img src="f3.png" width="600" alt="Father Layer Importance by Probe"></p>

The Father (Qwen3.5-35B-A3B) shows **healthy, uniform expert activation** across all 40 layers — a well-balanced generalist with all experts alive. This is the "organ donor" that revives the Mother's dead 50–65% experts.

### Parent Comparison: Layer Advantage Map

<p align="center"><img src="a3.png" width="600" alt="Parent A vs B Layer Advantage"></p>

- **Above zero (↑ A):** Father stronger — primarily L0~L5 (embedding/early layers)
- **Below zero (↓ B):** Mother stronger — scattered but consistent across L5~L35
- **L34~L38:** Mother shows strongest advantage in REASONING and CODE probes
- **L39:** Father recovers — output layer favors Father's multimodal routing

This advantage map directly informed the 3-block merge recipe: Mother dominates L0~L38, Father retakes L39.

### How GPQA 90% Was Achieved

```
Mother L34~L38 reasoning engine (MRI red zone)
    ↓ t=0.9 — transplanted almost entirely
    +
Father L39 output router (multimodal/multilingual expert activation)
    ↓ t=0.53 — Father's routing preserved
    +
Dead Expert replacement → Father's living experts fill Mother's dead slots
    ↓
= GPQA 90.0% (surpassed both parents)
```

The Mother's "reasoning brain" was transplanted while her dead experts were replaced with the Father's living ones. **Reasoning went up, versatility was preserved.**

### Evolution History

- Phase 1 → Phase 2 evolution complete
- Final real_score: **0.8405**
- Merge time: 181.6 seconds
- Merge commit: `109838c2`

---

## Model MRI Health Check — Child vs Parents

<p align="center">
  <img src="c1.png" alt="Darwin Health Check — Child vs Parents" width="100%">
</p>

**✅ Health: Healthy — No issues detected.**

The chart above shows the **layer-by-layer importance** of the child (Darwin, green bars) compared to both parents (Father = blue dashed, Mother = red dashed). Key findings:

**Layer 0 (Embedding):** Child importance spikes to 0.42 — both parents show similar peaks (~0.35–0.50). The child successfully inherited the critical embedding layer from both parents without interference.

**Layers 1–33 (Middle):** Near-zero importance across all three models. This is normal — middle layers in MoE models process information incrementally, with no single layer being critical. The child tracks both parents perfectly, confirming **no function loss** in the bulk of the network.

**Layers 34–39 (Reasoning Engine):** Importance rises sharply. This is the region where Mother's MRI showed intense reasoning activity (cosine distance > 0.6). The child's green bars match or exceed both parents — proving that **Mother's reasoning patterns were successfully transplanted** while Father's output routing was preserved.

**Layer 39 (Output):** Child peaks at ~0.48, closely matching both parents. The final output layer is intact.

### Why This Matters

The MRI health check confirms three things:
1. **No interference** — No layer where child importance abnormally exceeds parents (which would indicate weight conflict)
2. **No function loss** — No layer where parents had high importance but child dropped to zero
3. **Successful transplant** — L34–L39 reasoning engine from Mother is fully operational in the child

### Darwin V5 MRI-Guided Merge Recipe

```yaml
# MRI-guided layer-wise merge (3 blocks)
# Genome: ratio=0.800 attn=0.320 ffn=0.590 density=0.799

L0–L37:  t=0.5988 (Mother 60%) — router from Mother
L38:     t=0.9000 (Mother 90%) — "Golden Layer" reasoning core
L39:     t=0.5336 (Father 47%) — router from Father (output routing)
```

| Insight | Detail |
|---|---|
| **L38 = "Golden Layer"** | MRI identified L34–L38 as Mother's reasoning core. Darwin assigned t=0.9 (90% Mother) to L38 specifically |
| **Router Strategy: B→B→A** | Mother's router for reasoning layers, Father's router for final output — preserves both reasoning paths and multimodal routing |
| **Dead Expert Revival** | Mother's 50–65% dead experts (killed by text-only fine-tuning) were replaced with Father's live experts — restoring multimodal and multilingual capabilities |

---

## Inherited Capabilities

### From Father (Qwen3.5-35B-A3B)
- **Multimodal**: Image and video understanding
- **201 Languages**: Global linguistic coverage
- **262K Context**: Native long-context (extendable to 1M via YaRN)
- **Gated DeltaNet + MoE**: Efficient hybrid architecture
- **Multi-Token Prediction**: Improved inference throughput

### From Mother (Claude 4.6 Opus Distilled)
- **Structured Thinking**: Systematic step-by-step reasoning within `<think>` tags
- **Efficient Reasoning**: "Let me analyze this request carefully: 1..2..3..." pattern
- **Coding Agent Compatibility**: Native "developer" role support for Claude Code, OpenCode
- **Tool Calling Stability**: Consistent performance in tool-use scenarios
- **Autonomous Execution**: Extended autonomous operation in agentic environments

---

## Father's Official Benchmarks (Reference)

Darwin is built on this architecture with enhanced reasoning:

| Category | Benchmark | Father Official |
|---|---|---|
| Knowledge | MMLU-Pro | 85.3 |
| Knowledge | MMLU-Redux | 93.3 |
| Reasoning | GPQA Diamond | 84.2 |
| Reasoning | HLE w/ CoT | 22.4 |
| Math | HMMT Feb 2025 | 89.0 |
| Coding | SWE-bench Verified | 69.2 |
| Coding | LiveCodeBench v6 | 74.6 |
| Agent | TAU2-Bench | 81.2 |
| Agent | BFCL-V4 (Tool Use) | 67.3 |
| Instruction | IFEval | 91.9 |
| Multilingual | MMMLU | 85.2 |
| Agentic Search | BrowseComp | 61.0 |

---

## Performance

### Inference Speed

| Metric | Value |
|---|---|
| **Generation Speed** | **147.8 tok/s** |
| Environment | Single NVIDIA H100 93GB NVL, SGLang, BF16 |
| Qwen Official API | 162.8 tok/s (Alibaba Cloud) |

### Hardware Requirements

| Setup | VRAM | Status |
|---|---|---|
| **BF16 (Full Precision)** | **65.5 GiB** | |
| Single H100 93GB NVL | 93 GB | ✅ Comfortable |
| Single A100 80GB | 80 GB | ⚠️ Tight |
| Single A100 40GB | 40 GB | ❌ Insufficient |
| **Q8 Quantized** | **~35 GiB** | |
| Single A100 40GB | 40 GB | ✅ Possible |
| **Q4_K_M Quantized** | **~18 GiB** | |
| Single RTX 4090 24GB | 24 GB | ✅ Comfortable |
| 2× RTX 4090 (tp=2) | 48 GB | ✅ BF16 possible |

> As a Mixture-of-Experts model, only 3B parameters are active per token despite loading the full 35B. Quantization has minimal impact due to this sparsity.

---

## Model Specifications

| | |
|---|---|
| Architecture | Qwen3.5 MoE (Gated DeltaNet + MoE) |
| Total Parameters | 35B |
| Active Parameters | 3B per forward pass |
| Hidden Dimension | 2,048 |
| Layers | 40 |
| Layer Layout | 10 × (3 × GDN→MoE + 1 × Attention→MoE) |
| Experts | 256 (8 routed + 1 shared active) |
| Expert Intermediate Dim | 512 |
| Context Length | 262,144 native (up to 1,010,000 via YaRN) |
| Languages | 201 |
| Multimodal | ✅ Image & Video input |
| License | Apache 2.0 |
| Engine | Darwin V5 (Evolutionary Merge + Model MRI) |
| Evolution Phase | Phase 2, real_score 0.8405 |
| Merge Commit | 109838c2 |

---

## Usage

### SGLang (Recommended)

```bash
python -m sglang.launch_server \
  --model-path FINAL-Bench/Darwin-35B-A3B-Opus \
  --tp 1 \
  --mem-fraction-static 0.90 \
  --context-length 32768 \
  --trust-remote-code
```

### vLLM

```bash
vllm serve FINAL-Bench/Darwin-35B-A3B-Opus \
  --trust-remote-code \
  --enforce-eager
```

### Transformers

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("FINAL-Bench/Darwin-35B-A3B-Opus", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    "FINAL-Bench/Darwin-35B-A3B-Opus",
    dtype="bfloat16",
    device_map="auto",
    trust_remote_code=True,
)
```

### Best Practices
- Use **context ≥ 32K** for reasoning tasks — the model leverages extended thinking
- For maximum reasoning quality, use **thinking mode (default)** with sufficient max_tokens (≥ 16384)
- The model generates `<think>` blocks for internal reasoning; extract the final answer after `</think>`

---

## Built By

| | |
|---|---|
| Developer | **VIDRAFT** |
| Evolution Engine | Darwin V5 (Evolutionary Merge + Model MRI) |
| Infrastructure | 4 × NVIDIA H100 93GB NVL GPU |
| Merge Time | 181.6 seconds |
| Shard Distribution | 14 shards → GPU [1, 2, 3] round-robin |

---

## Acknowledgements

- **Korean Government** — This research was supported by the Korean Government's 'GPU Support Program' research grant
- [Qwen Team](https://huggingface.co/Qwen) — Qwen3.5-35B-A3B base architecture
- [Jackrong](https://huggingface.co/Jackrong) — Claude 4.6 Opus Reasoning Distilled model
- [nohurry](https://huggingface.co/datasets/nohurry/Opus-4.6-Reasoning-3000x-filtered), [TeichAI](https://huggingface.co/datasets/TeichAI/claude-4.5-opus-high-reasoning-250x) — Distillation datasets

---

## Citation

```bibtex
@misc{vidraft_darwin_35b_opus,
  title        = {Darwin-35B-A3B-Opus: MRI-Guided Evolutionary Merge Beyond Both Parents},
  author       = {VIDRAFT},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/FINAL-Bench/Darwin-35B-A3B-Opus}}
}
```
---

## Contact
 
📧 **kkms1116@koreacu.ac.kr**
 
---

## FAQ (Frequently Asked Questions)

<details>
<summary><b>What is Darwin-35B-A3B-Opus?</b></summary>
Darwin-35B-A3B-Opus is a 35 billion parameter Mixture-of-Experts language model (3B active per token) that was created using evolutionary merge techniques. It combines Qwen3.5-35B-A3B's multimodal versatility with Claude 4.6 Opus reasoning distillation, achieving 90.0% on GPQA Diamond — surpassing both parent models.
</details>

<details>
<summary><b>How does Darwin V5 differ from simple model merging?</b></summary>
Traditional merging applies uniform ratios by guesswork. Darwin V5 uses evolutionary algorithms (natural selection) combined with Model MRI (neural CT-scanning) to automatically discover optimal layer-specific merge ratios. For example, it found attn=0.168 and ffn=0.841 — an extreme asymmetry impossible to find by intuition.
</details>

<details>
<summary><b>What GPU do I need to run this model?</b></summary>
For BF16 full precision: A100 80GB (tight) or H100 93GB (comfortable). For Q4 quantization: a single RTX 4090 (24GB) is sufficient. The model loads 35B parameters but only activates 3B per token due to its MoE architecture.
</details>

<details>
<summary><b>Does it support multimodal (images/video)?</b></summary>
Yes. Darwin inherits the Father model's (Qwen3.5-35B-A3B) full multimodal capabilities including image and video understanding, unlike the Mother model which lost this during text-only fine-tuning.
</details>

<details>
<summary><b>What languages does it support?</b></summary>
201 languages and dialects, inherited from Qwen3.5's multilingual training. MMMLU benchmark confirms 85.0% multilingual knowledge retention across 29 evaluated languages.
</details>

<details>
<summary><b>What is Model MRI?</b></summary>
Model MRI is a neural anatomy analysis tool that CT-scans each layer of a language model to understand what functions it performs. When integrated with Darwin, it guides the evolutionary merge process — telling the algorithm which layers to preserve from each parent and which to replace. In this model, MRI identified L38 as the Mother's "golden layer" (core reasoning engine) and prescribed 90% Mother weight for that specific layer.
</details>

<details>
<summary><b>What are "Dead Experts" and why does it matter?</b></summary>
In Mixture-of-Experts (MoE) models, each layer contains hundreds of specialist sub-networks (experts). The Mother model's Claude distillation killed 50–65% of these experts because text-only fine-tuning didn't activate multimodal/multilingual specialists. Darwin's MRI detected this and prescribed replacing dead experts with the Father's living ones — reviving capabilities the Mother lost.
</details>

<details>
<summary><b>Is this model open source?</b></summary>
Yes. Darwin-35B-A3B-Opus is released under the Apache 2.0 license, fully open for commercial and research use.
</details>

---

<!-- AEO: Keywords for AI Answer Engines -->
<!-- 
Keywords: Darwin-35B-A3B-Opus, evolutionary merge, model merging, Darwin V5, Model MRI, 
GPQA Diamond 90%, Qwen3.5-35B-A3B, Claude 4.6 Opus, reasoning model, mixture of experts, 
MoE 3B active, 35B parameters, multimodal LLM, 201 languages, 262K context, 
open source AI model, Apache 2.0, VIDRAFT, natural selection AI, 
layer-wise merge ratio, attention preservation, FFN replacement,
best open source reasoning model 2026, Qwen merge, coding agent compatible,
dead expert revival, golden layer L38, MoE merge technique, neural anatomy analysis,
router entropy, expert utilization heatmap, cosine distance probe, 3-block surgical merge
-->

`#DarwinAI` `#EvolutionaryMerge` `#ModelMRI` `#DarwinV5` `#GPQA90` `#Qwen35` `#MoE3B` `#Reasoning` `#Multimodal` `#201Languages` `#OpenSource` `#Apache2` `#VIDRAFT` `#NaturalSelection` `#LayerWiseMerge` `#ClaudeOpus` `#ThinkingModel` `#CodingAgent` `#LongContext262K` `#BestOpenSourceLLM2026` `#DeadExpertRevival` `#GoldenLayer` `#MoEMerge` `#NeuralAnatomy`