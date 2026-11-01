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
- ner
- spacy
pretty_name: Korean NER Dataset (spaCy format)
---

# Korean NER Dataset (spaCy format)

한국어 NER(Named Entity Recognition) 학습을 위해 여러 공개 데이터셋을 수집·변환한 데이터셋입니다.

> 변환 스크립트 및 상세 문서: [GitHub - HERIUN/kor_ner_spacy_data](https://github.com/HERIUN/kor_ner_spacy_data)

## 데이터 형식

각 줄은 하나의 문장이며 JSONL 형식입니다.

```json
{"text": "홍길동이 서울에 산다.", "entities": [[0, 3, "PER"], [5, 7, "LOC"]]}
```

- `text` : 원문 문장
- `entities` : `[start, end, label]` 리스트
  - `start` : 0-based, inclusive
  - `end` : exclusive (Python slice 기준)

## 파일 구성

| 파일 | 원본 데이터 | 레코드 수 |
|------|------------|----------:|
| `data/094_ner_dataset.jsonl` | AIHub 관광 특화 말뭉치 | 907,787 |
| `data/208_ner_dataset.jsonl` | AIHub 전시 공연 도슨트 | 981 |
| `data/naver_ner_dataset.jsonl` | 네이버 NER 데이터셋 | 67,800 |
| `data/kmou_ner_dataset.jsonl` | 말뭉치 - 형태소_개체명 | 18,659 |
| **합계** | | **995,227** |

## 태그 체계

| 태그 | 의미 |
|:----:|------|
| `PER` | 인물 |
| `ORG` | 기관 |
| `LOC` | 장소 |
| `DAT` | 날짜·기간 |
| `TIM` | 시간 |
| `QT` | 수량·금액·퍼센트 |
| `ADD` | 주소 (094 전용) |
| `PHN` | 전화번호 (094 전용) |
| `URL` | 웹 주소 (094 전용) |

## 엔티티 통계

| 태그 | 건수 | 비율 |
|:----:|-----:|-----:|
| `LOC` | 723,199 | 44.00% |
| `QT` | 224,596 | 13.67% |
| `DAT` | 168,670 | 10.26% |
| `ADD` | 129,320 | 7.87% |
| `ORG` | 116,121 | 7.07% |
| `PER` | 92,001 | 5.60% |
| `PHN` | 91,674 | 5.58% |
| `URL` | 67,166 | 4.09% |
| `TIM` | 30,651 | 1.87% |
| **합계** | **1,643,398** | **100%** |

## 원본 데이터 출처

- [AIHub - 관광 특화 말뭉치 데이터](https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71714)
- [AIHub - 전시 공연 도슨트 데이터](https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71323)
- [GitHub - naver/nlp-challenge NER](https://github.com/naver/nlp-challenge/tree/master/missions/ner)
- [GitHub - 한국해양대](https://github.com/kmounlp/NER)
