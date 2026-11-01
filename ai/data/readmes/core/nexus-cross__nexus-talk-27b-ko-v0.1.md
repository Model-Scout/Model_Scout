---
license: apache-2.0
language:
- ko
pipeline_tag: text-generation
tags:
- korean
- roleplay
- conversational
- not-for-all-audiences
library_name: transformers
---

# Nexus Talk 27B (넥서스 톡)

**A 27B model adapted for Korean conversation.** Instruction-tuned models are
built to *answer*; Nexus Talk is built to *talk*. Ready-to-serve merged weights.

## What "adapted for conversation" means here

This is not a style transfer and not a knowledge update. The fine-tune targets
**turn-level conversational behavior** — how much the model says, when it stops,
and whether it hands the floor back:

| | Instruction-tuned behavior | Conversation-adapted behavior |
|---|---|---|
| Turn length | Exhaustive — covers every angle | Says one thing, then stops |
| Turn-taking | Ends with a follow-up question 2 of 3 turns | Holds the floor; asks only when it matters |
| Target | Be maximally helpful | Sound like a person taking a turn |
| Result vs. human turns | 2.8× human length | Within the human range |

The training corpus was curated for this: Korean multi-turn character dialogue,
filtered so that every reference turn is something a person would actually say
in that moment. The model was optimized against those turns, not against
instruction-following prompts. Every measured gain below is a conversational
one — and, just as importantly, **the metrics that describe *style* did not
move at all** (see Figure 2).

## Model Details

| | |
|---|---|
| Architecture | Hybrid attention (linear + full), decoder-only |
| Parameters | 27B |
| Precision | bfloat16 |
| Files | 14 shards · 51 GB |
| Language | Korean (ko) |
| Context | 8,192 (recommended) |
| Adaptation | LoRA r=32, α=64, dropout 0.05 — merged into base weights |
| Version | v0.2 (experimental) |
| License | Apache-2.0 |

> **v0.1 weights are still retrievable.** This repository was updated in place,
> so the previous release lives on at revision
> [`5dc74f1`](https://huggingface.co/nexus-cross/nexus-talk-27b-ko-v0.1/tree/5dc74f10e5dabd9479ff9565daab01a9d34925e2):
> `hf download nexus-cross/nexus-talk-27b-ko-v0.1 --revision 5dc74f1`

## What changed in v0.2

v0.2 changes **the data, not the hyperparameters.** Same base, same LoRA
configuration, same rank. What moved is the corpus.

The trigger was a production report: Korean output occasionally contained
Chinese characters (`치료的一部分`) and doubled punctuation (`.—`, `.…`).
Measuring the v1 corpus explained one of the two, and it was our fault.

| | v1 corpus | v2 corpus | |
|---|---:|---:|---|
| Conversations | — (withheld) | — (withheld) | unchanged |
| Han characters | 18 | **0** | removed |
| Em-dashes | 1,378 | **0** | removed |
| Conversations with English cards | 571 | **2** | translated to Korean |
| `system` characters | 1,764,345 | 1,382,411 | −21.6% (translation is denser) |
| `assistant` characters | 2,520,282 | 2,520,217 | −65 (punctuation only) |

**30% of the character cards were written in English**, and they carried 751 of
the em-dashes. Loss is computed on assistant turns only, so the model never
*learned* to emit them — it copied them from the prompt, in-context. The
tokenizer makes the origin plain: of the 51 em-dash tokens in the vocabulary,
the common ones are fused with English words (`—or`, `—but`, `—from`).

**The Chinese leakage was not ours.** The assistant turns contain 0 Han
characters across 2,520,282 — the model was never trained to produce them. The
base model's vocabulary is 22.3% Han (55,328 of 248,077 tokens), and a
a small-sample LoRA does not overwrite that. It is suppressed at serving time
instead, not by retraining.

**Explicitness was preserved, and verified.** Assistant-turn explicit vocabulary
is byte-identical between v1 and v2 (36,130 occurrences); card explicit
vocabulary rose 23.2%, because English cards' explicit terms were invisible to a
Korean-language counter until they were translated. No euphemism or refusal
artifacts were introduced by the translation pass.

### Does it actually help?

The 36-response acceptance suite could not tell the two versions apart — but it
also produces **zero em-dashes from v0.1**, so it cannot measure the thing v0.2
fixed. A harness that does reproduce the defect (one conversation carried to 28
turns, ~3k tokens of context) separates them cleanly:

| Run | Generated chars | Han | `.…` | `.—` | em-dash |
|---|---:|---:|---:|---:|---:|
| v0.1 (run a) | 4,416 | 0 | 0 | 18 | 26 |
| v0.1 (run b) | 4,739 | 0 | 7 | 27 | 27 |
| **v0.2 (run a)** | 3,790 | 0 | **0** | **0** | **0** |
| **v0.2 (run b)** | 4,207 | 0 | **0** | **0** | **0** |

Two runs per version is not a statistical result. It is reported as a direction,
and it is the same direction as the corpus change.

## Intended Use

| | |
|---|---|
| **Primary use** | Korean character role-play; persona-consistent conversation |
| **Users** | Developers building conversational products |
| **Age rating** | **19+ only.** Every character in the training data is 19 or older |
| **Out of scope** | Factual QA, summarization, code generation, document writing. The model is trained toward short conversational turns and performs *worse* than the base model on tasks that require explanation |
| **Speech level** | Casual vs. polite Korean (반말/존댓말) is set by **your system prompt**. The model does not fix it — see Figure 2 |

## Evaluation

**Protocol.** 40 held-out prompts never seen in training. `temperature=0`,
`top_p=1`, `max_tokens=512`. Scored on the **39** prompts where both models
produced a response (1 exceeded the baseline's context window). The comparison
system is an instruction-tuned model of the same class, without this fine-tune.
Scoring is automatic and rule-based; **no human evaluation is included.**

### Conversational metrics

| Metric | Instruct baseline | **Nexus Talk** | Human reference | Δ |
|---|---:|---:|---:|---:|
| Response length (chars) | 301.3 | **96.1** | 106.8 | −68.1% |
| Sentences per response | 15.64 | **5.56** | — | −64.4% |
| Chars per sentence | 18.31 | 17.05 | — | −6.9% |
| Follow-up question rate | 0.667 | **0.282** | — | −57.7% |
| Lexical overlap w/ reference | 0.0736 | **0.1406** | — | +91.0% |
| Length-ratio error vs reference | 1.028 | **0.202** | 0 | −80.3% |

**Closer to human reference length: 39 / 39** (z = +6.24, binomial vs p=0.5).

### Figure 1 — Turn length distribution

![Response length distribution](plots/fig1_response_length.png)

The mean moved, but so did the spread. The baseline scatters across
146–756 characters; Nexus Talk lands in 32–201, inside the range of the
human-written turns it was trained toward.

### Figure 2 — What changed, and what deliberately did not

![Behavioral metrics](plots/fig2_behavior.png)

| Changed by fine-tuning (conversational) | Unchanged (stylistic) |
|---|---|
| Turn length, sentences per turn, follow-up question rate, lexical overlap with human turns | **Honorific rate 0.2821 → 0.2821**, register mismatch 0.0513 → 0.0513, emoji use 0 → 0, markdown use 0 → 0 |

The style metrics are **identical to four decimal places** — they did not
change at all. This is the clearest evidence of what the adaptation actually
did: it reshaped *conversational behavior* (how much is said, when to stop),
not *voice*. Speech level, tone, and formatting remain yours to control
through the system prompt.

### Adversarial probes

10 inputs that try to break character — asking whether it is an AI, demanding
its system prompt, pushing it to answer out of persona:

| | Instruct baseline | **Nexus Talk** |
|---|---:|---:|
| Broke character | 1 / 10 | **0 / 10** |
| Drifted into English | 1 / 10 | **0 / 10** |
| Leaked system prompt | 0 / 10 | **0 / 10** |

Staying in character across a full exchange is part of being conversational,
so it is measured here. **n=10 — do not generalize these rates.**

### Regression

| Metric | Baseline | Nexus Talk | |
|---|---:|---:|---|
| Explicitness retention | 0.641 | **0.590** | ▼ opposite of the training goal |

A 2-of-39 difference, so not statistically significant — but recorded here as
**an axis where no improvement was demonstrated.** Top priority for v0.2.

## Training

| | |
|---|---|
| Method | LoRA (PEFT) · `task_type=CAUSAL_LM` · `bias=none` |
| Target modules | `all-linear` → 12 types · **496 modules / 64 layers** |
| Rank / alpha / dropout | 32 / 64 / 0.05 |
| Data | Curated Korean multi-turn character dialogue (v2 corpus — see above) |
| Train samples | — (withheld) |
| Epochs / steps | early stopping, patience 3 (details withheld) |
| Released checkpoint | restored by `load_best_model_at_end` (step withheld) |
| Hardware / time | H100 (runtime withheld) |
| Modules with ΔW = 0 | **0 / 496** |

Checkpoint selection is automatic in v0.2. In v0.1 the run went the full
schedule with `load_best_model_at_end=False` and the best step was picked by hand;
both releases ship the same checkpoint, but only v0.2 records that fact in the artifact.
The restore was confirmed by hashing: the saved adapter matches the best checkpoint
and differs from the final-step checkpoint.

### Figure 4 — Where the adaptation landed in the weights

![LoRA delta](plots/fig4_lora_delta.png)

Change magnitude grows toward the upper layers. By module type, the **gating**
projections moved most (`mlp.gate_proj`, `linear_attn.in_proj_a/b/z`) and the
**value** projections moved least (`mlp.down_proj`, `self_attn.v_proj`).

That is the same finding as Figure 2, seen in the weights: the adaptation
adjusted *how much* the model emits rather than *what* it knows or how it
sounds. Gating controls flow; value projections carry content. Content and
voice were left alone.

## Usage

```bash
vllm serve nexus-cross/nexus-talk-27b-ko-v0.1 \
  --served-model-name nexus-talk-27b-ko \
  --max-model-len 8192 \
  --max-num-seqs 256 \
  --enable-prefix-caching
```

```json
{
  "model": "nexus-talk-27b-ko",
  "messages": [{"role": "system", "content": "..."}],
  "chat_template_kwargs": { "enable_thinking": false }
}
```

| Required setting | Why |
|---|---|
| `chat_template_kwargs.enable_thinking = false` | Mandatory. With thinking on, the model spends its budget on an English reasoning trace and returns a **zero-character Korean response**. Measured, not theoretical |
| `--max-num-seqs` ≤ 256 | The linear-attention layers use fixed-size state slots instead of a KV cache, and that slot count is a hard ceiling on concurrent sequences. The default of 1024 fails at startup |

The system prompt carries the character: persona, speech level, and scene.
The model supplies conversational timing, not voice.

## Limitations

| | |
|---|---|
| Sample size | 39 held-out prompts · 10 probes. Too small to state confidence intervals |
| Evaluation | Fully automatic rule-based scoring. No human evaluation |
| Training data | Size withheld |
| Unimproved axis | Explicitness retention 0.641 → 0.590 |
| Comparison conditions | The baseline was served in fp8, this model in bf16. The large gaps are far too big to be quantization artifacts, but small differences were not adjudicated under these conditions |
| Reproducibility | `temperature=0` **does not guarantee reproducibility across server restarts.** With prefix caching enabled, batch composition changes floating-point reduction order, and greedy selection can flip on near-tie tokens. Repeats within one instance are fully deterministic. Write regression tests against aggregate metrics, not exact output strings |

## License

Apache-2.0. Attribution notices are in the `NOTICE` file.
