---
license: apache-2.0
language: [ko]
tags: [rag, korean, evaluation, hallucination, instruction-following]
pretty_name: Korean Contract Derivation Benchmark
size_categories: [n<1K]
task_categories:
- question-answering
- text-generation
---

# Korean Contract Derivation Benchmark

A model that derives a discount and a unit-price total without being told to will still return the
**VAT-inclusive figure verbatim** when asked for the contract amount — and a generic instruction to
"compute the relation" does not fix it. This benchmark isolates that.

## The finding

240 synthetic Korean procurement summaries. Half state the contract amount directly among distractor
figures (`disambiguate`); half state it only as a relation the model must compute (`derive`), in three
flavours: VAT-inclusive ÷1.1, list price × 0.8 after a stated 20% discount, and unit price × quantity.
Three system prompts, two model arms, one serving run.

Accuracy by derivation type (n=40 per cell):

| prompt | disambiguate | discount | unit × qty | **VAT** |
|---|---|---|---|---|
| none | 1.000 | 0.83–0.90 | 0.93–0.98 | **0.000** |
| generic ("if stated as a relation, compute it") | 1.000 | 0.98–1.00 | 1.000 | **0.000** |
| VAT-specific ("divide by 1.1") | 1.000 | 0.95–1.00 | 0.95–0.98 | **0.85–0.90** |

Ranges span the two arms (bf16 and a 4-bit build); both behave the same way.

**The model is not bad at deriving.** With no instruction at all it handles discount and unit-price
arithmetic 83–98% of the time. Only VAT collapses, and it collapses completely. ÷1.1 is not harder than
×0.8 or ×2, so arithmetic is not the explanation.

**The generic instruction is worth nothing here.** It lifts the cases that already worked and leaves VAT
at zero. What we think is happening: `부가세 포함 997,700,000원` ("997,700,000 won including VAT") is such
a standard phrase in Korean contracts that the model reads the number as *the answer*, not as an input to
a calculation — so a prompt conditioned on "the value is not stated directly" never fires.

## Why this shape of failure is dangerous

It is narrow, total, and invisible next to its neighbours. If your eval set happens to contain only
discount-style derivations you will conclude derivation works. We drew exactly that wrong conclusion
twice before widening the set from one derivation type to three.

The practical implication for Korean-document RAG: **a single generic instruction is not a product asset.**
What is needed is a lexicon of *answer-masquerading phrases* per domain, each with its own rule. Which
phrases those are differs by document type, so it is a spec item, not prompt tuning.

## Contents

- `data/cases.jsonl` — 240 cases: `document` (contract summary, padding stripped), `question`,
  `answer_krw`, `mode` (`disambiguate` | `derive:vat` | `derive:discount` | `derive:unit`), `distractors`.
- `data/results.jsonl` — measured accuracy per (arm, prompt variant, mode).
- `data/prompts.json` — the three system prompts verbatim.

Every derived figure is exactly invertible from the document (997,700,000 ÷ 1.1 = 907,000,000), and the
answer never appears verbatim in a `derive` document — verified programmatically before the run.

## Method

vLLM 0.27.1, greedy decoding, one serving session, identical config across arms, model path the only
difference. Scored by string/numeric match against `answer_krw`. Documents are padded to the target
context length by the harness at eval time; the padding is filler and is stripped here.

## Limits

- **Synthetic.** These are generated documents, not real contracts. The distribution of
  answer-masquerading phrases in actual Korean procurement paperwork is unmeasured.
- **The three derivation types are not equally hard** — unit × quantity uses small integers and is the
  easiest. Compare prompt variants *within* a type, not accuracies *across* types.
- **n=40 per cell.** One item is 0.025. Do not read small differences as trends.
- One run, one model family.
- The VAT-specific prompt hands the model the formula. Its 0.85–0.90 shows that instructing works, not
  that the model knows the rule unprompted.

## Collection

Part of [Evals & Reproducibility](https://huggingface.co/collections/ThakiCloud/evals-and-reproducibility-6a9e6effa3c3b027077af99e).
