---
language:
- en
- ja
- ko
- zh
task_categories:
- translation
tags:
- wmt24pp
- machine-translation
- multilingual
- reversed-directions
size_categories:
- 1K<n<10K
---

# WMT24++ Parallel Mix (Direction-Flipped)

- Source dataset dir: `/Users/inertia/Desktop/preprocessing/processed/wmt24pp_parallel_80_20`
- Transformation: `direction flip per row (source/target swap)`
- Pair+sample_key overlap with source: `0`
- Primary(stats): `{'en->ko': 450, 'ko->en': 449}`
- Auxiliary(flipped): `ja->en, en->ja, zh->en, en->zh`
- Target primary ratio: `0.8000`
- Achieved primary ratio: `0.7998`
- Tag template: `<{tgt_upper}>`
- Text template: `{src_tag} {source} {tgt_tag} {target}`

## Columns
`id, dataset, pair_config, pair, source_lang_iso, target_lang_iso, lp, domain, document_id, segment_id, sample_key, is_bad_source, tag, src_tag, tgt_tag, source_text, target_text, text, content`