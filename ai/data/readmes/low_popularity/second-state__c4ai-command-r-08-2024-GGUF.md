---
base_model: CohereForAI/c4ai-command-r-08-2024
license: cc-by-nc-4.0
model_creator: CohereForAI
model_name: c4ai-command-r-08-2024
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

# c4ai-command-r-08-2024-GGUF

## Original Model

[CohereForAI/c4ai-command-r-08-2024](https://huggingface.co/CohereForAI/c4ai-command-r-08-2024)

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
  wasmedge --dir .:. --nn-preload default:GGML:AUTO:c4ai-command-r-08-2024-Q5_K_M.gguf \
    llama-api-server.wasm \
    --model-name c4ai-command-r-08-2024 \
    --prompt-template chatml \
    --ctx-size 128000
  ```

- Run as LlamaEdge command app

  ```bash
  wasmedge --dir .:. --nn-preload default:GGML:AUTO:c4ai-command-r-08-2024-Q5_K_M.gguf \
    llama-chat.wasm \
    --prompt-template chatml \
    --ctx-size 128000
  ``` -->

## Quantized GGUF Models

| Name | Quant method | Bits | Size | Use case |
| ---- | ---- | ---- | ---- | ----- |
| [c4ai-command-r-08-2024-Q2_K.gguf](https://huggingface.co/second-state/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q2_K.gguf)     | Q2_K   | 2 | 12.8 GB| smallest, significant quality loss - not recommended for most purposes |
| [c4ai-command-r-08-2024-Q3_K_L.gguf](https://huggingface.co/second-state/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q3_K_L.gguf) | Q3_K_L | 3 | 17.6 GB| small, substantial quality loss |
| [c4ai-command-r-08-2024-Q3_K_M.gguf](https://huggingface.co/second-state/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q3_K_M.gguf) | Q3_K_M | 3 | 16.2 GB| very small, high quality loss |
| [c4ai-command-r-08-2024-Q3_K_S.gguf](https://huggingface.co/second-state/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q3_K_S.gguf) | Q3_K_S | 3 | 14.7 GB| very small, high quality loss |
| [c4ai-command-r-08-2024-Q4_0.gguf](https://huggingface.co/second-state/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q4_0.gguf)     | Q4_0   | 4 | 18.7 GB| legacy; small, very high quality loss - prefer using Q3_K_M |
| [c4ai-command-r-08-2024-Q4_K_M.gguf](https://huggingface.co/second-state/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q4_K_M.gguf) | Q4_K_M | 4 | 19.8 GB| medium, balanced quality - recommended |
| [c4ai-command-r-08-2024-Q4_K_S.gguf](https://huggingface.co/second-state/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q4_K_S.gguf) | Q4_K_S | 4 | 18.8 GB| small, greater quality loss |
| [c4ai-command-r-08-2024-Q5_0.gguf](https://huggingface.co/second-state/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q5_0.gguf)     | Q5_0   | 5 | 22.5 GB| legacy; medium, balanced quality - prefer using Q4_K_M |
| [c4ai-command-r-08-2024-Q5_K_M.gguf](https://huggingface.co/second-state/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q5_K_M.gguf) | Q5_K_M | 5 | 23.1 GB| large, very low quality loss - recommended |
| [c4ai-command-r-08-2024-Q5_K_S.gguf](https://huggingface.co/second-state/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q5_K_S.gguf) | Q5_K_S | 5 | 22.5 GB| large, low quality loss - recommended |
| [c4ai-command-r-08-2024-Q6_K.gguf](https://huggingface.co/second-state/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q6_K.gguf)     | Q6_K   | 6 | 26.5 GB| very large, extremely low quality loss |
| [c4ai-command-r-08-2024-Q8_0.gguf](https://huggingface.co/second-state/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-Q8_0.gguf)     | Q8_0   | 8 | 34.3 GB| very large, extremely low quality loss - not recommended |
| [c4ai-command-r-08-2024-f16-00001-of-00003.gguf](https://huggingface.co/second-state/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-f16-00001-of-00003.gguf)       | f16    | 16 | 29.9 GB| |
| [c4ai-command-r-08-2024-f16-00002-of-00003.gguf](https://huggingface.co/second-state/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-f16-00002-of-00003.gguf)       | f16    | 16 | 29.8 GB| |
| [c4ai-command-r-08-2024-f16-00003-of-00003.gguf](https://huggingface.co/second-state/c4ai-command-r-08-2024-GGUF/blob/main/c4ai-command-r-08-2024-f16-00003-of-00003.gguf)       | f16    | 16 | 4.93 GB| |

*Quantized with llama.cpp b3613*