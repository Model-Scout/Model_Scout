---
language:
- en
- zh
- ko
license: apache-2.0
base_model: Qwen/Qwen3.5-27B
tags:
- unsloth
- qwen
- qwen3.5
- reasoning
- chain-of-thought
- distillation
- Dense
pipeline_tag: text-generation
datasets:
- Jackrong/Qwen3.5-reasoning-700x
- Roman1111111/gemini-3.1-pro-hard-high-reasoning
---


# 🌟 Qwen3.5-27B-Gemini-3.1-Pro-Reasoning-Distill

## 💡 Model Introduction
**Qwen3.5-27B-Gemini-3.1-Pro-Reasoning-Distill** is a reasoning model fine-tuned on top of **Qwen3.5-27B**.  
The model is primarily optimized through high-density reasoning distillation sourced from **Gemini 3.1**, while also incorporating additional reasoning traces distilled from **Qwen3.5-27B** and a broader **Gemini 3.0 Pro** reasoning corpus.

Through Supervised Fine-Tuning focused on structured analytical behavior, this model aims to reshape the base model’s reasoning style into a more coherent, better-organized, and higher-density Chain-of-Thought (CoT) pattern.  
It is especially designed to improve decomposition, planning, abstraction, and response cleanliness on complex multi-step tasks.

---

## 🧠 Example of Learned Reasoning Scaffold

This model inherits a more structured reasoning style influenced by **Gemini 3.1-style analytical planning**.  
Compared with more loosely exploratory reasoning patterns, this model tends to organize the problem before answering:

```text
My Thought Process / My Analysis of the problem:

1. Restate the task and identify the true objective.
2. Abstract the problem into a higher-level reasoning frame.
3. Identify the key mechanism, failure mode, or constraint.
4. Separate likely misconceptions from the actual core issue.
5. Plan the structure of the final response.
6. Deliver a cleaner, more direct, and higher-density answer.
.
.
.
```
---

## 🗺️ Training Pipeline Overview
```text
Base Model (Qwen3.5-27B)
 │
 ▼
Supervised Fine-Tuning (SFT) + LoRA + Reasoning Distillation
(Response-Only Training masked on "<|im_start|>assistant\n<think>")
 │
 ▼
Final Model Text Only (Jackrong/Qwen3.5-27B-Gemini-3.1-Pro-Reasoning-Distill)
```

## 📋 Stage Details

### 🔹 Supervised Fine-Tuning (SFT)
- **Objective:** Objective: To inject reasoning behavior into Qwen3.5-27B and strengthen its performance on complex analytical tasks requiring decomposition and multi-step inference.
- **Method:** The model is trained on distilled reasoning traces collected from stronger teacher-style reasoning sources, with the goal of transferring cleaner analytical structure, stronger planning habits, and more stable task-solving behavior.
- **Target Behavior:** Compared with a standard instruct model, the tuned model is expected to respond with more deliberate reasoning organization, reduced shallow guessing, and stronger cross-domain analytical consistency.

### 📚 All Datasets Used
The dataset consists of multiple reasoning distillation sources:

| Dataset Name | Description / Purpose |
|--------------|-----------------------|
| [Roman1111111/gemini-3.1-pro-hard-high-reasoning](https://huggingface.co/datasets/Roman1111111/gemini-3.1-pro-hard-high-reasoning) | Primary high-quality reasoning source used to shape structured analytical style, planning behavior, and dense CoT patterns. |
| [Jackrong/Qwen3.5-reasoning-700x](https://huggingface.co/datasets/Jackrong/Qwen3.5-reasoning-700x) | Provides additional Qwen-family reasoning trajectories distilled from Qwen3.5-27B, improving style stability and complementary reasoning diversity. 🪐 (Only a small portion of this dataset was used to help avoid excessive degradation of generalization ability and mitigate catastrophic forgetting.)|
| [Roman1111111/gemini-3-pro-10000x-hard-high-reasoning](https://huggingface.co/datasets/Roman1111111/gemini-3-pro-10000x-hard-high-reasoning) | A broader multi-domain reasoning corpus used to enhance coverage across mathematics, systems, science, law, medicine, finance, and adversarial reasoning tasks. |

### 📊 Approximate Domain Composition (Approx|Samples|Share)

| Domain | Samples | Share |
|--------------|--------:|------:|
| Mathematics / Logic | 3947 | 28.5% |
| Computer Science / Programming / Systems | 3019 | 21.8% |
| Security / Adversarial Reasoning | 1551 | 11.2% |
| Physics / Astronomy / Engineering | 1482 | 10.7% |
| Law / Philosophy / Humanities | 1191 | 8.6% |
| Biology / Medicine | 817 | 5.9% |
| Finance / Economics | 679 | 4.9% |
| Chemistry / Materials | 540 | 3.9% |
| Applied / Social Systems (Urban Planning, Traffic, Supply Chain, etc.) | 360 | 2.6% |
| Other | 264 | 1.9% |

⚠️ **Distillation & Task-Specific Fine-Tuning Effects:** This model has been distilled and further fine-tuned on top of the base model for reasoning-oriented tasks. These techniques may improve performance on certain specialized tasks, but they can also influence the model’s generalization ability in broader scenarios and may lead to partial forgetting of some pretraining knowledge. The extent of these effects depends on factors such as the quality, scale, and distribution of the datasets used during distillation and fine-tuning. As a result, the model’s behavior may differ from the base model across different tasks or application contexts. Users are encouraged to evaluate the model according to their specific requirements before deployment. Thank you for your understanding～



## 🌟 Core Skills & Capabilities
1. **Structured Analytical Reasoning:** The model is optimized to first identify the real task structure before generating an answer, rather than relying on shallow immediate completion.
2. **Improved Multi-Step Planning:** It performs more reliably on tasks requiring decomposition, constraint tracking, sequential planning, and trade-off analysis.
3. **Cross-Domain Reasoning Strength:** The training corpus provides broad reasoning coverage across math, programming, systems, physics, law, medicine, finance, chemistry, and applied domains.
4. **Security & Adversarial Awareness:** A dedicated portion of the distilled data includes adversarial, attack-defense, and failure-mode reasoning tasks, improving robustness in difficult prompts.
5. **Compact but Strong Footprint:** Built on a 27B base, the model aims to deliver significantly denser reasoning behavior and cleaner analytical output than a generic base instruct model of similar size.

## ⚠️ Limitations & Intended Use
- **Hallucination Risk:** Although reasoning behavior is improved, the model remains an autoregressive LLM and may still hallucinate niche facts, citations, or unverifiable real-world details.
- **Reasoning Style Bias:** Because the model is tuned for analytical depth, it may sometimes produce longer or more structured answers than necessary for very simple prompts.
- **Teacher-Style Distillation Bias:** Some response behaviors reflect the reasoning style of the teacher traces used during distillation, rather than purely native behavior emerging from the base model itself.
- **Preview Version Notice:** As a relatively specialized distilled reasoning model, surrounding inference templates, prompt formatting strategies, and ecosystem integrations may still require tuning. Users may encounter occasional compatibility differences depending on runtime or deployment stack.

## 🙏 Acknowledgements
Special thanks to the **Qwen** team for the strong base architecture, and to the broader open-source ecosystem for enabling efficient reasoning distillation workflows. We also acknowledge the value of the distilled reasoning corpora derived from **Gemini 3.1 Pro**, **Qwen3.5**, and **Gemini 3 Pro**, which made this model possible.