---
language: [en, ko]
license: other
pretty_name: Qwen3.8 Executor Unified Training Dataset
tags: [qwen, executor, tool-calling, agents]
---

# Qwen3.8 Executor Unified Training Dataset

## Purpose

Public, provenance-pinned executor records for tool use, repository agents, computer use, and Korean coverage. This is an attributed integration; the upstream authors collected or generated the source data.

## Schema

The Parquet files share the canonical fields documented in `manifests/schema.json`. `messages` uses role/content/tool-call structs. Dynamic tool arguments are validated JSON in `arguments_json`. Images and executable artifacts are self-contained bytes where included.

## Sources, revisions, licenses, and transformations

| HF repo | revision | config | source split | license | rows before | accepted | rejected | transformation |
|---|---|---|---|---:|---:|---:|---:|---|
| [tuandunghcmut/toolbench-v1](https://huggingface.co/datasets/tuandunghcmut/toolbench-v1/tree/36de9b189753ad5de276181974f97df15e8c3202) | `36de9b189753ad5de276181974f97df15e8c3202` | `default` | `train` | apache-2.0 | 187542 | 181695 | 5847 | canonicalized |
| [glaiveai/glaive-function-calling-v2](https://huggingface.co/datasets/glaiveai/glaive-function-calling-v2/tree/e7f4b6456019f5d8bcb991ef0dd67d8ff23221ac) | `e7f4b6456019f5d8bcb991ef0dd67d8ff23221ac` | `default` | `train` | apache-2.0 | 112960 | 46430 | 66530 | canonicalized |
| [NousResearch/hermes-function-calling-v1](https://huggingface.co/datasets/NousResearch/hermes-function-calling-v1/tree/dae3e1d28cfbcf4b915c04ea1e072030529b4bda) | `dae3e1d28cfbcf4b915c04ea1e072030529b4bda` | `func_calling_singleturn` | `train` | apache-2.0 | 1893 | 1096 | 797 | canonicalized |
| [NousResearch/hermes-function-calling-v1](https://huggingface.co/datasets/NousResearch/hermes-function-calling-v1/tree/dae3e1d28cfbcf4b915c04ea1e072030529b4bda) | `dae3e1d28cfbcf4b915c04ea1e072030529b4bda` | `func_calling` | `train` | apache-2.0 | 1893 | 1094 | 799 | canonicalized |
| [NousResearch/hermes-function-calling-v1](https://huggingface.co/datasets/NousResearch/hermes-function-calling-v1/tree/dae3e1d28cfbcf4b915c04ea1e072030529b4bda) | `dae3e1d28cfbcf4b915c04ea1e072030529b4bda` | `glaive_func_calling` | `train` | apache-2.0 | 5209 | 3998 | 1211 | canonicalized |
| [NousResearch/hermes-function-calling-v1](https://huggingface.co/datasets/NousResearch/hermes-function-calling-v1/tree/dae3e1d28cfbcf4b915c04ea1e072030529b4bda) | `dae3e1d28cfbcf4b915c04ea1e072030529b4bda` | `json_mode_agentic` | `train` | apache-2.0 | 1342 | 1284 | 58 | canonicalized |
| [NousResearch/hermes-function-calling-v1](https://huggingface.co/datasets/NousResearch/hermes-function-calling-v1/tree/dae3e1d28cfbcf4b915c04ea1e072030529b4bda) | `dae3e1d28cfbcf4b915c04ea1e072030529b4bda` | `json_mode_singleturn` | `train` | apache-2.0 | 1241 | 1240 | 1 | canonicalized |
| [heegyu/glaive-function-calling-v2-ko](https://huggingface.co/datasets/heegyu/glaive-function-calling-v2-ko/tree/c8b54e70bfbdd2fd6be037557e6feaf1abf14f5d) | `c8b54e70bfbdd2fd6be037557e6feaf1abf14f5d` | `default` | `train` | apache-2.0 | 15170 | 15035 | 135 | canonicalized |
| [nvidia/Open-SWE-Traces](https://huggingface.co/datasets/nvidia/Open-SWE-Traces/tree/ad4805a5aa7de70d99cab0bb8f99b15304c76de0) | `ad4805a5aa7de70d99cab0bb8f99b15304c76de0` | `openhands` | `minimax_m25` | cc-by-4.0 | 49948 | 45165 | 4783 | canonicalized |
| [nvidia/Open-SWE-Traces](https://huggingface.co/datasets/nvidia/Open-SWE-Traces/tree/ad4805a5aa7de70d99cab0bb8f99b15304c76de0) | `ad4805a5aa7de70d99cab0bb8f99b15304c76de0` | `openhands` | `qwen35_122b` | cc-by-4.0 | 55488 | 50364 | 5124 | canonicalized |
| [nvidia/Open-SWE-Traces](https://huggingface.co/datasets/nvidia/Open-SWE-Traces/tree/ad4805a5aa7de70d99cab0bb8f99b15304c76de0) | `ad4805a5aa7de70d99cab0bb8f99b15304c76de0` | `sweagent` | `minimax_m25` | cc-by-4.0 | 57268 | 53035 | 4233 | canonicalized |
| [nvidia/Open-SWE-Traces](https://huggingface.co/datasets/nvidia/Open-SWE-Traces/tree/ad4805a5aa7de70d99cab0bb8f99b15304c76de0) | `ad4805a5aa7de70d99cab0bb8f99b15304c76de0` | `sweagent` | `qwen35_122b` | cc-by-4.0 | 44785 | 40375 | 4410 | canonicalized |
| [nvidia/ProCUA-SFT](https://huggingface.co/datasets/nvidia/ProCUA-SFT/tree/120de7e954f851c2d24399230367f2b01ff815f9) | `120de7e954f851c2d24399230367f2b01ff815f9` | `raw` | `shard_00000` | cc-by-4.0 | 93566 | 1861 | 91705 | 1_of_50_deterministic_shards |
| [nvidia/Nemotron-Personas-Korea](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Korea/tree/ada0f5b53a38bb5a30cce09358adde883c1ab63a) | `ada0f5b53a38bb5a30cce09358adde883c1ab63a` | `default` | `train` | cc-by-4.0 | 1000000 | 274531 | 725469 | deterministic_27.5_percent_sample |
| [NousResearch/Hermes-3-Dataset](https://huggingface.co/datasets/NousResearch/Hermes-3-Dataset/tree/b1fddbdcae4e6714889365d1e6ce266a45289cc9) | `b1fddbdcae4e6714889365d1e6ce266a45289cc9` | `default` | `train` | apache-2.0 | 958829 | 296777 | 662052 | executor_user_intent_filter_all_matches |
| [mlx-community/ToolMind](https://huggingface.co/datasets/mlx-community/ToolMind/tree/7b8e1d44d8dbe0e707dc336fdc1f7091fd6a9273) | `7b8e1d44d8dbe0e707dc336fdc1f7091fd6a9273` | `graphsyn` | `train` | apache-2.0 | 163180 | 160849 | 2331 | complete_pinned_component_after_normalization_and_dedup |
| [mlx-community/ToolMind](https://huggingface.co/datasets/mlx-community/ToolMind/tree/7b8e1d44d8dbe0e707dc336fdc1f7091fd6a9273) | `7b8e1d44d8dbe0e707dc336fdc1f7091fd6a9273` | `APIGen-MT-5k-query` | `train` | apache-2.0 | 25109 | 24571 | 538 | complete_pinned_component_after_normalization_and_dedup |
| [mlx-community/ToolMind](https://huggingface.co/datasets/mlx-community/ToolMind/tree/7b8e1d44d8dbe0e707dc336fdc1f7091fd6a9273) | `7b8e1d44d8dbe0e707dc336fdc1f7091fd6a9273` | `BUTTONInstruct-query` | `train` | apache-2.0 | 21202 | 21136 | 66 | complete_pinned_component_after_normalization_and_dedup |
| [mlx-community/ToolMind](https://huggingface.co/datasets/mlx-community/ToolMind/tree/7b8e1d44d8dbe0e707dc336fdc1f7091fd6a9273) | `7b8e1d44d8dbe0e707dc336fdc1f7091fd6a9273` | `ToolACE-query` | `train` | apache-2.0 | 7327 | 7307 | 20 | complete_pinned_component_after_normalization_and_dedup |
| [mlx-community/ToolMind](https://huggingface.co/datasets/mlx-community/ToolMind/tree/7b8e1d44d8dbe0e707dc336fdc1f7091fd6a9273) | `7b8e1d44d8dbe0e707dc336fdc1f7091fd6a9273` | `When2Call-query` | `train` | apache-2.0 | 17531 | 17402 | 129 | complete_pinned_component_after_normalization_and_dedup |
| [mlx-community/ToolMind](https://huggingface.co/datasets/mlx-community/ToolMind/tree/7b8e1d44d8dbe0e707dc336fdc1f7091fd6a9273) | `7b8e1d44d8dbe0e707dc336fdc1f7091fd6a9273` | `glaive-function-calling-v2-query` | `train` | apache-2.0 | 20017 | 19955 | 62 | complete_pinned_component_after_normalization_and_dedup |
| [mlx-community/ToolMind](https://huggingface.co/datasets/mlx-community/ToolMind/tree/7b8e1d44d8dbe0e707dc336fdc1f7091fd6a9273) | `7b8e1d44d8dbe0e707dc336fdc1f7091fd6a9273` | `tau-train-query` | `train` | apache-2.0 | 12882 | 12879 | 3 | complete_pinned_component_after_normalization_and_dedup |
| [mlx-community/ToolMind](https://huggingface.co/datasets/mlx-community/ToolMind/tree/7b8e1d44d8dbe0e707dc336fdc1f7091fd6a9273) | `7b8e1d44d8dbe0e707dc336fdc1f7091fd6a9273` | `xlam-function-calling-60k-query` | `train` | apache-2.0 | 101363 | 83785 | 17578 | complete_pinned_component_after_normalization_and_dedup |
| [greghavens/fable-5-coding-and-debugging-traces](https://huggingface.co/datasets/greghavens/fable-5-coding-and-debugging-traces/tree/c63e82adec30798edcbd6e1dcb0014d2b15de236) | `c63e82adec30798edcbd6e1dcb0014d2b15de236` | `default` | `train` | cc-by-4.0 | 12490 | 2160 | 10330 | verified_final_train_trajectories_only; validation_and_prefix_views_excluded |
| [Nanbeige/ToolMind-Web-QA](https://huggingface.co/datasets/Nanbeige/ToolMind-Web-QA/tree/2690dcdfdd82ab147aad4a65ab231d4e344f5cd0) | `2690dcdfdd82ab147aad4a65ab231d4e344f5cd0` | `open-wiki-traj` | `train` | apache-2.0 | 5624 | 3859 | 1765 | answer_validated; >=2 evidence URLs; dated freshness anchor; benchmark markers excluded |

No single license is asserted over the mixture. Apply each row's `source_license` and upstream attribution requirements.

## Build and isolation methodology

Evaluation data is canonicalized first. Exact SHA-256, normalized SHA-256 (whitespace, timestamps, UUIDs, and volatile IDs normalized), normalized user-prompt SHA-256, and 64-bit SimHash are then checked while admitting Train rows. Exact, normalized, prompt collisions, and near matches at Hamming distance <=3 are removed from Train. A trajectory/task is always one row and never split by turn.

High-confidence secrets, Korean resident registration numbers, missing user queries, empty assistant targets, invalid JSON tool arguments, missing tool references, broken images, and duplicate rows are rejected. `persona_seed` rows are excluded from `trainable_rows`. OpenWebRL and Uni-GUI are reference-only because their cards identify benchmark-derived task families. ProCUA uses deterministic shard 00000 only. Hermes-3 keeps executor-relevant rows; Korean personas use a deterministic 27.5% sample. ToolMind uses every pinned component after normalization and deduplication. Fable-5 keeps one complete verified Train trajectory and excludes cumulative prefix views and validation tasks. ToolMind-Web-QA requires upstream answer validation, at least two evidence URLs, a dated freshness anchor, and no known benchmark marker.

## Multimodal and tool handling

Screenshots are not replaced with text descriptions. Included screenshots use bytes/path/mime/hash records and were decoded with Pillow. Tool definitions remain stable JSON strings; calls have name/id/type and validated `arguments_json`.

## Recommended filters and limitations

Sample by `record_type` and source instead of uniform row sampling. Exclude `persona_seed` from direct response loss. Eval is not an independent benchmark where `metadata.contamination_family` says ToolBench. Source licenses and upstream terms still apply. The near-duplicate index uses a bounded within-Train collision bucket; exact and normalized checks are exhaustive.

## Reproduction

```bash
pip install huggingface_hub pyarrow pillow requests numpy
python build_executor_datasets.py --output executor_dataset_build --cache /mnt/HDD0/executor_dataset_cache
python build_executor_datasets.py --output executor_dataset_build --cache /mnt/HDD0/executor_dataset_cache --eval-seed-repo snowman0919/qwen38-executor-eval-v1 --eval-seed-revision d348a8f0d951337f427f37cd027fffa3de26631f
python build_executor_datasets.py --validate-only --output executor_dataset_build
```

See `manifests/`, `reports/`, and `reports/sanity_sample.jsonl` for pinned source metadata and validation evidence.
