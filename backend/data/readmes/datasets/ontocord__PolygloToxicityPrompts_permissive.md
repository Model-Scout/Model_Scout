---
license: cc-by-4.0
task_categories:
- text-generation
language:
- ar
- cs
- de
- en
- es
- fr
- hi
- id
- it
- ja
- ko
- nl
- pl
- pt
- ru
- sv
- zh
pretty_name: Polyglo PTP Permissive
configs:
- config_name: default
  data_files: data/*.parquet
---

# Polyglo PTP Permissive

Permissive-source subset of the PTP configs from `ToxicityPrompts/PolygloToxicityPrompts`, filtered using the local URL/source permissiveness rules in this workspace. WildChat configs are not included because they do not provide row-level source URLs.

Source split: `full` for `ptp-*` configs.

Rows scanned: 425,000. Rows kept: 1,649.

See `polyglo_ptp_permissive_stats_620972.json` for kept/discard reason distributions and per-language counts.
