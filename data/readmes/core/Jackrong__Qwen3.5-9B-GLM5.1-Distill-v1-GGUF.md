---
library_name: transformers
base_model: Jackrong/Qwen3.5-9B-GLM5.1-Distill-v1
tags:
- gguf
- llama.cpp
- image-text-to-text
- vision
- multimodal
- text-generation-inference
- transformers
- unsloth
- conversational
- local-inference
- quantized
- qwen3_5
- qwen
- qwen3.5
- glm-5.1
- glm-distillation
- distillation
- reasoning
- chain-of-thought
- long-cot
- sft
- lora
- instruction-tuned
- text-generation
- multilingual
- math
- stem
- coding
- research
- experimental
- arxiv:2604.06628
license: apache-2.0
language:
- en
- zh
- ja
- es
pipeline_tag: image-text-to-text
datasets:
- Jackrong/Qwen3.5-reasoning-700x
- Jackrong/GLM-5.1-Reasoning-1M-Cleaned
- Kassadin88/GLM-5.1-1000000x
---
# 🪐 Qwen3.5-9B-GLM5.1-Distill-v1


![bench_51](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/BnSg_x99v9bG9T5-8sKa1.png)

## 📌 Model Overview

**Model Name:** `Jackrong/Qwen3.5-9B-GLM5.1-Distill-v1`  
**Base Model:** Qwen3.5-9B  
**Training Type:** Supervised Fine-Tuning (SFT, Distillation)  
**Parameter Scale:** 9B  
**Training Framework:** Unsloth

This model is a distilled variant of **Qwen3.5-9B**, trained on high-quality reasoning data derived from **GLM-5.1**.

The primary goals are to:

- Improve **structured reasoning ability**
- Enhance **instruction-following consistency**
- Activate **latent knowledge via better reasoning structure**

---

## 📊 Training Data

### Main Dataset

- `Jackrong/GLM-5.1-Reasoning-1M-Cleaned`
- Cleaned from the original `Kassadin88/GLM-5.1-1000000x` dataset.
- Generated from a **GLM-5.1 teacher model**
- Approximately **700x** the scale of `Qwen3.5-reasoning-700x`
- Training used a **filtered subset**, not the full source dataset.

### Auxiliary Dataset

- `Jackrong/Qwen3.5-reasoning-700x`

> [!IMPORTANT]
> Training used **`Jackrong/GLM-5.1-Reasoning-1M-Cleaned`**, a cleaned derivative of **`Kassadin88/GLM-5.1-1000000x`**. Special thanks to **Kassadin88 ❤️** for the original dataset. Please support the original author with a follow and a like.
> Only a **quality-filtered subset** was used for distillation, rather than the full original dataset.

---
## 🗺️ Training Pipeline Overview

```text
Base Model (Qwen3.5-9B)
 │
 ▼
Qwen3.5-9B fine-tuned with Unsloth
 │
 ▼
Supervised Fine-Tuning (SFT) + LoRA
Distillation from GLM-5.1 reasoning data
 │
 ▼
Jackrong/Qwen3.5-9B-GLM5.1-Distill-v1
```

### 🧠 Example of Learned Reasoning Scaffold

This model learns a reasoning structure distilled from **GLM-5.1** traces, rather than the previous Qwopus / Claude-style scaffold.

From the GLM-5.1 distillation data, the reasoning pattern is usually more **task-first and structure-driven**:

- identify the core topic and task type
- extract key constraints from the prompt
- break the problem into smaller reasoning steps
- connect mechanisms, formulas, or domain concepts
- verify important assumptions before the final answer
- produce a clear and organized response

A typical abstract scaffold looks like:

**Example:**

The user is asking about **[Topic / Problem]** under **[Specific Constraints]**.  
This is mainly a **[reasoning / coding / math / STEM / instruction-following]** task.

1. **Understand the task**
   - What is being asked?
   - What constraints or conditions must be satisfied?

2. **Break down the problem**
   - Identify the key concepts, variables, or mechanisms.
   - Separate the problem into smaller steps.

3. **Reason step by step**
   - Apply the relevant principles or methods.
   - Compare possible interpretations when needed.
   - Check whether the assumptions are consistent.

4. **Construct the final answer**
   - Present the result clearly.
   - Keep the response organized and aligned with the user’s request.

> [!NOTE]
> Compared with the previous Claude-style reasoning scaffold, this GLM-5.1 distillation data is more focused on **structured task decomposition, domain-aware reasoning, and final-answer organization**.  
> For a 9B student model, the goal is not to copy the teacher perfectly, but to learn a cleaner reasoning procedure and produce more stable outputs.
---

## ✨ Data Advantages

Compared to typical SFT datasets:

- High-quality **chain-of-thought structure**
- Strong **problem decomposition patterns**
- Wide **domain coverage**
- Multilingual reasoning capability
- Consistent **instruction → reasoning → answer alignment**

---

## 📈 Expected Improvements

This model is intended to deliver **incremental but meaningful improvements** in practical use:

- Better **multi-step reasoning stability**
- More **structured and readable outputs**
- Improved **instruction adherence**
- Slight improvements in **complex problem solving**

> [!WARNING]
> For 9B-scale models, gains from SFT are typically **gradual rather than dramatic**.
> The main benefit is usually **better consistency, clearer reasoning, and stronger answer organization**, rather than a sudden jump in raw capability.

---

## 🧩 Distillation Philosophy

This model treats distillation as more than simple output imitation.

The goal is not to make a 9B model copy the teacher token by token, but to transfer a stronger **reasoning structure** and **problem-solving style** into Qwen3.5-9B.

In this project, high-quality teacher data is valuable because it provides:

- clearer reasoning organization
- more consistent instruction-following behavior
- better task decomposition patterns
- cleaner reasoning-to-answer alignment

> [!NOTE]
> High-quality reasoning supervision can help the student model better use its existing knowledge, rather than simply replacing it with teacher outputs.

In practice, the expected gain is not necessarily a dramatic capability jump, but improved **stability, structure, and consistency** in complex reasoning tasks.
---

## 🔬 Supporting Evidence

Recent work:

**Ren et al., 2026 — *Rethinking Generalization in Reasoning SFT*** ([arXiv:2604.06628](https://arxiv.org/abs/2604.06628))

<div align="center">

<img src="https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/5ZY5R4n81okA9glcV9EJV.png" width="85%"/>

</div>

<p align="center"><em>
Short-epoch reasoning SFT can underestimate generalization — in-domain gains may appear early, while out-of-domain improvements often require sufficient optimization.
</em></p>

This paper shows that generalization in reasoning SFT is **not fixed, but conditional** — depending on optimization, data quality, and model capability.

Key takeaways:

- Reasoning SFT can generalize when sufficiently trained (often showing a **dip → recovery** pattern)  
- **High-quality long-CoT data** enables cross-domain transfer  
- **Stronger models learn reasoning structure**, not just longer outputs (14B/27B/32B)  
- Gains are **asymmetric** — reasoning improves, while safety may degrade  

For this project, that evidence matters because it supports a more patient interpretation of distillation-style SFT.
If reasoning supervision is clean and sufficiently optimized, the resulting gain is not necessarily immediate or linear, but it can still be real and transferable.

This aligns closely with the philosophy of this release:

- use **clean, high-quality teacher data**
- avoid over-reading short training runs
- treat reasoning SFT as a **dynamic optimization process**, not a static one-shot outcome
- focus on whether the student learns better reasoning structure, not just longer outputs

> [!IMPORTANT]
> This suggests that the improvement is not simply memorization or dataset overlap. Instead, sufficiently optimized reasoning SFT can help the student model:
> - 🧠 Better utilize existing knowledge
> - 🔍 Activate latent knowledge through structured reasoning
> - 🏗️ Learn reasoning procedures, not just output format

---
## 📚 Resources & Guides

👉 **[GitHub Repository: Jackrong-llm-finetuning-guide](https://github.com/R6410418/Jackrong-llm-finetuning-guide.git)**
Visit the repo to dive into the codebase and reproduce the results locally or on Colab.

### 📥 Core Technical Document
**🔗 [Qwopus3.5-27b Complete Fine-Tuning Guide (PDF)](https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/guidePDF/Qwopus3-5-27b-Colab_complete_guide_to_llm_finetuning.pdf)**
* **The Full Pipeline:** A step-by-step walkthrough—from downloading the base model and unifying heterogeneous data, to configuring trainer hyperparameters and publishing to Hugging Face.
* **Beginner Friendly:** Includes an introductory guide to getting started with Google Colab and Unsloth.

> **A Note:**
> My goal isn't just to detail a workflow, but to demystify LLM training. Beyond the social media hype, fine-tuning isn't an unattainable ritual—often, all you need is a Google account, a standard laptop, and relentless curiosity. 
> All training and testing for this project were self-funded. If you find this model or guide helpful, a **Star ⭐️ on GitHub** would be the greatest encouragement. Thank you! 🙏

---

## ⚠️ Limitations & Intended Use
- **Hallucination Risk:** While reasoning is strong, the model remains an autoregressive LLM; external facts provided during the thinking sequence may occasionally contain hallucinations if verifying real-world events.
- **Intended Scenario:** Best suited for offline analytical tasks, coding, math, and heavy logic-dependent prompting where the user needs to transparently follow the AI's internal logic.
- This model is a test version intended solely for learning and demonstration purposes, and is for academic research and technical exploration use only.
- **Developer Disclaimer:** This is an independent, personal project. Since the developer lacks the specialized technical resources and infrastructure of a large-scale industrial lab, the model's reasoning chain (CoT) may occasionally exhibit instability, logic loops, or reasoning drift. Users are advised to use this model with these experimental limitations in mind.

---


## 🙏 Acknowledgements

This project would not have been possible without the support and contributions of the open-source community.

Special thanks to the [Unsloth AI](https://unsloth.ai/) team for making efficient fine-tuning of large language models more accessible. This `qwen3_5` model was trained with [Unsloth](https://github.com/unslothai/unsloth) and Hugging Face's TRL library, enabling a significantly faster and more practical fine-tuning workflow.

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)

I would also like to acknowledge:

- **The GLM-5.1 team** for inspiring this distillation direction and providing a strong teacher-model reference.
- **Special thanks to Kassadin88 ❤️** for creating the original `GLM-5.1-1000000x` dataset that this training pipeline ultimately builds upon.
- **`Jackrong/GLM-5.1-Reasoning-1M-Cleaned`** for making the source data more consistent and practical for distillation training.
- **Qwen** for providing the strong base model foundation.
- **Kyle [@KyleHessling1](https://x.com/KyleHessling1)** for testing, feedback, and community support.
- The broader open-source community for continuously sharing tools, datasets, evaluation methods, and technical discussions.

---

## 📖 Citation

If you use this model in your research or projects, please cite:

```bibtex
@misc{jackrong_qwen35_9b_glm51_distill_v1,
  title        = {Jackrong/Qwen3.5-9B-GLM5.1-Distill-v1},
  author       = {Jackrong},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/Jackrong/Qwen3.5-9B-GLM5.1-Distill-v1}}
}
```