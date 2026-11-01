---
base_model: CohereForAI/c4ai-command-r-plus-08-2024
license: cc-by-nc-4.0
model_creator: CohereForAI
model_name: c4ai-command-r-plus-08-2024
quantized_by: Second State Inc.
library_name: transformers
language:
- en
- fr
- de
- es
- it
- pt
- ja
- ko
- zh
- ar
---

<!-- header start -->
<!-- 200823 -->
<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="https://github.com/LlamaEdge/LlamaEdge/raw/dev/assets/logo.svg" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>
<hr style="margin-top: 1.0em; margin-bottom: 1.0em;">
<!-- header end -->

# c4ai-command-r-plus-08-2024-GGUF

## Original Model

[CohereForAI/c4ai-command-r-plus-08-2024](https://huggingface.co/CohereForAI/c4ai-command-r-plus-08-2024)

## Run with LlamaEdge

- LlamaEdge version: coming soon

<!-- - LlamaEdge version: [v0.13.2](https://github.com/LlamaEdge/LlamaEdge/releases/tag/0.13.2) and above

- Prompt template

  - Prompt type: `chatml`

  - Prompt string

    ```text
    <|im_start|>system
    {system_message}<|im_end|>
    <|im_start|>user
    {prompt}<|im_end|>
    <|im_start|>assistant
    ```

- Context size: `128000`

- Run as LlamaEdge service

  ```bash
  wasmedge --dir .:. --nn-preload default:GGML:AUTO:c4ai-command-r-plus-08-2024-Q5_K_M.gguf \
    llama-api-server.wasm \
    --model-name c4ai-command-r-plus-08-2024 \
    --prompt-template chatml \
    --ctx-size 128000
  ```

- Run as LlamaEdge command app

  ```bash
  wasmedge --dir .:. --nn-preload default:GGML:AUTO:c4ai-command-r-plus-08-2024-Q5_K_M.gguf \
    llama-chat.wasm \
    --prompt-template chatml \
    --ctx-size 128000
  ``` -->

## Quantized GGUF Models

| Name | Quant method | Bits | Size | Use case |
| ---- | ---- | ---- | ---- | ----- |
| [c4ai-command-r-plus-08-2024-Q2_K.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q2_K.gguf)     | Q2_K   | 2 | 39.5 GB| smallest, significant quality loss - not recommended for most purposes |
| [c4ai-command-r-plus-08-2024-Q3_K_L-00001-of-00002.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q3_K_L-00001-of-00002.gguf) | Q3_K_L | 3 | 29.8 GB| small, substantial quality loss |
| [c4ai-command-r-plus-08-2024-Q3_K_L-00002-of-00002.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q3_K_L-00002-of-00002.gguf) | Q3_K_L | 3 | 25.6 GB| small, substantial quality loss |
| [c4ai-command-r-plus-08-2024-Q3_K_M-00001-of-00002.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q3_K_M-00001-of-00002.gguf) | Q3_K_M | 3 | 29.1 GB| very small, high quality loss |
| [c4ai-command-r-plus-08-2024-Q3_K_M-00002-of-00002.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q3_K_M-00002-of-00002.gguf) | Q3_K_M | 3 | 21.1 GB| very small, high quality loss |
| [c4ai-command-r-plus-08-2024-Q3_K_S-00001-of-00002.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q3_K_S-00001-of-00002.gguf) | Q3_K_S | 3 | 29.9 GB| very small, high quality loss |
| [c4ai-command-r-plus-08-2024-Q3_K_S-00002-of-00002.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q3_K_S-00002-of-00002.gguf) | Q3_K_S | 3 | 15.9 GB| very small, high quality loss |
| [c4ai-command-r-plus-08-2024-Q4_0-00001-of-00002.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q4_0-00001-of-00002.gguf)     | Q4_0   | 4 | 29.9 GB| legacy; small, very high quality loss - prefer using Q3_K_M |
| [c4ai-command-r-plus-08-2024-Q4_0-00002-of-00002.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q4_0-00002-of-00002.gguf)     | Q4_0   | 4 | 29.3 GB| legacy; small, very high quality loss - prefer using Q3_K_M |
| [c4ai-command-r-plus-08-2024-Q4_K_M-00001-of-00003.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q4_K_M-00001-of-00003.gguf) | Q4_K_M | 4 | 29.9 GB| medium, balanced quality - recommended |
| [c4ai-command-r-plus-08-2024-Q4_K_M-00002-of-00003.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q4_K_M-00002-of-00003.gguf) | Q4_K_M | 4 | 29.9 GB| medium, balanced quality - recommended |
| [c4ai-command-r-plus-08-2024-Q4_K_M-00003-of-00003.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q4_K_M-00003-of-00003.gguf) | Q4_K_M | 4 | 2.99 GB| medium, balanced quality - recommended |
| [c4ai-command-r-plus-08-2024-Q4_K_S-00001-of-00002.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q4_K_S-00001-of-00002.gguf) | Q4_K_S | 4 | 29.9 GB| small, greater quality loss |
| [c4ai-command-r-plus-08-2024-Q4_K_S-00002-of-00002.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q4_K_S-00002-of-00002.gguf) | Q4_K_S | 4 | 29.8 GB| small, greater quality loss |
| [c4ai-command-r-plus-08-2024-Q5_0-00001-of-00003.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q5_0-00001-of-00003.gguf)     | Q5_0   | 5 | 29.9 GB| legacy; medium, balanced quality - prefer using Q4_K_M |
| [c4ai-command-r-plus-08-2024-Q5_0-00002-of-00003.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q5_0-00002-of-00003.gguf)     | Q5_0   | 5 | 30.0 GB| legacy; medium, balanced quality - prefer using Q4_K_M |
| [c4ai-command-r-plus-08-2024-Q5_0-00003-of-00003.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q5_0-00003-of-00003.gguf)     | Q5_0   | 5 | 11.9 GB| legacy; medium, balanced quality - prefer using Q4_K_M |
| [c4ai-command-r-plus-08-2024-Q5_K_M-00001-of-00003.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q5_K_M-00001-of-00003.gguf) | Q5_K_M | 5 | 29.9 GB| large, very low quality loss - recommended |
| [c4ai-command-r-plus-08-2024-Q5_K_M-00002-of-00003.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q5_K_M-00002-of-00003.gguf) | Q5_K_M | 5 | 30.0 GB| large, very low quality loss - recommended |
| [c4ai-command-r-plus-08-2024-Q5_K_M-00003-of-00003.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q5_K_M-00003-of-00003.gguf) | Q5_K_M | 5 | 13.8 GB| large, very low quality loss - recommended |
| [c4ai-command-r-plus-08-2024-Q5_K_S-00001-of-00003.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q5_K_S-00001-of-00003.gguf) | Q5_K_S | 5 | 29.9 GB| large, low quality loss - recommended |
| [c4ai-command-r-plus-08-2024-Q5_K_S-00002-of-00003.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q5_K_S-00002-of-00003.gguf) | Q5_K_S | 5 | 30.0 GB| large, low quality loss - recommended |
| [c4ai-command-r-plus-08-2024-Q5_K_S-00003-of-00003.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q5_K_S-00003-of-00003.gguf) | Q5_K_S | 5 | 11.9 GB| large, low quality loss - recommended |
| [c4ai-command-r-plus-08-2024-Q6_K-00001-of-00003.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q6_K-00001-of-00003.gguf)     | Q6_K   | 6 | 29.7 GB| very large, extremely low quality loss |
| [c4ai-command-r-plus-08-2024-Q6_K-00002-of-00003.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q6_K-00002-of-00003.gguf)     | Q6_K   | 6 | 29.7 GB| very large, extremely low quality loss |
| [c4ai-command-r-plus-08-2024-Q6_K-00003-of-00003.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q6_K-00003-of-00003.gguf)     | Q6_K   | 6 | 25.8 GB| very large, extremely low quality loss |
| [c4ai-command-r-plus-08-2024-Q8_0-00001-of-00004.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q8_0-00001-of-00004.gguf)     | Q8_0   | 8 | 29.9 GB| very large, extremely low quality loss - not recommended |
| [c4ai-command-r-plus-08-2024-Q8_0-00002-of-00004.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q8_0-00002-of-00004.gguf)     | Q8_0   | 8 | 29.9 GB| very large, extremely low quality loss - not recommended |
| [c4ai-command-r-plus-08-2024-Q8_0-00003-of-00004.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q8_0-00003-of-00004.gguf)     | Q8_0   | 8 | 29.6 GB| very large, extremely low quality loss - not recommended |
| [c4ai-command-r-plus-08-2024-Q8_0-00004-of-00004.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-Q8_0-00004-of-00004.gguf)     | Q8_0   | 8 | 20.8 GB| very large, extremely low quality loss - not recommended |
| [c4ai-command-r-plus-08-2024-f16-00001-of-00007.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-f16-00001-of-00007.gguf)       | f16    | 16 | 29.8 GB| |
| [c4ai-command-r-plus-08-2024-f16-00002-of-00007.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-f16-00002-of-00007.gguf)       | f16    | 16 | 30.0 GB| |
| [c4ai-command-r-plus-08-2024-f16-00003-of-00007.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-f16-00003-of-00007.gguf)       | f16    | 16 | 30.0 GB| |
| [c4ai-command-r-plus-08-2024-f16-00004-of-00007.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-f16-00004-of-00007.gguf)       | f16    | 16 | 29.8 GB| |
| [c4ai-command-r-plus-08-2024-f16-00005-of-00007.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-f16-00005-of-00007.gguf)       | f16    | 16 | 30.0 GB| |
| [c4ai-command-r-plus-08-2024-f16-00006-of-00007.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-f16-00006-of-00007.gguf)       | f16    | 16 | 29.8 GB| |
| [c4ai-command-r-plus-08-2024-f16-00007-of-00007.gguf](https://huggingface.co/second-state/c4ai-command-r-plus-08-2024-GGUF/blob/main/c4ai-command-r-plus-08-2024-f16-00007-of-00007.gguf)       | f16    | 16 | 28.3 GB| |

*Quantized with llama.cpp b3613*