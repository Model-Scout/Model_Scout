---
license: mit
base_model: JEJUMA/JEJUMA-002
tags:
- gguf
- Dialect
- Language
model-index:
- name: joongi007/JEJUMA-002-GGUF
  results: []
language:
- ko
pipeline_tag: text-generation
---
- Original model is [JEJUMA/JEJUMA-002](https://huggingface.co/JEJUMA/JEJUMA-002) - [bbd7ec2](https://huggingface.co/JEJUMA/JEJUMA-002/tree/bbd7ec2d14c9074cfe72aeaeb113f8530f070cf8)
- quantized using [llama.cpp](https://github.com/ggerganov/llama.cpp) - [b3542](https://github.com/ggerganov/llama.cpp/releases/tag/b3542)
- JEJUMA Official Quantization is [JEJUMA/JEJUMA-002-GGUF](https://huggingface.co/JEJUMA/JEJUMA-002-GGUF)

- After trying out this model, I noticed a few things:
    1. It's more like a translation model. You can't chat with it, it only does translations.
    2. It can only handle one dialect (or standard Korean) at a time.
    3. Don't expect a conversation. It's strictly for translation purposes! Look at the example below!   
        system prompt   
        ```
        Answer your questions using the Jeju dialect.
        ```
        user question   
        ```
        hello! How are you doing now?
        ```
        assistant answer   
        ```
        헐쯤 험과게
        # 할수 많습니까
        ```
    

Prompt(LM Studio)
```prompt
<|start_header_id|>system<|end_header_id|>

{System}
<|eot_id|><|start_header_id|>user<|end_header_id|>

{User}
<|eot_id|><|start_header_id|>assistant<|end_header_id|>

{Assistant}
```
   
Example of User Prompts
````example
Detect the following sentence or word is standard, jeju, chungcheong, gangwon, gyeongsang, or jeonla's dialect: 
```
{Enter the Jeju island dialect or standard Korean here}
```
````
````example
Detect the following sentence or word is which dialect and convert the following sentence or word to standard Korean: 
```
{Enter Jeju island dialect or standard Korean here}
```
````