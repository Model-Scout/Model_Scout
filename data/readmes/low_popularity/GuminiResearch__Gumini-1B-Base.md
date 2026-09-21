---
license: other
license_name: qwen-research
license_link: https://huggingface.co/Qwen/Qwen2.5-3B/blob/main/LICENSE
library_name: transformers
language:
  - ko
  - en
tags:
  - text-generation
  - korean
  - bilingual
  - qwen2
  - built-with-qwen
  - continued-pretraining
base_model: Qwen/Qwen2.5-3B
datasets:
  - HuggingFaceFW/fineweb-edu
  - uonlp/CulturaX
  - wikimedia/wikipedia
pipeline_tag: text-generation
---

# 🐻 Gumini-1B (구미니)

<p align="center">
  <img src="https://img.shields.io/badge/Parameters-1.08B-blue" style="display:inline-block; margin-right:6px;" />
  <img src="https://img.shields.io/badge/Layers-10-green" style="display:inline-block; margin-right:6px;" />
  <img src="https://img.shields.io/badge/Languages-Korean%20%7C%20English-orange" style="display:inline-block; margin-right:6px;" />
  <img src="https://img.shields.io/badge/Built%20with-Qwen-purple" style="display:inline-block; margin-right:6px;" />
</p>

<p align="center">
  <a href="https://linkedin.com/in/devgumin" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Gumin%20Kwon-0A66C2?logo=linkedin&logoColor=white" style="display:inline-block; margin-right:6px;" />
  </a>

  <a href="https://x.com/Gumini_Research" target="_blank">
    <img src="https://img.shields.io/badge/X-@Gumini__Research-black?logo=x&logoColor=white" style="display:inline-block; margin-right:6px;" />
  </a>

  <a href="https://www.instagram.com/gumini_research/" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-gumini__research-E4405F?logo=instagram&logoColor=white" style="display:inline-block;" />
  </a>
</p>

<p align="center"><b>Built with Qwen</b></p>

## Model Description

**Gumini** (구미니) is a bilingual Korean-English **base language model** created by inheriting the first 10 layers of **Qwen 2.5 3B** using the *Inheritune* methodology, followed by **continued pretraining** on a Korean–English mixed corpus (~393M tokens).

> This is a **BASE model**, not instruction-tuned.  
> It produces text continuations rather than conversational responses.

## What We Modified

The original **Qwen 2.5 3B** model was modified as follows:

1. **Layer Inheritance (Inheritune)**  
   - Inherited the first **10 transformer layers** out of 36  
   - Reduced model size while preserving early linguistic abilities  

2. **Pretraining**  
   - Trained for **393M tokens** on a Korean–English dataset  
   - Maintains base-model behavior (not SFT or instruction-tuning)

3. **Identity Injection**  
   - Added system-level identity tokens for model conditioning  

This model **inherits early layers from Qwen 2.5 3B** and is 
**retrained with progressive layer expansion using Inheritune** methodology.

## Model Details

| Attribute | Value |
|-----------|-------|
| **Researcher** | Gumin Kwon (권구민) |
| **Base Model** | Qwen/Qwen2.5-3B |
| **Training Method** | Inheritune + Pretraining |
| **Parameters** | 1.08B |
| **Layers** | 10 |
| **Hidden Size** | 2048 |
| **Attention Heads** | 16 |
| **KV Heads** | 2 (GQA) |
| **Vocab Size** | 151,936 |
| **Tokens Trained** | 393M |

## Training Data

| Dataset | Language | Weight |
|---------|----------|---------|
| FineWeb-Edu | English | 20% |
| CulturaX-ko | Korean | 50% |
| Wikipedia-ko | Korean | 30% |
---
## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model = AutoModelForCausalLM.from_pretrained(
    "GuminiResearch/Gumini-1B-Base",
    torch_dtype=torch.bfloat16,
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("GuminiResearch/Gumini-1B-Base")

prompt = "저는 구미니입니다."
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(
    **inputs,
    max_new_tokens=100,
    repetition_penalty=1.2,
    do_sample=True,
    temperature=0.7
)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

```python
from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="GuminiResearch/Gumini-1B-Base",
)

prompt = "저는 구미니입니다."
output = generator(prompt, max_new_tokens=100, temperature=0.7, repetition_penalty=1.2)

print(output[0]["generated_text"])
```
---
## Limitations

- **Base model**: no instruction-tuning or safety alignment  
- **High repetition risk**: use `repetition_penalty >= 1.2`  
- May generate **incorrect or outdated information**  
- Should not be used in **sensitive or safety-critical** contexts  

## License

### Qwen Research License (Non-Commercial)

This model is **Built with Qwen** and derived from Qwen 2.5 3B.

```
Qwen is licensed under the Qwen RESEARCH LICENSE AGREEMENT.
Copyright (c) Alibaba Cloud. All Rights Reserved.
```

**This model is for NON-COMMERCIAL / RESEARCH use only.**  
For commercial use, contact Alibaba Cloud.

### Inheritune Paper (CC BY 4.0)

```bibtex
@inproceedings{Sanyal2024inheritune,
  title={Inheritune: Training Smaller Yet More Attentive Language Models},
  author={Sunny Sanyal and Ravid Shwartz-Ziv and Alexandros G. Dimakis and Sujay Sanghavi},
  year={2024},
  url={https://arxiv.org/abs/2404.08634}
}
```

## Citation

```bibtex
@misc{gumini2025,
  title={Gumini-1B: Bilingual Language Model Built with Qwen via Inheritune},
  author={Gumin Kwon},
  year={2025},
  note={Built with Qwen},
  url={https://huggingface.co/GuminiResearch/Gumini-1B-Base}
}
```

## Author

**[Gumin Kwon (권구민)](https://linkedin.com/in/devgumin)**  
- LinkedIn: [linkedin.com/in/devgumin](https://linkedin.com/in/devgumin)
- HuggingFace: [GuminiResearch](https://huggingface.co/GuminiResearch)

---

<p align="center">
  <b>Built with Qwen</b><br>
  <i>Gumini - 작지만 똑똑한 AI</i>
</p>
