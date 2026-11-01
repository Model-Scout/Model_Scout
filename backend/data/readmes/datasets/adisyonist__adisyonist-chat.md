---
language:
- en
- tr
- bn
- ca
- hr
- cs
- da
- nl
- fi
- fr
- de
- el
- gu
- he
- hi
- hu
- id
- it
- ja
- kn
- ko
- ms
- ml
- mr
- nb
- or
- pl
- pt
- pa
- ro
- ru
- zh
- sk
- sl
- es
- sv
- ta
- te
- th
- uk
- ur
- vi
license: unknown
task_categories:
- text-generation
tags:
- sft
- chat
- restaurant
- multilingual
- synthetic
pretty_name: Adisyonist Chat SFT Corpus
---

# Adisyonist Chat SFT Corpus

Synthetic supervised fine-tuning corpus for a restaurant-management chat assistant
(menu, table/bill, stock, staff/shift, reservation, and sales-analytics actions,
plus general chit-chat and refusal cases).

- **532,856 rows** across **43 languages**, 12,392 rows each, all sharing the same
  distribution of 150 (agent, answer-template) groups.
- Format: JSONL, one `{"messages": [...], "lang": ..., "agents": [...]}` object per line.
  - `messages`: a two-turn `user`/`assistant` chat pair.
  - `lang`: ISO-ish language code (`tr`, `en`, `zh-Hans`, `zh-Hant`, ...).
  - `agents`: the backend tool/function call sequence the assistant response corresponds to
    (empty list for chit-chat / refusal rows).
- `{apiPlaceholder}`-style tokens inside assistant answers (e.g. `{totalSales}`,
  `{currencyCode}`) are intentional — they're backend template variables meant to be
  filled in by the application at runtime, kept in English/camelCase across every
  language on purpose.

Generated from a hand-built Turkish seed corpus, expanded via a language-agnostic
templating engine and localized per language (translated templates + entity pools:
names, menu items, categories, etc.), not machine-translated row-by-row.

Known limitation: in heavily inflected languages (e.g. Finnish, Hungarian, Russian,
Polish), inserted slot values (names, items, table references) are not grammatically
declined, which can produce minor grammatical roughness in a small fraction of rows.
