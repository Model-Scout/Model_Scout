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
- competitive-programming
pipeline_tag: image-text-to-text
datasets:
- Jackrong/Competitive-Programming-python-blend
- stepfun-ai/Step-3.5-Flash-SFT
metrics:
- accuracy
new_version: Jackrong/Qwen3.5-4B-Neo
---

# 🌟 Qwen3.5-4B-Neo

## Model Introduction
**Qwen3.5-4B-Neo** is a reasoning-focused fine-tune of Qwen3.5-4B. It is designed to make the model’s reasoning process more concise and efficient, while keeping overall accuracy competitive.

> On a 250-question MMLU-Pro subset covering five categories, Qwen3.5-4B-Neo achieved **82.00% pass@1 (205/250)**, compared with **80.40% (201/250)** for the base Qwen3.5-4B. The gain is modest, but Neo also shows a much shorter reasoning process overall.

> On non-truncated outputs, the average think-chain length was reduced from **6,962 to 3,955 characters**, and the median length dropped from **4,600 to 1,951 characters**. In efficiency terms, this corresponds to **2.31 correct solutions per 10k think characters**, compared with 1.03 for the base model.

Across the five categories, Neo performed better in biology, computer science, mathematics, and other sciences, while trailing in physics. Overall, the results suggest that Qwen3.5-4B-Neo offers slightly better accuracy than the base model, with a substantially more efficient reasoning style.

> ⚠️ Note: The evaluation results shown here are based on a sampled subset of MMLU-Pro rather than the full benchmark. While the subset was kept balanced across five categories, the reported numbers are intended mainly for relative comparison under this specific setting and may not fully represent the model’s performance on the complete benchmark.



### MMLU-Pro Benchmark Analysis 🪐

![Screenshot 2026-03-23 at 6.06.07 PM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/TlcPXA7tRb2cC_qC2_so_.png)

![Screenshot 2026-03-23 at 6.07.39 PM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/KG76kNeIJ88F4iYhOxcHI.png)

![Screenshot 2026-03-23 at 6.07.59 PM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/JeN8ulnILxwqXDb6TgW6w.png)

![Screenshot 2026-03-23 at 6.08.18 PM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/6acL4CyZzLuNX0cOB7jil.png)

![Screenshot 2026-03-23 at 6.08.38 PM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/mHEjeqz8jdm76b1gFfosV.png)

![Screenshot 2026-03-23 at 6.08.53 PM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/rUwyqwr24ZCRKeFqDcjUq.png)

![Screenshot 2026-03-23 at 6.09.10 PM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/yDmQ-FncNkxlHu0D0XbCa.png)

## 🗺️ Training Pipeline Overview

```text
Base Model (Qwen/Qwen3.5-4B)
 │
 ▼
Qwen3.5-4B fine-tuned with Unsloth
 │
 ▼
Supervised Fine-Tuning (SFT) + LoRA
(Response-Only Training masked on "<|im_start|>assistant\n<think>")
 │
 ▼
Jackrong/Qwen3.5-4B-Neo
```

### 🧠 Example of Learned Reasoning Scaffold

Through robust data cleaning and formatting, the model was conditioned to explicitly structure its thought processes inside `<think>...</think>` tags before emitting the final answer. This forces the model to methodically break down complex programming or logical problems without repetitive thoughts.

```text
<|im_start|>user
[User Query here]<|im_end|>
<|im_start|>assistant
<think>
  .
  .
  .
    ...
</think>
[Final concise and accurate answer]
```

### 📚 All Datasets Used
The dataset consists of high-quality, filtered reasoning distillation data merged during the pipeline. Our pipeline dynamically sampled and structured conversations, strictly maintaining the intended layout.

1. **[stepfun-ai/Step-3.5-Flash-SFT](https://huggingface.co/datasets/stepfun-ai/Step-3.5-Flash-SFT)**
2. **Jackrong/Competitive-Programming-python-blend** (A custom curated blend specifically for Python competitive programming and logic). 

Detailed breakdown of the **Competitive-Programming-python-blend**:

| Source | Role in the Blend |
|--------|-------------------|
| `nohurry/Opus-4.6-Reasoning-3000x-filtered` | Reasoning-heavy synthetic SFT data |
| `Jackrong/Qwen3.5-reasoning-700x` | Distilled reasoning and instruction-following data |
| `nvidia/Nemotron-SFT-Competitive-Programming-v2` (`competitive_coding_python`) | Primary Python competitive-programming supervision |
| `nvidia/Nemotron-SFT-Competitive-Programming-v2` (`competitive_coding_cpp`) | Small cross-language competitive-programming supplement |
| `nvidia/Nemotron-SFT-SWE-v2` (`agentless`) | Lightweight agentless SWE-style supervision |
| `nvidia/Nemotron-SFT-Instruction-Following-Chat-v2` (`reasoning_on`) | Small reasoning-oriented chat supplement |

## ⚠️ Limitations & Intended Use
- **Hallucination Risk:** While reasoning is strong, the model remains an autoregressive LLM; external facts provided during the thinking sequence may occasionally contain hallucinations if verifying real-world events.
- **Context Boundaries:** In rare cases of extremely complex logic where the model struggles to converge, it may exhibit truncation events from excessive circular thinking.
- **Intended Scenario:** Best suited for offline analytical tasks, coding, competitive programming, math, and heavy logic-dependent prompting where the user needs to transparently follow the AI's internal logic with high token efficiency.
- This model is a test version intended solely for learning and demonstration purposes, and is for academic research and technical exploration use only.

## 🙏 Acknowledgements
Significant thanks to the [Unsloth AI](https://unsloth.ai/) team for making rapid fine-tuning of large LLM models accessible. Additionally, we acknowledge Qwen internally, and the open-source community developers producing exceptional distilled datasets.