---
base_model:
  - xtools-at/LFM3-1.7B-AgentOrange-Claude-Code-2xMerge
base_model_relation: finetune
library_name: transformers
pipeline_tag: text-generation
license: other
license_name: lfm1.0
language:
  - en
  - ar
  - zh
  - fr
  - de
  - it
  - ja
  - ko
  - pt
  - es
  - vi
  - th
  - id
  - hi
  - ru
  - pl
tags:
  - lfm3
  - liquid-ai
  - reasoning
  - reasoning-distillation
  - agentic
  - coding
  - tool-calling
  - function-calling
  - claude-code
  - claude-opus
  - claude-sonnet
  - transformers
  - safetensors
  - unsloth
datasets:
  - TeichAI/Claude-Opus-4.6-Reasoning-887x
  - TeichAI/claude-4.5-opus-high-reasoning-250x
  - TeichAI/claude-sonnet-4.5-high-reasoning-250x
  - Roman1111111/claude-opus-4.6-10000x
---
<p align="center"><a href="https://huggingface.co/xtools-at"><img src="banner-opus.jpg" alt="Made by xtools-at" width="100%"/></a></p>

# ✴️ LFM3-1.7B Agent Orange - Claude Reasoning Distilled

A reasoning-focused fine-tune of [xtools-at/LFM3-1.7B-AgentOrange-Claude-Code-2xMerge](https://huggingface.co/xtools-at/LFM3-1.7B-AgentOrange-Claude-Code-2xMerge), built on top of Liquid AI's LFM3-1.7B.

This experiment combines an existing coding- and agent-focused foundation with additional training on 8,000 examples of Claude Opus and Sonnet reasoning traces. The aim is to bring more structured problem-solving and analytical reasoning into a compact model that already has a foundation in coding assistance and tool use.

## 🧩 The starting point

[Agent Orange](https://huggingface.co/xtools-at/LFM3-1.7B-AgentOrange-Claude-Code-2xMerge) is a [xtools-at](https://huggingface.co/xtools-at) merge of two LFM3 fine-tunes:

- [mondk/LFM3-1.7B-Claude-Code-Safetensors](https://huggingface.co/mondk/LFM3-1.7B-Claude-Code-Safetensors), focused on coding and general agentic behavior.
- [saidutta69/LFM3-1.7B-Claude-Fable5.1](https://huggingface.co/saidutta69/LFM3-1.7B-Claude-Fable5.1), focused on structured tool calling and argument generation.

The merge combines these checkpoints using linear merge weights of 1.0 and 0.8, respectively.

Both originate from [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B), a 1.73B-parameter text model built around a tri-hybrid architecture combining gated short convolutions, sliding-window attention, and global attention. LFM3 was designed with local deployment, tool use, and agentic applications in mind.

This fine-tune builds on that starting point with a different emphasis: improving the model's exposure to structured, multi-step reasoning.

## ✨ What's the idea?

Good reasoning isn't just about producing longer explanations. It's about approaching a problem methodically, exploring relevant possibilities, and arriving at a useful answer.

The additional training focuses on examples that may help with:

- 🧠 Multi-step reasoning and analytical problem-solving.
- 💻 Coding questions and technical tasks.
- 🔢 Mathematical and logical problems.
- 🛠️ Breaking down complex tasks into manageable steps.
- 🤖 Reasoning in workflows that involve tools and external actions.

The goal is to complement Agent Orange's existing coding and agent-oriented foundation with more examples of deliberate problem-solving.

These are intended use cases, not measured improvements. Whether the additional training actually improves performance over the parent checkpoint still needs to be established through independent evaluations.

## 📚 Training data

The additional fine-tuning dataset combines four collections of Claude-generated reasoning examples:

| Dataset | Contribution |
|---|---|
| [Claude-Opus-4.6-Reasoning-887x](https://huggingface.co/datasets/TeichAI/Claude-Opus-4.6-Reasoning-887x) | Opus 4.6 reasoning traces |
| [claude-4.5-opus-high-reasoning-250x](https://huggingface.co/datasets/TeichAI/claude-4.5-opus-high-reasoning-250x) | High-reasoning Opus examples |
| [claude-sonnet-4.5-high-reasoning-250x](https://huggingface.co/datasets/TeichAI/claude-sonnet-4.5-high-reasoning-250x) | Additional Sonnet reasoning examples |
| [claude-opus-4.6-10000x](https://huggingface.co/datasets/Roman1111111/claude-opus-4.6-10000x) | Larger pool of Opus 4.6 traces, randomly sampled |

A total of **8,000 examples** were used for training, with a separate **400-example evaluation set (5%)** sampled proportionally to the dataset composition. Entries were filtered to a maximum length of 8,000 characters.

The parent Agent Orange checkpoint also inherits training from the [Ultra-Trio-Unfiltered](https://huggingface.co/datasets/mondk/Ultra-Trio-Unfiltered) and [Fable 5.1 Premium](https://huggingface.co/datasets/saidutta69/fable-5.1-premium-v2) datasets. The four collections above are the additional reasoning data used in this fine-tuning stage.

As with any synthetic-data approach, the model may inherit stylistic biases, recurring mistakes, or weaknesses from its source traces.

## 🔬 Training setup

The additional fine-tuning used LoRA for one epoch, targeting all LoRA-compatible model modules.

| Parameter | Value |
|---|---|
| Base model | `xtools-at/LFM3-1.7B-AgentOrange-Claude-Code-2xMerge` |
| Original model family | `LiquidAI/LFM3-1.7B` |
| Fine-tuning method | LoRA, 16-bit |
| Training examples | 8,000 |
| Evaluation examples | 400 |
| Epochs | 1 |
| Maximum training context | 8,192 tokens |
| Learning rate | 2e-4 |
| LoRA rank (`r`) | 16 |
| LoRA alpha | 32 |
| LoRA dropout | 0.02 |
| Optimizer | AdamW 8-bit |
| Learning rate scheduler | Linear |
| Weight decay | 0.001 |
| Batch configuration | 4 × 8 |

The single-epoch approach keeps the experiment relatively lightweight while limiting repeated exposure to the synthetic examples. It is a practical starting point, but doesn't guarantee that all of the parent model's existing coding and tool-use capabilities will be preserved.

### 📊 Training results

| Metric | Result |
|---|---:|
| Training loss | 0.814 |
| Evaluation loss | 0.796 |

The evaluation loss finished slightly below the training loss. These values are useful training diagnostics, but they don't directly measure reasoning quality or demonstrate an improvement over Agent Orange.

Benchmark comparisons and qualitative tests on unseen problems would be needed to understand the actual effect of this fine-tuning stage.

## 🎯 Intended use

This model is intended for experimentation with compact reasoning and coding agents, particularly:

- Multi-step reasoning and analytical assistance.
- Coding, debugging, and technical problem-solving.
- Repository exploration and code navigation.
- Structured function calling and tool-assisted workflows.
- Local inference and resource-conscious deployments.
- Research into synthetic-data distillation and agent-oriented fine-tuning.

For tool-driven applications, a compatible runtime or agent harness must provide the tools and execute the model's requested actions. The model generates tool requests; it does not independently execute commands or modify files.

## ⚠️ Limitations

A few things worth keeping in mind:

- **Reasoning can still be wrong.** Detailed explanations don't guarantee correct conclusions.
- **Small model trade-offs.** At 1.73B parameters, the model is not a drop-in replacement for larger coding or reasoning models.
- **Synthetic-data bias.** The additional training may reproduce errors and stylistic habits found in the source traces.
- **Tool compatibility.** Agent Orange inherits reconstructed Claude-Code-style tool schemas. These may not exactly match official tool implementations, so names, arguments, and outputs should be validated by the host application.
- **Capability retention isn't guaranteed.** Additional fine-tuning can change existing instruction-following, coding, and tool-use behavior.
- **Long-context behavior is unverified.** LFM3 advertises a context window of up to 256K tokens, but the upstream Agent Orange components were trained with shorter windows, and this fine-tuning used 8,192 tokens. Equivalent performance at 256K should not be assumed.
- **Limited evaluation.** Training and evaluation losses alone cannot establish improvements. No independent benchmark results are reported for this checkpoint.

For agentic use, run the model with appropriate sandboxing and permission controls. Review shell commands and file operations before allowing them to affect important data.

## 🙏 Acknowledgements

Thanks to Liquid AI for releasing the LFM3 model family, mondk and saidutta69 for their complementary LFM3 fine-tunes and training datasets, and the TeichAI and Roman1111111 dataset authors for sharing the reasoning collections used in this experiment.

Thanks also to the Unsloth team for making efficient fine-tuning more accessible.

Please review the [LFM Open License v1.0](https://huggingface.co/LiquidAI/LFM3-1.7B) and the underlying dataset terms before redistributing or using this model commercially.

---

✴️ A small model, a coding-oriented foundation, and a little more practice at thinking through problems. Enjoy experimenting!