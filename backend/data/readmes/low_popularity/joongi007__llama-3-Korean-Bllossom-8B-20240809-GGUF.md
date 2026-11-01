---
license: llama3.1
base_model: MLP-KTLim/llama-3-Korean-Bllossom-8B
language:
- en
- ko
pipeline_tag: text-generation
model-index:
- name: joongi007/llama-3-Korean-Bllossom-8B-20240809-GGUF
  results: []
tags:
- gguf
- llama
- ' conversational'
---
- Original model is [MLP-KTLim/llama-3-Korean-Bllossom-8B](https://huggingface.co/MLP-KTLim/llama-3-Korean-Bllossom-8B) - [ece1eea](https://huggingface.co/MLP-KTLim/llama-3-Korean-Bllossom-8B/tree/ece1eea3e0f1653eebac5016bdae1fbd37894078)
- quantized using [llama.cpp](https://github.com/ggerganov/llama.cpp) - [b3547](https://github.com/ggerganov/llama.cpp/releases/tag/b3547)

**The model was based on the version of Llama3.1 but was named Llama3.**

Prompt(LM Studio)
```prompt
<|start_header_id|>system<|end_header_id|>

{System}
<|eot_id|><|start_header_id|>user<|end_header_id|>

{User}
<|eot_id|><|start_header_id|>assistant<|end_header_id|>

{Assistant}
```