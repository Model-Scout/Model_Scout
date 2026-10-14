---
library_name: transformers
base_model: unsloth/Qwen3.5-9B
base_model_relation: finetune
license: apache-2.0
language:
- en
- zh
- ko
- ja
- ru
- es
pipeline_tag: image-text-to-text
tags:
- qwen3_5
- unsloth
- merged-lora
- reasoning
- code-generation
- tool-use
- agent
- mtp
- local-inference
- vision
- multimodal
- safetensors
---

# ⚡️Qwopus3.5-9B-Coder-Flash

![Qwopus Coder Flash — practical coding, focused reasoning; 9B, merged LoRA, original chat template, MTP weights retained](assets/model_hero.png)

**Qwopus3.5-9B-Coder-Flash** is a coding and agent-focused fine-tune of [Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B), prepared from the [Unsloth distribution](https://huggingface.co/unsloth/Qwen3.5-9B). This repository provides the **merged dense checkpoint**. The benchmarks below evaluate the release checkpoint.

## 💡 1. The Flash Philosophy — Make Each Token Count

A small model should make useful work accessible on local hardware. Following the efficiency-first philosophy of [Qwopus3.8-27B-Flash-V2](https://huggingface.co/Jackrong/Qwopus3.8-27B-Flash-V2), Coder Flash aims to preserve practical problem-solving ability while reducing unproductive reasoning.

This matters especially in an agent loop: **read → reason → call tools → edit → test**. A little extra thinking on every turn accumulates into a long wait. The goal is focused reasoning that reaches usable code and a clear next action, with less generation overhead.

> [!IMPORTANT]
> **Efficiency includes correctness.** A shorter answer is valuable when it still solves the task. The results below pair coding quality with measured reasoning length, rather than treating brevity alone as success.

## 🧪 2. Model Preparation and Collaboration

**Built with community support.** Special thanks to [Kyle Hessling · @KyleHessling1 on X](https://x.com/KyleHessling1) for his collaboration, test, feedback, and machine support for the Qwopus project, and to [Unsloth](https://unsloth.ai/) for making efficient fine-tuning more accessible. Explore the [Unsloth framework on GitHub](https://github.com/unslothai/unsloth).

## 📊 3. Coding Quality — HumanEval and HumanEval+

Both models were evaluated on **HumanEval+ v0.1.10**, with **164 programming tasks, five samples per task, and 820 generations per model**. The reported configuration uses **temperature 0.2**, **top-p 0.95**, **Q8_0 GGUF**, **llama.cpp CUDA**, and **MTP speculative decoding with maximum draft length 2**.

![HumanEval and HumanEval+ results](assets/coding_quality.png)

On the expanded HumanEval+ diagnostic scores, Coder Flash produced **63 more correct samples**, a **9.56% relative increase**, with a **7.68 percentage-point gain in Pass@1**. Here, Pass@1 is estimated from all five samples per task; Pass@5 measures the probability that at least one of the five samples passes.

> [!NOTE]
> Run-configuration differences are described in the efficiency section below.

## ⚡ 4. Efficiency — Shorter Reasoning, More Useful Code

Across **820 generations per model**, Qwen3.5-9B averaged **4,189.07 reasoning tokens**, compared with **885.31 tokens for Coder Flash** — a **78.87% reduction**, or approximately **3,304 fewer tokens per attempt**. Coder Flash also produced **63 more correct HumanEval+ samples**.

Reasoning lengths were calculated from the saved evaluation outputs, including the recorded `reasoning_content`.

![Reasoning length and efficiency comparison](assets/reasoning_efficiency.png)

![HumanEval chain-of-thought length comparison](assets/reasoning_comparison.png)

> [!TIP]
> **More useful code with less reasoning.** Correct HumanEval+ samples per 1,000 reasoning tokens increased from **0.192 to 0.995**, giving Coder Flash **5.18× the reasoning efficiency**.

Median chain-of-thought length decreased from **727.5 to 398 tokens**, while the 95th percentile decreased from **15,360 to 2,586 tokens**.

Reasoning-length variance decreased by **85.76% overall** and **85.22% across repeated attempts on the same task**.


## 🍎 5. Practical Agent Evaluation — BenchLocal

We evaluated Coder Flash and Qwen3.5-9B with [**BenchLocal**](https://github.com/stevibe/BenchLocal) to compare their performance on local agent tasks.

**Test environment:** Apple Silicon Mac, **LM Studio**.

Coder Flash achieved **higher overall scores in both suites**:

![BenchLocal suite scores](assets/benchlocal_scores.png)

The following breakdown compares performance across selected capabilities:

![Selected BenchLocal capability scores](assets/benchlocal_capabilities.png)

Scores are BenchLocal composite scores. Docker-based verification was unavailable during these runs.

Thank you to [**Steven Lei (`stevenlei`)**](https://github.com/stevenlei) for creating [BenchLocal](https://github.com/stevibe/BenchLocal).


## 🧭 6. Intended Use and Limitations

Coder Flash is intended for local code generation, debugging, tool-assisted development, and experimentation with compact agents. Review generated code and run your own tests before relying on it.

The reported results cover specific tasks, prompts, sampling settings, and runtimes. They do not establish universal coding accuracy, vision quality, long-context reliability, or agent safety. Reasoning-length variability measures generation behavior, not the probability of a correct answer. Difficult tasks can still produce errors, inefficient reasoning, or unsuccessful tool interactions.

## 🙏 7. Acknowledgements and Citation

Thanks to the [Qwen team](https://huggingface.co/Qwen/Qwen3.5-9B) for the foundation model; [Unsloth](https://unsloth.ai/) and its [open-source framework](https://github.com/unslothai/unsloth) for fine-tuning tooling; [Kyle Hessling](https://x.com/KyleHessling1) for Qwopus collaboration and support; [EvalPlus](https://github.com/evalplus/evalplus), [llama.cpp](https://github.com/ggml-org/llama.cpp), [LM Studio](https://lmstudio.ai/), [MLX](https://github.com/ml-explore/mlx), and [BenchLocal](https://github.com/stevibe/BenchLocal) for the evaluation and local inference ecosystem.

**License:** Apache-2.0, following the upstream model license.

```bibtex
@misc{jackrong2026qwopus35coderflash,
  title        = {Qwopus3.5-9B-Coder-Flash},
  author       = {Jackrong},
  year         = {2026},
  howpublished = {Hugging Face},
  url          = {https://huggingface.co/Jackrong/Qwopus3-5-9B-Coder-Flash}
}
```
