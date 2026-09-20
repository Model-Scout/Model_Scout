---
library_name: transformers
license: other
license_name: nvidia-open-model-license
license_link: >-
  https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/
pipeline_tag: text-generation
language:
  - en
  - es
  - fr
  - de
  - ja
  - it
  - pt
  - zh
  - ar
  - da
  - ko
  - nl
  - pl
  - ru
  - sv
  - th
tags:
- nvidia
- pytorch
- two-tower
- diffusion
- mamba
datasets:
  - nvidia/Nemotron-Pretraining-Code-v1
  - nvidia/Nemotron-CC-v2
  - nvidia/Nemotron-Pretraining-SFT-v1
  - nvidia/Nemotron-CC-Math-v1
  - nvidia/Nemotron-Pretraining-Code-v2
  - nvidia/Nemotron-Pretraining-Specialized-v1
  - nvidia/Nemotron-CC-v2.1
  - nvidia/Nemotron-CC-Code-v1
  - nvidia/Nemotron-Pretraining-Dataset-sample
track_downloads: true
---

# Nemotron-Labs-TwoTower-30B-A3B-Base-BF16

<div align="center" style="line-height: 1;">
<a href="https://arxiv.org/abs/2606.26493" target="_blank" style="margin: 2px;">
    <img alt="Paper" src="https://img.shields.io/badge/📝Paper-Nemotron--Labs--TwoTower-76B900?logoColor=white" style="display: inline-block; vertical-align: middle;"/>
</a>
<a href="https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16" target="_blank" style="margin: 2px;">
    <img alt="Backbone" src="https://img.shields.io/badge/🏗️Backbone-Nemotron_3_Nano_30B--A3B-76B900?logoColor=white" style="display: inline-block; vertical-align: middle;"/>
</a>
<a href="https://huggingface.co/collections/nvidia/nemotron-labs-twotower" target="_blank" style="margin: 2px;">
    <img alt="Collection" src="https://img.shields.io/badge/🤗Collection-Nemotron--Labs--TwoTower-76B900?logoColor=white" style="display: inline-block; vertical-align: middle;"/>
</a>
</div>

<div align="center" style="line-height: 1;">
  <a href="https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-nemotron-open-model-license/" style="margin: 2px;">
    <img alt="License" src="https://img.shields.io/badge/License-NVIDIA Nemotron Open Model License-f5de53?&color=f5de53" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>

<p align="center">
  <img src="table_comparison.png" alt="Category-level comparison between Nemotron-3-Nano-30B-A3B and Nemotron-Labs-TwoTower" style="max-width: 100%;"/>
  <em>Category-level comparison between the Nemotron-3-Nano-30B-A3B autoregressive baseline and Nemotron-Labs-TwoTower Diffusion.</em>
</p>

## Model Overview

**Model Developer:** NVIDIA Corporation

**Model Dates:** September 2025 – April 2026

**Data Freshness:** The pre-training data has a cutoff date of June 25, 2025.

Nemotron-Labs-TwoTower-30B-A3B-Base-BF16 is a **block-wise autoregressive diffusion** language model built on the [NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16) backbone. It generates text by iteratively denoising blocks of tokens in parallel rather than one token at a time.

This model is ready for commercial use.

## Description

Nemotron-Labs-TwoTower uses two towers:

- **Context tower (AR / context)** — a frozen causal, autoregressive tower that processes the clean prompt and all previously committed tokens, producing the per-layer KV cache (attention) and final Mamba-2 states.
- **Denoiser tower (diffusion / denoiser)** — a trainable tower that generates a block of tokens at a time via mask diffusion, refining noisy blocks with bidirectional in-block attention, layer-aligned cross-attention to the context tower, and context-seeded Mamba states.

Both towers are copies of the same 52-layer hybrid Mamba-2 / attention / MoE backbone; only the diffusion/denoiser tower is trained, and the AR/context tower stays frozen. The denoiser is trained on **~2.1T tokens** (the backbone was pretrained on 25T tokens). At the default operating point, Nemotron-TwoTower retains **98.7%** of the autoregressive baseline's aggregate benchmark quality and provides **2.42×** the AR baseline's wall-clock generation throughput.

### What is Nemotron?

NVIDIA Nemotron™ is a family of open models with open weights, training data, and recipes, delivering leading efficiency and accuracy for building specialized AI agents.

## Nemotron-Labs-TwoTower: Diffusion LLM with Autoregressive Context

```
      AR / Context Tower            Diffusion / Denoiser Tower

          clean tokens                   noisy token blocks
               │                                 │
       ┌───────▼───────┐                 ┌───────▼───────┐
       │   Embedding   │                 │   Embedding   │
       └───────┬───────┘                 └───────┬───────┘
               │                                 │
       ┌───────▼───────┐    KV + Mamba   ┌───────▼───────┐
       │ Mamba-2/Attn  │─────states─────▶│ Mamba-2/Attn  │
       └───────┬───────┘                 └───────┬───────┘
               │                                 │
       ┌───────▼───────┐                 ┌───────▼───────┐
       │      MoE      │                 │      MoE      │
       └───────┬───────┘                 └───────┬───────┘
               │                                 │
       ┌───────▼───────┐                 ┌───────▼───────┐
       │  Output Head  │                 │  Output Head  │
       └───────┬───────┘                 └───────┬───────┘
               │                                 │
         logits / loss                     logits / loss
          (optional)
```

The AR/context tower (left) runs causally over clean token blocks and exposes, at every layer, the attention KV cache and the Mamba-2 conv/SSM boundary states. The diffusion/denoiser tower (right) consumes a noisy block; at each layer it cross-attends to the corresponding layer of the context tower (KV) and seeds its Mamba-2 layer from the corresponding context Mamba state.

### Two-Tower Generation Modes

| Mode | Description | Tokens / step | API |
|------|-------------|---------------|-----|
| **Mask Diffusion** | Diffusion/denoiser mode: block-wise iterative denoising with confidence-based unmasking. | up to `block_size` | `generate_mask_diffusion()` |
| **Mock-AR** | Two-tower **autoregressive**: AR/context tower builds the cache, diffusion/denoiser predicts the next token. | 1 | `generate_mock_ar()` |
| **AR** | Standard **autoregressive** generation using the AR/context tower only (single GPU). | 1 | `generate_ar()` |

### How mask diffusion works

Generation is **block-wise autoregressive**: the AR/context tower encodes the prompt once, then the diffusion/denoiser fills one block of `block_size` positions at a time. For each new block:

1. Initialize the block as all `[MASK]` tokens (`mask_token_id`).
2. For `steps_per_block` denoising iterations:
   - Compute the diffusion timestep `t` = current masked fraction of the block, and feed it to the **time-conditioned denoiser** (adaLN-single modulation — a global MLP maps `t` to per-layer scale/shift/gate, PixArt-α style).
   - Run the diffusion/denoiser over the whole block (bidirectional in-block self-attention + layer-aligned causal cross-attention to the AR/context cache; Mamba-2 chunk-scan seeded from the context state).
   - Constrain to `p(x₀ | xₜ)` (mask token forbidden; already-decoded positions fixed), then **commit** the high-confidence positions (all above `confidence_threshold`, with a floor that guarantees completion within `steps_per_block`) and re-mask the rest (**confidence unmasking**).
3. Commit the resolved block, advance the AR/context tower over it to update the KV + Mamba caches, and continue with the next block.

Each step predicts all masked positions in parallel and commits the confident subset, so multiple tokens may be committed per step.

## License/Terms of Use

GOVERNING TERMS: Use of this model is governed by the [NVIDIA Nemotron Open Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-nemotron-open-model-license/).

## Benchmark Evaluations

Default operating point: **confidence unmasking**, threshold `γ = 0.8`, block size `S = 16`, BF16 on 2×H100 GPUs. At this point Nemotron-Labs-TwoTower retains **98.7%** of the AR baseline's aggregate benchmark quality and reaches **2.42×** the AR baseline's wall-clock generation throughput. Lowering the confidence threshold increases the tokens committed per step and the throughput, with reduced quality.

Per-task results below compare the autoregressive backbone (AR/context baseline) against Nemotron-Labs-TwoTower (diffusion/denoiser decoding). <!-- TODO: fill in final released-checkpoint numbers -->

| Task | NVIDIA-Nemotron-3-Nano-30B-A3B-Base (AR baseline) | Nemotron-Labs-TwoTower-30B-A3B-Base (diffusion) |
| :---- | :---- | :---- |
| **General Knowledge** | | |
| MMLU (5-shot, acc) | 78.56 | 78.24 |
| MMLU-Pro (5-shot, CoT EM) | 62.59 | 60.93 |
| **Commonsense Understanding** | | |
| ARC-Challenge (25-shot, acc_norm) | 91.72 | 92.66 |
| WinoGrande (5-shot, acc) | 76.09 | 76.09 |
| **Reading Comprehension** | | |
| RACE (0-shot, acc) | 88.90 | 88.90 |
| **Code** | | |
| HumanEval (0-shot) | 79.27 | 75.58 |
| MBPP-Sanitized (3-shot) | 74.71 | 74.28 |
| **Math** | | |
| GSM8K (8-shot, acc) | 92.49 | 90.14 |
| MATH-500 (4-shot) | 84.40 | 80.60 |
| **Multilingual** | | |
| MMLU Global Lite (5-shot, avg acc) | 73.97 | 73.94 |
| MGSM (8-shot, avg acc) | 80.80 | 80.40 |
| **Aggregate** | | |
| Quality retained (% of AR baseline) | 100% | **98.7%** |
| Generation throughput (× AR baseline) | 1.0× | **2.42×** |

<!-- TODO: confirm AR-baseline column values and the evaluation harness/configs for the diffusion column before release. -->

## Model Architecture

- **Architecture Type:** Two-Tower Block-Diffusion over a Mamba2-Transformer Hybrid Mixture of Experts (MoE) backbone
- **Backbone:** [NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16)
- **Layers per tower:** 52 — **23 Mamba-2**, **6 self-attention**, **23 MoE**
- **Number of model parameters:** ~60B total (30B AR/context tower + 30B diffusion/denoiser tower); the released checkpoint ships both towers
- **Active parameters per token:** ~3B per tower, 128 routable experts of which 6 are activated, with 2 shared experts. 
- **Denoiser-only modifications vs. the backbone:**
  - **Bidirectional in-block attention** — noisy tokens attend bidirectionally within the current block, causally to past clean blocks (no added parameters).
  - **Layer-aligned cross-attention** — denoiser layer *i* attends to context-tower layer *i*'s KV.
  - **Context-seeded Mamba-2** — denoiser Mamba layers seed their initial conv/SSM state from the corresponding context Mamba state (causal; the bidirectional-Mamba variant is not used).
  - **adaLN-single time conditioning** — the diffusion timestep `t` modulates every denoiser layer (≈1.5M added parameters; replicated per tensor-parallel rank).

## Training Methodology

Nemotron-Labs-TwoTower is produced by adapting a pretrained autoregressive backbone into a block-wise diffusion generator — **only the diffusion/denoiser tower is trained; the AR/context tower is optionally trainable, but kept frozen here.**

- **Stage 1 — Backbone pre-training (AR).** The single-tower [NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16) is pre-trained from scratch with next-token prediction (~25T tokens).
- **Stage 2 — Two-tower denoiser training (diffusion).** Both towers are initialized from the same backbone checkpoint. The AR/context tower is frozen; the diffusion/denoiser tower is trained under a **masked-diffusion** objective (mean negative log-likelihood over masked positions), conditioned on the context tower's per-layer KV cache and Mamba boundary states. Training follows the backbone's two-stage data curriculum (broad phase-1 blend → higher-quality phase-2 blend), over **~2.1T tokens** total.

The released checkpoint is trained in three stages: phase-1 adaptation at block size `S=32`, phase-2 continuation at `S=32`, and a final phase-2 continuation at `S=16` (the default sampling block size).

- **Precision:** BF16. **Optimizer:** AdamW with a Warmup-Stable-Decay schedule (peak LR `1e-4`, final LR `1e-6`), reset at phase boundaries.
- **Software used for training:** [Megatron-LM](https://github.com/NVIDIA/Megatron-LM)

## Input

- **Input Type(s):** Text
- **Input Format(s):** String
- **Input Parameters:** One-Dimensional (1D): Sequences
- **Maximum input size:** 128K tokens

## Output

- **Output Type(s):** Text
- **Output Format:** String
- **Output Parameters:** One-Dimensional (1D): Sequences
- **Maximum output size:** 128K tokens

Our AI models are designed and optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.

## Software Integration

- **Runtime Engine(s):** HuggingFace Transformers (with `trust_remote_code=True`)
- **Supported Hardware Microarchitecture Compatibility:** NVIDIA H100-80GB, NVIDIA A100 (full two-tower diffusion inference uses **2 GPUs**, ~59GB per GPU for BF16 weights)
- **Operating System(s):** Linux

### Use it with Transformers

Full **two-tower diffusion** inference places the AR/context tower and the diffusion/denoiser tower on separate GPUs.

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "nvidia/Nemotron-Labs-TwoTower-30B-A3B-Base-BF16"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
)

# AR/context tower -> GPU 0, diffusion/denoiser tower -> GPU 1
model.place_towers_on_devices("cuda:0", "cuda:1")
model.eval()

prompt = "France is a country "
inputs = tokenizer(prompt, return_tensors="pt").to("cuda:0")

# Mask-diffusion generation (two-tower)
outputs = model.generate_mask_diffusion(
    inputs["input_ids"],
    max_new_tokens=128,
    block_size=16,            # tokens generated per block
    steps_per_block=16,       # denoising iterations per block
    mask_token_id=3,          # [MASK]
    temperature=0.1,
    confidence_threshold=0.8, # commit positions above this confidence each step
    eos_token_id=tokenizer.eos_token_id,
)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

**Mock-AR** (two-tower autoregressive, one token per step):

```python
outputs = model.generate_mock_ar(
    inputs["input_ids"], max_new_tokens=128, temperature=0.0,
    eos_token_id=tokenizer.eos_token_id,
)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

**AR-only** (single GPU, AR/context tower only — load with `.cuda()` instead of `place_towers_on_devices`):

```python
outputs = model.generate_ar(
    inputs["input_ids"], max_new_tokens=128, temperature=0.0,
    eos_token_id=tokenizer.eos_token_id,
)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Model Version(s)

- **v1.1** — Block-wise **mask-diffusion** generation enabled (time-conditioned diffusion/denoiser, bidirectional in-block attention, context-seeded chunk-scan Mamba-2); AR and mock-AR also supported.
- **v1.0** — Two-tower AR (mock-AR) checkpoint.

# Training, Testing, and Evaluation Datasets

The diffusion/denoiser tower is trained on the same data sources as the [NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16) backbone (a ~2.1T-token subset of the backbone's two-phase blend). See the [base model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16#training-testing-and-evaluation-datasets) for the full dataset listing.

- **Data Modality:** Text
- **Data Collection Method by dataset:** Hybrid: Automated, Human, Synthetic
- **Labeling Method by dataset:** Not applicable (self-supervised mask-diffusion objective)

## Inference

- **Engine(s):** HuggingFace Transformers (with `trust_remote_code=True`)
- **Test Hardware:** 2× NVIDIA A100 80GB or 2× NVIDIA H100 80GB (two-tower diffusion); 1× 80GB GPU sufficient for AR-only mode

## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our [Trustworthy AI terms of service](https://www.nvidia.com/en-us/agreements/trustworthy-ai/terms/), developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

For more detailed information on ethical considerations for this model, please see the Model Card++ [Bias](bias.md), [Explainability](explainability.md), and [Privacy](privacy.md) Subcards.

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Citation

<!-- TODO: authors omitted for now; fill in arXiv id / venue / year when the report is public. -->

```
@misc{nemotron_labs_twotower_2026,
  title  = {{Nemotron-Labs-TwoTower}: Diffusion Language Modeling with Pretrained Autoregressive Context},
  author = {Reda, Fitsum and Kamalu, John and Waleffe, Roger and Patwary, Mostofa and Shoeybi, Mohammad and Catanzaro, Bryan},
  year   = {2026},
  url    = {https://arxiv.org/abs/2606.26493},
  doi    = {10.48550/arXiv.2606.26493},
  note   = {arXiv preprint arXiv:2606.26493}
}
```
