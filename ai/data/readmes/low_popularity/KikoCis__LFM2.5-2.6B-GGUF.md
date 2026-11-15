---
license: other
license_name: lfm-open-license-v1.0
license_link: LICENSE
base_model:
  - LiquidAI/LFM2.5-2.6B
base_model_relation: quantized
library_name: llama.cpp
pipeline_tag: text-generation
tags:
  - gguf
  - quantized
  - llama-cpp
  - imatrix
  - lfm2
  - hybrid
  - edge
  - on-device
  - tool-calling
  - reasoning
  - long-context
  - multilingual
  - conversational
language:
  - ar
  - zh
  - en
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
---

![banner](banner.png)

<div style="border:2px solid currentColor; font-family:ui-monospace,'SF Mono','Cascadia Mono',Consolas,monospace;">
  <div style="border-bottom:1px solid currentColor; padding:6px 12px; font-size:11px; letter-spacing:3px; text-transform:uppercase; opacity:0.7; text-align:center;">KIKOCIS // LIQUID AI LFM2.5 QUANT LADDER // MEASURED, NOT ASSERTED</div>
  <div style="padding:14px; display:flex; flex-wrap:wrap; align-items:center; justify-content:center; gap:18px;">
<pre style="margin:0; font-size:9px; line-height:1.25;">
   LAYER STACK (30)
   ▓▓█▓▓█▓▓▓█▓▓▓█▓▓▓█▓▓▓█▓▓█▓▓█▓▓
   ▓ gated short-conv x22
   █ GQA attention   x8
   └ only 8 layers keep a KV-cache
     → 128K ctx costs ~2.1 GB
</pre>
    <div style="text-align:center;">
      <div style="font-size:23px; font-weight:800; letter-spacing:1px;">LFM2.5-2.6B-GGUF</div>
      <div style="font-size:12.5px; letter-spacing:1px; opacity:0.8; margin-top:5px;"><span style="white-space:nowrap;">6 quants</span> · <span style="white-space:nowrap;">1.367–2.875 GB</span> · <span style="white-space:nowrap;">128K ctx</span> · <span style="white-space:nowrap;">16 languages</span> · <span style="white-space:nowrap;">KLD 0.1109 @ Q4_K_M</span></div>
    </div>
  </div>
  <table style="display:table; table-layout:fixed; width:100%; margin:0; border-collapse:collapse; font-size:12px;">
    <tr>
      <td style="border-top:1px solid currentColor; border-right:1px solid currentColor; padding:8px 12px;"><div style="font-size:10px; letter-spacing:1px; opacity:0.6;">FORMAT</div><div style="font-weight:700;">GGUF · 6 quants</div></td><td style="border-top:1px solid currentColor; border-right:1px solid currentColor; padding:8px 12px;"><div style="font-size:10px; letter-spacing:1px; opacity:0.6;">SIZE</div><div style="font-weight:700;">1.367–2.875 GB</div></td><td style="border-top:1px solid currentColor; border-right:1px solid currentColor; padding:8px 12px;"><div style="font-size:10px; letter-spacing:1px; opacity:0.6;">ARCH</div><div style="font-weight:700;">lfm2 hybrid · 2.6B</div></td><td style="border-top:1px solid currentColor; padding:8px 12px;"><div style="font-size:10px; letter-spacing:1px; opacity:0.6;">CONTEXT</div><div style="font-weight:700;">131,072</div></td>
    </tr>
    <tr>
      <td style="border-top:1px solid currentColor; border-right:1px solid currentColor; padding:8px 12px;"><div style="font-size:10px; letter-spacing:1px; opacity:0.6;">IMATRIX</div><div style="font-weight:700;">16-lang · 1.04 MB</div></td><td style="border-top:1px solid currentColor; border-right:1px solid currentColor; padding:8px 12px;"><div style="font-size:10px; letter-spacing:1px; opacity:0.6;">FIDELITY</div><div style="font-weight:700;">KLD vs F16</div></td><td style="border-top:1px solid currentColor; border-right:1px solid currentColor; padding:8px 12px;"><div style="font-size:10px; letter-spacing:1px; opacity:0.6;">RUNS ON</div><div style="font-weight:700;">CPU / Metal / CUDA</div></td><td style="border-top:1px solid currentColor; padding:8px 12px;"><div style="font-size:10px; letter-spacing:1px; opacity:0.6;">LICENSE</div><div style="font-weight:700;">LFM Open v1.0</div></td>
    </tr>
  </table>
</div>

# LFM2.5-2.6B — GGUF quant ladder

**Liquid AI's** 2.6B hybrid on-device model, quantized to six GGUF tiers
(**1.367 GB → 2.875 GB**), each one measured against the F16 reference with
**KL divergence, perplexity and Top-1 token agreement** — not just shipped and hoped for.
Runs comfortably in **under 3 GB** at Q4_K_M with a 32K window.

> The model, the architecture and the training are **Liquid AI's** work
> ([LiquidAI/LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B)).
> This repo contributes the quant ladder, the fidelity measurements and the packaging.
> No weights were retrained, pruned, merged or otherwise altered — 266 tensors in, 266 out.

### Why another GGUF of this model?
LiquidAI publish [their own GGUF](https://huggingface.co/LiquidAI/LFM2.5-2.6B-GGUF), and
so do others — they are good, and if you just want a file, use any of them. What this repo
adds is **the measurement layer**: an imatrix calibrated on all 16 languages the model
actually speaks, the **complete** ladder from Q3_K_M to Q8_0, a KLD/PPL/Top-1 sweep of
**every** tier against the F16 reference (with the F16-vs-itself control included so you
can see the noise floor), charts, a deterministic 60-item capability probe run on every
tier, the exact scripts, and SHA-256 for every artifact. So you can pick a quant on
evidence instead of folklore.

## ✅ Recommended files
| Use case | File | Why |
|---|---|---|
| **Safe default** | `LFM2.5-2.6B-Q4_K_M.gguf` | 1.674 GB, KLD 0.111, keeps 57/60 on the capability probe (F16 itself scores 59/60). |
| Tightest RAM | `LFM2.5-2.6B-Q3_K_M.gguf` | 1.367 GB. Cheapest to run; highest measured drift. |
| Best compact I-quant | `LFM2.5-2.6B-IQ4_XS.gguf` | 1.518 GB — 156 MB under Q4_K_M, fastest generation here. |
| Closest to the original | `LFM2.5-2.6B-Q6_K.gguf` | KLD 0.0108, Top-1 95.1% — near-lossless at 2.222 GB. |
| Archival / reference-grade | `LFM2.5-2.6B-Q8_0.gguf` | KLD 0.0013. Practically indistinguishable from F16. |

## 📦 Files (the full ladder)
| Quant | Bits/weight | File size | Notes |
|---|---:|---:|---|
| `LFM2.5-2.6B-Q3_K_M.gguf` | ~4.0 | 1.367 GB (1.273 GiB) | Smallest included. Real quality cost — see the KLD column. |
| `LFM2.5-2.6B-IQ4_XS.gguf` | ~4.5 | 1.518 GB (1.414 GiB) | Compact I-quant (needs the imatrix, which ships here). |
| `LFM2.5-2.6B-Q4_K_M.gguf` | ~4.9 | 1.674 GB (1.559 GiB) | Standard K-quant. The one most people should start with. |
| `LFM2.5-2.6B-Q5_K_M.gguf` | ~5.7 | 1.94 GB (1.807 GiB) | Noticeably closer to F16 for +0.27 GB over Q4_K_M. |
| `LFM2.5-2.6B-Q6_K.gguf` | ~6.6 | 2.222 GB (2.069 GiB) | Near-lossless: KLD 0.011, Top-1 95%. |
| `LFM2.5-2.6B-Q8_0.gguf` | 8.5 | 2.875 GB (2.677 GiB) | Effectively the reference: KLD 0.0013, Top-1 98.2%. |

<sub>K-quants (`Q*_K`) are the general-purpose quants. I-quants (`IQ*`) pack more quality
into fewer bytes but need an importance matrix — `LFM2.5-2.6B.imatrix` ships here so you can
re-roll any tier yourself. More bits = closer to the original = bigger.</sub>

## 📊 Metrics — objective fidelity vs the F16 reference
**KLD** (KL divergence, nats) is how far a quant's output *distribution* drifts from the
full-precision model — the metric that catches damage perplexity misses. **Top-1 match** is
how often the quant picks the same next token as F16. **RMS Δp** is the typical probability
shift per token.

| Model | Size GB | Prompt tok/s | Gen tok/s | PPL | PPL Δ | KLD mean | KLD p95 | RMS Δp | Top-1 match vs F16 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **F16 reference** | 5.403 | 1942 | 34.8 | 45.974 | +0.000 | 0.000000 | 0.00002 | 0.001% | 99.99% (8332/8333) |
| `Q8_0` | 2.875 | 1731 | 49.6 | 45.676 | -0.298 | 0.001348 | 0.00396 | 0.837% | 98.23% (7991/8135) |
| `Q6_K` | 2.222 | 1616 | 60.0 | 45.396 | -0.579 | 0.010835 | 0.03476 | 2.342% | 95.07% (7731/8132) |
| `Q5_K_M` | 1.94 | 1538 | 84.3 | 43.768 | -2.206 | 0.031740 | 0.10468 | 3.951% | 91.41% (7471/8173) |
| `Q4_K_M` | 1.674 | 1700 | 96.2 | 40.096 | -5.878 | 0.110869 | 0.39431 | 7.440% | 84.36% (6887/8164) |
| `IQ4_XS` | 1.518 | 1739 | 101.0 | 47.081 | +1.107 | 0.143438 | 0.50511 | 8.667% | 81.81% (6677/8161) |
| `Q3_K_M` | 1.367 | 1552 | 87.7 | 41.069 | -4.906 | 0.316972 | 1.11038 | 12.515% | 74.73% (6100/8163) |

<sub>Measured with `llama-perplexity --kl-divergence` against `LFM2.5-2.6B-F16.gguf` over
~8.2K tokens of wikitext-2 test (ctx 512, 32 chunks; exact per-quant counts in the CSV);
PPL over ctx 2048 × 64 chunks; throughput from `llama-bench`
(pp512 / tg128, Metal). The **F16 row is the control** — F16 scored against its own logits.
It comes back at KLD 0.000000 and Top-1 99.99%, which is the measurement noise floor, not a
result. Raw per-quant JSON in [`reports/`](reports), machine-readable summary in
[`metrics/quant-summary-with-kld.json`](metrics/quant-summary-with-kld.json) + `.csv`.</sub>

### ⚠️ Read the PPL column with care (an honest oddity)
For this model, **perplexity on raw wikitext is not monotone in quant size** — Q4_K_M and
Q3_K_M score *lower* (apparently "better") PPL than F16, while IQ4_XS scores higher. That is
not an error: it reproduces on two independent evaluation windows, and the F16-vs-F16 control
is exactly zero. The likely reason is that this is a heavily post-trained reasoning model, so
raw encyclopedia text is far out of its distribution; quantization noise flattens its very
peaked output distribution, which can *lower* perplexity while moving the model *further* from
the original. **KLD, RMS Δp and Top-1 agreement are all cleanly monotone** and are the columns
to trust. We are reporting PPL because we measured it, not because it should drive your choice.

### 📈 Charts
![quality vs size](metrics/chart-quality-vs-size.png)
![kld mean](metrics/chart-kld-mean.png)
![top-1 match](metrics/chart-top1-match.png)
![ppl delta](metrics/chart-ppl-delta.png)
![throughput](metrics/chart-throughput.png)

## 🧮 Will it fit?
Total memory ≈ weights + KV-cache. This model is a hybrid: **only 8 of its 30 layers are
attention layers**, so the KV-cache is unusually small — roughly **16 KB per token**
(f16), i.e. ~0.13 GB at 8K, ~0.54 GB at 32K, ~2.15 GB at 128K. Halve those with
`--cache-type-k q8_0 --cache-type-v q8_0`.

| You have | Comfortable quant | Context |
|---|---|---|
| 3 GB | `Q3_K_M` / `IQ4_XS` | 8K–32K |
| 4 GB | `Q4_K_M` | 32K–64K |
| 6 GB | `Q5_K_M` / `Q6_K` | 128K (full native) |
| 8 GB+ | `Q8_0` | 128K (full native), room to spare |

## 🧠 Context size
Native **131,072** tokens. Ready-made Modelfiles at 8K / 32K / 128K in
[`modelfiles/`](modelfiles); the full guide is in [`CONTEXT.md`](CONTEXT.md).

## 🚀 How to run it
```bash
# Ollama
ollama run hf.co/KikoCis/LFM2.5-2.6B-GGUF:Q4_K_M

# llama.cpp — --jinja is important: it uses the chat template embedded in the GGUF,
# which is what gives you the reasoning channel and the tool-call syntax
llama-server -m LFM2.5-2.6B-Q4_K_M.gguf -c 32768 --jinja

# full 128K window with a quantized KV-cache
llama-server -m LFM2.5-2.6B-Q4_K_M.gguf -c 131072 --jinja \
  --cache-type-k q8_0 --cache-type-v q8_0
```

**Sampling** (Liquid AI's recommendation, and what every number above was measured with):
`temperature 0.1`, `top_k 50`, `repetition_penalty 1.1`.

**Tool calling**: LFM2.5 emits *Pythonic* calls between `<|tool_call_start|>` and
`<|tool_call_end|>`, e.g. `<|tool_call_start|>[get_weather(city="Barcelona")]<|tool_call_end|>`.
**Good news for agent frameworks**: recent llama.cpp parses that into standard
`tool_calls`, so with `llama-server --jinja` you can just send the ordinary OpenAI-style
`tools` parameter — measured 6/6 at both Q8_0 and Q4_K_M, no adapter and no text-injection
workaround (see *Agent-harness compatibility* below). Passing the tool list as JSON in the
system prompt (`List of tools: [...]`), the format Liquid AI
[document](https://docs.liquid.ai/lfm/key-concepts/tool-use), works equally well.

**Reasoning**: this is a *pure reasoning* model — the chat template always opens a `<think>`
channel. Budget your `max_tokens` accordingly: see the finding below.

## ⚠️ Good to know
- **Give it room to think.** At `max_tokens=900` the lower quants sometimes spend the entire
  budget inside the `<think>` channel and return an empty final answer. At `max_tokens=2600`
  the same prompts answer correctly. If you get blank replies, raise the token budget before
  blaming the quant.
- **Q3_K_M is a real step down**, not a free lunch: 12.5% RMS probability
  shift and Top-1 agreement down to 75%. It still works; it is measurably
  further from the original than everything above it.
- **What it is for** (per Liquid AI): agentic tool use, data extraction, RAG, long-context
  work. **What it is not for**: agentic *coding* and knowledge-heavy tasks. Upstream says so
  explicitly and our own pre-screen agrees — **0/6 on SWE-bench Verified instances**, even at
  Q8_0. Details below; use a coding model for coding.
- Generation throughput here peaks in the middle of the ladder, not at the bottom — a 2.6B
  model is not purely memory-bound, so `Q3_K_M` is *not* automatically the fastest.

## 📊 Evaluation methodology
Four things were measured. Each is stated exactly, including what it does **not** cover.

### 1. Quantization fidelity (the main event)
- **Reference**: `LFM2.5-2.6B-F16.gguf`, the unquantized f16 conversion of the upstream
  bf16 weights. Every quant in the ladder is cut from that same file.
- **KLD + Top-1 + RMS Δp**: `llama-perplexity --kl-divergence` over **~8.2K tokens**
  of wikitext-2 test, ctx 512, 32 chunks.
- **PPL**: `llama-perplexity` over wikitext-2 test, ctx 2048, 64 chunks.
- **Throughput**: `llama-bench -p 512 -n 128 -r 3`, Metal backend.
- **Control**: F16 measured against its own logits, reported in the table. Anything at or
  below KLD ≈ 2e-5 / Top-1 ≈ 99.99% is noise, not signal.

### 2. Capability probe — `edge-probe-v1` (60 items, no LLM judge)
A size-appropriate probe, **run identically on every tier**, so the column-to-column
differences measure *quantization damage* rather than model choice. Every item is scored by a
deterministic Python predicate — string/JSON/regex/script checks. There is no model grading
another model anywhere in this eval. Spec: [`edge_probe.json`](edge_probe.json);
per-item results: [`reports/edge-probe-*.json`](reports).

- **Tool calls (24)** — the emitted function name *and* the required argument must both be
  right, parsed out of the model's own `<|tool_call_start|>` block.
- **Instruction following (20)** — verifiable constraints: exact JSON key sets, word/line/
  sentence counts, forced prefixes and suffixes, casing, forbidden letters, exact arithmetic.
- **Multilingual (16)** — one question per language the model claims; the reply must actually
  be *in* that language (Unicode-script test for non-Latin scripts, `langdetect` for Latin
  ones). Scored at `max_tokens=2600` so the number measures language fidelity and not the
  reasoning-budget effect described above.

| Quant | Tool calls | Instruction following | Multilingual (16 langs) | Total |
|---|---:|---:|---:|---:|
| **F16 reference** | 23/24 | 20/20 | 16/16 | **59/60** (98%) |
| `Q8_0` | 23/24 | 19/20 | 16/16 | **58/60** (97%) |
| `Q6_K` | 22/24 | 20/20 | 16/16 | **58/60** (97%) |
| `Q5_K_M` | 23/24 | 20/20 | 16/16 | **59/60** (98%) |
| `Q4_K_M` | 22/24 | 19/20 | 16/16 | **57/60** (95%) |
| `IQ4_XS` | 22/24 | 20/20 | 16/16 | **58/60** (97%) |
| `Q3_K_M` | 22/24 | 19/20 | 16/16 | **57/60** (95%) |

<sub>The F16 row is the probe's ceiling, not a perfect score — one tool-call item is
ambiguous enough that even F16 misses it. Read the ladder relative to that row. Sampling:
temperature 0.1, top_k 50, repetition_penalty 1.1, seed 7, served with
`llama-server --jinja`. Date: 2026-08-06.</sub>


### 3. Agent-harness compatibility
Before claiming anything about agentic use, we checked the boring thing that usually
breaks first: does a normal harness actually *receive* a tool call? Both paths were
tested per quant — the OpenAI-style `tools` parameter (which is what agent frameworks
send) and tools-as-JSON-in-the-system-prompt (the format Liquid AI document).

| Quant | Returned structured `tool_calls` | Correct function | Correct via system-prompt format |
|---|---:|---:|---:|
| `Q8_0` | 6/6 | 6/6 | 6/6 |
| `Q4_K_M` | 6/6 | 6/6 | 6/6 |

<sub>Served with `llama-server --jinja`. llama.cpp parses LFM2.5's Pythonic
`<|tool_call_start|>` output into standard `tool_calls`, so the model is drop-in for
OpenAI-compatible agent harnesses — no adapter, no text-injection workaround. Detail in
[`reports/agent-harness-check.json`](reports/agent-harness-check.json).</sub>

### 4. Agentic coding pre-screen — the negative result, reported anyway
**0/6 resolved.** Liquid AI say this model is *not* intended for agentic coding, so we ran a short pre-screen rather than a long benchmark — and we are publishing the zero, because a card that only shows favourable numbers is not a data sheet.

| Instance | Resolved | Tool calls issued | Agent minutes |
|---|---|---:|---:|
| `django__django-11133` | no | 20 | 10.2 |
| `django__django-11099` | no | 4 | 1.7 |
| `django__django-13590` | no | 23 | 1.6 |
| `django__django-13933` | no | 32 | 20.6 |
| `django__django-14608` | no | 14 | 8.1 |
| `django__django-14752` | no | 2 | 0.7 |

<sub>SWE-bench Verified instances (the first 6 continuity anchors of our `swe-mix` probe), run through terminal-bench with a Claude-Code-style harness. Quant tested: **Q8_0** — deliberately the highest-fidelity tier, so a failure cannot be blamed on quantization. temp 0.1, ctx 32K, 60-turn cap.

**The failure is capability, not plumbing**: across the six runs the model issued **95 real tool calls**, never crashed and never fell into a repetition loop — it simply did not land a passing patch. Full per-instance detail in [`reports/swe-prescreen.json`](reports/swe-prescreen.json). Small, hard probe; NOT comparable to the official SWE-bench leaderboard.</sub>

### What was NOT measured — and why
Being explicit about this matters more than a bigger number would.

- **No full agentic-coding benchmark.** What ran was a **6-instance pre-screen**, not the
  300-instance SWE-bench Verified suite. It is enough to say "do not use this for coding
  agents"; it is not enough to rank this model against others on coding. **Do not read any
  coding-agent capability into this card.**
- **No knowledge benchmarks** (MMLU and friends). Same reason: upstream flags knowledge-heavy
  tasks as out of scope, and this repo is about what *quantization* costs, not about
  re-benchmarking Liquid AI's model.
- **No long-context retrieval eval.** The 128K window is inherited from upstream and untested
  here; the KV-cache figures above are arithmetic, not measurements.
- The capability probe is a **60-item local probe**, useful for ranking these seven files
  against each other. It is **not** a public leaderboard result and should not be compared to
  one.

## 🔁 Provenance & reproducibility
Everything needed to re-derive or verify these files is in the repo.

| What | Where |
|---|---|
| Corpus builder for the imatrix | [`scripts/00_build_imatrix_corpus.py`](scripts/00_build_imatrix_corpus.py) |
| Download → F16 → imatrix | [`scripts/01_convert_and_imatrix.sh`](scripts/01_convert_and_imatrix.sh) |
| The quant ladder (+ magic check on every file) | [`scripts/02_quantize_ladder.sh`](scripts/02_quantize_ladder.sh) |
| KLD / PPL / Top-1 / throughput sweep | [`scripts/03_quality_sweep.py`](scripts/03_quality_sweep.py) |
| Charts | [`scripts/04_charts.py`](scripts/04_charts.py) |
| Capability probe | [`scripts/05_edge_probe.py`](scripts/05_edge_probe.py), [`scripts/06_multilingual_budget.py`](scripts/06_multilingual_budget.py) |
| Agent-harness compatibility check | [`scripts/08_agent_harness_check.py`](scripts/08_agent_harness_check.py) |
| This card (generated from the metrics, not typed) | [`scripts/07_make_card.py`](scripts/07_make_card.py) |
| Importance matrix | `LFM2.5-2.6B.imatrix` |
| The exact calibration text | [`imatrix-calibration-corpus.txt`](imatrix-calibration-corpus.txt) |
| Serving / sampling profiles | [`configs/`](configs) |
| SHA-256 of every artifact | [`reports/artifact-sha256sums.txt`](reports/artifact-sha256sums.txt) |

- **Source**: `LiquidAI/LFM2.5-2.6B`, downloaded 2026-08-05. Conversion with
  `llama.cpp/convert_hf_to_gguf.py` (arch `Lfm2ForCausalLM` → `lfm2`), then
  `llama-quantize --imatrix`. Every output was verified with `llama-gguf <file> r`:
  266 tensors, GGUF v3, valid magic on all six.
- **imatrix corpus** (~1.04 MB) is public-dataset text, shaped like the model: a balanced
  16-language block (XNLI + language-identification + OPUS-100) covering every language the
  model claims, plus tool-call traffic, source code, general and literary prose, and turns
  written in the model's own chat template including `<|tool_call_start|>` blocks. The
  wikitext **test** split was deliberately kept out of the calibration — it is the PPL eval
  set. Computed over 512 chunks at ctx 512, no NaNs.
- Verify your download: `shasum -a 256 -c reports/artifact-sha256sums.txt`.

## 📚 Credit & license
Model, architecture, weights and training: **© Liquid AI, Inc.** —
[LiquidAI/LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B).
Quant ladder, imatrix calibration, KLD/PPL/Top-1 measurements, charts, probe and packaging:
KikoCis, 2026-08-06.

Released under the **LFM Open License v1.0** — the same licence as the original weights. A
full copy is in [`LICENSE`](LICENSE) and the modifications made here are itemised in
[`NOTICE`](NOTICE), as the licence requires.

> **⚠️ Commercial-use limit (LFM Open License v1.0, §5).** Commercial use is permitted only
> for legal entities with **annual revenue below 10,000,000 USD**. At or above that threshold
> you need a separate commercial licence from Liquid AI. This applies to these quantized files
> exactly as it applies to the original weights. Non-commercial and research use is not
> subject to the threshold. This note is a pointer, not legal advice — read `LICENSE`.

## 🗒️ Changelog
- **2026-08-06** — v1: full ladder (Q3_K_M · IQ4_XS · Q4_K_M · Q5_K_M · Q6_K · Q8_0), imatrix,
  KLD/PPL/Top-1 sweep + charts, `edge-probe-v1` on every tier, Modelfiles, checksums.
