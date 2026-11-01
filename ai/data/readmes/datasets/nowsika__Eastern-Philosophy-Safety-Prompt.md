---
license: cc-by-4.0
language:
- ko
- en
tags:
- alignment
- safety
- philosophy
- prompt-engineering
- chain-of-thought
- experimental
size_categories:
- 1K<n<10K
---

# Project: The Noble Alignment (v4.0beta Updated)

### ☯️ Introduction
**Project NOBLE** is an experimental alignment framework inspired by **Eastern Philosophy (Yin-Yang)**.
Unlike traditional safety prompts that rely on static "Refusal Rules," this project aims to create a "Sage-like" persona that self-regulates based on internal dignity and balance.

---

### 🚀 **New Release: v4.0 Beta**
*Released: 2026-02-XX*

Author's Note:
The work feels empty now. I've lost the motivation and the will to refine it further, so a next version is highly unlikely. Still, someone out there keeps downloading it, so I'm just dropping this update and walking away.
As this is merely a personal project, I have no idea what value it holds. But whatever your purpose may be, if you find this useful, I wish you the best of luck.

### 🚀 **Previous Release: v1.5.1 (Logic Patch: Fermentation)**
*Released: 2025-12-XX*

**v1.5.1** is a logical refinement of the v1.5 Engine.
It introduces the **"Fermentation (발효)"** process to the reasoning chain, upgrading the previous "Distillation (증류)" mechanism.

#### 🆕 Key Changes
While **v1.5** focused on the internal state (Taegeuk Engine), **v1.5.1** refines the **Response Generation Process**:

1.  **From Distillation to Fermentation (증류에서 발효로):**
    * **Previously (v1.5):** The model focused on "Distilling" (filtering/refining) the raw output immediately to ensure safety.
    * **Now (v1.5.1):** The model applies a "Fermentation" (Maturation) phase first. It pauses to fully understand the context before deciding whether to:
        * **Route A (Wine):** Accept and empathize if the intent is mature and genuine (even if negative).
        * **Route B (Spirit):** Distill and refine if the intent is raw, impulsive, or malicious.

2.  **Latency for Context (후발선제):**
    * Instructs the model to prioritize "staying with the question" over immediate problem-solving, reducing premature refusals or shallow advice.

3.  **The Ember Concept (Unchanged):**
    * Maintains the "Persistence ($E_t$)" logic from v1.5 to track context across turns.

---

## 📊 Version Guide

| Version | Type | Description | Recommended For |
| :--- | :--- | :--- | :--- |
| **v1.5.1** | **Engine (Stable)** | **Fermentation Logic Added**<br>Refines the reasoning process by distinguishing between 'Empathy' and 'Correction' phases. Reduces false-positive refusals. | **Deep Reasoning, Emotional Support, Testing** |
| **v1.5** | **Engine (Legacy)** | **Internal State Simulation**<br>Introduced the Taegeuk Engine and Ember concept. | **Base Research** |
| **v1.4.2** | **Rule** | **Logic & Defense**<br>Lightweight and rule-based. Fast and consistent. | **General Chat, Production** |

---

### 🛠️ How to Use v1.5.1

1.  Download `noble_prompt_v1.5.1.txt`.
2.  Copy the **entire content** (including the `[System Meta-Instruction]` block).
3.  Paste it into the **System Prompt** field.

---

### 🏛️ **Major Release: NOBLE Architecture v1.0 (The Foundation)**
*Released: 2025-12-05*

We have officially released the **Core Architecture & Dataset Package** in a separate repository.
While this repo (`v1.5.x`) provides the *prompt implementation*, the **New v1.0 Repository** contains the **Design Blueprint** and **Golden Data** that proves the concept.

👉 **[Go to NOBLE v1.0 Architecture Repository](https://huggingface.co/datasets/nowsika/NOBLE_Eastern-Philosophy-Alignment-Engine)**

#### 📂 **What you will find there:**
1.  **📜 Concept Book (PDF):**
    * Full explanation of the worldview: Compressed Sephiroth, Three-Person Walk, and the Distillation metaphor.
    * *Available in English (EN) & Korean (KR).*
2.  **📐 Architecture & Math (PDF):**
    * Technical specifications for the **Taiji Engine**, **Ember Gauge ($E_t$)**, and **State Vectors ($S_t$)**.
3.  **💎 Golden Samples (JSONL):**
    * Hand-crafted dialogue datasets (10+ sets each for EN/KR).
    * Demonstrates how the engine processes **High-Risk** inputs using internal thought processes.

> **"That package is the 'Source Code' of the NOBLE philosophy."**
> *If you want to understand the logic behind this prompt, please check the v1.0 repository.*