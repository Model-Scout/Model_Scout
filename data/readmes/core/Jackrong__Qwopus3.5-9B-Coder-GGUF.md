---
library_name: transformers
base_model:
- Jackrong/Qwopus3.5-9B-v3.5
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
- qwen3_5
- reasoning
- chain-of-thought
- lora
- sft
- agent
- tool-use
- function-calling
- coder
license: apache-2.0
language:
- en
- zh
- es
- ru
- ja
pipeline_tag: image-text-to-text
datasets:
- lambda/hermes-agent-reasoning-traces
- Jackrong/Claude-opus-4.7-TraceInversion-5000x
- Jackrong/Claude-opus-4.6-TraceInversion-9000x
---
# 🌟 Qwopus3.5-9B-coder

## 🚀 Model Fine-Tuning and Logical Alignment (Qwopus3.5-9B-coder)

As the base model of this model, **Qwopus3.5-9B-v3.5** is already a model with powerful capabilities. On this foundation, **Qwopus3.5-9B-coder** is specially optimized and fine-tuned for high-performance **🤖 Agentic Coding, complex Tool Calling, and logical reasoning.**

> 💡 **Why the 9B Dense Model?**
> We believe that the 9B dense architecture represents the perfect **"sweet spot"** for large language models. It runs seamlessly at 8-bit precision on entry-level 16GB RAM devices—such as standard laptops and the Mac mini—making it exceptionally lightweight yet highly versatile. Without requiring expensive hardware, it allows you to achieve excellent performance paired with impressive inference speeds. Simply put, **Qwen3.5-9B is currently the best open-source model in its class.**


![image](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/8qFQVuCxbgkWqKa2B_Vph.jpeg)

> [!TIP]
>**Vision & Tool Calling Support**: This model supports visual capabilities and tool calling. To enable vision, please place the `mmproj.gguf` file from the [GGUF repository](https://huggingface.co/Jackrong/Qwopus3.5-9B-coder-GGUF) into the same directory as the main `.gguf` file.

---

### 🛠 Training Strategy

The fine-tuning process of this model deeply integrates **Trace Inversion** data augmentation technology with high-quality **Agent Traces**. This systematic approach not only strengthens the model's ability to solve complex programming tasks, but also greatly improves its logical coherence and accuracy when using various tools.

This model is designed specifically for the following goals:

- 🧩 More structured and stronger logical reasoning capabilities, reducing repetitive thinking
- 💻 More powerful capabilities in code writing, debugging, and repository-level task processing
- 🛠 More stable and accurate Tool Calling capabilities for terminal commands, file operations, and browsers
- 🔁 Better cross-data source distillation alignment


> [!WARNING]
> - **Community Release Notice**: Qwopus3.5-9B-coder is released purely as an experimental community version, aiming to explore the combination of Agent capabilities and deep reasoning, and is only for research and exploration use.
> - **Warning**: Because this model is vertically fine-tuned for programming agents and deep reasoning, and has not undergone comprehensive general performance evaluation, its capabilities in general domains or specific non-programming tasks may suffer from Capability Decay. Users are advised to be aware of its limitations in other scenarios while exploring its core capabilities.

---


## 📊 Baseline Performance Comparison

To verify the execution efficiency and logical robustness of **Qwopus3.5-9B-coder** in actual agent scenarios, we adopted the open-source testing framework [benchlocal](https://github.com/stevibe/benchlocal).

### Test Configuration
- **Hardware Environment**: Apple Silicon (Mac)
- **Inference Backend**: LM Studio / MLX / GGUF
- **Testing Platform**: [benchlocal](https://github.com/stevibe/benchlocal) - An evaluation suite focusing on local model agent capabilities.
- 🍎 You can see the actual inference speeds of different model formats on the same device.

### 🧪 Benchmark Results 

<div style="display: inline-block; padding: 6px 16px; background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; border-radius: 8px; font-weight: 700; font-size: 16px; margin-bottom: 12px;">1. Complex Agent Performance - HermesAgent-20</div>
The following is the comparative performance under the HermesAgent-20 task set:

<table style="width: 100%; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <thead>
    <tr>
      <td colspan="4" style="padding: 8px 12px; font-weight: 600; color: #7c3aed; border-bottom: 1px solid rgba(124, 58, 237, 0.2); background: rgba(124, 58, 237, 0.05);">HermesAgent-20 Performance Metrics</td>
    </tr>
    <tr style="background: rgba(128, 128, 128, 0.02);">
      <th style="padding: 7px 7px; padding-left: 20px; text-align: left; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Model</th>
      <th style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Test Set</th>
      <th style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Comprehensive Score</th>
      <th style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Core Dimensions (M/O/S/S/B)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><b><a href="https://huggingface.co/Jackrong/Qwopus3.5-9B-coder-GGUF" style="color: #7c3aed; text-decoration: none;">Qwopus3.5-9B-coder</a></b></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">HermesAgent-20</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); color: #7c3aed; font-weight: bold;">85</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">84 / 93 / 88 / 75 / 84</td>
    </tr>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><a href="https://huggingface.co/Qwen/Qwen3.5-9B" style="color: #666; text-decoration: none;">Qwen/Qwen3.5-9B</a></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">HermesAgent-20</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">71</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">75 / 58 / 100 / 53 / 69</td>
    </tr>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><a href="https://huggingface.co/armand0e/Qwen3.5-9B-Agent" style="color: #666; text-decoration: none;">armand0e/Qwen3.5-9B-Agent</a></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">HermesAgent-20</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">68</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">71 / 83 / 43 / 61 / 80</td>
    </tr>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><a href="https://huggingface.co/DJLougen/Harmonic-Hermes-9B" style="color: #666; text-decoration: none;">DJLougen/Harmonic-Hermes-9B</a></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">HermesAgent-20</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">47</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">60 / 45 / 23 / 69 / 38</td>
    </tr>
  </tbody>
</table>

<div style="display: inline-block; padding: 6px 16px; background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; border-radius: 8px; font-weight: 700; font-size: 16px; margin-bottom: 12px;">2. Tool Call Stability - ToolCall-15</div>
This is a ToolCall-15 test set targeting the stability of tool calls, aiming to test the stability of the model in tool calling:

<table style="width: 100%; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <thead>
    <tr>
      <td colspan="4" style="padding: 8px 12px; font-weight: 600; color: #7c3aed; border-bottom: 1px solid rgba(124, 58, 237, 0.2); background: rgba(124, 58, 237, 0.05);">ToolCall-15 Stability Metrics</td>
    </tr>
    <tr style="background: rgba(128, 128, 128, 0.02);">
      <th style="padding: 7px 7px; padding-left: 20px; text-align: left; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Model</th>
      <th style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Test Set</th>
      <th style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Comprehensive Score</th>
      <th style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Dimension Scores (A/B/C/D/E)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><b><a href="https://huggingface.co/Jackrong/Qwopus3.5-9B-coder-GGUF" style="color: #7c3aed; text-decoration: none;">Qwopus3.5-9B-coder</a></b></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">ToolCall-15</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); color: #7c3aed; font-weight: bold;">100</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">100 / 100 / 100 / 100 / 100</td>
    </tr>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><a href="https://huggingface.co/Qwen/Qwen3.5-9B" style="color: #666; text-decoration: none;">Qwen/Qwen3.5-9B</a></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">ToolCall-15</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); color: #7c3aed; font-weight: bold;">100</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">100 / 100 / 100 / 100 / 100</td>
    </tr>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><a href="https://huggingface.co/armand0e/Qwen3.5-9B-Agent" style="color: #666; text-decoration: none;">armand0e/Qwen3.5-9B-Agent</a></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">ToolCall-15</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">93</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">100 / 100 / 100 / 67 / 100</td>
    </tr>
  </tbody>
</table>

<div style="display: inline-block; padding: 6px 16px; background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; border-radius: 8px; font-weight: 700; font-size: 16px; margin-bottom: 12px;">3. Code Debugging & Bug Fixing - BugFind-15</div>
BugFind-15 is a test set containing 15 scenarios from shallow to deep, aiming to evaluate the real debugging capabilities of the model in discovering and fixing syntax, logical errors, and "trap" code in multiple programming languages through deterministic environment runtime verification.

<table style="width: 100%; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <thead>
    <tr>
      <td colspan="4" style="padding: 8px 12px; font-weight: 600; color: #7c3aed; border-bottom: 1px solid rgba(124, 58, 237, 0.2); background: rgba(124, 58, 237, 0.05);">BugFind-15 Performance Metrics</td>
    </tr>
    <tr style="background: rgba(128, 128, 128, 0.02);">
      <th style="padding: 7px 7px; padding-left: 20px; text-align: left; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Model</th>
      <th style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Test Set</th>
      <th style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Comprehensive Score</th>
      <th style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Dimension Scores (A/B/C/D/E)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><b><a href="https://huggingface.co/Jackrong/Qwopus3.5-9B-coder-GGUF" style="color: #7c3aed; text-decoration: none;">Qwopus3.5-9B-coder</a></b></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">BugFind-15</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); color: #7c3aed; font-weight: bold;">79</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">67 / 87 / 100 / 77 / 43</td>
    </tr>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><a href="https://huggingface.co/Jackrong/MLX-Qwen3.5-9B-DeepSeek-V4-Flash-8bit" style="color: #666; text-decoration: none;">Jackrong/MLX-Qwen3.5-9B-DeepSeek-V4-Flash</a></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">BugFind-15</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">75</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">67 / 100 / 67 / 57 / 80</td>
    </tr>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><a href="https://huggingface.co/armand0e/Qwen3.5-9B-Agent" style="color: #666; text-decoration: none;">armand0e/Qwen3.5-9B-Agent</a></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">BugFind-15</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">58</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">29 / 87 / 73 / 20 / 67</td>
    </tr>
  </tbody>
</table>

### 🪐 SWE-bench Verified Performance (Repository-level Coding Capability)
The following shows the comparative performance on **SWE-bench Verified**, which evaluates language models on resolving software engineering issues in real-world open-source repositories:

<table style="width: 100%; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <thead>
    <tr>
      <td colspan="3" style="padding: 8px 12px; font-weight: 600; color: #7c3aed; border-bottom: 1px solid rgba(124, 58, 237, 0.2); background: rgba(124, 58, 237, 0.05);">SWE-bench Verified Performance Metrics</td>
    </tr>
    <tr style="background: rgba(128, 128, 128, 0.02);">
      <th style="padding: 7px 7px; padding-left: 20px; text-align: left; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Model</th>
      <th style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Test Set</th>
      <th style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Comprehensive Score (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><span style="color: #666;">Claude 4.5 Opus</span></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">SWE-bench Verified</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">80.9</td>
    </tr>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><a href="https://huggingface.co/Qwen/Qwen3.5-27B" style="color: #666; text-decoration: none;">Qwen/Qwen3.5-27B</a></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">SWE-bench Verified</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">75.0</td>
    </tr>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><a href="https://huggingface.co/Qwen/Qwen3.6-35B-A3B" style="color: #666; text-decoration: none;">Qwen/Qwen3.6-35B-A3B</a></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">SWE-bench Verified</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">73.4</td>
    </tr>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><b><a href="https://huggingface.co/Jackrong/Qwopus3.5-9B-coder-GGUF" style="color: #7c3aed; text-decoration: none;">Qwopus3.5-9B-coder</a></b></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">SWE-bench Verified</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); color: #7c3aed; font-weight: bold;">53.89</td>
    </tr>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><a href="https://huggingface.co/google/gemma-4-31B-it" style="color: #666; text-decoration: none;">google/gemma-4-31B-it</a></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">SWE-bench Verified</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">52.0</td>
    </tr>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><span style="color: #666;">google/gemma-4-26B-A4B</span></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">SWE-bench Verified</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">45.0 - 48.0</td>
    </tr>
  </tbody>
</table>

---

#### Community-Reported Tool Calling Evaluation

> [!TIP]
> A community user independently evaluated Qwopus3.5-9B-coder on a tool-recall test with up to 31 available tools and an adversarial tool-selection phase containing semantic overlaps and decoy tools.

| Model | Phase 1: Tool Recall | Phase 2: Adversarial Tool Selection |
|---|---:|---:|
| Qwopus3.5-9B-coder | 100% | 27 / 28 (96%) |
| Claude Opus 4.6 | 100% | 27 / 28 (96%) |
| Qwen3.5-9B | 100% | 26 / 28 (93%) |

---

> [!IMPORTANT]
> - ⚙️ All tests were conducted with a temperature of 1 as officially recommended by qwen3.5. All errors and model issues were attempted to be regenerated twice after a test failure. If both attempts fail, it is considered a failure.
> - 🍎 All screenshots of the test interfaces have been uploaded to the image folder in the repository. Click the link below to view and verify:  
> - 🔗 [View Test Screenshots](https://huggingface.co/Jackrong/Qwopus3.5-9B-coder/tree/main/test_images)
> - ❤️ **Kyle Hessling** for his generous hardware and equipment support. You can follow him for more updates on X / Twitter: [@KyleHessling1](https://x.com/KyleHessling1).


---

### 🧪 Core Dataset Usage: Trace Inversion and High-Quality Agent Traces

In order to break through the "reasoning bubble" limitation of the model in actual programming and tool usage, and to endow it with real Agent behavioral capabilities, this model introduced core augmented datasets during training:

#### 1. Reasoning Synthetic Data Combining Trace Inversion
**Currently, based on public information, commercial models such as OpenAI's GPT series and Anthropic's Claude series have very clearly hidden the true internal reasoning chains of their models. For these models, what we can ultimately see in the API or front-end interface can often only be considered a highly compressed "Reasoning Bubble".** 

To break through this limitation, we adopted the **Trace Inversion** technology. This technology utilizes an external "surrogate model" to reconstruct a complete and logically coherent deep reasoning chain based on the "question + final answer + compressed reasoning summary" published by commercial models. The "reasoning bubble", which originally consisted of only a few sentences and logical leaps, is expanded into a high-quality deep learning trace with complete derivation, calculation, and logical verification, providing step-by-step logical learning signals for the model.


![a_high_resolution_infographic_slide_style_figure](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/Jo2bm_rUJQmfK3Na4Uja2.png)




#### 2. GLM-5.1 Agent Real Trace Data: lambda/hermes-agent-reasoning-traces
To significantly enhance the model's execution and coding capabilities in real environments, this model additionally introduced the **`lambda/hermes-agent-reasoning-traces`** dataset.

![Screenshot 2026-05-16 at 5.34.59 PM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/BTusWFqYaOS5GmRYvBuPq.png)


- **Data Source and Scale**: This data subset contains approximately 10,000 high-quality multi-turn Tool Calling Trajectories generated based on the ZhipuAI GLM-5.1 and kimi-4.6 models.
- **Real Agent Behavior**: Unlike traditional synthetic data, these samples represent real Agent conversations. Each sample not only contains the step-by-step reasoning process in the `<think>` tags, but also includes actual tool execution results (rather than fabricated outputs out of thin air).
- **Extensive Domain Coverage**:
  - **Terminal & Coding**: Script writing, code debugging, environment configuration, and data processing.
  - **Repository Tasks**: Involving real code repository work, such as bug fixes, refactoring, and code review.
  - **Browser Automation**: Web navigation, scraping, and form filling.
  - **Agent Tools**: Memory persistence, task delegation, skill management, etc.

By learning these Agent trajectories that contain real feedback and thoughtful processes, Qwopus3.5-9B-coder can exhibit thinking and operational modes closer to human experts when facing complex programming and system operations tasks.

---

## 🗺️ Training Pipeline Overview

The training of this model integrates a phased learning pipeline of **Trace Inversion** data augmentation technology and **high-quality Agent Trajectories data**. Its core logic lies in restoring the highly compressed "reasoning bubble" of commercial models into a deep path for learning, and combining it with real agent operational traces to comprehensively improve the model's logical reasoning and code execution capabilities.

```text
       [ 🗺️ Trace Inversion: Full Process of Data Inversion and "Attack" Distillation ]

  A. Surrogate Model Training
     Open Source Model (GLM-5.1 / DS-V4) ──► Complete Reasoning Chain ──► [ Qwen3-235B Compression ] ──► Reasoning Bubbles
                                       │                                   │
                                       └──────────► [ Training ] ◄─────────┘
                                            (Base: Qwen3-4B-Instruct)
                                            (Result: Trace-Inverter-4B)

  B. Inversion Phase: "Attacking" Claude-4.7-Max
     _______________________________________________________
    |                                                       |
    |  Claude-4.7-Max API ──► Compressed Bubbles + Final Answer |
    |_______________________________________________________|
                      │
                      ▼
    [ 🧠 Trace-Inverter-4B (Logical Reconstructor) ] ────► Synthetic CoT
                      │
                      ▼
    [ 🧩 Data Splicing ] ◄────────── (Original Prompt + Response)
    (Embed the inverted chain of thought into <think> tags, and splice with the original Q&A pair for restoration)
                      │
                      ▼
            (Result: claude-opus-4.6/4.7 Inversion Set)

  C. Final SFT Pipeline
     ___________________________________________
    |                                           |
    |      Base Model (Qwopus3.5-9B-v3.5)       |
    |___________________________________________|
                      │
                      ▼
    [ 📦 Stage 1: Format Establishment and Logic Injection ] ───────► [ 🛠️ Stage 2: Agent Trajectories and Programming Reinforcement ]
     (Integrate inverted reasoning data, stabilize thinking format)        (Introduce GLM-5.1 Agent Trajectories, reinforce interaction and execution)
                      │                                 │
                      │                                 ▼
                      │           __________________________________________________
                      │          |  🔍 Hermes Agent Trace Sample Structure Breakdown (GLM-5.1) |
                      │          |  1. [🛠️ System] -> JSON Tool Definition          |
                      │          |  2. [👤 Human]  -> Initial Task Instruction        |
                      │          |  ┌──────────────────────────────────────────────┐ |
                      │          |  │ 🔁 Multi-turn Loop:                           │ |
                      │          |  │ 3. [🧠 GPT]  -> <think> Logical Reasoning/Reflection │ |
                      │          |  │ 4. [🤖 GPT]  -> Tool Call Execution Action    │ |
                      │          |  │ 5. [⚙️ Tool] -> Real Feedback                 │ |
                      │          |  └──────────────────────────────────────────────┘ |
                      │          |__________________________________________________|
                      │                                 │
                      └────────────────┬────────────────┘
                                       ▼
                      ___________________________________
                     |                                   |
                     |   🌟 Final Model: Qwopus3.5-9B-coder  |
                     |___________________________________|
```


> [!NOTE]
> Because agent trajectory datasets are complex and diverse. The datasets have undergone rigorous cleaning and formatting.

## 🎯 Three-Stage Curriculum Learning

**Qwopus3.5-9B-coder** adopts a phased reasoning data mixture strategy similar to Curriculum Learning, gradually increasing the difficulty and complexity of training signals:

1. **Early Stage (Format Establishment):** Focuses on short-to-medium length reasoning samples with stable formats. The primary goal of this stage is to establish a reliable, structured new reasoning format while avoiding overwhelming the model with extreme complexity.

2. **Middle Stage (Complexity Scaling & Multi-Teacher Distillation):** Gradually increases the proportion of complex reasoning samples from multiple teacher models.
   - The distillation data is sourced from more powerful models whose style distribution closely matches the base model, ensuring that the capability gap is not too wide, thereby achieving efficient learning.

3. **Late Stage (Long-Context Reinforcement & Drift Prevention):** Reinforces reasoning capabilities in long contexts. Crucially, this stage retains **short-sample replay** to ensure the model maintains its short-context instruction-following capability and minimizes capability drift.

---

## 🚀 Context Length and Long-Context Usage

During fine-tuning, this model was trained with a maximum sequence length of **32K tokens**. The training data mixture was also constructed around samples up to **32K tokens**, so the "Context Length Distribution" shown in this model card reflects the fine-tuning data distribution rather than a hard architectural limit.

The model still inherits the native long-context capability of the Qwen3.6 base model. Therefore, longer context windows such as **128K** or **256K** may be available in compatible inference runtimes, depending on the backend and configuration.

For practical long-context inference beyond 32K, especially when using **llama.cpp / GGUF**, it is recommended to enable **RoPE/YaRN scaling** instead of only increasing `n_ctx` / `--ctx-size`. Directly setting a larger context window without RoPE scaling may work in some cases, but it can be less stable and may not achieve the expected long-context performance.

This is consistent with Qwen community guidance for long-context GGUF usage: **128K context generally requires YaRN/RoPE scaling**, and it is not necessarily enabled by default in llama.cpp. For example, Qwen maintainers have noted that "128K context length needs YaRN" and that it should be explicitly enabled when supported by the runtime.  
Reference: https://huggingface.co/Qwen/Qwen2.5-72B-Instruct-GGUF/discussions/2

Community feedback also suggests that RoPE/YaRN scaling can improve long-context stability for this model family. One user reported that, on **HermesAgent-20**, `Qwopus3.6-35B-A3B-v1` performed better when extending from **32K to 128K via RoPE scaling** than when directly setting a **128K context window** without scaling, with scores of **83 vs. 72** in their setup. This result may vary depending on the backend, quantization type, KV cache settings, hardware, and benchmark configuration, but it is consistent with the recommendation to use RoPE/YaRN scaling for contexts beyond 32K.

Example llama.cpp configuration for extending from 32K to 128K:

```bash
./llama-server \
  -m model.gguf \
  --ctx-size 131072 \
  --rope-scaling yarn \
  --rope-scale 4 \
  --yarn-orig-ctx 32768
```

For 256K context, users may need to adjust the scaling factor accordingly and validate the result in their own workload:

```bash
./llama-server \
  -m model.gguf \
  --ctx-size 262144 \
  --rope-scaling yarn \
  --rope-scale 8 \
  --yarn-orig-ctx 32768
```

Please note that long-context behavior may vary depending on the inference backend, quantization type, KV cache settings, available memory, and task type. For best results, users should benchmark their own target workload when using contexts beyond 32K.

---

## 🤝 Collaboration & Training Details

This model is the result of continuous exploration in Agentic AI and reasoning capabilities. 

**Training Infrastructure & Configuration:**
- 🖥️ **Hardware:** Local compute devices / Cloud GPUs (e.g. GB10 / H100 / RTX 5090 / A100)
- ⚙️ **Framework:** Unsloth for efficient fine-tuning

---

## ⚠️ IMPORTANT

> [!CAUTION]
> **Compatibility and Deployment Notice**
> - **Tool Calling Format**: When using this model for tool calling, please ensure that you use a Prompt format and System Prompt that match the training data to activate its Agent capabilities.
> - **Reasoning Output Extraction**: The model's thinking process is typically wrapped in `<think>` and `</think>` tags. When deploying to front-end applications, these tags may need to be parsed and hidden.

---

## 📚 Resources & Guides

👉 **[GitHub Repository: Jackrong-llm-finetuning-guide](https://github.com/R6410418/Jackrong-llm-finetuning-guide.git)**
Visit the repository to dive into our fine-tuning codebase and guides.

---

## 🙏 Acknowledgements

Special thanks to:
- The Qwen team for the strong Qwen3.6 MoE base model.
- Unsloth for efficient fine-tuning frameworks.
- Open-source datasets and community contributors.
- **Kyle Hessling** for his generous hardware and equipment support. You can follow him for more updates on X / Twitter: [@KyleHessling1](https://x.com/KyleHessling1).



---

## 📖 Citation

```bibtex
@misc{jackrong_qwopus35_9b_coder,
  title        = {Qwopus3.5-9B-coder},
  author       = {Jackrong},
  year         = {2026},
  publisher    = {Hugging Face}
}
```