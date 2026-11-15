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
- moe
- nvfp4
- modelopt
- blackwell
- vllm
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

# Trinity-Large-Thinking-NVFP4

## Introduction

Trinity-Large-Thinking is a reasoning-optimized variant of Arcee AI's Trinity-Large family — a 398B-parameter sparse Mixture-of-Experts (MoE) model with approximately 13B active parameters per token, post-trained with extended chain-of-thought reasoning and agentic RL.

**This repository contains the NVFP4 quantized weights of Trinity-Large-Thinking for deployment on NVIDIA Blackwell GPUs.**

For full model details, benchmarks, and usage guidance, see the main [Trinity-Large-Thinking](https://huggingface.co/arcee-ai/Trinity-Large-Thinking) model card.

## Quantization Details

- **Scheme:** NVFP4 (`nvfp4_experts_only` — MoE expert weights only, attention and dense layers remain BF16)
- **Tool:** [NVIDIA ModelOpt](https://github.com/NVIDIA/Model-Optimizer)
- **Calibration:** 2048 samples, seq_length=4096
- **KV cache:** Not quantized

## Usage

### Inference tested on

- Both Hopper (via Marlin) and Blackwell B300 node
- vLLM 0.18.0+

### vLLM

Requires [vLLM](https://github.com/vllm-project/vllm) >= 0.18.0. Native FP4 compute requires Blackwell GPUs; older GPUs fall back to Marlin weight decompression automatically.

#### Example Blackwell GPUs (B200/B300/GB300) — Docker (recommended)

```bash
docker run --runtime nvidia --gpus all -p 8000:8000 \
  -v ~/.cache/huggingface:/root/.cache/huggingface \
  vllm/vllm-openai:v0.18.0-cu130 \
  arcee-ai/Trinity-Large-Thinking-NVFP4 \
  --trust-remote-code \
  --tensor-parallel-size 8 \
  --gpu-memory-utilization 0.90 \
  --max-model-len 8192 \
  --enable-reasoning \
  --reasoning-parser deepseek_r1 \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder
```

#### Hopper GPUs (H100/H200) and others

```bash
vllm serve arcee-ai/Trinity-Large-Thinking-NVFP4 \
  --trust-remote-code \
  --tensor-parallel-size 8 \
  --gpu-memory-utilization 0.90 \
  --max-model-len 8192 \
  --enable-reasoning \
  --reasoning-parser deepseek_r1 \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder
```

> **Note (For Blackwell pip installs):** If installing vLLM via pip on Blackwell rather than using Docker, native FP4 kernels may produce incorrect output due to package version mismatches. As a workaround, force the Marlin backend:
>
> ```bash
> export VLLM_NVFP4_GEMM_BACKEND=marlin
>
> vllm serve arcee-ai/Trinity-Large-Thinking-NVFP4 \
>   --trust-remote-code \
>   --tensor-parallel-size 8 \
>   --moe-backend marlin \
>   --gpu-memory-utilization 0.90 \
>   --max-model-len 8192 \
>   --enable-reasoning \
>   --reasoning-parser deepseek_r1 \
>   --enable-auto-tool-choice \
>   --tool-call-parser qwen3_coder
> ```
>
> Marlin decompresses FP4 weights to BF16 for compute, providing the full memory compression benefit but not native FP4 compute speedup. On Hopper GPUs (H100/H200), Marlin is selected automatically and no extra flags are needed.

### Transformers

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "arcee-ai/Trinity-Large-Thinking-NVFP4"
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

outputs = model.generate(input_ids, max_new_tokens=4096, do_sample=True, temperature=0.3, top_p=0.95)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

### API

Works out of the box on [OpenRouter](https://openrouter.ai/) as `arcee-ai/trinity-large-thinking`.

## License

Trinity-Large-Thinking-NVFP4 is released under the OpenMDW License, version 1.1 (OpenMDW-1.1).

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