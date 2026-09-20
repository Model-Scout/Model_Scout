---
license: apache-2.0
tags:
  - heretic
  - uncensored
  - decensored
  - mistral-small-4
  - 119b
  - gguf
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

# Mistral-Small-4-119B-2603-heretic GGUf Quantizations

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

## Available Quantizations

Standard quantizations without importance matrix (imatrix) optimization.

| File | Type | Size | BPW | Description |
|------|------|------|-----|-------------|
| `Mistral-Small-4-119B-2603-heretic-BF16.gguf` | BF16 | 221.6 GiB | 16.00 | Base model, highest quality |
| `Mistral-Small-4-119B-2603-heretic-Q8_0.gguf` | Q8_0 | 117.8 GiB | 8.00 | Very high quality |
| `Mistral-Small-4-119B-2603-heretic-Q6_K.gguf` | Q6_K | 91.0 GiB | 6.00 | High quality |
| `Mistral-Small-4-119B-2603-heretic-Q5_K_M.gguf` | Q5_K_M | 78.5 GiB | 5.37 | Good quality/size balance |
| `Mistral-Small-4-119B-2603-heretic-Q5_K_S.gguf` | Q5_K_S | 76.3 GiB | 5.25 | |
| `Mistral-Small-4-119B-2603-heretic-Q4_K_M.gguf` | Q4_K_M | 67.2 GiB | 4.58 | Recommended |
| `Mistral-Small-4-119B-2603-heretic-Q4_K_S.gguf` | Q4_K_S | 63.1 GiB | 4.37 | |
| `Mistral-Small-4-119B-2603-heretic-IQ4_NL.gguf` | IQ4_NL | 63.0 GiB | 4.50 | Non-linear quantization |
| `Mistral-Small-4-119B-2603-heretic-Q3_K_L.gguf` | Q3_K_L | 57.4 GiB | 3.70 | |
| `Mistral-Small-4-119B-2603-heretic-Q3_K_M.gguf` | Q3_K_M | 53.1 GiB | 3.63 | |
| `Mistral-Small-4-119B-2603-heretic-Q3_K_S.gguf` | Q3_K_S | 47.8 GiB | 3.41 | |
| `Mistral-Small-4-119B-2603-heretic-Q2_K.gguf` | Q2_K | 40.4 GiB | 2.96 | Low memory usage |
