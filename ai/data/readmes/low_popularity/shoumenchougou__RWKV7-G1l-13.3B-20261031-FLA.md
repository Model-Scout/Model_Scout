---
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
base_model: BlinkDL/rwkv7-g1
language:
- en
- zh
- fr
- es
- de
- pt
- ru
- it
- ja
- ko
- vi
- ar
tags:
- rwkv
- rwkv7
- fla
- recurrent
- causal-lm
---

<!-- markdownlint-disable first-line-h1 -->
<!-- markdownlint-disable html -->

<div align="center">
  <a href="https://www.rwkv.com/">
    <img src="assets/rwkv-logo.webp" width="140" alt="RWKV logo" />
  </a>
  <h1>RWKV7-G1l-13.3B-20261031-FLA</h1>
  <p><strong>RWKV-7 “Goose” in Flash Linear Attention format</strong></p>
</div>

This repository provides the **RWKV-7 G1l 13.3B** checkpoint in the
[`flash-linear-attention`](https://github.com/fla-org/flash-linear-attention)
(FLA) RWKV7 layout for Transformers-compatible inference.

> [!IMPORTANT]
> This is a base language model, not a safety-aligned instruction-tuned
> assistant. The included chat template provides a conversational prompt
> format, but the model may not follow instructions consistently.

## About RWKV-7

RWKV-7, also called **Goose**, is an attention-free recurrent language model.
It maintains a constant-size recurrent state instead of an attention KV cache
that grows with the preceding sequence. Training remains parallelizable, while
recurrent decoding uses constant state size and constant work per generated
token with respect to sequence length.

`G1l` identifies this checkpoint revision. The source checkpoint is available
from [`BlinkDL/rwkv7-g1`](https://huggingface.co/BlinkDL/rwkv7-g1).

## Model details

| Property | Value |
| --- | --- |
| Architecture | RWKV-7 G1l |
| Parameters in this FLA checkpoint | 13.269B |
| Layers | 61 |
| Hidden size | 4,096 |
| Heads | 64 × 64 |
| Feed-forward size | 16,384 |
| Vocabulary | RWKV World tokenizer, 65,536 tokens |
| Configured context length | 34,304 tokens |
| Weight dtype | BF16 |
| License | Apache-2.0 |

## Run with FLA

Use a CUDA-capable NVIDIA GPU with BF16 support. Install the audited FLA
revision with its CUDA dependency extra:

```bash
python -m pip install \
  "flash-linear-attention[cuda] @ git+https://github.com/fla-org/flash-linear-attention.git@8e84ed4a6727be082c34a3855c60623fd11411e9" \
  "transformers>=4.50.2"
```

Import `fla` before using the Auto classes so that the RWKV7 implementation is
registered:

```python
import fla
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "shoumenchougou/RWKV7-G1l-13.3B-20261031-FLA"

tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
).to("cuda").eval()

messages = [
    {"role": "user", "content": "Explain recurrent language models in one paragraph."}
]
prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    thinking=False,
)
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

with torch.inference_mode():
    output_ids = model.generate(
        **inputs,
        max_new_tokens=128,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
    )

new_tokens = output_ids[0, inputs.input_ids.shape[1]:]
print(tokenizer.decode(new_tokens, skip_special_tokens=True))
```

Set `thinking=True` when applying the chat template to leave an open thinking
prefix. This changes only the prompt format; it does not turn the base model
into an instruction-tuned or safety-aligned assistant.

## Compatibility and validation

The package was checked with FLA commit
`8e84ed4a6727be082c34a3855c60623fd11411e9` and Transformers 4.50.2. Its
configuration, tokenizer, chat template, BF16 weights, and Transformers model
loading were validated locally. All 2,016 model tensors load into
`RWKV7ForCausalLM` without missing, unexpected, or mismatched keys.

CUDA/Triton generation was not executed in the local CPU-only validation
environment. Runtime behavior can depend on the GPU, CUDA, PyTorch, Triton,
and FLA versions. Cross-check benchmark or evaluation results against the
official RWKV implementation before reporting them.

## References

- [RWKV-7 paper](https://arxiv.org/abs/2503.14456)
- [RWKV-LM](https://github.com/BlinkDL/RWKV-LM)
- [Flash Linear Attention](https://github.com/fla-org/flash-linear-attention)
- [Source checkpoint repository](https://huggingface.co/BlinkDL/rwkv7-g1)
