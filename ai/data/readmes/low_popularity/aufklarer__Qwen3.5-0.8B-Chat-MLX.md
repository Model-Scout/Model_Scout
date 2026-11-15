---
license: apache-2.0
language:
  - en
  - zh
  - de
  - es
  - fr
  - it
  - ja
  - ko
  - pt
  - ru
tags:
  - mlx
  - qwen3.5
  - text-generation
  - on-device
  - apple-silicon
  - quantized
  - int4
  - int5
  - int8
base_model: Qwen/Qwen3.5-0.8B
library_name: mlx
pipeline_tag: text-generation
---

# Qwen3.5-0.8B Chat — MLX (Apple Silicon)

Text-only extraction of [Qwen3.5-0.8B](https://huggingface.co/Qwen/Qwen3.5-0.8B),
quantized with [MLX](https://github.com/ml-explore/mlx) for on-device chat on
Apple Silicon. Three bit widths are published so the quality/size tradeoff can be
made with measured numbers rather than assumed.

**INT8 is the recommended default.** INT4 is kept for size-constrained use but is
no longer recommended for anything that parses the reply as JSON — see
[Measured quality](#measured-quality).

## Model

| | |
|---|---|
| Parameters | 752 M (text model; the tied embedding / LM head is 254 M of that) |
| Architecture | Qwen3.5 hybrid — 24 layers, 18× DeltaNet linear attention + 6× GatedAttention, pattern `[linear, linear, linear, full] × 6` |
| Positional encoding | Partial RoPE, 25 % of `head_dim` (64 of 256 rotary dims) |
| Output head | Tied to the token embedding (`lm_head` = `embed_tokens`) |
| Format | MLX safetensors |
| Quantization | `mx.quantize` affine round-to-nearest, group size 64, at 4 / 5 / 8 bits |
| Declared context | 2048 (`max_seq_len`); the MLX path does not enforce it — DeltaNet is recurrent and the KV cache grows on demand |
| Vocabulary | 248 320 |

Norm weights, `A_log`, `dt_bias` and the causal `conv1d` kernels are **not**
quantized; they stay float. Quantized tensors are stored as MLX's
`weight` / `scales` / `biases` triple with fp16 scales and biases.

| Variant | File size | Quantized | Use it when |
|---|---|---|---|
| **INT8** | 800 MB | 8-bit, group 64 | Default. Effectively indistinguishable from bf16. |
| **INT5** | 518 MB | 5-bit, group 64 | Memory matters more than the last 2 % of quality. |
| INT4 | 424 MB | 4-bit, group 64 | Smallest download, free-form text only. Not for JSON. |

## Files

| File | Size | Description |
|---|---|---|
| `int4/model.safetensors` | 424 MB | INT4 weights |
| `int4/config.json` | 1.3 kB | Architecture + `quantization_bits: 4`, `quantization_group_size: 64` |
| `int4/tokenizer.json` | 12.8 MB | Tokenizer |
| `int4/tokenizer_config.json` | 16.7 kB | Chat template and special tokens |
| `int5/model.safetensors` | 518 MB | INT5 weights |
| `int5/config.json` | 1.3 kB | Same, `quantization_bits: 5` |
| `int5/tokenizer.json` | 12.8 MB | Tokenizer |
| `int5/tokenizer_config.json` | 16.7 kB | Chat template and special tokens |
| `int8/model.safetensors` | 800 MB | INT8 weights |
| `int8/config.json` | 1.3 kB | Same, `quantization_bits: 8` |
| `int8/tokenizer.json` | 12.8 MB | Tokenizer |
| `int8/tokenizer_config.json` | 16.7 kB | Chat template and special tokens |

Each variant is self-contained: one directory is everything needed to run it.
The vision tower and the multi-token-prediction draft head (`mtp.*`) are not
included — no runtime here reads them. Dropping the draft head alone took 14 MB
off the INT4 download compared with the previous revision.

## Measured quality

Every number below is measured, not estimated. Method: the exporter's exact
quantize/dequantize step is reproduced on the bf16 checkpoint — same kernel,
same bit width, same group size — and the result is compared against the
unmodified bf16 model on identical inputs. 32 768 teacher-forced tokens per
corpus. A control run with quantization disabled reproduced bf16 exactly
(0.000 % perplexity change, 100 % agreement, 0 KL), so the deltas below are the
quantization and nothing else.

Perplexity is relative to the bf16 checkpoint; **lower is better and 0 % is the
target.** Top-1 agreement is how often the quantized model's most likely next
token is the same as bf16's.

| Variant | Perplexity vs bf16 (wikitext) | Perplexity vs bf16 (dialogsum) | Top-1 agreement | Mean KL from bf16 |
|---|---|---|---|---|
| bf16 reference | 22.798 | 4.846 | — | — |
| **INT8** | **+0.19 %** | −0.002 % | 97.9 % / 98.8 % | 0.0013 / 0.0008 nats |
| **INT5** | **+2.2 %** | +1.6 % | 89.6 % / 94.7 % | 0.032 / 0.016 nats |
| INT4 | **+19.9 %** | +9.5 % | 78.3 % / 88.5 % | 0.149 / 0.079 nats |

### Structured replies

24 tasks that ask for a single JSON object and are scored the way a strict
parser would score them: greedy decoding, no repair pass, no leniency for
markdown fences or prose. bf16 passes 24 of 24.

| Variant | Strict JSON valid | Byte-identical to bf16 |
|---|---|---|
| **INT8** | **24 / 24** | 18 / 24 |
| **INT5** | **23 / 24** | 12 / 24 |
| INT4 | **18 / 24** | 5 / 24 |

The INT4 failures are not near-misses. Five of the six are **unbalanced braces** —
replies such as `{"action_items": [{"owner": "Chen", "task": "..."]}` that drop
the object's closing brace, which no parser recovers from. The sixth invents a
different key name. This is why INT4 is no longer recommended for any consumer
that parses the reply: it degrades exactly where a downstream pipeline is least
able to cope. INT5's single failure is the same kind of dropped closing brace.

Raising only the embedding to 8 bits while keeping the body at 4 was measured and
does not rescue INT4: +15.4 % perplexity, 23 of 24 JSON. If structured output
matters, use INT5 or INT8 rather than a mixed INT4.

## Usage

### Swift (speech-swift)

```swift
import Qwen3Chat

let model = try await Qwen35MLXChat.fromPretrained(quantization: .int8)
let response = try model.generate(
    messages: [ChatMessage(role: .user, content: "Hello!")],
    sampling: ChatSamplingConfig(temperature: 0.3, maxTokens: 100)
)
```

> **INT5 and INT8 need a runtime that reads the bit width from `config.json`.**
> Older speech-swift versions build every `QuantizedLinear` and
> `PreQuantizedEmbedding` with `bits = 4` hardcoded, which fits the INT4 file
> only; they will not read an INT5 or INT8 file correctly. Use a speech-swift
> version that takes `quantization_bits` and `quantization_group_size` from
> `config.json`, or stay on INT4.

### Python

```python
import json
import mlx.core as mx
from huggingface_hub import snapshot_download

path = snapshot_download("aufklarer/Qwen3.5-0.8B-Chat-MLX",
                         allow_patterns=["int8/*"])

cfg = json.load(open(f"{path}/int8/config.json"))
weights = mx.load(f"{path}/int8/model.safetensors")

# Quantized tensors are stored as a weight/scales/biases triple. Always take the
# bit width and group size from config.json rather than assuming them.
up = mx.dequantize(
    weights["layers.0.mlp.up_proj.weight"],
    weights["layers.0.mlp.up_proj.scales"],
    weights["layers.0.mlp.up_proj.biases"],
    group_size=cfg["quantization_group_size"],
    bits=cfg["quantization_bits"],
)
print(cfg["quantization"], up.shape)   # int8 (3584, 1024)
```

The layout is the custom key set the Swift runtime loads (`layers.N.linear_attn.*`
for DeltaNet, `layers.N.self_attn.*` for the attention layers), not the
`mlx-lm` naming, so `mlx_lm.load` will not read it directly.

### CLI

```bash
# One variant only — do not pull all three
hf download aufklarer/Qwen3.5-0.8B-Chat-MLX --include "int8/*" \
    --local-dir ./qwen35-0.8b-int8
```

## A note on earlier downloads

These files replace an earlier export in which the model's **final** RMSNorm
weight was written without the `+1` offset that Qwen3.5 stores its norm weights
with. That mis-scaled the hidden state feeding the LM head and cost about
+19 % perplexity on its own, on top of any quantization error. If you downloaded
this repository before this revision, re-download it; the numbers in this card
apply only to the current files.

## Source

Converted from [Qwen/Qwen3.5-0.8B](https://huggingface.co/Qwen/Qwen3.5-0.8B)
(Apache-2.0). The vision tower and the multi-token-prediction head are dropped;
the text model is quantized with `mx.quantize` at group size 64, the
zero-centered RMSNorm weights are folded to `1 + w`, and the DeltaNet `conv1d`
kernels are transposed to MLX's channels-last layout.

## Links

- [speech-swift](https://github.com/soniqo/speech-swift) — Apple SDK
- [Docs](https://soniqo.audio/getting-started) — install and CLI docs
- [soniqo.audio](https://soniqo.audio) — website
- [blog](https://soniqo.audio/blog) — blog
