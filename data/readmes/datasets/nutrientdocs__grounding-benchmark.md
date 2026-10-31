---
license: cc-by-sa-4.0
pretty_name: Grounding Benchmark (document value grounding / NLI)
task_categories:
- text-classification
- zero-shot-classification
language:
- en
- de
- fr
- es
- it
- pt
- nl
- ru
- zh
- ja
- ar
- hi
- tr
- vi
- ko
tags:
- grounding
- hallucination-detection
- nli
- table-question-answering
- document-ai
- fact-verification
size_categories:
- 100K<n<1M
configs:
- config_name: en
  data_files:
  - split: test
    path: en.jsonl
- config_name: multi
  data_files:
  - split: test
    path: multi.jsonl
---

# Grounding Benchmark

**Is a claim actually supported by the document it cites?** This benchmark evaluates *value grounding* —
whether a short hypothesis (a number, date, or fact) is entailed by a premise drawn from a real document
(financial tables, filings, Wikipedia tables, prose evidence). It is a binary NLI task framed for the
document-AI setting, with a deliberate focus on the case general NLI models fail: **numeric and date
grounding**, and **hard negatives** that are lexically close but factually wrong (adjacent cell, wrong
period, ×1000 scale error, sign flip, transposed digits).

It powers the [Grounding leaderboard](https://huggingface.co/spaces/nutrientdocs/grounding-leaderboard),
backs the open [`grounding-en`](https://huggingface.co/nutrientdocs/grounding-en) model, and you can try
grounding live in the [demo](https://huggingface.co/spaces/nutrientdocs/grounding-demo).

A fixed, held-out **evaluation** benchmark (test only — not for training), stratified so each reported
facet is well-populated and, for `multi`, no single language dominates.

| Config | Rows | Languages | Contents |
|---|---:|---|---|
| `en`    | 5,000  | English | financial tables (SEC/XBRL), Wikipedia table facts, prose evidence |
| `multi` | 8,421  | 40 (≤15% each) | the EN sources plus native + machine-translated multilingual grounding |

```python
from datasets import load_dataset
en    = load_dataset("nutrientdocs/grounding-benchmark", "en",    split="test")
multi = load_dataset("nutrientdocs/grounding-benchmark", "multi", split="test")
```

## Schema

Each row is a `(premise, hypothesis)` pair with a binary label and facet tags used for sliced scoring:

| field | meaning |
|---|---|
| `premise` | the document context (a rendered table, or prose evidence) |
| `hypothesis` | the claim to verify against the premise |
| `label` | `1` = supported / entailed, `0` = not supported |
| `value_type` | `number` / `date` / `string` / `null` — the kind of value being grounded |
| `premise_shape` | `table` / `prose` / `mixture` |
| `inference` | `verbatim` / `selection` / `arithmetic` / `null` — how much reasoning the grounding needs |
| `hyp_style` | `template` / `natural` / `native` / `qa` — how the hypothesis is phrased |
| `source` | originating dataset (a `/synth` suffix marks synthesized hard negatives) |
| `meta` | provenance as a JSON string — `json.loads` it (doc id, perturbation kind, language, …) |

## How to score

The task is ranking positives above negatives, so the headline metric is **ROC-AUC**, reported overall
and **per facet** (the per–`value_type` AUC — especially `number` — is the number that matters). A
reference scorer + submission instructions live in the benchmark repo:

```bash
python benchmark/score.py --model <your-model-or-hub-id> --config en
# emits a results JSON; open a PR / HF discussion to appear on the leaderboard
```

See [`SUBMISSION.md`](./SUBMISSION.md) for the exact
submission format.

## License & attribution

This benchmark is released under **CC-BY-SA-4.0**. It aggregates multiple upstream
datasets; per-source licenses and citations are in
[`ATTRIBUTION.md`](./ATTRIBUTION.md).

## About the author

<a href="https://nutrient.io/">
  <img src="https://avatars2.githubusercontent.com/u/1527679?v=3&s=200" height="80" />
</a>

This project is maintained and funded by [Nutrient](https://nutrient.io/) - The deterministic document infrastructure enterprises run their highest-stakes workflows on: replayable output, clear exceptions, and full audit trails on the messy, regulated documents where AI alone breaks.