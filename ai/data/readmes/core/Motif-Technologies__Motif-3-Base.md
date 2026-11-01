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
- pretrained
- base-model
license: mit
---

<div align="center">
  <img src="https://cdn-avatars.huggingface.co/v1/production/uploads/6836935d054aee793ffd78f1/L3Rw_g8vkvD8dqhOYGZhl.png" width="180" alt="Motif">
</div>
<hr>

<div align="center" style="line-height: 1;">
  <a href="https://motiftech.io" target="_blank"><img alt="Homepage" src="https://img.shields.io/badge/Homepage-Motif%20Technologies-1783ff?logoColor=white"/></a>
  <a href="https://huggingface.co/Motif-Technologies" target="_blank"><img alt="Hugging Face" src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Motif-ffc107?color=ffc107&logoColor=white"/></a>
  <a href="https://arxiv.org/abs/2608.09119" target="_blank"><img alt="Tech Report" src="https://img.shields.io/badge/📄%20Tech%20Report-lightgrey"/></a>
  <a href="https://huggingface.co/Motif-Technologies/Motif-3-Base/blob/main/LICENSE.md" target="_blank"><img alt="License" src="https://img.shields.io/badge/License-MIT-f5de53?&color=f5de53"/></a>
</div>

## 1. Model Introduction

**Motif 3 Base** is the **base pretrained checkpoint** of Motif 3 — a large-scale, decoder-only Mixture-of-Experts (MoE) language model with **314 billion total parameters** and **13.2 billion parameters activated per token**. It is built from the ground up by [Motif Technologies](https://motiftech.io) following a fully in-house, proprietary design.

This repository provides the **foundation model prior to post-training**: it has completed large-scale pretraining but has **not** undergone supervised fine-tuning, reinforcement learning, or preference/safety alignment. It is released for **further fine-tuning, continued pretraining, and research**. For the instruction-tuned, post-trained model, see **[Motif-Technologies/Motif-3](https://huggingface.co/Motif-Technologies/Motif-3)**.

Motif 3 is built around **Grouped Differential Latent Attention (GDLA)**, which integrates grouped differential attention with the compressed key–value representation of Multi-head Latent Attention. The architecture further incorporates **modified manifold-constrained hyper-connections (mHC)**, **Expert-Specific PolyNorm** activations, and a **Multi-Token Prediction (MTP)** auxiliary objective to improve optimization stability, expert specialization, and training efficiency.

The model is pretrained on approximately **12.5 trillion tokens** spanning web documents, STEM, code, mathematics, multilingual content, and domain-specialized corpora, with additional emphasis on Korean, reasoning-intensive, legal, and financial data.

### Key Features
- 🧠 **Fine-grained sparse MoE** — 384 routed experts with only 8 activated per token (plus 1 shared expert), providing a large expert pool at limited per-token compute.
- 📏 **Native 256K context** (262,144 tokens), trained with window-aware context parallelism.
- ⚙️ **Novel architecture** — GDLA attention, Expert-Specific PolyNorm, and modified mHC, with MTP used as an auxiliary pretraining objective.
- 🌐 **Multilingual & general-purpose**, with a strong bytes-per-token tokenizer for English, Korean, code, and math.
- 🧩 **Clean foundation** — a base checkpoint intended as a starting point for supervised fine-tuning, RL, and domain adaptation.

## 2. Model Summary

<div align="center">
<table>
<tbody>
<tr><td><b>Model Type</b></td><td>Base (pretrained, not instruction-tuned)</td></tr>
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
<tr><td><b>Context Length</b></td><td>262,144 (256K)</td></tr>
<tr><td><b>Vocabulary Size</b></td><td>220,160</td></tr>
<tr><td><b>Pretraining Tokens</b></td><td>~12.5T</td></tr>
<tr><td><b>Tensor Type</b></td><td>bfloat16</td></tr>
</tbody>
</table>
</div>

## 3. Intended Use & Limitations

**Intended use.** Motif 3 Base is a foundation model. Typical uses are supervised fine-tuning (SFT), continued pretraining, reinforcement learning, distillation, and research on pretrained representations.

**Not an assistant.** This checkpoint is **not instruction-tuned or aligned** and ships **without a chat template**. Do not expect it to follow instructions, hold a conversation, or refuse unsafe requests out of the box. Use it in **text-completion** mode (or fine-tune it first).

**Limitations.** Because no alignment or safety tuning has been applied, outputs may be factually incorrect, biased, or otherwise unsafe. Downstream users are responsible for adding appropriate fine-tuning, evaluation, and safety mitigations before deployment.

## 4. Evaluation Results

We report the absolute performance of the pretrained base checkpoint under the prompting settings indicated below, to characterize the capabilities acquired during pretraining. We deliberately omit cross-model comparisons: base-model results are increasingly not published, and scores are highly sensitive to the evaluation harness and prompting protocol. Accuracy is reported for the multiple-choice and mathematics benchmarks; pass@1 is reported for HumanEval and MBPP. "CoT" denotes chain-of-thought prompting.

<div align="center">

| Benchmark | Setting | **Motif-3-Base** |
|:---|:---:|:---:|
| MMLU | 5-shot | 86.20 |
| MMLU-Pro | 5-shot CoT | 68.56 |
| ARC-C | 25-shot | 94.71 |
| WinoGrande | 5-shot | 80.90 |
| HellaSwag | 10-shot | 88.30 |
| PIQA | 0-shot | 85.14 |
| GSM8K | 8-shot CoT | 93.93 |
| MATH | 4-shot CoT | 70.58 |
| HumanEval | 0-shot | 73.70 |
| MBPP | 3-shot | 84.60 |

</div>

## 5. Architecture

> [!NOTE]
> The architecture and distributed training framework used for Motif 3 are available at [MotifTechnologies/motif3-training-example](https://github.com/MotifTechnologies/motif3-training-example).

Motif 3 is a fully in-house design and introduces several custom components (full details in the technical report):

- **Grouped Differential Latent Attention (GDLA)** — integrates grouped differential attention (asymmetric signal/noise heads with a token-dependent differential coefficient) with the compressed KV latent of Multi-head Latent Attention, plus a query-dependent output gate. Retains the expressive attention dynamics of differential attention while substantially reducing KV-cache requirements.
- **Expert-Specific PolyNorm** — replaces the SiLU gate with a learned polynomial normalization whose coefficients are learned independently per expert, reducing activation outliers while allowing each expert to specialize.
- **Modified manifold-constrained hyper-connections (mHC)** — replaces conventional residual additions with a doubly-stochastic (Birkhoff-polytope) mixing of 4 parallel residual streams; the post-mapping multiplier is annealed from 2 → 1 during pretraining to limit activation-outlier accumulation.
- **Multi-Token Prediction (MTP)** — a DeepSeek-V3-style multi-token-prediction objective used as an auxiliary target during pretraining. (The MTP head is not shipped with this base checkpoint.)

## 6. Access

This model is **openly available** — anyone can download the weights, no access request required.

## 7. License

This model is released under the **MIT License**. See the [LICENSE](https://huggingface.co/Motif-Technologies/Motif-3-base/blob/main/LICENSE.md) file for details.  
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
