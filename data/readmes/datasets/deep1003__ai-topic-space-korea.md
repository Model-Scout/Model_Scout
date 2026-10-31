---
license: cc-by-4.0
language:
- en
- ko
pretty_name: AI Topic Space — Korea AI Knowledge Ecosystem (1990–2026)
tags:
- science-technology-policy
- ai-governance
- policy-gap
- scientometrics
- semantic-embedding
- korea
size_categories:
- 10K<n<100K
configs:
- config_name: relative_l3_gap_state_by_period_domain
  data_files: data/relative_l3_gap_state_by_period_domain.csv
- config_name: relative_l3_gap_summary_by_period_domain
  data_files: data/relative_l3_gap_summary_by_period_domain.csv
- config_name: policy_gap_2022_2026_top
  data_files: data/policy_gap_2022_2026_109_l3_for_appendix.csv
- config_name: l0_l1_l2_l3_dictionary
  data_files: data/l0_l1_l2_l3_dictionary_for_appendix.csv
- config_name: l0_l1_l2_cluster_counts
  data_files: data/l0_l1_l2_cluster_counts.csv
- config_name: l0_l1_l2_l3_representative_examples
  data_files: data/l0_l1_l2_l3_representative_examples.csv
---

# AI Topic Space — Korea AI Knowledge Ecosystem (1990–2026)

Reference space, Korean activation, and policy-gap tables behind the paper
**"Semantic Diversity Convergence and Policy Agenda Gaps in the AI Knowledge Ecosystem: An Embedding-Based Coupling Analysis of Korean Policy/Institutional Documents, Academic Papers, and Patents (1990–2026)."**

- 🌐 Interactive map: https://deep1003.github.io/AI_Topic_Space.github.io/
- 💻 Site & code: https://github.com/deep1003/AI_Topic_Space.github.io

## What this is

We projected 107,004 Korean academic papers, patents, and policy/institutional documents (1990–2026) into a single semantic space — the Science–Technology–Policy Interface (STPI) — built on a dictionary-defined four-level AI topic reference space (L0 domain → L1 family → L2 cluster → L3 key phrase). Documents are mapped to L3 nodes by multilingual sentence-embedding (BGE-M3) similarity. This dataset releases the **reference dictionary**, the **Korean activation / international benchmark masses per L3 and period**, and the **policy-gap tables**.

The unit of analysis for gaps is the **policy domain only**: science and technology corpora are Korea-only, so no cross-national gap is defined for them; they are released for within-Korea diversity analysis.

## Files

| File | Rows (header) | Description |
|---|---|---|
| `data/relative_l3_gap_state_by_period_domain.csv` | per L3 × 5-year period × domain | Korea mass/docs vs. benchmark mass/docs, ratio, gap strength/severity. Core table. |
| `data/relative_l3_gap_summary_by_period_domain.csv` | per period × domain | Reference L3 count, relative/absolute/strong/moderate under-representation counts, gap share. |
| `data/policy_gap_2022_2026_109_l3_for_appendix.csv` | 109 absolute-gap L3 | 2022–2026 policy L3 covered internationally but with zero Korean activation. |
| `data/l0_l1_l2_l3_dictionary_for_appendix.csv` | full L3 dictionary | L3 id, L0/L1/L2/L3 labels, Korean label, definition, source, review status. |
| `data/l0_l1_l2_cluster_counts.csv` | per L2 | L3 counts by L0/L1/L2. |
| `data/l0_l1_l2_l3_representative_examples.csv` | per L1 | Representative L2 and example L3 phrases. |
| `data/l0_l1_l2_l3_hierarchy_counts.csv` | 1 row | Total L0/L1/L2/L3 counts. |
| `data/interactive_l1_l2_l3_payload.json` | — | Full payload powering the interactive map (nodes, tree, activation, policy_gap, periods). |
| `data/ai_topic_space_snapshot_manifest.json` | — | Manifest of static snapshots used in the paper/appendix. |

## Key column semantics (gap tables)

- `l0_domain`: Policy / Science / Technology.
- `period_5y`: 1992-1996 … 2022-2026 (five-year bins).
- `korea_mass`, `korea_docs`: fractional activation mass and unique document count from Korean corpora.
- `benchmark_mass`, `benchmark_docs`: reference mass. For Policy, `benchmark_type = global_policy_benchmark` (observed domestic + international policy space); for Science/Technology, an internal domain reference mean.
- `korea_to_benchmark_ratio`: Korea / benchmark. `< 0.50` = relative gap, `< 0.25` = strong under-representation, `0` (Korea) = absolute gap.

## Headline numbers (2022–2026, Policy)

- Observed policy space: **380 L3**; Korea leaves **109 (28.7%)** entirely uncovered (absolute gaps).
- **209** further L3 are relative gaps (covered below half the international intensity).
- Gaps concentrate in **rights & biometrics, participatory governance, AI security & critical infrastructure, responsible AI**.

## License & citation

Released under **CC BY 4.0**. If you use this dataset, please cite the paper (STEPI, 2026) and link the interactive site.

> STEPI (2026). Semantic Diversity Convergence and Policy Agenda Gaps in the AI Knowledge Ecosystem: An Embedding-Based Coupling Analysis of Korean Policy/Institutional Documents, Academic Papers, and Patents (1990–2026).

## Notes

- Gap figures are a function of the observed reference space and should be read as estimates over currently observable international policy material, not a global census.
- Reference dictionaries were built from OECD/WIPO/EU/MIT-related prior taxonomies plus model-assisted candidate generation and researcher validation; they are an operational taxonomy, not a universal ontology of AI.
