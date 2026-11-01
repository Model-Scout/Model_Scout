# Adaption Uncharted Jejueo Corpus (jje)

Jejueo (jje) — 255 parallel jje-ko pairs, 4 Wikimedia, UNESCO endangered

Jejueo+ v1.6 is a multi-source, openly licensed corpus for Jejueo (제주어, ISO 639-3: jje) — a UNESCO critically endangered language spoken on Jeju Island, Korea. It integrates FOUR Wikimedia properties (Incubator, Wiktionary, Wikisource, Wikipedia) — nine sub-sources — with rigorous per-record attribution, Datasheet-for-Datasets-style documentation, and PUBLISHED empirical baseline evaluations on six 2024-2026 frontier LLMs.

Built for The Uncharted Data Challenge by Adaption (May 2026). Powered by Adaptive Data by Adaption.

=== v1.5+ EMPIRICAL HEADLINE RESULTS ===

NEW v1.8 — 23 additional jje<->ko parallel lemmas extracted from 제주어 표기법 hanja annotations (e.g. 삼춘<->삼촌 via 〔三寸〕, 곡석<->곡식 via 〔穀食〕, ᄌᆞᆷ녜<->잠녀 via 〔潛女〕).

6 frontier LLMs (GPT-5, GPT-4.1, Gemini 3.1 Pro, GPT-4o, GPT-4o-mini, Gemini 3 Pro) tested cold (no fine-tune, no in-context):
  GPT-5 chrF6 = 0.141 (best); all others < 0.12

5-shot in-context learning with Jejueo+ parallel pairs:
  GPT-5 chrF6 = 0.193 (+37%)
  GPT-4.1 chrF6 = 0.199 (+54%)
  GPT-4o-mini chrF6 = 0.136 (zero -> learning)

Full per-pair results in baseline_eval_gpt4omini.jsonl, multimodel_baseline_eval.json, icl_baseline_eval.json, icl_scaling_curve.json.

=== CONTENT (3,376 deduplicated entries) ===

- 30 parallel jje<->ko pairs (29 from Ieodosana + 1 from Wp 제주어 article)
- 45 folklore-only Jejueo lines from Ieodosana folk song (Jeju women divers' work song)
- 3 lines from 차사본풀이 (Chasa Bonpuri — Jeju shamanic origin myth) — first-time NLP coverage
- 82 Jejueo lemmas from official 제주어 표기법 spelling rules (Public Domain — South Korean government work)
- 80+ Wiktionary lexicon lemmas
- 2,700+ Jejueo-signal-bearing sentences from Wikimedia Incubator wikitext
- 255 entries with explicit jje<->ko alignment (incl. 80 GPT-5-aligned, marked confidence 0.6/UNVERIFIED)
- Phonological tags: archaic ㆍ vowel, ᄒᆞ verb stem, -곡 conjunctive, ᄆᆞ morpheme, double-araea ᄋᆢ, archaic ieung ㆆ

=== FILES ===

main corpus: jejueo_plus.jsonl, lexicon.jsonl
metadata: STATS.json, README.md, DATASHEET.md, LICENSE, CITATION.cff
baselines: baseline_eval_gpt4omini.jsonl, baseline_eval_summary.json, multimodel_baseline_eval.json, icl_baseline_eval.json, icl_scaling_curve.json

=== SCHEMA ===

jejueo, korean (when available), domain, register, phonetic_tags, era, confidence, source, license, license_url, attribution_url, hanja (where applicable), page_title.

=== LICENSE ===

Aggregate: CC BY-SA 4.0 (upgrade-compatible with CC BY-SA 3.0/4.0 Wikimedia sources). Public-domain Korean government works (제주어 표기법) clearly tagged. Apache-2.0 Kakao Brain JIT material referenced by citation only, NOT redistributed.

=== USES ===

Endangered-language preservation, low-resource machine translation (jje<->ko), dialectal NLP, phonological-feature classification, Jeju cultural heritage NLP (folk song / shamanic narrative), LLM evaluation on under-represented languages.

출처: Kaggle (syu21125/adaption-uncharted-jejueo-corpus)
태그: languages, linguistics, nlp
라이선스: CC BY-SA 4.0
수정일: 2026-05-02T23:35:23.677Z
