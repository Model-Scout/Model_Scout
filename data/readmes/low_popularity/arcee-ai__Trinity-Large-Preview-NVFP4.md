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
- arcee-ai/Trinity-Large-Preview
base_model_relation: quantized
tags:
- moe
- nvfp4
- modelopt
- blackwell
- vllm
license_link: LICENSE
license_name: openmdw-1.1
---

<div align="center">
  <picture>
    <img
      src="https://cdn-uploads.huggingface.co/production/uploads/6435718aaaef013d1aec3b8b/i-v1KyAMOW_mgVGeic9WJ.png"
      alt="Arcee Trinity Large"
      style="max-width: 100%; height: auto;"
    >
  </picture>
</div>
<hr>

# Trinity-Large-Preview-NVFP4

**This repository contains the NVFP4 quantized weights of Trinity-Large-Preview for deployment on NVIDIA Blackwell GPUs.**

Trinity-Large-Preview is a 398B-parameter sparse Mixture-of-Experts (MoE) model with approximately 13B active parameters per token. It is the largest model in Arcee AI's Trinity family, trained on more than 17 trillion tokens and delivering frontier-level performance with strong long-context comprehension.
Trinity-Large-Preview is a lightly post-trained model based on Trinity-Large-Base.

Try it at [chat.arcee.ai](http://chat.arcee.ai/)

More details on the training of Trinity Large are available in the [technical report](https://arxiv.org/abs/2602.17004).

***

## Quantization Details

- **Scheme:** NVFP4 (`nvfp4_mlp_only` — MLP/expert weights only, attention remains BF16)
- **Tool:** [NVIDIA ModelOpt](https://github.com/NVIDIA/Model-Optimizer)
- **Calibration:** 512 samples, seq_length=2048, all-expert calibration enabled
- **KV cache:** Not quantized

***

## Model Variants

The Trinity Large family consists of three checkpoints from the same training run:

- **[Trinity-Large-Preview](https://huggingface.co/arcee-ai/Trinity-Large-Preview)**: Lightly post-trained, chat-ready model undergoing active RL
- **[Trinity-Large-TrueBase](https://huggingface.co/arcee-ai/Trinity-Large-TrueBase)**: 10T-token pre-anneal pretraining checkpoint
- **[Trinity-Large-Base](https://huggingface.co/arcee-ai/Trinity-Large-Base)**: Full 17T-token pretrained foundation model with mid-training anneals

## Architecture

| Hyperparameter | Value |
|:---|:---:|
| Total parameters | ~398B |
| Active parameters per token | ~13B |
| Experts | 256 (1 shared) |
| Active experts | 4 |
| Routing strategy | 4-of-256 (1.56% sparsity) |
| Dense layers | 6 |
| Pretraining context length | 8,192 |
| Context length after extension | 512k |
| Architecture | Sparse MoE (AfmoeForCausalLM) |

## Benchmarks

| Benchmark | Llama 4 Maverick | Trinity-Large Preview |
|-----------|------------------|----------------------|
| MMLU | 85.5 | 87.2 |
| MMLU-Pro | 80.5 | 75.2 |
| GPQA-Diamond | 69.8 | 63.3 |
| AIME 2025 | 19.3 | 24.0 |

***

## Running with vLLM

Requires [vLLM](https://github.com/vllm-project/vllm) >= 0.18.0. Native FP4 compute requires Blackwell GPUs; older GPUs fall back to Marlin weight decompression automatically.

### Blackwell GPUs (B200/B300/GB300) — Docker (recommended)

```bash
docker run --runtime nvidia --gpus all -p 8000:8000 \
  -v ~/.cache/huggingface:/root/.cache/huggingface \
  vllm/vllm-openai:v0.18.0-cu130 \
  arcee-ai/Trinity-Large-Preview-NVFP4 \
  --trust-remote-code \
  --tensor-parallel-size 8 \
  --gpu-memory-utilization 0.90 \
  --max-model-len 8192
```

### Hopper GPUs (H100/H200) and others

```bash
vllm serve arcee-ai/Trinity-Large-Preview-NVFP4 \
  --trust-remote-code \
  --tensor-parallel-size 8 \
  --gpu-memory-utilization 0.90 \
  --max-model-len 8192 \
  --host 0.0.0.0 \
  --port 8000
```

 **Note (Blackwell pip installs):** If installing vLLM via pip on Blackwell rather than using Docker, native FP4 kernels may produce incorrect output due to package version mismatches. As a workaround, force the Marlin backend:

 ```bash
 export VLLM_NVFP4_GEMM_BACKEND=marlin

 vllm serve arcee-ai/Trinity-Large-Preview-NVFP4 \
   --trust-remote-code \
   --tensor-parallel-size 8 \
   --moe-backend marlin \
   --gpu-memory-utilization 0.90 \
   --max-model-len 8192 \
   --host 0.0.0.0 \
   --port 8000
```

Marlin decompresses FP4 weights to BF16 for compute, providing the full memory compression benefit but not native FP4 compute speedup. On Hopper GPUs (H100/H200), Marlin is selected automatically and no extra flags are needed.

### API

Available on OpenRouter:

```bash
curl -X POST "https://openrouter.ai/v1/chat/completions" \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "arcee-ai/trinity-large-preview",
    "messages": [
      {
        "role": "user",
        "content": "What are some fun things to do in New York?"
      }
    ]
  }'
```

***

## License

Trinity-Large-Preview-NVFP4 is released under the OpenMDW License, version 1.1 (OpenMDW-1.1).

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