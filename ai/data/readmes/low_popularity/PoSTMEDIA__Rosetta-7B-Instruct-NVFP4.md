---
license: apache-2.0
language:
  - ko
  - en
pipeline_tag: text-generation
library_name: transformers
base_model: PoSTMEDIA/Rosetta-7B-Instruct
base_model_relation: quantized
tags:
  - rosetta
  - korean
  - bilingual
  - postmedia
  - nvfp4
  - fp4
  - modelopt
---

<div align="center">

# Rosetta-7B-Instruct-NVFP4

[![Collection](https://img.shields.io/badge/Rosetta-Collection-0052CC?style=for-the-badge)](https://huggingface.co/collections/PoSTMEDIA/rosetta-6a9db30fd1b4585b0c1845e9)
[![vLLM](https://img.shields.io/badge/vLLM-PoSTMEDIA--AI-00A3FF?style=for-the-badge&logo=github)](https://github.com/PoSTMEDIA-AI/vllm)
[![License](https://img.shields.io/badge/License-Apache_2.0-7856FF?style=for-the-badge)](./LICENSE)

</div>

## Introduction

**Rosetta-7B-Instruct-NVFP4** is the official **NVFP4 (4-bit floating point)** quantization of [Rosetta-7B-Instruct](https://huggingface.co/PoSTMEDIA/Rosetta-7B-Instruct), PoSTMEDIA's bilingual (Korean-English) instruction-tuned model. It was produced with **NVIDIA TensorRT Model Optimizer** using the official NVFP4 post-training-quantization recipe, and targets **NVIDIA Blackwell** GPUs — DGX Spark, GeForce RTX 50 series, and B200/GB200-class datacenter parts — where vLLM selects native NVFP4 GEMM kernels automatically.

The checkpoint shrinks from **14.5 GB (BF16) to 6.3 GB (~2.3× smaller)**, and because single-stream decoding is dominated by weight memory bandwidth, decode throughput improves substantially on bandwidth-bound devices such as DGX Spark. The same checkpoint also loads on pre-Blackwell GPUs (Hopper, Ada, Ampere) through vLLM's weight-only Marlin fallback — with the identical memory savings.

| Model | Download | Note |
|---|---|---|
| Rosetta-7B-Base | [HuggingFace](https://huggingface.co/PoSTMEDIA/Rosetta-7B-Base) | Foundation model (completion-style) |
| Rosetta-7B-Instruct | [HuggingFace](https://huggingface.co/PoSTMEDIA/Rosetta-7B-Instruct) | Instruction following / chat (BF16) |
| **Rosetta-7B-Instruct-NVFP4** | [HuggingFace](https://huggingface.co/PoSTMEDIA/Rosetta-7B-Instruct-NVFP4) | NVFP4 quantization *(this model)* |
| Rosetta-7B-Think | [HuggingFace](https://huggingface.co/PoSTMEDIA/Rosetta-7B-Think) | Explicit reasoning (`<think>`, BF16) |
| Rosetta-7B-Think-NVFP4 | [HuggingFace](https://huggingface.co/PoSTMEDIA/Rosetta-7B-Think-NVFP4) | NVFP4 quantization of Think |

## Quantization Details

<div align="center">
<table><tbody>
<tr><td><b>Method</b></td><td>NVIDIA TensorRT Model Optimizer (<code>nvidia-modelopt</code> 0.46.1), official NVFP4 PTQ recipe</td></tr>
<tr><td><b>Weight format</b></td><td>NVFP4 — FP4 (E2M1) elements, 16-element blocks, FP8 (E4M3) per-block scales + FP32 per-tensor scale</td></tr>
<tr><td><b>Activations</b></td><td>NVFP4 (W4A4) with calibrated static input scales</td></tr>
<tr><td><b>KV cache</b></td><td>FP8 (E4M3) with calibrated static scales (activated when serving with FP8 KV cache)</td></tr>
<tr><td><b>Kept in BF16</b></td><td>embeddings, <code>lm_head</code>, normalization layers</td></tr>
<tr><td><b>Calibration</b></td><td>1,024 bilingual samples — Korean instruction conversations from PoSTMEDIA's in-house synthetic data assets (8 domains, rendered through the model's chat template) + English news articles</td></tr>
<tr><td><b>Checkpoint size</b></td><td>6.3 GB (vs. 14.5 GB BF16)</td></tr>
<tr><td><b>Format</b></td><td>ModelOpt unified HuggingFace checkpoint (<code>quantization_config</code> + <code>hf_quant_config.json</code>)</td></tr>
</tbody></table>
</div>

In internal side-by-side evaluations against the BF16 model under an identical protocol, output quality is broadly preserved across Korean and English instruction following, knowledge, and math. As with any 4-bit quantization, minor differences can surface on knowledge-recall edge cases; for maximum-accuracy use cases, prefer the [BF16 model](https://huggingface.co/PoSTMEDIA/Rosetta-7B-Instruct).

## Quickstart

### vLLM

Use the PoSTMEDIA vLLM distribution with native Rosetta support — no `trust_remote_code` required:

```bash
VLLM_USE_PRECOMPILED=1 pip install git+https://github.com/PoSTMEDIA-AI/vllm@rosetta-v0.26.0

vllm serve PoSTMEDIA/Rosetta-7B-Instruct-NVFP4
```

vLLM detects the ModelOpt NVFP4 checkpoint automatically:

- **Blackwell (SM 100/120/121 — B200, RTX 50, DGX Spark)** — native NVFP4 GEMM kernels (CUTLASS / FlashInfer / Marlin, auto-selected)
- **Hopper / Ada / Ampere (SM ≥ 80)** — weight-only Marlin fallback: same 6.3 GB footprint, BF16 arithmetic

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")
resp = client.chat.completions.create(
    model="PoSTMEDIA/Rosetta-7B-Instruct-NVFP4",
    messages=[{"role": "user", "content": "부산 여행 1박 2일 코스를 짜줘."}],
    temperature=0.7,
)
print(resp.choices[0].message.content)
```

> [!IMPORTANT]
> vLLM **v0.26 or later** is required. Recommended sampling: `temperature 0.7, top_p 0.9` (or greedy for deterministic tasks).
> This NVFP4 checkpoint is designed for serving stacks that understand the ModelOpt unified format (vLLM; TensorRT-LLM- and SGLang-compatible layout). For plain `transformers` inference, use the [BF16 model](https://huggingface.co/PoSTMEDIA/Rosetta-7B-Instruct).

### DGX Spark

On DGX Spark (GB10, 128 GB unified memory), the 6.3 GB NVFP4 checkpoint leaves nearly all memory free for KV cache and other workloads, and decode speed improves markedly over BF16 because decoding on Spark is bound by weight-streaming bandwidth. Install the PoSTMEDIA vLLM distribution in a CUDA 13 environment and serve with the same command as above.

## Model Summary

Identical to [Rosetta-7B-Instruct](https://huggingface.co/PoSTMEDIA/Rosetta-7B-Instruct): Rosetta dense decoder-only Transformer (`RosettaForCausalLM`), 7B parameters, 32 layers, interleaved sliding-window (4,096) + global attention (3:1) with QK-normalization, 65,536-token context, 161,425-token Korean-extended vocabulary. See the base model card for training details and full benchmark results.

## Limitations

- Inherits the limitations of the BF16 base model (factuality, bias, Korean/English focus, 32K alignment window).
- 4-bit quantization can introduce small deviations from BF16 outputs; verify quality on your workload before production use.
- Native FP4 acceleration requires NVIDIA Blackwell GPUs and a serving stack with NVFP4 kernels (vLLM ≥ 0.26 recommended).

## License

Apache License 2.0 — see [LICENSE](./LICENSE). If you build something with Rosetta, we'd appreciate a *"Built with Rosetta"* attribution.

## Citation

```bibtex
@misc{rosetta2026,
  title  = {Rosetta-7B: A Bilingual Korean-English Language Model Family},
  author = {{PoSTMEDIA AI Lab}},
  year   = {2026},
  url    = {https://huggingface.co/collections/PoSTMEDIA/rosetta-6a9db30fd1b4585b0c1845e9}
}
```

## Contact

Questions and feedback — please open a discussion on the model page.
