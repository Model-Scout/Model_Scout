---
base_model: microsoft/Phi-4-mini-instruct
license: mit
license_link: https://huggingface.co/microsoft/Phi-4-mini-instruct/resolve/main/LICENSE
language:
- "multilingual"
- "ar"
- "zh"
- "cs"
- "da"
- "nl"
- "en"
- "fi"
- "fr"
- "de"
- "he"
- "hu"
- "it"
- "ja"
- "ko"
- "no"
- "pl"
- "pt"
- "ru"
- "es"
- "sv"
- "th"
- "tr"
- "uk"
pipeline_tag: text-generation
library_name: transformers
model_creator: Microsoft
model_name: Phi-4-mini-instruct
quantized_by: Second State Inc.
tags:
- nlp
- code
---

<!-- header start -->
<!-- 200823 -->
<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="https://github.com/LlamaEdge/LlamaEdge/raw/dev/assets/logo.svg" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>
<hr style="margin-top: 1.0em; margin-bottom: 1.0em;">
<!-- header end -->

# Phi-4-mini-instruct-GGUF

## Original Model

[microsoft/Phi-4-mini-instruct](https://huggingface.co/microsoft/Phi-4-mini-instruct)

## Run with LlamaEdge

- LlamaEdge version: [v0.16.9](https://github.com/LlamaEdge/LlamaEdge/releases/tag/0.16.9) and above

- Prompt template

  - Prompt type: `phi-4-chat`

  - Prompt string

    ```text
    <|im_start|>system<|im_sep|>
    {system_message}<|im_end|>
    <|im_start|>user<|im_sep|>
    {user_message}<|im_end|>
    <|im_start|>assistant<|im_sep|>
    ```

- Context size: `128000`

- Run as LlamaEdge service

  ```bash
  wasmedge --dir .:. --nn-preload default:GGML:AUTO:Phi-4-mini-instruct-Q5_K_M.gguf \
    llama-api-server.wasm \
    --prompt-template phi-4-chat \
    --ctx-size 128000 \
    --model-name phi-4-mini
  ```

- Run as LlamaEdge command app

  ```bash
  wasmedge --dir .:. --nn-preload default:GGML:AUTO:Phi-4-mini-instruct-Q5_K_M.gguf \
    llama-chat.wasm \
    --prompt-template phi-4-chat \
    --ctx-size 128000
  ```

## Quantized GGUF Models

| Name | Quant method | Bits | Size | Use case |
| ---- | ---- | ---- | ---- | ----- |
| [Phi-4-mini-instruct-Q2_K.gguf](https://huggingface.co/second-state/Phi-4-mini-instruct-GGUF/blob/main/Phi-4-mini-instruct-Q2_K.gguf)     | Q2_K   | 2 | 1.68 GB| smallest, significant quality loss - not recommended for most purposes |
| [Phi-4-mini-instruct-Q3_K_L.gguf](https://huggingface.co/second-state/Phi-4-mini-instruct-GGUF/blob/main/Phi-4-mini-instruct-Q3_K_L.gguf) | Q3_K_L | 3 | 2.25 GB| small, substantial quality loss |
| [Phi-4-mini-instruct-Q3_K_M.gguf](https://huggingface.co/second-state/Phi-4-mini-instruct-GGUF/blob/main/Phi-4-mini-instruct-Q3_K_M.gguf) | Q3_K_M | 3 | 2.12 GB| very small, high quality loss |
| [Phi-4-mini-instruct-Q3_K_S.gguf](https://huggingface.co/second-state/Phi-4-mini-instruct-GGUF/blob/main/Phi-4-mini-instruct-Q3_K_S.gguf) | Q3_K_S | 3 | 1.90 GB| very small, high quality loss |
| [Phi-4-mini-instruct-Q4_0.gguf](https://huggingface.co/second-state/Phi-4-mini-instruct-GGUF/blob/main/Phi-4-mini-instruct-Q4_0.gguf)     | Q4_0   | 4 | 2.33 GB| legacy; small, very high quality loss - prefer using Q3_K_M |
| [Phi-4-mini-instruct-Q4_K_M.gguf](https://huggingface.co/second-state/Phi-4-mini-instruct-GGUF/blob/main/Phi-4-mini-instruct-Q4_K_M.gguf) | Q4_K_M | 4 | 2.49 GB| medium, balanced quality - recommended |
| [Phi-4-mini-instruct-Q4_K_S.gguf](https://huggingface.co/second-state/Phi-4-mini-instruct-GGUF/blob/main/Phi-4-mini-instruct-Q4_K_S.gguf) | Q4_K_S | 4 | 2.34 GB| small, greater quality loss |
| [Phi-4-mini-instruct-Q5_0.gguf](https://huggingface.co/second-state/Phi-4-mini-instruct-GGUF/blob/main/Phi-4-mini-instruct-Q5_0.gguf)     | Q5_0   | 5 | 2.73 GB| legacy; medium, balanced quality - prefer using Q4_K_M |
| [Phi-4-mini-instruct-Q5_K_M.gguf](https://huggingface.co/second-state/Phi-4-mini-instruct-GGUF/blob/main/Phi-4-mini-instruct-Q5_K_M.gguf) | Q5_K_M | 5 | 2.85 GB| large, very low quality loss - recommended |
| [Phi-4-mini-instruct-Q5_K_S.gguf](https://huggingface.co/second-state/Phi-4-mini-instruct-GGUF/blob/main/Phi-4-mini-instruct-Q5_K_S.gguf) | Q5_K_S | 5 | 2.73 GB| large, low quality loss - recommended |
| [Phi-4-mini-instruct-Q6_K.gguf](https://huggingface.co/second-state/Phi-4-mini-instruct-GGUF/blob/main/Phi-4-mini-instruct-Q6_K.gguf)     | Q6_K   | 6 | 3.16 GB| very large, extremely low quality loss |
| [Phi-4-mini-instruct-Q8_0.gguf](https://huggingface.co/second-state/Phi-4-mini-instruct-GGUF/blob/main/Phi-4-mini-instruct-Q8_0.gguf)     | Q8_0   | 8 | 4.08 GB| very large, extremely low quality loss - not recommended |
| [Phi-4-mini-instruct-f16.gguf](https://huggingface.co/second-state/Phi-4-mini-instruct-GGUF/blob/main/Phi-4-mini-instruct-f16.gguf)     | f16   | 16 | 7.68 GB|  |

*Quantized with llama.cpp b4792.*
