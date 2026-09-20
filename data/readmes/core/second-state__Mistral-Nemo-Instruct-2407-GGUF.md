---
license: apache-2.0
model_name: Mistral-Nemo-Instruct-2407
base_model: mistralai/Mistral-Nemo-Instruct-2407
inference: false
model_creator: mistralai
quantized_by: Second State Inc.
language:
  - en
  - fr
  - de
  - es
  - it
  - pt
  - ru
  - zh
  - ja
---

<!-- header start -->
<!-- 200823 -->
<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="https://github.com/LlamaEdge/LlamaEdge/raw/dev/assets/logo.svg" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>
<hr style="margin-top: 1.0em; margin-bottom: 1.0em;">
<!-- header end -->

# Mistral-Nemo-Instruct-2407-GGUF

## Original Model

[mistralai/Mistral-Nemo-Instruct-2407](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407)

## Run with LlamaEdge

- LlamaEdge version: [v0.12.4](https://github.com/LlamaEdge/LlamaEdge/releases/tag/0.12.4)

- Prompt template

  - Prompt type: `mistral-instruct`

  - Prompt string

    ```text
    <s>[INST] {user_message_1} [/INST]{assistant_message_1}</s>[INST] {user_message_2} [/INST]{assistant_message_2}</s>
    ```

- Context size: `128000`

- Run as LlamaEdge service

  ```bash
  wasmedge --dir .:. --nn-preload default:GGML:AUTO:Mistral-Nemo-Instruct-2407-Q5_K_M.gguf \
    llama-api-server.wasm \
    --prompt-template mistral-instruct \
    --ctx-size 128000 \
    --model-name Mistral-Nemo-Instruct-2407
  ```

- Run as LlamaEdge command app

  ```bash
  wasmedge --dir .:. --nn-preload default:GGML:AUTO:Mistral-Nemo-Instruct-2407-Q5_K_M.gguf \
    llama-chat.wasm \
    --prompt-template mistral-instruct \
    --ctx-size 128000
  ```

## Quantized GGUF Models

| Name | Quant method | Bits | Size | Use case |
| ---- | ---- | ---- | ---- | ----- |
| [Mistral-Nemo-Instruct-2407-Q2_K.gguf](https://huggingface.co/second-state/Mistral-Nemo-Instruct-2407-GGUF/blob/main/Mistral-Nemo-Instruct-2407-Q2_K.gguf)         | Q2_K   | 2 | 4.79 GB| smallest, significant quality loss - not recommended for most purposes |
| [Mistral-Nemo-Instruct-2407-Q3_K_L.gguf](https://huggingface.co/second-state/Mistral-Nemo-Instruct-2407-GGUF/blob/main/Mistral-Nemo-Instruct-2407-Q3_K_L.gguf)     | Q3_K_L | 3 | 6.56 GB| small, substantial quality loss |
| [Mistral-Nemo-Instruct-2407-Q3_K_M.gguf](https://huggingface.co/second-state/Mistral-Nemo-Instruct-2407-GGUF/blob/main/Mistral-Nemo-Instruct-2407-Q3_K_M.gguf)     | Q3_K_M | 3 | 6.08 GB| very small, high quality loss |
| [Mistral-Nemo-Instruct-2407-Q3_K_S.gguf](https://huggingface.co/second-state/Mistral-Nemo-Instruct-2407-GGUF/blob/main/Mistral-Nemo-Instruct-2407-Q3_K_S.gguf)     | Q3_K_S | 3 | 5.53 GB| very small, high quality loss |
| [Mistral-Nemo-Instruct-2407-Q4_0.gguf](https://huggingface.co/second-state/Mistral-Nemo-Instruct-2407-GGUF/blob/main/Mistral-Nemo-Instruct-2407-Q4_0.gguf)         | Q4_0   | 4 | 7.07 GB| legacy; small, very high quality loss - prefer using Q3_K_M |
| [Mistral-Nemo-Instruct-2407-Q4_K_M.gguf](https://huggingface.co/second-state/Mistral-Nemo-Instruct-2407-GGUF/blob/main/Mistral-Nemo-Instruct-2407-Q4_K_M.gguf)     | Q4_K_M | 4 | 7.48 GB| medium, balanced quality - recommended |
| [Mistral-Nemo-Instruct-2407-Q4_K_S.gguf](https://huggingface.co/second-state/Mistral-Nemo-Instruct-2407-GGUF/blob/main/Mistral-Nemo-Instruct-2407-Q4_K_S.gguf)     | Q4_K_S | 4 | 7.12 GB| small, greater quality loss |
| [Mistral-Nemo-Instruct-2407-Q5_0.gguf](https://huggingface.co/second-state/Mistral-Nemo-Instruct-2407-GGUF/blob/main/Mistral-Nemo-Instruct-2407-Q5_0.gguf)         | Q5_0   | 5 | 8.52 GB| legacy; medium, balanced quality - prefer using Q4_K_M |
| [Mistral-Nemo-Instruct-2407-Q5_K_M.gguf](https://huggingface.co/second-state/Mistral-Nemo-Instruct-2407-GGUF/resolve/main/Mistral-Nemo-Instruct-2407-Q5_K_M.gguf)  | Q5_K_M | 5 | 8.73 GB| large, very low quality loss - recommended |
| [Mistral-Nemo-Instruct-2407-Q5_K_S.gguf](https://huggingface.co/second-state/Mistral-Nemo-Instruct-2407-GGUF/blob/main/Mistral-Nemo-Instruct-2407-Q5_K_S.gguf)     | Q5_K_S | 5 | 8.52 GB| large, low quality loss - recommended |
| [Mistral-Nemo-Instruct-2407-Q6_K.gguf](https://huggingface.co/second-state/Mistral-Nemo-Instruct-2407-GGUF/blob/main/Mistral-Nemo-Instruct-2407-Q6_K.gguf)         | Q6_K   | 6 | 10.1 GB| very large, extremely low quality loss |
| [Mistral-Nemo-Instruct-2407-Q8_0.gguf](https://huggingface.co/second-state/Mistral-Nemo-Instruct-2407-GGUF/blob/main/Mistral-Nemo-Instruct-2407-Q8_0.gguf)         | Q8_0   | 8 | 13.0 GB| very large, extremely low quality loss - not recommended |
| [Mistral-Nemo-Instruct-2407-f16.gguf](https://huggingface.co/second-state/Mistral-Nemo-Instruct-2407-GGUF/blob/main/Mistral-Nemo-Instruct-2407-f16.gguf)           | f16   | 16 | 24.5 GB|  |

*Quantized with llama.cpp b3438.*