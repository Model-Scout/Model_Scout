---
language:
- en
- ko
license:
- mit
- apache-2.0
- other
size_categories:
- 100K<n<1M
task_categories:
- text-generation
tags:
- dpo
- preference
- rlhf
- korean
- bilingual
- raw
pretty_name: keural-DPO-raw
configs:
- config_name: default
  data_files:
  - split: ultrafeedback
    path: data/ultrafeedback.jsonl
  - split: multifaceted_dpo
    path: data/multifaceted_dpo.jsonl
  - split: hh_rlhf
    path: data/hh_rlhf.jsonl
  - split: orca_dpo_ko
    path: data/orca_dpo_ko.jsonl
  - split: aihub_71748
    path: data/aihub_71748.jsonl
  - split: aihub_71760
    path: data/aihub_71760.jsonl
---

# keural-DPO-raw

[keural-DPO](https://huggingface.co/datasets/mkd-chanwoo/keural-DPO)의 전처리 전 normalized 원본 데이터.
필터링 없이 원본 그대로 보존하여 재현성을 위해 제공합니다.

ChatML 변환 및 필터링이 적용된 학습용 데이터는 **[mkd-chanwoo/keural-DPO](https://huggingface.co/datasets/mkd-chanwoo/keural-DPO)** 를 사용하세요.

---

## 데이터셋 통계

| Split | 행 수 | 언어 | 라이선스 | 원본 |
|---|---|---|---|---|
| `ultrafeedback` | 61,054 | EN | MIT | [HuggingFaceH4/ultrafeedback_binarized](https://huggingface.co/datasets/HuggingFaceH4/ultrafeedback_binarized) |
| `multifaceted_dpo` | 65,139 | EN/KO | Apache-2.0 | [kaist-ai/Multifaceted-Collection-DPO](https://huggingface.co/datasets/kaist-ai/Multifaceted-Collection-DPO) |
| `hh_rlhf` | 160,608 | EN | MIT | [Anthropic/hh-rlhf](https://huggingface.co/datasets/Anthropic/hh-rlhf) |
| `orca_dpo_ko` | 12,727 | KO | — | [Ja-ck/Orca-DPO-Pairs-KO](https://huggingface.co/datasets/Ja-ck/Orca-DPO-Pairs-KO) |
| `aihub_71748` | 29,676 | KO | AI Hub | [AI Hub 71748](https://www.aihub.or.kr/aihubdata/data/view.do?dataSetSn=71748) |
| `aihub_71760` | 116,320 | KO | AI Hub | [AI Hub 71760](https://www.aihub.or.kr/aihubdata/data/view.do?dataSetSn=71760) |
| **합계** | **445,524** | | | |

---

## 데이터 형식

모든 split 공통 필드:

| 필드 | 타입 | 설명 |
|---|---|---|
| `prompt` | `str` | 첫 번째 user 질문 |
| `chosen` | `str` or `list[dict]` | 선택된 응답. `hh_rlhf`는 전체 대화 경로 `list[dict]` |
| `rejected` | `str` or `list[dict]` | 거부된 응답. `hh_rlhf`는 전체 대화 경로 `list[dict]` |
| `source` | `str` | 원본 데이터셋 이름 |

> `hh_rlhf`의 `chosen`/`rejected`는 멀티턴 대화 전체를 `[{"role": ..., "content": ...}, ...]` 형태로 저장합니다.

---

## 라이선스

각 split의 라이선스는 원본 데이터셋을 따릅니다.
AI Hub 데이터(`aihub_71748`, `aihub_71760`)는 [AI Hub 이용약관](https://www.aihub.or.kr/intro/policy.do) 준수 및 이용 승인 후 사용 가능합니다.
상업적 이용 전 각 원본 데이터셋의 라이선스를 반드시 확인하세요.