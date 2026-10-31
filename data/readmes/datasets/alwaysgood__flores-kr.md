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
size_categories:
- 1K<n<10K
---

# FLORES Parallel Mix

- Primary(all): `eng_Latn->kor_Hang, kor_Hang->eng_Latn`
- Primary mode: `disjoint_halves`
- Auxiliary(sampled, no oversampling): `eng_Latn->jpn_Jpan, eng_Latn->zho_Hans, jpn_Jpan->zho_Hans, zho_Hans->jpn_Jpan, zho_Hans->kor_Hang, jpn_Jpan->kor_Hang`
- Target primary ratio: `0.8000`
- Achieved primary ratio: `0.8001`
- Tag template: `<{tgt_upper}>`
- Text template: `{src_tag} {source} {tgt_tag} {target}`
- Normalize doubled quotes: `True`
- Strip control chars: `True`
- Runtime note: `facebook/flores` currently needs `datasets<4` in this script path.

## Columns
`id, dataset, pair_config, pair, source_lang, target_lang, source_lang_iso, target_lang_iso, split, flores_id, domain, topic, tag, src_tag, tgt_tag, source_text, target_text, text, content`