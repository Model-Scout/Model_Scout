---
license: other
license_name: mrl
license_link: https://mistral.ai/licenses/MRL-0.1.md
model_name: Mistral-Large-Instruct-2407
base_model: mistralai/Mistral-Large-Instruct-2407
model_creator: mistralai
quantized_by: Second State Inc.
language:
  - en
  - fr
  - de
  - es
  - it
  - pt
  - zh
  - ja
  - ru
  - ko
---

<!-- header start -->
<!-- 200823 -->
<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="https://github.com/LlamaEdge/LlamaEdge/raw/dev/assets/logo.svg" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>
<hr style="margin-top: 1.0em; margin-bottom: 1.0em;">
<!-- header end -->

# Mistral-Large-Instruct-2407-GGUF

## Original Model

[mistralai/Mistral-Large-Instruct-2407](https://huggingface.co/mistralai/Mistral-Large-Instruct-2407)

## Run with LlamaEdge

- LlamaEdge version: [v0.13.0](https://github.com/LlamaEdge/LlamaEdge/releases/tag/0.13.0)

- Prompt template

  - Prompt type: `mistral-instruct`

  - Prompt string

    ```text
    <s>[INST] {user_message_1} [/INST]{assistant_message_1}</s>[INST] {user_message_2} [/INST]{assistant_message_2}</s>
    ```

- Context size: `128000`

- Run as LlamaEdge service

  ```bash
  wasmedge --dir .:. --nn-preload default:GGML:AUTO:Mistral-Large-Instruct-2407-Q5_K_M.gguf \
      llama-api-server.wasm \
      --prompt-template mistral-instruct \
      --ctx-size 128000 \
      --model-name Mistral-Large-Instruct-2407
  ```

- Run as LlamaEdge command app

  ```bash
  wasmedge --dir .:. --nn-preload default:GGML:AUTO:Mistral-Large-Instruct-2407-Q5_K_M.gguf \
    llama-chat.wasm \
    --prompt-template mistral-instruct \
    --ctx-size 32000
  ```

## Quantized GGUF Models

| Name | Quant method | Bits | Size | Use case |
| ---- | ---- | ---- | ---- | ----- |
| [Mistral-Large-Instruct-2407-Q2_K.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q2_K.gguf)     | Q2_K   | 2 | 45.2 GB| smallest, significant quality loss - not recommended for most purposes |
| [Mistral-Large-Instruct-2407-Q3_K_L-00001-of-00003.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q3_K_L-00001-of-00003.gguf) | Q3_K_L | 3 | 29.9 GB| small, substantial quality loss |
| [Mistral-Large-Instruct-2407-Q3_K_L-00002-of-00003.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q3_K_L-00002-of-00003.gguf) | Q3_K_L | 3 | 29.9 GB| small, substantial quality loss |
| [Mistral-Large-Instruct-2407-Q3_K_L-00003-of-00003.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q3_K_L-00003-of-00003.gguf) | Q3_K_L | 3 | 4.70 GB| small, substantial quality loss |
| [Mistral-Large-Instruct-2407-Q3_K_M-00001-of-00002.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q3_K_M-00001-of-00002.gguf) | Q3_K_M | 3 | 29.9 GB| very small, high quality loss |
| [Mistral-Large-Instruct-2407-Q3_K_M-00002-of-00002.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q3_K_M-00002-of-00002.gguf) | Q3_K_M | 3 | 29.2 GB| very small, high quality loss |
| [Mistral-Large-Instruct-2407-Q3_K_S-00001-of-00002.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q3_K_S-00001-of-00002.gguf) | Q3_K_S | 3 | 29.9 GB| very small, high quality loss |
| [Mistral-Large-Instruct-2407-Q3_K_S-00002-of-00002.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q3_K_S-00002-of-00002.gguf) | Q3_K_S | 3 | 29.2 GB| very small, high quality loss |
| [Mistral-Large-Instruct-2407-Q4_0-00001-of-00003.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q4_0-00001-of-00003.gguf)     | Q4_0   | 4 | 30.0 GB| legacy; small, very high quality loss - prefer using Q3_K_M |
| [Mistral-Large-Instruct-2407-Q4_0-00002-of-00003.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q4_0-00002-of-00003.gguf)     | Q4_0   | 4 | 30.0 GB| legacy; small, very high quality loss - prefer using Q3_K_M |
| [Mistral-Large-Instruct-2407-Q4_0-00003-of-00003.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q4_0-00003-of-00003.gguf)     | Q4_0   | 4 | 9.09 GB| legacy; small, very high quality loss - prefer using Q3_K_M |
| [Mistral-Large-Instruct-2407-Q4_K_M-00001-of-00003.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q4_K_M-00001-of-00003.gguf) | Q4_K_M | 4 | 30.0 GB| medium, balanced quality - recommended |
| [Mistral-Large-Instruct-2407-Q4_K_M-00002-of-00003.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q4_K_M-00002-of-00003.gguf) | Q4_K_M | 4 | 29.9 GB| medium, balanced quality - recommended |
| [Mistral-Large-Instruct-2407-Q4_K_M-00003-of-00003.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q4_K_M-00003-of-00003.gguf) | Q4_K_M | 4 | 13.3 GB| medium, balanced quality - recommended |
| [Mistral-Large-Instruct-2407-Q4_K_S-00001-of-00003.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q4_K_S-00001-of-00003.gguf) | Q4_K_S | 4 | 29.9 GB| small, greater quality loss |
| [Mistral-Large-Instruct-2407-Q4_K_S-00002-of-00003.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q4_K_S-00002-of-00003.gguf) | Q4_K_S | 4 | 30.0 GB| small, greater quality loss |
| [Mistral-Large-Instruct-2407-Q4_K_S-00003-of-00003.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q4_K_S-00003-of-00003.gguf) | Q4_K_S | 4 | 9.67 GB| small, greater quality loss |
| [Mistral-Large-Instruct-2407-Q5_0-00001-of-00003.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q5_0-00001-of-00003.gguf)     | Q5_0   | 5 | 30.0 GB| legacy; medium, balanced quality - prefer using Q4_K_M |
| [Mistral-Large-Instruct-2407-Q5_0-00002-of-00003.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q5_0-00002-of-00003.gguf)     | Q5_0   | 5 | 30.0 GB| legacy; medium, balanced quality - prefer using Q4_K_M |
| [Mistral-Large-Instruct-2407-Q5_0-00003-of-00003.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q5_0-00003-of-00003.gguf)     | Q5_0   | 5 | 24.4 GB| legacy; medium, balanced quality - prefer using Q4_K_M |
| [Mistral-Large-Instruct-2407-Q5_K_M-00001-of-00003.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q5_K_M-00001-of-00003.gguf) | Q5_K_M | 5 | 29.9 GB| large, very low quality loss - recommended |
| [Mistral-Large-Instruct-2407-Q5_K_M-00002-of-00003.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q5_K_M-00002-of-00003.gguf) | Q5_K_M | 5 | 29.7 GB| large, very low quality loss - recommended |
| [Mistral-Large-Instruct-2407-Q5_K_M-00003-of-00003.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q5_K_M-00003-of-00003.gguf) | Q5_K_M | 5 | 26.8 GB| large, very low quality loss - recommended |
| [Mistral-Large-Instruct-2407-Q5_K_S-00001-of-00003.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q5_K_S-00001-of-00003.gguf) | Q5_K_S | 5 | 30.0 GB| large, low quality loss - recommended |
| [Mistral-Large-Instruct-2407-Q5_K_S-00002-of-00003.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q5_K_S-00002-of-00003.gguf) | Q5_K_S | 5 | 30.0 GB| large, low quality loss - recommended |
| [Mistral-Large-Instruct-2407-Q5_K_S-00003-of-00003.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q5_K_S-00003-of-00003.gguf) | Q5_K_S | 5 | 24.4 GB| large, low quality loss - recommended |
| [Mistral-Large-Instruct-2407-Q6_K-00001-of-00004.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q6_K-00001-of-00004.gguf)     | Q6_K   | 6 | 29.9 GB| very large, extremely low quality loss |
| [Mistral-Large-Instruct-2407-Q6_K-00002-of-00004.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q6_K-00002-of-00004.gguf)     | Q6_K   | 6 | 29.8 GB| very large, extremely low quality loss |
| [Mistral-Large-Instruct-2407-Q6_K-00003-of-00004.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q6_K-00003-of-00004.gguf)     | Q6_K   | 6 | 29.8 GB| very large, extremely low quality loss |
| [Mistral-Large-Instruct-2407-Q6_K-00004-of-00004.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q6_K-00004-of-00004.gguf)     | Q6_K   | 6 | 11.1 GB| very large, extremely low quality loss |
| [Mistral-Large-Instruct-2407-Q8_0-00001-of-00005.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q8_0-00001-of-00005.gguf)     | Q8_0   | 8 | 29.8 GB| very large, extremely low quality loss - not recommended |
| [Mistral-Large-Instruct-2407-Q8_0-00002-of-00005.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q8_0-00002-of-00005.gguf)     | Q8_0   | 8 | 29.8 GB| very large, extremely low quality loss - not recommended |
| [Mistral-Large-Instruct-2407-Q8_0-00003-of-00005.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q8_0-00003-of-00005.gguf)     | Q8_0   | 8 | 29.8 GB| very large, extremely low quality loss - not recommended |
| [Mistral-Large-Instruct-2407-Q8_0-00004-of-00005.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q8_0-00004-of-00005.gguf)     | Q8_0   | 8 | 29.8 GB| very large, extremely low quality loss - not recommended |
| [Mistral-Large-Instruct-2407-Q8_0-00005-of-00005.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q8_0-00005-of-00005.gguf)     | Q8_0   | 8 | 11.1 GB| very large, extremely low quality loss - not recommended |
| [Mistral-Large-Instruct-2407-f16-00001-of-00009.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-f16-00001-of-00009.gguf)      | f16   | 16 | 29.8 GB|  |
| [Mistral-Large-Instruct-2407-f16-00002-of-00009.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-f16-00002-of-00009.gguf)      | f16   | 16 | 29.8 GB|  |
| [Mistral-Large-Instruct-2407-f16-00003-of-00009.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-f16-00003-of-00009.gguf)      | f16   | 16 | 29.7 GB|  |
| [Mistral-Large-Instruct-2407-f16-00004-of-00009.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-f16-00004-of-00009.gguf)      | f16   | 16 | 29.8 GB|  |
| [Mistral-Large-Instruct-2407-f16-00005-of-00009.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-f16-00005-of-00009.gguf)      | f16   | 16 | 29.7 GB|  |
| [Mistral-Large-Instruct-2407-f16-00006-of-00009.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-f16-00006-of-00009.gguf)      | f16   | 16 | 29.8 GB|  |
| [Mistral-Large-Instruct-2407-f16-00007-of-00009.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-f16-00007-of-00009.gguf)      | f16   | 16 | 29.7 GB|  |
| [Mistral-Large-Instruct-2407-f16-00008-of-00009.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-f16-00008-of-00009.gguf)      | f16   | 16 | 29.7 GB|  |
| [Mistral-Large-Instruct-2407-f16-00009-of-00009.gguf](https://huggingface.co/second-state/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-f16-00009-of-00009.gguf)      | f16   | 16 | 7.05 GB|  |

*Quantized with llama.cpp b3499.*
