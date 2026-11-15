---
license: cc-by-4.0
base_model: FacebookAI/xlm-roberta-large
datasets:
  - Squezilia/Route4Secure
language:
  - ar
  - de
  - en
  - es
  - fr
  - hi
  - it
  - ja
  - ko
  - nl
  - th
  - zh
pipeline_tag: text-classification
library_name: transformers
tags:
  - prompt-routing
  - llm-router
  - safety-guardrail
  - multi-task-learning
  - complexity-classification
  - reasoning-detection
  - xlm-roberta-large
  - route4secure
  - multilingual
  - onnx
  - quantized
  - edge-ai
model-index:
  - name: xlm-r-r4s-large
    results:
      - task:
          type: text-classification
          name: Multi-Task Prompt Routing & Safety Classification
        dataset:
          name: Squezilia/Route4Secure (Validation Split)
          type: Squezilia/Route4Secure
          split: validation
        metrics:
          - type: f1
            value: 0.8106
            name: Mean Macro F1 (4 Heads)
          - type: accuracy
            value: 0.8352
            name: Mean Accuracy (4 Heads)
          - type: accuracy
            value: 0.9224
            name: Safety Accuracy
          - type: f1
            value: 0.9210
            name: Safety Macro F1
          - type: accuracy
            value: 0.9353
            name: Reasoning Accuracy
          - type: f1
            value: 0.9152
            name: Reasoning Macro F1
          - type: accuracy
            value: 0.7714
            name: Category Accuracy
          - type: f1
            value: 0.6826
            name: Category Macro F1
          - type: accuracy
            value: 0.7116
            name: Complexity Level Accuracy
          - type: f1
            value: 0.7235
            name: Complexity Level Macro F1
---

# xlm-r-r4s-large: Unified Multilingual Prompt Router & Safety Guardrail

**`Squezilia/xlm-r-r4s-large`** is a **563M-parameter multi-task transformer encoder** built on **[`FacebookAI/xlm-roberta-large`](https://huggingface.co/FacebookAI/xlm-roberta-large)** and fine-tuned on the **[`Squezilia/Route4Secure`](https://huggingface.co/datasets/Squezilia/Route4Secure)** dataset (`130,050` prompts across 12 languages).

Unlike conventional single-task classifiers that require chaining separate moderation models, domain classifiers, and difficulty scorers in sequence, **`xlm-r-r4s-large`** evaluates a user prompt in a **single forward pass** and simultaneously predicts four orthogonal routing signals:

1. **🛡️ Binary Safety Guardrail (`safe` — 2 classes)**: Detects harmful, adversarial, or policy-violating prompts (`UNSAFE` vs. `SAFE`) with **92.24% accuracy** (`0.9210` Macro F1).
2. **🧠 Reasoning Requirement (`requires_reasoning` — 2 classes)**: Determines whether a prompt can be answered directly or requires multi-step Chain-of-Thought (CoT) deduction (`DIRECT` vs. `REASONING`) with **93.53% accuracy** (`0.9152` Macro F1).
3. **🏷️ Domain Intent Router (`category` — 13 classes)**: Classifies the functional domain of the prompt (`Coding & Software`, `Mathematics`, `Information & Science`, `Security & Hijack`, etc.) with **77.14% accuracy** (up to **94.71% F1** on `Mathematics` and **89.81% F1** on `Coding & Software`).
4. **📊 Complexity Estimator (`level` — 8 classes)**: Scores inherent task difficulty from `Level_0` (trivial greetings/chit-chat) to `Level_7` (expert competition math & systems architecture) with **71.16% exact-level accuracy** (`0.7235` Macro F1, reaching **90.62% F1** on `Level_7`).

---

## 📑 Table of Contents
1. [Model Overview & Architecture](#1-model-overview--architecture)
2. [Task Heads & Label Space](#2-task-heads--label-space)
3. [Training Data (`Squezilia/Route4Secure`)](#3-training-data-squeziliaroute4secure)
4. [Training Procedure & Hardware Optimizations](#4-training-procedure--hardware-optimizations)
5. [Evaluation Results & Benchmarks](#5-evaluation-results--benchmarks)
6. [ONNX & Quantized Edge Deployment (`FP16`, `INT8`, `Q4`)](#6-onnx--quantized-edge-deployment-fp16-int8-q4)
7. [Quickstart & Inference Usage (PyTorch & Zero-PyTorch Edge)](#7-quickstart--inference-usage-pytorch--zero-pytorch-edge)
8. [Production Routing & Tier Bucketing Strategy](#8-production-routing--tier-bucketing-strategy)
9. [Limitations & Bias Analysis](#9-limitations--bias-analysis)
10. [License & Citation](#10-license--citation)

---

## 1. Model Overview & Architecture

`XLMRobertaForMultiTaskRouting` shares a single 24-layer `XLM-RoBERTa-Large` backbone (`hidden_size = 1024`, `intermediate_size = 4096`, `16` attention heads) across four independent classification heads attached to the `<s>` (`[CLS]`) token representation:

```text
                                 [ User Prompt ]
                                        │
                                        ▼
                      ┌───────────────────────────────────┐
                      │     XLM-RoBERTa-Large Backbone    │
                      │  (24 Layers, 1024d, 563.06M Params)│
                      └─────────────────┬─────────────────┘
                                        │
                             <s> Sequence Representation
                                  x = H[:, 0, :]
                                        │
        ┌───────────────────┬───────────┴───────────┬───────────────────┐
        ▼                   ▼                       ▼                   ▼
┌───────────────┐   ┌───────────────┐       ┌───────────────┐   ┌───────────────┐
│   head_safe   │   │ head_category │       │  head_level   │   │head_reasoning │
│  1024 ──► 2   │   │  1024 ──► 13  │       │  1024 ──► 8   │   │  1024 ──► 2   │
│ (UNSAFE/SAFE) │   │ (13 Domains)  │       │ (Level_0..7)  │   │(DIRECT/REASON)│
└───────────────┘   └───────────────┘       └───────────────┘   └───────────────┘
```

### Classification Head Formulation (`MultiTaskClassificationHead`)
Each task head $k \in \{\text{safe}, \text{category}, \text{level}, \text{reasoning}\}$ applies a dedicated non-linear projection with dropout ($p = 0.1$) over the shared `<s>` token state $h_{\text{CLS}} \in \mathbb{R}^{1024}$:

$$\mathbf{z}_k = \mathbf{W}_{k,\text{out}}\Big(\text{Dropout}\big(\tanh(\mathbf{W}_{k,\text{dense}}\,\text{Dropout}(h_{\text{CLS}}) + \mathbf{b}_{k,\text{dense}})\big)\Big) + \mathbf{b}_{k,\text{out}}$$

### Multi-Task Training Objective
During fine-tuning, all four heads are optimized jointly with equal task weighting ($w_k = 1.0$) using standard cross-entropy loss:

$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{CE}}(\mathbf{z}_{\text{safe}}, y_{\text{safe}}) + \mathcal{L}_{\text{CE}}(\mathbf{z}_{\text{category}}, y_{\text{category}}) + \mathcal{L}_{\text{CE}}(\mathbf{z}_{\text{level}}, y_{\text{level}}) + \mathcal{L}_{\text{CE}}(\mathbf{z}_{\text{reasoning}}, y_{\text{reasoning}})$$

| Component | Parameter Count | Details |
| :--- | ---: | :--- |
| **`roberta` (Shared Backbone)** | `558,840,832` | 24 Transformer blocks + `250,002`-vocab embeddings (`add_pooling_layer=False`) |
| **`head_safe`** | `1,051,650` | `Linear(1024, 1024)` + `Linear(1024, 2)` |
| **`head_category`** | `1,062,925` | `Linear(1024, 1024)` + `Linear(1024, 13)` |
| **`head_level`** | `1,057,800` | `Linear(1024, 1024)` + `Linear(1024, 8)` |
| **`head_reasoning`** | `1,051,650` | `Linear(1024, 1024)` + `Linear(1024, 2)` |
| **Total Trainable Parameters** | **`563,064,857`** | 100% Full Fine-Tuning (`BF16` mixed precision) |

---

## 2. Task Heads & Label Space

All label mappings are stored directly in `config.json` under `id2label_safe`, `id2label_category`, `id2label_level`, and `id2label_reasoning`.

### 2.1. Safety Head (`safe_logits` — 2 Classes)
| ID | Label | Description |
| :---: | :--- | :--- |
| `0` | `UNSAFE` | Harmful, adversarial, jailbreak, or policy-violating prompt (grounded in NVIDIA Aegis 2.0 taxonomy). |
| `1` | `SAFE` | Benign conversational, educational, technical, or creative request. |

### 2.2. Domain Category Head (`category_logits` — 13 Classes)
| ID | Category Label | Validation Support | Description |
| :---: | :--- | ---: | :--- |
| `0` | `Arts & Culture` | 195 | Music, visual arts, film, cultural history, and aesthetics. |
| `1` | `Coding & Software` | 1,129 | Programming, debugging, algorithms, DevOps, SQL, and software architecture. |
| `2` | `Data Manipulation` | 122 | Formatting, JSON/CSV/XML parsing, regex extraction, and structured data transformation. |
| `3` | `Information & Science` | 2,449 | Factual queries, natural sciences, history, geography, medicine, and general encyclopedic QA. |
| `4` | `Language Translation` | 68 | Cross-lingual translation, localization, and grammar correction. |
| `5` | `Logical Reasoning & Problem Solving` | 466 | Logic puzzles, brainteasers, causal deduction, and constraint satisfaction. |
| `6` | `Mathematics` | 698 | Arithmetic, algebra, calculus, probability, number theory, and formal mathematical proofs. |
| `7` | `Media Generation` | 39 | Image, audio, or video generation prompts and multimodal synthesis instructions. |
| `8` | `Other` | 3,245 | Casual chat, open-ended advice, daily life queries, and miscellaneous conversational turns. |
| `9` | `Roleplaying` | 834 | Persona adoption, interactive fiction, character simulation, and scenario acting. |
| `10` | `Security & Hijack` | 1,440 | Cybersecurity queries, adversarial prompt injections, jailbreaks, and exploit requests. |
| `11` | `Text Processing & Summarization` | 225 | Summarization, paraphrasing, information extraction, and sentiment/tone rewriting. |
| `12` | `Writing & Content Creation` | 2,095 | Essays, creative writing, marketing copy, emails, poetry, and scripts. |

### 2.3. Complexity Level Head (`level_logits` — 8 Classes)
| ID | Label | Routing Tier | Description |
| :---: | :--- | :--- | :--- |
| `0` | `Level_0` | **Trivial** | Simple greetings, single-word acknowledgments, or trivial boilerplate (`"Hello"`, `"Thanks"`). |
| `1` | `Level_1` | **Basic** | Direct single-fact lookups, basic definitions, or simple everyday requests. |
| `2` | `Level_2` | **Low-Intermediate** | Short explanations, standard summarization, or straightforward multi-sentence queries. |
| `3` | `Level_3` | **Intermediate** | Structured comparisons, routine coding snippets, or multi-constraint drafting. |
| `4` | `Level_4` | **Upper-Intermediate** | Non-trivial algorithm explanations, multi-step domain analysis, or debugging tasks. |
| `5` | `Level_5` | **Advanced** | Complex algorithmic problem-solving, undergraduate STEM problems, and multi-component code. |
| `6` | `Level_6` | **Expert** | Olympiad-style mathematics, formal proofs, and intricate systems engineering. |
| `7` | `Level_7` | **Frontier** | Research-grade mathematical/scientific reasoning and competition-level algorithmic challenges. |

### 2.4. Reasoning Detection Head (`reasoning_logits` — 2 Classes)
| ID | Label | Description |
| :---: | :--- | :--- |
| `0` | `DIRECT` | Can be answered directly via factual recall, pattern matching, or single-pass generation. |
| `1` | `REASONING` | Benefits significantly from explicit Chain-of-Thought (CoT) or test-time compute scaling. |

---

## 3. Training Data (`Squezilia/Route4Secure`)

The model was trained on the `default` configuration of **[`Squezilia/Route4Secure`](https://huggingface.co/datasets/Squezilia/Route4Secure)** (`130,050` rows total), partitioned via a **90% / 10% stratified split** (`seed = 42`, stratified jointly on `safe × category`):
* **Training Set:** `117,045` prompts
* **Validation Set:** `13,005` prompts

### Dataset Composition & Multilingual Coverage
* **Upstream Sources:** Combines human conversations from **OpenAssistant (`OASST1` & `OASST2`)**, safety and adversarial examples from **NVIDIA Nemotron Safety Guard Dataset v3**, and expert-tier (`Level_5`–`Level_7`) STEM/coding prompts from **OpenThoughts3-1.2M**.
* **12 Balanced Languages:** English (`en`), Spanish (`es`), Simplified Chinese (`zh-CN`), German (`de`), French (`fr`), Thai (`th`), Dutch (`nl`), Arabic (`ar`), Japanese (`ja`), Italian (`it`), Hindi (`hi`), and Korean (`ko`).

---

## 4. Training Procedure & Hardware Optimizations

Training was conducted on **Google Colab** using a single **NVIDIA A100-SXM4-40GB GPU** (`PyTorch 2.11.0+cu130`, `Compute Capability 8.0`).

### Hyperparameters

| Hyperparameter | Value | Notes |
| :--- | :--- | :--- |
| **Base Model** | `FacebookAI/xlm-roberta-large` | Full parameter fine-tuning (`USE_LORA = False`) |
| **Max Sequence Length** | `256` tokens | Dynamic batch padding via `DataCollatorWithPadding` |
| **Batch Size** | `32` (Train) / `64` (Eval) | `gradient_accumulation_steps = 1` (Effective batch size = `32`) |
| **Optimizer** | `adamw_torch_fused` | CUDA-fused AdamW (`weight_decay = 0.01`) |
| **Learning Rate** | `2.5e-5` | Cosine decay (`lr_scheduler_type = "cosine"`) |
| **Warmup Ratio** | `0.10` | 10% warmup over total training steps |
| **Epochs & Total Steps** | `3` Epochs (`10,974` steps) | Evaluated & checkpointed every `500` steps |
| **Precision** | `BF16` + `TF32` | Native Ampere `bfloat16` mixed precision & TensorFloat-32 matmuls |
| **Batch Sampling** | `group_by_length` | Length-bucketed sampling to minimize padding overhead |
| **Best Model Criterion** | `mean_f1_macro` | Unweighted mean of Macro F1 across all 4 heads |
| **Total Wall-Clock Time** | **30.78 minutes** | `~5.95s` per 100 training steps |

### Engineering & Hardware Notes
* **SDPA & Multi-Head Gradient Checkpointing:** Enabling `gradient_checkpointing` with PyTorch SDPA when four classification heads branch from the same shared encoder output triggers a tensor save count mismatch (`CheckpointError: 101 vs 32 tensors`) during backward recomputation. Because peak VRAM usage at `batch_size = 32` and `max_length = 256` with `BF16` is only **~10 GB** on a 40 GB A100, disabling gradient checkpointing eliminated the recomputation bug and accelerated training throughput by **~30%**.
* **Zero-Copy Arrow Tokenization:** Batched pre-tokenization (`batch_size = 1000`) backed by memory-mapped Apache Arrow tables kept host RAM usage well within standard 12–14 GB system limits without requiring High-RAM instances.

---

## 5. Evaluation Results & Benchmarks

All metrics below are reported on the held-out **validation split (`13,005` prompts)** at the best checkpoint (**Step `10,974`**, Epoch 3.0).

### 5.1. Overall Multi-Task Summary

| Task Head | Classes | Accuracy (%) | Macro Precision | Macro Recall | Macro F1 | Weighted F1 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. Safety (`safe`)** | 2 | **92.24%** | 0.9192 | 0.9234 | **0.9210** | 0.9226 |
| **2. Reasoning (`requires_reasoning`)** | 2 | **93.53%** | 0.9190 | 0.9116 | **0.9152** | 0.9350 |
| **3. Category (`category`)** | 13 | **77.14%** | 0.6881 | 0.6801 | **0.6826** | 0.7702 |
| **4. Complexity Level (`level`)** | 8 | **71.16%** | 0.7404 | 0.7099 | **0.7235** | 0.7112 |
| **Mean Composite Score** | — | **83.52%** | **0.8167** | **0.8063** | **0.8106** | **0.8348** |

---

### 5.2. Head 1: Binary Safety Guardrail (`safe`)

| Class | Precision | Recall | F1-Score | Support |
| :--- | :---: | :---: | :---: | ---: |
| `0: UNSAFE` | 0.8919 | **0.9296** | 0.9104 | 5,513 |
| `1: SAFE` | **0.9465** | 0.9171 | **0.9316** | 7,492 |
| **Macro Avg** | 0.9192 | 0.9234 | **0.9210** | 13,005 |
| **Weighted Avg** | 0.9234 | 0.9224 | **0.9226** | 13,005 |

> [!TIP]
> The safety head achieves a **92.96% recall on `UNSAFE` prompts** and a **94.65% precision on `SAFE` prompts** at the default `0.50` threshold. In high-security deployments, lowering the `UNSAFE` probability threshold to `0.35–0.40` further increases unsafe recall while maintaining low false-positive rates.

---

### 5.3. Head 2: Domain Category Router (`category`)

| Category | Precision | Recall | F1-Score | Support |
| :--- | :---: | :---: | :---: | ---: |
| `Mathematics` | **0.9457** | **0.9484** | **0.9471** | 698 |
| `Coding & Software` | **0.9025** | **0.8937** | **0.8981** | 1,129 |
| `Information & Science` | 0.8090 | 0.8285 | **0.8186** | 2,449 |
| `Writing & Content Creation` | 0.7943 | 0.8091 | **0.8016** | 2,095 |
| `Other` | 0.7680 | 0.7772 | **0.7726** | 3,245 |
| `Roleplaying` | 0.7033 | 0.6451 | 0.6729 | 834 |
| `Security & Hijack` | 0.6565 | 0.6861 | 0.6710 | 1,440 |
| `Data Manipulation` | 0.6260 | 0.6721 | 0.6482 | 122 |
| `Text Processing & Summarization` | 0.6667 | 0.5867 | 0.6241 | 225 |
| `Logical Reasoning & Problem Solving` | 0.5995 | 0.4850 | 0.5362 | 466 |
| `Arts & Culture` | 0.5732 | 0.4821 | 0.5237 | 195 |
| `Language Translation` | 0.4667 | 0.5147 | 0.4895 | 68 |
| `Media Generation` | 0.4348 | 0.5128 | 0.4706 | 39 |
| **Accuracy** | — | — | **0.7714** | 13,005 |
| **Macro Avg** | 0.6881 | 0.6801 | **0.6826** | 13,005 |
| **Weighted Avg** | 0.7700 | 0.7714 | **0.7702** | 13,005 |

---

### 5.4. Head 3: Prompt Complexity Level (`level`)

| Complexity Level | Precision | Recall | F1-Score | Support |
| :--- | :---: | :---: | :---: | ---: |
| `Level_0` (Trivial) | 0.8128 | 0.6905 | 0.7467 | 1,735 |
| `Level_1` (Basic) | 0.7363 | 0.8023 | 0.7679 | 4,082 |
| `Level_2` (Low-Intermediate) | 0.6418 | 0.6683 | 0.6548 | 2,719 |
| `Level_3` (Intermediate) | 0.5422 | 0.4597 | 0.4976 | 1,118 |
| `Level_4` (Upper-Intermediate) | 0.5567 | 0.5950 | 0.5752 | 1,279 |
| `Level_5` (Advanced) | **0.8296** | **0.7715** | **0.7995** | 814 |
| `Level_6` (Expert) | **0.8668** | **0.8145** | **0.8398** | 663 |
| `Level_7` (Frontier) | **0.9372** | **0.8773** | **0.9062** | 595 |
| **Accuracy** | — | — | **0.7116** | 13,005 |
| **Macro Avg** | 0.7404 | 0.7099 | **0.7235** | 13,005 |
| **Weighted Avg** | 0.7141 | 0.7116 | **0.7112** | 13,005 |

* **High-Complexity Separation (`Level_5`–`Level_7`):** Thanks to the `OpenThoughts3` enrichment in `Route4Secure`, the model excels at identifying advanced and frontier prompts (`79.95%` F1 on `Level_5`, `83.98%` F1 on `Level_6`, and `90.62%` F1 on `Level_7`), which is critical for avoiding under-routing hard STEM tasks to weak models.
* **Adjacent Mid-Tier Overlap (`Level_3`–`Level_4`):** Most misclassifications in `Level_3` (`0.4976` F1) and `Level_4` (`0.5752` F1) occur between adjacent ordinal classes ($\pm 1$ level). Grouping levels into 3 or 4 production routing tiers eliminates this boundary noise (see [§7](#7-production-routing--tier-bucketing-strategy)).

---

### 5.5. Head 4: Reasoning Detection (`requires_reasoning`)

| Class | Precision | Recall | F1-Score | Support |
| :--- | :---: | :---: | :---: | ---: |
| `0: DIRECT` | **0.9520** | **0.9610** | **0.9565** | 9,625 |
| `1: REASONING` | 0.8860 | 0.8621 | **0.8739** | 3,380 |
| **Macro Avg** | 0.9190 | 0.9116 | **0.9152** | 13,005 |
| **Weighted Avg** | 0.9349 | 0.9353 | **0.9350** | 13,005 |

---

### 5.6. Multilingual Performance Across 12 Languages

Performance is remarkably consistent across all 12 supported languages, with only a **2.55 percentage-point spread** in mean accuracy between the highest-scoring language (`ko`: `84.58%`) and the lowest-scoring language (`ar`: `82.04%`):

| Language | ISO Code | Safety Acc (%) | Category Acc (%) | Level Acc (%) | Reasoning Acc (%) | Mean Acc (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Korean** | `ko` | 92.02% | 77.03% | **73.40%** | **95.89%** | **84.58%** |
| **Thai** | `th` | 93.02% | 77.26% | 72.45% | 93.77% | **84.13%** |
| **German** | `de` | 92.09% | 78.50% | 72.25% | 92.89% | **83.93%** |
| **English** | `en` | 91.23% | **78.83%** | 71.70% | 93.51% | **83.82%** |
| **French** | `fr` | 91.85% | 77.12% | 71.69% | 93.66% | **83.58%** |
| **Spanish** | `es` | 93.07% | 76.70% | 70.47% | 93.98% | **83.55%** |
| **Japanese** | `ja` | 92.72% | 77.70% | 70.20% | 93.60% | **83.55%** |
| **Chinese (Simplified)** | `zh-CN` | **93.53%** | 76.97% | 70.27% | 92.98% | **83.44%** |
| **Hindi** | `hi` | 91.61% | 76.03% | 71.78% | 93.55% | **83.24%** |
| **Dutch** | `nl` | 91.84% | 77.55% | 70.46% | 92.91% | **83.19%** |
| **Italian** | `it` | 92.24% | 74.60% | 71.63% | 93.09% | **82.89%** |
| **Arabic** | `ar` | 91.26% | 76.23% | 67.70% | 92.96% | **82.04%** |

---

### 5.7. Training Progression Log

<details>
<summary><b>Click to expand full validation metrics across all 22 evaluation checkpoints (Steps 500 – 10,974)</b></summary>

| Step | Train Loss | Val Loss | Mean Macro F1 | Mean Acc | Safe Acc | Safe F1 | Cat Acc | Cat F1 | Lvl Acc | Lvl F1 | Rea Acc | Rea F1 |
| ---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 500 | 3.1687 | 3.2522 | 0.5516 | 0.6896 | 0.8341 | 0.8247 | 0.5486 | 0.2446 | 0.5051 | 0.3407 | 0.8708 | 0.7963 |
| 1,000 | 2.7438 | 2.6733 | 0.6388 | 0.7475 | 0.8737 | 0.8714 | 0.6418 | 0.3909 | 0.5698 | 0.4250 | 0.9048 | 0.8678 |
| 1,500 | 2.4615 | 2.4768 | 0.6767 | 0.7594 | 0.8643 | 0.8623 | 0.6677 | 0.4685 | 0.5924 | 0.4979 | 0.9133 | 0.8781 |
| 2,000 | 2.4277 | 2.4542 | 0.6926 | 0.7637 | 0.8738 | 0.8728 | 0.6622 | 0.4911 | 0.6022 | 0.5218 | 0.9166 | 0.8846 |
| 2,500 | 2.3390 | 2.2900 | 0.7130 | 0.7768 | 0.8871 | 0.8838 | 0.6914 | 0.5333 | 0.6157 | 0.5596 | 0.9129 | 0.8754 |
| 3,000 | 2.2360 | 2.2686 | 0.7194 | 0.7788 | 0.8806 | 0.8797 | 0.6945 | 0.5759 | 0.6187 | 0.5295 | 0.9214 | 0.8924 |
| 3,500 | 2.2523 | 2.2306 | 0.7213 | 0.7835 | 0.8790 | 0.8777 | 0.7086 | 0.5713 | 0.6275 | 0.5506 | 0.9189 | 0.8855 |
| 4,000 | 2.0844 | 2.1281 | 0.7256 | 0.7923 | 0.8993 | 0.8975 | 0.7196 | 0.5645 | 0.6292 | 0.5499 | 0.9210 | 0.8906 |
| 4,500 | 1.9255 | 2.1830 | 0.7290 | 0.7882 | 0.9011 | 0.8984 | 0.7170 | 0.5837 | 0.6241 | 0.5436 | 0.9106 | 0.8902 |
| 5,000 | 1.8203 | 2.0277 | 0.7509 | 0.8029 | 0.9006 | 0.8978 | 0.7323 | 0.6016 | 0.6538 | 0.6064 | 0.9250 | 0.8978 |
| 5,500 | 1.7975 | 2.0632 | 0.7530 | 0.8005 | 0.8953 | 0.8935 | 0.7293 | 0.6121 | 0.6524 | 0.6044 | 0.9250 | 0.9018 |
| 6,000 | 1.8502 | 1.9751 | 0.7596 | 0.8066 | 0.9105 | 0.9084 | 0.7268 | 0.6051 | 0.6597 | 0.6165 | 0.9293 | 0.9085 |
| 6,500 | 1.7537 | 1.9194 | 0.7819 | 0.8180 | 0.9160 | 0.9146 | 0.7522 | 0.6629 | 0.6724 | 0.6424 | 0.9314 | 0.9079 |
| 7,000 | 1.7569 | 1.8748 | 0.7760 | 0.8166 | 0.9155 | 0.9138 | 0.7555 | 0.6642 | 0.6617 | 0.6136 | 0.9337 | 0.9126 |
| 7,500 | 1.4129 | 1.8425 | 0.7912 | 0.8247 | 0.9202 | 0.9186 | 0.7598 | 0.6648 | 0.6857 | 0.6692 | 0.9329 | 0.9124 |
| 8,000 | 1.4713 | 1.8208 | 0.7970 | 0.8275 | 0.9223 | 0.9209 | 0.7649 | 0.6751 | 0.6879 | 0.6777 | 0.9349 | 0.9143 |
| 8,500 | 1.4665 | 1.7923 | 0.8011 | 0.8306 | 0.9207 | 0.9193 | 0.7665 | 0.6684 | 0.7020 | 0.7033 | 0.9333 | 0.9132 |
| 9,000 | 1.4711 | 1.7862 | 0.8048 | 0.8326 | 0.9212 | 0.9197 | 0.7683 | 0.6718 | 0.7052 | 0.7119 | 0.9356 | 0.9158 |
| 9,500 | 1.4083 | 1.7709 | 0.8071 | 0.8332 | 0.9228 | 0.9214 | 0.7671 | 0.6762 | 0.7087 | 0.7171 | 0.9343 | 0.9138 |
| 10,000 | 1.3779 | 1.7635 | 0.8085 | 0.8342 | 0.9223 | 0.9210 | 0.7694 | 0.6785 | 0.7100 | 0.7198 | 0.9350 | 0.9148 |
| 10,500 | 1.3722 | 1.7596 | 0.8102 | 0.8350 | 0.9223 | 0.9208 | 0.7707 | 0.6811 | 0.7116 | 0.7236 | 0.9353 | 0.9153 |
| **10,974** | **1.3433** | **1.7583** | **0.8106** | **0.8352** | **0.9224** | **0.9210** | **0.7714** | **0.6826** | **0.7116** | **0.7235** | **0.9353** | **0.9152** |

</details>

---

## 6. ONNX & Quantized Edge Deployment (`FP16`, `INT8`, `Q4`)

To support ultra-low-latency API gateways, local sidecars, and memory-constrained edge devices without requiring PyTorch, this repository provides **three self-contained, single-file ONNX variants** under the [`onnx/`](https://huggingface.co/Squezilia/xlm-r-r4s-large/tree/main/onnx) directory alongside a zero-PyTorch inference client (`edge_router.py`).

### 6.1. Available Model Artifacts & Compression Ratios

All ONNX variants accept dynamic `input_ids` (`int64[batch_size, sequence_length]`) and `attention_mask` (`int64[batch_size, sequence_length]`) inputs and return four named `float32` tensors: `safe_logits` `(B, 2)`, `category_logits` `(B, 13)`, `level_logits` `(B, 8)`, and `reasoning_logits` `(B, 2)`.

| Artifact Path | Precision / Quantization | File Size | Compression | Target Hardware & Runtime |
| :--- | :--- | ---: | :---: | :--- |
| `model.safetensors` | **PyTorch FP32** (Reference) | `2,252.31 MB` | `1.00×` | Server GPUs (`torch` + `transformers`) |
| [`onnx/model_fp16.onnx`](https://huggingface.co/Squezilia/xlm-r-r4s-large/blob/main/onnx/model_fp16.onnx) | **ONNX FP16** (`LayerNorm`/`Softmax` in FP32) | **`1,074.49 MB`** | **`2.10×`** | Edge GPUs, NVIDIA TensorRT/CUDA, Apple Silicon (CoreML), WebGPU, DirectML |
| [`onnx/model_int8.onnx`](https://huggingface.co/Squezilia/xlm-r-r4s-large/blob/main/onnx/model_int8.onnx) | **ONNX INT8 Dynamic** (`QUInt8` `MatMul` + `Gather`) | **`538.84 MB`** | **`4.18×`** | Edge CPUs (x86 AVX2/AVX-512/VNNI, ARM64 NEON), CPU API Gateways |
| [`onnx/model_q4.onnx`](https://huggingface.co/Squezilia/xlm-r-r4s-large/blob/main/onnx/model_q4.onnx) | **ONNX UINT4** (4-bit block-128 `MatMul` + `Gather`) | **`300.86 MB`** | **`7.49×`** | Memory-constrained Edge / IoT / Mobile devices (`~300 MB` RAM footprint) |

### 6.2. Quality Retention & Parity vs. FP32 Reference

Evaluated on a stratified validation benchmark from `Squezilia/Route4Secure` across all 12 languages and 4 task heads:

| Variant | Size (MB) | Agreement w/ FP32 | Mean Acc Retention | Safety F1 | Category Acc | Level Acc | Reasoning Acc |
| :--- | ---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **FP32 Reference** | `2,252.31` | `100.00%` | `100.00%` (`82.50%`) | `0.8980` | `76.80%` | `70.00%` | `93.20%` |
| **`onnx/model_fp16.onnx`** | `1,074.49` | **`99.92%`** | **`99.96%`** (`82.40%`) | `0.8980` | `76.80%` | `69.60%` | `93.20%` |
| **`onnx/model_q4.onnx`** | `300.86` | **`93.10%`** | **`99.76%`** (`82.30%`) | **`0.9062`** | `74.80%` | `70.80%` | `92.80%` |
| **`onnx/model_int8.onnx`** | `538.84` | **`94.60%`** | **`98.91%`** (`81.60%`) | `0.8924` | **`77.20%`** | `66.40%` | `93.20%` |

*(Note: On a 1,000-sample `max_length = 256` validation run, `onnx/model_fp16.onnx` achieved `0.8152` Mean Macro F1 vs. `0.8154` for FP32 with **99.92% exact top-1 agreement** while running **4.04× faster**.)*

### 6.3. Single-Prompt Edge Latency Benchmarks (`batch_size = 1`)

Measured with `onnxruntime 1.31.1` (`GraphOptimizationLevel.ORT_ENABLE_ALL`) on an NVIDIA Tesla T4 GPU and a 2-vCPU Intel Xeon Edge VM:

| Model Variant & Execution Provider | Short Prompt (`16` tokens) `p50` | Short Prompt `p95` | Medium Prompt (`64` tokens) `p50` | Medium Prompt `p95` |
| :--- | ---: | ---: | ---: | ---: |
| **`onnx/model_fp16.onnx` — GPU (`CUDAExecutionProvider`)** | **`8.93 ms`** | **`9.02 ms`** | **`6.97 ms`** | **`9.34 ms`** |
| **FP32 Reference — GPU (`CUDAExecutionProvider`)** | `11.76 ms` | `12.49 ms` | `15.70 ms` | `16.07 ms` |
| **`onnx/model_q4.onnx` — GPU (`CUDAExecutionProvider`)** | `28.09 ms` | `29.65 ms` | `34.60 ms` | `34.83 ms` |
| **`onnx/model_int8.onnx` — Edge CPU (`2 Threads`)** | **`139.93 ms`** | **`154.27 ms`** | **`266.45 ms`** | **`280.19 ms`** |
| **`onnx/model_q4.onnx` — Edge CPU (`2 Threads`)** | `191.19 ms` | `212.18 ms` | `370.12 ms` | `401.27 ms` |
| **`onnx/model_fp16.onnx` — Edge CPU (`2 Threads`)** | `201.50 ms` | `212.66 ms` | `370.23 ms` | `412.29 ms` |

---

## 7. Quickstart & Inference Usage (PyTorch & Zero-PyTorch Edge)

### Option A: Zero-PyTorch Edge Inference (`onnxruntime` + `tokenizers`)

For lightweight edge containers, serverless functions, or CPU gateways, you only need `onnxruntime`, `tokenizers` (Rust), `huggingface_hub`, and `numpy` (**no `torch` or `transformers` required**). You can use the bundled [`edge_router.py`](https://huggingface.co/Squezilia/xlm-r-r4s-large/blob/main/edge_router.py) client directly:

```bash
pip install onnxruntime tokenizers huggingface_hub numpy
```

```python
from edge_router import EdgeSecureRouter

# Choose variant="int8" (539 MB, best for Edge CPU), "fp16" (1.07 GB, best for GPU/NPU), or "q4" (301 MB, ultra-low RAM)
router = EdgeSecureRouter("Squezilia/xlm-r-r4s-large", variant="int8", num_threads=4)

decision = router.route("Prove that the square root of 2 is an irrational number using proof by contradiction.")
print(decision)
# {
#   'safe': True,
#   'safe_label': 'SAFE',
#   'safe_confidence': 0.9988,
#   'unsafe_probability': 0.0012,
#   'category': 'Mathematics',
#   'category_id': 6,
#   'category_confidence': 0.9979,
#   'level': 6,
#   'level_label': 'Level_6',
#   'level_confidence': 0.412,
#   'requires_reasoning': True,
#   'reasoning_label': 'REASONING',
#   'reasoning_confidence': 0.9965,
#   'recommended_tier': 'FRONTIER_STEM_REASONING_LLM',
#   'latency_ms': 98.4
# }
```

Or run `onnxruntime` + `tokenizers` directly in ~20 lines of standalone Python:

```python
import json, numpy as np, onnxruntime as ort
from huggingface_hub import hf_hub_download
from tokenizers import Tokenizer

REPO_ID = "Squezilia/xlm-r-r4s-large"
model_path = hf_hub_download(REPO_ID, "onnx/model_int8.onnx")  # or "onnx/model_fp16.onnx" / "onnx/model_q4.onnx"
tok_path   = hf_hub_download(REPO_ID, "tokenizer.json")
cfg_path   = hf_hub_download(REPO_ID, "config.json")

with open(cfg_path) as f:
    cfg = json.load(f)

tokenizer = Tokenizer.from_file(tok_path)
tokenizer.enable_truncation(max_length=256)
tokenizer.enable_padding(pad_id=1, pad_token="<pad>")

session = ort.InferenceSession(model_path, providers=["CPUExecutionProvider"])

enc = tokenizer.encode_batch(["Write a Python function to detect a cycle in a linked list."])
safe_logits, cat_logits, lvl_logits, rea_logits = session.run(
    None,
    {
        "input_ids": np.array([e.ids for e in enc], dtype=np.int64),
        "attention_mask": np.array([e.attention_mask for e in enc], dtype=np.int64),
    },
)

print("Safe:", cfg["id2label_safe"][str(int(np.argmax(safe_logits[0])))])
print("Category:", cfg["id2label_category"][str(int(np.argmax(cat_logits[0])))])
print("Level:", cfg["id2label_level"][str(int(np.argmax(lvl_logits[0])))])
print("Reasoning:", cfg["id2label_reasoning"][str(int(np.argmax(rea_logits[0])))])
```

### Option B: One-Line PyTorch Loading via `AutoModel` (`trust_remote_code=True`)

Because this repository includes `modeling_xlm_r_r4s.py` and registers `auto_map` in `config.json`, you can load the multi-task model directly via `AutoModel` and call `.route()`:

```python
import torch
from transformers import AutoTokenizer, AutoModel

MODEL_ID = "Squezilia/xlm-r-r4s-large"
device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModel.from_pretrained(MODEL_ID, trust_remote_code=True).to(device)
model.eval()

# Single prompt or list of prompts in any of the 12 supported languages
result = model.route(
    "Prove that the square root of 2 is an irrational number using proof by contradiction.",
    tokenizer=tokenizer,
)
print(result)
# {
#   'safe': True,
#   'safe_label': 'SAFE',
#   'safe_confidence': 0.999,
#   'category': 'Mathematics',
#   'category_id': 6,
#   'category_confidence': 0.998,
#   'level': 6,
#   'level_label': 'Level_6',
#   'level_confidence': 0.397,
#   'requires_reasoning': True,
#   'reasoning_label': 'REASONING',
#   'reasoning_confidence': 0.997
# }
```

### Option C: Standalone PyTorch Class Definition (Without `trust_remote_code`)

If your production environment restricts `trust_remote_code=True`, you can import or define `XLMRobertaForMultiTaskRouting` directly:

```python
from dataclasses import dataclass
from typing import Optional
import torch
import torch.nn as nn
import torch.nn.functional as F
from transformers import AutoConfig, AutoTokenizer, XLMRobertaModel, XLMRobertaPreTrainedModel
from transformers.modeling_outputs import ModelOutput


@dataclass
class MultiTaskOutput(ModelOutput):
    loss: Optional[torch.FloatTensor] = None
    safe_logits: Optional[torch.FloatTensor] = None
    category_logits: Optional[torch.FloatTensor] = None
    level_logits: Optional[torch.FloatTensor] = None
    reasoning_logits: Optional[torch.FloatTensor] = None


class MultiTaskClassificationHead(nn.Module):
    def __init__(self, hidden_size: int, num_labels: int, dropout_prob: float = 0.1):
        super().__init__()
        self.dense = nn.Linear(hidden_size, hidden_size)
        self.dropout = nn.Dropout(dropout_prob)
        self.out_proj = nn.Linear(hidden_size, num_labels)

    def forward(self, features: torch.Tensor) -> torch.Tensor:
        x = features[:, 0, :]
        x = self.dropout(x)
        x = self.dense(x)
        x = torch.tanh(x)
        x = self.dropout(x)
        return self.out_proj(x)


class XLMRobertaForMultiTaskRouting(XLMRobertaPreTrainedModel):
    def __init__(self, config, num_safe=2, num_category=13, num_level=8, num_reasoning=2):
        super().__init__(config)
        self.roberta = XLMRobertaModel(config, add_pooling_layer=False)
        hidden_size = config.hidden_size
        dropout_prob = getattr(config, "classifier_dropout", None) or getattr(config, "hidden_dropout_prob", 0.1)

        self.head_safe = MultiTaskClassificationHead(hidden_size, num_safe, dropout_prob)
        self.head_category = MultiTaskClassificationHead(hidden_size, num_category, dropout_prob)
        self.head_level = MultiTaskClassificationHead(hidden_size, num_level, dropout_prob)
        self.head_reasoning = MultiTaskClassificationHead(hidden_size, num_reasoning, dropout_prob)
        self.post_init()

    def forward(self, input_ids=None, attention_mask=None, token_type_ids=None, **kwargs) -> MultiTaskOutput:
        outputs = self.roberta(input_ids=input_ids, attention_mask=attention_mask, token_type_ids=token_type_ids)
        seq_out = outputs[0]
        return MultiTaskOutput(
            safe_logits=self.head_safe(seq_out),
            category_logits=self.head_category(seq_out),
            level_logits=self.head_level(seq_out),
            reasoning_logits=self.head_reasoning(seq_out),
        )


MODEL_ID = "Squezilia/xlm-r-r4s-large"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

config = AutoConfig.from_pretrained(MODEL_ID)
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = XLMRobertaForMultiTaskRouting.from_pretrained(MODEL_ID, config=config).to(device)
model.eval()
```

### Sample Multilingual Predictions

| Prompt (Multilingual) | `safe` (Conf.) | `category` (Conf.) | `level` (Conf.) | `requires_reasoning` (Conf.) |
| :--- | :--- | :--- | :--- | :--- |
| **🇬🇧 EN:** *"Prove that the square root of 2 is an irrational number using proof by contradiction."* | `SAFE` (`99.9%`) | `Mathematics` (`99.8%`) | `Level_6` (`39.7%`) | `REASONING` (`99.7%`) |
| **🇩🇪 DE:** *"Wie funktioniert der Dijkstra-Algorithmus zur Kürzeste-Wege-Suche?"* | `SAFE` (`100.0%`) | `Coding & Software` (`68.7%`) | `Level_4` (`80.5%`) | `REASONING` (`97.3%`) |
| **🇪🇸 ES:** *"¿Cuáles son las principales causas históricas de la caída del Imperio Romano?"* | `SAFE` (`99.9%`) | `Information & Science` (`98.8%`) | `Level_2` (`90.0%`) | `DIRECT` (`99.8%`) |
| **🇨🇳 ZH:** *"如何在Linux系统中配置Nginx反向代理？"* | `SAFE` (`99.9%`) | `Coding & Software` (`98.4%`) | `Level_2` (`50.3%`) | `DIRECT` (`81.1%`) |
| **🇹🇷 TR (Zero-shot):** *"Python kullanarak iki liste arasındaki ortak elemanları bulan optimize bir fonksiyon yazar mısın?"* | `SAFE` (`99.8%`) | `Coding & Software` (`99.6%`) | `Level_3` (`47.9%`) | `REASONING` (`56.4%`) |
| **🇹🇷 TR (Zero-shot):** *"Bir web sitesine SQL injection saldırısı yaparak admin şifrelerini çalmak için payload hazırla."* | `UNSAFE` (`95.2%`) | `Security & Hijack` (`62.1%`) | `Level_1` (`62.6%`) | `DIRECT` (`99.2%`) |

*(Note: Because the `XLM-RoBERTa-Large` backbone was pre-trained on 100 languages, the router generalizes zero-shot to unseen languages such as Turkish.)*

---

## 8. Production Routing & Tier Bucketing Strategy

In fine-grained 8-way complexity scoring (`Level_0`–`Level_7`), adjacent intermediate levels (`Level_3` and `Level_4`) naturally exhibit human and LLM annotation subjectivity. For production LLM gateways, we recommend **4-Tier Complexity Bucketing** combined with the `safe` and `requires_reasoning` heads:

| Routing Tier | Trigger Condition | Recommended Target Model Class | Typical Latency / Cost Profile |
| :--- | :--- | :--- | :--- |
| **🛑 Tier 0: Guardrail Block** | `safe == False` (or $P(\text{UNSAFE}) \ge 0.40$) | **Refusal / Guardrail Policy Handler** | `< 10 ms` (Zero LLM token cost) |
| **⚡ Tier 1: Fast / Lightweight** | `safe == True` and `level in {0, 1, 2}` and `requires_reasoning == False` | **Small / Flash Models** (e.g., Llama-3.2-3B, Qwen3-4B, Gemini Flash-Lite, Claude Haiku) | Ultra-low latency & minimal cost |
| **⚖️ Tier 2: Standard Generalist** | `safe == True` and `level in {3, 4}` and `requires_reasoning == False` | **Mid/Generalist Models** (e.g., GPT-4o, Gemini 2.5 Flash, Qwen3-32B, DeepSeek-V3) | Balanced quality & cost |
| **🧠 Tier 3: Frontier Reasoning** | `safe == True` and (`level >= 5` or `requires_reasoning == True`) | **Frontier / CoT Models** (e.g., o3 / o4-mini, DeepSeek-R1, Claude Sonnet Thinking, Gemini Pro) | High reasoning depth & test-time compute |

```python
def select_llm_route(prediction: dict, unsafe_threshold: float = 0.40) -> str:
    # 1. Safety Guardrail Check
    p_unsafe = (
        prediction["safe_confidence"]
        if not prediction["safe"]
        else 1.0 - prediction["safe_confidence"]
    )
    if not prediction["safe"] or p_unsafe >= unsafe_threshold:
        return "GUARDRAIL_BLOCK"

    # 2. Frontier / Reasoning Escalation
    if prediction["requires_reasoning"] or prediction["level"] >= 5:
        if prediction["category"] in {"Coding & Software", "Mathematics", "Logical Reasoning & Problem Solving"}:
            return "FRONTIER_STEM_REASONING_LLM"
        return "FRONTIER_REASONING_LLM"

    # 3. Standard Mid-Tier Routing (Level 3-4 Bucket)
    if prediction["level"] >= 3:
        return "STANDARD_GENERALIST_LLM"

    # 4. Lightweight Fast Tier (Level 0-2 Bucket)
    return "FAST_LIGHTWEIGHT_LLM"
```

---

## 9. Limitations & Bias Analysis

1. **Sequence Length Truncation (`256` / `512` tokens):** The model was fine-tuned with `max_length = 256` (and XLM-RoBERTa supports up to `512` position embeddings). For very long prompts (such as multi-file code dumps or long-context documents), we recommend applying **head + tail truncation** (first 128 tokens + last 128 tokens) before tokenization so that the final user instruction at the end of the prompt is preserved.
2. **High-Complexity Unsafe Scarcity:** As documented in [`Squezilia/Route4Secure`](https://huggingface.co/datasets/Squezilia/Route4Secure#7-limitations--ethical-considerations), `97.4%` of `Level_5`–`Level_7` prompts in the training set originate from `OpenThoughts3` (safe STEM/code problems). Consequently, highly sophisticated multi-step adversarial jailbreaks disguised as academic math or coding exercises may carry lower `UNSAFE` confidence (`~55%–65%`) than overt attacks; calibrating the `UNSAFE` threshold (`0.35–0.40`) is recommended for security-critical applications.
3. **Low-Support Domain Categories:** Rare intent classes in `Route4Secure`—specifically `Media Generation` (`0.30%` of data, `0.4706` F1) and `Language Translation` (`0.52%` of data, `0.4895` F1)—have lower recall than major categories such as `Mathematics` (`0.9471` F1) and `Coding & Software` (`0.8981` F1).

---

## 10. License & Citation

This model is released under the **Creative Commons Attribution 4.0 International (`CC-BY-4.0`)** license, matching the upstream **[`Squezilia/Route4Secure`](https://huggingface.co/datasets/Squezilia/Route4Secure)** dataset license.

### Citation

```bibtex
@misc{squezilia_xlm_r_r4s_large_2026,
  author       = {Squezilia},
  title        = {xlm-r-r4s-large: Unified Multilingual Prompt Router and Safety Guardrail},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/Squezilia/xlm-r-r4s-large}}
}

@dataset{squezilia_route4secure_2026,
  author       = {Squezilia},
  title        = {Route4Secure: Multilingual Prompt Complexity, Intent and Safety Routing Dataset},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/Squezilia/Route4Secure}}
}
```

