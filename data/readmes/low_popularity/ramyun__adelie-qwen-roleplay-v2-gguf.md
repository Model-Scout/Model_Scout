---
license: other
license_name: tongyi-qianwen
license_link: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/LICENSE
base_model: Qwen/Qwen2.5-7B-Instruct
base_model_relation: quantized
language:
  - ko
  - en
library_name: gguf
pipeline_tag: text-generation
tags:
  - gguf
  - quantized
  - q4_k_m
  - llama.cpp
  - korean
  - roleplay
  - persona
  - qwen2.5
---

# AdelieAI · Qwen-Roleplay v2 (GGUF q4_k_m)

CPU-friendly **q4_k_m quantization** of the merged
`Qwen2.5-7B-Instruct + adelie-qwen-roleplay-v2-lora` checkpoint.
Ships in a single 4.4 GB file — runs on a laptop without a GPU.

> Companion to the LoRA adapter at
> [`ramyun/adelie-qwen-roleplay-v2-lora`](https://huggingface.co/ramyun/adelie-qwen-roleplay-v2-lora).
> The LoRA repo is for FP16 + GPU mounting; this GGUF is for laptops /
> end-users without CUDA.

## How to use

### llama.cpp / llama-cpp-python

```bash
pip install llama-cpp-python --only-binary=:all: \
    --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu

huggingface-cli download ramyun/adelie-qwen-roleplay-v2-gguf \
    qwen-roleplay-v2.q4_k_m.gguf --local-dir ./models
```

```python
from llama_cpp import Llama

llm = Llama(
    model_path="./models/qwen-roleplay-v2.q4_k_m.gguf",
    n_ctx=4096,
    n_threads=8,
)
out = llm.create_chat_completion(
    messages=[
        {"role": "system", "content": "당신은 판타지 세계의 냉소적인 잡화상 주인입니다."},
        {"role": "user", "content": "할인 좀 안 돼요?"},
    ],
    temperature=0.7,
)
print(out["choices"][0]["message"]["content"])
```

### Or mount via the AdelieAI engine

```bash
huggingface-cli download ramyun/adelie-qwen-roleplay-v2-gguf \
    qwen-roleplay-v2.q4_k_m.gguf \
    --local-dir models/ours/qwen-roleplay-v2-gguf

MODEL_PATH=models/ours/qwen-roleplay-v2-gguf/qwen-roleplay-v2.q4_k_m.gguf \
PYTHONUTF8=1 .venv/Scripts/uvicorn core.api.app:app --port 8770
```

## Quantization details

| | |
|---|---|
| Source | merged FP16 (`Qwen2.5-7B-Instruct + adelie-qwen-roleplay-v2-lora`) |
| Method | llama.cpp `convert_hf_to_gguf.py` → `quantize` to `q4_k_m` |
| Original size | 14.5 GB (FP16) |
| **Quantized size** | **4.4 GB** (3.25× compression) |
| Runtime VRAM | 0 (pure CPU) |
| Runtime RAM | ~5 GB |

Style preservation verified: 4/5 persona prompts + 5/5 general prompts pass under greedy decoding (see [`recipe.md`](./recipe.md)).

## Recommended sampling

`temperature=0.7` and `top_p=0.9`. Greedy decoding (`temperature=0`) sometimes diverges on q4_k_m — known quantization artifact, mitigated by sampling.

## License

Inherits the **Tongyi Qianwen License v1** from the base model
(`Qwen/Qwen2.5-7B-Instruct`).

## Citation

```bibtex
@software{adelieai_2026,
  title  = {AdelieAI: a persona engine for small-deployment LLMs},
  author = {ramyun},
  year   = {2026},
  url    = {https://github.com/southglory/AdelieAI}
}
```
