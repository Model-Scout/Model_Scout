---
library_name: transformers
pipeline_tag: text-generation
language:
- en
- ko
tags:
- motif
- motif-3
- mixture-of-experts
- moe
- multilingual
- nvfp4
- quantized
base_model: Motif-Technologies/Motif-3
license: mit
---

<div align="center">
  <img src="https://cdn-avatars.huggingface.co/v1/production/uploads/6836935d054aee793ffd78f1/L3Rw_g8vkvD8dqhOYGZhl.png" width="180" alt="Motif">
</div>
<hr>

<div align="center" style="line-height: 1;">
  <a href="https://chat.motiftech.io/chat" target="_blank"><img alt="chatbot" src="https://img.shields.io/badge/chatbot-Chat%20Motif-17831f?logoColor=white"/></a>
  <a href="https://motiftech.io" target="_blank"><img alt="Homepage" src="https://img.shields.io/badge/Homepage-Motif%20Technologies-1783ff?logoColor=white"/></a>
  <a href="https://huggingface.co/Motif-Technologies" target="_blank"><img alt="Hugging Face" src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Motif-ffc107?color=ffc107&logoColor=white"/></a>
  <a href="https://arxiv.org/abs/2608.09119" target="_blank"><img alt="Tech Report" src="https://img.shields.io/badge/📄%20Tech%20Report-lightgrey"/></a>
  <a href="https://huggingface.co/Motif-Technologies/Motif-3-NVFP4/blob/main/LICENSE.md" target="_blank"><img alt="License" src="https://img.shields.io/badge/License-MIT-f5de53?&color=f5de53"/></a>
</div>

# Motif-3-NVFP4

> **NVFP4-quantized checkpoint of [Motif-Technologies/Motif-3](https://huggingface.co/Motif-Technologies/Motif-3).**
> This repository hosts the **NVFP4** build of Motif 3 for a reduced memory footprint on NVFP4-capable hardware. For the full model description, architecture, and evaluation, see the [base model card](https://huggingface.co/Motif-Technologies/Motif-3).

## 1. Model Introduction

**Motif 3** is a large-scale, decoder-only Mixture-of-Experts (MoE) language model with **314 billion total parameters** and **13.2 billion parameters activated per token**, built from the ground up by [Motif Technologies](https://motiftech.io) following a fully in-house, proprietary design. 

It is built around **Grouped Differential Latent Attention (GDLA)** and further incorporates **modified manifold-constrained hyper-connections (mHC)**, **Expert-Specific PolyNorm** activations, and a **Multi-Token Prediction (MTP)** head.

**This checkpoint (`Motif-3-NVFP4`)** is an **NVFP4-quantized** version of the model weights, intended for efficient serving on NVIDIA Blackwell-class GPUs. The architecture, context length, and behavior otherwise match the base model.

### Key Features
- 🗜️ **NVFP4-quantized** — lower memory footprint vs. the BF16 / Block-FP8 release.
- 🧠 **Fine-grained sparse MoE** — 384 routed experts with only 8 activated per token (plus 1 shared expert).
- 📏 **Native 256K context** (262,144 tokens).
- ⚙️ **Novel architecture** — GDLA attention, Expert-Specific PolyNorm, modified mHC, and a built-in MTP head enabling **self-speculative decoding**.
- 🌐 **Multilingual & general-purpose**, with particular strength on long-horizon agentic tool use.

## 2. Model Summary

<div align="center">
<table>
<tbody>
<tr><td><b>Base Model</b></td><td><a href="https://huggingface.co/Motif-Technologies/Motif-3">Motif-Technologies/Motif-3</a></td></tr>
<tr><td><b>Quantization</b></td><td>NVFP4 (weights)</td></tr>
<tr><td><b>Architecture</b></td><td>Mixture-of-Experts (MoE), decoder-only</td></tr>
<tr><td><b>Total Parameters</b></td><td>~314B</td></tr>
<tr><td><b>Activated Parameters</b></td><td>~13.2B / token</td></tr>
<tr><td><b>Number of Layers</b></td><td>53 (2 dense + 51 MoE)</td></tr>
<tr><td><b>Hidden Dimension</b></td><td>4096</td></tr>
<tr><td><b>Dense FFN Intermediate</b></td><td>12,288 (first 2 layers)</td></tr>
<tr><td><b>Attention</b></td><td>Grouped Differential Latent Attention (GDLA) with gated output</td></tr>
<tr><td><b>Query / KV Heads</b></td><td>80 / 16</td></tr>
<tr><td><b>Routed Experts</b></td><td>384 (top-8)</td></tr>
<tr><td><b>Shared Experts</b></td><td>1</td></tr>
<tr><td><b>Activation</b></td><td>Expert-Specific PolyNorm</td></tr>
<tr><td><b>Residual</b></td><td>Modified manifold-constrained hyper-connections (mHC)</td></tr>
<tr><td><b>MTP Head</b></td><td>1 layer (self-speculative decoding)</td></tr>
<tr><td><b>Context Length</b></td><td>262,144 (256K)</td></tr>
<tr><td><b>Vocabulary Size</b></td><td>220,160</td></tr>
</tbody>
</table>
</div>

> [!Important]
> **Note on Parameter Count:** This model uses packed 8-bit storage for 4-bit weights. The automatically calculated parameter count shown in the Hugging Face UI reports **half** the actual value. The true parameter count is **~314B**.

## 3. Evaluation Results

Motif 3 performs particularly well on **agentic and tool-oriented** benchmarks (e.g. τ³-Banking, Terminal-Bench 2.1) while remaining competitive on coding, mathematical reasoning, and general knowledge.

For the full benchmark table and evaluation setup, please refer to the **[base model card](https://huggingface.co/Motif-Technologies/Motif-3#3-evaluation-results)**.

### 3.1 NVFP4 Accuracy Benchmarks

To quantify the accuracy cost of quantization, we evaluate this **NVFP4** checkpoint against the **Block-FP8** release on the same suite, under identical prompts and decoding settings. Across the five benchmarks the two builds land within ~0.15 points of each other on average, so NVFP4 delivers its reduced memory footprint at essentially no accuracy penalty. Individual scores move in both directions (NVFP4 is ahead on AA-Omniscience accuracy and HLE, slightly behind on AA-LCR and non-hallucination), which is consistent with run-to-run evaluation noise rather than a systematic degradation.

| Benchmark | NVFP4 | Block-FP8 |
|---|---|---|
| AA-Omniscience (public set) — accuracy | **36.17** | 34.67 |
| AA-Omniscience (public set) — non-hallucination | 77.55 | **78.32** |
| GPQA-Diamond | 84.34 | **84.55** |
| AA-LCR | 70.50 | **72.30** |
| HLE (25% random sampled) | **39.70** | 39.15 |
| **Average** | **61.65** | **61.80** |

## 4. Architecture

Motif 3 introduces several custom components (full details in the technical report):

- **Grouped Differential Latent Attention (GDLA)** — integrates grouped differential attention with the compressed KV latent of Multi-head Latent Attention, plus a query-dependent output gate.
- **Expert-Specific PolyNorm** — a learned polynomial normalization with per-expert coefficients, reducing activation outliers while allowing each expert to specialize.
- **Modified manifold-constrained hyper-connections (mHC)** — doubly-stochastic mixing of 4 parallel residual streams, with the post-mapping multiplier annealed from 2 → 1 during pretraining.
- **Multi-Token Prediction (MTP)** — a 1-layer MTP head enabling **self-speculative decoding** at inference.

## 5. Deployment — vLLM (Recommended)

> [!Important]
> ### 🖥️  Serving runs on just 2 × NVIDIA B200 GPUs
> Thanks to NVFP4 quantization, this 314B checkpoint serves on **two B200 GPUs on a single node** — that is the validated deployment configuration for the command below.

> [!Note]
> - NVFP4 requires **NVFP4-capable hardware** (NVIDIA Blackwell / B200).
> - The model ships with a built-in **MTP head** (`num_nextn_predict_layers=1`), so it supports **self-speculative decoding** — add `--speculative-config` as shown below (`num_speculative_tokens: 1` is optimal for this model).
> - If you encounter any issues, please open an HF issue.

- **vLLM repo:** [MotifTechnologies/vllm](https://github.com/MotifTechnologies/vllm) — public vLLM fork with Motif-3 support (based on vLLM v0.26.0)
- **Docker image:** `ghcr.io/motiftechnologies/vllm:v0.26.0-motif3`

### B200 — 2 GPUs

```bash
vllm serve "Motif-Technologies/Motif-3-NVFP4" \
    --trust-remote-code \
    --quantization modelopt_nvfp4 \
    --speculative-config '{"model": "Motif-Technologies/Motif-3-NVFP4", "num_speculative_tokens": 1}' \
    --tensor-parallel-size 1 \
    --data-parallel-size 2 \
    --data-parallel-size-local 2 \
    --enable-expert-parallel \
    --enable-auto-tool-choice \
    --tool-call-parser motif \
    --reasoning-parser motif \
    --dtype bfloat16 \
    --gpu-memory-utilization 0.85 \
    --max-model-len 262144 \
    --block-size 128 \
    --host 0.0.0.0 --port 8080
```

## 6. Access

This model is **openly available** — anyone can download the weights, no access request required.

## 7. License

This model is released under the **MIT License**. See the [LICENSE](https://huggingface.co/Motif-Technologies/Motif-3-NVFP4/blob/main/LICENSE.md) file for details.  
If you build on Motif 3, we'd truly appreciate a mention (e.g., "Built with Motif 3") when you share your work. Thanks for building with Motif!

## 8. Citation
```
@misc{lim2026motif3technicalreport,
      title={Motif 3: Technical Report}, 
      author={Junghwan Lim and Joon Son Chung and Sungmin Lee and Wai Ting Cheung and Gihun Cho and Minsu Ha and Sangho Kang and Beomgyu Kim and Dongseok Kim and Jangwoong Kim and Taehyun Kim and Taewhan Kim and Jeesoo Lee and Jeongdoo Lee and Junhyeok Lee and Dongpin Oh and Hyeyeon Cho and Dahye Choi and Jaeheui Her and Hanbin Jung and Changjin Kang and Minjae Kim and Youngrok Kim and Hyukjin Kweon and Hongjoo Lee and Yeongjae Park and Bokki Ryu},
      year={2026},
      eprint={2608.09119},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2608.09119}, 
}
```
---

© Motif Technologies. All rights reserved.
