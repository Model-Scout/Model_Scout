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
library_name: mlx
base_model: arcee-ai/Trinity-Nano-Preview
tags:
- mlx
pipeline_tag: text-generation
license_link: LICENSE
license_name: openmdw-1.1
---

<div align="center">
  <picture>
    <img
      src="https://cdn-uploads.huggingface.co/production/uploads/6435718aaaef013d1aec3b8b/i-v1KyAMOW_mgVGeic9WJ.png"
      alt="Arcee Trinity Mini"
      style="max-width: 100%; height: auto;"
    >
  </picture>
</div>

# Trinity Nano MLX 6bit

Trinity Nano Preview is a preview of Arcee AI's 6B MoE model with 1B active parameters. It is the small-sized model in our new Trinity family, a series of open-weight models for enterprise and tinkerers alike.

This is a chat tuned model, with a delightful personality and charm we think users will love. We note that this model is pushing the limits of sparsity in small language models with only 800M non-embedding parameters active per token, and as such **may be unstable** in certain use cases, especially in this preview.

This is an *experimental* release, it's fun to talk to but will not be hosted anywhere, so download it and try it out yourself!

***

Trinity Nano Preview is trained on 10T tokens gathered and curated through a key partnership with [Datology](https://www.datologyai.com/), building upon the excellent dataset we used on [AFM-4.5B](https://huggingface.co/arcee-ai/AFM-4.5B) with additional math and code.

Training was performed on a cluster of 512 H200 GPUs powered by [Prime Intellect](https://www.primeintellect.ai/) using HSDP parallelism.

More details, including key architecture decisions, can be found on our blog [here](https://www.arcee.ai/blog/the-trinity-manifesto)

***

## Model Details

* **Model Architecture:** AfmoeForCausalLM
* **Parameters:** 6B, 1B active
* **Experts:** 128 total, 8 active, 1 shared
* **Context length:** 128k
* **Training Tokens:** 10T
* **License:** [OpenMDW-1.1](https://huggingface.co/arcee-ai/Trinity-Mini#license)

## Use with mlx

```
pip install mlx-lm
```

```python
from mlx_lm import load, generate
from mlx_lm.sample_utils import make_sampler, make_logits_processors

model, tokenizer = load("arcee-ai/Trinity-Nano-Preview-MLX-6bit")

prompt = "What is the capital of France?"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

sampler = make_sampler(temp=0.1, top_k=50, top_p=0.1)
logits_processors = make_logits_processors(repetition_penalty=1.05)

response = generate(
    model,
    tokenizer,
    prompt=prompt,
    max_tokens=512,
    sampler=sampler,
    logits_processors=logits_processors,
    verbose=True,
)
```

