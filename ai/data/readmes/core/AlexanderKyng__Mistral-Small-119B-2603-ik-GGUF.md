---
license: apache-2.0
datasets:
- ggml-org/ci
metrics:
- perplexity
base_model:
- mistralai/Mistral-Small-4-119B-2603
pipeline_tag: text-generation
language:
- ar
- en
- fr
- es
- de
- it
- pt
- nl
- ja
- ko
- zh
tags:
- ik_llama.cpp
- llama.cpp
---

# Mistral-Small-4-119B-2603 GGUF (ik_llama)

This repository provides [ik_llama](https://github.com/ikawrakow/ik_llama.cpp) optimized GGUF quantizations for the mistralai/Mistral-Small-4-119B-2603 model.

## Optimization and Importance Matrix
These files were generated using the [ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp) fork, which offers row interleaved formats (R4) specifically designed to minimize degradation in MoE architectures. I send my biggest thanks to the author [ikawrakow](https://github.com/ikawrakow) for developing and maintaining this tool.

To maximize precision, an importance matrix (iMatrix) was computed prior to quantization. This calculation was performed on a RunPod infrastructure equipped with 3 NVIDIA A100 80GB accelerators, ingesting the calibration_data_v5_rc.txt dataset provided by [tristandruyen](https://gist.github.com/tristandruyen/9e207a95c7d75ddf37525d353e00659c).

## Perplexity Scores
All tests were performed on the [`wikitext-2`](https://huggingface.co/datasets/ggml-org/ci) dataset using a context window of 1024 tokens and a batch size of 512. 

<table>
  <thead>
    <tr>
      <th>Model Format</th>
      <th>Perplexity (PPL)</th>
      <th>Size (GiB)</th>
      <th>Bits per Weight (BPW)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>BF16 (Unsloth Base)</td>
      <td>5.3035</td>
      <td>221.64</td>
      <td>16.00</td>
    </tr>
    <tr>
      <td>IQ5_K_R4 (ik_llama)</td>
      <td>5.3431</td>
      <td>82</td>
      <td>5.51</td>
    </tr>
    <tr>
      <td>UD_Q4_K_S (Unsloth)</td>
      <td>5.3883</td>
      <td>69.30</td>
      <td>~ 4.50</td>
    </tr>
    <tr>
      <td>IQ4_K_R4 (ik_llama)</td>
      <td>5.4242</td>
      <td>67.2</td>
      <td>4.31</td>
    </tr>
  </tbody>
</table>

## Vision and Multimodality Note
This model features vision capabilities. You may find the original model's .mmproj file in the ["Files and versions"](https://huggingface.co/AlexanderKyng/Mistral-Small-119B-2603-ik-GGUF/tree/main) tab.

### Credits
Original model: [mistralai/Mistral-Small-4-119B-2603](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603)




# ================== Original Description ==================

Mistral Small 4 is a powerful hybrid model capable of acting as both a general instruction model and a reasoning model. It unifies the capabilities of three different model families—**Instruct**, **Reasoning** (previously called Magistral), and **Devstral**—into a single, unified model.

With its multimodal capabilities, efficient architecture, and flexible mode switching, it is a powerful general-purpose model for any task. In a latency-optimized setup, Mistral Small 4 achieves a **40% reduction in end-to-end completion time**, and in a throughput-optimized setup, it handles **3x more requests per second** compared to Mistral Small 3.

To further improve efficiency you can either take advantages of:
- Speculative decoding thanks to our trained eagle head [`mistralai/Mistral-Small-4-119B-2603-eagle`](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603-eagle).
- 4 bit float precision quantization thanks to our NVFP4 checkpoint [`mistralai/Mistral-Small-4-119B-2603-NVFP4`](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603-NVFP4).

## Key Features

Mistral Small 4 includes the following architectural choices:

- **MoE**: 128 experts, 4 active.
- **119B parameters**, with **6.5B activated per token**.
- **256k context length**.
- **Multimodal input**: Accepts both text and image input, with text output.
- **Instruct and Reasoning functionalities** with function calls (reasoning effort configurable per request).

Mistral Small 4 offers the following capabilities:

- **Reasoning Mode**: Toggle between fast instant reply mode and reasoning mode, boosting performance with test-time compute when requested.
- **Vision**: Analyzes images and provides insights based on visual content, in addition to text.
- **Multilingual**: Supports dozens of languages, including English, French, Spanish, German, Italian, Portuguese, Dutch, Chinese, Japanese, Korean, and Arabic.
- **System Prompt**: Strong adherence and support for system prompts.
- **Agentic**: Best-in-class agentic capabilities with native function calling and JSON output.
- **Speed-Optimized**: Delivers best-in-class performance and speed.
- **Apache 2.0 License**: Open-source license for both commercial and non-commercial use.
- **Large Context Window**: Supports a 256k context window.

## Recommended Settings

- **Reasoning Effort**:
  - `'none'` → Do not use reasoning
  - `'high'` → Use reasoning (recommended for complex prompts)
  Use `reasoning_effort="high"` for complex tasks
- **Temperature**: 0.7 for `reasoning_effort="high"`. Temp between 0.0 and 0.7 for `reasoning_effort="none"` depending on task.

## Use Cases

Mistral Small 4 is designed for general chat assistants, coding, agentic tasks, and reasoning tasks (with reasoning mode toggled). Its multimodal capabilities also enable document and image understanding for data extraction and analysis.

Its capabilities are ideal for:
- Developers interested in coding and agentic capabilities for SWE automation and codebase exploration.
- Enterprises seeking general chat assistants, agents, and document understanding.
- Researchers leveraging its math and research capabilities.

Mistral Small 4 is also well-suited for customization and fine-tuning for more specialized tasks.

### Examples
- General chat assistant
- Document parsing and extraction
- Coding agent
- Research assistant
- Customization & fine-tuning
- And more...

## Benchmarks

### Comparison with internal models

Depending on your tasks you can trigger reasoning thanks to the support of the **per-request** parameter `reasoning_effort`. Set it to:
- `reasoning_effort="none"`: Fast, lightweight responses for everyday tasks, equivalent to the same chat style of [`mistralai/Mistral-Small-3.2-24B-Instruct-2506`](https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506).
- `reasoning_effort="high"`: Deep, step-by-step reasoning for complex problems, with equivalent verbosity to previous Magistral models such as [`mistralai/Magistral-Small-2509`](https://huggingface.co/mistralai/Magistral-Small-2509).

![Internal benchmark](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603/resolve/main/images/image2.png)

#### Comparing Reasoning Models

![Internal benchmark - Reasoning](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603/resolve/main/images/image3.png)


### Comparison with other models

Mistral Small 4 with reasoning achieves competitive scores, matching or surpassing GPT-OSS 120B across all three benchmarks while generating significantly
shorter outputs. On AA LCR, Mistral Small 4 scores **0.72** with just **1.6K characters**, whereas Qwen models require **3.5-4x more output** (5.8-6.1K)
for comparable performance. On LiveCodeBench, Mistral Small 4 outperforms GPT-OSS 120B while producing **20% less output**.
This efficiency reduces latency, inference costs, and improves user experience.

![Comparison benchmark - LCR](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603/resolve/main/images/lcr.png)
![Comparison benchmark - LiveCodeBench](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603/resolve/main/images/livecode.png)
![Comparison benchmark - AIME25](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603/resolve/main/images/aime.png)

## Usage

You can find Mistral Small 4 support on multiple libraries for inference and fine-tuning. We here thank everyone contributors and maintainers that helped us making it happen.

## License

This model is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0.txt).

*You must not use this model in a manner that infringes, misappropriates, or violates any third party’s rights, including intellectual property rights.*
