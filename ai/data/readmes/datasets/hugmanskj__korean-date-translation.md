---
language:
- ko
license: cc-by-4.0
size_categories:
- 1K<n<10K
task_categories:
- translation
tags:
- korean
- date-parsing
- seq2seq
- synthetic
- education
- text2text-generation
pretty_name: Korean Date Translation Dataset
dataset_info:
  features:
  - name: id
    dtype: int64
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 400000
    num_examples: 5000
  - name: validation
    num_bytes: 40000
    num_examples: 500
  - name: test
    num_bytes: 40000
    num_examples: 500
  download_size: 480000
  dataset_size: 480000
---

# Korean Date Translation Dataset

한국어 날짜 표현을 ISO 8601 형식(YYYY-MM-DD)으로 변환하는 데이터셋입니다.

## Dataset Description

이 데이터셋은 자연어처리 실습을 위해 제작된 **교육용 합성 데이터셋**입니다.
다양한 한국어 날짜 표현을 표준화된 형식으로 변환하는 **Sequence-to-Sequence (N-to-M)** 과제용입니다.

### Dataset Summary

- **언어**: 한국어 (Korean)
- **도메인**: 날짜 표현 정규화
- **태스크**: Text-to-Text Generation (Date Parsing / Translation)
- **생성 방식**: 템플릿 기반 합성 데이터 (Synthetic)

### Supported Tasks

- **Text-to-Text Generation**: 입력 날짜 표현 -> ISO 8601 형식 변환
- **N-to-M Task**: 가변 길이 입력 -> 고정 형식 출력 (YYYY-MM-DD)

### Languages

한국어 (Korean, ko)

## Dataset Structure

### Data Instances

```json
{
  "id": 0,
  "input": "2025년 12월 3일",
  "output": "2025-12-03"
}
```

### Data Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | int | 샘플 고유 ID |
| `input` | str | 한국어 날짜 표현 (다양한 형식) |
| `output` | str | ISO 8601 형식의 날짜 (YYYY-MM-DD) |

### Input Variations

이 데이터셋은 다양한 한국어 날짜 표현을 포함합니다:

| 카테고리 | 예시 |
|---------|------|
| 기본 한글 | "2025년 12월 3일", "2025년 12월 03일" |
| 2자리 연도 | "25년 12월 3일" |
| 슬래시 구분 | "2025/12/3", "2025/12/03" |
| 점 구분 | "2025.12.3", "2025.12.03" |
| 하이픈 구분 | "2025-12-3" |
| 순서 변형 | "12월 3일 2025년", "12월 3일, 2025년" |
| 한글 숫자 | "2025년 십이월 삼일" |
| 완전 한글 | "이천이십오년 십이월 삼일" |
| 공백 변형 | "2025 년 12 월 3 일" |
| 접미사 변형 | "2025년도 12월 3일" |
| 축약형 | "2025. 12. 3." |
| 괄호 사용 | "(2025년 12월 3일)", "[2025.12.03]" |
| 한자 | "2025年12月3日" |
| 접두어 | "날짜: 2025년 12월 3일" |
| 영문 혼합 | "2025년 Dec 3일" |

### Data Splits

| Split | Examples | Description |
|-------|----------|-------------|
| train | 5,000 | 학습용 데이터 |
| validation | 500 | 검증용 데이터 |
| test | 500 | 테스트용 데이터 |

### Date Range

- 연도: 2020년 ~ 2030년
- 월: 1월 ~ 12월
- 일: 1일 ~ 31일 (월별 유효 범위 내)

## Dataset Creation

### Curation Rationale

이 데이터셋은 다음 목적으로 제작되었습니다:

1. **교육용**: 딥러닝/NLP 입문자를 위한 Seq2Seq 실습 데이터
2. **N-to-M 과제 학습**: 가변 길이 입력 -> 고정 형식 출력 변환
3. **T5/GPT Fine-tuning**: Encoder-Decoder 또는 Decoder-only 모델 실습
4. **Date Parsing**: 자연어 날짜 표현의 정규화 학습

### Source Data

#### Initial Data Collection and Normalization

- **생성 방식**: 템플릿 기반 합성 (Template-based Synthetic Generation)
- **날짜 범위**: 2020-2030년
- **변형 유형**: 15개 이상의 다양한 날짜 표현 패턴

#### Who are the source language producers?

합성 데이터로, 실제 문서나 사용자 생성 콘텐츠가 아닙니다.

### Annotations

#### Annotation process

템플릿 기반 자동 생성으로, 입력 생성 시 정답(ISO 형식)이 함께 결정됩니다.

#### Who are the annotators?

자동 생성된 레이블 (생성 규칙에 따라 결정)

### Personal and Sensitive Information

이 데이터셋은 합성 데이터로, 개인정보나 민감 정보를 포함하지 않습니다.

## Considerations for Using the Data

### Social Impact of Dataset

교육 목적으로 제작된 데이터셋으로, 실제 문서의 날짜 표현과 다를 수 있습니다.

### Discussion of Biases

- 템플릿 기반 생성으로 표현 패턴이 제한적일 수 있습니다
- 실제 텍스트에서 발생하는 오타나 비표준 표현은 포함되지 않습니다
- 교육 및 실습 목적에 적합하며, 실제 서비스 적용에는 추가 검증이 필요합니다

### Other Known Limitations

1. **합성 데이터의 한계**: 실제 텍스트의 다양성 부족
2. **문맥 없음**: 단독 날짜 표현만 포함 (문장 내 날짜 추출 미지원)
3. **시간 미포함**: 시간 정보(시:분:초) 없음
4. **기원전/기원후**: 음력, 기원전 연도 등 미지원

## Additional Information

### Dataset Curators

정상근 (hugmanskj@gmail.com)

### Licensing Information

CC BY 4.0 (Creative Commons Attribution 4.0 International)

이 데이터셋은 교육 목적으로 자유롭게 사용할 수 있습니다.

### Citation Information

```bibtex
@dataset{korean_date_translation,
  author = {정상근},
  title = {Korean Date Translation Dataset},
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
dataset = load_dataset("YOUR_USERNAME/korean-date-translation")

# 또는 로컬 파일에서 로드
dataset = load_dataset("json", data_files={
    "train": "train.json",
    "validation": "valid.json",
    "test": "test.json"
})
```

### Example Usage with T5

```python
from transformers import T5Tokenizer, T5ForConditionalGeneration
from transformers import Seq2SeqTrainer, Seq2SeqTrainingArguments

# 모델 및 토크나이저 로드
model_name = "google/mt5-small"  # 또는 한국어 T5 모델
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# 데이터 전처리
def preprocess_function(examples):
    # 입력에 task prefix 추가
    inputs = ["날짜 변환: " + inp for inp in examples["input"]]
    targets = examples["output"]

    model_inputs = tokenizer(
        inputs,
        max_length=64,
        truncation=True,
        padding="max_length"
    )

    labels = tokenizer(
        targets,
        max_length=16,
        truncation=True,
        padding="max_length"
    )

    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

# 데이터셋 전처리
tokenized_dataset = dataset.map(preprocess_function, batched=True)

# 학습
training_args = Seq2SeqTrainingArguments(
    output_dir="./results",
    num_train_epochs=5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    evaluation_strategy="epoch",
    predict_with_generate=True,
)

trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["validation"],
    tokenizer=tokenizer,
)

trainer.train()
```

### Example Usage with GPT-style Model

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

# 모델 로드
model_name = "skt/kogpt2-base-v2"  # 한국어 GPT
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# 프롬프트 형식
def format_prompt(input_date):
    return f"날짜 변환\n입력: {input_date}\n출력:"

# 추론
input_text = "2025년 12월 3일"
prompt = format_prompt(input_text)
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=12)
result = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(result)  # 날짜 변환\n입력: 2025년 12월 3일\n출력: 2025-12-03
```

## Sample Data

### Example 1: Basic Korean Format

```
Input:  "2025년 12월 3일"
Output: "2025-12-03"
```

### Example 2: Slash Separated

```
Input:  "2025/12/03"
Output: "2025-12-03"
```

### Example 3: Full Korean Numerals

```
Input:  "이천이십오년 십이월 삼일"
Output: "2025-12-03"
```

### Example 4: Order Variation

```
Input:  "12월 3일, 2025년"
Output: "2025-12-03"
```

### Example 5: With Prefix

```
Input:  "날짜: 2025년 12월 3일"
Output: "2025-12-03"
```

## Evaluation Metrics

이 데이터셋에서 사용할 수 있는 평가 지표:

- **Exact Match (EM)**: 정확히 일치하는 비율
- **Character Error Rate (CER)**: 문자 수준 오류율
- **Token Accuracy**: 토큰별 정확도

권장 평가 방식: **Exact Match**가 가장 적합합니다. 날짜 형식이 정확해야 의미가 있기 때문입니다.
