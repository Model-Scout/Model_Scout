---
license: cc-by-4.0
task_categories:
- text-generation
language:
- en
- ko
- ja
- pt
- fr
- nl
- de
- es
- vi
tags:
- synthetic
- personas
- nemotron
- derived
size_categories:
- 100K<n<1M
configs:
- config_name: belgium
  data_files: nemotron-personas-belgium/*.parquet
- config_name: brazil
  data_files: nemotron-personas-brazil/*.parquet
- config_name: el-salvador
  data_files: nemotron-personas-el-salvador/*.parquet
- config_name: france
  data_files: nemotron-personas-france/*.parquet
- config_name: india
  data_files: nemotron-personas-india/*.parquet
- config_name: japan
  data_files: nemotron-personas-japan/*.parquet
- config_name: korea
  data_files: nemotron-personas-korea/*.parquet
- config_name: singapore
  data_files: nemotron-personas-singapore/*.parquet
- config_name: usa
  data_files: nemotron-personas-usa/*.parquet
- config_name: vietnam
  data_files: nemotron-personas-vietnam/*.parquet
---

# Nemotron-Personas Lite (10 countries × 10k)

A **~63MB derived subsample** of NVIDIA's [Nemotron-Personas](https://huggingface.co/nvidia) synthetic persona datasets (10 countries, ~24GB total in the originals), built for the [persona-lightsim](https://github.com/Dongkyu-ES/persona-lightsim) harness — lightweight persona market research and simulation with coding agents.

## What was derived, exactly

Per country: **10,000 personas** sampled with fixed seed 42 (shard-size-proportional, row-group random extraction) from the original train splits.

- **Columns**: 15 of the original 26 — `persona`, `professional_persona`, `arts_persona`, `hobbies_and_interests_list`, `skills_and_expertise_list`, `career_goals_and_ambitions`, `sex`, `age`, `marital_status`, `education_level`, `occupation`, `province`, `district`, `country`, `cultural_background`
- **Trimming**: `persona`/`professional_persona`/`arts_persona` truncated to 400 chars, `career_goals_and_ambitions`/`cultural_background` to 300 chars (marked with a trailing `…`)
- **Structure preserved**: original shard file layout, including Belgium's language-quota shards (`nl/fr/de/en_BE.parquet`) and India's English-only shards (`en_IN-*`), so samplers written for the originals run unchanged
- Build script: [`scripts/build_lite_pack.py`](https://github.com/Dongkyu-ES/persona-lightsim/blob/main/scripts/build_lite_pack.py); per-file sha256 in [`scripts/data_manifest.json`](https://github.com/Dongkyu-ES/persona-lightsim/blob/main/scripts/data_manifest.json)

Countries: Belgium, Brazil, El Salvador, France, India, Japan, Korea, Singapore, USA, Vietnam.

If you need full narratives or all 26 columns, use the NVIDIA originals instead.

## Attribution / License

This dataset is a derivative work of the **Nemotron-Personas** dataset family by **NVIDIA Corporation**, each released under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) (Nemotron-Personas-Belgium, -Brazil, -El-Salvador, -France, -India, -Japan, -Korea, -Singapore, -USA, -Vietnam, produced with NeMo Data Designer). Changes made: column selection (15/26), narrative-field truncation, and per-country subsampling to 10k rows as described above. This derivative is likewise distributed under **CC-BY-4.0**.

The personas are synthetic — they represent statistically grounded population composition, not real individuals or behavioral logs.
