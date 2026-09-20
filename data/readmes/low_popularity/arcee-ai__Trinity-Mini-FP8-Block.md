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
- arcee-ai/Trinity-Mini
base_model_relation: quantized
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

# Trinity Mini FP8-Block

**This repository contains the FP8 block-quantized weights of Trinity-Mini (FP8 weights and activations with per-block scaling).**

Trinity Mini is an Arcee AI 26B MoE model with 3B active parameters. It is the medium-sized model in our new Trinity family, a series of open-weight models for enterprise and tinkerers alike.

This model is tuned for reasoning, but in testing, it uses a similar total token count to competitive instruction-tuned models.

***

Trinity Mini is trained on 10T tokens gathered and curated through a key partnership with [Datology](https://www.datologyai.com/), building upon the excellent dataset we used on [AFM-4.5B](https://huggingface.co/arcee-ai/AFM-4.5B) with additional math and code.

Training was performed on a cluster of 512 H200 GPUs powered by [Prime Intellect](https://www.primeintellect.ai/) using HSDP parallelism.

More details, including key architecture decisions, can be found on our blog [here](https://www.arcee.ai/blog/the-trinity-manifesto)

Try it out now at [chat.arcee.ai](http://chat.arcee.ai/)

***

## Model Details

* **Model Architecture:** AfmoeForCausalLM
* **Parameters:** 26B, 3B active
* **Experts:** 128 total, 8 active, 1 shared
* **Context length:** 128k
* **Training Tokens:** 10T
* **License:** [OpenMDW-1.1](https://huggingface.co/arcee-ai/Trinity-Mini#license)
* **Recommended settings:**
    * temperature: 0.15
    * top_k: 50
    * top_p: 0.75
    * min_p: 0.06

***

## Quantization Details

- **Scheme:** `FP8 Block` (FP8 weights and activations, per-block scaling with E8M0 scale format)
- **Format:** `compressed-tensors`
- **Intended use:** High-throughput FP8 deployment of Trinity-Mini with near-lossless quality, optimized for NVIDIA Hopper GPUs
- **Supported backends:** [DeepGEMM](https://github.com/deepseek-ai/DeepGEMM), vLLM CUTLASS, Triton

## Benchmarks

![](https://cdn-uploads.huggingface.co/production/uploads/6435718aaaef013d1aec3b8b/UMV0OZh_H1JfvgzBTXh6u.png)

<div align="center">
  <picture>
      <img src="https://cdn-uploads.huggingface.co/production/uploads/6435718aaaef013d1aec3b8b/sSVjGNHfrJKmQ6w8I18ek.png" style="background-color:ghostwhite;padding:5px;" width="17%" alt="Powered by Datology">
  </picture>
</div>

### Running our model

- [VLLM](https://huggingface.co/arcee-ai/Trinity-Mini-FP8-Block#vllm)
- [Transformers](https://huggingface.co/arcee-ai/Trinity-Mini-FP8-Block#transformers)

## VLLM

Supported in VLLM release 0.18.0+ with DeepGEMM FP8 MoE acceleration.

```
# pip
pip install "vllm>=0.18.0"
```

Serving the model with DeepGEMM enabled:

```
VLLM_USE_DEEP_GEMM=1 vllm serve arcee-ai/Trinity-Mini-FP8-Block \
  --trust-remote-code \
  --max-model-len 4096 \
  --enable-auto-tool-choice \
  --reasoning-parser deepseek_r1 \
  --tool-call-parser hermes
```

Serving without DeepGEMM (falls back to CUTLASS/Triton):

```
vllm serve arcee-ai/Trinity-Mini-FP8-Block \
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

model_id = "arcee-ai/Trinity-Mini-FP8-Block"
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
    temperature=0.15,
    top_k=50,
    top_p=0.75,
    min_p=0.06
)

response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

## API

Trinity Mini is available today on openrouter:

https://openrouter.ai/arcee-ai/trinity-mini

```
curl -X POST "https://openrouter.ai/v1/chat/completions" \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "arcee-ai/trinity-mini",
    "messages": [
      {
        "role": "user",
        "content": "What are some fun things to do in New York?"
      }
    ]
  }'
```

## License

Trinity-Mini-FP8-Block is released under the OpenMDW-1.1 license.