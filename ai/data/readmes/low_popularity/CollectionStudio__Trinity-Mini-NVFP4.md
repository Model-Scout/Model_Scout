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
      alt="Arcee Trinity Mini"
      style="max-width: 100%; height: auto;"
    >
  </picture>
</div>

# Trinity Mini NVFP4

**This repository contains the NVFP4 quantized weights of Trinity-Mini for deployment on NVIDIA Blackwell GPUs.**

Trinity Mini is an Arcee AI 26B MoE model with 3B active parameters. It is the medium-sized model in our new Trinity family, a series of open-weight models for enterprise and tinkerers alike.

This model is tuned for reasoning, but in testing, it uses a similar total token count to competitive instruction-tuned models.

***

Trinity Mini is trained on 10T tokens gathered and curated through a key partnership with [Datology](https://www.datologyai.com/), building upon the excellent dataset we used on [AFM-4.5B](https://huggingface.co/arcee-ai/AFM-4.5B) with additional math and code.

Training was performed on a cluster of 512 H200 GPUs powered by [Prime Intellect](https://www.primeintellect.ai/) using HSDP parallelism.

More details, including key architecture decisions, can be found on our blog [here](https://www.arcee.ai/blog/the-trinity-manifesto)

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

## Benchmarks

![](https://cdn-uploads.huggingface.co/production/uploads/6435718aaaef013d1aec3b8b/UMV0OZh_H1JfvgzBTXh6u.png)

<div align="center">
  <picture>
      <img src="https://cdn-uploads.huggingface.co/production/uploads/6435718aaaef013d1aec3b8b/sSVjGNHfrJKmQ6w8I18ek.png" style="background-color:ghostwhite;padding:5px;" width="17%" alt="Powered by Datology">
  </picture>
</div>

## Quantization Details

- **Scheme:** NVFP4 (`nvfp4_mlp_only` — MLP/expert weights only, attention remains BF16)
- **Tool:** [NVIDIA ModelOpt](https://github.com/NVIDIA/Model-Optimizer)
- **Calibration:** 512 samples, seq_length=2048, all-expert calibration enabled
- **KV cache:** Not quantized

## Running with vLLM

Requires [vLLM](https://github.com/vllm-project/vllm) >= 0.18.0. Native FP4 compute requires Blackwell GPUs; older GPUs fall back to Marlin weight decompression automatically.

### Blackwell GPUs (B200/B300/GB300) — Docker (recommended)

```bash
docker run --runtime nvidia --gpus all -p 8000:8000 \
  -v ~/.cache/huggingface:/root/.cache/huggingface \
  vllm/vllm-openai:v0.18.0-cu130 \
  arcee-ai/Trinity-Mini-NVFP4 \
  --trust-remote-code \
  --gpu-memory-utilization 0.90 \
  --max-model-len 8192
```

### Hopper GPUs (H100/H200) and others

```bash
vllm serve arcee-ai/Trinity-Mini-NVFP4 \
  --trust-remote-code \
  --gpu-memory-utilization 0.90 \
  --max-model-len 8192 \
  --host 0.0.0.0 \
  --port 8000
```

 **Note (Blackwell pip installs):** If installing vLLM via pip on Blackwell rather than using Docker, native FP4 kernels may produce incorrect output due to package version mismatches. As a workaround, force the Marlin backend:

 ```bash
 export VLLM_NVFP4_GEMM_BACKEND=marlin

 vllm serve arcee-ai/Trinity-Mini-NVFP4 \
   --trust-remote-code \
   --moe-backend marlin \
   --gpu-memory-utilization 0.90 \
   --max-model-len 8192 \
   --host 0.0.0.0 \
   --port 8000
 ```

Marlin decompresses FP4 weights to BF16 for compute, providing the full memory compression benefit (~3.7× vs BF16) but not native FP4 compute speedup. On Hopper GPUs (H100/H200), Marlin is selected automatically and no extra flags are needed.

## License

Trinity-Mini-NVFP4 is released under the OpenMDW-1.1 license.