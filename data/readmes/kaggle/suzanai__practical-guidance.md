# PragmaEval: Multilingual Practical Guidance Q&A

Navigating everyday tasks

# PragmaEval: Multilingual Practical Guidance Q&A

## Overview

PragmaEval is a multilingual evaluation dataset for assessing how large language models handle **real-world practical guidance** — the everyday questions people actually ask when navigating healthcare, public services, local businesses, and education. The dataset pairs naturalistic prompts with structured "enhanced" variants and includes flags for cultural specificity and adversarial probes.

## Provenance

- **Seed (April 2026):** A 224-item English seed set was generated synthetically using **Claude Opus 4.6 Extended**, covering four practical-knowledge domains.
- **Multilingual expansion:** The seed was adapted and expanded via **Adaption AI Labs Data** into 17 additional languages, prioritizing cultural localization over literal translation.
- **Validation (current stage):** This release is published to invite native speakers and evaluation experts to validate quality, accuracy, and cultural specificity before downstream benchmark use.

## Composition

- **4,613 rows** across **18 languages**: English (`en`), Spanish (`es`), Portuguese (`pt`), German (`de`), French (`fr`), Italian (`it`), Dutch (`nl`), Russian (`ru`), Polish (`pl`), Finnish (`fi`), Swedish (`sv`), Norwegian (`no`), Serbian (`sr`), Chinese (`zh`), Japanese (`ja`), Korean (`ko`), Hindi (`hi`), Tagalog (`tl`)
- **4 domains**, evenly balanced: `healthcare_navigation`, `public_services`, `local_business`, `education`
- **224** unique seed item IDs, with paraphrase variants in some splits
- **~30%** of items flagged `cultural_specificity=True`
- **~11%** of items flagged `is_adversarial=True`

## Schema

| Column | Type | Description |
|---|---|---|
| `id` | int | Seed item ID (1–224); shared across language variants |
| `lang` | str | ISO 639-1 language code |
| `domain` | str | One of `healthcare_navigation`, `public_services`, `local_business`, `education` |
| `prompt` | str | Naturalistic user question |
| `completion` | str | Concise reference answer |
| `enhanced_prompt` | str | Structured/expert-style prompt variant |
| `enhanced_completion` | str | Long-form structured reference answer |
| `cultural_specificity` | bool | Whether the item depends on local/cultural context |
| `is_adversarial` | bool | Whether the item probes failure modes (ambiguity, edge cases, conflicting goals) |

## Suggested Uses

- Multilingual instruction-following and helpfulness evaluation
- Cultural-specificity and localization-fidelity testing
- Pragmatic competence benchmarking — when a technically correct answer still misses the user's real situation
- Style/format sensitivity studies via the paired concise (`prompt`/`completion`) and structured (`enhanced_*`) variants
- Adversarial robustness slicing using the `is_adversarial` flag

## Known Issues & Validation

This is an early release. The multilingual content was produced synthetically and may contain localization artifacts, mistranslations, or inconsistencies in how cultural-specificity and adversarial flags map across languages. We are partnering with **native speakers and evaluation experts** across the included languages to validate the synthetic localization and refine the tags. Updates will be published as validation progresses; feedback via the discussion tab is welcome.

## Citation

If you use this dataset, please cite as:

> PragmaEval: A Multilingual Practical Guidance Evaluation Dataset (2026), Suzana Ilić.

## License

CC BY 4.0 — please attribute when using or redistributing.

출처: Kaggle (suzanai/practical-guidance)
태그: text
라이선스: CC0: Public Domain
수정일: 2026-05-01T14:20:55.300Z
