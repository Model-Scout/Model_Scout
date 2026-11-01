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
- arcee-ai/Trinity-Nano-Preview
base_model_relation: quantized
license_link: LICENSE
license_name: openmdw-1.1
---
<div align="center">
  <picture>
    <img
      src="https://cdn-uploads.huggingface.co/production/uploads/6435718aaaef013d1aec3b8b/i-v1KyAMOW_mgVGeic9WJ.png"
      alt="Arcee Trinity Nano Preview"
      style="max-width: 100%; height: auto;"
    >
  </picture>
</div>

# Trinity Nano Preview FP8-Block

Trinity Nano Preview is a preview of Arcee AI's 6B MoE model with 1B active parameters. It is the small-sized model in our new Trinity family, a series of open-weight models for enterprise and tinkerers alike.

This is a chat tuned model, with a delightful personality and charm we think users will love. We note that this model is pushing the limits of sparsity in small language models with only 800M non-embedding parameters active per token, and as such **may be unstable** in certain use cases, especially in this preview.

This is an *experimental* release, it's fun to talk to but will not be hosted anywhere, so download it and try it out yourself!

***

Trinity Nano Preview is trained on 10T tokens gathered and curated through a key partnership with [Datology](https://www.datologyai.com/), building upon the excellent dataset we used on [AFM-4.5B](https://huggingface.co/arcee-ai/AFM-4.5B) with additional math and code.

Training was performed on a cluster of 512 H200 GPUs powered by [Prime Intellect](https://www.primeintellect.ai/) using HSDP parallelism.

More details, including key architecture decisions, can be found on our blog [here](https://www.arcee.ai/blog/the-trinity-manifesto)

***

**This repository contains the FP8 block-quantized weights of Trinity-Nano-Preview (FP8 weights and activations with per-block scaling).**

## Model Details

* **Model Architecture:** AfmoeForCausalLM
* **Parameters:** 6B, 1B active
* **Experts:** 128 total, 8 active, 1 shared
* **Context length:** 128k
* **Training Tokens:** 10T
* **License:** [OpenMDW-1.1](https://huggingface.co/arcee-ai/Trinity-Nano-Preview#license)

***

<div align="center">
  <picture>
      <img src="https://cdn-uploads.huggingface.co/production/uploads/6435718aaaef013d1aec3b8b/sSVjGNHfrJKmQ6w8I18ek.png" style="background-color:ghostwhite;padding:5px;" width="17%" alt="Powered by Datology">
  </picture>
</div>

## Quantization Details

- **Scheme:** `FP8 Block` (FP8 weights and activations, per-block scaling with E8M0 scale format)
- **Format:** `compressed-tensors`
- **Intended use:** High-throughput FP8 deployment of Trinity-Nano-Preview with near-lossless quality, optimized for NVIDIA Hopper/Blackwell GPUs
- **Supported backends:** [DeepGEMM](https://github.com/deepseek-ai/DeepGEMM), vLLM CUTLASS, Triton

### Running our model

- [VLLM](https://huggingface.co/arcee-ai/Trinity-Nano-Preview-FP8-Block#vllm)
- [Transformers](https://huggingface.co/arcee-ai/Trinity-Nano-Preview-FP8-Block#transformers)

## VLLM

Supported in VLLM release 0.18.0+ with DeepGEMM FP8 MoE acceleration.

```
# pip
pip install "vllm>=0.18.0"
```

Serving the model with DeepGEMM enabled:

```
VLLM_USE_DEEP_GEMM=1 vllm serve arcee-ai/Trinity-Nano-Preview-FP8-Block \
  --trust-remote-code \
  --max-model-len 4096 \
  --enable-auto-tool-choice \
  --reasoning-parser deepseek_r1 \
  --tool-call-parser hermes
```

Serving without DeepGEMM (falls back to CUTLASS/Triton):

```
vllm serve arcee-ai/Trinity-Nano-Preview-FP8-Block \
  --trust-remote-code \
  --max-model-len 4096 \
  --enable-auto-tool-choice \
  --reasoning-parser deepseek_r1 \
  --tool-call-parser hermes
```

## Transformers

Use the `main` transformers branch

```
git clone https://github.com/huggingface/transformers.git
cd transformers

# pip
pip install '.[torch]'

# uv
uv pip install '.[torch]'
```

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "arcee-ai/Trinity-Nano-Preview-FP8-Block"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True
)

messages = [
    {"role": "user", "content": "Who are you?"},
]

input_ids = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

outputs = model.generate(
    input_ids,
    max_new_tokens=256,
    do_sample=True,
    temperature=0.5,
    top_k=50,
    top_p=0.95
)

response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

## License

Trinity-Nano-Preview-FP8-Block is released under the OpenMDW-1.1 license.