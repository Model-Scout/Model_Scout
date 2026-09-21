---
license: other
language:
- en
- es
- fr
- de
- it
- pt
- ru
- ar
- hi
- ko
- zh
library_name: transformers
base_model:
- arcee-ai/Trinity-Large-Thinking
base_model_relation: quantized
tags:
- reasoning
- agentic
- tool-calling
- thinking
license_link: LICENSE
license_name: openmdw-1.1
---
<!-- markdownlint-disable first-line-h1 -->
<!-- markdownlint-disable html -->
<!-- markdownlint-disable no-duplicate-header -->

<div align="center">
  <picture>
    <img
      src="https://cdn-uploads.huggingface.co/production/uploads/6435718aaaef013d1aec3b8b/i-v1KyAMOW_mgVGeic9WJ.png"
      alt="Arcee Trinity Large Thinking"
      style="max-width: 100%; height: auto;"
    >
  </picture>
</div>
<hr>

# Trinity-Large-Thinking-W4A16

## Introduction

Trinity-Large-Thinking is a reasoning-optimized variant of Arcee AI's Trinity-Large family — a 398B-parameter sparse Mixture-of-Experts (MoE) model with approximately 13B active parameters per token, post-trained with extended chain-of-thought reasoning and agentic RL.

**This repository contains the W4A16 quantized weights of Trinity-Large-Thinking (INT4 weights, 16-bit activations).**

For full model details, benchmarks, and usage guidance, see the main [Trinity-Large-Thinking](https://huggingface.co/arcee-ai/Trinity-Large-Thinking) model card.

## Quantization Details

- **Scheme:** `W4A16` (INT4 weights, 16-bit activations)
- **Intended use:** Quality-preserving 4-bit deployment of Trinity-Large-Thinking

## Usage

### Inference tested on

- 8x NVIDIA H100 80GB (tensor parallel = 8)
- vLLM 0.15.1+

### vLLM

Supported in vLLM 0.15.1+.

```bash
vllm serve arcee-ai/Trinity-Large-Thinking-W4A16 \
  --trust-remote-code \
  --tensor-parallel-size 8 \
  --enable-reasoning \
  --reasoning-parser deepseek_r1 \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder
```

### Transformers

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "arcee-ai/Trinity-Large-Thinking-W4A16"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    trust_remote_code=True
)

messages = [{"role": "user", "content": "Who are you?"}]

input_ids = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt"
).to(model.device)

outputs = model.generate(input_ids, max_new_tokens=4096, do_sample=True, temperature=0.6, top_k=50, top_p=0.95)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

### API

Works out of the box on [OpenRouter](https://openrouter.ai/) as `arcee-ai/trinity-large-thinking`.

## License

Trinity-Large-Thinking-W4A16 is released under the OpenMDW License, version 1.1 (OpenMDW-1.1).

## Citation

If you use this model, please cite:

```bibtex
@misc{singh2026arceetrinity,
  title        = {Arcee Trinity Large Technical Report},
  author       = {Varun Singh and Lucas Krauss and Sami Jaghouar and Matej Sirovatka and Charles Goddard and Fares Obied and Jack Min Ong and Jannik Straube and Fern and Aria Harley and Conner Stewart and Colin Kealty and Maziyar Panahi and Simon Kirsten and Anushka Deshpande and Anneketh Vij and Arthur Bresnu and Pranav Veldurthi and Raghav Ravishankar and Hardik Bishnoi and DatologyAI Team and Arcee AI Team and Prime Intellect Team and Mark McQuade and Johannes Hagemann and Lucas Atkins},
  year         = {2026},
  eprint       = {2602.17004},
  archivePrefix= {arXiv},
  primaryClass = {cs.LG},
  doi          = {10.48550/arXiv.2602.17004},
  url          = {https://arxiv.org/abs/2602.17004}
}
```