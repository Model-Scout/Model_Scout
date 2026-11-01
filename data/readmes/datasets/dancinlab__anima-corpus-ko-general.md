---
license: odc-by
language:
  - ko
tags:
  - anima
  - corpus
  - byte-level
  - general
  - register
size_categories:
  - 100K<n<1M
---

# anima-corpus-ko-general

anima 4-cell register corpus — **ko-일반 (general) — Korean web/wiki prose**.

Part of the anima production chat corpus = **2 languages (ko·en) × 2 registers
(general·SNS) = 4 cells** (a_chat_registers). This is one cell.

## composition (language-verified)
- **language purity:** 100.0% ko (re-audited; non-target lines dropped)
- **size:** 60.00 MB · 340512 lines
- **cleaning:** per-line language classification (script + stopword), de/es/fr/ja/zh
  dropped, exact-duplicate dedup, broken/short-line drop

## language audit (provenance)
source is single-language ko (FineWeb-2 kor_Hang); range-read raw .txt, kept only ko lines (script-detected), deduped → **100.0% ko** (re-audited).

Method: script/charset + stopword-fingerprint per-line classifier (torch-free,
deterministic). Audit tool + reproduce script: `state/clm303_clean_corpus/`
(`langaudit.py` measures composition, `build_corpus.py` rebuilds this cell).
*(Measured by the anima clm303-retrain build, 2026-06-24; cross-referenced by the
governance rule `a_chat_registers` as the precedent that mandates per-cell language
verification.)*

## sources (repo · license)
| source | license |
|--------|---------|
| dancinlab/anima-corpus-ko-fineweb2-broad → FineWeb-2 kor_Hang | ODC-BY |

## sha256
```
19e6ac9e34d19fb66114ead146cdd0c44f4c55d49b1515f0bcffe65b5b1c5b43  anima-corpus-ko-general.txt
```

## role in the 4-cell register
| cell | language | register |
|------|----------|----------|
| anima-corpus-ko-general | ko | general |
| anima-corpus-en-general | en | general |
| anima-corpus-ko-sns | ko | SNS |
| anima-corpus-en-sns | en | SNS |



## why this rebuild
The prior "en" cells were silently 5lang mixtures (only ~20% en — de/es/fr/ko
contamination) and a single 4MB cell was the entire effective training corpus
(~120× repetition = memorization). These clean cells fix both: every cell is
language-verified, and training uses **size-proportional sampling** so per-cell
repetition is uniform (no small cell is over-repeated).
