---
language:
- ko
license: cc-by-4.0
size_categories:
- 1K<n<10K
task_categories:
- token-classification
task_ids:
- named-entity-recognition
tags:
- korean
- ner
- synthetic
- bio-tagging
- education
pretty_name: Korean NER Dataset (Synthetic)
dataset_info:
  features:
  - name: id
    dtype: int64
  - name: tokens
    sequence: string
  - name: ner_tags
    sequence:
      class_label:
        names:
          '0': O
          '1': B-PER
          '2': I-PER
          '3': B-ORG
          '4': I-ORG
          '5': B-LOC
          '6': I-LOC
          '7': B-DAT
          '8': I-DAT
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1200000
    num_examples: 5000
  - name: validation
    num_bytes: 120000
    num_examples: 500
  - name: test
    num_bytes: 120000
    num_examples: 500
  download_size: 1440000
  dataset_size: 1440000
---

# Korean NER Dataset (Synthetic)

한국어 개체명 인식(NER)을 위한 합성 데이터셋입니다.

## Dataset Description

이 데이터셋은 자연어처리 실습을 위해 제작된 **교육용 합성 데이터셋**입니다.

### Dataset Summary

- **언어**: 한국어 (Korean)
- **도메인**: 뉴스 헤드라인 스타일
- **태스크**: Token Classification (Named Entity Recognition)
- **태깅 스킴**: BIO (Begin-Inside-Outside)
- **생성 방식**: 템플릿 기반 합성 데이터 (Synthetic)

### Supported Tasks

- **Token Classification**: 각 토큰에 대해 개체명 태그 예측
- **N-to-N Task**: 입력 토큰 시퀀스 -> 태그 시퀀스

### Languages

한국어 (Korean, ko)

## Dataset Structure

### Data Instances

```json
{
  "id": 0,
  "tokens": ["삼성전자", "가", "신제품을", "출시했다", "."],
  "ner_tags": ["B-ORG", "O", "O", "O", "O"],
  "text": "삼성전자가 신제품을 출시했다."
}
```

### Data Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | int | 샘플 고유 ID |
| `tokens` | List[str] | 토큰화된 단어 리스트 |
| `ner_tags` | List[str] | 각 토큰에 대한 BIO 태그 |
| `text` | str | 원본 문장 |

### Entity Types

| Entity Type | Description | Examples |
|-------------|-------------|----------|
| PER (인물) | 사람 이름, 연예인, 스포츠 선수 등 | 김철수, 손흥민, 아이유 |
| ORG (기관) | 회사, 정부 기관, 학교, 방송사 등 | 삼성전자, 서울대학교, KBS |
| LOC (장소) | 지역, 국가, 시설, 자연지물 등 | 서울, 한국, 강남, 한강 |
| DAT (날짜) | 날짜, 시간, 요일, 기간 표현 | 오늘, 2024년, 월요일 |

### BIO Tagging Scheme

| Tag | Description |
|-----|-------------|
| O | Outside (개체명이 아님) |
| B-PER | Begin-Person (인물 개체의 시작) |
| I-PER | Inside-Person (인물 개체의 내부) |
| B-ORG | Begin-Organization (기관 개체의 시작) |
| I-ORG | Inside-Organization (기관 개체의 내부) |
| B-LOC | Begin-Location (장소 개체의 시작) |
| I-LOC | Inside-Location (장소 개체의 내부) |
| B-DAT | Begin-Date (날짜 개체의 시작) |
| I-DAT | Inside-Date (날짜 개체의 내부) |

### Data Splits

| Split | Examples | Description |
|-------|----------|-------------|
| train | 5,000 | 학습용 데이터 |
| validation | 500 | 검증용 데이터 |
| test | 500 | 테스트용 데이터 |

## Dataset Creation

### Curation Rationale

이 데이터셋은 다음 목적으로 제작되었습니다:

1. **교육용**: 딥러닝/NLP 입문자를 위한 실습 데이터
2. **한국어 NLP**: 한국어 토큰 분류 모델 학습 및 평가
3. **BERT Fine-tuning**: 사전학습 모델의 토큰 분류 미세조정 실습
4. **BIO 태깅 학습**: 시퀀스 라벨링의 기본 개념 이해

### Source Data

#### Initial Data Collection and Normalization

- **생성 방식**: 템플릿 기반 합성 (Template-based Synthetic Generation)
- **템플릿 수**: 약 50개 이상의 다양한 문장 구조
- **개체명 풀**: 각 카테고리별 수십 개의 개체명

#### Who are the source language producers?

합성 데이터로, 실제 뉴스 기사나 사용자 생성 콘텐츠가 아닙니다.

### Annotations

#### Annotation process

템플릿 기반 자동 생성으로, 문장 생성 시 태그가 함께 결정됩니다.

#### Who are the annotators?

자동 생성된 레이블 (템플릿 슬롯에 따라 결정)

### Personal and Sensitive Information

이 데이터셋은 합성 데이터로, 개인정보나 민감 정보를 포함하지 않습니다.
인물명은 가상 또는 공인의 이름을 사용했습니다.

## Considerations for Using the Data

### Social Impact of Dataset

교육 목적으로 제작된 데이터셋으로, 실제 뉴스 기사와 다를 수 있습니다.

### Discussion of Biases

- 템플릿 기반 생성으로 문장 패턴이 제한적일 수 있습니다
- 실제 텍스트의 복잡성과 다양성을 완전히 반영하지 못합니다
- 교육 및 실습 목적에 적합하며, 실제 서비스 적용에는 추가 검증이 필요합니다

### Other Known Limitations

1. **합성 데이터의 한계**: 실제 텍스트의 문체나 표현 다양성 부족
2. **토큰화 방식**: 간단한 규칙 기반 토큰화 사용 (형태소 분석 미적용)
3. **개체 중첩**: 중첩 개체명(nested entities)은 지원하지 않음

## Additional Information

### Dataset Curators

정상근 (hugmanskj@gmail.com)

### Licensing Information

CC BY 4.0 (Creative Commons Attribution 4.0 International)

이 데이터셋은 교육 목적으로 자유롭게 사용할 수 있습니다.

### Citation Information

```bibtex
@dataset{korean_ner_synthetic,
  author = {정상근},
  title = {Korean NER Dataset (Synthetic)},
  year = {2024},
  publisher = {Hugging Face},
  note = {Educational dataset for deep learning textbook}
}
```

## How to Use

### Loading the Dataset

```python
from datasets import load_dataset

# Hugging Face Hub에서 로드
dataset = load_dataset("YOUR_USERNAME/korean-ner")

# 또는 로컬 파일에서 로드
dataset = load_dataset("json", data_files={
    "train": "train.json",
    "validation": "valid.json",
    "test": "test.json"
})
```

### Example Usage with BERT

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import DataCollatorForTokenClassification, Trainer, TrainingArguments

# 레이블 정의
label_list = ["O", "B-PER", "I-PER", "B-ORG", "I-ORG", "B-LOC", "I-LOC", "B-DAT", "I-DAT"]
label_to_id = {label: i for i, label in enumerate(label_list)}

# 모델 및 토크나이저 로드
model_name = "klue/bert-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name, num_labels=len(label_list))

# 토큰화 함수
def tokenize_and_align_labels(examples):
    tokenized_inputs = tokenizer(
        examples["tokens"],
        truncation=True,
        is_split_into_words=True,
        padding="max_length",
        max_length=128
    )

    labels = []
    for i, label in enumerate(examples["ner_tags"]):
        word_ids = tokenized_inputs.word_ids(batch_index=i)
        label_ids = []
        previous_word_idx = None
        for word_idx in word_ids:
            if word_idx is None:
                label_ids.append(-100)
            elif word_idx != previous_word_idx:
                label_ids.append(label_to_id[label[word_idx]])
            else:
                label_ids.append(-100)  # subword는 -100으로 마스킹
            previous_word_idx = word_idx
        labels.append(label_ids)

    tokenized_inputs["labels"] = labels
    return tokenized_inputs

# 데이터셋 전처리
tokenized_dataset = dataset.map(tokenize_and_align_labels, batched=True)

# 학습
data_collator = DataCollatorForTokenClassification(tokenizer)

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
    data_collator=data_collator,
)

trainer.train()
```

## Sample Data

### Example 1: Single Entity

```
Tokens: ["삼성전자", "가", "신제품을", "출시했다", "."]
Tags:   ["B-ORG",    "O",  "O",       "O",       "O"]
```

### Example 2: Multiple Entities

```
Tokens: ["오늘", "손흥민", "이", "런던", "에서", "경기를", "했다", "."]
Tags:   ["B-DAT", "B-PER", "O", "B-LOC", "O",   "O",     "O",    "O"]
```

### Example 3: Complex Sentence

```
Tokens: ["삼성전자", "가", "내일", "서울", "에서", "컨퍼런스를", "개최한다", "."]
Tags:   ["B-ORG",    "O",  "B-DAT", "B-LOC", "O",  "O",        "O",       "O"]
```
