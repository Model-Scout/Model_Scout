---
language:
- ko
task_categories:
- text-classification
- sentiment-analysis
tags:
- sentiment-analysis
- korean
- finance
- news
pretty_name: Korean News Sentiment Analysis Dataset
size_categories:
- 10K<n<100K
---

# Korean News Sentiment Analysis Dataset

## 데이터셋 설명

한국어 뉴스 기사에서 추출한 기업 관련 문장의 감성 분석 데이터셋입니다.

### 데이터 통계

- **총 샘플 수**: 45,544개
- **Train**: 36,435개 (80%)
- **Test**: 9,109개 (20%)

### 레이블 분포

| Label | Count | Percentage |
|-------|-------|------------|
| negative | 4,161 | 9.1% |
| neutral | 23,403 | 51.4% |
| positive | 17,980 | 39.5% |

## 데이터 구조

```python
{
  'sentence': str,  # 뉴스 기사 문장
  'label': str      # 감성 레이블 (negative, neutral, positive)
}
```

## 사용 예시

### 데이터셋 로드

```python
from datasets import load_dataset

# 데이터셋 로드
dataset = load_dataset("FISA-conclave/news-sentiment-dataset")

# Train 데이터 확인
print(dataset['train'][0])
# {'sentence': '...', 'label': 'positive'}

# Test 데이터 확인
print(dataset['test'][0])
```

### 학습에 사용

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments

# 모델 및 토크나이저 로드
model_name = "klue/roberta-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=3)

# 데이터셋 토크나이징
def tokenize_function(examples):
    return tokenizer(examples['sentence'], truncation=True, padding='max_length', max_length=128)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# 학습
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=64,
    evaluation_strategy="epoch",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets['train'],
    eval_dataset=tokenized_datasets['test'],
)

trainer.train()
```

## 데이터 출처

- 한국어 뉴스 기사에서 추출
- KLUE-RoBERTa 모델로 감성 분석 수행
- asset_type='ST' (주식) 기업만 포함

## 라이센스

이 데이터셋은 연구 및 교육 목적으로 사용할 수 있습니다.

## 인용

```bibtex
@misc{korean-news-sentiment,
  title={Korean News Sentiment Analysis Dataset},
  author={FISA-conclave},
  year={2025},
  publisher={Hugging Face},
  howpublished={\url{https://huggingface.co/datasets/FISA-conclave/news-sentiment-dataset}}
}
```

## 제작

- Organization: FISA-conclave
- Model: FISA-conclave/klue-roberta-news-sentiment
- Year: 2025
