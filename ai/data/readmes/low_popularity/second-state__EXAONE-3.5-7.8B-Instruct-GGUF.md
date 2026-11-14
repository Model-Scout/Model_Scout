---
license: other
license_name: exaone
license_link: LICENSE
model_name: EXAONE-3.5-7.8B-Instruct
base_model: LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct
quantized_by: Second State Inc.
language:
- en
- ko
tags:
- lg-ai
- exaone
- gguf
pipeline_tag: text-generation
library_name: transformers
---

<!-- header start -->
<!-- 200823 -->
<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="https://github.com/LlamaEdge/LlamaEdge/raw/dev/assets/logo.svg" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>
<hr style="margin-top: 1.0em; margin-bottom: 1.0em;">
<!-- header end -->

# EXAONE-3.5-7.8B-Instruct-GGUF

## Original Model

[LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct](https://huggingface.co/LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct)

## Run with LlamaEdge

- LlamaEdge version: [v0.16.13](https://github.com/LlamaEdge/LlamaEdge/releases/tag/0.16.13) and above

- Prompt template

  - Prompt type: `exaone-chat`

  - Prompt string

    ```text
    [|system|]{system_message}[|endofturn|]
    [|user|]{user_message_1}
    [|assistant|]{assistant_message_1}[|endofturn|]
    [|user|]{user_message_2}
    [|assistant|]
    ```

- Context size: `32000`

- Run as LlamaEdge service

  ```bash
  wasmedge --dir .:. --nn-preload default:GGML:AUTO:EXAONE-3.5-7.8B-Instruct-Q5_K_M.gguf \
      llama-api-server.wasm \
      --prompt-template exaone-chat \
      --ctx-size 32000 \
      --model-name EXAONE-3.5-7.8B-Instruct
  ```

- Run as LlamaEdge command app

  ```bash
  wasmedge --dir .:. --nn-preload default:GGML:AUTO:EXAONE-3.5-7.8B-Instruct-Q5_K_M.gguf \
    llama-chat.wasm \
    --prompt-template exaone-chat \
    --ctx-size 32000
  ```

## Quantized GGUF Models

| Name | Quant method | Bits | Size | Use case |
| ---- | ---- | ---- | ---- | ----- |
| [EXAONE-3.5-7.8B-Instruct-Q2_K.gguf](https://huggingface.co/second-state/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-Q2_K.gguf)     | Q2_K   | 2 | 3.05 GB| smallest, significant quality loss - not recommended for most purposes |
| [EXAONE-3.5-7.8B-Instruct-Q3_K_L.gguf](https://huggingface.co/second-state/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-Q3_K_L.gguf) | Q3_K_L | 3 | 4.19 GB| small, substantial quality loss |
| [EXAONE-3.5-7.8B-Instruct-Q3_K_M.gguf](https://huggingface.co/second-state/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-Q3_K_M.gguf) | Q3_K_M | 3 | 3.88 GB| very small, high quality loss |
| [EXAONE-3.5-7.8B-Instruct-Q3_K_S.gguf](https://huggingface.co/second-state/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-Q3_K_S.gguf) | Q3_K_S | 3 | 3.53 GB| very small, high quality loss |
| [EXAONE-3.5-7.8B-Instruct-Q4_0.gguf](https://huggingface.co/second-state/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-Q4_0.gguf)     | Q4_0   | 4 | 4.51 GB| legacy; small, very high quality loss - prefer using Q3_K_M |
| [EXAONE-3.5-7.8B-Instruct-Q4_K_M.gguf](https://huggingface.co/second-state/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-Q4_K_M.gguf) | Q4_K_M | 4 | 4.77 GB| medium, balanced quality - recommended |
| [EXAONE-3.5-7.8B-Instruct-Q4_K_S.gguf](https://huggingface.co/second-state/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-Q4_K_S.gguf) | Q4_K_S | 4 | 4.54 GB| small, greater quality loss |
| [EXAONE-3.5-7.8B-Instruct-Q5_0.gguf](https://huggingface.co/second-state/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-Q5_0.gguf)     | Q5_0   | 5 | 5.44 GB| legacy; medium, balanced quality - prefer using Q4_K_M |
| [EXAONE-3.5-7.8B-Instruct-Q5_K_M.gguf](https://huggingface.co/second-state/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-Q5_K_M.gguf) | Q5_K_M | 5 | 5.57 GB| large, very low quality loss - recommended |
| [EXAONE-3.5-7.8B-Instruct-Q5_K_S.gguf](https://huggingface.co/second-state/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-Q5_K_S.gguf) | Q5_K_S | 5 | 5.44 GB| large, low quality loss - recommended |
| [EXAONE-3.5-7.8B-Instruct-Q6_K.gguf](https://huggingface.co/second-state/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-Q6_K.gguf)     | Q6_K   | 6 | 6.42 GB| very large, extremely low quality loss |
| [EXAONE-3.5-7.8B-Instruct-Q8_0.gguf](https://huggingface.co/second-state/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-Q8_0.gguf)     | Q8_0   | 8 | 8.31 GB| very large, extremely low quality loss - not recommended |
| [EXAONE-3.5-7.8B-Instruct-f16.gguf](https://huggingface.co/second-state/EXAONE-3.5-7.8B-Instruct-GGUF/blob/main/EXAONE-3.5-7.8B-Instruct-f16.gguf)       | f16    | 16 | 15.6 GB|  |

*Quantized with llama.cpp b4932.*