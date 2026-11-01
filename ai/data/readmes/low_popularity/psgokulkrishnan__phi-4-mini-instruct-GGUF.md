---
language:
- multilingual
- ar
- zh
- cs
- da
- nl
- en
- fi
- fr
- de
- he
- hu
- it
- ja
- ko
- 'no'
- pl
- pt
- ru
- es
- sv
- th
- tr
- uk
library_name: transformers
license: mit
license_link: https://huggingface.co/microsoft/Phi-4-mini-instruct/resolve/main/LICENSE
pipeline_tag: text-generation
tags:
- nlp
- code
widget:
- messages:
  - role: user
    content: Can you provide ways to eat combinations of bananas and dragonfruits?
---
https://huggingface.co/microsoft/Phi-4-mini-instruct


Usage:
from llama_cpp import Llama

GGUF_PATH = "./phi_4_mini_instruct_Q4_K_M.gguf"

print("⏳ Initializing long-context GGUF engine directly into memory layout...")
llm = Llama(
    model_path=GGUF_PATH,
    n_ctx=16384,        
    flash_attn=True,     
    n_threads=4,        
    verbose=False
)