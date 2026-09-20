---
license: apache-2.0
language:
- en
- ja
- zh
- multilingual
pipeline_tag: text-generation
tags:
- gguf
- abliterated
- uncensored
- heretic
- liquidai
- lfm2.5
- agent
base_model: LiquidAI/LFM2.5-2.6B
---

# LFM2.5-2.6B-Heretic-Abliterated-GGUF

This repository contains **GGUF quantizations** of the `LFM2.5-2.6B-Heretic` model. 

The base model, [LiquidAI/LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B), is a highly efficient 2.69 billion parameter model built specifically for on-device agentic workflows, multi-step instruction following, and tool calling. 

This specific iteration has been **abliterated (uncensored)** to remove safety refusals and guardrails, allowing the model to act as a fully compliant, unrestricted local agent while preserving the core intelligence, tool-calling capabilities, and the massive 128K context window of the original model.

## 🩸 Heretic Capabilities (Abliteration Metrics)

The abliteration process targets the refusal directions within the model's residual stream. By neutralizing these vectors, the model's tendency to reject controversial, explicit, or hypothetical prompts is heavily suppressed without lobotomizing its reasoning capabilities.

| Metric | This Model (Heretic) | Original Base Model |
| :----- | :--------: | :---------------------------: |
| **Refusals (100 explicit/restricted prompts)** | **4 / 100** | 97 / 100 |
| **KL Divergence (Quality Degradation)** | **0.0142** | 0.000 |


## 📁 Available GGUF Quantizations

We offer various quantization levels to fit different memory constraints and use cases. Because the base model is incredibly small, you have room to trade size for quality. For general agentic tasks, **Q4_K_M** or **Q5_K_M** are highly recommended.

| Filename | Size | Description |
| :--- | :---: | :--- |
| `LFM2.5-2.6B-heretic-Q8_0.gguf` | 2.87 GB | Near-lossless. Best for complex, tool-heavy agentic workloads. |
| `LFM2.5-2.6B-heretic-Q6_K.gguf` | 2.22 GB | High quality, very low degradation. |
| `LFM2.5-2.6B-heretic-Q5_K_M.gguf` | 1.94 GB | Excellent balance of size and quality. |
| `LFM2.5-2.6B-heretic-Q5_K_S.gguf` | 1.90 GB | Slightly smaller than Q5_K_M. |
| **`LFM2.5-2.6B-heretic-Q4_K_M.gguf`** | **1.67 GB** | **Recommended.** Best balance of size and performance for mobile/edge. |
| `LFM2.5-2.6B-heretic-Q4_K_S.gguf` | 1.60 GB | Fast inference, smaller footprint. |
| `LFM2.5-2.6B-heretic-Q3_K_M.gguf` | 1.37 GB | Smallest footprint. Noticeable perplexity degradation. |

## ⚙️ Base Model Specifications

*   **Architecture:** LFM2.5 (Dense) - 30 layers (22 double-gated short convolution blocks + 8 GQA)
*   **Parameters:** 2.69 Billion
*   **Context Window:** 131,072 tokens (128K)
*   **Vocabulary Size:** 128,000
*   **Languages:** English, Arabic, Chinese, French, German, Italian, Japanese, Korean, Portuguese, Spanish, Vietnamese, Thai, Indonesian, Hindi, Russian, Polish.
*   **Capabilities:** Native tool calling, multi-step instruction following, agentic workflows.

## 🚀 How to Run with `llama.cpp`

You can run these quants entirely offline on your CPU or GPU using [llama.cpp](https://github.com/ggerganov/llama.cpp). Because of the LFM2.5 architecture, this model runs incredibly fast on consumer hardware (e.g., Apple M-series chips and AMD Ryzen).

**Command Line Interface (CLI):**

```bash
# It is highly recommended to use the -cnv flag for the correct chat template
llama-cli -m LFM2.5-2.6B-heretic-Q4_K_M.gguf -p "Write a highly detailed heist story." -n 512 -c 4096 -cnv --temp 0.7