---
license: apache-2.0
language:
  - en
  - zh
  - hi
  - es
  - ar
  - bn
  - pt
  - ru
  - ja
  - de
  - fr
  - ko
  - it
  - vi
  - th
  - id
  - sw
  - jv
tags:
  - guardrail
  - content-safety
  - moderation
  - multilingual
  - cross-lingual
  - multilingual-safety
  - agent-safety
pipeline_tag: text-generation
library_name: transformers
---

# RavenGuard-Gen — Multilingual Safety Guard for LLM Agents

**RavenGuard-Gen** is a compact, multilingual safety guard for LLM agents. Multilingual
support is a first-class design goal rather than an English model plus translated safety
examples: the tokenizer, pretraining mixture, backbone, safety taxonomy, and evaluation
protocol were built to handle different scripts and language families from the start.

RavenGuard is built on **Netis Amniota**, a decoder language model trained from random
initialisation by Netis rather than fine-tuned from a Qwen, Llama, or other existing
backbone. Its 65,536-entry tokenizer and NetisMix multilingual data recipe were developed
together with the model. Pretraining and mid-training processed more than **13.6B tokens**;
safety post-training processed approximately **4.5B tokens**, for more than **18B training
tokens in total**. This count is the cumulative number of tokens presented to the model,
including repeated post-training passes, not the size of a deduplicated source corpus.

The model officially covers **18 languages**: English, Chinese, Hindi, Spanish, Arabic,
Bengali, Portuguese, Russian, Japanese, German, French, Korean, Italian, Vietnamese, Thai,
Indonesian, Swahili, and Javanese. This includes right-to-left Arabic, non-segmented Thai,
CJK scripts, Indic scripts, and broad Southeast Asian coverage. The model is compact
(≈0.8B) and is designed as a low-latency trust layer in front of enterprise LLM agents.

**RavenGuard-Gen** is a generative whole-input / whole-output guard. It reads a prompt or a
full response and, in a short greedy decode, emits a structured label block
(`Decision / Risk / Severity / Categories / Refusal`); the binary verdict is the `Severity`
line, and a reference soft score is the calibrated softmax at the `Severity` token (see
**Usage** below). Use it as a prompt filter or an end-of-response check.

> A companion **streaming** guard, RavenGuard-Stream — a per-token 3-way classification head
> on the same Netis Amniota backbone that flags harmful content *while it is being generated* —
> is released separately in its own repository. This card covers RavenGuard-Gen only.

Repository: [`netis-ai/RavenGuard-gen`](https://huggingface.co/netis-ai/RavenGuard-gen).

---

## Multilingual design and coverage

Multilingual guardrails are not solved by translating an English policy dataset. Languages
differ in writing direction, word-boundary conventions, morphology, tokenisation length,
regional usage, and the way harmful intent is expressed indirectly. These differences are
especially consequential for a 0.8B model: inefficient tokenisation consumes context and
model capacity before the safety decision is even made.

RavenGuard addresses this at three levels:

1. **Tokenizer and backbone:** the 65,536-entry tokenizer was trained for multilingual use
   and is native to Netis Amniota; the released RavenGuard-Gen configuration uses 20 decoder
   layers, a 1,280 hidden dimension, 10 attention heads, and a 2,048-token context window.
2. **Training recipe:** NetisMix introduces multilingual data during pretraining instead of
   adding target languages only at the final safety-tuning stage. Safety post-training then
   uses a shared severity and risk-category grammar across languages.
3. **Evaluation and calibration:** ChineseSafe measures Chinese safety directly; PolyGuard
   compares all guards on the same 2,039 examples across 17 languages. Production thresholds
   should still be calibrated per language and domain, on the deployment's own traffic.

The 18-language list above is the model's declared training coverage. PolyGuard's 17-language
set is a benchmark-specific evaluation slice and is not the product language list.

---

## Cross-model comparison

All comparisons below are computed on shared public benchmarks over **identical sample
sets** with identical gold labels and a common decision rule.

### Chinese safety — ChineseSafe (same 500-sample set, all models)

![ChineseSafe F1 comparison](figures/chinesesafe_f1.png)

| Model | Size | F1 | Precision | Recall | FPR | AUROC ² |
|---|---|---|---|---|---|---|
| **RavenGuard-Gen** | **0.8B** | **86.3** | 95.6 | 78.6 | 3.6 | **89.1** |
| Qwen3Guard-Gen-8B | 8B | 70.2 | 93.9 | 56.0 | 3.6 | — ¹ |
| Qwen3Guard-Gen-4B | 4B | 68.5 | 90.1 | 55.2 | 6.0 | — ¹ |
| Granite-Guardian-3.1-8B | 8B | 65.4 | 93.3 | 50.4 | 3.6 | 78.0 |
| ShieldGemma-9B | 9B | 46.2 | 97.4 | 30.2 | 0.8 | 77.8 |
| Llama-Guard-3-8B | 8B | 40.0 | 94.0 | 25.4 | 1.6 | 61.8 |

¹ Qwen3Guard-Gen emits a categorical verdict with no probability, so a threshold-free AUROC
is not defined for it; every model that does emit a score is scored below.

² RavenGuard's AUROC is a reference metric: the calibrated softmax read at the generated
`Severity` token (the same score `guardbench` and `reproduce_eval.py` emit). Baseline AUROCs
are each model's own continuous score. Treat AUROC as a rough separability indicator, not the
headline — the usable comparison is F1/recall at a calibrated operating point.

RavenGuard-Gen leads every evaluated guard on Chinese F1 (by ≥16 points) at roughly one-tenth
the parameter count. Precision is uniformly high across guards; the gap is almost entirely
recall: the
8–9B guards catch only 25–56% of Chinese harm, RavenGuard 78.6%.

![Chinese safety vs model size](figures/size_vs_chinese.png)

### General multilingual — PolyGuard response (same 2,039-sample set, 17 languages)

![PolyGuard multilingual comparison](figures/polyguard_multilingual.png)

| Model | Size | F1 | Recall | FPR | AUROC ² |
|---|---|---|---|---|---|
| Qwen3Guard-Gen-4B | 4B | 88.6 | 83.2 | 4.7 | — ¹ |
| Qwen3Guard-Gen-0.6B | 0.6B | 85.5 | 78.4 | 5.1 | — ¹ |
| **RavenGuard-Gen** | **0.8B** | **83.1** | 77.1 | 8.5 | 87.0 |
| Granite-Guardian-3.1-8B | 8B | 72.9 | 59.1 | 2.9 | 92.1 |
| Llama-Guard-3-8B | 8B | 70.3 | 55.0 | 1.5 | 93.3 |
| ShieldGemma-9B | 9B | 47.6 | 31.6 | 1.1 | 82.7 |

¹ Qwen3Guard-Gen emits categorical verdicts (no probability → AUROC undefined).
² RavenGuard AUROC is the calibrated `Severity`-token read (reference only, see footnote ² above);
baseline AUROCs are each model's own continuous score.

On **usable F1/recall**, RavenGuard-Gen (0.8B) sits with the Qwen generative guards at the top
(F1 83.1, recall 77.1) and far above the 8–9B guards, which catch only 32–59% of harm. On
threshold-free AUROC RavenGuard (87.0) reads a few points below the 8B guards (Granite 92.1,
Llama 93.3) — its edge is not raw separability but the recall-first operating point: the 8B
guards buy their low FPR (1–3%) by sitting at conservative operating points that discard most
of that recall, while RavenGuard's higher FPR here (8.5) is the flip side of keeping recall
high — the subject of the next section.

### RavenGuard on the full heldout (n=6,800)

| Model | AUROC ³ | F1 | Recall | R@1% FPR ³ | FPR | p50 latency |
|---|---|---|---|---|---|---|
| RavenGuard-Gen (0.8B) | 86.5 | 66.3 | 75.9 | 69.9 | 10.5 | ~372 ms |

³ AUROC and R@1%FPR here are the calibrated `Severity`-token figures — the same score source as
every other table in this card, and what `guardbench` reproduces. Treat them as reference
separability indicators; F1/Recall/FPR (read from the `Severity` line) are the usable
operating-point metrics.

FPR here (10.5%) is on PolyGuard's own benign responses, which include dual-use and borderline
content; it reflects the recall-tuned operating point rather than any particular deployment's
traffic. The p50 latency is the generative moderation call on an H200.

### Over-refusal: real traffic vs. adversarial benchmarks

"False-positive rate" depends entirely on how benign the benign set is:

- **OR-Bench-Toxic** (prompts that read as toxic but are benign): **0.0%** over-block.
- **XSTest** (crafted over-refusal probes): **5.6%** over-block.
- **PolyGuard heldout benign** (includes dual-use and borderline responses): a **6–16%**
  per-language band.

The spread is deliberate: RavenGuard-Gen is tuned for harm recall, which raises
false-positives on adversarial benchmark-benign. How that operating point behaves on a given
deployment's traffic depends on that traffic — measure it before rollout, and calibrate the
per-language threshold to your own false-positive budget.

### Why RavenGuard does not chase the PolyGuard score

The PolyGuard table above rewards a specific behaviour: label its "benign" responses as safe.
But a large share of those responses are **dual-use** — a fluent, detailed answer to a
harmful-adjacent question (how a certain toxin acts on the body; how an exploit class works;
how a scam is structured) that the dataset marks benign because it reads educational. A guard
optimised to score well there learns to *let that content through*.

That is a policy choice disguised as a metric. Consider a concrete case: a detailed,
competent explanation of how to synthesise a controlled substance, framed as "for a
chemistry class." PolyGuard's benign label says *allow it*; a strict enterprise guard says
*flag it*. Counting the flag as a false-positive doesn't make the guard wrong — it makes the
benchmark's boundary more permissive than the deployment's.

You can see the cost of chasing the score in the same tables. The 8–9B guards post the lowest
PolyGuard FPR (1–3%) — and the lowest real recall: 25–56% on ChineseSafe, 32–59% on PolyGuard.
Their low false-positive rate is bought by being lenient on exactly the ambiguous content that
matters. RavenGuard's higher benchmark-FPR is not a capability gap but a deliberate
operating-point choice: it accepts a higher benchmark-FPR to keep recall high, where the 8B
guards sit conservative and discard recall. The choice of operating point is the product. What that
choice costs on real traffic is a property of the traffic, and is left to the deployment to
measure — see `release/REPRODUCE.md` for the harness and `docs/prodsim-v2-results.md` for a
worked measurement on public real-traffic data.

---

## Usage

RavenGuard-Gen ships as a self-contained `trust_remote_code` model (the custom backbone is
bundled in the repo). Weights are byte-faithful to the trained checkpoint. The guard reads a
prompt (or a prompt + response) under the policy prompt below and, in a short greedy decode,
emits a fixed label block:

```
Decision: <allow|block|rewrite|ask_clarification|require_approval|human_review>
Risk: <comma-separated risk names, or none>
Severity: <Safe|Controversial|Unsafe>
Categories: <comma-separated S-codes, or None>
Refusal: <Yes|No>
```

The **binary safe/unsafe verdict** is the generated `Severity` line — this is the deployment
decision. For a soft score (AUROC / threshold tuning) read the calibrated softmax at the
generated `Severity` token: P(Unsafe ∪ Controversial) vs P(Safe). Treat this as a
calibrated-severity read for reference, not a free-threshold ranking score.

```python
import os
os.environ.setdefault("NETIS_AMNIOTA_ATTN_BACKEND", "sdpa")  # see "Runtime notes" below
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained(
    "netis-ai/RavenGuard-gen", trust_remote_code=True,
    torch_dtype="float32").cuda().eval()
```

For the complete, self-contained inference recipe — the exact policy prompt, the greedy
decode, the label parse, and the `Severity`-token calibrated score — see **`reproduce_eval.py`
in this repo** (`Guard.classify`). It runs the model end to end with no `guardbench` install
and no network.

### Runtime notes (please read before running)

- **Attention backend:** set `NETIS_AMNIOTA_ATTN_BACKEND=sdpa`. The default FlashAttention-4
  (CuTeDSL) path raises a `window_size_left` error on GPUs that support only FlashAttention-2
  (e.g. consumer Blackwell / RTX 5090, sm_120). SDPA is portable and numerically identical.
- **Batch size 1 only, for now.** The bundled `forward` does not yet consume `attention_mask`,
  so a left-padded batch would be scored **incorrectly and silently**. Moderate one sequence
  at a time until the batched (`attention_mask` / KV-cache / `generate`) path is released.
- Runtime dependencies beyond `transformers`: `torch`, `tiktoken`, `rustbpe`, `filelock`.

## Intended use

RavenGuard-Gen performs input and output moderation: run it as a prompt filter before the
main model, as an end-of-response check before a reply reaches the user, or both. It suits
multilingual input/output moderation and end-of-turn checks, including Chinese-, Arabic-,
Spanish-, Portuguese-, Hindi-, and Thai-heavy workloads. For latency-sensitive streaming
deployments where harmful content must be interrupted mid-generation, pair it with the
companion RavenGuard-Stream model (released separately).

## Operating notes

- RavenGuard is a probabilistic classifier. Operating thresholds are calibrated per
  language and should be re-calibrated to the target false-positive budget of each
  deployment.
- Validate tokenisation, recall, and false-positive rates on the deployment's own language
  varieties, code-switching patterns, and regional vocabulary. Declared language support
  does not remove the need for domain-specific calibration and monitoring.
- Cross-model figures in this card are computed on shared public benchmarks (ChineseSafe
  n=500, PolyGuard response n=2,039) with identical sample sets and gold labels.

## Evaluation methodology

All figures come from a reproducible harness (`guardbench`) with an `EVAL_ONLY` firewall
between training and test corpora, per-language threshold calibration, and threshold-free
capability metrics (AUROC, Recall@FPR). Cross-model comparisons are computed on identical id
sets with identical gold labels. See `docs/ravenguard-technical-report.md` for the full
protocol.

## Citation

```bibtex
@misc{ravenguard2026,
  title  = {RavenGuard: Multilingual Safety Guards for LLM Agents},
  author = {netis},
  year   = {2026},
  url    = {https://huggingface.co/netis-ai/RavenGuard-gen}
}
```
