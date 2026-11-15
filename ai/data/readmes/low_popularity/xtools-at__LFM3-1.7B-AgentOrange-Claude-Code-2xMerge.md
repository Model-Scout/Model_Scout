---
license: other
license_name: lfm1.0
library_name: transformers
pipeline_tag: text-generation
base_model: 
  - LiquidAI/LFM3-1.7B
  - mondk/LFM3-1.7B-Claude-Code-Safetensors
  - saidutta69/LFM3-1.7B-Claude-Fable5.1
datasets:
  - mondk/Ultra-Trio-Unfiltered
  - saidutta69/fable-5.1-premium-v2
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
  - agentic
  - tool-calling
  - function-calling
  - coding
  - claude-code
  - lfm
  - liquid-ai
  - tool-use
  - agent
  - claude-code
  - claude
  - coding-agent
  - code-generation
  - terminal
  - transformers
  - safetensors
  - merge
---

<p align="center"><a href="https://huggingface.co/xtools-at"><img src="banner-agentorange.jpg" alt="Made by xtools-at" width="100%"/></a></p>

# 🍊 LFM3-1.7B Agent Orange - Claude Code 2xMerge

A small, agent-focused merge of two community fine-tunes of Liquid AI's LFM3-1.7B.

**Agent Orange** aims to bring together structured tool use, coding assistance, and the action-oriented behavior needed for Claude-Code-style workflows, while keeping the model lightweight enough for local inference.

The goal isn't to recreate Claude Code itself, but to provide a compact model that can work with a compatible agent harness, navigate files, invoke tools, and participate in iterative coding workflows.

## 🧩 The Ingredients

This merge combines two complementary fine-tunes:

### 1. mondk/LFM3-1.7B-Claude-Code-Safetensors

[Model on Hugging Face](https://huggingface.co/mondk/LFM3-1.7B-Claude-Code-Safetensors)

A community fine-tune by **mondk**, built on LiquidAI's LFM3-1.7B and trained over several rounds using the `mondk/Ultra-Trio-Unfiltered` dataset.

Its training process focused on three areas:

- **Round 1:** Improving tool usage and function calling.
- **Round 2:** Improving benchmark performance.
- **Round 3:** Reinforcement learning with model-generated questions and answers.

This checkpoint provides the coding-oriented and general agentic foundation of the merge.

### 2. saidutta69/LFM3-1.7B-Claude-Fable5.1

[Model on Hugging Face](https://huggingface.co/saidutta69/LFM3-1.7B-Claude-Fable5.1)

A tool-calling fine-tune by **saidutta69**, based on LiquidAI/LFM3-1.7B and trained on the `claude_code` configuration of `saidutta69/fable-5.1-premium-v2`.

The fine-tune specifically targets reliable tool-call formatting and argument generation. It teaches the model to work with tools such as:

`Bash`, `Read`, `Write`, `Edit`, `Glob`, `Grep`, `WebFetch`, `WebSearch`, `TodoWrite`, `TaskCreate`, `TaskUpdate`, `TaskOutput`, and `ToolSearch`.

Its training uses BF16 LoRA, with assistant-turn-only loss masking and 4,096-token training windows. The intention is to improve schema fidelity and reduce invalid tool names in agentic environments.

## 🏗️ Base Model

Both fine-tunes originate from [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B), which in turn is built on [LiquidAI/LFM3-1.7B-Base](https://huggingface.co/LiquidAI/LFM3-1.7B-Base).

LFM3-1.7B is a 1.73B-parameter text model developed by Liquid AI. Its tri-hybrid architecture combines gated short convolutions, sliding-window attention, and global attention. The model was designed for efficient local deployment, tool calling, and agentic applications, with an advertised context window of up to 256K tokens.

This makes it an interesting foundation for experimenting with agent workflows in a relatively small parameter budget.

## ⚖️ Merge Configuration

The two fine-tunes were combined with a linear merge, using the following weights:

| Source model | Merge weight |
|---|---:|
| `mondk/LFM3-1.7B-Claude-Code-Safetensors` | 1.0 |
| `saidutta69/LFM3-1.7B-Claude-Fable5.1` | 0.8 |

The intention is to combine the coding and agentic behavior of the first checkpoint with the more focused tool-call formatting of the second.

## 🎯 Intended Use

Agent Orange is intended for experimentation with lightweight coding agents and tool-driven workflows, including:

- Repository exploration and code navigation.
- Reading, editing, and creating files.
- Shell and terminal tool interactions.
- Structured function calling.
- Multi-step coding assistance.
- Claude-Code-style agent harnesses with compatible tool definitions.

A compatible runtime or harness must provide the actual tools and execute the model's requested actions. The model itself does not execute shell commands or modify files.

## ⚠️ Limitations

Agent Orange is an experimental community merge, not a drop-in replacement for larger coding models.

Tool schemas learned during fine-tuning are reconstructed representations of Claude-Code-style tools, not guaranteed to match Anthropic's official implementation exactly. Tool names, arguments, and outputs should be validated by the host application.

The Fable fine-tune used 4,096-token training windows, so the base model's advertised 256K context length should not be interpreted as a guarantee of equivalent long-context performance after fine-tuning and merging.

No independent benchmark results are currently reported for this merged checkpoint. Evaluate it with your own agent harness and tasks before relying on it for more demanding coding work.

**Safety recommendation:** Run the model with appropriate sandboxing and permission controls. Review shell commands and file operations before execution, particularly when working with untrusted repositories or inputs.

## 📜 License

This model retains the **LFM Open License v1.0** (`lfm1.0`) licensing of its upstream LFM3 fine-tunes.

Please review the included `LICENSE` file and the upstream license terms before redistribution or commercial deployment.

## 🙏 Acknowledgements

Thanks to:

- [Liquid AI](https://huggingface.co/LiquidAI) for the LFM3 model family.
- [mondk](https://huggingface.co/mondk) for the Claude Code-oriented LFM3 fine-tune and Ultra-Trio-Unfiltered dataset.
- [saidutta69](https://huggingface.co/saidutta69) for the Fable5.1 tool-calling fine-tune and associated training data.

And, of course, to the creators and contributors behind the datasets used in these projects.

--- 

🍊 Enjoy experimenting with Agent Orange!