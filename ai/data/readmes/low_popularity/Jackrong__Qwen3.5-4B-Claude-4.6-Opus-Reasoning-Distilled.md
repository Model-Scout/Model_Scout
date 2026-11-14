---
language:
- en
- zh
- ko
license: apache-2.0
base_model: Qwen/Qwen3.5-4B
tags:
- unsloth
- qwen
- qwen3.5
- reasoning
- chain-of-thought
- lora
pipeline_tag: image-text-to-text
datasets:
- nohurry/Opus-4.6-Reasoning-3000x-filtered
- Jackrong/Qwen3.5-reasoning-700x
---

# 🌟 Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled
🔥 **Update (April 5):** I’ve released the complete training notebook, codebase, and a comprehensive PDF guide to help beginners and enthusiasts understand and reproduce this model's fine-tuning process. 

> ❤️ Special thanks to the [**Unsloth**](https://unsloth.ai) open-source library and [@KyleHessling1](https://x.com/kylehessling1) for their support.

## 📚 Resources & Guides

👉 **[GitHub Repository: Jackrong-llm-finetuning-guide](https://github.com/R6410418/Jackrong-llm-finetuning-guide.git)**
Visit the repo to dive into the codebase and reproduce the results locally or on Colab.

### 📥 Core Technical Document
**🔗 [Qwopus3.5-27b Complete Fine-Tuning Guide (PDF)](https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/guidePDF/Qwopus3-5-27b-Colab_complete_guide_to_llm_finetuning.pdf)**
* **The Full Pipeline:** A step-by-step walkthrough—from downloading the base model and unifying heterogeneous data, to configuring trainer hyperparameters and publishing to Hugging Face.
* **Beginner Friendly:** Includes an introductory guide to getting started with Google Colab and Unsloth.
* *Feedback welcome! If you spot any areas for improvement, please let me know and I will update it promptly.*

> **A Note:**
> My goal isn't just to detail a workflow, but to demystify LLM training. Beyond the social media hype, fine-tuning isn't an unattainable ritual—often, all you need is a Google account, a standard laptop, and relentless curiosity. 
> 
> *No one starts as an expert, but every expert was once brave enough to begin.*
> 
> All training and testing for this project were self-funded. If you find this model or guide helpful, a **Star ⭐️ on GitHub** would be the greatest encouragement. Thank you! 🙏

> [!Note]
> The Claude series model optimizations are named under the **Qwopus3.5 series**, with the latest version being **🌟Qwopus3.5-v3**.

---

## 📢 Announcement

> **Update:**
> This model has been **further enhanced with additional reasoning data distilled from Qwen3.5-27B**.
>
> The new training data introduces higher-quality reasoning trajectories across domains such as **science, instruction-following, and mathematics**.
>
> Part of the data comes from **[Jackrong/Qwen3.5-reasoning-700x](https://huggingface.co/datasets/Jackrong/Qwen3.5-reasoning-700x)**, a curated dataset designed to improve **structured step-by-step reasoning** and **reasoning diversity**.


![HCaJnUQaoAAaMIc](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/k4JsVit-31Fw8RZ4pFkun.jpeg)

## 💡 Model Introduction
**Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled** is a highly capable reasoning model fine-tuned on top of the Qwen3.5-4B dense architecture. The model's core directive is to leverage state-of-the-art Chain-of-Thought (CoT) distillation primarily sourced from Claude-4.6 Opus interactions.

Through Supervised Fine-Tuning (SFT) focusing specifically on structured reasoning logic, this model excels in breaking down complex user problems, planning step-by-step methodologies within strictly formatted `<think>` tags, and ultimately delivering precise, nuanced solutions.

## 🗺️ Training Pipeline Overview

```text
Base Model (Qwen3.5-4B)
 │
 ▼
Supervised Fine-Tuning (SFT) + LoRA
(Response-Only Training masked on "<|im_start|>assistant\n<think>")
 │
 ▼
Final Model Text Only (Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled)
```

### 🧠 Example of Learned Reasoning Scaffold（Example）

The model includes targeted optimizations addressing Qwen3.5’s tendency toward excessive transitional or repetitive reasoning on simple queries. Through deep distillation and structural imitation of Claude-4.6-Opus reasoning chains, the model adopts a more efficient structured thinking pattern:  
**“Let me analyze this request carefully: 1..2..3...”.**  
This streamlined reasoning paradigm significantly reduces redundant cognitive loops while preserving deep analytical capacity, resulting in substantially improved inference efficiency.

```text
Let me analyze this request carefully:

1. Identify the core objective of the problem.
2. Break the task into clearly defined subcomponents.
3. Evaluate constraints and edge cases.
4. Formulate a step-by-step solution plan.
5. Execute the reasoning sequentially and verify consistency.
            .
            .
            .
```

### 🔹 Supervised Fine-Tuning (SFT)
- **Objective:** To inject high-density reasoning logic and establish a strict format for problem-solving involving an internal thinking state prior to outputting the final response.
- **Method:** We utilized **Unsloth** for highly efficient memory and compute optimization. A critical component of this stage is the `train_on_responses_only` strategy, masking instructions so the loss is purely calculated over the generation of the `<think>` sequences and the subsequent solutions.
- **Format Enforcement:** All training samples were systematically normalized so the model strictly abides by the structure `<think> {internal reasoning} </think>\n {final answer}`.

### 📈 Training Loss Curve
The training loss showed a strong and healthy downward trend throughout the run, demonstrating effective knowledge distillation. Starting from an initial loss of **0.74356**, the model converged steadily to a final loss of **0.23984** — indicating the model successfully internalized the structured `<think>` reasoning patterns from the Claude 4.6 Opus teacher data.

### 📚 All Datasets Used
The dataset consists of high-quality, filtered reasoning distillation data:

| Dataset Name | Description / Purpose |
|--------------|-----------------------|
| [nohurry/Opus-4.6-Reasoning-3000x-filtered](https://huggingface.co/datasets/nohurry/Opus-4.6-Reasoning-3000x-filtered) | Provides comprehensive Claude 4.6 Opus reasoning trajectories. |
| [Jackrong/Qwen3.5-reasoning-700x](https://huggingface.co/datasets/Jackrong/Qwen3.5-reasoning-700x) | Additional curated reasoning samples designed to strengthen structured step-by-step problem solving and improve reasoning diversity. |

## 🌟 Benchmark

| Benchmark | Baseline (4B) | Distilled (4B) |
|-----------|---------------|---------------|
| GPQA Diamond (0-shot) | 33.82 | **38.88** |
| AI2 ARC-Challenge (25-shot) | 64.59 | **66.38** |

These evaluation results were originally reported by khitsly.
Evaluation was conducted using the EleutherAI `lm-evaluation` with 8-bit inference and temperature 0. Higher scores indicate better performance.

## 🌟 Core Skills & Capabilities
1. **Modular & Structured Thinking:** Inheriting traits from Opus-level reasoning, the model demonstrates confident parsing of the prompt, establishing an outlined plan in its `<think>` block sequentially rather than exploratory "trial-and-error" self-doubt.
2. **Extended Context Support:** Fine-tuned smoothly with a 16,384 token context window allowing complex multi-step reasoning traces to exist gracefully within memory limits.

## ⚠️ Limitations & Intended Use
- **Hallucination Risk:** While reasoning is strong, the model remains an autoregressive LLM; external facts provided during the thinking sequence may occasionally contain hallucinations if verifying real-world events.
- **Intended Scenario:** Best suited for offline analytical tasks, coding, math, and heavy logic-dependent prompting where the user needs to transparently follow the AI's internal logic.
- This model is a test version intended solely for learning and demonstration purposes, and is for academic research and technical exploration use only.
## 🙏 Acknowledgements
Significant thanks to the [Unsloth AI](https://unsloth.ai/) team for making rapid fine-tuning of large LLM models accessible. Additionally, we acknowledge Qwen internally, and the open-source community developers producing exceptional distilled datasets (`nohurry` and `TeichAI`).