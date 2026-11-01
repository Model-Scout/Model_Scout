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
- mxfp8
- jang
- quantized
- apple-silicon
- lfm2.5
- liquid
- edge
- reasoning
- osaurus
---

<p align="center"><a href="https://osaurus.ai"><img src="./osaurus-x-banner.png" alt="Osaurus AI"></a></p>

# OsaurusAI/LFM2.5-2.6B-MXFP8

MXFP8 build of [LiquidAI/LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B) — LiquidAI's **always-thinking** 2.6B agentic model (16 languages, 128K context) in the OCP microscaling FP8 format, with **learned codes**: activation-aware AWQ folds plus GPTQ codes-only QAT on every FFN tensor. Same size as the vendor's own MXFP8 export, lower KL in both measured domains.

> **Want the best quality per GB?** Take
> [`LFM2.5-2.6B-JANG_6M`](https://huggingface.co/OsaurusAI/LFM2.5-2.6B-JANG_6M)
> (2.30 GiB, KL 0.033/0.0033 bits vs this build's 0.272/0.113). Choose MXFP8 when
> you want the OCP microscaling format end-to-end.

## Bundle

| Field | Value |
|---|---|
| Source | `LiquidAI/LFM2.5-2.6B` @ `dca1825` (LFM 1.0 license) |
| Architecture | `lfm2` dense hybrid — 22 double-gated short-conv (LIV) blocks + 8 GQA attention layers, 2.69B params, 128K ctx |
| On-disk size | 2.59 GiB (1 shard) |
| Quantization | every 2-D weight MXFP8 (`mx.quantize mode="mxfp8"`): e4m3 codes + e8m0 scales, group size 32 |
| AWQ | per-channel folds (α 0.25, clip 0.5–2.0) into `ffn_norm`→w1/w3 and w3-rows→w2 — function-preserving, zero runtime cost |
| QAT | GPTQ codes-only learned rounding of the e4m3 codes on the fixed e8m0 scale grid, all 90 FFN tensors, BRECQ-sequenced w1/w3→w2, best-of-RTN guard, byte-parity with `mx.quantize` verified at build — mean recon error **−69.7%** vs RTN (`qat_report.json`) |
| Calibration | canonical mix rendered through the chat template **with greedy thinking continuations** (10.4K tokens/layer) |
| Norms, conv kernels | fp16 passthrough — plain Llama RMSNorm, **no +1 shift** |
| Attention | 32 heads / 8 KV heads (GQA), head_dim 64, per-head q/k RMSNorm, NeoX RoPE θ = 1e7 |
| Modality | **text-only** (verified from the tensor index — no vision/audio weights; the template's `<image>` item handling is inert on this model) |

## Measured (M5 Max, stock mlx-lm 0.31, vs bf16 source)

Two 768-token held-out texts: general/encyclopedic and agentic/code+thinking. KL is mean full-vocabulary KL(bf16 ‖ quant).

| Bundle | Size | Top-1 (gen / agentic) | Mean KL bits (gen / agentic) | Decode |
|---|---|---|---|---|
| [`LFM2.5-2.6B-MXFP8`](https://huggingface.co/OsaurusAI/LFM2.5-2.6B-MXFP8) (this) | 2.59 GiB | 91.1% / **93.4%** | **0.272** / **0.113** | 146 tok/s |
| vendor MLX mxfp8 (RTN) | 2.59 GiB | 91.7% / 92.7% | 0.303 / 0.115 | — |
| [`LFM2.5-2.6B-JANG_6M`](https://huggingface.co/OsaurusAI/LFM2.5-2.6B-JANG_6M) | **2.30 GiB** | 97.3% / 98.4% | 0.033 / 0.0033 | 156 tok/s |
| bf16 source | 5.02 GiB | 100% | 0 | 83 tok/s |

As on every model we have measured, **6-bit affine beats MXFP8 on fidelity while being smaller** — e4m3 elements carry ~3 mantissa bits, so "8-bit MX" is not strictly better than 6-bit affine with a per-group scale and bias. It shows in behaviour too: under pure greedy decoding this build thinks more verbosely than bf16 (it re-verifies its own arithmetic before answering — still correct, `</think>` closes, eos fires); with the card's default sampling (`temperature 0.1`) outputs are clean and concise. Runtime gates all pass: greedy math reasoning, card-default sampling coherence, Liquid-format tool calls, grounded 2K-token long-context answers.

## Chat / reasoning

- **Thinking is ALWAYS on.** LFM2.5-2.6B is a pure reasoning model: the chat template unconditionally opens `<think>` at the start of every assistant turn. There is **no** `enable_thinking` switch — the only template kwarg is `preserve_thinking` (default `false`: prior turns' reasoning is stripped except after the last user turn).
- The template is shipped verbatim (`chat_template.jinja`, also inlined into `tokenizer_config.json`), and `capabilities.think_in_template = true` is stamped so think-tag parsers route the pre-opened block correctly.
- **No BOS trap:** the template emits `<|startoftext|>` itself and the tokenizer never auto-adds one — both `apply_chat_template(tokenize=True)` and re-encoding the rendered string yield exactly one BOS.
- Stop token `eos_token_id = 124900` (`<|im_end|>`).
- Tool calls use the Liquid Python-call format: `<|tool_call_start|>[get_weather(city='Seoul')]<|tool_call_end|>` (verified live).
- Sampling defaults (vendor card + `generation_config.json`, mirrored in `jang_config.chat.sampling_defaults` and gate-checked against each other at build): `temperature 0.1 · top_k 50 · repetition_penalty 1.1`.

## Usage

Standard MLX safetensors with `{"group_size": 32, "bits": 8, "mode": "mxfp8"}` in `config.json[quantization]`. Loads with **stock `mlx_lm >= 0.31`** — no custom code, no `trust_remote_code`. Runs in [Osaurus](https://osaurus.ai) and vMLX-compatible runtimes (`lfm2` family).

```python
from mlx_lm import load, generate

model, tokenizer = load("OsaurusAI/LFM2.5-2.6B-MXFP8")
prompt = tokenizer.apply_chat_template(
    [{"role": "user", "content": "Which number is bigger, 9.11 or 9.8?"}],
    add_generation_prompt=True,
)
print(generate(model, tokenizer, prompt=prompt, max_tokens=1024))
```

---

Quantized and verified by **Jinho Jang** (eric@osaurus.ai). Base model © Liquid AI, released under the [LFM 1.0 license](LICENSE).
