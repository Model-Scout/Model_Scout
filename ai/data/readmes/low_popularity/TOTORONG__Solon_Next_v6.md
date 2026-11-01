---
language:
- ko
- en
license: other
base_model:
- RadixArk/Qwen3.8-Flash-Next-NVFP4
tags:
- qwen
- qwen4-exp
- qwen3.8
- korean
- korean-history
- stem
- nvfp4
- moe
- axolotl
- fsdp2
- vllm
library_name: transformers
pipeline_tag: text-generation
---

# Solon-Next_v6

**Solon-Next_v6** is an NVFP4-preserving fine-tune of **RadixArk/Qwen3.8-Flash-Next-NVFP4**, enhanced with additional Korean language, Korean history, and STEM knowledge.

It was trained directly from the quantized checkpoint using **Axolotl + FSDP2** on two NVIDIA RTX PRO 6000 Blackwell GPUs, and the final LoRA weights were merged back into the ModelOpt NVFP4 experts with scale-aware re-quantization.

The goal of this model is to retain the efficiency and general capabilities of the original Qwen3.8-Flash-Next NVFP4 model while improving Korean language understanding, Korean knowledge, Korean history, and STEM knowledge/reasoning.

## Model Overview

| Item | Description |
|---|---|
| Model name | **Solon-Next_v6** |
| Base model | **RadixArk/Qwen3.8-Flash-Next-NVFP4** |
| Architecture | Qwen3.8-Flash-Next / `qwen4_exp_text` |
| Main additions | Korean, Korean history, STEM |
| Training framework | Axolotl |
| Distributed training | FSDP2 |
| GPUs | 2 × NVIDIA RTX PRO 6000 Blackwell 96 GB |
| Quantization | ModelOpt NVFP4 |
| Adapter method | LoRA / rsLoRA |
| Expert training | ScatterMoE / NVFP4 expert LoRA |
| Serving | vLLM |

Solon-Next_v6 is not a dequantized BF16 reconstruction. The routed MoE experts remain in NVFP4 form after the final LoRA merge and re-quantization step.

# Training

The model was fine-tuned using **Axolotl + FSDP2** on:

```text
2 × NVIDIA RTX PRO 6000 Blackwell
96 GB VRAM per GPU
256 GB system RAM
Ubuntu Linux
```

Representative software environment:

```text
Python       3.12
Axolotl      0.19.0.dev0
Transformers 5.16.1
Accelerate   1.13.0
PEFT         0.20.0
torchao      0.17.x
CUDA         13.x
NCCL         2.29.7
```

Representative final training settings:

```yaml
sequence_len: 2816

lora_r: 24
lora_alpha: 12
peft_use_rslora: true

gradient_checkpointing: false
activation_checkpointing: true

fsdp_version: 2

cut_cross_entropy: true
chunked_cross_entropy: false

num_epochs: 1
```

The routed MoE expert LoRA path included:

```text
mlp.experts.gate_up_proj
mlp.experts.down_proj
```

The training configuration also included attention and linear-attention LoRA targets.

## Direct NVFP4 Fine-Tuning

A major technical goal of this project was to fine-tune the original NVFP4 checkpoint directly instead of converting the entire model to BF16 first.

The routed MoE experts remained in the ModelOpt NVFP4 representation during training.

The training stack used Axolotl, FSDP2, ScatterMoE, CUTLASS grouped FP4 kernels, rsLoRA, Cut Cross Entropy, and host-backed PLE / n-gram lookup.

## PLE / N-gram Embedding

Qwen3.8-Flash-Next contains a very large PLE / n-gram embedding table.

For the checkpoint used in this project, its logical shape is approximately:

```text
320,001,536 × 160
```

with FP8 storage of approximately:

```text
47.7 GiB
```

Loading this table as a normal FSDP parameter can trigger extremely large GPU allocations.

For training, the PLE table was therefore kept as a **host mmap-backed FP8 table**, and only the rows needed for the current batch were transferred to the GPU.

## Cut Cross Entropy

Training used Axolotl's Cut Cross Entropy integration for the `qwen4_exp_text` architecture to reduce memory required for full-vocabulary logits.

## ScatterMoE / CUTLASS NVFP4

The routed experts were trained through the ScatterMoE / CUTLASS FP4 path.

During development, multiple CUTLASS engine buckets could remain resident in VRAM and cause progressive memory growth. For the final setup, the CUTLASS engine factory was stabilized with a validated fixed bucket:

```text
Mt = 98304
```

for the workload used in this project.

# NVFP4 LoRA Merge

The final LoRA adapter was merged back into the original NVFP4 checkpoint without permanently converting the complete model into BF16.

```text
original NVFP4 weight
        ↓
temporary dequantization
        ↓
add LoRA delta
        ↓
re-quantize to NVFP4
        ↓
write updated shard
```

The original PLE tensors and input quantization scales are preserved.

## NVFP4 Expert Scale Handling

For ModelOpt-compatible routed experts, `gate_proj` and `up_proj` are fused by the inference implementation as the `w13` path.

Therefore the following values must be identical for each expert:

```text
gate_proj.weight_scale_2
up_proj.weight_scale_2
```

During the final merge, Solon-Next_v6 computes a shared global NVFP4 scale from the joint post-LoRA gate/up maximum value and re-quantizes both projections with the same scale. `down_proj` is quantized independently.

The final merged checkpoint was exhaustively checked across:

```text
48 MoE layers
× 512 experts
= 24,576 gate/up pairs
```

Result:

```text
pairs       : 24576
mismatched  : 0
match rate  : 100.000000%
```

# Evaluation

A full KMMLU evaluation was performed using standard multiple-choice log-likelihood scoring.

| KMMLU Group | Accuracy |
|---|---:|
| **Overall** | **68.33%** |
| Applied Science | 65.86% |
| Humanities / Social Sciences | 72.09% |
| Other | 67.48% |
| STEM | 69.99% |

Evaluation was performed with `lm-evaluation-harness` using vLLM as the inference backend.

# Fine-Tuning Recipe

The full fine-tuning recipe is included in the repository under:

```text
finetune/
```

It contains documentation and scripts for:

- Axolotl installation
- FSDP2 configuration
- Qwen4Exp PLE host mmap support
- NVFP4-aware loading
- Cut Cross Entropy
- ScatterMoE / CUTLASS configuration
- checkpoint handling
- NVFP4 LoRA merge
- NVFP4 scale validation
- vLLM installation
- vLLM serving

Please read:

```text
finetune/README.md
```

before attempting to reproduce the training.

# Running with vLLM

Solon-Next_v6 can be served with a recent vLLM build containing support for the Qwen3.8 / Qwen4Exp FP8 PLE loading path.

The exact installation procedure used for this model is documented in:

```text
finetune/README.md
```

Representative two-GPU serving command:

```bash
export CUDA_DEVICE_ORDER=PCI_BUS_ID
export NCCL_P2P_DISABLE=1
export NCCL_IB_DISABLE=1
export NCCL_DEBUG=WARN
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

vllm serve /path/to/Solon-Next_v6 \
  --tensor-parallel-size 2 \
  --enable-expert-parallel \
  --disable-custom-all-reduce \
  --gpu-memory-utilization 0.90 \
  --max-model-len 8192 \
  --max-num-seqs 2 \
  -cc.mode=0 \
  -cc.cudagraph_mode=FULL_DECODE_ONLY \
  --host 0.0.0.0 \
  --port 8000
```

The `NCCL_P2P_DISABLE=1` and `--disable-custom-all-reduce` settings were required for stability on the specific dual-RTX-PRO-6000 workstation used during development and may not be necessary on other systems.

## Example API Request

```bash
curl http://127.0.0.1:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "/path/to/Solon-Next_v6",
    "messages": [
      {
        "role": "user",
        "content": "Explain the significance of the Joseon Dynasty in Korean history."
      }
    ],
    "temperature": 0.7,
    "max_tokens": 512
  }'
```

# Intended Use

Solon-Next_v6 is intended primarily for:

- Korean-language text generation
- Korean knowledge tasks
- Korean history questions
- STEM questions
- general instruction following
- research and experimentation with NVFP4 MoE fine-tuning

The model also retains multilingual and general reasoning capabilities inherited from the base model.

# Limitations

Solon-Next_v6 is an experimental fine-tuned model.

Users should be aware that:

- factual errors and hallucinations are still possible;
- Korean historical or technical answers should be independently verified when accuracy is important;
- benchmark performance does not guarantee correctness on individual examples;
- the training recipe is tightly coupled to the Qwen4Exp / ModelOpt NVFP4 checkpoint layout used in this project;
- some Axolotl and vLLM patches may become unnecessary or incompatible as upstream projects evolve;
- the tested two-GPU communication settings are machine-specific.

# Base Model

Solon-Next_v6 is derived from:

**RadixArk/Qwen3.8-Flash-Next-NVFP4**

Please review the original model card, architecture documentation, license, and usage restrictions of the base checkpoint.

# Acknowledgements

This work builds on Qwen / Qwen3.8-Flash-Next, RadixArk's NVFP4 checkpoint, Axolotl, Hugging Face Transformers, PyTorch / FSDP2, torchao, NVIDIA CUTLASS, vLLM, lm-evaluation-harness, and KMMLU.
