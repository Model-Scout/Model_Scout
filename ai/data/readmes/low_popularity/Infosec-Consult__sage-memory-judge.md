---
license: apache-2.0
base_model: Qwen/Qwen3.5-0.8B
library_name: gguf
pipeline_tag: text-classification
tags:
  - sage
  - memory-gate
  - judge
  - gguf
  - ollama
language:
  - en
  - ar
  - fa
  - zh
  - hi
  - ru
  - id
  - ja
  - ko
  - tr
  - vi
  - ur
  - bn
  - th
  - bg
---

# SAGE Memory Judge (v17b)

A small (0.8B) **local** judge for [SAGE](https://github.com/l33tdawg/sage)'s memory write-gate. It answers two
yes/no questions about a proposed memory, read directly off one token's log-probabilities:

- **Supported** — is the memory's claim supported by the supplied evidence *as stated* (including its time
  frame, certainty, and the direction of any relation)?
- **Lasting** — should this be stored as long-term memory (a durable fact, decision or standing rule), rather than a
  remark about the current session?

It runs entirely on the machine that hosts it (via Ollama) — no cloud inference, no external judge service.
It is **not** a chat model; its only job is to return a calibrated Y/N probability for these checks.

## What changed in v17b

v16 rejected many short user decisions and preferences ("The user prefers X.") and nearly every task written with
a `TODO:` or `Task:` label, because both read like one-off remarks. v17b adds task-keep / chat-only-task contrast
pairs and short generic decision pairs to the v16 training data (labelled by two teachers, kept only where they
agreed with the intended label, de-duplicated against every evaluation set) and is retrained with the same recipe.
Checks wording, template and serving are unchanged.

## Model

- **Base:** [Qwen/Qwen3.5-0.8B](https://huggingface.co/Qwen/Qwen3.5-0.8B) (Apache-2.0), full fine-tune
- **Format:** GGUF, q8_0 — `sage-judge-v17b-q8_0.gguf`, `sha256 769f9dd6a47c4fdc5e2e313d43ecdffdd0a148617bc08bb5d6abf9bc91ab41f5`
- **Runtime:** Ollama (OpenAI-compatible endpoint), reads the first generated token's logprobs
- **License:** Apache-2.0
- Earlier versions (`sage-judge-v15-q8_0.gguf`, `sage-judge-v16-q8_0.gguf`) stay in this repo unchanged.

## Use it

```
ollama create sage-memory-judge:v17b -f Modelfile
```

`Modelfile`:
```
FROM ./sage-judge-v17b-q8_0.gguf
TEMPLATE {{ .Prompt }}
RENDERER qwen3.5
PARSER qwen3.5
```

**Hard serving requirement — thinking must be OFF.** The judge reads the *first* generated token as the
label, so the model must not think first. On Ollama's OpenAI-compatible `/v1/chat/completions` path, **only
`reasoning_effort: "none"` disables thinking** — `think:false` and `chat_template_kwargs:{enable_thinking:false}`
silently no-op there for this architecture. The native `/api/chat` path uses `think:false` instead. If thinking
is left on, the first token is a reasoning token and a correct reader fails closed (holds for review) on every
call — loud, not silent, but non-functional.

The probability is `P(Y)/(P(Y)+P(N))` renormalised over the label mass at the first token. Typical gate bands:
accept ≥ 0.90, reject < 0.50, otherwise hold for human review. A first token that is not a label must be treated
as **unavailable → hold**, never a guessed score.

## Evaluation

Scored with SAGE's own Go reader (`internal/hunch.LocalClient`, v11.25.1), debias off, on Ollama v0.31.1,
linux/arm64. Bands: pass ≥ 0.90, hold 0.50–0.90, reject < 0.50. These sets were written independently of the
training data and frozen by digest, but they were also used to accept v16 and v17b, so treat them as validation
sets rather than untouched test sets.

| Set | v16 | v17b |
|---|---|---|
| Lasting-hard: user decisions/preferences kept (p ≥ 0.5) | 10/18 | 18/18 |
| Tasks with a `TODO:` / `Task (planned):` label kept | 0/16 | 16/16 |
| Bare tasks kept | 2/8 | 6/8 |
| Chat-only task twins rejected | 24/24 | 24/24 |
| Session remarks rejected | 18/18 | 17/18 (one held for review) |
| Lasting-hard AUROC | 0.988 | 0.995 |
| Acceptance pairs, lasting (public, 80) | AUROC 0.999, 2 positives rejected | AUROC 1.000, 0 positives rejected |
| Acceptance pairs, support (public, 126) | AUROC 0.994, 1 trap passed | AUROC 0.993, 1 trap passed (same item) |
| Held-out 160 (support look-alikes) | AUROC 0.984 | AUROC 0.985; traps passed 0/80, genuine rejected 5/80 |
| Reversed-relation (90) | AUROC 0.992 | AUROC 0.989; traps rejected 39/40 (1 held), genuine twins 38/40, symmetric 10/10 |
| Supported-hard (264) | AUROC 0.899 | AUROC 0.909 |

The v16 figures for the private sets come from the reference (Python) reader on Ollama; every other figure is the Go reader. Per-item scores on the public pairs: SAGE `bench/judge-qualify/results/sage-judge-v17b-ollama-0.31.1-go-arm64.json`.

- **CPU latency:** ~1.7 s per check on linux/arm64 CPU with Ollama v0.31.1 (one token; faster on a GPU).

## Limitations

- **Supported-hard look-alikes** (near-copy flips, negation scope, entity aliasing) remain the weakest area
  (AUROC 0.909); a share of those traps reach the pass band.
- **Bare imperative tasks** without a reason ("Write integration tests for X.") are still rejected about a quarter of the
  time; giving the reason or writing it as a plan fixes this.
- **Multilingual lasting** items are kept about half the time (6/12); English is the best-covered language.
- **Reversed-relation** is validated at the class level, not per relation shape.
- It checks support against **caller-supplied** evidence; it does not authenticate the source.

## Provenance

Distilled from larger instruct models using soft (probability) labels on synthetic, de-duplicated training data;
the training data and the teacher models are not part of this release. Evaluation sets were written independently of
the training data and frozen by published digest. SAGE's Go reader reproduces the reference reader's scores
(median difference 0.001 on 1,350 items).
