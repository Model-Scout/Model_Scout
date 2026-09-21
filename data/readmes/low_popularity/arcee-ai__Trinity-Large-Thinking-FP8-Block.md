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

# Trinity-Large-Thinking-FP8-Block

## Introduction

Trinity-Large-Thinking is a reasoning-optimized variant of Arcee AI's Trinity-Large family — a 398B-parameter sparse Mixture-of-Experts (MoE) model with approximately 13B active parameters per token, post-trained with extended chain-of-thought reasoning and agentic RL.

**This repository contains the FP8 block-quantized weights of Trinity-Large-Thinking (FP8 weights and activations with per-block scaling).**

For full model details, benchmarks, and usage guidance, see the main [Trinity-Large-Thinking](https://huggingface.co/arcee-ai/Trinity-Large-Thinking) model card.

## Quantization Details

- **Scheme:** `FP8 Block` (FP8 weights and activations, per-block scaling with E8M0 scale format)
- **Format:** `compressed-tensors`
- **Intended use:** High-throughput FP8 deployment with near-lossless quality, optimized for NVIDIA Hopper/Blackwell GPUs
- **Supported backends:** [DeepGEMM](https://github.com/deepseek-ai/DeepGEMM), vLLM CUTLASS, Triton

## Usage

### Inference tested on

- 8x NVIDIA H100 80GB (tensor parallel = 8)
- vLLM 0.18.0+

### vLLM

Supported in vLLM 0.18.0+ with DeepGEMM FP8 MoE acceleration.

```bash
pip install "vllm>=0.18.0"
```

Serving with DeepGEMM enabled (recommended):

```bash
VLLM_USE_DEEP_GEMM=1 vllm serve arcee-ai/Trinity-Large-Thinking-FP8-Block \
  --trust-remote-code \
  --tensor-parallel-size 8 \
  --enable-reasoning \
  --reasoning-parser deepseek_r1 \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder
```

Without DeepGEMM (falls back to CUTLASS/Triton):

```bash
vllm serve arcee-ai/Trinity-Large-Thinking-FP8-Block \
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

model_id = "arcee-ai/Trinity-Large-Thinking-FP8-Block"
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

Trinity-Large-Thinking-FP8-Block is released under the OpenMDW License, version 1.1 (OpenMDW-1.1).

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