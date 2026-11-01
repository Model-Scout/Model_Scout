---
pretty_name: DECKEDIT-BENCH
license: cc-by-nc-4.0
language:
  - en
  - ko
tags:
  - powerpoint
  - pptx
  - instruction-following
  - document-editing
  - agents
  - benchmark
size_categories:
  - n<1K
task_categories:
  - other
configs:
  - config_name: prompts
    data_files: prompts.jsonl
---

# DECKEDIT-BENCH

A benchmark for **instruction-guided PowerPoint (`.pptx`) editing**. It pairs
28 real-world presentation decks with **183 natural-language editing
instructions**, organized along a **Cell × Action × Target** taxonomy and three
deck-length tiers (Short / Medium / Long).

Each instance is a `(deck, instruction)` pair: a system reads the instruction,
edits the deck, and the before/after decks are compared. The benchmark stresses
locating the right targets, decomposing multi-step instructions, compressing
repeated edits into a pattern, and **not damaging what should stay untouched**.

## Contents

```
DECKEDIT-BENCH/
├── decks/{Short,Medium,Long}/*.pptx   # 28 source decks (≤10 / 11–30 / >30 slides)
├── prompts.jsonl                       # 183 editing instructions (one JSON / line)
├── taxonomy.json                       # cell + action definitions, 14 reusable templates
├── deck_info.json                      # per-deck metadata (size, language, topic, visuals)
├── DATASHEET.md                        # datasheet-for-datasets (composition, collection, cleaning)
├── TAXONOMY.md                         # Cell × Action × Target taxonomy + template catalog
├── fonts/S-Core_Dream_OTF.zip          # required font, official release, unmodified
├── THIRD_PARTY_NOTICES.md              # image/figure/font provenance & attributions
├── LICENSE                             # data license (CC BY-NC 4.0)
└── CITATION.cff
```

## Prompt format (`prompts.jsonl`)

One JSON object per line:

```json
{"deck_id":"02_UTI","id":"02_UTI-01","cell":"PS","ops_per_slide":1,
 "actions":["REPLACE"],"derived_from":"U-01",
 "intent":"…what this instance tests…","text":"…instruction sent to the system…"}
```

- `text` — the instruction handed to the editing system.
- `cell` ∈ `{ES, EC, PS, PC}` · `actions` ⊆ `{ADD, DELETE, REPLACE, SLIDE}`.
- `derived_from` — a universal template id (`U-xx`, see `taxonomy.json`) or `"deck-specific"`.

See **TAXONOMY.md** for definitions.

## Quickstart

```python
import json
prompts = [json.loads(l) for l in open("prompts.jsonl", encoding="utf-8")]
info = {d["id"]: d for d in json.load(open("deck_info.json", encoding="utf-8"))["decks"]}

p = prompts[0]
deck_path = info[p["deck_id"]]["path"]      # e.g. "decks/Short/01_CausalAGI.pptx"
# 1. open deck_path, 2. apply p["text"] with your system, 3. diff before/after.
```

## Coverage

| | total | breakdown |
|---|---|---|
| Decks | **28** | Short 9 · Medium 12 · Long 7 |
| Prompts | **183** | Short 54 · Medium 81 · Long 48 |
| Cells | — | ES 17 · EC 57 · PS 87 · PC 22 |
| Deck languages | — | en 21 · ko 7 (translate targets also span ja/fr/es/zh) |

Full Cell × Action matrix and known imbalances are in **DATASHEET.md**.

## Notes on the decks

- **Full resolution.** The `.pptx` files keep original-resolution media (~1 GB
  total) and are distributed via Git LFS / the dataset host.
- **Privacy.** Every deck was scrubbed of author/coauthoring/comment PII; see
  **DATASHEET.md → Preprocessing/cleaning**.
- **Provenance.** Embedded figures in paper-review decks, and the replacement
  images in `11_FourthIndustryStartup`, are credited in **THIRD_PARTY_NOTICES.md**.

## Fonts

**Required.** Install **S-Core Dream** to edit `decks/Long/01_Transformer.pptx` and
`decks/Long/06_Algorithm.pptx`. It is included at `fonts/S-Core_Dream_OTF.zip`
(source: https://s-core.co.kr/company/font/). See **THIRD_PARTY_NOTICES.md** for its license.

**Recommended.** Other fonts referenced by the decks are not required. Without them,
PowerPoint substitutes similar fonts, and decks still open, edit, and score normally, but
line breaks and text measurements may differ from the original rendering.

| Fonts | Decks |
|---|---|
| Pretendard | Long/02, Long/04, Short/07 |
| Nanum Gothic, NanumSquare, NanumSquareRound | Long/04, Long/07, Medium/01 |
| Source Han Sans KR, Raleway | Long/06 |
| Poppins, Nobile, Alexandria | Short/08 |
| Gmarket Sans, KoPub Dotum | Long/04, Medium/09 |
| HCR Dotum, HCR Batang | Long/01, Medium/01 |
| Aptos (Microsoft 365) | Medium/01, 07, 10, Short/03, 04, 08 |

Rule-based scoring reads the OOXML directly and does not depend on installed fonts.

## License & citation

Data is released under **CC BY-NC 4.0** (see `LICENSE`). If you use
DECKEDIT-BENCH, please cite it — see `CITATION.cff`.
