---
language:
- en
- zh
- ko
license: apache-2.0
base_model: Qwen/Qwen3.5-9B
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
- Roman1111111/claude-opus-4.6-10000x
---

# 🌟 Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2
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

> *Note: Due to the constraints of SFT sample size and training scope, the model's broad general-purpose capabilities might be slightly impacted. The efficiency and accuracy results discussed here are based on the HumanEval and HumanEval+ benchmarks. Thank you for your understanding!*

![HCaJnUQaoAAaMIc](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/k4JsVit-31Fw8RZ4pFkun.jpeg)

## 💡 Model Introduction
**Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2** is the second iteration of this reasoning-focused Qwen3.5-9B fine-tune, built to drastically improve the *efficiency* of chain-of-thought generation, unlocking highly substantial gains in reasoning speed and cost-reduction while actually increasing absolute accuracy.

Compared with the earlier version, **v2 was trained with 14,000 Claude 4.6 Opus-style general reasoning samples**, with a stronger emphasis on transferring concise, reusable reasoning patterns rather than only maximizing raw benchmark scores. The goal of v2 is not simply to make the model "think more," but to help it **think more economically**: reducing unnecessarily long internal chains, avoiding verbose over-analysis on easy problems, and massively improving the reasoning-cost-to-quality ratio while beating the baseline's benchmark correctness.

A key design choice in v2 is that the distillation data is **primarily general-domain reasoning data**—specifically focused on mathematics, word problems, logical deduction, and a balanced mix of general knowledge and instructions—rather than specialized code-heavy supervision. Consequently, **HumanEval and HumanEval+ are employed here to evaluate cross-task generalization and capability transfer**, rather than serving as direct optimization targets. High performance on these benchmarks, despite the lack of code-centric training, confirms that the model's **reasoning scaffold** has become more robust and transferable, proving that fundamental reasoning logic can effectively power specialized tasks like programming.

### HumanEval | HumanEval+ Benchmark Analysis 🪐


![Screenshot 2026-03-23 at 5.28.20 PM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/VI6a_jMAnoFW7_75d3gO1.png)


![Screenshot 2026-03-23 at 5.28.33 PM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/Q6CsbuScRp6juKkgFgSh9.png)


![Screenshot 2026-03-23 at 5.29.13 PM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/PJQJEWUGoXtz6SMe1HrSF.png)


![Screenshot 2026-03-23 at 5.29.34 PM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/-JEWsx2y9aCLpsgKteEgO.png)


![Screenshot 2026-03-23 at 5.29.52 PM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/puDjTvm_H2EtcvhFceOTq.png)

 

![Screenshot 2026-03-23 at 5.30.06 PM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/y_e3gUeer4zZmKQyYz6Lm.png)

For users who care about **reasoning efficiency per unit of inference budget**, v2 is exceptionally powerful—not only achieving higher peak accuracy, but doing so while consuming over 20% fewer characters and tokens.

That matters especially for:

- **Resource-constrained local deployment**: On consumer GPUs or lower-memory local setups, shorter and cleaner reasoning traces can reduce latency, memory pressure, and the effective cost of generation.
- **Agentic workflows**: In multi-step agents, the model often solves many *easy* or *medium* subtasks. In those settings, excessively elaborate chain-of-thought can become a tax on throughput. A model that reaches a better answer with fewer reasoning tokens can radically improve end-to-end agent speed and lower cumulative inference cost.
- **Open-source tool use and emerging agent stacks**: For users building with lightweight open reasoning systems, browser-use agents, terminal agents, or projects in the "OpenClaw / local autonomous agent" style ecosystem, a model that achieves better peak accuracy while drastically improving reasoning economy is highly practical for real-world loops.
- **Simple problems at scale**: One common issue with strong reasoning-tuned base models is that they sometimes produce very elaborate internal traces even for simple prompts. While that can look impressive, it is often inefficient in practice. v2 is explicitly aimed at trimming this overhead.

In short, **v2 no longer forces a trade-off between absolute coding benchmark scores and reasoning economy**. It provides a fully optimized deployment-ready profile: **faster, shorter, more economical reasoning** paired with stronger generalization and accuracy. For local users, agent builders, and cost-sensitive applications, v2 is a strict upgrade.

## 🗺️ Training Pipeline Overview

```text
Base Model (Qwen3.5-9B)
 │
 ▼
Qwen3.5-9B fine-tuned with Unsloth
 │
 ▼
Supervised Fine-Tuning (SFT) + LoRA
(Response-Only Training masked on "<|im_start|>assistant\n<think>")
 │
 ▼
Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2
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

### 📚 All Datasets Used
The dataset consists of high-quality, filtered reasoning distillation data:

| Dataset Name | Description / Purpose |
|--------------|-----------------------|
| [nohurry/Opus-4.6-Reasoning-3000x-filtered](https://huggingface.co/datasets/nohurry/Opus-4.6-Reasoning-3000x-filtered) | Provides comprehensive Claude 4.6 Opus reasoning trajectories. |
| [Roman1111111/claude-opus-4.6-10000x](https://huggingface.co/datasets/Roman1111111/claude-opus-4.6-10000x) | Large-scale public Claude 4.6 Opus distillation data used to strengthen general reasoning transfer in v2. |
| [Jackrong/Qwen3.5-reasoning-700x](https://huggingface.co/datasets/Jackrong/Qwen3.5-reasoning-700x) | Additional curated reasoning samples designed to strengthen structured step-by-step problem solving and improve reasoning diversity. |


## ⚠️ Limitations & Intended Use
- **Hallucination Risk:** While reasoning is strong, the model remains an autoregressive LLM; external facts provided during the thinking sequence may occasionally contain hallucinations if verifying real-world events.
- **Intended Scenario:** Best suited for offline analytical tasks, coding, math, and heavy logic-dependent prompting where the user needs to transparently follow the AI's internal logic.
- This model is a test version intended solely for learning and demonstration purposes, and is for academic research and technical exploration use only.

## 🙏 Acknowledgements
Significant thanks to the [Unsloth AI](https://unsloth.ai/) team for making rapid fine-tuning of large LLM models accessible. Additionally, we acknowledge Qwen internally, and the open-source community developers producing exceptional distilled datasets.