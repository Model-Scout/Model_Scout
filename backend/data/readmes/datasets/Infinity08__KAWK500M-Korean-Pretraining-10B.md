---
language:
- ko
license: other
task_categories:
- text-generation
tags:
- korean
- pretraining
- tokenized
- parquet
- streaming
- llama
size_categories:
- 1M<n<10M
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train/part-*/*.parquet
  - split: validation
    path: data/validation/part-*/*.parquet
---

# KAWK500M Korean Pretraining 10B

한국어 중심 500M급 decoder-only 모델을 처음부터 학습하기 위한 사전 토큰화
데이터입니다. 각 행의 `input_ids`는 `uint16[2049]`이며 앞의
2,048개 토큰을 causal-LM 입력·레이블로 사용합니다.

## 크기

- train: 5,075,616 rows / 10,399,937,184 stored tokens /
  10,394,861,568 effective 2048-token training positions
- validation: 9,761 rows / 20,000,289 stored tokens
- tokenizer: 한국어 SentencePiece Unigram 32K, NFC + identity + byte fallback
- 원천 데이터: `HuggingFaceFW/fineweb-2`, `kor_Hang`
- 고정 revision: `af9c13333eb981300149d5ca60a8e9d659b276b9`
- FineWeb2의 전역 MinHash 중복 제거 이후 한국어 품질·반복·코드·수식·PII 필터 적용
- 영어·코드 전용 데이터는 포함하지 않으며 한국어 문서에 자연스럽게 포함된
  영문·숫자·기호만 유지

train과 validation은 FineWeb2 스트림의 서로 겹치지 않는 contiguous partition에서
만들었습니다. 원문 텍스트는 이 저장소에 포함하지 않습니다.

## Streaming

```python
from datasets import load_dataset
import torch

dataset = load_dataset(
    "Infinity08/KAWK500M-Korean-Pretraining-10B",
    split="train",
    streaming=True,
).shuffle(seed=42, buffer_size=10_000)

row = next(iter(dataset))
tokens = torch.tensor(row["input_ids"], dtype=torch.long)
input_ids = tokens[:-1]
labels = input_ids.clone()
```

전체 데이터 다운로드 없이 Parquet row group을 순차적으로 읽습니다. 정확한 학습
재개를 위해 trainer 체크포인트에 Hugging Face `IterableDataset.state_dict()`도
함께 저장해야 합니다.

## 라이선스와 주의사항

원천 FineWeb2는 ODC-By-1.0으로 배포되며 Common Crawl 이용 조건도 적용됩니다.
이 토큰 데이터는 원천 조건을 제거하거나 단일 라이선스로 재허가하지 않습니다.
웹 데이터에는 필터가 놓친 개인정보, 유해 문장, 편향 및 평가 데이터와 유사한
문장이 남을 수 있으므로 사용자가 추가 감사를 수행해야 합니다.
