---
license: mit
language:
  - ko
tags:
  - anima
  - corpus
  - byte-level
  - sns
  - register
size_categories:
  - 10K<n<100K
---

# anima-corpus-ko-sns

anima 4-cell register corpus — **ko-SNS — Korean casual/social conversational voice**.

Part of the anima production chat corpus = **2 languages (ko·en) × 2 registers
(general·SNS) = 4 cells** (a_chat_registers). This is one cell.

## composition (language-verified)
- **language purity:** 100.0% ko (re-audited; non-target lines dropped)
- **size:** 6.18 MB · 47994 lines
- **cleaning:** per-line language classification (script + stopword), de/es/fr/ja/zh
  dropped, exact-duplicate dedup, broken/short-line drop

## language audit (provenance)
ko-SNS base (persona_sns_corpus) was already clean **100% ko**; ko lines from the 5lang persona file + the MIT/Apache ko-chat datasets were ko-verified and merged, deduped → **100.0% ko**, 4.18MB → 6.18MB.

Method: script/charset + stopword-fingerprint per-line classifier (torch-free,
deterministic). Audit tool + reproduce script: `state/clm303_clean_corpus/`
(`langaudit.py` measures composition, `build_corpus.py` rebuilds this cell).
*(Measured by the anima clm303-retrain build, 2026-06-24; cross-referenced by the
governance rule `a_chat_registers` as the precedent that mandates per-cell language
verification.)*

## sources (repo · license)
| source | license |
|--------|---------|
| anima persona_sns_corpus (ko) | as-authored |
| NLPBada/korean-persona-chat-dataset | MIT |
| JaeJiMin/korean_chat_friendly | MIT |
| jojo0217/korean_safe_conversation | Apache-2.0 |

## sha256
```
c836e9fc948e56303b5edd3690fdb146dea90fc8748c3a83967d937fff6b4abe  anima-corpus-ko-sns.txt
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
