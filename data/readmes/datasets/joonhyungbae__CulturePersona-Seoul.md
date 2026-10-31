---
license: cc-by-nc-4.0
language:
- ko
- en
pretty_name: CulturePersona-Seoul
size_categories:
- 10K<n<100K
task_categories:
- text-generation
tags:
- synthetic
- personas
- survey
- korean
configs:
- config_name: default
  data_files:
  - split: train
    path: personas_all.parquet
---

# CulturePersona-Seoul — v1.0

**What.** 45,000 synthetic personas across weighted survey waves [2020, 2022, 2024]
(2020: 15,000, 2022: 15,000, 2024: 15,000).
Each row has 24 quantitative anchors from aggregate tables only and 12 Korean narrative fields.
The 2024 rows also carry, as a demonstration, a theme code `wish_theme` (drawn from the released table of the survey's own
open-ended answers, `grounding/era_2024/T7_theme_*`, codebook in `T7_theme_codebook.csv`), and a field
`narr_wish_for_seoul` written from it; both are null in 2020 and 2022, whose questionnaires had no such item.
This field is outside the registered human audit (which covers the twelve anchor-only fields).

**Grounded and invented content.** The anchors are the grounded layer; the narratives elaborate them, and the
prompt tells the model to invent what the anchors do not give. Three fields ask for information no anchor carries:
`narr_family_context` (marriage, co-resident children), `narr_participation_history` (playing, creating, clubs) and
`narr_view_on_seoul` (satisfaction, status); `eval/era_family_mentions.csv` counts how often family status is stated.
Treat these three fields as invented text, not survey evidence, and drop them where family status or participation matters.

**Grounding target.** Weighted estimates of an online panel of Seoul residents (not the Seoul population), from the
Seoul Citizens' Cultural Participation Survey. These are cultural-participation personas from one survey; they do not
represent other cities, populations or survey domains, and must not be read as evidence about cultural participation itself.
No synthetic individual derives from an individual response record. Cells below the project cell floor are withheld; geography stops at living area.

**Generator.** qwen3.8:27b-mtp-q4_K_M. Validator pass: 44,951/45,000.

**Evaluation layer.** `eval/`: held-out item registry, frozen SSR temperature (`tau.json`), per wave the frozen
evaluation subset (`eval_bank.jsonl`, also marked by `eval_subset` in the persona files), SSR reference statements, the
personas' answers and cosines (release arm), PPI and held-out score tables, model-judge runs and the rater guideline
(Korean). Twin-arm answers are not included because they read real respondents' anchors.

**Code.** `code_snapshot/` holds all study code, from microdata preparation to the script that writes the paper's numbers.

**Disclosure.** No individual record is released. `eval/era_rapid.md` reports a RAPID audit (Templ, Thees and Mueller
2026, arXiv:2602.09235) of this dump against the survey's respondents: an attacker who knows a respondent's sex, age
band, living area, education and occupation and trains on these personas is compared with one who uses the released
tables alone and with the reference of releasing the records themselves.

**Source and citation.** Seoul Citizens' Cultural Participation Survey, 2020, 2022 and 2024 waves (Seoul Foundation for
Arts and Culture; reports published 2021, 2023 and 2025), used under the publisher's data-use terms. Cite the survey
together with this dataset. This dataset is not an official statistic or product of the Seoul Foundation for Arts and
Culture and implies no approval or endorsement by it.

**Licence.** Data (grounding tables, sampler specifications, theme tables, personas and narratives): CC BY-NC 4.0.
Code and evaluation layer: CC BY 4.0; persona records and table values inside `eval/` remain CC BY-NC 4.0. See `LICENSE`.
