---
language:
  - ko
license: cc-by-4.0
task_categories:
  - token-classification
task_ids:
  - named-entity-recognition
tags:
  - korean
  - pii
  - ner
  - privacy
  - de-identification
  - synthetic
size_categories:
  - 10K<n<100K
configs:
  - config_name: default
    data_files:
      - split: train
        path: train.jsonl
      - split: validation
        path: valid.jsonl
      - split: test
        path: test.jsonl
      - split: test_kdpii
        path: test_kdpii.jsonl
---

# 한국 PII 특화 학습용 데이터셋 (ko_pii_v1)

> 한국 고유 식별자와 조사 결합 경계를 정면으로 다루는 한국어 PII NER 학습 데이터셋.

## 1. 개요

- 학습용 **98,845건** + 외부 평가용 홀드아웃 **2,006건**
- 라벨 **20종 3티어** / BIO 41 클래스
- 시드 `42`, 검증자릿수 정책 `invalid`, 사용 티어 `[1, 2, 3]`
- 포맷: JSONL. `{id, text, spans:[{start,end,label,value}], meta}`
- 이 레포의 `NERPreprocessor` span 포맷과 동일해 학습 경로 수정 없이 사용 가능

## 1-1. 이 데이터셋으로 학습한 모델

[`seongyeon1/ko-pii-ner-roberta-base`](https://huggingface.co/seongyeon1/ko-pii-ner-roberta-base)
(klue/roberta-base 파인튜닝, CC-BY-SA-4.0)

**학습에 한 번도 쓰이지 않은 KDPII 공식 test split 기준 F5 0.9344.**
내부 test 전체 F5는 0.9937이지만 그 절반 이상이 합성 구간이고 거기서 F1이 0.9994라,
그 수치는 실제 성능이 아니다. 자세한 내용은 모델 카드를 참고할 것.

## 1-2. 불러오기

```python
from datasets import load_dataset

ds = load_dataset("seongyeon1/ko-pii-ner-100k")
print(ds["train"][0])
# {"id": "kopii-l3c-000123",
#  "text": "...",
#  "spans": [{"start": 12, "end": 26, "label": "RRN", "value": "900101-1234567"}],
#  "meta": {"layer": "L3", "domain": "medical", ...}}
```

span은 문자 offset 기준이며 `text[start:end] == value`가 전체 레코드에서 100% 성립한다.

## 1-3. 평가용 split — `test_kdpii`

KDPII가 공식 지정한 test split을 그대로 뺀 **2,006건**(span 3,895개)이다.
학습·검증·내부 test 어디에도 들어가지 않으며, 빌드 시 본 split과의
텍스트 해시 교집합이 0인지 검사한다.

**KDPII를 쓰는 다른 연구와 같은 평가셋에서 비교하려면 이 split을 쓸 것.**
`test.jsonl`은 합성 레이어가 절반을 넘어 실제 성능을 과대평가한다.

## 2. 구성

| split | 문서 | span | 무-PII 비율 |
|---|---:|---:|---:|
| train | 78,963 | 366,438 | 6.0% |
| valid | 9,994 | 45,745 | 6.1% |
| test | 9,888 | 45,292 | 6.1% |
| **test_kdpii** (외부 평가) | 2,006 | 3,895 | 0.1% |

### 레이어별 분포

| 레이어 | 설명 | train | valid | test |
|---|---|---:|---:|---:|
| L1 | KDPII 대화 (원본 재활용) | 3,298 | 412 | 413 |
| L1b | KDPII PII 포함 단문 (원본 재활용) | 11,551 | 1,456 | 1,417 |
| L2 | ai4privacy 한국어 문맥 + PII 값 한국화 재주입 | 16,798 | 2,100 | 2,100 |
| L3 | 합성 (문장 조각 조합형 + 템플릿형) | 42,676 | 5,446 | 5,378 |
| L4 | 무-PII 문서 (hard negative 전용) | 4,640 | 580 | 580 |

### 도메인별 분포 (train)

| 도메인 | 문서 |
|---|---:|
| translated_doc | 16,798 |
| dialogue | 14,849 |
| customer_support | 7,236 |
| recruiting | 7,165 |
| internal_mail | 7,088 |
| public_service | 7,071 |
| finance | 7,063 |
| medical | 7,053 |
| negative | 4,640 |

## 3. 라벨 분포

| 라벨 | 티어 | train | valid | test |
|---|---:|---:|---:|---:|
| `RRN` | 1 | 19,658 | 2,451 | 2,440 |
| `FOREIGNER_REG_NUM` | 1 | 10,237 | 1,325 | 1,247 |
| `PASSPORT_NUM` | 1 | 12,662 | 1,656 | 1,535 |
| `DRIVER_LICENSE_NUM` | 1 | 13,341 | 1,699 | 1,711 |
| `PERSON_NAME` | 2 | 61,638 | 7,643 | 7,674 |
| `PHONE_NUM` | 2 | 28,968 | 3,572 | 3,555 |
| `EMAIL` | 2 | 27,474 | 3,407 | 3,349 |
| `ADDRESS` | 2 | 32,067 | 3,978 | 4,052 |
| `ACCOUNT_NUM` | 2 | 16,341 | 2,122 | 2,026 |
| `CARD_NUM` | 2 | 16,399 | 2,036 | 1,954 |
| `BIZ_REG_NUM` | 2 | 10,771 | 1,295 | 1,321 |
| `USER_ID` | 2 | 10,497 | 1,259 | 1,270 |
| `URL_PERSONAL` | 2 | 13,119 | 1,692 | 1,704 |
| `PLATE_NUM` | 2 | 10,678 | 1,415 | 1,347 |
| `IP_ADDRESS` | 2 | 10,329 | 1,314 | 1,275 |
| `DOB` | 3 | 10,921 | 1,382 | 1,445 |
| `AGE` | 3 | 14,364 | 1,810 | 1,761 |
| `AFFILIATION` | 3 | 21,635 | 2,600 | 2,554 |
| `POSITION` | 3 | 14,121 | 1,738 | 1,701 |
| `SENSITIVE_ATTR` | 3 | 11,218 | 1,351 | 1,371 |

티어별 합계

| 티어 | 이름 | train | valid | test |
|---|---|---:|---:|---:|
| 1 | 고유식별정보 | 55,898 | 7,131 | 6,933 |
| 2 | 직접식별자 | 238,281 | 29,733 | 29,527 |
| 3 | 준식별자·민감정보 | 72,259 | 8,881 | 8,832 |

## 4. 생성 방법

```bash
python script/build_ko_pii_dataset.py --config configs/ko_pii_dataset.yaml
```

시드 `42` 고정으로 완전히 재현된다. 레이어별 목표 수량:

```
l1: 4,500
l1b: 15,000
l2: 21,000
l3_composed: 51,500
l3_template: 2,000
l4: 6,000
```

빌드는 다음 검증 게이트를 모두 통과해야만 파일을 쓴다.

1. offset 무결성 `text[start:end] == value` — 100% (`PiiRecord` 생성 시 강제)
2. span 겹침 0건 (`PiiRecord` 생성 시 강제)
3. 라벨 화이트리스트 (`KoPiiLabel` 타입으로 구조적 보장)
4. split 간 텍스트 누수 0건 — 대화 ID·조합 ID 단위 분리
5. 근접중복률 ≤ 5%
6. Tier 1 각 엔티티 train ≥ 3,000 / test ≥ 300
7. 무-PII 문서 비율 5~10%

## 5. 라이선스와 귀속

본 데이터셋은 **CC-BY-4.0**을 따른다. 원본 두 소스가 모두 CC-BY-4.0이므로 파생물도 동일하며, **원저작자 귀속 표기가 의무**다.

- **KDPII** — *KDPII: A New Korean Dialogic Dataset for the Deidentification of Personally Identifiable Information*, IEEE Access, 2024. Zenodo DOI [10.5281/zenodo.10968609](https://doi.org/10.5281/zenodo.10968609). CC-BY-4.0
- **ai4privacy** — [`pii-masking-openpii-1.5m`](https://huggingface.co/datasets/ai4privacy/pii-masking-openpii-1.5m), Copyright (c) 2026 Ai Suisse SA. CC-BY-4.0

## 6. 안전 고지

- 모든 PII 값은 **합성**이다. 실제 개인정보는 어떤 경로로도 포함되지 않는다.
- 주민등록번호·사업자등록번호·카드번호는 **검증자릿수가 의도적으로 틀리다** (`checksum: invalid`). 자릿수·구분자·앞자리 규칙은 실제와 같지만 실제 번호로는 사용할 수 없다. 검증식까지 유효한 값을 대량 생성하면 실존 인물의 번호와 구조적으로 구분되지 않기 때문이다.
- 주소는 시·도·시군구까지만 실제 지명이고 도로명·건물번호·상세주소는 조합 생성이다. 시·도와 시군구는 실제 행정구역 관계로 묶여 있어 '충청북도 종로구' 같은 조합이 나오지 않는다.
- L2의 원본 PII 값(기계번역 산물)은 전부 폐기되고 한국 포맷으로 새로 생성된 값으로 대체되었다.

## 7. 한계

- **합성 구간과 실제 발화의 성능 격차가 크다.** 이 데이터로 학습한 모델을 `test.jsonl`로 재면 합성 구간 F5가 0.999에 붙지만, 실제 발화(`test_kdpii`)에서는 0.93 수준이다. 서로 다른 베이스 모델 두 종에서 동일하게 재현됐다. **`test.jsonl` 전체 수치를 실제 성능으로 인용하지 말 것.**
- **ai4privacy 한국어는 21,225건이 상한이다.** train split 1,309,912행을 전수 스캔한 결과 정확히 21,225건이었고, 20만 행 지점 이후로는 한 건도 늘지 않았다. 데이터셋이 언어별로 블록 정렬되어 있어 한국어가 앞쪽에 몰려 있다. L2를 21,000건으로 맞추고 부족분은 합성으로 채웠다.
- **L2는 기계번역 기반 문맥이라 문체가 다소 정형적이다.** 문장 구조는 원본을 따르고 PII 값만 한국화했다.
- **템플릿형 합성(L3 템플릿)은 고유 문맥이 82개뿐이다.** 손으로 쓴 템플릿 50종은 PII 값만 바뀌므로 소량(2,000건)만 섞었고, 주력은 문장 조각 조합형(51,500건)이다. 조합형은 도메인당 1억 7천만 조합을 갖는다.
- **Tier 3(준식별자)은 문맥 의존적이라 라벨 경계가 Tier 1·2보다 모호하다.** `configs/ko_pii_dataset.yaml`의 `tiers: [1, 2]`로 제외할 수 있다.
- **512 토큰 초과로 잘리는 span 비율: 0.019% (train 20% 표본, klue/roberta-large, max_length=512).**
- KDPII는 대화체라 문체 폭이 좁고, 합성 레이어는 문서·서식 위주다. 실사용 분포와 완전히 같지는 않다.
