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
size_categories:
- 1K<n<10K
---

# WMT24++ Parallel Mix

- Primary(all): `en->ko, ko->en`
- Primary mode: `disjoint_halves`
- Auxiliary(sampled, no oversampling): `en->ja, ja->en, en->zh, zh->en`
- Target primary ratio: `0.8000`
- Achieved primary ratio: `0.7998`
- Tag template: `<{tgt_upper}>`
- Text template: `{src_tag} {source} {tgt_tag} {target}`
- Normalize doubled quotes: `True`
- Strip control chars: `True`
- Drop bad source: `True`
- Drop canary: `True`
- Drop @user handles: `True`
- Drop one-word sentences: `True`

## Columns
`id, dataset, pair_config, pair, source_lang_iso, target_lang_iso, lp, domain, document_id, segment_id, sample_key, is_bad_source, tag, src_tag, tgt_tag, source_text, target_text, text, content`