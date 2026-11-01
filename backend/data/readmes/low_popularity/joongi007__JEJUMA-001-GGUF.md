---
license: mit
base_model: JEJUMA/JEJUMA-001
tags:
- gguf
- Dialect
- Language
model-index:
- name: joongi007/JEJUMA-001-GGUF
  results: []
language:
- ko
pipeline_tag: text-generation
---
- Original model is [JEJUMA/JEJUMA-001](https://huggingface.co/JEJUMA/JEJUMA-001)
- quantized using [llama.cpp](https://github.com/ggerganov/llama.cpp) - [b3510](https://github.com/ggerganov/llama.cpp/releases/tag/b3510)

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
Detect the following sentence or word is Jeju island dialect or standard Korean: 
```
{Enter the Jeju island dialect or standard Korean here}
```
````
````example
Detect the following sentence or word is Jeju island dialect or standard Korean and convert the following sentence or word to Jeju island dialect or standard Korean: 
```
{Enter Jeju island dialect or standard Korean here}
```
````