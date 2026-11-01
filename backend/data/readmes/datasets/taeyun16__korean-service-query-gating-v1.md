---
language:
- ko
license: mit
configs:
- config_name: core
  default: true
  data_files:
  - split: train
    path: core/train.jsonl
  - split: validation
    path: core/validation.jsonl
  - split: test
    path: core/test.jsonl
- config_name: stress_eval
  data_files:
  - split: train
    path: stress_eval/train.jsonl
task_categories:
- text-classification
- text-retrieval
pretty_name: Korean Service Query Gating V1
size_categories:
- 1K<n<10K
tags:
- synthetic
- korean
- ood-detection
- routing
- helpdesk
---

# Korean Service Query Gating V1

한국어 서비스 질의 게이팅 연구를 위한 합성 데이터셋입니다.

현실의 서비스 회사에서는 질문 분해, 도메인 판별, 라우팅 같은 태스크가 매우 중요하지만, 실제 질의 로그는 개인정보와 내부 정책 문제 때문에 공개하기 어렵습니다.  
이 데이터셋은 그런 제약 아래에서도 재현 가능한 연구를 시작할 수 있도록 만든 **공개 가능한 Korean starting benchmark**입니다.

쉽게 말해 이 데이터셋은 아래 질문을 연구하기 위한 리소스입니다.

- “이 질문이 우리 서비스 범위 안인가, 밖인가?”
- “겉보기엔 비슷한데 실제 의미는 다른 질문을 어떻게 구분할까?”
- “모델이 어떤 실패 유형에서 흔들리는가?”

## Quick Summary

- 언어: 한국어
- 용도: 서비스 질의 게이팅 / 헬프데스크 질의 분류 / OOD stress evaluation
- 구성: `core` + `stress_eval`
- 성격: 합성 연구용 데이터셋

## Friendly Glossary

- `ID` (In-Domain)
  - 모델이 원래 처리해야 하는 질문
  - 이 데이터셋에서는 IT 헬프데스크 질문을 뜻합니다.
- `OOD` (Out-of-Domain)
  - 모델이 원래 처리 범위 밖이라고 판단해야 하는 질문
  - 예: 날씨, 여행, 쇼핑, 음식
- `OOD hard`
  - 단어만 보면 IT 같지만 실제 의미는 IT가 아닌 질문
- `gate`
  - 질문을 먼저 빠르게 거르는 1차 판단기
- `gray-zone`
  - 모델이 확신하지 못해서 2차 검토로 넘길 수 있는 애매한 구간
- `keyword_trap`
  - `로그인`, `계정`, `업데이트`처럼 IT 단어가 들어 있어 모델이 속기 쉬운 케이스
- `mixed_intent`
  - 한 질문 안에 서로 다른 의도가 섞인 경우
- `needs_context`
  - 질문이 너무 짧거나 맥락이 부족해서 사람도 바로 판단하기 어려운 경우

## Structure

```text
core/train.jsonl
core/validation.jsonl
core/test.jsonl
stress_eval/train.jsonl
metadata/stress_eval_summary.json
supplemental/raw/
supplemental/prompts/
```

## Datasets

이 리포지토리에는 두 개의 주요 데이터셋이 있습니다.

### 1. `core`

`core/`는 메인 실험용 canonical split입니다.

- `core/train.jsonl`
- `core/validation.jsonl`
- `core/test.jsonl`

여기에는 세 종류의 질문이 섞여 있습니다.

- `id`: IT 헬프데스크 질의
- `ood_easy`: 명백한 비IT 질의
- `ood_hard`: IT 키워드를 포함하지만 실제 의미는 비IT인 질의

초보자 관점에서 보면 `core`는:

- “기본 모델이나 threshold를 맞춰보는 데 쓰는 메인 데이터셋”
- “무엇이 잘 되는지 보기 좋은 셋”

입니다.

canonical split은 row-level random split이 아니라 `label + subcategory + text prefix` 기반 grouped split으로 만들었다.  
또한 `id`와 `ood_easy`에는 반복적인 opening/template를 줄이는 표면 다양화 보정을 적용했다.

즉, 단순히 “합성 데이터를 많이 만든 것”이 아니라,  
**가설 검증에 너무 쉬워지지 않도록 한 번 더 손본 메인 연구용 셋**입니다.

### 2. `stress_eval`

`stress_eval/train.jsonl`는 failure mode 진단용 보조 평가셋입니다.

핵심 필드:

- `text`
- `label`
- `primary_tag`
- `secondary_tags`
- `difficulty`
- `scenario`
- `subcategory`
- `keywords`

라벨:

- `id`
- `ood`
- `uncertain`

대표 시나리오:

- `ood_keyword_trap`
- `too_short_id`
- `too_short_ood`
- `too_short_uncertain`
- `uncertain_mixed_intent`
- `uncertain_needs_context`

이 셋은 “평균 점수가 잘 나오는지”보다

- 모델이 키워드에 속는지
- 너무 짧은 질문에서 흔들리는지
- 한 문장에 두 의도가 섞이면 무너지는지
- 맥락이 부족할 때 과감하게 틀리는지

를 확인하기 위한 평가셋입니다.

즉, `stress_eval`은:

- “어디서 망가지는지 보기 좋은 셋”
- “failure mode를 설명하기 좋은 셋”

입니다.

## Provenance

최종 canonical v1은 단순 프롬프트 출력물이 아닙니다.

1. source prompts로 원천 synthetic raw 생성
2. 일부 클래스(`id`, `ood_easy`)에 대해 반복 표현을 줄이는 후처리 적용
3. train/test가 너무 비슷해지지 않도록 grouped split 재구성

즉 `supplemental/prompts/`는 원천 생성에 사용된 프롬프트이며,  
최종 v1은 그 raw에 후처리와 canonical split 정책을 더한 결과물입니다.

## Recommended Usage

- 구조 탐색/튜닝:
  - `core/`
- stress evaluation:
  - `stress_eval/train.jsonl`

처음 시작할 때는 보통 이렇게 씁니다.

1. `core`로 기본 모델을 학습하거나 threshold를 맞춘다.
2. `stress eval`로 실제로 어디서 실수하는지 본다.
3. 나중에 실데이터가 있으면 그걸로 최종 검증한다.

## Quick Start

허깅페이스에서 가장 일반적으로는 `datasets` 라이브러리로 바로 읽습니다.

예시:

```python
from datasets import load_dataset

dataset = load_dataset("taeyun16/korean-service-query-gating-v1")

print(dataset)
print(dataset["train"][0])
```

`stress_eval`을 읽고 싶다면 config를 지정하면 됩니다.

```python
from datasets import load_dataset

stress = load_dataset(
    "taeyun16/korean-service-query-gating-v1",
    "stress_eval",
    split="train",
)

keyword_trap = stress.filter(lambda row: row["primary_tag"] == "keyword_trap")
print(len(keyword_trap))
```

로컬 JSONL을 직접 읽고 싶다면 이렇게도 할 수 있습니다.

```python
import json
from pathlib import Path

rows = [
    json.loads(line)
    for line in Path("core/train.jsonl").open(encoding="utf-8")
    if line.strip()
]
```

## Limitations

- 합성 데이터라 템플릿 편향이 남아 있습니다.
- 한국어 기업형 헬프데스크 맥락에 최적화돼 있습니다.
- 실제 운영 로그 기반 최종 검증을 대체하지는 못합니다.

그래서 이 데이터셋은  
**실서비스를 그대로 대표하는 benchmark**라기보다,

- 공개 가능한 Korean starting benchmark
- failure-mode-aware research dataset
- real-world validation 이전 단계의 연구 리소스

로 보는 것이 가장 적절합니다.

## Citation

이 데이터셋을 사용한다면 아래 형식으로 참조할 수 있습니다.

```bibtex
@misc{korean_service_query_gating_v1,
  title = {Korean Service Query Gating V1},
  year = {2026},
  note = {Synthetic Korean benchmark for embedding-gate and service-query routing research}
}
```
