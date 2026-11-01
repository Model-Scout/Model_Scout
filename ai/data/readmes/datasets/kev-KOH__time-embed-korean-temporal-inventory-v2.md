---
language:
- ko
license: other
task_categories:
- sentence-similarity
tags:
- temporal-reasoning
- korean
- bge-m3
configs:
- config_name: C1
  data_files:
  - split: train
    path: train/C1.jsonl
- config_name: C3
  data_files:
  - split: train
    path: train/C3.jsonl
- config_name: C5
  data_files:
  - split: train
    path: train/C5.jsonl
- config_name: nested_C1_30k
  data_files:
  - split: train
    path: nested_v1/train_C1_30k.jsonl
- config_name: nested_C3_80k
  data_files:
  - split: train
    path: nested_v1/train_C3_80k.jsonl
- config_name: nested_C5_120k
  data_files:
  - split: train
    path: nested_v1/train_C5_120k.jsonl
- config_name: nested_control_C1_30k
  data_files:
  - split: train
    path: nested_v1/control_C1_30k.jsonl
- config_name: nested_control_C3_30k
  data_files:
  - split: train
    path: nested_v1/control_C3_30k.jsonl
- config_name: nested_control_C5_30k
  data_files:
  - split: train
    path: nested_v1/control_C5_30k.jsonl
- config_name: legacy_validation
  data_files:
  - split: validation
    path: validation.jsonl
- config_name: legacy_test
  data_files:
  - split: test
    path: test.jsonl
- config_name: inventory_eval
  data_files:
  - split: validation
    path: evaluation/inventory_eval.jsonl
---

# Time-Embed Korean Temporal Inventory v2

한국어 시간 표현 임베딩 학습·평가 데이터셋입니다.

- `C1`, `C3`, `C5`: 문맥 허용 범위가 다른 학습 조건이며 각 314개 query를 포함합니다.
- 각 학습 query는 승인된 모든 동의 positive(최소 3개)와 정확히 7개 negative를 가집니다.
- `legacy_validation`, `legacy_test`: 기존 동결 dev/test bytes를 그대로 보존합니다.
- `inventory_eval`: 승인된 희귀·격식·경계 시간 표현 118개입니다.
- Inventory Test 원문과 라벨은 공개하지 않으며 `sealed/inventory_test_handle.json`만 제공합니다.

승인 방식은 개별 행 검수로 위장하지 않은 `owner_policy_waiver`입니다. 정확한 승인·감사
해시와 산출물은 `evidence/`, `audit/`, `dataset_manifest.json`에 포함됩니다.

## Nested scale v1

- `nested_C1_30k`, `nested_C3_80k`, `nested_C5_120k`: 30k ⊂ 80k ⊂ 120k nested training views.
- 각 행은 positive 1개, temporal hard negative 4개, semantic control negative 3개를 가집니다.
- `nested_control_*`: 각 main view와 겹치지 않는 조건별 30k matched control입니다.
- `nested_v1/manifest.json`과 `nested_v1/audit_report.json`이 행 수, SHA-256, prefix nesting, control disjointness를 고정합니다.
