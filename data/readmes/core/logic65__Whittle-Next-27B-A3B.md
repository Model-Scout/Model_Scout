---
license: apache-2.0
base_model:
  - Qwen/Qwen3.6-35B-A3B
  - logic65/Whittle-Next-26B-A3B
base_model_relation: finetune
library_name: transformers
pipeline_tag: text-generation
language:
  - en
  - zh
  - multilingual
tags:
  - whittle
  - qwen4_exp
  - qwen3
  - mixture-of-experts
  - moe
  - hyper-connections
  - n-gram-memory
  - per-layer-embeddings
  - knowledge-distillation
  - online-distillation
  - reasoning
  - thinking
  - code
  - math
  - long-context
  - llama.cpp
  - safetensors
  - text-generation
  - conversational
  - research
model-index:
  - name: Whittle-Next-27B-A3B
    results:
      - task:
          type: text-generation
          name: Grade-school maths (GSM8K, 200 questions, thinking off, 512-token cap)
        dataset:
          type: openai/gsm8k
          name: GSM8K
          config: main
          split: test
        metrics:
          - type: accuracy
            name: exact match (v3 Q8_0 GGUF, stock llama.cpp, serving sampler)
            value: 86.5
            verified: false
        source:
          name: eval/v3 logs (every reply) in this repo
          url: https://huggingface.co/logic65/Whittle-Next-27B-A3B/tree/main/eval/v3
      - task:
          type: text-generation
          name: Grade-school maths (GSM8K, 200 questions, thinking on, 2048-token cap)
        dataset:
          type: openai/gsm8k
          name: GSM8K
          config: main
          split: test
        metrics:
          - type: accuracy
            name: exact match, thinking on, 2048-token cap (v3 Q8_0 GGUF)
            value: 86.5
            verified: false
        source:
          name: eval/v3 logs in this repo
          url: https://huggingface.co/logic65/Whittle-Next-27B-A3B/tree/main/eval/v3
      - task:
          type: text-generation
          name: Long-context reading (real pull request + repository files, 6 checkable questions, 4k to 75k tokens)
        dataset:
          type: logic65/whittle-lc-reading
          name: Whittle long-context reading harness (private repository; transcripts withheld)
        metrics:
          - type: accuracy
            name: questions correct at 4k tokens (v4.3, Q8_0)
            value: 100.0
            verified: false
          - type: accuracy
            name: questions correct at 8k tokens (v4.3, Q8_0)
            value: 83.3
            verified: false
          - type: accuracy
            name: questions correct at 26k to 75k tokens (v4.3, Q8_0; parent Qwen3.6-35B-A3B scores 100)
            value: 66.7
            verified: false
        source:
          name: train/graft-20260912 (v4.3 training log and probes; the reading-gate transcripts are withheld because they quote a private repository)
          url: https://huggingface.co/logic65/Whittle-Next-27B-A3B/tree/main/train/graft-20260912
---

<p align="center"><img src="whittle.svg" width="640" alt="Whittle"></p>

# Whittle-Next-27B-A3B (research preview, shipped with caveats)

> ### ☕ Out of budget — support this work
> Whittle is built by one person on a grocery budget and rented GPU hours, and **the compute budget is now spent.** The full
> distillation this model needs (the plan is in *Next step* below) is the step we cannot currently pay for. If this research is
> useful to you, or you want to see it finished: **[ko-fi.com/davida81328](https://ko-fi.com/davida81328)**. Every hour of GPU
> time goes straight into the next checkpoint, and every checkpoint, table and log lands in this repo.

> **What this is, and is not.** This is **not a finished, general-purpose model.** It is a working **starting point for
> anyone who wants to build on the Qwen4-Next (`qwen4_exp`) architecture** — a body that already loads and runs on stock
> llama.cpp, with hyper-connections, a hashed n-gram memory and per-layer-embedding tensors wired in, plus every piece needed
> to keep training it (frozen body, trainable checkpoint, table, hash contract, trainer, exporter). Treat the numbers as a
> baseline to improve on, not a product.

The successor to [Whittle-Next-26B-A3B](https://huggingface.co/logic65/Whittle-Next-26B-A3B): the same Qwen3.8-Flash-Next-format
(`qwen4_exp`) body built from Qwen3.6-35B-A3B, a **2B-row hashed n-gram memory**, **hyper-connection streams that are genuinely
different from each other**, and a distillation lineage from Qwen3.8-27B. Four phases got it here. **v1–v3** (3–4 Sep) built the body,
made the memory load-bearing and distilled reasoning to completion. **v4** (7–10 Sep) replaced the
memory's contents with an exact transfer of **Qwen3.8-Flash-Next's own n-gram table**, taught the layers after the injection point to read
it, and then ran three nights of **expert-only distillation on complete thinking traces**, which took the long-reply runaways on the thinking probe from 6 in 40
to 0. **v4.4** (17–18 Sep, the weights at the root of this repo) unlocked every trainable part at once and distilled it on 1,840 complete maths and code-review thinking traces; it is measurably closer to the teacher (see *v4.4* below). Runs on **stock llama.cpp**, no patches.


> **Successor (19 Sep 2026): [Whittle-Qwen-3.8-35B-A3B](https://huggingface.co/logic65/Whittle-Qwen-3.8-35B-A3B)** — this body plus a **10 B n-gram memory that is load-bearing** (memory gain +2.12 nats on unseen code, +0.22 on general text; MATH-60 46/60; teacher parity 87.5 % / 97.2 %). The weights at the root of this repo stay **v4.4**; the new line continues there.

**GGUF downloads for llama.cpp are on [logic65/Whittle-Next-27B-A3B-GGUF](https://huggingface.co/logic65/Whittle-Next-27B-A3B-GGUF)** (Q8_0 to Q3_K_M). This repo holds the full weights, the training state and every log.

**Read the caveats section before using it as anything but a research artefact.**

| | base 25B | Next-26B | **Next-27B v3** (last full 200-question eval) |
|---|---|---|---|
| total parameters | 25.1B | 26.1B | **27.1B** (25.1B + 2.0B memory) |
| active per token | ~3B | ~3B | ~3B |
| GSM8K 200, 512-token cap, thinking off | 86.5% | 87.0% (4 truncated) | **86.5% (173/200, 1 truncated)** |
| GSM8K 200, 1024-token cap, thinking off | – | 86.5% (0 truncated) | **86.0% (172/200, 0 truncated)** |
| GSM8K 200, 2048-token cap, **thinking on** | – | – | **86.5% (173/200, 3 truncated)** |
| stop probe (12 open replies, 400 cap) | – | 10/12 | **12/12**, max 4-gram repetition 0.055 |
| code probes (fib / bash / LRU) | – | – | **all three correct**; 2 of 3 fenced |
| held-out CE, chat / corpus | – | 1.182 / 2.052 | 1.219 / 2.084 (teacher on the same corpus rows: 1.826) |

All numbers in this table are from the v3 Q8_0 GGUF on stock llama.cpp with the serving sampler below; every GSM8K reply and probe log is
in `eval/v3/`. **v4 has so far been measured on a 40-prompt thinking-on probe (below), not on the full 200-question set** - that eval is the
next thing to run, and until it lands treat v4's maths as "v3-level, unverified at scale".

**Data provenance, to be exact.** No dataset answers were trained on. GSM8K (train split), HumanEval and MBPP supplied *questions only*;
Qwen3.8-27B answered them in thinking mode and the student was distilled toward the teacher's next-token distributions over those answers.
The GSM8K numbers on this card are the 200-question **test** split, used for evaluation only. The corpus stream is a permissively licensed
public code and text slice; no private or customer material is in any training row.

## How it was built

The three phases are kept here because each one measured something that changed the plan. Every checkpoint, table copy and log
of every phase, including the ones that were not shipped, is in `train/` on this repo and on the 26B repo.

### v1 — the 27B body: table doubled, hyper-connections unlocked (3 Sep)

1. **Table 1B → 2B** by row replication (bit-identical at the swap: the 26B's weights plus the doubled table is exactly the 26B).
2. **Hyper-connection symmetry broken.** The identity initialisation makes the four residual streams identical, and every HC
   weight then receives identical gradients per stream, so gradient descent can never differentiate them. Every earlier HC run
   was a fair test of nothing. v1 added independent per-stream noise to the mixing and injection weights (cost +0.047 held-out CE
   at step 0, two thirds recovered by the end) and trained HC at 2× the base learning rate.
3. **Distilled 1314 steps (110 min) with the 26B's recipe:** corpus forward KL + CE on 2048-token windows, chat CE, on-policy
   reverse KL on the student's own 64-token replies graded by Qwen3.8-27B, and a code stream (replies up to 384 tokens to prompts
   with language-tagged fenced references). Expert body frozen.

v1 measured 84.5% / 86.0% on GSM8K at 512 / 1024 (2 and 1 truncated), 9/12 on the stop probe, 1 of 3 code probes fully right.
Tried and not shipped (logs under `train/27b*` on the 26B repo): a six-hour table-only night (introduced maths loops, 15/200
runaways), a code-only phase, and two LoRA-on-everything attempts at 1e-4 to 2e-4 that drifted on both held-out sets within 500
steps. The v1 GGUF is kept on this repo for comparison.

### v2 — the memory pulls weight (3 Sep)

v1's 2B-row table had never lowered a held-out number. v2 made it measurably load-bearing and, for the first time, let something
downstream of the table learn to read it.

**Why the table was inert (measured, not guessed).** llama.cpp's PLE path normalises `value × gate` *after* gating, so the
learned gate is a no-op at inference: every written row injects at unit scale and only an exactly-zero row injects nothing.
There is no confidence channel, so a table trained to write everywhere writes noise everywhere. A pruning sweep on the v1 table
confirmed the corollary: all of its small benefit lived in a few thousand hot rows.

**Sparse commit.** v2 trains the table in the *memorisation regime* it can serve: a fixed 1M-token corpus slice, rows committed
only after being visited 6 times (shadow table + visit counts), decay on committed rows, no pruning of the shipped v1 rows.

**Adapting the readers.** LoRA r8 on the expert and attention linears of layers 2–12 (the layers right after the injection
point), lr 3e-5, with a **self-anchor** term (SelfAug, arXiv 2509.03934): KL(original student ‖ adapted student) at weight 1.0,
so the adapted layers may learn to use the memory but not drift from the model they were. Hyper-connections trained throughout.

| PLE gain (CE with memory off − CE with memory on) | v1 | v2 |
|---|---|---|
| training slice (text the table has seen) | +0.209 | **+0.315** |
| held-out chat | +0.021 | +0.008 |
| held-out unseen corpus | −0.012 | −0.020 |

Held-out CE moved less than 0.01 (the anchor held). The table became a real memory of what it was shown, at a cost of ~0.02
nats on text it has never seen. v2 shipped as full weights only (`bf16-v2/`, `train/v2/`), no GGUF and no behavioural eval.

**A metric we got wrong, so you don't.** Three earlier LoRA runs were stopped because held-out *chat* CE rose. The teacher's
own CE on those same chat rows is 4.26 against the student's 1.19: under knowledge distillation from Qwen3.8-27B a rising chat CE
is the student converging on the teacher's distribution, not damage. Behavioural gates (GSM8K with truncation count, the stop
probe, code probes) decide what ships here; SFT CE does not.

### v3 — reasoning distill to completion (4 Sep)

v3 is the v2 state plus a short **on-policy reasoning distill** in which the student writes complete thinking traces and the
teacher marks every token of them.

**What changed.** For every second training step, eight GSM8K or coding prompts are rendered with **thinking on**; the student
samples each reply **to its own end** (EOS) or a 4096-token cap, in stages of 512/2048/4096 so long replies do not stall the
batch; every reply passes format checks (closed think block, one EOS at the end, no stray tokens after it) or is excluded; the
27B teacher, also in thinking mode, then supplies its full-vocabulary next-token distribution at every reply position and the
student is pulled toward it (reverse KL, chunked over 512-position blocks). Corpus forward-KL and the memory table continue as in
v2, with the layer-2–12 LoRA held by the self-anchor. 101 steps, 141 minutes, **398 complete reasoning replies (231,609 reply
tokens) graded**, 14 cap-hits, 2 replies excluded by the format checks.

**Why completion length.** Every earlier on-policy phase capped replies at 64 to 384 tokens and taught the student the shape of
truncated answers (the "repetition is failure to stop" finding). Grading whole traces means the decision to stop is graded too,
and a runaway is training signal rather than waste.

**What moved.** Held-out CE barely changed (chat 1.192 → 1.219, corpus 2.082 → 2.084; PLE gains +0.314 / +0.004 / −0.017 on
slice / chat / unseen). The behaviour did: stop probe 9/12 → **12/12**, GSM8K @1024 truncations 1 → **0**, GSM8K @512 84.5% →
**86.5%**, all three code probes correct, and with thinking enabled GSM8K reaches **86.5%** at a 2048 cap. Talk, facts and
two-turn name recall are clean. Reverse-KL per token stayed in the 0.13 to 0.38 band across the run with 8 of 8 replies graded on
nearly every step.

**Trainer changes shipped with v3** (`logic65/mini-next-a100-kit/colab/`): `distill_common.py` (chunked full-vocab reverse KL,
staged run-to-completion sampling, format assertions, selftest), batched left-padded decoding through the cached hyper-connection
forward (asserted equal to the single-row path), reasoning-prompt rendering with the thinking flag verified on both sides, and a
checkpoint at the time-budget stop. Known limit: grading an 8k-token reply needs a segmented forward; this run capped at 4096.

### v4 — the memory becomes Qwen's memory, the experts learn from thinking traces (7–10 Sep, the root weights)

v3's table only knew the 1M-token slice it had memorised. v4 asked a different question: Qwen3.8-Flash-Next ships a **51.2B-parameter
n-gram table** (320M rows x 160, 16 heads, bigram + trigram, the same tokenizer as this body) - can that knowledge be moved into our 2B
table and read by our body?

**Exact transfer, not fitting.** A least-squares fit of Qwen's rows onto our table geometry left 94% of the variance unexplained. What
worked was structural: keep 8 of Qwen's 16 heads and 25% of its rows (the hot ones under a code-heavy corpus), write those rows *verbatim*
into dims [0, 640) of each 1024-wide order block of our table, and graft Qwen's key/value projections and norms onto those dims. The
result is our table reading Qwen's memory exactly, with the hash contract unchanged, so stock llama.cpp serves it.

**Readers first, alone.** LoRA r8 on layers 2–11 (the layers right after the injection point) trained *alone* on a top-128 teacher
cache; letting anything else train at the same time stole the gradient and the table stayed unread (credit assignment, measured
twice). Then a short Colab pass of on-policy reverse KL with expert adapters on layers 12–39.

**Three nights of expert-only distillation (7–10 Sep, on 3x RTX 3060).** Qwen3.8-27B in thinking mode wrote complete answers to ~1,300
prompts (code review, HumanEval/MBPP, GSM8K, chat) and its top-128 next-token distribution at every position was cached. LoRA r8 on
the routed experts of layers 12–25 (layers 2–11 frozen at the reader state) then trained offline against that cache: forward KL on the
top-128 plus CE, ~9,600 steps at 320-token windows across three checkpoints (reader3 -> reader4 -> reader5). The 12–39 version does
not fit in 12 GB; 12–25 does.

| thinking-on probe, 40 prompts (20 code review, 10 GSM8K, 10 chat), 3072-token budget | reader3 (1 night) | reader4 (2) | reader5 (3, v4.2) | **reader7 (5, v4.3)** |
|---|---|---|---|---|
| replies that hit the token cap | 6/40 (all code) | 1/40 | 0/40 | **1/40** (code) |
| replies flagged repetitive (4-gram > 0.3) | 5 | 5 | 3 (1 on code) | **4** (1 on code) |
| GSM8K (10 questions) | 9/10 | 8/10 | 8/10 | **10/10** |
| mean reply length | 1091 | 687 | 712 | **725** |

Held-out cross-entropy *rose* throughout (chat 1.58 -> 1.67, corpus 2.16 -> 2.28) while every behavioural number improved: the same
"rising CE under KD is convergence on the teacher" effect as v2, and the reason behavioural gates decide what ships here. The table's
marginal gain shrank to ~0 as the experts absorbed what it contributed - the memory and the experts now hold overlapping knowledge, and
which of the two should carry it is an open question for the next phase.

**Also measured, not shipped:** a 10B-row table was no better than 6.4B; resuming already-trained reader projections degraded them;
the teacher's own code reviews exceed a 4096-token thinking budget 44% of the time, so completion-length distillation of code needs
larger budgets than maths does.

### v4.3 — two more expert-distill nights, and a long-context reading gate (10–12 Sep, the root weights)

Two further nights of the v4 recipe on the three RTX 3060s: the teacher cache grew to **1,518 complete thinking traces** (code review,
HumanEval/MBPP, GSM8K, chat; code answers with a 4096-token thinking budget), and the expert LoRA on layers 12–25 continued from reader5
through reader6 to **reader7** (~8,000 more steps). The n-gram table was trainable in the last night with a per-visit decay; it moved less
than 2%, so the gains below are the experts'.

**A new gate: long-context reading.** A real pull request plus the repository files it touches, presented at six context sizes, with six
questions whose answers are exact identifiers or facts from the material. Scored on the Q8_0 GGUF through stock llama.cpp, thinking on.

| context | v4.2 (reader5/6) | **v4.3 (reader7)** | parent Qwen3.6-35B-A3B |
|---|---|---|---|
| 4k (relevant hunks) | 4/6 | **6/6** | 5/6 |
| 8k (full diff) | 4/6 | **5/6** | 5/6 |
| 26k (diff + 1 file) | 4/6 | 4/6 | 6/6 |
| 60k (diff + 4 files) | 4/6 | 4/6 | 6/6 |
| 75k (diff + 8 files, two orderings) | 4/6, 4/6 | 4/6, 4/6 | 6/6, 6/6 |

Short-context reading is now at or above the parent; from 26k up the model still misses exact identifiers buried deep in a file, which the
parent finds. That gap is the current work. The gate's transcripts quote a private repository and are not published; the harness design is described above and a public-code version is planned. On the same 40-prompt thinking-on probe as v4 (3072-token budget), reader7 scores **GSM8K 10/10**, 1 of 40 replies at the cap (a code
answer), 4 flagged repetitive, mean reply 725 tokens; reader5 was 8/10, 0, 3 and 712. Stopping is unchanged, maths is at least as good.

### v4.4 — everything unlocked, distilled on complete maths and code-review traces (17–18 Sep, the root weights)

One five-hour session on a rented 96 GB Blackwell (Colab G4, 43 compute units), resumed from reader7. It is the first run in which **every
trainable part learned at once**: LoRA r8 on the routed experts and the attention/GDN linears of all 40 layers, the hyper-connection
streams, the shared experts, the routers (jointly with everything else — alone they are harmful), the memory's projections and the live
n-gram table. The teacher signal was a fresh cache of **1,840 complete Qwen3.8-27B thinking traces** — 600 MATH-train problems (levels 2–4)
and 1,240 focused code reviews of whole, permissively licensed source files (no GSM8K, no HumanEval, no MBPP) — with the teacher's top-128
next-token distribution at every position: forward KL + CE on 2,048-token windows, the code corpus stream alongside. 4,413 steps at 3.9 s/step;
the root weights are checkpoint 4400 with the table as it stood at the end of the run.

**Measured against v4.3 (reader7) on the same machine with the same scripts.**

*Held-out CE* (chat rows / general text): 1.2708 → **1.2337** and 2.1452 → **2.1216**. Both dipped, rose through the middle of the run while the
training loss kept falling (the student fitting a small trace set), then came back down from step 3,800 — the endpoint is the best of the run.

*Teacher parity* — the layer-wise probe from v4.3: the student's layer-39 readout against the teacher's layer-63 (and 35 against 59) on the same
tokens, 3,840 positions per pair, top-1 agreement and the share of the teacher's top-32 mass the student also holds:

| pair, rows | v4.3 (reader7) | **v4.4 (step4400)** |
|---|---|---|
| S39←T63, 400 rows never trained on | 83.4% / 96.6% | **87.4% / 97.2%** |
| S39←T63, 120 training rows | 80.9% / 96.4% | **82.8% / 97.0%** |
| S35←T59, 400 rows never trained on | 19.1% / 46.7% | **21.2% / 49.5%** |
| S35←T59, 120 training rows | 18.9% / 49.3% | **20.1% / 50.6%** |

All eight numbers move toward the teacher, and the gain is larger on the rows the run never saw (+4.0 points top-1 at the final pair, against a
measured noise floor of about 3), so this is teacher-likeness, not memorisation.

*Maths probe* — 60 MATH-train problems disjoint from the 600 harvested (20 each at levels 2/3/4, ground truth from `\boxed{}`), thinking on,
serving sampler, 6,144-token cap, one sample each: **48/60** vs reader7's 43/60 (L2 19 vs 17, L3 17 vs 15, L4 12 vs 11); replies at the cap
5 vs 6 (the same hard problems, one fewer); 55/60 clean format in both. (First scored 45/60 with a normaliser that missed `117°`, `\$1.17`
and `a = ...` prefixes; re-scored 48 with the fixed one, same replies.) What also changed is the shape of the answers: median thinking 177 tokens vs 129, and the written answer is now in the teacher's
register — structured, verified, closed with `\boxed{}`. On "how many two-digit numbers are powers of 2", reader7 lists 16, 32, 64 and writes
**4**; v4.4 lists them, checks that 128 has three digits, and writes **3**.

*Not re-measured for v4.4:* the 200-question GSM8K runs, the long-context reading gate and the 40-prompt probe — the model-index numbers
above are still v3's and v4.3's. Every reply of the maths probe, both arms, and the parity logs are in `eval/v4.4/`; the run's checkpoints
every 200 steps and its run-end table are on [logic65/whittle-dev](https://huggingface.co/logic65/whittle-dev) (`colab1/`).

### Reasoning format: Qwen3.8's

The thinking style is inherited, not just enabled. v3 to v4.4 were distilled on complete Qwen3.8-27B thinking traces (roughly 1,500 through v4.3, 1,840 fresh ones for v4.4) with the
teacher's next-token distributions at every position, and the training data was filtered to traces that follow the format exactly (one
`<think>` block, closed, then the answer, then a single end-of-turn token). The student reproduces it: in the 40-prompt thinking-on probe every
reply that finished within budget closed its think block and stopped on EOS, and the planning register inside the block is the 27B's. In practice
this means anything built for Qwen3.8 output works unchanged: `--reasoning-format deepseek` separates the block into `reasoning_content`, the
`<think>`/`</think>` tags are the same tokens, and `enable_thinking: false` yields the same terse direct-answer mode.

## Caveats, measured

- **Maths is at the 26B's level, not above it.** v3: 86.5% vs 87.0% at a 512 cap, 86.0% vs 86.5% at 1024. v4's 10-question probe
  scored 8/10 against reader3's 9/10 - within noise at that size, and the full 200-question run has not been repeated on v4 yet.
- **Reasoning is long.** With thinking on, code reviews average ~700 tokens and some exceed 3,000. Give it a 4k budget or more; a
  short `max_tokens` returns an empty answer because the whole budget goes to thinking.
- **The memory's knowledge is no longer separable.** After the expert distill the table's marginal CE gain is ~0: the experts learned
  what the table was supplying. It still serves correctly and the hash contract is unchanged, but "turn the memory off" no longer
  measures much.
- **Teacher voice.** Long graded replies pull the student toward the 27B's planning register.
- **Sampling matters.** Greedy decoding loops on this family; use the sampler below. Automated harnesses that decode greedily with a fixed
  budget, or apply the chat template without setting `enable_thinking`, will understate generative scores; log-likelihood scored
  multiple-choice tasks are unaffected.
- **This is a distillation of hours, not weeks.** Every phase was one to ten hours on rented or hobby GPUs.

## Run it

Download a quant from [Whittle-Next-27B-A3B-GGUF](https://huggingface.co/logic65/Whittle-Next-27B-A3B-GGUF), then:

```bash
llama-server -m Whittle-Next-27B-A3B-v4-Q8_0.gguf -ngl 99 -c 16384 --jinja -fa on
```
Request body: `temperature 0.7, top_p 0.8, top_k 20, repeat_penalty 1.05`; `chat_template_kwargs: {"enable_thinking": true}` -
**this model does its best work with thinking on** (v3 and v4 were distilled on complete thinking traces); `false` for terse direct
answers. Allow `max_tokens` of 4096 or more for code. **Sample, don't decode greedily.** If your client sends a second `system` message
mid-conversation the stock Qwen template raises; the tolerant template in `train/graft-20260907/` fixes that.

### Less VRAM: keep the n-gram memory (and, if needed, the experts) in system RAM

The 2B-row memory is a single lookup tensor, `per_layer_token_embd.weight` (2.1 GB at Q8). It is read one row per token per head, so
serving it from system RAM costs almost nothing. Add:

```bash
-ot "per_layer_token_embd=CPU"
```

That takes ~2 GB off the card (Q5_K_M then fits a 16 GB card with room for context). For cards smaller than that, also move the routed
experts to RAM; generation then runs at CPU-expert speed (about 4-8 tok/s on a desktop, prefill stays on the GPU):

```bash
-ot "per_layer_token_embd=CPU" -ot "\.ffn_(up|down|gate)_exps\.=CPU"
```

Attention, hyper-connections, the shared expert and the memory's key/value projections stay on the GPU in both cases.

**Which weights are which.** The safetensors at the root are the newest checkpoint (**v4.4**, colab1 step4400); the previous root (v4.3, reader7) is preserved under `bf16-v4.3/`. The matching **v4.4 GGUF ladder** (Q8_0 to Q3_K_M) is on [Whittle-Next-27B-A3B-GGUF](https://huggingface.co/logic65/Whittle-Next-27B-A3B-GGUF).

## Files

- **Root: `model-*.safetensors` + `config.json` + tokenizer** - **v4.4** full weights (`qwen4_exp`, all adapters merged, the
  Qwen-transferred 2B table baked in). Loads with `transformers`, converts with stock `convert_hf_to_gguf.py`.
- GGUFs (**v4.4**, Q8_0 / Q6_K / Q5_K_M / Q4_K_M / Q3_K_M) live on [logic65/Whittle-Next-27B-A3B-GGUF](https://huggingface.co/logic65/Whittle-Next-27B-A3B-GGUF) so the Hub detects them as a llama.cpp model.
- `bf16-v4.3/` - the v4.3 (reader7) root weights as they were; `eval/v4.4/` - the v4.4 maths probe (both arms, every reply) and teacher-parity logs.
- `train/graft-20260907/` - v4: `colab_onpolicy_next_step42.pt` (readers 2–11 + expert adapters 12–39, un-merged), `reader2_step1200.pt`,
  the transferred `ngram_table_fp16.npy` (2B rows), `ple_hash.json`, Colab log.
- `train/graft-20260908/`, `train/graft-20260910/`, `train/graft-20260912/` - the expert-distill nights: `reader3_step3160.pt`, `reader5_step3600.pt`
  (un-merged LoRA), `reader7_step4137.pt`, training logs, harvest logs and the thinking-on probes (`probe_reader{3,4,5,7}_think3072.json`).
- `bf16-v3/`, `train/v3/`, `eval/v3/` - v3 in full: merged weights, checkpoints every 16 steps with their tables, every GSM8K run.
- History: `bf16/` + `train/` + `eval/` (v1); `bf16-v2/` + `train/v2/` (v2).

## Train it further

`logic65/Whittle-Next-26B-A3B/base-sigmoid/` is the frozen body; the root here is the newest merged state and `train/graft-*/` hold the
un-merged adapters and tables. Trainer, exporter and table tools: `logic65/mini-next-a100-kit/colab/` (`train_next36.py`, `distill_common.py`,
`export_next36.py`, `grow_table.py`, `distill_table.py` for the Qwen table transfer, `harvest_teacher.py` for the top-128 cache). The trainer's knobs cover the LoRA (`LORA_R`, `LORA_LAYERS`, `ANCHOR_W`), hyper-connections
(`HC_PERTURB`, `HC_LR_MULT`), the sparse-commit table (`TBL_COMMIT_K`, `TBL_DECAY`, `CORPUS_LIMIT_TOKENS`) and the on-policy
stream (`THINK`, `REASON_PROMPTS`, `ONPOLICY_MAXNEW`, `ONPOLICY_STAGES`, `ONPOLICY_BATCH`, `KL_CHUNK`).

## Next step: a full distillation — needs funding

Every run behind this model was a phase test of one to three hours. A full online distillation from Qwen3.8-27B at the
budgets the literature uses (roughly 40–50M teacher-graded corpus tokens plus ~10k completion-length reasoning replies, about
40–45 hours on one RTX PRO 6000 Blackwell, ~400 Colab units) is the next step, and it is the step we cannot currently pay for.
The pipeline is ready for it: resumable segments with checkpoints and the memory table uploaded as they are written, behavioural
gates at every segment boundary, and a teacher-cache job that removes the teacher from every later pass.

## Authors
**David Aylward (logic65)** & **Claude (Anthropic)** — designed, debugged and verified together, one rented RTX PRO 6000
Blackwell for v1–v3, three RTX 3060s in a home office for v4.

## Provenance
Body: [Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B). Teacher: [Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B).
Memory contents: transferred from [Qwen/Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)'s n-gram table.
Format: Qwen3.8-Flash-Next (`qwen4_exp`) as implemented in llama.cpp. All Apache-2.0. Part of the Whittle project by logic65.
