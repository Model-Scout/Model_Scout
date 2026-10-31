---
license: apache-2.0
task_categories: [image-to-text, visual-question-answering]
language: [vi, ko, en]
size_categories: [1K<n<10K]
tags: [synthetic, document-understanding, key-information-extraction, ocr, npl]
---

# EVE-Train-NPL-1.0

Synthetic scanned-document images with gold key-information-extraction labels,
built to train a vision-language model on Vietnamese non-performing-loan (NPL)
collateral appraisal paperwork.

**Every value in this dataset is fabricated.** No real borrower, property,
contract or person appears here. Images are drawn programmatically, so the gold
labels are exact by construction rather than annotated by hand.

## Why it exists

Real VAMC appraisal letters are scanner output with no text layer at all.
Measuring a Tesseract baseline and a Qwen2.5-VL-7B zero-shot baseline on genuine
documents showed the hard part is not character recognition — the base model
already reproduces 92.6% of gold values somewhere in its output — but **field
discipline**: returning exactly the value a schema field asks for, and returning
`null` when a field is absent. Exact-match field accuracy was 51.9%.

This dataset reproduces the specific failure modes that were measured:

| Observed failure | How the generator induces it |
|---|---|
| Row confusion — one contract's figures mixed with the totals row | 1-3 credit-contract rows plus an always-present totals row |
| Absent fields filled with junk instead of `null` | Fields randomly omitted; gold value is `null` |
| Handwritten entries misread (`1406` read as `146`) | Handwriting font in dotted blanks, per-glyph rotation and baseline jitter |
| Text lost under the company seal | Semi-transparent red seal composited over body text at random positions |
| Vietnamese number formats altered | `.` thousands separator and `,` decimal separator preserved in gold |
| Low-quality capture | Skew, blur, downsampling to 150-200 DPI, JPEG artifacts |

## Contents

- 1,500 JPEG page images: Vietnamese 900 / Korean 300 / English 300
- `metadata.jsonl` — 30 schema fields per image, plus `lang` and `split_role`
- `vamc_gen.py` — the generator, so the corpus can be reproduced or extended

`split_role` marks 60 images (20 per language) held out of training and used only
to check whether adapting to Vietnamese degraded the other two languages.

## Schema

Document metadata, credit-contract totals, collateral registry details, address
components, and optional amounts. Field names are identical across languages;
only the values change language. Fields absent from a document are `null`.

## Load

```python
from datasets import load_dataset
ds = load_dataset("ysmeta/EVE-Train-NPL-1.0")
```

## Limitations

- Layout is modelled on one document family (VAMC valuation-request appendices).
- The generator draws clean geometry then degrades it; genuine scanner artefacts,
  paper texture and print bleed are only approximated.
- Korean and English variants reuse the Vietnamese layout with translated labels.
  They are a language-robustness control, not authentic local paperwork.
- Evaluation of models trained on this data should use real documents. Training
  and evaluating on synthetic data alone measures nothing.
