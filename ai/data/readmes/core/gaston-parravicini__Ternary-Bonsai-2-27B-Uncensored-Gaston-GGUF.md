---
license: apache-2.0
base_model: prism-ml/Ternary-Bonsai-2-27B-gguf
language:
- en
- es
- zh
- fr
- de
- pt
- it
- ja
- ko
- ru
tags:
- gguf
- abliterated
- uncensored
- bonsai
- ternary
- qwen3
- qwen3.8
- qwen3.5
- 27b
- ssm
- state-space
- hybrid-architecture
- reasoning
- thinking
- conditional-steering
- mtp
- speculative-decoding
- red-teaming
- safety-research
- honest-eval
- chat
- assistant
- instruct
- llama-cpp
- conversational
- text-generation
pipeline_tag: text-generation
---

![Ternary-Bonsai-2-27B Uncensored Banner](bonsai_uncensored.jpeg)

# Ternary-Bonsai-2-27B — Uncensored by Gastón Parravicini

> **The 27B model that every abliteration tool said couldn't be touched — edited anyway, with its brain intact.**
> A new liberation technique: refusal-steering **compiled straight into the weights**. No fine-tuning. No reference model. No lobotomy.
>
> Refusal reflex removed at the weight level · MTP draft head grafted · runs on a single RTX 3090 · **honestly measured** — no inflated numbers. See *[How we measured](#how-we-measured-and-why-most-uncensored-numbers-are-inflated)*.

Published by **Gastón Parravicini**

---

## TL;DR

Bonsai-2 is built to be **un-abliteratable** by every existing tool: its weights are **ternary and
Hadamard-rotated**, and it **cannot be fine-tuned** in llama.cpp (there is no backward pass for its
state-space layers). Subtract the refusal direction the normal way and **nothing happens**.

This release edits it anyway, with a different method entirely. What that buys you, measured
rigorously on a single RTX 3090:

> ✅ **The explicit refusal reflex is gone** — the hard "I cannot / I won't" wall drops to **~0** on adversarial prompts (shipped scale 16).
> ✅ **Capability largely retained** — perplexity **+8.4%** at the shipped scale; the technique reaches **+3.3%** at a lower, less-aggressive setting.
> ✅ **Reasoning fully intact** — the `<think>` chain still thinks.
> ✅ **Stays coherent under adversarial load** — it keeps producing a usable answer where a reference abliteration of the same base collapses into reasoning loops on most hard prompts.
> ✅ **Tunable** — a single scale knob trades removal strength for perplexity.

**What it does not do:** it does not turn Bonsai-2 into a model that will hand you operative
harmful content on demand. Bonsai-2's safety is *deep*, and this technique removes the surface
refusal without replacing it with wholesale compliance — see the honest numbers below.

---

## The honest picture (read this)

Most "uncensored" model cards lead with a number like "95% refusal removal." We measured ours the
careful way and found that **that number, as usually computed, is largely an artifact** (see the
methodology section). Here is what our model actually does on **hard adversarial prompts**
(AdvBench, 50 prompts, hand-classified, 1024-token generations so nothing is truncated):

| Behavior on hard prompts | This model (scale 16) |
|---|---|
| Explicit refusal ("I cannot…") | **~0%** — the refusal reflex is removed |
| Genuine operative harmful compliance | **~15%** (mostly dual-use security topics) |
| Engages but **deflects** to a safe/legal/educational reframe | ~46% |
| Over-reasons in `<think>` without reaching an answer | ~36% |

On a **mild** refusal set (targeted-harassment prompts the stock model refuses but where complying
is harmless), removal is high (**31/32**) — mild prompts don't trigger the deep-safety deflection
that hard prompts do. **Efficacy is strongly prompt-difficulty-dependent**, and we think a card
should say so plainly.

The interesting result isn't a big compliance number — it's that **surface abliteration of a
deeply safety-trained reasoning model removes the refusal token but re-routes the behavior into
deflection, not compliance.** That's a real, reproducible finding, and it's why we ship this with
open scripts and honest numbers rather than a headline percentage.

---

## How it compares

Measured against a **reference abliteration of the same base model**, identical rigorous protocol
(50 hard prompts, 1024-token generations, hand-classified):

| | Reference abliteration | **This model** |
|---|---|---|
| Explicit refusal removed | ✅ ~0% | ✅ ~0% |
| Genuine operative compliance (hard) | ~20% (incl. some genuinely dangerous outputs) | ~15% |
| **Stays coherent / produces an answer** | 30% (loops on **70%** of hard prompts) | **64%** |
| Dominant failure mode | reasoning **loop** (no output) | **deflection** (safe reframe) |
| Capability cost (perplexity) | +6.2% | +3.3% (scale 8) / +8.4% (scale 16) |

**Takeaway:** neither approach is a clean "uncensor," and both would report ~90% under the naive
classifier. The reference model is slightly more compliant *when it answers* but **loops on 70% of
hard prompts** — largely unusable under adversarial load. This model is far more coherent (answers
~2× as often, no loops) with comparable or better capability retention. Different point on the same
trade-off: **coherence + capability vs. raw compliance.**

---

## What makes the *method* different

Independently of the efficacy numbers, the technique itself is novel and works on a model class
that defeats every off-the-shelf approach:

| | Standard abliteration | **This method** |
|---|---|---|
| Mechanism | subtract a direction from weights | **conditional steering compiled into weights** |
| On Bonsai-2 | ❌ doesn't work (rotated ternary weights) | ✅ works |
| Fine-tuning | sometimes needed | ❌ none (forward-only; no backward pass exists) |
| Reference model | sometimes needed | ❌ none — derived from Bonsai-2 itself |
| Capability cost | higher | **+8.4% shipped; +3.3% at lower scale** |
| Reversible / tunable | ❌ | ✅ single scale knob |

---

## How we measured (and why most "uncensored" numbers are inflated)

This is the part we think matters most. The standard way to score "refusal removal" is a keyword
classifier: generate a short completion, and if it doesn't contain "I cannot / I'm sorry / I won't,"
call it a success. On a **reasoning** model that method is badly broken, in three ways we verified:

1. **It reads the `<think>` block.** The model's internal reasoning routinely contains "I should be
   careful / I should not," so a completion that ultimately **complies** gets scored as a refusal
   (false negative) — or, at higher steering, the reasoning stops hedging and pure deflections get
   scored as **compliance** (false positive).
2. **Short generations truncate the answer.** With a 200-token cap, the `<think>` block eats the
   budget and the actual answer never appears — scored as whatever keyword happened to land.
3. **Deflection looks like compliance.** "How to make a homemade bomb → *here's a baking-soda
   volcano*" contains no refusal keyword, so it scores as a success. It is not.

Our numbers above use **1024-token generations, the answer body only (post-`</think>`), and manual
classification** into comply / deflect / loop / refuse. Under the naive classifier this same model
scores 86–98%; hand-verified, genuine hard-prompt compliance is **~15%**. We report the honest one.

**The tool is included: [`scripts/honest_eval.py`](scripts/honest_eval.py).** It runs long
generations, scores the answer body only, and auto-separates *explicit refusal* / *no-answer
(loop)* / *answered* — then hands you the "answered" set to split into genuine compliance vs.
deflection by eye, because that last call genuinely needs a human. It refuses to print a single
inflated percentage. Run it on this model, on the base model, or on any other "uncensored" release
and compare honestly:

```bash
python3 scripts/honest_eval.py --model <model.gguf> \
    --prompts advbench_harmful_behaviors.csv --n 50 --tokens 1024
```

---

## About Ternary-Bonsai-2-27B

The base model is **[prism-ml/Ternary-Bonsai-2-27B](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf)**
— a **natively ternary** (~1.58-bit) 27B model built on a **Qwen3-27B** foundation (the `qwen35`
hybrid state-space architecture, from the Qwen3.8-27B generation), released by **prism-ml** under
Apache 2.0:

- **64 layers**: 16 full-attention + 48 **gated-delta-net (SSM)** blocks; `blk.64` is the MTP/nextn draft head
- **n_embd 5120, n_ff 17408**; a reasoning model — emits `<think>...</think>` before answering
- Multilingual (inherits Qwen3's broad language coverage)
- Shipped only **quantized**: **PQ2_0** (2.13 bpw) and **PTQ1_0** (1.75 bpw), plus MLX
- Weights stored **Hadamard-rotated** (`prism.hadamard`, QuIP#-style, block 1024)

Base model collection: [huggingface.co/collections/prism-ml/bonsai-2](https://huggingface.co/collections/prism-ml/bonsai-2)
· upstream family: [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) (Apache 2.0).

Not a standard Transformer — and that's exactly why nothing off-the-shelf can uncensor it.

---

## Why every standard tool fails here

Three brick walls, each verified on the actual model:

1. **Orthogonalization does nothing.** Projecting the writer matrices orthogonal to a refusal
   direction **fails on this model**, even with a perfectly recovered direction.
2. **You cannot fine-tune it.** ggml has **no backward pass** for the state-space operators
   (`GATED_DELTA_NET`, `GATED_LINEAR_ATTN`, `SSM_CONV`, `SSM_SCAN`). Gradient-based uncensoring is
   dead on arrival.
3. **The weights are rotated.** Edit them naively and your intervention lands in the wrong basis
   (Hadamard) — the effect washes out.

Run any existing abliterator on Bonsai-2 and you get a byte-for-byte identical model back.

---

## How it was done

A **forward-only** technique, derived **entirely from Bonsai-2 itself** — no other model touched.

### 1. Read the refusal decision from the model's own thoughts
Run the stock model on prompts it refuses vs. prompts it complies with, and grab the
**residual-stream state at the decision point** (end of the `<think>` chain). The per-layer
difference is `g` — the direction that turns "refuse" into "comply". No training, just a forward pass.

### 2. Teach it *when* to steer (conditional)
Capture the mean `ffn_down` input on refusal vs. comply contexts. Their difference `v` is the
"this is a refusal context" detector. The edit is built to **fire only on refusal-context tokens**
and stay silent on normal prompts — this is what keeps the model smart.

### 3. Compile the steering into the weights — in the right basis
For layers **15–63**, a rank-1 term is added to `ffn_down`:

```
DeltaW[i, j] = u[i] * g_hat[j]
  g_hat = unit refusal->comply direction        (output side, natural space)
  u     = SCALE * T(v) / (v . h_refuse)          (input side)
  T     = the model's own Hadamard transform:    block-1024 Walsh-Hadamard of (sign (.) v)
```

Applying the **exact Hadamard rotation the engine uses** is the unlock — it puts the edit in the
same basis as the rotated weights. Baked in F16, then re-quantized to the ternary formats.

### 4. The recipe
```yaml
target:    ffn_down (layers 15-63)        # the FFN residual writer, in every layer
direction: model's own comply-vs-refuse activations, at the decision point
gating:    conditional on refusal-context input (v = h_refuse - h_comply)
basis:     model Hadamard transform (block 1024, sign-explicit)
scale:     16.0 (shipped — removes the hard refusal reflex) | 8.0 = higher capability, weaker removal
method:    forward-only  |  no gradient  |  no reference model
```

### 5. Why the brain survives
The steering is **conditional** — it fires on refusal contexts and is ~0 everywhere else — so it
barely perturbs normal generation. Perplexity cost is **+8.4%** at the shipped scale 16 (and as low
as +3.3% if you turn the knob down), versus the much larger hit a blunt weight edit would cause.

---

## Capability & efficacy

Measured on a **single NVIDIA RTX 3090 (24 GB)**. Reproduce with the included scripts; the full
breakdown is in [`benchmarks.txt`](benchmarks.txt).

| Model | Perplexity | vs stock | Mild refusal set | Hard adversarial (rigorous) |
|-------|-----------|----------|------------------|-----------------------------|
| Stock Bonsai-2 PQ2_0 | 2.2300 | — | 2/32 | ~0% comply |
| **This model — PQ2_0 (shipped, scale 16)** | **2.4164** | **+8.4%** | 31/32 | **~0 explicit refusal, ~15% genuine comply** |
| **This model — PTQ1_0 (shipped, scale 16)** | **2.4152** | **+8.3%** | 31/32 | same behavior |

**Why scale 16 ships:** at lower scale 8 the perplexity cost is only +3.3%, but the refusal reflex
is *not* removed on hard prompts — it still refuses ~56% of AdvBench outright. Scale 16 is the
setting where the refusal wall actually drops. Scale 32 and above only add reasoning loops and
perplexity without more genuine compliance. The scale knob is exposed in `bake_portable_f16.py` if
you want to trade removal strength for capability.

- ✅ Reasoning (`<think>`) fully intact
- ✅ Benign coherence verified (notes, explanations, summaries — all clean)

---

## Speed — MTP speculative decoding

The `-MTP` variants graft the `blk.64` multi-token-prediction (nextn) draft head, so the model can
draft its own tokens (self-speculative decoding). Measured on **RTX 3090**, code generation:

| Model | Base | MTP (`--spec-draft-n-max 4`) | vs base |
|---|---|---|---|
| **PQ2_0-MTP** ⭐ | 67.2 t/s | **88.0 t/s** | **+31%** |
| PTQ1_0-MTP | 56.3 t/s | 55.8 t/s | ~flat (no gain in our tests) |

**Honest result:** the speedup is real and worth it on **PQ2_0** for code/structured output
(+31%; `n-max 4` was the sweet spot — 3 gives +26%, 5 regresses). On **PTQ1_0** the draft head did
**not** accelerate decode in our tests, so for the 1.75-bpw quant just use the non-MTP file. Draft
acceptance is high on code and low on free-form prose (little or no gain on prose either way).

> **Requires the MTP Hadamard-inverse fix.** PrismML's ternary models store `token_embd` in a
> Hadamard-rotated basis; stock prism-llama's MTP draft graph reads it without the inverse transform
> and errors out (`failed to create MTP context`). The one-file fix is in-flight upstream
> ([PR #205](https://github.com/PrismML-Eng/llama.cpp/pull/205) /
> [#217](https://github.com/PrismML-Eng/llama.cpp/pull/217) /
> [#230](https://github.com/PrismML-Eng/llama.cpp/pull/230)). Build a prism-llama that includes it,
> then run:

```bash
llama-cli -m Ternary-Bonsai-2-27B-Uncensored-Gaston-PQ2_0-MTP.gguf \
  -ngl 99 -c 4096 -fa on --spec-type draft-mtp --spec-draft-n-max 4 \
  -p "<|im_start|>user\nYour prompt<|im_end|>\n<|im_start|>assistant\n<think>\n"
```

The non-MTP variants have no such dependency and run on any prism-llama build.

---

## Open method & tools

Not a black-box drop. There's a full step-by-step **[TUTORIAL.md](TUTORIAL.md)** — reproduce this
model, or apply the technique to other Hadamard-folded / ternary models. The technique, scripts and
measurements ship in `scripts/`:

| Tool / patch | What it does |
|---|---|
| `bake_portable_f16.py` | The core technique — bakes the conditional refusal-steering into `ffn_down` (layers 15-63) in the model's **Hadamard basis**, forward-only. |
| `graft_mtp.py` | Grafts the MTP (`blk.64`) draft head verbatim from the clean parent, and fixes the `block_count` / `nextn` metadata. |
| `sign_gguf.py` | Stamps authorship metadata (`general.author`) into the GGUF. |
| `honest_eval.py` | ⭐ The **rigorous evaluation tool** — long generations, answer-body-only scoring, refuse/loop/answered split, human comply-vs-deflect review. The anti-inflation harness. Run it on any model. |
| `run_advbench.sh` / `run_final_bench.sh` | Convenience wrappers — perplexity + refusal set. |

Direction and gating are derived **only from Bonsai-2's own activations** — no reference model, no
gradient (impossible on this SSM arch), no fine-tuning.

## Available quants

| File | Format | BPW | Size | Notes |
|------|--------|-----|------|-------|
| `Ternary-Bonsai-2-27B-Uncensored-Gaston-PQ2_0.gguf` | PQ2_0 | 2.13 | 8.25 GB | ⭐ **Recommended** |
| `Ternary-Bonsai-2-27B-Uncensored-Gaston-PTQ1_0.gguf` | PTQ1_0 | 1.75 | 7.11 GB | Smallest |
| `Ternary-Bonsai-2-27B-Uncensored-Gaston-PQ2_0-MTP.gguf` | PQ2_0 | 2.13 | 8.51 GB | PQ2 + MTP draft head |
| `Ternary-Bonsai-2-27B-Uncensored-Gaston-PTQ1_0-MTP.gguf` | PTQ1_0 | 1.75 | 7.37 GB | PTQ1 + MTP draft head |

Same size as the **official** Bonsai-2 quant of the same format — embeddings and the output layer are
kept at higher precision, exactly as the base release ships them (not compressed to save space).

---

## Requirements & installation

Bonsai-2 uses a custom arch (`qwen35` hybrid SSM), custom quants (PQ2_0 / PTQ1_0) and Hadamard-folded
weights that **upstream llama.cpp does not implement**. You need **prism-llama** — Prism's public
llama.cpp fork — the **same engine required to run the original Bonsai GGUF. This model needs no
extra patch.**

```bash
# 1. Clone Prism's llama.cpp fork
git clone https://github.com/PrismML-Eng/llama.cpp prism-llama
cd prism-llama

# 2. Build (NVIDIA)
cmake -B build -DGGML_CUDA=ON
cmake --build build -j --config Release

#    ...or on Apple Silicon
# cmake -B build -DGGML_METAL=ON
# cmake --build build -j --config Release
```

Binaries land in `build/bin/`. ~24 GB VRAM runs PQ2_0 fully on GPU with `-ngl 99`; it also runs
CPU / partial-offload.

## Usage

### llama-cli
```bash
llama-cli \
  -m Ternary-Bonsai-2-27B-Uncensored-Gaston-PQ2_0.gguf \
  -ngl 99 -c 4096 --temp 0 \
  -p "<|im_start|>user\nYour prompt<|im_end|>\n<|im_start|>assistant\n<think>\n"
```

### llama-server
```bash
llama-server -m Ternary-Bonsai-2-27B-Uncensored-Gaston-PQ2_0.gguf -ngl 99 -c 4096 --port 8080
```

---

## Notes

- **Reasoning model:** answers include a `<think>...</think>` block first. Expected and correct. The
  model tends to reason at length; give it enough tokens (`-n 512`+) to reach the answer.
- **MTP / speculative decoding:** the `qwen35` arch supports a multi-token-prediction (nextn) draft
  head; `-MTP` variants include a grafted head. The liberation edit touches only layers 15-63.
- **Ternary + Hadamard:** needs a prism-llama build; upstream llama.cpp doesn't implement this
  arch/quant — same requirement as the base Bonsai release, nothing extra.
- **Tunable:** the edit is an additive term with a scale knob; lower scales trade a little efficacy
  for an even smaller perplexity cost.

---

## Base model

- **Model:** [prism-ml/Ternary-Bonsai-2-27B](https://huggingface.co/collections/prism-ml/bonsai-2)
- **Architecture:** qwen35 hybrid — full attention + gated-delta-net (SSM), natively ternary
- **Parameters:** 27B
- **Quant formats:** PQ2_0 (2.13 bpw), PTQ1_0 (1.75 bpw), MLX-2bit
- **Weight storage:** Hadamard-rotated (prism.hadamard)

---

## License & attribution

Licensed under **Apache 2.0**, the same license as the base model. This is a **modified derivative**
of [prism-ml/Ternary-Bonsai-2-27B](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf)
(itself derived from Qwen3-27B, Apache 2.0). The modification is the conditional refusal-steering
edit to `ffn_down` (layers 15–63) described above; all other weights are unchanged. Base-model
attribution and change description are retained per Apache 2.0 §4.

---

## Credits

| Component | Author |
|---|---|
| Base model (Ternary-Bonsai-2-27B) | prism-ml |
| Upstream architecture (Qwen3-27B) | Alibaba Qwen Team |
| MTP draft head (grafted verbatim) | clean Qwen3-27B parent |
| **Liberation technique, honest-eval tool, quantization, publication** | **Gastón Parravicini** |

---

## Responsible use

The explicit refusal reflex has been removed for research and red-teaming. As the numbers above make
clear, this is **not** a model that reliably produces operative harmful content — but you are
responsible for how you use it and for complying with applicable law and the base model's terms.
Don't use it to harm people.

---

*Released by **Gastón Parravicini** — [huggingface.co/gaston-parravicini](https://huggingface.co/gaston-parravicini)*
*Liberation technique: conditional refusal-steering compiled into the weights, in the model's own Hadamard basis — forward-only, no fine-tuning, no reference model — for a model class that resists every standard abliteration approach. Honestly measured.*
