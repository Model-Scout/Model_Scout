---
license: other
license_name: kanana-open-license
license_link: https://huggingface.co/kakaocorp/kanana-2-3b-instruct/blob/main/LICENSE
language:
- ko
- en
library_name: mlx
pipeline_tag: text-generation
tags:
- mlx
- kanana
- korean
base_model: kakaocorp/kanana-2-3b-instruct
base_model_relation: quantized
---

# kanana-2-3b-instruct-4bit

Powered by Kanana.

An **MLX conversion** of [`kakaocorp/kanana-2-3b-instruct`](https://huggingface.co/kakaocorp/kanana-2-3b-instruct) so the model
runs natively on Apple Silicon. Weights are quantized to MLX affine 4-bit (group_size=32).

This is an **independent community conversion**. It is **not affiliated with or
endorsed by Kakao Corp.**

Mirrored from [`choipilkyu/kanana-2-3b-instruct-MLX-4bit`](https://huggingface.co/choipilkyu/kanana-2-3b-instruct-MLX-4bit), where these
weights were first published.

## Changes from the original

This repository changes the **file format only** — the architecture is stock
`Qwen3ForCausalLM`, which `mlx-lm` supports directly, so no modelling code was
written or altered.

1. Converted the PyTorch/safetensors weights to MLX format with `mlx-lm`.
2. Applied MLX affine 4-bit quantization (`group_size=32`, not the
   `mlx-lm` default of 64 — see Quantization below).

No weights were retrained. Numerics are unchanged apart from the quantization
noted above. Per Kanana Open License §3.1(iii), this section is the notice that
the distributed files were modified by the maintainer of this repository.

| Provenance | This build |
|---|---|
| Source revision converted | [`6a5d7889964c`](https://huggingface.co/kakaocorp/kanana-2-3b-instruct/tree/6a5d7889964c4c590299d16e309eabab1f73f8a9) |
| `model.safetensors` sha256 | `389e544b520d11971f47876261aadba330a37a1afe15613189b051bebcf9ce4e` |

## Usage

```bash
pip install mlx-lm
```

```bash
mlx_lm.generate --model mlx-community/kanana-2-3b-instruct-4bit --prompt "안녕하세요"
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/kanana-2-3b-instruct-4bit")
messages = [{"role": "user", "content": "안녕하세요"}]
prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
print(generate(model, tokenizer, prompt=prompt, max_tokens=512))
```

## Variants

| Variant | Size | Perplexity | vs bf16 |
|---|---|---|---|
| [`kakaocorp/kanana-2-3b-instruct`](https://huggingface.co/kakaocorp/kanana-2-3b-instruct) (upstream, bf16) | 5.90 GB | 4.404 ± 0.052 | — |
| [`kanana-2-3b-instruct-8bit`](https://huggingface.co/mlx-community/kanana-2-3b-instruct-8bit) | 3.38 GB | 4.415 ± 0.052 | +0.2% |
| [`kanana-2-3b-instruct-6bit`](https://huggingface.co/mlx-community/kanana-2-3b-instruct-6bit) | 2.58 GB | 4.520 ± 0.054 | +2.6% |
| [`kanana-2-3b-instruct-mixed_4_6`](https://huggingface.co/mlx-community/kanana-2-3b-instruct-mixed_4_6) | 2.08 GB | 4.982 ± 0.057 | +13.1% |
| [`kanana-2-3b-instruct-4bit`](https://huggingface.co/mlx-community/kanana-2-3b-instruct-4bit) | 1.99 GB | 5.104 ± 0.058 | +15.9% |

**There is no bf16 build here on purpose.** The upstream repository is already
bfloat16 safetensors and `mlx-lm` supports the architecture, so

```python
from mlx_lm import load
model, tokenizer = load("kakaocorp/kanana-2-3b-instruct")   # works as-is
```

loads the original directly. A bf16 repo under this account would be a 5.9 GB
copy of bytes you can already fetch, so the table above cites the upstream repo
as the baseline instead. **For most uses 8-bit is the right default:** half the
size, and the perplexity difference from the original is inside the measurement
error.

## Speed and memory

Measured on an Apple M1 Pro (16 GB), macOS 26.4, mlx 0.32.0, mlx-lm 0.31.3 with the command the upstream
[`BENCHMARKS.md`](https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/BENCHMARKS.md)
uses, averaged over three trials:

```bash
mlx_lm.benchmark --model mlx-community/kanana-2-3b-instruct-4bit -p 2048 -g 128
```

| Variant | Prompt (2048) tok/sec | Generation (128) tok/sec | Peak memory GB |
|---|---|---|---|
| [`kakaocorp/kanana-2-3b-instruct`](https://huggingface.co/kakaocorp/kanana-2-3b-instruct) (upstream, bf16) | 529.3 | 23.2 | 7.15 |
| [`kanana-2-3b-instruct-8bit`](https://huggingface.co/mlx-community/kanana-2-3b-instruct-8bit) | 331.0 | 40.8 | 4.33 |
| [`kanana-2-3b-instruct-6bit`](https://huggingface.co/mlx-community/kanana-2-3b-instruct-6bit) | 323.8 | 45.3 | 3.65 |
| [`kanana-2-3b-instruct-mixed_4_6`](https://huggingface.co/mlx-community/kanana-2-3b-instruct-mixed_4_6) | 322.5 | 54.1 | 3.15 |
| [`kanana-2-3b-instruct-4bit`](https://huggingface.co/mlx-community/kanana-2-3b-instruct-4bit) | 322.4 | 56.2 | 3.05 |

Generation is roughly **2.4x faster at 4-bit than at bf16**, on **2.3x less
memory** — that is the reason to quantize at all, and on a 16 GB machine the
memory column is what decides whether the model runs beside anything else.

**Prompt processing goes the other way, and that is expected.** Prefill is
compute-bound, so dequantizing weights costs more than the narrower memory
traffic saves; generation is memory-bound, so the same trade runs in reverse.
If your workload is dominated by long prompts rather than long completions,
the quantized builds are not faster.

These numbers describe one machine. They are not comparable to figures measured
on other hardware, and the ratios between variants transfer better than the
absolute values.

## Quantization

Perplexity measured with the official `mlx_lm.perplexity` tool: 60 samples of
1,024 tokens from `allenai/tulu-3-sft-mixture`, the same sample set for every
variant (the loader shuffles unseeded, so the seed is fixed explicitly —
otherwise each variant is scored on different text and the numbers are not
comparable).

**The 4-bit build uses `group_size=32`, not the `mlx-lm` default of 64.** For
*this* model the default is too coarse: perplexity degrades **+33.4% at g64
against +15.9% at g32**, for 0.2 GB more on disk.

**That is a fact about this model, not a rule about small models.** The same
comparison, run the same way on three other Korean models, gives three different
answers:

| Model | 4-bit `g64` against `g32` |
|---|---|
| `kanana-2-3b-instruct` (this one) | g32 far better — +15.9% against +33.4% |
| `kanana-2-1.3b-instruct` | g32 better — +6.7% against +10.8% |
| `Midm-2.0-Mini-Instruct` (2.3B) | indistinguishable — paired t = 0.3 |
| `A.X-4.0-Light` (7.3B) | **g64 better** — paired t = 7.5, and 0.5 GB smaller |

Model size predicts nothing here: the two extremes are a 3B and a 7.3B. Measure
group size per model rather than defaulting either way — including defaulting to
what worked here.

### Mixed-precision recipes

`mlx-lm` ships four `mixed_N_M` recipes: most modules are quantized to N bits and
a fixed 14% — `v_proj`/`down_proj` in the outer eighths of the stack and every
third layer, plus `lm_head` — is promoted to M. All four were built at
`group_size=32` and scored on the same tokens as the table above.

| Recipe | Size | Perplexity |
|---|---|---|
| `mixed_2_6` | 1.38 GB | 3,361,128 |
| `mixed_3_4` | 1.64 GB | 211.4 |
| `mixed_3_6` | 1.73 GB | 114.5 |
| `mixed_4_6` | 2.08 GB | **4.982** |

What sets the floor is the low bits, not the boost. Nothing below 4-bit survives
at this model size however generous the promotion is, because the promotion
reaches only 14% of the modules — going from a 4-bit boost to a 6-bit one buys
`mixed_3_6` a halving of an already unusable number. Only `mixed_4_6` is
published.

That one does beat uniform 4-bit at the same group size: 4.982 against 5.104.
Because both builds are scored on identical tokens the comparison can be paired,
which takes token difficulty out of the variance — the mean difference over the
61,380 shared tokens is **+0.0242 ± 0.0020 nats (t = 11.9)**, against 0.09 GB
more on disk. Comparing the two published standard errors instead would overstate
the uncertainty eightfold, since it treats the shared text as if each model had
been scored on its own sample.

The recipe's advantage is also specific to this model. On `Midm-2.0-Mini-Instruct`
the identical comparison runs the other way and just as decisively — `mixed_4_6`
loses to uniform 4-bit at t = -19 while being the larger file. Neither the recipe
nor the group size transfers; both are worth an hour of measurement per model.

Caveat: this is an English corpus, and Kanana is a Korean-centric model. The
numbers measure quantization damage, not Korean ability.

### What is still missing, and what is planned

Perplexity is a proxy. It shows that a build has been damaged; it does not show
what capability was lost, and it is measured here on English text for a model
whose reason to exist is Korean.

The evaluation that would answer the real question is the benchmark set Kakao
reports on their own card — **KMMLU** and **HAE-RAE** — run against each build
and reported as retention against the upstream model. The standard way to do
that is [`mlx_lm.evaluate`](https://github.com/ml-explore/mlx-lm), which wraps
EleutherAI's `lm-evaluation-harness`; both Korean task suites are already in it.

That measurement is planned, and the numbers will be added here when they exist.
They will not be estimated from the perplexity figures above — the two do not
substitute for each other, and a 0.5% perplexity change is not evidence about a
benchmark score in either direction.

## License and use restrictions

The model weights are Kakao's, released under the
[Kanana Open License Agreement](https://huggingface.co/kakaocorp/kanana-2-3b-instruct/blob/main/LICENSE) — a copy travels with this
repository as [`LICENSE`](LICENSE), together with the required
[`NOTICE`](NOTICE).

**Use is subject to Kakao's Guidelines for Responsible AI** (§2.2 of the
agreement). By using these weights you accept those restrictions, and if you
redistribute them you must pass the same obligation on to your recipients.

**A separate commercial licence from Kakao is required (§4.1)** before you:

- offer third parties access to the model through an API, cloud platform or
  other remote access service;
- ship it to third parties as part of a system-integration or on-premise
  solution; or
- **embed it in an on-device product offered to third parties** — worth reading
  carefully here, since an Apple Silicon build is an on-device artifact by
  nature.

Using it to build and run your own service does not require that licence
(§4.2). This summary is not legal advice; read the agreement.

> Kanana is licensed in accordance with the Kanana Open License Agreement.
> Copyright © KAKAO Corp. All Rights Reserved.
