---
base_model: ibm-granite/granite-4.2-30b
base_model_relation: quantized
library_name: transformers
pipeline_tag: text-generation
license: apache-2.0
language:
  - en
  - de
  - es
  - fr
  - ja
  - pt
  - ar
  - cs
  - it
  - ko
  - nl
  - zh
datasets:
  - NeelNanda/pile-10k
tags:
  - granite
  - granite-4.2
  - ibm
  - awq
  - int4
  - 4-bit
  - auto-round
  - vllm
  - xpu
  - intel-arc
  - reasoning
  - thinking
  - tool-calling
quantized_by: derikn
---

# Granite-4.2-30B AWQ INT4 (W4A16, group 128)

4-bit weight-only quantization of [ibm-granite/granite-4.2-30b](https://huggingface.co/ibm-granite/granite-4.2-30b),
built with Intel's [AutoRound](https://github.com/intel/auto-round) and tested on Intel Arc Pro B70 GPUs.

This is an unofficial community quantization by `derikn`. IBM did not author it and does not endorse
it. GRANITE is a registered trademark of International Business Machines Corporation. For the model
itself, its capabilities and its evaluation results, read the
[base model card](https://huggingface.co/ibm-granite/granite-4.2-30b).

## What this is

| | |
|---|---|
| Base model | `ibm-granite/granite-4.2-30b` (Apache 2.0) |
| Parameters | 29,276,770,304 (see the note on the parameter count below) |
| Quantization | AWQ, weight-only, 4-bit (W4A16) |
| Group size | 128, symmetric, zero-point off |
| Method | AutoRound `auto_awq` export, `gemm` version |
| Kept at 16-bit | `lm_head` and the non-text modules |
| Size on disk | 16.4 GB in 6 safetensors shards, down from 58.6 GB at bf16 |
| Native context | 131,072 tokens, same as the base model |
| Chat template | included, with `enable_thinking` and `low_effort` control |
| Extra files | `granite_thinking_parser.py`, IBM's reasoning parser for vLLM |

Only the linear weights are quantized. The architecture, tokenizer, chat template and configuration
match the base model, and no fine-tuning or extra training data went into this.

### Note on the parameter count

The Safetensors panel on this page reports a model size of about 5B parameters. That is not the size of
the model. The 4-bit weights are packed into int32 tensors, eight weights per int32, and the panel's
total counts that packed storage instead of the parameters it encodes.

This checkpoint holds **29,276,770,304 parameters**, the same count as the base model. The Hub API's own
per-dtype breakdown adds up to exactly that figure (`I32` 28,454,158,336 plus `BF16` 822,611,968), while
the panel's single total does not. `I32` and `BF16` describe storage, not precision of the model: packed
4-bit weights, and the tensors held at bfloat16.

The repository mirrors the base model layout, with `quantization_config.json` added by AutoRound and
IBM's `granite_thinking_parser.py` kept alongside it.

## How it was made

Quantized from the bf16 checkpoint with AutoRound **0.15.1** on a single Intel Arc Pro B70 (34 GB).
Weights stream to the card during tuning, which keeps VRAM bounded:

```
python layer2/quantize.py \
  --model <base-model-dir> \
  --format auto_awq \
  --device xpu:0 \
  --out-dir ./granite-4.2-30b-awq-int4 \
  --low-gpu-mem --n_samples 128 --seqlen 1024 --batch_size 8 \
  --torch-compile
```

Calibration used **NeelNanda/pile-10k**: 128 samples of 1024 tokens each, batch size 8. `lm_head` and
the non-text modules stayed at 16-bit.

The script above is a private wrapper around AutoRound and is not published, so that exact command
will not run for you. These are the AutoRound settings it passes, which are the whole recipe:

- export format `auto_awq`, W4A16 (4-bit weight-only), group size 128, symmetric, zero-point off
- `lm_head` and the non-text modules excluded from quantization
- calibration on NeelNanda/pile-10k, 128 samples of 1024 tokens, batch size 8
- weights streamed to the device during tuning, to keep VRAM bounded
- `torch.compile` enabled on the tuning step

## Running it

Tested on **vLLM XPU** (`vllm/vllm-openai-xpu:nightly`, vLLM `0.30.1rc1`) with tensor parallelism
across two Arc Pro B70s, fp8 KV cache and the full 128K context:

```bash
vllm serve /models/Granite-4.2-30B-AWQ-INT4 \
  --served-model-name granite-4.2-30b-awq \
  --quantization awq --dtype bfloat16 \
  --max-model-len 131072 --block-size 64 \
  --max-num-seqs 8 --max-num-batched-tokens 16384 \
  --gpu-memory-utilization 0.90 --kv-cache-dtype fp8_e4m3 \
  --enable-prefix-caching \
  --tool-call-parser qwen3_coder --enable-auto-tool-choice \
  --reasoning-parser granite_thinking_parser \
  --trust-remote-code --tensor-parallel-size 2
```

Container settings that matter on Arc: `--device=/dev/dri`, `--group-add` for the render and video
groups, `--ipc=host`, `--security-opt seccomp=unconfined`, and `ZE_AFFINITY_MASK` set to the cards you
want to use. Without the device, group and seccomp combination Level Zero reports zero devices.

### Thinking modes

Granite 4.2 has three thinking modes, selected either through OpenAI's `reasoning_effort` or through
the chat template. vLLM accepts the whole `reasoning_effort` scale, but only three states exist:

| Request | Behaviour |
|---|---|
| `reasoning_effort: "none"` (or `enable_thinking: false`) | no thinking |
| `reasoning_effort: "low"` (or `low_effort: true`) | brief reasoning |
| omitted, or `minimal` / `medium` / `high` / `xhigh` / `max` | full thinking |

Measured with `usage.completion_tokens_details.reasoning_tokens` on the same prompt: `none` gives 0,
`low` gives about 10, the rest give between 100 and 200. `minimal` does not produce minimal reasoning;
it behaves like full thinking. `medium`, `high`, `xhigh` and `max` are all the same as each other.

### What was tested, and what was not

Tested:

- 128K context loads and serves. That is the native maximum. The base model documents an optional
  extension to 512K, which needs rope extrapolation and about four times the KV memory.
- Thinking works and separates from the answer. vLLM returns it as `message.reasoning`, and a LiteLLM
  proxy returns it as `reasoning_content`.
- Tool calling works with the `qwen3_coder` parser, which matches the template format
  `<tool_call><function=...><parameter=...>`. IBM's serving recipe recommends the same parser.
- This checkpoint has no MTP tensors, so MTP speculative decoding is not available. That needs a
  separate draft model.

Not tested:

- No accuracy or throughput numbers are published with this repository. The quantizer's own
  measurements come from one home-lab setup (Arc Pro B70, XPU vLLM nightly, fp8 KV cache) and are not
  a fair comparison for anyone running different hardware or software. Model quality is the base
  model's, so read its card.

## Licence and attribution

Apache License 2.0, inherited from the base model. `LICENSE` and `NOTICE.txt` are in this repository.

- Base model: [ibm-granite/granite-4.2-30b](https://huggingface.co/ibm-granite/granite-4.2-30b) (Apache 2.0)
- Quantization tooling: [intel/auto-round](https://github.com/intel/auto-round) (Apache 2.0)
- Quantizer: a private in-house wrapper around AutoRound (not published)
- The name follows IBM's
  [derivative naming guidance](https://www.ibm.com/granite/docs/models/granite4-2): entity first,
  family name next, descriptors last.
