---
license: apache-2.0
model_name: Mistral-Small-24B-Instruct-2501
base_model: mistralai/Mistral-Small-24B-Instruct-2501
model_creator: mistralai
quantized_by: Second State Inc.
inference: false
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
tags:
- transformers
---

<!-- header start -->
<!-- 200823 -->
<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="https://github.com/LlamaEdge/LlamaEdge/raw/dev/assets/logo.svg" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>
<hr style="margin-top: 1.0em; margin-bottom: 1.0em;">
<!-- header end -->

# Mistral-Small-24B-Instruct-2501-GGUF

## Original Model

[mistralai/Mistral-Small-24B-Instruct-2501](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501)

## Run with LlamaEdge

- LlamaEdge version: [v0.16.5](https://github.com/LlamaEdge/LlamaEdge/releases/tag/0.16.5)

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
    wasmedge --dir .:. --nn-preload default:GGML:AUTO:Mistral-Small-24B-Instruct-2501-Q5_K_M.gguf \
        llama-api-server.wasm \
        --prompt-template mistral-small-chat \
        --ctx-size 32000 \
        --model-name Mistral-Small-24B-Instruct-2501
    ```

  - Chat + Tool Use
 
    ```bash
    wasmedge --dir .:. --nn-preload default:GGML:AUTO:Mistral-Small-24B-Instruct-2501-Q5_K_M.gguf \
        llama-api-server.wasm \
        --prompt-template mistral-small-tool \
        --ctx-size 32000 \
        --model-name Mistral-Small-24B-Instruct-2501
    ```
 
    Example:
    
    ![image/png](https://cdn-uploads.huggingface.co/production/uploads/64e47b341deccdb4dccaa431/MlKzPbiZ8yz8j18vqa6Ax.png)

- Run as LlamaEdge command app

  - Chat 

    ```bash
    wasmedge --dir .:. --nn-preload default:GGML:AUTO:Mistral-Small-24B-Instruct-2501-Q5_K_M.gguf \
      llama-chat.wasm \
      --prompt-template mistral-small-chat \
      --ctx-size 32000
    ```

## Quantized GGUF Models

| Name | Quant method | Bits | Size | Use case |
| ---- | ---- | ---- | ---- | ----- |
| [Mistral-Small-24B-Instruct-2501-Q2_K.gguf](https://huggingface.co/second-state/Mistral-Small-24B-Instruct-2501-GGUF/blob/main/Mistral-Small-24B-Instruct-2501-Q2_K.gguf)     | Q2_K   | 2 | 8.89 GB| smallest, significant quality loss - not recommended for most purposes |
| [Mistral-Small-24B-Instruct-2501-Q3_K_L.gguf](https://huggingface.co/second-state/Mistral-Small-24B-Instruct-2501-GGUF/blob/main/Mistral-Small-24B-Instruct-2501-Q3_K_L.gguf) | Q3_K_L | 3 | 12.4 GB| small, substantial quality loss |
| [Mistral-Small-24B-Instruct-2501-Q3_K_M.gguf](https://huggingface.co/second-state/Mistral-Small-24B-Instruct-2501-GGUF/blob/main/Mistral-Small-24B-Instruct-2501-Q3_K_M.gguf) | Q3_K_M | 3 | 11.5 GB| very small, high quality loss |
| [Mistral-Small-24B-Instruct-2501-Q3_K_S.gguf](https://huggingface.co/second-state/Mistral-Small-24B-Instruct-2501-GGUF/blob/main/Mistral-Small-24B-Instruct-2501-Q3_K_S.gguf) | Q3_K_S | 3 | 10.4 GB| very small, high quality loss |
| [Mistral-Small-24B-Instruct-2501-Q4_0.gguf](https://huggingface.co/second-state/Mistral-Small-24B-Instruct-2501-GGUF/blob/main/Mistral-Small-24B-Instruct-2501-Q4_0.gguf)     | Q4_0   | 4 | 13.4 GB| legacy; small, very high quality loss - prefer using Q3_K_M |
| [Mistral-Small-24B-Instruct-2501-Q4_K_M.gguf](https://huggingface.co/second-state/Mistral-Small-24B-Instruct-2501-GGUF/blob/main/Mistral-Small-24B-Instruct-2501-Q4_K_M.gguf) | Q4_K_M | 4 | 14.3 GB| medium, balanced quality - recommended |
| [Mistral-Small-24B-Instruct-2501-Q4_K_S.gguf](https://huggingface.co/second-state/Mistral-Small-24B-Instruct-2501-GGUF/blob/main/Mistral-Small-24B-Instruct-2501-Q4_K_S.gguf) | Q4_K_S | 4 | 13.5 GB| small, greater quality loss |
| [Mistral-Small-24B-Instruct-2501-Q5_0.gguf](https://huggingface.co/second-state/Mistral-Small-24B-Instruct-2501-GGUF/blob/main/Mistral-Small-24B-Instruct-2501-Q5_0.gguf)     | Q5_0   | 5 | 16.3 GB| legacy; medium, balanced quality - prefer using Q4_K_M |
| [Mistral-Small-24B-Instruct-2501-Q5_K_M.gguf](https://huggingface.co/second-state/Mistral-Small-24B-Instruct-2501-GGUF/blob/main/Mistral-Small-24B-Instruct-2501-Q5_K_M.gguf) | Q5_K_M | 5 | 16.8 GB| large, very low quality loss - recommended |
| [Mistral-Small-24B-Instruct-2501-Q5_K_S.gguf](https://huggingface.co/second-state/Mistral-Small-24B-Instruct-2501-GGUF/blob/main/Mistral-Small-24B-Instruct-2501-Q5_K_S.gguf) | Q5_K_S | 5 | 16.3 GB| large, low quality loss - recommended |
| [Mistral-Small-24B-Instruct-2501-Q6_K.gguf](https://huggingface.co/second-state/Mistral-Small-24B-Instruct-2501-GGUF/blob/main/Mistral-Small-24B-Instruct-2501-Q6_K.gguf)     | Q6_K   | 6 | 19.3 GB| very large, extremely low quality loss |
| [Mistral-Small-24B-Instruct-2501-Q8_0.gguf](https://huggingface.co/second-state/Mistral-Small-24B-Instruct-2501-GGUF/blob/main/Mistral-Small-24B-Instruct-2501-Q8_0.gguf)     | Q8_0   | 8 | 25.1 GB| very large, extremely low quality loss - not recommended |
| [Mistral-Small-24B-Instruct-2501-f16.gguf](https://huggingface.co/second-state/Mistral-Small-24B-Instruct-2501-GGUF/blob/main/Mistral-Small-24B-Instruct-2501-f16.gguf)     | f16   | 16 | 47.2 GB|  |

*Quantized with llama.cpp b4595.*