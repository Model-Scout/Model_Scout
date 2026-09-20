---
license: apache-2.0
base_model: Qwen/Qwen3.8-27B
language:
- ko
pipeline_tag: text-generation
tags:
- korean
- style-alignment
- vocabulary-pruning
- qwen
base_model_relation: finetune
library_name: transformers
---

# Qwen3.8-27B-Human-KO

A full-weight checkpoint that adapts Qwen3.8-27B for Korean conversation along two axes.

1. **Style alignment** — trained on an in-house synthetic corpus and merged into the weights.
   The free-generation (no system prompt) distribution shifts from a bullet-list rate of
   97.5% → **2.0%**, and a median length of 1,326 characters → **220 characters**. The default
   output is short, flowing Korean prose.
2. **Hygiene (CJK output suppression)** — blocks the output path for Chinese-word and kana
   tokens at the weight level. Single-character Hanja used for Korean Hanja glosses (e.g.
   개항(開港), gaehang, "opening of a port") are preserved.

## Measurements (2026-09-01, temperature and conditions stated)

| Axis | base | This model |
|---|---|---|
| Human-likeness pairwise (LLM judge, n=175) | 1.1% win | **94.9% win** (tie 4.0%, position-swap consistency 96%) |
| Free-generation bullet-list rate (n=200) | 97.5% | 2.0% |
| CJK contamination, T=0, n=3,369 | 2.55% | **0.33%** (true error rate 0.24%) |
| HumanEval (paired n=58) | 93.85% | +3.03pp |
| Instruction following | 81% | −3.0pp (statistically equivalent) |
| KMMLU (n=300) | 55.67% | −2.0pp — **minimum detectable difference is 11.4pp, so no verdict is possible** |

Honest caveats:

- The pairwise judge (Qwen3.8-27B, T=0, position-swapped) has not completed human-label
  calibration (P1.5). The figures above are "win rate on the judge's axis," not human
  evaluation itself.
- The KMMLU row is not "no regression" — it is "a regression on the order of −1pp cannot be
  detected with this sample."
- The floor for CJK contamination is not 0. A rare Hanja character with no standalone token
  in the vocabulary can be assembled via byte fallback (the measured residual 0.24% is mostly
  the single-character class kept for gloss preservation).

## Usage

```python
from vllm import LLM
llm = LLM(model="ThakiCloud/Qwen3.8-27B-Human-KO", dtype="bfloat16", trust_remote_code=True)
```

The tokenizer, vocabulary size, and architecture are identical to base (standard load). The
model can **read** Hanja but **cannot generate** Chinese-word tokens.

## Limitations

- The default tendency is toward short answers. If you need a long, structured document,
  specify length and format in the prompt.
- The measurements above center on the Korean conversation axis. The English and math axes
  have not been measured with a sufficient sample.
- The safety axis inherits base's alignment as-is (no separate safety training).

## License

Apache-2.0 (base: Qwen/Qwen3.8-27B). Distributed together with `LICENSE`, `NOTICE`, and
`DATA_PROVENANCE.md`.

## Paper

Off-Target Effects of Response-Style Alignment in a Korean 27B Language Model — [arXiv:2609.11291](https://arxiv.org/abs/2609.11291)

The style alignment behind this line also moved two behaviors nobody trained for: abstention on ambiguous social questions (KoBBQ) and unprompted disclosure in securities guidance. Both moved through the **emission policy** — how often the model answers and how much it says — rather than through what it says when it does answer. Holding prompts, recipe, data volume and serving fixed and changing only the training target, three style seeds moved answer rate one way and three neutral seeds moved it the other (observed ranges do not overlap). Read this card's numbers with that in mind.
