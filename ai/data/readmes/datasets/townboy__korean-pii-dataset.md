---
language:
- ko
task_categories:
- token-classification
tags:
- korean
- pii
- synthetic-data
- named-entity-recognition
license: cc-by-4.0
pretty_name: Korean Synthetic PII Dataset
configs:
- config_name: raw
  default: true
  data_files:
  - split: train
    path: data/train.jsonl
  - split: validation
    path: data/validation.jsonl
  - split: test
    path: data/test.jsonl
- config_name: bio
  data_files:
  - split: train
    path: bio/train.jsonl
  - split: validation
    path: bio/validation.jsonl
  - split: test
    path: bio/test.jsonl
---

# Korean Synthetic PII Dataset

한국어 문장 안의 개인정보(PII)를 탐색·분석하거나 토큰 분류 모델을 학습할 수 있도록 제작한 합성 데이터셋입니다. 모든 이름·번호·주소와 문장은 합성 값이며 실제 개인의 개인정보를 의도적으로 포함하지 않았습니다.

## 라이선스

이 데이터셋은 [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)으로 제공합니다. 재배포·수정·상업적 이용이 가능하지만, `townboy/korean-pii-dataset`과 원 저작자를 표시해야 합니다. 라이선스 전문은 저장소의 `LICENSE` 파일을 확인하세요.

## 구성

| 항목 | 수량 |
|---|---:|
| 전체 문서 | 11,732 |
| Train | 9,227 |
| Validation | 1,510 |
| Test | 995 |
| PII span | 55,627 |
| PII 유형 | 33 |
| BIO 라벨 | 67 (`O` 포함) |
| 최대 토큰 길이 | 511 |

`dataset_stats.json`에는 split·라벨별 상세 통계가 들어 있습니다.

## Hugging Face에서 불러오기

사람이 읽을 수 있는 원문과 문자 위치 span이 필요하면 기본 `raw` 구성을 사용합니다.

```python
from datasets import load_dataset

dataset = load_dataset("townboy/korean-pii-dataset", "raw")
print(dataset["train"][0])
```

KPF-BERT 토크나이저로 변환된 BIO 학습 입력이 필요하면 `bio` 구성을 사용합니다.

```python
from datasets import load_dataset

dataset = load_dataset("townboy/korean-pii-dataset", "bio")
print(dataset["train"][0]["input_ids"])
```

## 파일

- `corpus_all.jsonl`: 세 split을 합친 원문·span 데이터
- `corpus_all_bio.jsonl`: 세 split을 합친 KPF-BERT BIO 데이터
- `data/{train,validation,test}.jsonl`: Viewer와 `load_dataset()`용 원문 구성
- `bio/{train,validation,test}.jsonl`: Viewer와 `load_dataset()`용 BIO 구성
- `label_map.json`: BIO 라벨과 정수 ID의 양방향 매핑
- `dataset_stats.json`: split 및 라벨별 통계

합본과 split 파일은 별개의 데이터가 아닙니다. `corpus_all.jsonl`을 `split` 필드로 나눈 것이 `data/` 아래의 세 파일이며, BIO도 동일합니다.

## Raw 스키마

```json
{
  "id": 100,
  "source_text": "회원 이름은 홍길동이고 이메일은 hong@example.com입니다.",
  "privacy_mask": [
    {"label": "NAME", "value": "홍길동", "start": 7, "end": 10, "label_index": 1},
    {"label": "EMAIL", "value": "hong@example.com", "start": 17, "end": 33, "label_index": 1}
  ],
  "language": "ko",
  "region": "KR",
  "split": "train"
}
```

`start`는 Python 문자열의 0-based 시작 위치이고 `end`는 exclusive 끝 위치입니다. 따라서 항상 아래 조건을 만족합니다.

```python
source_text[start:end] == value
```

## BIO 스키마

각 행에는 다음 필드가 있습니다.

- `id`, `split`
- `input_ids`
- `token_type_ids`
- `attention_mask`
- `labels`

`labels`는 `B-LABEL`, `I-LABEL`, `O`를 정수로 변환한 배열입니다. `-100`은 special token처럼 loss 계산에서 제외할 위치입니다. 각 배열의 길이는 동일하고 512를 넘지 않습니다.

## PII 라벨 33종

`ACCOUNT_NUMBER`, `ADDRESS`, `AGE`, `ALIEN_NUMBER`, `BIRTHDATE`, `BLOOD_TYPE`, `CARD_NUMBER`, `CITY`, `DEPARTMENT`, `DRIVER_LICENSE`, `EMAIL`, `EMPLOYEE_ID`, `GENDER`, `HEIGHT`, `IP_ADDRESS`, `MAJOR`, `MEMBER_ID`, `NAME`, `NATIONALITY`, `NICKNAME`, `PARTICIPANT_ID`, `PASSPORTNUM`, `PHONE`, `POSITION`, `RELIGION`, `RRN`, `SCHOOL`, `URL`, `USER_ID`, `VEHICLE_NUMBER`, `WEIGHT`, `WORKPLACE`, `ZIPCODE`.

## 데이터 품질 개선 사항

- 주민등록번호는 출생 연도와 성별 코드 `1`~`4`의 의미가 일치하도록 생성했습니다.
- 외국인등록번호는 성별 코드 `5`~`8`과 구 외국인등록번호 체크섬 규칙을 적용했습니다.
- 카드번호에는 Luhn 검증을 적용한 예시를 포함했습니다.
- 라벨 안내어가 없는 표·목록·CSV·JSON 형태와 여러 PII가 함께 나타나는 문서를 포함했습니다.
- RRN/외국인등록번호 주변의 문맥 단어가 실제 7번째 자리와 충돌하는 counterfactual train 480행을 포함했습니다.
- RRN과 외국인등록번호가 한 문서에 함께 등장하는 무라벨 구조화 train 500행을 포함했습니다.
- 긴 문서 학습을 위해 BIO 입력 길이를 최대 512 토큰으로 확장했습니다.
- 학습용 hard negative에는 PII처럼 보이지만 대상 라벨이 아닌 일반 코드 문맥을 포함했습니다.

## Split 사용 시 주의

현재 `train/validation/test`는 실제 모델 학습에 사용한 고정 split을 재현하기 위해 그대로 공개합니다. 라벨 분포가 균등한 벤치마크 split은 아닙니다. 특히 일부 희소 라벨은 공개 test에 거의 없거나 없으므로 `test`만으로 라벨별 성능을 판단하면 안 됩니다.

공개 모델의 최종 평가는 이 corpus와 템플릿·값이 겹치지 않는 별도의 합성 holdout에서 라벨별 양성 100개를 사용했습니다. 최종 holdout은 반복적인 튜닝과 데이터 오염을 막기 위해 공개 학습 corpus에 합치지 않았습니다.

## 한계

- 합성 문장과 실제 RAG 응답·업무 문서의 표현 및 분포는 다를 수 있습니다.
- 제한된 생성 규칙이나 반복되는 표현이 남아 있을 수 있습니다.
- 이름·닉네임·직급·사용자 ID처럼 문맥 의존성이 큰 라벨은 도메인이 달라지면 성능 저하가 클 수 있습니다.
- 이 데이터셋이나 이를 학습한 모델만으로 개인정보 보호를 보장할 수 없습니다.
