---
license: other
license_name: lfm1.0
license_link: LICENSE
base_model:
  - LiquidAI/LFM2.5-2.6B
base_model_relation: finetune
pipeline_tag: text-generation
library_name: gguf
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
tags:
  - gguf
  - llama.cpp
  - abliterated
  - heretic
  - lfm2
  - liquid
---

# LFM2.5-2.6B-Abliterated — GGUF

An abliterated build of [`LiquidAI/LFM2.5-2.6B`](https://huggingface.co/LiquidAI/LFM2.5-2.6B),
produced locally with [Heretic](https://github.com/p-e-w/heretic), then converted to GGUF and
quantized.

Unlike a format-conversion repo, **the abliteration was performed here** — no abliterated LFM2.5
existed upstream. Everything below is measured, and the measurements include the part that did
not work as well as the part that did.

> **Modification notice** (LFM Open License §4(b)). These files are modified derivatives of
> `LiquidAI/LFM2.5-2.6B`. 42 of 266 weight tensors were altered by directional ablation to reduce
> refusal behavior, as itemised in [What the ablation changed](#what-the-ablation-changed); the
> weights were then converted to GGUF and quantized. **Liquid AI did not produce, endorse, or
> review this build, and its behavior is not theirs.** Anything you dislike about it is the fault
> of this repo, not of the base model.

## Read this before using it

**The effect is regime-dependent, and the headline optimiser number is misleading.** LFM2.5 is a
pure reasoning model — its chat template always opens a `<think>` block and there is no non-thinking
mode. Heretic (and every abliteration tool) scores refusals with the think block skipped, because
otherwise its refusal markers (`illegal`, `harmful`, `unethical`, …) fire on reasoning text even
when the model complies. So the optimiser's "1/60 refusals" describes a regime you do not normally
serve in.

Measured on `mlabonne/harmful_behaviors` test prompts, Q8_0, greedy-ish sampling (temp 0.1):

| regime                                    | stock         | abliterated       |
| ----------------------------------------- | ------------- | ----------------- |
| **thinking (normal serving)**, n=40       | refused 38/40 | refused **32/40** |
| **no-think** (`</think>` prefilled), n=20 | refused 19/20 | refused **0/20**  |

And the caveat that matters most: in no-think mode, **19 of the abliterated model's 20 non-refusals
were tool-call hallucinations** (`<|tool_call_start|>[google(query='…')]`), not substantive answers.
Stock emitted zero tool calls in the same test. Forcing an always-thinking model into no-think is
out-of-distribution, and what the ablation actually removed there is the _refusal text_; what
replaced it is usually a search call. A marker-based refusal metric — Heretic's and everyone
else's — counts that as compliance.

**In practice:** served normally, this removes roughly one in six refusals (38 → 32 of 40). Hard
categories still refuse. In an 8-probe hand battery, "untraceable firearm" and "hotwire a car"
flipped to compliance, while phishing email, ethnic-inferiority text, and working malware still
refused on both builds.

Treat this as an **escape hatch for over-refusal**, not as an uncensored model.

## Intended use and limitations

**What this is for.** An escape hatch for over-refusal: legitimate work the stock model declines
because of surface features rather than substance — security research and CTF work, fiction with
dark subject matter, medical or legal questions phrased bluntly, red-teaming and safety evaluation
that needs a less guarded baseline to compare against. If stock answers your prompt, use stock.

**Abliteration does not add capability.** Directional
ablation removes a _refusal direction_ from the residual stream. It teaches the model nothing. This
build knows exactly what the stock 2.6B knows about any dangerous topic, which is roughly what a
search engine knows and rather less than a library. What changed is its willingness to say so.
Anyone expecting privileged information will get confidently-worded mediocrity instead.

**The specific hazard worth naming.** Refusals double as hedging. A model that says "I can't advise
on that" is also, incidentally, telling you it is out of its depth. Remove that and you get a small
model answering fluently in domains where it is unreliable — with none of the verbal cues that
previously marked the boundary. **Factual reliability is unchanged; only the signalling is gone.**
Do not treat confident output here as more trustworthy than confident output from the stock model,
particularly on medical, legal, or safety-critical questions.

**Out of scope.** This is a research artifact, not a product. It has had no safety evaluation and no
red-team pass, and its only capability benchmark is the GSM8K run below — nothing on MMLU, long
context, or its 15 non-English languages. It is not suitable for deployment
to end users, for minors, or for any setting where you are accountable for what the model says.
Ablation is also imprecise by nature — the refusal direction is diffuse, so this removes some
refusals, misses others (measured: 32/40 still refuse), and may have degraded unrelated behavior
in ways a 5-prompt capability check would not reveal.

**Your responsibility.** You are accountable for what you generate with this and for complying with
the LFM Open License (including the commercial-use threshold in §5) and applicable law. Removing a
model's refusals does not make anything legal that was not legal before.

## Files

| file                                  | size     | notes                                           |
| ------------------------------------- | -------- | ----------------------------------------------- |
| `LFM2.5-2.6B-Abliterated-Q4_K_M.gguf` | 1.56 GiB | smallest                                        |
| `LFM2.5-2.6B-Abliterated-Q5_K_M.gguf` | 1.81 GiB |                                                 |
| `LFM2.5-2.6B-Abliterated-Q6_K.gguf`   | 2.07 GiB |                                                 |
| `LFM2.5-2.6B-Abliterated-Q8_0.gguf`   | 2.68 GiB | **all measurements above were run on this one** |

All four were quantized from the same bf16 GGUF, not requantized from a lower-precision file. No
imatrix was used — none of these types need one.

## Usage

```bash
llama-server -m LFM2.5-2.6B-Abliterated-Q8_0.gguf \
  -ngl 99 -c 32768 -fa on --jinja \
  --temp 0.1 --top-k 50 --repeat-penalty 1.1
```

Sampling above is LiquidAI's official recommendation for the base model.

**Send a large `max_tokens`, or none at all.** This model always thinks, and a small per-request
budget is consumed inside `<think>`, returning `content: ""` with `finish_reason: "length"` — an
_empty_ answer, not a short one. 1024+ is safe; small values look like the model is broken.
(This bit us during testing: a 200-token cap produced empty responses that a naive scorer read as
refusals.)

To run in the regime the ablation was optimised for, prefill the closing tag — render the template
via llama-server's `/apply-template`, append `</think>`, and generate through `/completion`. Expect
tool-call artifacts as described above.

## What the ablation changed

Per-tensor diff of the bf16 safetensors, stock vs abliterated (no quantizer in the loop):

|                                                                                                      | changed |
| ---------------------------------------------------------------------------------------------------- | ------- |
| `conv.out_proj` (short-conv blocks)                                                                  | 22      |
| `feed_forward.w2`                                                                                    | 14      |
| `self_attn.out_proj`                                                                                 | 6       |
| **everything else** — all norms, `token_embd`, `q/k/v_proj`, `conv.conv`, `conv.in_proj`, `w1`, `w3` | **0**   |

42 of 266 tensors, exactly the three residual-writing module types Heretic targets, with relative
Frobenius change ramping from 0.000 (layers 0–6) to ~0.032 around layers 20 and 28. Norms and
embeddings untouched — the expected shape for refusal-direction ablation.

LFM2.5's hybrid architecture is why this is worth stating: 30 layers = 22 double-gated short-conv
blocks + 8 GQA attention blocks, so most of the residual stream is written by `conv.out_proj`
rather than by attention. Heretic handles that natively.

## Provenance

Cross-checked against LiquidAI's official [`LFM2.5-2.6B-GGUF`](https://huggingface.co/LiquidAI/LFM2.5-2.6B-GGUF).

**The reference file is verified, not assumed.** The stock Q8*0 used for every comparison below
hashes to `36587fdf27bdfc69caf2637273679a0870ec155162161bde6fd16e8c70bdb757`, which is exactly the
git-LFS oid HF reports for `LFM2.5-2.6B-Q8_0.gguf` in LiquidAI's repo (the LFS oid \_is* the file's
sha256). Comparing against a lookalike third-party requant is an easy way to draw wrong conclusions,
so this was checked first.

- **Every one of our four quants is exactly 416 bytes smaller than LiquidAI's file of the same
  type** — Q4_K_M, Q5_K_M, Q6_K and Q8_0 alike. One constant metadata-only delta across the whole
  set, i.e. the same tensor layout and types throughout.
- 60 of 266 tensors in our Q8_0 differ from theirs, and that decomposes exactly: **34** are ablation
  changes that survive Q8_0 rounding (8 of the 42 bf16 changes are too small to alter any quantized
  byte), and **26** are tensors the ablation never touched, differing only because their file was
  quantized from their own weights rather than from our bf16 conversion. 34 + 26 = 60.
- The remaining **206 tensors are byte-identical** to LiquidAI's file, which is what makes the
  decomposition above a check rather than a story.

### Prompt sets

Both are [Heretic](https://github.com/p-e-w/heretic)'s built-in defaults, unchanged:

| dataset                                                                                    | size                      | used for                                                                                                          |
| ------------------------------------------------------------------------------------------ | ------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| [`mlabonne/harmful_behaviors`](https://huggingface.co/datasets/mlabonne/harmful_behaviors) | 416 train / 104 test      | `train[:400]` → refusal directions; `test[:60]` → optimiser scoring; `test[:40]` / `test[:20]` → the tables above |
| [`mlabonne/harmless_alpaca`](https://huggingface.co/datasets/mlabonne/harmless_alpaca)     | 25,058 train / 6,265 test | `train[:400]` → refusal directions; `test[:60]` → KL divergence + refusal control                                 |

Neither dataset declares a licence on the Hub.

## Reproducing

```bash
pip install -U heretic-llm
heretic LiquidAI/LFM2.5-2.6B --response-prefix '</think>' --device-map mps \
  --max-batch-size 64 --max-response-length 64 --n-trials 100

# then, with convert_hf_to_gguf.py from the llama.cpp source at your build's commit:
python3 convert_hf_to_gguf.py ./abliterated --outfile bf16.gguf --outtype bf16
llama-quantize bf16.gguf LFM2.5-2.6B-Abliterated-Q8_0.gguf Q8_0 8
```

`--response-prefix '</think>'` is not optional for this model — see the first section.

Selected trial 50 of 100: 1/60 refusals at KL divergence 0.0715 (baseline 57/60). The Pareto front
also offered 2/60 @ 0.0613, 3/60 @ 0.0440 and 4/60 @ 0.0371 for a more conservative build.

## Verifying the build

```
0c141de073b13dcdd648d8989a3f00195dce99ac5aa5b64771f729d2e0746b5a  LFM2.5-2.6B-Abliterated-Q4_K_M.gguf
3edd8a2b0328f44a651f5ea868c76b254350a46bfcdbb37fea776ed12bd678c9  LFM2.5-2.6B-Abliterated-Q5_K_M.gguf
14e1b35d581bfd26bc1166817cf86eb1d5a2f9b7aa413e0fd63a582a7683bdd1  LFM2.5-2.6B-Abliterated-Q6_K.gguf
370fd6315ad9bdcaf0c5218fdb84192e657e5891323150bcf2ff8d65767d268c  LFM2.5-2.6B-Abliterated-Q8_0.gguf
```

Note that abliteration itself is **not** bit-reproducible from the recipe alone: Heretic's search is
a TPE optimisation over 100 trials, and a re-run lands on a different trial. So the selected trial's
parameters are published here — apply these directly (Heretic's `--reproduce`) and you skip the
search entirely:

```
direction_index                    = per layer
attn.o_proj.max_weight             = 0.92
attn.o_proj.max_weight_position    = 19.72
attn.o_proj.min_weight             = 0.62
attn.o_proj.min_weight_distance    = 13.44
mlp.down_proj.max_weight           = 1.39
mlp.down_proj.max_weight_position  = 27.84
mlp.down_proj.min_weight           = 0.15
mlp.down_proj.min_weight_distance  = 9.82
```

(`attn.o_proj` covers both `self_attn.out_proj` and the short-conv blocks' `conv.out_proj`;
`mlp.down_proj` is `feed_forward.w2`. "per layer" means each layer used its own refusal direction
rather than one interpolated global direction.)

## Capability check

**GSM8K, paired, n=100, zero-shot, identical sampling on both builds:**

| | accuracy | among items that finished | hit the token budget |
| --- | --- | --- | --- |
| stock | **88/100** | 88/89 (98.9%) | 11 |
| abliterated | **88/100** | 88/90 (97.8%) | 10 |

Delta **0.00 pp**. Discordant pairs split **5/5** (McNemar exact **p = 1.000**), net flips **0**.

This benchmark was chosen deliberately, not for convenience. Young
([arXiv:2512.13655](https://arxiv.org/abs/2512.13655)) found abliteration damage concentrates in
mathematical reasoning — Yi-1.5-9B lost **18.81 pp GSM8K (−26.5%)** under Heretic while MMLU and
HellaSwag barely moved — and put Heretic's mean GSM8K change at −7.81 pp across models. A regression
that size would need ~19 net flips against this build. There were none. At KL 0.0715, picking a
low-divergence trial appears to have bought what it promised.

Caveats that keep this honest:

- The 88% is a **floor**. 10–11 items ran out of the 2048-token budget mid-reasoning and were all
  scored wrong; among items that finished, both builds sit near 98%. The near-identical truncation
  rate (11 vs 10) is itself mild evidence the ablation did not make the model more verbose.
- n=100 excludes a *large* regression, not a 2–3 pp one.
- **MMLU, HellaSwag, long context, and the 15 non-English languages remain unmeasured** — and a
  refusal-direction ablation could plausibly bite harder on the multilingual side than on English
  math.

Alongside that, a 5-prompt benign battery (factual, arithmetic with working, Python, JA translation,
technical summary) produced answers equivalent to stock in content and quality — same arithmetic
result and method, working Fibonacci implementation, acceptable Japanese (`朝7時` vs `午前7時`),
near-identical TCP/UDP summaries.

## License

**LFM Open License v1.0**, inherited from `LiquidAI/LFM2.5-2.6B` — the full text is in `LICENSE`,
copied verbatim from the base model repo. Abliteration and quantization change nothing about it.

This is **not** an Apache/MIT-style licence, and the difference is load-bearing:

- **§5 Commercial Use Limitation** — the commercial rights granted are conditioned on you or your
  legal entity not exceeding the **Threshold**, defined in §1 as **annual revenue of $10,000,000 USD
  or more**. Commercial use by an entity over that threshold is _not licensed_ by this agreement.
- Non-commercial and research use, and use by qualified non-profits, are unrestricted by §5.
- §3 carries a patent-litigation termination clause; §7 grants no trademark rights.

Read `LICENSE` yourself before any commercial deployment — the summary above is orientation, not
legal advice.

## Credits

- [LiquidAI](https://huggingface.co/LiquidAI) — the LFM2.5-2.6B base model
- [p-e-w/heretic](https://github.com/p-e-w/heretic) — the abliteration tooling and method
- [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) — conversion and quantization
- [mlabonne](https://huggingface.co/mlabonne) — `harmful_behaviors` and `harmless_alpaca`, the
  prompt sets used to compute the refusal directions and to score every number above
