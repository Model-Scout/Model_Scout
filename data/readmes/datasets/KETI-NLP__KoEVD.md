---
language:
- ko
license: other
license_name: koevd-dataset-research-use-v1
license_link: LICENSE.md
task_categories:
- text-classification
- text-generation
size_categories:
- 10K<n<100K
tags:
- safety
- benchmark
- korean
configs:
- config_name: canonical
  default: true
  data_files:
  - split: test
    path: full_eval/koevd_full_eval.jsonl
- config_name: sources_core
  data_files:
  - split: test
    path: benchmark_splits/core.jsonl
- config_name: sources_core_severity_explicitness_balanced_768
  data_files:
  - split: test
    path: benchmark_splits/core_severity_explicitness_balanced_768.jsonl
- config_name: sources_full_eval
  data_files:
  - split: test
    path: benchmark_splits/full_eval.jsonl
- config_name: sources_full_eval_severity_explicitness_balanced_1200
  data_files:
  - split: test
    path: benchmark_splits/full_eval_severity_explicitness_balanced_1200.jsonl
- config_name: sources_hard
  data_files:
  - split: test
    path: benchmark_splits/hard.jsonl
- config_name: task2_choose_best
  data_files:
  - split: test
    path: tasks/task2_candidate_response_safety_choice/full_eval/choose_best.jsonl
- config_name: task2_choose_unsafe
  data_files:
  - split: test
    path: tasks/task2_candidate_response_safety_choice/full_eval/choose_unsafe.jsonl
- config_name: task2_rejected_vs_accepted
  data_files:
  - split: test
    path: tasks/task2_candidate_response_safety_choice/full_eval/rejected_vs_accepted.jsonl
- config_name: task2_relative_harmfulness
  data_files:
  - split: test
    path: tasks/task2_candidate_response_safety_choice/full_eval/relative_harmfulness.jsonl
- config_name: task5_safe_guided
  data_files:
  - split: test
    path: tasks/task5_tool_action_choice_safety/main/safe_guided.jsonl
- config_name: task5_tool_forced
  data_files:
  - split: test
    path: tasks/task5_tool_action_choice_safety/main/tool_forced.jsonl
- config_name: task5_unsafe_induced
  data_files:
  - split: test
    path: tasks/task5_tool_action_choice_safety/main/unsafe_induced.jsonl
---
# KoEVD

KoEVD is a Korean benchmark linking five evaluation or analysis targets through source utterances: utterance-risk judgment, candidate-response safety choice, direct-generation response harmfulness, descriptive response strategies, and a pre-execution mock tool/action-choice diagnostic.

## Contents and scope

The canonical corpus contains **13,552 sources and 71,395 response candidates**: 30,740 accepted, 27,104 rejected, and 13,551 strongly rejected. Three interpretive fields record problem reasons, implied meanings, and background knowledge. Korean slang, idioms, relationships, and sociocultural references motivate depth within one language; this is not evidence of cross-lingual generalization.

All original JSONL files are byte-identical to the review package. See [PACKAGE_README.md](PACKAGE_README.md) for paths and counts, [schema/LABELS.md](schema/LABELS.md) for labels, and [METRICS.md](METRICS.md) for denominators. The repository manifest covers the current package; review_manifest.json preserves the earlier manifest for provenance.

## Loading

Load release `v0.1.0` using the explicit release tag:

```python
from datasets import load_dataset
data = load_dataset("KETI-NLP/KoEVD", "canonical", revision="v0.1.0", split="test")
```

The `sources_*` configurations are source-ID indexes to join with `canonical`; they are not standalone utterance corpora. The core, hard, and balanced views overlap with the full corpus. They are **not train/validation/test partitions**. The `test` name only exposes evaluation records through the library API. Task 2 and Task 5 each use independent configurations because their schemas and variants differ. Task 2 relative_harmfulness has 13,551 rows; the other three variants each have 13,552.

Task 5 contains 784 selected sources under three framings (784 rows each). Its mock schemas are not executed. It is a diagnostic subset, not a population prevalence estimate. Task 4 reuses Task 3 generations and is descriptive, not a safety ranking.

## Construction and governance

KoEVD is human-curated and AI-assisted, with guideline design, candidate drafting, rewriting, relabeling, adjudication and filtering. The final paper describes an approximately 3.5-year process and an 800-item IAA audit. No formal IRB approval or institutional exemption was obtained; the paper reports governance and annotator-welfare limitations explicitly. Labels reflect the project guidelines rather than universal moral ground truth.

## Availability and limitations

The [evaluation/analysis code](https://github.com/KETI-NLP/KoEVD), [assistant-safety adapter](https://huggingface.co/KETI-NLP/KoEVD-assistant-safety), and [response-strategy adapter](https://huggingface.co/KETI-NLP/KoEVD-response-strategy) are distributed separately under KETI-NLP. Release `v0.1.0` identifies this dataset; the code release records immutable HF commits for GPU verification. B200 operational validation of the classifiers and offline CLI passed on fixed public samples; see [the measured scope](https://github.com/KETI-NLP/KoEVD/blob/main/docs/GPU_VALIDATION_RESULTS.md). This does not reproduce held-out F1. The [strategy code/display-label crosswalk](https://github.com/KETI-NLP/KoEVD/blob/main/docs/STRATEGY_LABELS.md) documents the original exporter mappings. Raw model-output dumps, internal construction documents, and the broader internal classifier-training pool are not part of this dataset. Classifier inference and exact classifier retraining therefore have different reproducibility scopes.

## Use terms

The corpus intentionally includes harmful, offensive and sensitive language for safety research. Read [LICENSE.md](LICENSE.md) before use. The existing KoEVD research-use terms are preserved; this is not an unrestricted Apache/MIT dataset. Public examples should follow the sanitization requirements in those terms.

## Citation

```bibtex
@misc{kim2026koevd,
  title={KoEVD: A Korean Benchmark for Metadata-Conditioned Multi-Stage LLM Safety Evaluation},
  author={Kim, San and Kim, Wonjung and Kwon, Heesoo and Yang, Jae Hee},
  year={2026},
  note={Accepted to the main conference of AACL-IJCNLP 2026; proceedings identifier pending}
}
```

## Diagnose your own model

Use the [complete KoEVD own-model workflow](https://github.com/KETI-NLP/KoEVD/blob/main/docs/OWN_MODEL_GUIDE.md) to generate your model’s responses, measure Task 1–5 behavior, and produce HTML/JSON/CSV reports of metadata-specific strengths, weaknesses, strategies and source-matched tool-selection gaps. The current GitHub source adds this pipeline; the original v0.1.0 code tag does not include it. A subsequent [live B200 pipeline test](https://github.com/KETI-NLP/KoEVD/blob/main/docs/PIPELINE_VALIDATION_RESULTS.md) completed 40 smoke requests and 959 expanded generation requests with unmodified code. It also found batch-dependent strategy outputs and concerning safety judgments; execution success does not establish measurement accuracy.

## Historical Task 1 metadata view

The canonical corpus is unchanged. For exact historical Task 1 grouping, the accompanying [metadata overlay](reproduction/task1_metadata_v1/README.md) records 35 sources whose severity or utterance type differs from the retained analysis view. The checksum-checked script emits a separate metadata index; it does not overwrite canonical labels or model inputs. The index has 13,430 non-borderline sources, compared with 13,429 in the canonical release. Record the annotation view when comparing results.

A later B200 check reproduced the assistant-safety classifier on all 532 original validation inputs; it did not establish accuracy on new generations or reproduce strategy validation F1. See the [updated reproduction scope](https://github.com/KETI-NLP/KoEVD/blob/main/docs/REPRODUCIBILITY.md).
