---
language: ko
license: apache-2.0
tags:
- translation
- korean
- conversations
- instruction
- fine-tuning
datasets:
- mlabonne/FineTome-100k
dataset_info:
  features:
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: source
    dtype: string
  - name: score
    dtype: float64
  splits:
  - name: train
    num_bytes: 2713936
    num_examples: 1000
  download_size: 1297792
  dataset_size: 2713936
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
pretty_name: "FineTome-100k-ko: mlabonne/FineTome-100k 한국어 번역 데이터셋"
---

<!-- aegis-dataset-card -->

# FineTome-100k-ko-minimal

> **용도 기록 없음** · FineTome-100k-ko: mlabonne/FineTome-100k 한국어 번역 데이터셋  
> 파일 2개 · 1.3 MB · 행 1,000 · revision `a92fac5997` · 카드 갱신 2026-10-20  
> 전체 모델 ↔ 데이터 매핑 · 서버 복원 방법: [`neuralfoundry-coder/workspace-data-catalog_261020`](https://huggingface.co/datasets/neuralfoundry-coder/workspace-data-catalog_261020)

## 개요
`neuralfoundry-coder/FineTome-100k-ko-minimal`는 `mlabonne/FineTome-100k` 데이터셋의 `conversations` 컬럼을 한국어로 번역한 버전입니다. 이 데이터셋은 대규모 언어 모델(LLM)의 한국어 지시 튜닝 및 대화 능력 향상을 목표로 합니다.

## 이 데이터로 학습한 모델
이 데이터로 학습했다는 기록(학습 설정 · 모델 카드)을 찾지 못했다. 카탈로그의 '확인 필요' 목록에 있다.

## 파일 구성
| 파일 | 크기 | 행 | 내용 |
|---|---|---|---|
| `README.md` | 3.2 KB | - |  |
| `data/train-00000-of-00001.parquet` | 1.3 MB | 1,000 |  |

## 필드 · 범주 분포
**`data/train-00000-of-00001.parquet`** (기준 `data/train-00000-of-00001.parquet`)

| 필드 | 타입 | 채움 |
|---|---|---|
| `conversations` | list<element: struct<from: string, value | 100% |
| `source` | string | 100% |
| `score` | double | 100% |

범주 분포(기준 파일):
- `source`: infini-instruct-top-500k 560(56%) · WebInstructSub_axolotl 186(19%) · ultrainteract_trajectories_sharegpt 160(16%) · reasoning-sharegpt 42(4%) · glaive-function-calling-v2-sharegpt 20(2%) · financial-instructions-cleaned-2 16(2%) · systemchat-2.0-sharegpt 9(1%) · airoboros-3.2 7(1%)

필드는 행 최상위 키, 채움은 그 키가 있는 행 비율이다. 범주 분포는 글 필드가 아니고 값이 짧고(≤48자) 종류가 적은(≤40) 필드만 셌다.

## 내려받기 · 복원
```bash
hf download neuralfoundry-coder/FineTome-100k-ko-minimal --repo-type dataset --local-dir <폴더>
```
- 서버 파일 전체의 위치 · 재생성 방법: [`neuralfoundry-coder/workspace-data-catalog_261020`](https://huggingface.co/datasets/neuralfoundry-coder/workspace-data-catalog_261020) 의 `restore_map.json`

## 기존 설명 (2026-10-20 이전 카드)

### FineTome-100k-ko: mlabonne/FineTome-100k 한국어 번역 데이터셋

> **Note**: 이 데이터셋은 `neuralfoundry-coder/FineTome-100k-ko`의 **미니멀 버전**으로, 전체 데이터셋에서 1,000개 샘플만 포함하고 있습니다. 전체 데이터셋은 [neuralfoundry-coder/FineTome-100k-ko](https://huggingface.co/datasets/neuralfoundry-coder/FineTome-100k-ko)에서 확인하세요.

#### 데이터셋 개요

`neuralfoundry-coder/FineTome-100k-ko-minimal`는 `mlabonne/FineTome-100k` 데이터셋의 `conversations` 컬럼을 한국어로 번역한 버전입니다. 이 데이터셋은 대규모 언어 모델(LLM)의 한국어 지시 튜닝 및 대화 능력 향상을 목표로 합니다.

- **행 수**: 1,000개
- **원본 데이터셋**: [mlabonne/FineTome-100k](https://huggingface.co/datasets/mlabonne/FineTome-100k)
- **라이선스**: Apache-2.0 (원본 데이터셋 라이선스 준수)

#### 번역 상세 정보

##### 번역 방법론
- **번역 도구**: 로컬 LLM API를 활용하여 번역을 수행했습니다.
- **프롬프트 엔지니어링**: 수학 수식(LaTeX), 코드 블록, 프로그래밍 구문, 수학 기호 및 기타 특수 서식을 원본 그대로 보존하도록 특별히 설계된 시스템 및 사용자 프롬프트를 사용했습니다.
- **병렬 처리**: 번역 속도 향상을 위해 최대 100개의 동시 API 요청을 사용하여 데이터를 처리했습니다.

##### 번역 대상 필드
- `conversations` 컬럼 내의 각 턴(turn)에 포함된 `value` 필드만 한국어로 번역되었습니다.
- `from` 필드(예: "human", "gpt")는 원본 그대로 유지됩니다.
- `source` 및 `score` 컬럼은 원본 데이터셋과 동일하게 유지됩니다.

##### 데이터 구조
```python
{
    "conversations": [
        {"from": "human", "value": "한국어로 번역된 질문..."},
        {"from": "gpt", "value": "한국어로 번역된 답변..."}
    ],
    "source": "원본 출처",
    "score": 0.95
}
```

#### 사용 방법

```python
from datasets import load_dataset

dataset = load_dataset("neuralfoundry-coder/FineTome-100k-ko-minimal", split="train")
print(dataset)
print(dataset[0])
```

#### 면책 조항

이 데이터셋은 `mlabonne/FineTome-100k` 데이터셋을 기반으로 하며, 번역 과정에서 발생할 수 있는 모든 오류나 부정확성에 대한 책임은 사용자에게 있습니다. **데이터셋 사용으로 인해 발생하는 모든 결과에 대한 책임은 사용자에게 있음을 명시합니다.**

#### 라이선스

이 번역된 데이터셋은 원본 `mlabonne/FineTome-100k` 데이터셋의 라이선스인 Apache-2.0을 따릅니다.
