---
language:
- en
- ko
license: other
license_name: ha-hwang-research-data-use-1.0
license_link: LICENSE
pretty_name: Agent deliberation Study 1 reproduction data
---

# Agent deliberation Study 1

Reproduction data release, 2026-10-26. Repository: haha0309/agent-deliberation-study1. Cite a fixed repository revision when using these data.

This repository contains analysis-level numerical inputs for 18,209 completed runs (including specified exclusions), exact analyzed coding targets and context, paired position-change targets, and purpose-selected case records. It is not the complete raw discussion corpus.

`numeric/AI-run-index.csv` separates failed/retried records from the analysis inclusion flag. `numeric/AI-survey-numeric.csv` contains pre/post numerical responses. Numerical input and display mappings are under `numeric/analysis-inputs` and `numeric/display-map.json`. `columns.csv` describes fields.

Utterance/evidence/device inputs use opaque ids joined to the respective frame and label files. Evidence coding includes the full original 120 discussion inputs in `evidence-discussions.jsonl` and 600 final explanations in `evidence-reasons.jsonl`; join on discussion_id to reconstruct the exact original input. Position-change coding used target-only inputs, not preceding context. New coding is a post-hoc robustness analysis, not human accuracy validation. Original labels and primary estimates are preserved separately.

The 12 case discussions were purpose-selected, not a representative random sample. Card-extraction audit texts are stratified by model and condition with seed 20261026, 30 per cell; this is an audit input set, not completed independent validation. Numerical event series permit recalculation of process outcomes; rerunning extraction on every utterance would require additional raw transcripts.

## Reproduction

Code is released separately at https://github.com/hahwang0309/agent-deliberation-lab. From the reproduction code root run `python scripts/reanalyze_public_numeric.py --source-data PATH/numeric --out OUTPUT`. Python dependencies and R/lme4/lmerTest are required. The original local check refit 15 E1--E5 model contrasts from numeric CSVs, without raw DBs or model APIs, reproducing estimates and confidence limits within 1e-6. This does not assert all registered and exploratory models have been refit.

For six-figure regeneration, copy `numeric/plot-inputs/` into the reproduction code root preserving paths and run `python scripts/build_manuscript_figures.py`. Archived estimates reproduce displays, not statistical fitting. The experimental frozen version is 7a244351f3374b3e1ac4b02bf55a4f41ff9ca91c.

## Access and terms

No arbitrary percentage of the full corpus defines sufficiency. This release separates numerical reanalysis, text-coding audit, and complete original extraction. The full raw discussion databases are not included. Requests for additional records needed to assess the paper may be addressed to the corresponding author; any applicable third-party restrictions and access arrangements will be disclosed to the journal. No unavailable file is represented as public.

Original research dataset material is supplied under the accompanying research-data-use terms. The separately published software license does not automatically license third-party datasets. Third-party sources retain their own terms; see THIRD_PARTY.md. Contact: Ha Hwang, ghkdgk0309@gmail.com.
