---
language:
- en
- ja
- ko
- zh
task_categories:
- translation
tags:
- flores
- machine-translation
- multilingual
- reversed-directions
size_categories:
- 1K<n<10K
---

# FLORES Parallel Mix (Direction-Flipped)

- Source dataset dir: `/Users/inertia/Desktop/preprocessing/processed/flores_parallel_80_20`
- Transformation: `direction flip per row (source/target swap)`
- Pair+sample_key overlap with source: `0`
- Primary: `en<->ko` (kept disjoint by inherited sample assignment)
- Auxiliary(flipped): `jpn_Jpan->eng_Latn, zho_Hans->eng_Latn, zho_Hans->jpn_Jpan, jpn_Jpan->zho_Hans, kor_Hang->zho_Hans, kor_Hang->jpn_Jpan`
- Target primary ratio: `0.8000`
- Achieved primary ratio: `0.8001`
- Tag template: `<{tgt_upper}>`
- Text template: `{src_tag} {source} {tgt_tag} {target}`

## Columns
`id, dataset, pair_config, pair, source_lang, target_lang, source_lang_iso, target_lang_iso, split, flores_id, sample_key, domain, topic, tag, src_tag, tgt_tag, source_text, target_text, text, content`