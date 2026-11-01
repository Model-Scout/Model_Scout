---
language:
- ko
- en
license: apache-2.0
license_link: https://ai.google.dev/gemma/docs/gemma_4_license
library_name: transformers
pipeline_tag: text-generation
tags:
- conversational
- roleplay
- korean
- english
- vllm
- gisp
- pruning
base_model:
- mente-ai/uyu-2-28B
---

# uyu-2-28B

<div align="center">
<img src="https://raw.githubusercontent.com/menteai/vllm-uyu2/main/mente.png" width="30%" alt="uyu-2 logo" />
</div>

## Introduction

uyu-2-28B is a language model specialized for role-playing. It is
derived from `google/gemma-4-31B-it`, structurally pruned with Global Iterative
Structured Pruning (GISP), and then fine-tuned on English and Korean question-answering data.

## Model details

| Property | Value |
| --- | --- |
| Model name | uyu-2-28b |
| Parameters | 28,181,549,312 |
| Weight format | BF16 Safetensors, 6 shards |
| Weight size | 56,363,098,744 bytes |
| Layers | 60 |
| Hidden size | 5,376 |
| Configured maximum position length | 262,144 tokens |
| Validated serving length | 2,048 tokens |
| Modalities | Text only |
| Languages | Korean and English |
| Primary use | Conversation and role-play |
| Base checkpoint | `google/gemma-4-31B-it` |
| Pruning | GISP structured pruning |
| Recovery fine-tuning | LoRA on Korean and English question-answering data, merged into the weights |

## Pruning method: GISP

This checkpoint was produced through a staged sequence of globally ranked
structured pruning passes. Each pass used the same Korean role-playing
calibration set, BF16 inference, a fixed maximum sequence length, and
teacher-forced language-model loss restricted to assistant response tokens. The
model weights were frozen during calibration; only temporary scalar pruning
gates received gradients.

### 1. MLP group calibration and pruning

- Each layer's high-dimensional MLP intermediate space was divided into
  equal-sized contiguous channel groups.
- A scalar gate initialized to one was inserted after the gated MLP activation
  for every group. A backward pass for each calibration sample produced each
  gate's sensitivity score.
- Group importance was accumulated as the sample mean of
  `|gate * d(loss)/d(gate)|`.
- All eligible groups were ranked globally rather than layer by layer. The
  first and final decoder layers were protected.
- A small fraction of the lowest-scoring groups was selected. The global
  ranking concentrated most of these groups in a narrow range of later decoder
  layers.

### 2. Attention recalibration after MLP pruning

The selected MLP mask was applied before attention importance was measured, so
the second pass estimated attention sensitivity on the already reduced MLP
structure rather than on the original model.

- In a sliding-window layer, one pruning set contains a paired group of Q heads,
  their associated K/V head, and the corresponding input channels of `o_proj`.
- In a full-attention layer, one set contains a paired group of Q heads and the
  corresponding `o_proj` input channels. The shared global K/V heads were
  retained.
- Each set received a scalar gate and was scored with the same assistant-only
  `|gate * d(loss)/d(gate)|` criterion.
- A globally selected fraction of the lowest-scoring attention sets was removed
  across a subset of layers. Most selected sets came from sliding-window
  attention, with a smaller number coming from full-attention layers. This
  removed a substantial number of Q heads together with their paired
  sliding-window K/V heads.

### 3. Physical structural conversion and recovery

The masks were converted into smaller tensors rather than left as runtime
zeros. Selected MLP rows were removed from `gate_proj` and `up_proj`, with the
matching columns removed from `down_proj`. Selected attention rows were removed
from Q/K/V projections and the matching columns from `o_proj`. All decoder
layers and the full residual stream were retained, which leaves different MLP
widths and attention head counts in different layers.

The conversion also removed the multimodal weight keys, making this a text-only
checkpoint. A recovery LoRA was then trained on Korean and English
question-answering data and merged into the pruned weights. Exact per-layer
removed groups, heads, and retained tensor shapes are recorded in
`pruning_config.json` and duplicated under `pruned_shapes` in `config.json`.

## Standalone Transformers status

The included `modeling_uyu2.py` is required by the vLLM Transformers modeling
backend. Direct `AutoModelForCausalLM.generate()` is not supported in this
release: the checkpoint loads without missing or mismatched tensors, but direct
Transformers generation did not match the validated vLLM output in the current
test environment. Do not use the snippet below for inference until this section
is updated in a later release.

```bash
pip install "transformers>=5.13.0,<5.14" accelerate safetensors torch
```

## Evaluation status

The merged checkpoint has been smoke-tested for coherent Korean and English
generation with vLLM main and the bundled integration matching vllm-uyu2 0.3.2.
Validation included a three-conversation batch and a 1,983-token prompt. With a
2,048-token model length and `--gpu-memory-utilization 0.80`, vLLM reported
60,800 GPU KV cache tokens and 29.69x maximum concurrency on the validation
system. These capacity figures are hardware- and configuration-dependent.

No standardized benchmark results are published yet. The reported parameter
and pruning statistics are derived directly from the distributed checkpoint
and pruning metadata, not from an estimated model label. The checkpoint also
contains 60 non-parameter BF16 buffer elements.

## Limitations

- This is a role-playing model and may generate fictional, inaccurate, biased,
  unsafe, or otherwise undesirable content.
- It has not received a comprehensive safety evaluation. Applications should
  add safeguards appropriate to their use case.
- Pruning and task fine-tuning can reduce capabilities relative to the base
  checkpoint, especially outside Korean/English conversation and role-play.
- The configured maximum context is inherited from the base architecture, but
  this release has only been locally validated at short context lengths.
- This release is text-only despite retaining some tokenizer special tokens for
  base-tokenizer compatibility.
- Standalone Transformers generation is not supported in this release. Use the
  vLLM plugin path.

## License and attribution

The model weights and repository code are released under Apache License 2.0.
This is a modified derivative of `google/gemma-4-31B-it`; Google DeepMind did
not create or endorse uyu-2-28B. See `NOTICE` for modification and attribution
details.
