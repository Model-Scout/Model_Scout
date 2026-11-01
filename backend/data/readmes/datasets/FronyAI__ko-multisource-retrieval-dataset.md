---
language:
- ko
task_categories:
- text-retrieval
- sentence-similarity
tags:
- retrieval
- korean
- embedding
size_categories:
- 100K<n<1M
dataset_info:
- config_name: stage1
  features:
  - name: dataset
    dtype: large_string
  - name: query
    dtype: large_string
  - name: passage
    dtype: large_string
  splits:
  - name: train
    num_bytes: 145604026
    num_examples: 100001
  - name: valid
    num_bytes: 14553095
    num_examples: 9999
  download_size: 95054902
  dataset_size: 160157121
- config_name: stage2
  features:
  - name: query
    dtype: large_string
  - name: positive
    dtype: large_string
  - name: negative
    dtype: large_string
  splits:
  - name: train
    num_bytes: 83799175
    num_examples: 100000
  - name: valid
    num_bytes: 8317990
    num_examples: 10000
  download_size: 55485343
  dataset_size: 92117165
configs:
- config_name: stage1
  data_files:
  - split: train
    path: stage1/train-*
  - split: valid
    path: stage1/valid-*
- config_name: stage2
  data_files:
  - split: train
    path: stage2/train-*
  - split: valid
    path: stage2/valid-*
---

## 구성

- 여러 공개 출처를 하나의 스키마로 통합한 한국어 query–passage 페어 데이터셋입니다.
- `stage1`, `stage2` 두 subset. 각각 train 100,000 / valid 10,000행 (총 220,000행, parquet, 151MB)

| 필드 | 설명 |
|---|---|
| `dataset` | 원 출처 식별자 (18종) |
| `query` | 질의문 (2~2,020자) |
| `passage` | 대응 문서 (10~2,050자) |

## 출처

- **AI 허브** — `기계독해` `지식검색` `일반상식` `도서자료` `행정문서` `뉴스기사` `금융법률` `숫자연산` `표정보` `추상요약` `이벤트` (`AI허브_` 접두사)
- **KLUE** — `klue-mrc` `klue-nli` `klue-sts`
- **기타** — `kakao-nli` `공공데이터포털-deepqa` `LGNLP`

## 참고

출처별로 페어 성격이 다르므로 용도에 맞게 필터링을 권장합니다.

- `klue-nli` `klue-sts` `kakao-nli` — NLI/STS 유래. 짧은 문장 ↔ 짧은 문장
- `AI허브_추상요약` — `query`가 원문, `passage`가 요약문으로 길이 방향이 반대
- `AI허브_표정보` `LGNLP` — passage에 마크다운 표 포함

```python
from datasets import load_dataset

ds = load_dataset("FronyAI/ko-multisource-retrieval-dataset", "stage1")
mrc = ds["train"].filter(lambda x: x["dataset"] == "AI허브_기계독해")
```

## 라이선스

출처별 원 라이선스가 그대로 적용됩니다.

- **AI 허브** — 과학기술정보통신부·한국지능정보사회진흥원 「지능정보산업 인프라 조성」 사업 결과물. 이용 시 출처 표기 필요하며 2차적 저작물에도 동일 적용. [이용정책](https://aihub.or.kr/intrcn/guid/usagepolicy.do)
- **KLUE** — CC BY-SA 4.0 (동일조건변경허락)
