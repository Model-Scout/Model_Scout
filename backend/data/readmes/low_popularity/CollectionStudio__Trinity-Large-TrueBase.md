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
      alt="Arcee Trinity Large"
      style="max-width: 100%; height: auto;"
    >
  </picture>
</div>
<hr>


# Trinity-Large-TrueBase

## Introduction

Trinity-Large-TrueBase is a base pretraining checkpoint from Arcee AI's Trinity Large training run. It is a 398B-parameter sparse Mixture-of-Experts (MoE) model with approximately 13B active parameters per token. The checkpoint was captured after 10 trillion tokens of pretraining, prior to learning-rate annealing and before any instruction tuning or reinforcement learning.

This checkpoint is intended for research, probing, ablation studies, and downstream fine-tuning and comes without any pre-baked alignment, instruction formatting, or preference optimization.

More details on the training of Trinity Large are available in the [technical report](https://github.com/arcee-ai/trinity-large-tech-report/).

## Model Variants

The Trinity Large family consists of three checkpoints from the same training run:

- **Trinity-Large-TrueBase** (this release): 10T-token pre-anneal checkpoint with no instruction data
- **[Trinity-Large-Thinking](https://huggingface.co/arcee-ai/Trinity-Large-Thinking)**: Reasoning-optimized, agentic post-training with extended chain-of-thought
- **[Trinity-Large-Base](https://huggingface.co/arcee-ai/Trinity-Large-Base)**: Full 17T-token pretrained foundation model with mid-training anneals
- **[Trinity-Large-Preview](https://huggingface.co/arcee-ai/Trinity-Large-Preview)**: Lightly post-trained, chat-ready model undergoing active RL

## Architecture

Trinity-Large-TrueBase uses a sparse MoE configuration designed to maximize efficiency while maintaining large-scale capacity.

| Hyperparameter | Value |
|:---|:---:|
| Total parameters | ~398B |
| Active parameters per token | ~13B |
| Experts | 256 |
| Active experts | 4 |
| Routing strategy | 4-of-256 (1.56% sparsity) |
| Dense layers | 6 |
| Pretraining context length | 8,192 |
| Architecture | Sparse MoE (AfmoeForCausalLM) |


Note: Extended context support (e.g., 512k) was introduced after this checkpoint and is not available in TrueBase.

## Benchmark Results

| Benchmark                     | N-shot | Metric                        | Score  | Stderr  |
|-------------------------------|--------|-------------------------------|--------|---------|
| arc_challenge_0shot           | 0      | acc_norm,none                 | 0.6237 | ±0.0142 |
| bbh_fewshot                   | 3      | exact_match,remove_whitespace | 0.5784 | ±0.0054 |
| gpqa_diamond_5shot            | 5      | acc_norm,none                 | 0.4091 | ±0.0350 |
| gpqa_diamond_generative_5shot | 5      | exact_match,flexible-extract  | 0.3788 | ±0.0346 |
| gsm8k_8shot                   | 8      | exact_match,flexible-extract  | 0.8036 | ±0.0109 |
| gsm8k_cot                     | 8      | exact_match,flexible-extract  | 0.8044 | ±0.0109 |
| hellaswag_5shot               | 5      | acc_norm,none                 | 0.8813 | ±0.0032 |
| humaneval_plus                | 0      | pass@1,create_test            | 0.5183 | ±0.0391 |
| leaderboard_math_hard         | 4      | exact_match,none              | 0.2696 | ±0.0113 |
| mbpp_plus                     | 3      | pass_at_1,none                | 0.8095 | ±0.0202 |
| minerva_math500               | 4      | math_verify,none              | 0.4820 | ±0.0224 |
| mmlu_5shot                    | 5      | acc,none                      | 0.7845 | ±0.0033 |
| mmlu_generative_5shot         | 5      | exact_match,get_response      | 0.7848 | ±0.0033 |
| mmlu_pro                      | 5      | exact_match,custom-extract    | 0.5160 | ±0.0044 |
| triviaqa_5shot                | 5      | exact_match,remove_whitespace | 0.8096 | ±0.0029 |
| winogrande_5shot              | 5      | acc,none                      | 0.8145 | ±0.0109 |


## Training Configuration

### Pretraining

- Training tokens: 10 trillion
- Checkpoint type: Pre-anneal
- Instruction data: None
- RLHF or post-training: None

This checkpoint branches from the main Trinity Large run at the 10T-token mark, prior to learning-rate decay or post-training phases.

### Optimizers

Optimizer learning rates after WSD warm-up:
- Adam learning rate: 2e-4
- Muon learning rate: 8e-4

Muon was used to support larger critical batch sizes in a highly sparse MoE regime.

### Infrastructure

- Hardware: 2,048 NVIDIA B300 GPUs
- Parallelism: HSDP + Expert Parallelism
- Compute partner: [Prime Intellect](https://www.primeintellect.ai/)
- Data partner: [Datology](https://www.datologyai.com/)

<div align="center">
  <picture>
      <img src="https://cdn-uploads.huggingface.co/production/uploads/6435718aaaef013d1aec3b8b/sSVjGNHfrJKmQ6w8I18ek.png" style="background-color:ghostwhite;padding:5px;" width="17%" alt="Powered by Datology">
  </picture>
</div>

<div align="center">
  <picture>
      <img src="https://cdn-avatars.huggingface.co/v1/production/uploads/61e020e4a343274bb132e138/H2mcdPRWtl4iKLd-OYYBc.jpeg" style="background-color:ghostwhite;padding:5px;" width="17%" alt="Powered by Datology">
  </picture>
</div>


## Intended Use

- Studying emergent behavior from large-scale pretraining
- Sparse MoE routing and load-balancing research
- Interpretability, probing, and ablation studies
- Domain-specific fine-tuning from a clean base
- Academic and industrial foundation model research

## Rationale for Release

Most base model releases include instruction data, annealed training dynamics, or early alignment stages. Trinity-Large-TrueBase excludes these, providing an opportunity to study what large-scale models learn from pretraining data alone. This checkpoint is intended as a foundation for research rather than as a finished conversational assistant.

## Known Limitations

- Not aligned for safety, helpfulness, or conversational tone
- Requires substantial compute and expertise to fine-tune
- May exhibit raw or unstable behaviors typical of unaligned models
- No extended-context tuning beyond the 8K pretraining window

## License

Trinity-Large-TrueBase is released under the OpenMDW License, version 1.1 (OpenMDW-1.1).
