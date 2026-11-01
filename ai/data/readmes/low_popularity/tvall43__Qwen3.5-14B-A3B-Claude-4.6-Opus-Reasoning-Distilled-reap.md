---
base_model: Jackrong/Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled
tags:
- text-generation-inference
- transformers
- unsloth
- qwen3_5_moe
- unsloth
- qwen
- qwen3.5
- reasoning
- chain-of-thought
license: apache-2.0
language:
- zh
- en
- ko
pipeline_tag: text-generation
datasets:
- nohurry/Opus-4.6-Reasoning-3000x-filtered
- Jackrong/Qwen3.5-reasoning-700x
---

# more crazy reap
can i fit moe qwen3.5 in 10gb vram? since thats already risky, lets yolo and use claude distil too. 0.65 compression this time. my original goal was 8gb vram but i mathed wrong somewhere. that fits fine on my gpro x080 but not single gpu in the radeon v340l. maybe ill give it another attempt if it turns out not terrible.

test results:
- snake clone in single html file: fail even after 8 iterations.
- car wash test: pushing the car is "Possible but exhausting"

# 🌟 Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled

> 📢 **Release Note**
> **Build Environment Upgrades:**
> - **Fine-tuning Framework**: **Unsloth 2026.3.3** 
> - **Core Dependencies**: **Transformers 5.2.0**
> - Compared to the original model, **autonomy and stability are significantly improved**.

![HB8AleUaMAArNyM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/GHkMJL6I383eIwK1qj80K.jpeg)


## 💡 Model Introduction
**Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled** is a highly capable reasoning model fine-tuned on top of the powerful Qwen3.5 architecture. The model's core directive is to leverage state-of-the-art Chain-of-Thought (CoT) distillation primarily sourced from Claude-4.6 Opus interactions. 

Through Supervised Fine-Tuning (SFT) focusing specifically on structured reasoning logic, this model excels in breaking down complex user problems, planning step-by-step methodologies within strictly formatted `<think>` tags, and ultimately delivering precise, nuanced solutions. 

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

## 🗺️ Training Pipeline Overview

```text
Base Model (Qwen3.5-35B-A3B)
 │
 ▼
Supervised Fine-Tuning (SFT) + LoRA
 │
 ▼
Final Model (Claude-4.6-Opus-Reasoning-Distilled,text-only)
```

## 📋 Stage Details

### 🔹 Supervised Fine-Tuning (SFT)
- **Objective:** To inject high-density reasoning logic and establish a strict format for problem-solving involving an internal thinking state prior to outputting the final response.
- **Methodology:** We utilized **Unsloth** for highly efficient memory and compute optimization. A critical component of this stage is the `train_on_responses_only` strategy, masking instructions so the loss is purely calculated over the generation of the `<think>` sequences and the subsequent solutions. 
- **Format Enforcement:** All training samples were systematically normalized so the model strictly abides by the structure `<think> {internal reasoning} </think>\n {final answer}`.

### 📚 All Datasets Used
The dataset consists of high-quality, filtered reasoning distillation data:

| Dataset Name | Description / Purpose |
|--------------|-----------------------|
| [nohurry/Opus-4.6-Reasoning-3000x-filtered](https://huggingface.co/datasets/nohurry/Opus-4.6-Reasoning-3000x-filtered) | Provides comprehensive Claude 4.6 Opus reasoning trajectories. |
| [TeichAI/claude-4.5-opus-high-reasoning-250x](https://huggingface.co/datasets/TeichAI/claude-4.5-opus-high-reasoning-250x) | Injecting high-intensity, structured reasoning instances. |
| [Jackrong/Qwen3.5-reasoning-700x](https://huggingface.co/datasets/Jackrong/Qwen3.5-reasoning-700x) | Additional curated reasoning samples designed to strengthen structured step-by-step problem solving and improve reasoning diversity. |

## 🌟 Core Skills & Capabilities
1. **Modular & Structured Thinking:** Inheriting traits from Opus-level reasoning, the model demonstrates confident parsing of the prompt, establishing an outlined plan in its `<think>` block sequentially rather than exploratory "trial-and-error" self-doubt.
2. **Extended Context Support:** Fine-tuned smoothly with an 8192 context window allowing complex multi-step reasoning traces to exist gracefully within memory limits.

## ⚠️ Limitations & Intended Use
- **Hallucination Risk:** While reasoning is strong, the model remains an autoregressive LLM; external facts provided during the thinking sequence may occasionally contain hallucinations if verifying real-world events.
- **Intended Scenario:** Best suited for offline analytical tasks, coding, math, and heavy logic-dependent prompting where the user needs to transparently follow the AI's internal logic.
- **Preview Version Notice:** Because this model is relatively new and intentionally lightweight, the surrounding ecosystem — including inference templates, fine-tuning pipelines, routing configurations, and tooling integrations — may not yet be fully mature or standardized. As a result, users may encounter occasional bugs, compatibility inconsistencies, or integration edge cases. The current release should be considered a preview build while the broader architectural stack and supporting utilities continue to stabilize and improve.

### ⚠️ Training Disclaimer

During the fine-tuning process, the Triton kernel required approximately **131072 bytes of shared memory per CUDA block**. On some GPUs this exceeded the available shared memory limits, which caused kernel execution issues. To ensure training stability and proper kernel execution, the fine-tuning was therefore conducted on **80GB VRAM GPUs**.

This model was fine-tuned using a **LoRA-based parameter-efficient training strategy**, where only a small subset of parameters were updated. In total, **465,551,360 parameters were trainable out of 35,572,733,296 total parameters**, corresponding to **approximately 1.31% of the model being trained**.

During training, the loss curve exhibited noticeable fluctuations, which is common in LoRA-based reasoning distillation tasks. However, the overall trend remained **consistently decreasing**, with the training loss eventually converging to approximately **0.384**.
## 🙏 Acknowledgements
Significant thanks to the [Unsloth AI](https://unsloth.ai/) team for making rapid fine-tuning of MoE and large LLM models accessible. Additionally, we acknowledge Qwen internally, and the open-source community developers producing exceptional distilled datasets (`nohurry` and `TeichAI`).

## 📖 Citation

If you use this model in your research or projects, please cite:

```bibtex
@misc{jackrong_qwen35_opus_distilled,
  title        = {Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled},
  author       = {Jackrong},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/Jackrong/Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled}}
}
```
