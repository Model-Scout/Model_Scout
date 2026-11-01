---
language:
- ko
license: cc-by-4.0
size_categories:
- 1K<n<10K
task_categories:
- text-classification
task_ids:
- topic-classification
tags:
- korean
- news
- synthetic
- topic-classification
- education
pretty_name: Korean News Topic Classification (Synthetic)
dataset_info:
  features:
  - name: text
    dtype: string
  - name: label
    dtype:
      class_label:
        names:
          '0': 경제
          '1': 사회
          '2': 생활문화
          '3': IT과학
  - name: label_name
    dtype: string
  splits:
  - name: train
    num_bytes: 450000
    num_examples: 5000
  - name: validation
    num_bytes: 45000
    num_examples: 500
  - name: test
    num_bytes: 45000
    num_examples: 500
  download_size: 540000
  dataset_size: 540000
---

# Korean News Topic Classification Dataset (Synthetic)

한국어 뉴스 토픽 분류를 위한 합성 데이터셋입니다.

## Dataset Description

이 데이터셋은 자연어처리 실습을 위해 제작된 **교육용 합성 데이터셋**입니다.

### Dataset Summary

- **언어**: 한국어 (Korean)
- **도메인**: 뉴스 헤드라인 스타일
- **태스크**: 4-class 텍스트 분류 (Topic Classification)
- **생성 방식**: 템플릿 기반 합성 데이터 (Synthetic)

### Supported Tasks

- **Text Classification**: 주어진 문장을 4개 카테고리 중 하나로 분류
- **N-to-1 Task**: 입력 시퀀스 -> 단일 클래스 레이블

### Languages

한국어 (Korean, ko)

## Dataset Structure

### Data Instances

```json
{
  "text": "코스피 지수가 급등했다",
  "label": 0,
  "label_name": "경제"
}
```

### Data Fields

| Field | Type | Description |
|-------|------|-------------|
| `text` | string | 뉴스 스타일의 한국어 문장 |
| `label` | int | 카테고리 레이블 (0-3) |
| `label_name` | string | 카테고리 이름 |

### Label Mapping

| Label | Label Name | Description |
|-------|------------|-------------|
| 0 | 경제 | 주식, 금융, 부동산, 무역 등 경제 관련 |
| 1 | 사회 | 사건, 사고, 복지, 환경 등 사회 이슈 |
| 2 | 생활문화 | 연예, 스포츠, 여행, 음식 등 문화 콘텐츠 |
| 3 | IT과학 | 기술, 과학, 인공지능, 우주 등 |

### Data Splits

| Split | Examples | Description |
|-------|----------|-------------|
| train | 5,000 | 학습용 데이터 |
| validation | 500 | 검증용 데이터 |
| test | 500 | 테스트용 데이터 |

각 카테고리별로 균등하게 분포되어 있습니다 (25%씩).

## Dataset Creation

### Curation Rationale

이 데이터셋은 다음 목적으로 제작되었습니다:

1. **교육용**: 딥러닝/NLP 입문자를 위한 실습 데이터
2. **한국어 NLP**: 한국어 텍스트 분류 모델 학습 및 평가
3. **BERT Fine-tuning**: 사전학습 모델의 미세조정 실습

### Source Data

#### Initial Data Collection and Normalization

- **생성 방식**: 템플릿 기반 합성 (Template-based Synthetic Generation)
- **템플릿 수**: 카테고리당 약 20개
- **키워드 풀**: 카테고리당 수십~수백 개의 도메인 특화 키워드

#### Who are the source language producers?

합성 데이터로, 실제 뉴스 기사나 사용자 생성 콘텐츠가 아닙니다.

### Annotations

#### Annotation process

템플릿 기반 자동 생성으로, 문장 생성 시 레이블이 함께 결정됩니다.

#### Who are the annotators?

자동 생성된 레이블 (템플릿 카테고리에 따라 결정)

### Personal and Sensitive Information

이 데이터셋은 합성 데이터로, 개인정보나 민감 정보를 포함하지 않습니다.

## Considerations for Using the Data

### Social Impact of Dataset

교육 목적으로 제작된 데이터셋으로, 실제 뉴스 기사와 다를 수 있습니다.

### Discussion of Biases

- 템플릿 기반 생성으로 문장 패턴이 제한적일 수 있습니다
- 실제 뉴스 데이터의 복잡성과 다양성을 완전히 반영하지 못합니다
- 교육 및 실습 목적에 적합하며, 실제 서비스 적용에는 추가 검증이 필요합니다

### Other Known Limitations

1. **합성 데이터의 한계**: 실제 뉴스의 문체나 표현 다양성 부족
2. **도메인 특수성**: 특정 키워드에 의존적인 분류 패턴
3. **시의성**: 최신 트렌드나 이슈 반영 제한

## Additional Information

### Dataset Curators

정상근 (hugmanskj@gmail.com)

### Licensing Information

CC BY 4.0 (Creative Commons Attribution 4.0 International)

이 데이터셋은 교육 목적으로 자유롭게 사용할 수 있습니다.

### Citation Information

```bibtex
@dataset{korean_topic_classification_synthetic,
  author = {정상근},
  title = {Korean News Topic Classification Dataset (Synthetic)},
  year = {2024},
  publisher = {Hugging Face},
  note = {Educational dataset for deep learning textbook}
}
```

### Contributions
이 데이터셋은 교육용 목적을 위해 제작되었습니다.

## How to Use

### Loading the Dataset

```python
from datasets import load_dataset

# Hugging Face Hub에서 로드
dataset = load_dataset("YOUR_USERNAME/korean-news-topic-classification")

# 또는 로컬 파일에서 로드
dataset = load_dataset("json", data_files={
    "train": "train.json",
    "validation": "valid.json",
    "test": "test.json"
})
```

### Example Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# 모델 및 토크나이저 로드
model_name = "klue/bert-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=4)

# 데이터 전처리
def preprocess(examples):
    return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=128)

tokenized_dataset = dataset.map(preprocess, batched=True)

# 학습
from transformers import Trainer, TrainingArguments

training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    evaluation_strategy="epoch",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["validation"],
)

trainer.train()
```

## Sample Data

### 경제 (Economy)
- "코스피 지수가 상승했다"
- "한국은행이 기준금리 인상을 발표했다"
- "원달러 환율이 전월 대비 하락했다"

### 사회 (Society)
- "서울에서 교통사고가 발생했다"
- "정부가 재난 대응 매뉴얼을 시행한다"
- "저출산 문제가 심각해지고 있다"

### 생활문화 (Culture & Lifestyle)
- "BTS가 신곡을 발표했다"
- "새 드라마가 넷플릭스에서 1위를 기록했다"
- "힐링 여행이 MZ세대 사이에서 인기를 끌고 있다"

### IT과학 (Technology & Science)
- "인공지능이 의료에 적용되고 있다"
- "삼성전자가 새로운 스마트폰을 출시했다"
- "화성 탐사가 순조롭게 진행하고 있다"
