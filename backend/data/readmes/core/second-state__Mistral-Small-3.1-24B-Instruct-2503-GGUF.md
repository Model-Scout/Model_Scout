---
license: apache-2.0
model_name: Mistral-Small-3.1-24B-Instruct-2503
base_model: mistralai/Mistral-Small-3.1-24B-Instruct-2503
model_creator: mistralai
quantized_by: Second State Inc.
inference: false
language:
- en
- fr
- de
- es
- pt
- it
- ja
- ko
- ru
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
tags:
- transformers
pipeline_tag: image-text-to-text
---

<!-- header start -->
<!-- 200823 -->
<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="https://github.com/LlamaEdge/LlamaEdge/raw/dev/assets/logo.svg" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>
<hr style="margin-top: 1.0em; margin-bottom: 1.0em;">
<!-- header end -->

# Mistral-Small-3.1-24B-Instruct-2503-GGUF

## Original Model

[mistralai/Mistral-Small-3.1-24B-Instruct-2503](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503)

## Run with LlamaEdge

- LlamaEdge version: [v0.16.13](https://github.com/LlamaEdge/LlamaEdge/releases/tag/0.16.13) and above

- Prompt template

  - Chat

    - Prompt type: `mistral-small-chat`

    - Prompt string

      ```text
      <s>[SYSTEM_PROMPT]<system prompt>[/SYSTEM_PROMPT][INST]<user message>[/INST]<assistant response></s>[INST]<user message>[/INST]
      ```

  - Chat + Tool Use

    - Prompt type: `mistral-small-tool`

    - Prompt string

      ```text
      <s>[INST] {user_message_1}[/INST][TOOL_CALLS] [{tool_call_1},{tool_call_2}]</s>[TOOL_RESULTS] {tool_result_1}[/TOOL_RESULTS] {assistant_message_1}</s>[AVAILABLE_TOOLS] [{tool_1},{tool_2}][/AVAILABLE_TOOLS][INST] {system_message}<0x0A><0x0A>{user_message_2}[/INST]
      ```

- Context size: `32000`

- Run as LlamaEdge service

  - Chat

    ```bash
    wasmedge --dir .:. --nn-preload default:GGML:AUTO:Mistral-Small-3.1-24B-Instruct-2503-Q5_K_M.gguf \
        llama-api-server.wasm \
        --prompt-template mistral-small-chat \
        --ctx-size 32000 \
        --model-name Mistral-Small
    ```

  - Chat + Tool Use

    ```bash
    wasmedge --dir .:. --nn-preload default:GGML:AUTO:Mistral-Small-3.1-24B-Instruct-2503-Q5_K_M.gguf \
        llama-api-server.wasm \
        --prompt-template mistral-small-tool \
        --ctx-size 32000 \
        --model-name Mistral-Small
    ```

- Run as LlamaEdge command app

  - Chat

    ```bash
    wasmedge --dir .:. --nn-preload default:GGML:AUTO:Mistral-Small-3.1-24B-Instruct-2503-Q5_K_M.gguf \
      llama-chat.wasm \
      --prompt-template mistral-small-chat \
      --ctx-size 32000
    ```

## Quantized GGUF Models

| Name | Quant method | Bits | Size | Use case |
| ---- | ---- | ---- | ---- | ----- |
| [Mistral-Small-3.1-24B-Instruct-2503-Q2_K.gguf](https://huggingface.co/second-state/Mistral-Small-3.1-24B-Instruct-2503-GGUF/blob/main/Mistral-Small-3.1-24B-Instruct-2503-Q2_K.gguf)     | Q2_K   | 2 | 8.89 GB| smallest, significant quality loss - not recommended for most purposes |
| [Mistral-Small-3.1-24B-Instruct-2503-Q3_K_L.gguf](https://huggingface.co/second-state/Mistral-Small-3.1-24B-Instruct-2503-GGUF/blob/main/Mistral-Small-3.1-24B-Instruct-2503-Q3_K_L.gguf) | Q3_K_L | 3 | 12.4 GB| small, substantial quality loss |
| [Mistral-Small-3.1-24B-Instruct-2503-Q3_K_M.gguf](https://huggingface.co/second-state/Mistral-Small-3.1-24B-Instruct-2503-GGUF/blob/main/Mistral-Small-3.1-24B-Instruct-2503-Q3_K_M.gguf) | Q3_K_M | 3 | 11.5 GB| very small, high quality loss |
| [Mistral-Small-3.1-24B-Instruct-2503-Q3_K_S.gguf](https://huggingface.co/second-state/Mistral-Small-3.1-24B-Instruct-2503-GGUF/blob/main/Mistral-Small-3.1-24B-Instruct-2503-Q3_K_S.gguf) | Q3_K_S | 3 | 10.4 GB| very small, high quality loss |
| [Mistral-Small-3.1-24B-Instruct-2503-Q4_0.gguf](https://huggingface.co/second-state/Mistral-Small-3.1-24B-Instruct-2503-GGUF/blob/main/Mistral-Small-3.1-24B-Instruct-2503-Q4_0.gguf)     | Q4_0   | 4 | 13.4 GB| legacy; small, very high quality loss - prefer using Q3_K_M |
| [Mistral-Small-3.1-24B-Instruct-2503-Q4_K_M.gguf](https://huggingface.co/second-state/Mistral-Small-3.1-24B-Instruct-2503-GGUF/blob/main/Mistral-Small-3.1-24B-Instruct-2503-Q4_K_M.gguf) | Q4_K_M | 4 | 14.3 GB| medium, balanced quality - recommended |
| [Mistral-Small-3.1-24B-Instruct-2503-Q4_K_S.gguf](https://huggingface.co/second-state/Mistral-Small-3.1-24B-Instruct-2503-GGUF/blob/main/Mistral-Small-3.1-24B-Instruct-2503-Q4_K_S.gguf) | Q4_K_S | 4 | 13.5 GB| small, greater quality loss |
| [Mistral-Small-3.1-24B-Instruct-2503-Q5_0.gguf](https://huggingface.co/second-state/Mistral-Small-3.1-24B-Instruct-2503-GGUF/blob/main/Mistral-Small-3.1-24B-Instruct-2503-Q5_0.gguf)     | Q5_0   | 5 | 16.3 GB| legacy; medium, balanced quality - prefer using Q4_K_M |
| [Mistral-Small-3.1-24B-Instruct-2503-Q5_K_M.gguf](https://huggingface.co/second-state/Mistral-Small-3.1-24B-Instruct-2503-GGUF/blob/main/Mistral-Small-3.1-24B-Instruct-2503-Q5_K_M.gguf) | Q5_K_M | 5 | 16.8 GB| large, very low quality loss - recommended |
| [Mistral-Small-3.1-24B-Instruct-2503-Q5_K_S.gguf](https://huggingface.co/second-state/Mistral-Small-3.1-24B-Instruct-2503-GGUF/blob/main/Mistral-Small-3.1-24B-Instruct-2503-Q5_K_S.gguf) | Q5_K_S | 5 | 16.3 GB| large, low quality loss - recommended |
| [Mistral-Small-3.1-24B-Instruct-2503-Q6_K.gguf](https://huggingface.co/second-state/Mistral-Small-3.1-24B-Instruct-2503-GGUF/blob/main/Mistral-Small-3.1-24B-Instruct-2503-Q6_K.gguf)     | Q6_K   | 6 | 19.3 GB| very large, extremely low quality loss |
| [Mistral-Small-3.1-24B-Instruct-2503-Q8_0.gguf](https://huggingface.co/second-state/Mistral-Small-3.1-24B-Instruct-2503-GGUF/blob/main/Mistral-Small-3.1-24B-Instruct-2503-Q8_0.gguf)     | Q8_0   | 8 | 25.1 GB| very large, extremely low quality loss - not recommended |
| [Mistral-Small-3.1-24B-Instruct-2503-f16.gguf](https://huggingface.co/second-state/Mistral-Small-3.1-24B-Instruct-2503-GGUF/blob/main/Mistral-Small-3.1-24B-Instruct-2503-f16.gguf)     | f16   | 16 | 47.2 GB|  |

*Quantized with llama.cpp b4944.*