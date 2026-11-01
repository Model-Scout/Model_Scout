---
dataset_info:
  features:
    - name: 문제
      dtype: string
    - name: 답변
      dtype: string
    - name: 프로그램명
      dtype: string
  splits:
    - name: test
      num_bytes: 30138
      num_examples: 100
  download_size: 10155
  dataset_size: 30138
configs:
  - config_name: default
    data_files:
      - split: test
        path: data/test-*
license: mit
language:
  - ko
source_datasets:
  - umiyuki/Ani-Bench-JP
---

# Ani-Bench-JP-ko

## 데이터셋 개요

`Ani-Bench-JP-ko`는 일본의 인기 애니메이션에 관한 지식을 측정하기 위한 `Ani-Bench-JP`의 한국어 버전 벤치마크 데이터셋입니다. 이 데이터셋은 5개의 애니메이션 작품(『마법소녀 마도카☆마기카』, 『봇치 더 록!』, 『기동전사 건담』, 『HUNTER×HUNTER』, 『신세기 에반게리온』)에서 각각 20문제씩, 총 100문제의 퀴즈 형식 문제로 구성되어 있습니다.
LLM의 애니메이션 관련 이해도를 한국어로 평가하는 용도를 상정하고 있습니다.

## 데이터 구조

데이터는 Parquet 형식으로 제공되며, `test` 스플릿으로 업로드되어 있습니다. 파일에는 다음 3개의 열이 포함됩니다:

- **문제**: 애니메이션 관련 퀴즈 질문
- **답변**: 해당 질문에 대한 정답
- **프로그램명**: 질문과 관련된 애니메이션 작품 제목

### 열 상세

| 열 이름    | 설명                   | 예시                        |
| ---------- | ---------------------- | --------------------------- |
| 문제       | 퀴즈 질문 문장         | 주인공의 이름은 무엇입니까? |
| 답변       | 질문에 대한 정답       | 카나메 마도카               |
| 프로그램명 | 관련 애니메이션 타이틀 | 마법소녀 마도카☆마기카      |

## 사용 방법

이 데이터셋은 Hugging Face의 `datasets` 라이브러리를 사용하여 쉽게 로드할 수 있습니다. 다음은 Python 사용 예시입니다:

```python
from datasets import load_dataset

dataset = load_dataset("ychoikr/Ani-Bench-JP-ko", split="test")
print(dataset[0])
```

## 수록 애니메이션

- **마법소녀 마도카☆마기카**
- **봇치 더 록!**
- **기동전사 건담**
- **HUNTER×HUNTER**
- **신세기 에반게리온**

각 애니메이션에서 20문제씩, 총 100문제가 포함되어 있습니다.

## 목적

- LLM(특히 한국어 모델)의 이해력 및 지식 평가

## 크레딧

이 데이터셋은 `umiyuki`가 제작한 `Ani-Bench-JP`를 기반으로 번역 및 가공되었습니다.
