---
license: odc-by
language: [ko, en, zh, ru, ja]
pretty_name: clm_prod 5-lang monolingual BACKBONE sample (mC4)
tags: [clm-prod, byte-vocab, multilingual, backbone, sample]
---

# clm-backbone-5lang-sample

clm_prod 3B/7B BACKBONE corpus (step 2 DATA PREP). A **bounded streaming SAMPLE** —
NOT the full 60B-token pretrain set (that is the step 3 H100 fire).

- **Source**: `allenai/c4` (mC4 multilingual), configs `ko/en/zh/ru/ja`
- **License**: ODC-BY (Open Data Commons Attribution)
- **real_fraction**: 1.0 — every line is real downloaded web text. NO synthesis, NO LLM generation.
- **Preferred set blocked**: `uonlp/CulturaX` is GATED; the token has no data access (403 on stream) → fell back to c4.
- **Format**: plain newline corpus, one text line per sample, byte-vocab V=256 (UTF-8). clm_prod reads it via `CLM_PROD_CORPUS`.
- **Balance**: 4000 docs/language, round-robin interleaved (5-way balanced).

| field | value |
|---|---|
| total lines | 20000 (4000 x 5) |
| total bytes | 67,733,426 (~67.7 MB) |
| ko bytes | 16,679,968 |
| en bytes | 7,739,055 |
| zh bytes | 9,317,034 |
| ru bytes | 14,529,169 |
| ja bytes | 19,468,200 |
| max line bytes | 8192 |
| corpus sha256 | 7cc86c9afd5347920fb40be48d8f22b17ca2f72e04ea172f2496b13f42df3b04 |

## clm_prod sanity (F-CLM-PROD-DESCENT)
```
corpus: clm_backbone_5lang_sample.txt  (67733426 bytes, V=256)
windows: 8/8  (T=24 stride=8466675)
epoch-1 mean CE = 4.747
epoch-12 mean CE = 1.49606
F-CLM-PROD-DESCENT = 1
PASS — real-corpus mean CE descends under int4 envelope
```

Files: `clm_backbone_5lang_sample.txt` (corpus), `clm_backbone_5lang.corpus.kosmos` (manifest), `clm_backbone_5lang.meta.json` (provenance).
