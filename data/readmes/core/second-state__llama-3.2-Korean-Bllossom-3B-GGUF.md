---
base_model: Bllossom/llama-3.2-Korean-Bllossom-3B
license: llama3.2
model_creator: Bllossom
model_name: llama-3.2-Korean-Bllossom-3B
quantized_by: Second State Inc.
language:
- en
- ko
library_name: transformers
---

<!-- header start -->
<!-- 200823 -->
<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="https://github.com/LlamaEdge/LlamaEdge/raw/dev/assets/logo.svg" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>
<hr style="margin-top: 1.0em; margin-bottom: 1.0em;">
<!-- header end -->

# llama-3.2-Korean-Bllossom-3B-GGUF

## Original Model

[Bllossom/llama-3.2-Korean-Bllossom-3B](https://huggingface.co/Bllossom/llama-3.2-Korean-Bllossom-3B)

## Run with LlamaEdge

- LlamaEdge version: [v0.16.9](https://github.com/LlamaEdge/LlamaEdge/releases/tag/0.16.9) and above

- Prompt template

  - Prompt type for chat: `llama-3-chat`

    - Prompt string
  
      ```text
      <|begin_of_text|><|start_header_id|>system<|end_header_id|>
  
      {{ system_prompt }}<|eot_id|><|start_header_id|>user<|end_header_id|>
  
      {{ user_message_1 }}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
  
      {{ model_answer_1 }}<|eot_id|><|start_header_id|>user<|end_header_id|>
  
      {{ user_message_2 }}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
      ```

  - Prompt type for tool use: `llama-3-tool`
 
    - Prompt string

      ```text
      <|begin_of_text|><|start_header_id|>system<|end_header_id|>

      {system_message}<|eot_id|><|start_header_id|>user<|end_header_id|>
  
      Given the following functions, please respond with a JSON for a function call with its proper arguments that best answers the given prompt.
  
      Respond in the format {"name": function name, "parameters": dictionary of argument name and its value}. Do not use variables.
  
      [{"type":"function","function":{"name":"get_current_weather","description":"Get the current weather in a given location","parameters":{"type":"object","properties":{"location":{"type":"string","description":"The city and state, e.g. San Francisco, CA"},"unit":{"type":"string","description":"The temperature unit to use. Infer this from the users location.","enum":["celsius","fahrenheit"]}},"required":["location","unit"]}}}]
  
      Question: {user_message}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
      ```

- Context size: `128000`

- Run as LlamaEdge service

  - Chat
  
    ```bash
    wasmedge --dir .:. --nn-preload default:GGML:AUTO:llama-3.2-Korean-Bllossom-3B-Q5_K_M.gguf \
        llama-api-server.wasm \
        --prompt-template llama-3-chat \
        --ctx-size 128000 \
        --model-name llama-3.2-Korean
    ```

  - Tool use

    ```bash
    wasmedge --dir .:. --nn-preload default:GGML:AUTO:llama-3.2-Korean-Bllossom-3B-Q5_K_M.gguf \
        llama-api-server.wasm \
        --prompt-template llama-3-tool \
        --ctx-size 128000 \
        --model-name llama-3.2-Korean
    ```

- Run as LlamaEdge command app

  ```bash
  wasmedge --dir .:. --nn-preload default:GGML:AUTO:llama-3.2-Korean-Bllossom-3B-Q5_K_M.gguf \
    llama-chat.wasm \
    --prompt-template llama-3-chat \
    --ctx-size 128000
  ```

## Quantized GGUF Models

| Name | Quant method | Bits | Size | Use case |
| ---- | ---- | ---- | ---- | ----- |
| [llama-3.2-Korean-Bllossom-3B-Q2_K.gguf](https://huggingface.co/second-state/llama-3.2-Korean-Bllossom-3B-GGUF/blob/main/llama-3.2-Korean-Bllossom-3B-Q2_K.gguf)     | Q2_K   | 2 | 581 MB| smallest, significant quality loss - not recommended for most purposes |
| [llama-3.2-Korean-Bllossom-3B-Q3_K_L.gguf](https://huggingface.co/second-state/llama-3.2-Korean-Bllossom-3B-GGUF/blob/main/llama-3.2-Korean-Bllossom-3B-Q3_K_L.gguf) | Q3_K_L | 3 | 733 MB| small, substantial quality loss |
| [llama-3.2-Korean-Bllossom-3B-Q3_K_M.gguf](https://huggingface.co/second-state/llama-3.2-Korean-Bllossom-3B-GGUF/blob/main/llama-3.2-Korean-Bllossom-3B-Q3_K_M.gguf) | Q3_K_M | 3 | 691 MB| very small, high quality loss |
| [llama-3.2-Korean-Bllossom-3B-Q3_K_S.gguf](https://huggingface.co/second-state/llama-3.2-Korean-Bllossom-3B-GGUF/blob/main/llama-3.2-Korean-Bllossom-3B-Q3_K_S.gguf) | Q3_K_S | 3 | 642 MB| very small, high quality loss |
| [llama-3.2-Korean-Bllossom-3B-Q4_0.gguf](https://huggingface.co/second-state/llama-3.2-Korean-Bllossom-3B-GGUF/blob/main/llama-3.2-Korean-Bllossom-3B-Q4_0.gguf)     | Q4_0   | 4 | 771 MB| legacy; small, very high quality loss - prefer using Q3_K_M |
| [llama-3.2-Korean-Bllossom-3B-Q4_K_M.gguf](https://huggingface.co/second-state/llama-3.2-Korean-Bllossom-3B-GGUF/blob/main/llama-3.2-Korean-Bllossom-3B-Q4_K_M.gguf) | Q4_K_M | 4 | 808 MB| medium, balanced quality - recommended |
| [llama-3.2-Korean-Bllossom-3B-Q4_K_S.gguf](https://huggingface.co/second-state/llama-3.2-Korean-Bllossom-3B-GGUF/blob/main/llama-3.2-Korean-Bllossom-3B-Q4_K_S.gguf) | Q4_K_S | 4 | 776 MB| small, greater quality loss |
| [llama-3.2-Korean-Bllossom-3B-Q5_0.gguf](https://huggingface.co/second-state/llama-3.2-Korean-Bllossom-3B-GGUF/blob/main/llama-3.2-Korean-Bllossom-3B-Q5_0.gguf)     | Q5_0   | 5 | 893 MB| legacy; medium, balanced quality - prefer using Q4_K_M |
| [llama-3.2-Korean-Bllossom-3B-Q5_K_M.gguf](https://huggingface.co/second-state/llama-3.2-Korean-Bllossom-3B-GGUF/blob/main/llama-3.2-Korean-Bllossom-3B-Q5_K_M.gguf) | Q5_K_M | 5 | 912 MB| large, very low quality loss - recommended |
| [llama-3.2-Korean-Bllossom-3B-Q5_K_S.gguf](https://huggingface.co/second-state/llama-3.2-Korean-Bllossom-3B-GGUF/blob/main/llama-3.2-Korean-Bllossom-3B-Q5_K_S.gguf) | Q5_K_S | 5 | 893 MB| large, low quality loss - recommended |
| [llama-3.2-Korean-Bllossom-3B-Q6_K.gguf](https://huggingface.co/second-state/llama-3.2-Korean-Bllossom-3B-GGUF/blob/main/llama-3.2-Korean-Bllossom-3B-Q6_K.gguf)     | Q6_K   | 6 | 1.02 GB| very large, extremely low quality loss |
| [llama-3.2-Korean-Bllossom-3B-Q8_0.gguf](https://huggingface.co/second-state/llama-3.2-Korean-Bllossom-3B-GGUF/blob/main/llama-3.2-Korean-Bllossom-3B-Q8_0.gguf)     | Q8_0   | 8 | 1.32 GB| very large, extremely low quality loss - not recommended |
| [llama-3.2-Korean-Bllossom-3B-f16.gguf](https://huggingface.co/second-state/llama-3.2-Korean-Bllossom-3B-GGUF/blob/main/llama-3.2-Korean-Bllossom-3B-f16.gguf)       | f16    | 16 | 2.48 GB| |

*Quantized with llama.cpp b4831*
