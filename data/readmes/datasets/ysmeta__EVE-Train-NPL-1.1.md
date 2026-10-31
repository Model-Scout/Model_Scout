---
license: apache-2.0
task_categories: [image-to-text, visual-question-answering]
language: [vi, ko, en]
size_categories: [1K<n<10K]
tags: [synthetic, document-understanding, key-information-extraction, ocr, npl]
---

# EVE-Train-NPL-1.1

Synthetic scanned-document pages with gold key-information-extraction labels for
Vietnamese non-performing-loan collateral paperwork. **Every value is fabricated** —
no real borrower, property, contract or person appears. Pages are drawn
programmatically, so labels are exact by construction rather than annotated.

Training a QLoRA adapter on this corpus moved field exact-match accuracy on
**genuine** VAMC scans from 64.0% to **81.4%**
([ysmeta/EVE-OCR-1.0-NPL](https://huggingface.co/ysmeta/EVE-OCR-1.0-NPL)).

## What changed from 1.0

Version 1.0 improved the average but **made one real page worse** (69.0% -> 65.5%).
That page prints addresses abbreviated (`Q. Tân Phú`, `TP.HCM`); 1.0 only ever
spelled the administrative prefix out (`huyện …`, `tỉnh …`), so the adapter learned
to normalise toward the single form it had seen.

Version 1.1 adds variation drawn from features observed in real documents:

| Added | Seen in |
|---|---|
| Abbreviated address forms `P.` `X.` `TT.` `Q.` `H.` `T.` `TP.` (~39% of pages) | the regressed page |
| Municipality addresses (`TP.HCM`, `TP. Hà Nội` …) replacing province/district | real filings |
| Currency unit varies: `VNĐ` / `đồng` / `VND` / `đ` | differs per document |
| Numbered appendix titles (`PHỤ LỤC 1:`) | one real page |
| Three term-of-use phrasings: a date, `tháng MM/YYYY`, `Lâu dài` | across pages |
| Mortgage contracts with **no number**, only a date — gold value `null` (~25%) | one real page |
| Certificate numbers containing a space (`CV 366117`) | one real page |
| Two more credit-contract number families | real filings |

Result on the previously regressed page: **65.5% -> 79.3%**, above its untuned
score. Every other page improved as well. 1,500 -> 1,800 pages.

## Contents

- 1,800 JPEG pages — Vietnamese 1,080 / Korean 360 / English 360
- `metadata.jsonl` — 30 schema fields per page, plus `lang` and `split_role`
- `vamc_gen.py` — the generator, so the corpus is reproducible and extensible

`split_role` marks 60 pages (20 per language) held out of training and used only
to check whether adapting to Vietnamese degraded the other languages. It did not:
Korean rose 63.3% -> 92.2%, English 75.0% -> 91.1%.

## Failure modes the generator deliberately induces

| Observed in real scans | How it is reproduced |
|---|---|
| One contract's figures mixed with the totals row | 1-3 contract rows plus an always-present totals row |
| Absent fields filled with junk instead of `null` | fields randomly omitted, gold value `null` |
| Handwritten entries misread (`1406` read as `146`) | handwriting font in dotted blanks, per-glyph rotation and jitter |
| Text lost under the company seal | semi-transparent red seal composited over body text |
| Vietnamese number formats altered | `.` thousands / `,` decimal preserved in gold |
| Low-quality capture | skew, blur, downsample to 150-200 DPI, JPEG artifacts |
| Vertically merged table cells | merged mortgage/status columns across asset rows |

## Load

```python
from datasets import load_dataset
ds = load_dataset("ysmeta/EVE-Train-NPL-1.1")
```

## Limitations

- One document family: VAMC valuation-request appendices.
- The generator draws clean geometry then degrades it. Real scanner artefacts,
  paper texture and print bleed are approximated, not simulated. A 21 pp gap
  remains between held-out synthetic (93.3%) and real pages (81.4%).
- Korean and English variants reuse the Vietnamese layout with translated labels.
  They are a language-robustness control, not authentic local paperwork.
- **Evaluate on real documents.** Training and evaluating on synthetic data alone
  measures nothing.
