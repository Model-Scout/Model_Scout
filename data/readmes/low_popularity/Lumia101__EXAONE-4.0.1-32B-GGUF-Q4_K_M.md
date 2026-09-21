---
license: other
license_name: exaone
license_link: LICENSE
language:
- ko
- en
- es
base_model:
- LGAI-EXAONE/EXAONE-4.0.1-32B
pipeline_tag: text-generation
---

# Lumia101/EXAONE-4.0.1-32B-GGUF-Q4_K_M

This model is converted to GGUF format from [LGAI-EXAONE/EXAONE-4.0.1-32B](https://huggingface.co/LGAI-EXAONE/EXAONE-4.0.1-32B) using llama.cpp release [b6795](https://github.com/ggml-org/llama.cpp/releases/tag/b6795).

Original model card: [LGAI-EXAONE/EXAONE-4.0.1-32B](https://huggingface.co/LGAI-EXAONE/EXAONE-4.0.1-32B)

(I wanted to make other versions besides Q4_K_M, but I didn't have time because I'm a high school student...)

# How to use this model with llama-cpp-python

1. Install llama-cpp-python with this command.

```bash
pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu124
```

2. Use this code to use this model.

```python
from llama_cpp import Llama

llm = Llama.from_pretrained(
    repo_id="Lumia101/EXAONE-4.0.1-32B-GGUF-Q4_K_M",
    filename="EXAONE-4.0.1-Q4_K_M-ctemplate-removed.gguf", # Because there is an issue with the Chat Template in the original model, you must use the version with the tool usage section removed.
    n_gpu_layers=-1,
    n_ctx=8192, # If you have enough GPU memory, increase this value.
    verbose=False
)

prompt = "Tell me the reason why I need GPU to run a language model." # If you would like to ask this model another question, please edit it here.

output_stream = llm.create_chat_completion(
    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.6,
    top_p=0.95,
    presence_penalty=1.5,
    stream=True
)

for chunk in output_stream:
    content = chunk.get('choices', [{}])[0].get('delta', {}).get('content', '')
    
    if content:
        print(content, end='', flush=True)
        
print()
```