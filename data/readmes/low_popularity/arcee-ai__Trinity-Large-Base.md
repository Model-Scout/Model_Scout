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
- arcee-ai/Trinity-Large-TrueBase
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


# Trinity-Large-Base

## Introduction

Trinity-Large-Base is a pretrained foundation model from Arcee AI's Trinity Large training run. It is a 398B-parameter sparse Mixture-of-Experts (MoE) model with approximately 13B active parameters per token. The checkpoint was captured after 17 trillion tokens of pretraining, including mid-training learning-rate anneals and context extension, but prior to any instruction tuning or reinforcement learning.

This checkpoint represents the completed pretraining phase and serves as a foundation for research and downstream fine-tuning.

More details on the training of Trinity Large are available in the [technical report](https://github.com/arcee-ai/trinity-large-tech-report/).


## Model Variants

The Trinity Large family consists of three checkpoints from the same training run:

- **Trinity-Large-Base** (this release): Full 17T-token pretrained foundation model with mid-training anneals
- **[Trinity-Large-Thinking](https://huggingface.co/arcee-ai/Trinity-Large-Thinking)**: Reasoning-optimized, agentic post-training with extended chain-of-thought
- **[Trinity-Large-TrueBase](https://huggingface.co/arcee-ai/Trinity-Large-TrueBase)**: 10T-token pre-anneal checkpoint with no instruction data
- **[Trinity-Large-Preview](https://huggingface.co/arcee-ai/Trinity-Large-Preview)**: Lightly post-trained, chat-ready model undergoing active RL

## Architecture

Trinity-Large-Base uses a sparse MoE configuration designed to maximize efficiency while maintaining large-scale capacity.

| Hyperparameter | Value |
|:---|:---:|
| Total parameters | ~398B |
| Active parameters per token | ~13B |
| Experts | 256 |
| Active experts | 4 |
| Routing strategy | 4-of-256 (1.56% sparsity) |
| Dense layers | 6 |
| Pretraining context length | 8,192 |
| Context length after extention | 512k |
| Architecture | Sparse MoE (AfmoeForCausalLM) |


## Benchmark Results

| Benchmark              | N-shot | Metric                        | Score  | Stderr  |
|------------------------|--------|-------------------------------|--------|---------|
| mbpp_plus              | 3      | pass_at_1,none                | 0.8862 | ±0.0164 |
| minerva_math500        | 4      | math_verify,none              | 0.6520 | ±0.0213 |
| hellaswag_5shot        | 5      | acc_norm,none                 | 0.9011 | ±0.0030 |
| winogrande_5shot       | 5      | acc,none                      | 0.8082 | ±0.0111 |
| mmlu_5shot             | 5      | acc,none                      | 0.8258 | ±0.0031 |
| mmlu_generative_5shot  | 5      | exact_match,get_response      | 0.8260 | ±0.0031 |
| mmlu_pro               | 5      | exact_match,custom-extract    | 0.6602 | ±0.0042 |
| triviaqa_5shot         | 5      | exact_match,remove_whitespace | 0.8330 | ±0.0028 |
| arc_challenge_0shot    | 0      | acc_norm,none                 | 0.6544 | ±0.0139 |
| bbh_fewshot            | 3      | exact_match,remove_whitespace | 0.6570 | ±0.0051 |
| gpqa_diamond_5shot     | 5      | acc_norm,none                 | 0.4394 | ±0.0354 |
| gsm8k_cot              | 8      | exact_match,flexible-extract  | 0.9136 | ±0.0077 |

## Training Configuration

### Pretraining

- Training tokens: 17 trillion
- Checkpoint type: Post-anneal (foundation)
- Instruction data: None
- RLHF or post-training: None

This checkpoint represents the final pretrained state after completion of the pretraining phase, including mid-training learning-rate anneals, but before instruction tuning or reinforcement learning.

### Optimizers

Optimizer learning rates during WSD stable phase:

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
- Domain-specific fine-tuning from a pretrained foundation
- Academic and industrial foundation model research

## Comparison with TrueBase

Trinity-Large-Base includes an additional 7 trillion training tokens compared to Trinity-Large-TrueBase, along with mid-training learning-rate anneals. These anneals stabilize training dynamics and typically improve downstream fine-tuning performance compared to the pre-anneal checkpoint. Researchers studying raw pretraining dynamics may prefer TrueBase, while those seeking a foundation for fine-tuning may prefer this checkpoint.

## Known Limitations

- Not aligned for safety, helpfulness, or conversational tone
- Requires substantial compute and expertise to fine-tune
- May exhibit raw or unstable behaviors typical of unaligned models
- No extended-context tuning beyond the 8K pretraining window

## License

Trinity-Large-Base is released under the OpenMDW License, version 1.1 (OpenMDW-1.1).
