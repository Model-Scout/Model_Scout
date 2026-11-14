---
library_name: transformers
license: apache-2.0
language:
- ko
---

# Model Card for Model ID


## Model Details

### Model Description

The Gemma Self-Attention Merged model is a large language model created by merging the self-attention layers of an [English-based Gemma 7B model](https://huggingface.co/google/gemma-1.1-7b-it) and a [Korean-based Gemma 7B model](beomi/gemma-ko-7b). This merger allows the model to leverage the capabilities of both the English and Korean models, resulting in a more versatile and capable language model that can perform well on tasks involving both English and Korean text.

The key features of this merged model include:

- Increased self-attention capacity with doubled number of attention heads
- Ability to handle both English and Korean language input
- Potential for improved performance on a wide range of natural language processing tasks

#### Chat template

**system:** system message...  
**B:** user message...  
**A:** assistant message...  

### Model Sources

- **Repository:** https://github.com/lcw99/merge-gemma-attn.git