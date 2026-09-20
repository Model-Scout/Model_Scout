---
license: apache-2.0
tags:
  - heretic
  - uncensored
  - decensored
  - mistral-small-4
  - 119b
  - gguf
  - imatrix
language:
  - en
  - fr
  - de
  - es
  - pt
  - it
  - ja
  - ko
  - zh
  - ar
  - fa
  - id
  - ms
  - ne
  - pl
  - ro
  - sr
  - sv
  - tr
  - uk
  - vi
  - hi
  - bn
pipeline_tag: image-text-to-text
base_model: darkc0de/Mistral-Small-4-119B-2603-heretic
datasets:
  - bartowski1182/calibration_datav5.txt
---

# Mistral-Small-4-119B-2603-heretic GGUf Quantizations (imatrix)

## Model Information

| Field | Value |
|-------|-------|
| **Base Model** | [Mistral Small 4 119B 2603](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603) by Mistralai |
| **Heretic Model** | [Mistral Small 4 119B 2603 Heretic](https://huggingface.co/darkc0de/Mistral-Small-4-119B-2603-heretic) by darkc0de |
| **Architecture** | Mistral4 (MoE, MLA attention) |
| **Total Parameters** | 119B |
| **Active Parameters** | 6.5B per token |
| **Experts** | 128 experts, 4 active |
| **Context Length** | 256k tokens |

## Key Features

- **MoE Architecture**: 128 experts with 4 active per token (6.5B activated parameters)
- **Multimodal**: Accepts both text and image input, produces text output
- **Reasoning Mode**: Toggle between fast instant reply and reasoning mode with test-time compute
- **Function Calling**: Native function calling with JSON output
- **Agentic**: Best-in-class agentic capabilities
- **System Prompts**: Strong adherence and support for system prompts
- **Speed-Optimized**: Best-in-class performance and speed
- **Large Context Window**: 256k context length supported
- **Apache 2.0 License**: Open-source for commercial and non-commercial use
- **Multilingual**: Supports English, French, Spanish, German, Italian, Portuguese, Dutch, Chinese, Japanese, Korean, Arabic and more

## Heretic Model Statistics

| Metric | Value |
|--------|-------|
| KL Divergence | 0.0167 (0 for refusable tokens by definition) |
| Refusals | 27/100 (98/100 original model) |

## imatrix Quantizations

These models were quantized using an importance matrix (`imatrix`) computed from a reference corpus. The imatrix helps preserve quality for important token patterns, typically yielding better results at low bitrates compared to standard quantization.

The `imatrix` file was generated using the Q8_0 quantization of the heretic model on the following calibration dataset:

> **Calibration Dataset**: [bartowski1182/calibration_datav5.txt](https://gist.github.com/bartowski1182/82ae9b520227f57d79ba04add13d0d0d#file-calibration_datav5-txt)
> **Reference imatrix**: [Mistral-Small-4-119B-2603-heretic-imatrix.gguf](Mistral-Small-4-119B-2603-heretic-imatrix.gguf) (118 MB)

## Available Quantizations

| File | Type | Size | BPW | Description |
|------|------|------|-----|-------------|
| `Mistral-Small-4-119B-2603-heretic-i1-Q6_K.gguf` | Q6_K | 91.0 GiB | 6.00 | High quality |
| `Mistral-Small-4-119B-2603-heretic-i1-Q5_K_M.gguf` | Q5_K_M | 78.5 GiB | 5.37 | Recommended |
| `Mistral-Small-4-119B-2603-heretic-i1-Q4_K_M.gguf` | Q4_K_M | 67.2 GiB | 4.58 | |
| `Mistral-Small-4-119B-2603-heretic-i1-IQ4_NL.gguf` | IQ4_NL | 62.5 GiB | 4.50 | Non-linear quantization |
| `Mistral-Small-4-119B-2603-heretic-i1-Q3_K_L.gguf` | Q3_K_L | 57.4 GiB | 3.70 | |
| `Mistral-Small-4-119B-2603-heretic-i1-Q3_K_M.gguf` | Q3_K_M | 53.1 GiB | 3.63 | |
| `Mistral-Small-4-119B-2603-heretic-i1-Q3_K_S.gguf` | Q3_K_S | 47.8 GiB | 3.41 | |
| `Mistral-Small-4-119B-2603-heretic-i1-IQ4_XS.gguf` | IQ4_XS | 59.1 GiB | 4.25 | Linear variant |
| `Mistral-Small-4-119B-2603-heretic-i1-Q2_K.gguf` | Q2_K | 40.4 GiB | 2.96 | |
| `Mistral-Small-4-119B-2603-heretic-i1-IQ3_XS.gguf` | IQ3_XS | 45.3 GiB | 3.30 | |
| `Mistral-Small-4-119B-2603-heretic-i1-IQ3_XXS.gguf` | IQ3_XXS | 42.7 GiB | 3.06 | |
| `Mistral-Small-4-119B-2603-heretic-i1-IQ2_S.gguf` | IQ2_S | 32.8 GiB | 2.50 | |
| `Mistral-Small-4-119B-2603-heretic-i1-IQ2_XS.gguf` | IQ2_XS | 32.4 GiB | 2.34 | |
| `Mistral-Small-4-119B-2603-heretic-i1-IQ2_XXS.gguf` | IQ2_XXS | 29.0 GiB | 2.10 | Lowest memory usage |
