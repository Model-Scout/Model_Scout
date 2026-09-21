---
language:
- en
- ar
- zh
- fr
- de
- hi
- id
- it
- ja
- ko
- pl
- pt
- ru
- es
- th
- vi
library_name: mlx
license: other
license_name: lfm1.0
license_link: LICENSE
base_model: LiquidAI/LFM2.5-2.6B
base_model_relation: quantized
pipeline_tag: text-generation
tags:
- mlx
- jang
- jang_6m
- quantized
- apple-silicon
- lfm2.5
- liquid
- edge
- reasoning
- osaurus
---

<p align="center"><a href="https://osaurus.ai"><img src="./osaurus-x-banner.png" alt="Osaurus AI"></a></p>

# OsaurusAI/LFM2.5-2.6B-JANG_6M

JANG_6M build of [LiquidAI/LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B) — LiquidAI's **always-thinking** 2.6B agentic model (16 languages, 128K context), quantized for Apple Silicon with 6-bit affine FFN weights, 8-bit token-mixing operators, and **learned codes**: activation-aware AWQ folds plus GPTQ codes-only QAT on every FFN tensor. This is the quality build of the pair — smaller *and* more faithful than MXFP8.

## Bundle

| Field | Value |
|---|---|
| Source | `LiquidAI/LFM2.5-2.6B` @ `dca1825` (LFM 1.0 license) |
| Architecture | `lfm2` dense hybrid — 22 double-gated short-conv (LIV) blocks + 8 GQA attention layers, 2.69B params, 128K ctx |
| On-disk size | 2.30 GiB (1 shard) |
| Quantization | attention + conv projections 8-bit · FFN w1/w2/w3 6-bit · tied embedding 6-bit — all affine, group size 32 |
| AWQ | per-channel folds (α 0.25, clip 0.5–2.0) into `ffn_norm`→w1/w3 and w3-rows→w2 — function-preserving, zero runtime cost |
| QAT | GPTQ codes-only learned rounding on the fixed f16 grid, all 90 FFN tensors, BRECQ-sequenced w1/w3→w2, best-of-RTN guard — mean recon error **−64.7%** vs RTN (`qat_report.json`) |
| Calibration | canonical mix rendered through the chat template **with greedy thinking continuations** (10.4K tokens/layer) — the model's own `<think>` distribution is in-calibration |
| Norms, conv kernels | fp16 passthrough — plain Llama RMSNorm, **no +1 shift** |
| Attention | 32 heads / 8 KV heads (GQA), head_dim 64, per-head q/k RMSNorm, NeoX RoPE θ = 1e7 |
| Modality | **text-only** (verified from the tensor index — no vision/audio weights; the template's `<image>` item handling is inert on this model) |

## Measured (M5 Max, stock mlx-lm 0.31, vs bf16 source)

Two 768-token held-out texts: general/encyclopedic and agentic/code+thinking (the workload LiquidAI built this model for). KL is mean full-vocabulary KL(bf16 ‖ quant).

| Metric | general | agentic |
|---|---|---|
| Top-1 agreement | 97.3% | **98.4%** |
| Mean KL | 0.033 bits | **0.0033 bits** |
| Perplexity (bf16: 3.065 / 2.812) | 3.076 | 2.787 |

Decode **156 tok/s** greedy (bf16 source: 83 tok/s in the same harness). Runtime gates all pass: greedy math reasoning with clean `<think>…</think>` close and eos stop, card-default sampling coherence, Liquid-format tool calls, grounded 2K-token long-context answers.

## Profile comparison

| Bundle | Size | Top-1 (gen / agentic) | Mean KL bits (gen / agentic) | Decode |
|---|---|---|---|---|
| [`LFM2.5-2.6B-JANG_6M`](https://huggingface.co/OsaurusAI/LFM2.5-2.6B-JANG_6M) | **2.30 GiB** | 97.3% / **98.4%** | 0.033 / **0.0033** | **156 tok/s** |
| [`LFM2.5-2.6B-MXFP8`](https://huggingface.co/OsaurusAI/LFM2.5-2.6B-MXFP8) | 2.59 GiB | 91.1% / 93.4% | 0.272 / 0.113 | 146 tok/s |
| vendor MLX 6bit (gs64 RTN) | 2.04 GiB | 97.5% / 97.9% | 0.026 / 0.0084 | — |
| vendor MLX mxfp8 (RTN) | 2.59 GiB | 91.7% / 92.7% | 0.303 / 0.115 | — |

On general text the 6-bit builds are within sample noise of each other; on the agentic/thinking distribution this build's KL is **2.5× lower** than the vendor's 6-bit RTN export — that is what the QAT/AWQ calibration is aimed at. And as on every model we have measured, **6-bit affine beats MXFP8 on fidelity while being smaller**: e4m3 elements carry ~3 mantissa bits, so "8-bit MX" is not strictly better than 6-bit affine with a per-group scale and bias.

## Chat / reasoning

- **Thinking is ALWAYS on.** LFM2.5-2.6B is a pure reasoning model: the chat template unconditionally opens `<think>` at the start of every assistant turn. There is **no** `enable_thinking` switch — the only template kwarg is `preserve_thinking` (default `false`: prior turns' reasoning is stripped except after the last user turn).
- The template is shipped verbatim (`chat_template.jinja`, also inlined into `tokenizer_config.json`), and `capabilities.think_in_template = true` is stamped so think-tag parsers route the pre-opened block correctly.
- **No BOS trap:** the template emits `<|startoftext|>` itself and the tokenizer never auto-adds one — both `apply_chat_template(tokenize=True)` and re-encoding the rendered string yield exactly one BOS.
- Stop token `eos_token_id = 124900` (`<|im_end|>`).
- Tool calls use the Liquid Python-call format: `<|tool_call_start|>[get_weather(city='Seoul')]<|tool_call_end|>` (verified live).
- Sampling defaults (vendor card + `generation_config.json`, mirrored in `jang_config.chat.sampling_defaults` and gate-checked against each other at build): `temperature 0.1 · top_k 50 · repetition_penalty 1.1`.

## Usage

Standard MLX safetensors with a per-module `{bits, group_size, mode}` map in `config.json[quantization]`. Loads with **stock `mlx_lm >= 0.31`** — no custom code, no `trust_remote_code`. Runs in [Osaurus](https://osaurus.ai) and vMLX-compatible runtimes (`lfm2` family). Fits in 8 GB of unified memory.

```python
from mlx_lm import load, generate

model, tokenizer = load("OsaurusAI/LFM2.5-2.6B-JANG_6M")
prompt = tokenizer.apply_chat_template(
    [{"role": "user", "content": "Which number is bigger, 9.11 or 9.8?"}],
    add_generation_prompt=True,
)
print(generate(model, tokenizer, prompt=prompt, max_tokens=1024))
```

---

Quantized and verified by **Jinho Jang** (eric@osaurus.ai). Base model © Liquid AI, released under the [LFM 1.0 license](LICENSE).
