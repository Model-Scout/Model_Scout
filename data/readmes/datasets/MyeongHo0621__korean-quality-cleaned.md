---
language:
- ko
license: cc-by-nc-sa-4.0
size_categories:
- 50K<n<100K
task_categories:
- text-generation
- question-answering
- conversational
pretty_name: Korean Quality Dataset (Cleaned)
tags:
- korean
- instruction
- cleaned
- chat
---

# Korean Quality Dataset (Cleaned)

> **고품질 한국어 Instruction 데이터셋 (정제 버전)**

## English

### Dataset Description

This is a **cleaned and standardized** Korean instruction dataset, combining multiple high-quality open-source Korean datasets with unified formatting and quality filtering.

#### Key Features

- ✅ **Unified Format**: Standardized `messages` format (OpenAI-compatible)
- ✅ **Quality Filtering**: Length, special characters, repetition filtering
- ✅ **Clean Structure**: Removed redundant fields, keeping only essential data
- ✅ **Ready-to-Use**: No additional preprocessing needed

### Dataset Statistics

| Metric | Value |
|--------|-------|
| **Total Samples** | 54,190 |
| **File Size** | 116.3 MB |
| **Format** | JSON (messages array) |
| **Languages** | Korean (primary), English (minimal) |

### Source Distribution

| Source | Samples | Percentage |
|--------|---------|------------|
| **KULLM-v2** | 33,422 | 61.7% |
| **KoAlpaca** | 20,768 | 38.3% |

### Data Format

```json
[
  {
    "messages": [
      {
        "content": "사용자 질문",
        "role": "user"
      },
      {
        "content": "AI 응답",
        "role": "assistant"
      }
    ],
    "source": "kullm_v2"
  }
]
```

### Usage

#### Load with Datasets Library

```python
from datasets import load_dataset

# Load dataset
dataset = load_dataset("MyeongHo0621/korean-quality-cleaned")

# Access data
print(dataset['train'][0])
```

#### Direct JSON Load

```python
import json

with open('korean_quality_dataset_clean.json', 'r') as f:
    data = json.load(f)

for item in data:
    messages = item['messages']
    user_msg = messages[0]['content']
    assistant_msg = messages[1]['content']
    print(f"Q: {user_msg}\nA: {assistant_msg}\n")
```

#### Fine-tuning Example (Transformers)

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer
from datasets import load_dataset

# Load dataset
dataset = load_dataset("MyeongHo0621/korean-quality-cleaned")

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("your-model")

# Format function
def format_instruction(sample):
    messages = sample['messages']
    prompt = f"### User:\n{messages[0]['content']}\n\n### Assistant:\n{messages[1]['content']}"
    return {"text": prompt}

# Apply formatting
dataset = dataset.map(format_instruction)

# Tokenize
def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True, max_length=2048)

tokenized_dataset = dataset.map(tokenize_function, batched=True)

# Train...
```

### Quality Filtering Applied

1. **Length Filtering**
   - User message: 5-2000 characters
   - Assistant message: 10-4000 characters

2. **Special Characters**
   - Removed excessive special symbols
   - Cleaned control characters

3. **Repetition Detection**
   - Removed highly repetitive content
   - Filtered low-quality responses

4. **Format Standardization**
   - Unified to `messages` format
   - Removed unnecessary fields (`instruction`, `input`, `output`, `id`, `url`)

### Original Sources & Credits

This dataset is derived from and cleaned version of:

- **KULLM-v2** (61.7%)
  - Source: [nlpai-lab/kullm-v2](https://huggingface.co/datasets/nlpai-lab/kullm-v2)
  - License: CC-BY-NC-SA-4.0
  - Description: High-quality Korean instruction dataset

- **KoAlpaca** (38.3%)
  - Source: [beomi/KoAlpaca-v1.1a](https://huggingface.co/datasets/beomi/KoAlpaca-v1.1a)
  - License: CC-BY-NC-SA-4.0
  - Description: Korean Alpaca instruction dataset

**All credit goes to the original dataset authors!**

### Use Cases

#### ✅ Recommended For

- Korean language model fine-tuning
- Instruction tuning
- Conversational AI training
- Question-answering systems
- General-purpose Korean LLM training

#### ⚠️ Limitations

- Primarily Korean language (some English mixed)
- Inherits biases from original datasets
- Not suitable for domain-specific tasks without additional data
- Quality varies by source

### License

- **Dataset License**: CC-BY-NC-SA-4.0
- **Inherited From**: Original source datasets
- **Commercial Use**: Limited (see license)

### Citation

If you use this dataset, please cite both this cleaned version and the original sources:

```bibtex
@misc{korean-quality-cleaned-2025,
  author = {MyeongHo0621},
  title = {Korean Quality Dataset (Cleaned): Standardized Korean Instruction Data},
  year = {2025},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/MyeongHo0621/korean-quality-cleaned}},
  note = {Cleaned and standardized version of KULLM-v2 and KoAlpaca}
}

@misc{kullm-v2,
  author = {NLP & AI Lab, Korea University},
  title = {KULLM-v2: Korean Instruction Dataset},
  year = {2023},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/nlpai-lab/kullm-v2}}
}

@misc{koalpaca,
  author = {Junbum Lee (beomi)},
  title = {KoAlpaca: Korean Alpaca Dataset},
  year = {2023},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/beomi/KoAlpaca-v1.1a}}
}
```

### Acknowledgments

- **Original Authors**: NLP & AI Lab (Korea University), Junbum Lee (beomi)
- **Cleaning & Formatting**: MyeongHo0621
- **Inspiration**: Stanford Alpaca, Vicuna

### Related Resources

| Resource | Description |
|----------|-------------|
| [eeve-vss-smh](https://huggingface.co/MyeongHo0621/eeve-vss-smh) | Model trained on this dataset |
| [KULLM-v2](https://huggingface.co/datasets/nlpai-lab/kullm-v2) | Original KULLM dataset |
| [KoAlpaca](https://huggingface.co/datasets/beomi/KoAlpaca-v1.1a) | Original KoAlpaca dataset |

### Contact

- **Dataset Issues**: Open an issue on the Hugging Face dataset page
- **Model**: [MyeongHo0621/eeve-vss-smh](https://huggingface.co/MyeongHo0621/eeve-vss-smh)

---

**Created**: 2025-10-11  
**Version**: 1.0  
**Status**: Production-Ready ✅

---

## 한국어

### 데이터셋 설명

여러 고품질 오픈소스 한국어 데이터셋을 **정제하고 표준화**한 한국어 instruction 데이터셋입니다.

#### 주요 특징

- ✅ **통일된 포맷**: `messages` 형식으로 표준화 (OpenAI 호환)
- ✅ **품질 필터링**: 길이, 특수문자, 반복 필터링
- ✅ **깔끔한 구조**: 불필요한 필드 제거, 필수 데이터만 유지
- ✅ **바로 사용 가능**: 추가 전처리 불필요

### 데이터셋 통계

| 항목 | 값 |
|------|-----|
| **총 샘플 수** | 54,190 |
| **파일 크기** | 116.3 MB |
| **포맷** | JSON (messages 배열) |
| **언어** | 한국어 (주), 영어 (일부) |

### 출처별 분포

| 출처 | 샘플 수 | 비율 |
|------|---------|------|
| **KULLM-v2** | 33,422 | 61.7% |
| **KoAlpaca** | 20,768 | 38.3% |

### 데이터 형식

```json
[
  {
    "messages": [
      {
        "content": "사용자 질문",
        "role": "user"
      },
      {
        "content": "AI 응답",
        "role": "assistant"
      }
    ],
    "source": "kullm_v2"
  }
]
```

### 사용 방법

#### Datasets 라이브러리로 로드

```python
from datasets import load_dataset

# 데이터셋 로드
dataset = load_dataset("MyeongHo0621/korean-quality-cleaned")

# 데이터 확인
print(dataset['train'][0])
```

#### 직접 JSON 로드

```python
import json

with open('korean_quality_dataset_clean.json', 'r') as f:
    data = json.load(f)

for item in data:
    messages = item['messages']
    user_msg = messages[0]['content']
    assistant_msg = messages[1]['content']
    print(f"질문: {user_msg}\n답변: {assistant_msg}\n")
```

#### 파인튜닝 예시

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
from datasets import load_dataset

# 데이터셋 로드
dataset = load_dataset("MyeongHo0621/korean-quality-cleaned")

# 토크나이저 로드
tokenizer = AutoTokenizer.from_pretrained("your-model")

# 포맷팅 함수
def format_instruction(sample):
    messages = sample['messages']
    prompt = f"### User:\n{messages[0]['content']}\n\n### Assistant:\n{messages[1]['content']}"
    return {"text": prompt}

# 포맷 적용
dataset = dataset.map(format_instruction)

# 토크나이징
def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True, max_length=2048)

tokenized_dataset = dataset.map(tokenize_function, batched=True)

# 훈련...
```

### 적용된 품질 필터링

1. **길이 필터링**
   - 사용자 메시지: 5-2000자
   - 어시스턴트 메시지: 10-4000자

2. **특수문자 제거**
   - 과도한 특수기호 제거
   - 제어 문자 정리

3. **반복 탐지**
   - 반복적인 콘텐츠 제거
   - 저품질 응답 필터링

4. **포맷 표준화**
   - `messages` 형식으로 통일
   - 불필요한 필드 제거 (`instruction`, `input`, `output`, `id`, `url`)

### 원본 출처 및 크레딧

이 데이터셋은 다음 데이터셋들을 정제한 버전입니다:

- **KULLM-v2** (61.7%)
  - 출처: [nlpai-lab/kullm-v2](https://huggingface.co/datasets/nlpai-lab/kullm-v2)
  - 라이선스: CC-BY-NC-SA-4.0
  - 설명: 고품질 한국어 instruction 데이터셋

- **KoAlpaca** (38.3%)
  - 출처: [beomi/KoAlpaca-v1.1a](https://huggingface.co/datasets/beomi/KoAlpaca-v1.1a)
  - 라이선스: CC-BY-NC-SA-4.0
  - 설명: 한국어 Alpaca instruction 데이터셋

**모든 크레딧은 원본 데이터셋 제작자에게 있습니다!**

### 사용 사례

#### ✅ 추천 용도

- 한국어 언어 모델 파인튜닝
- Instruction 튜닝
- 대화형 AI 훈련
- 질의응답 시스템
- 범용 한국어 LLM 훈련

#### ⚠️ 제한사항

- 주로 한국어 (일부 영어 혼재)
- 원본 데이터셋의 편향 상속
- 추가 데이터 없이는 도메인 특화 작업에 부적합
- 출처별로 품질 차이 존재

### 라이선스

- **데이터셋 라이선스**: CC-BY-NC-SA-4.0
- **상속**: 원본 데이터셋 라이선스
- **상업적 사용**: 제한적 (라이선스 참조)

### Citation

이 데이터셋을 사용하시면, 정제 버전과 원본 출처를 모두 인용해주세요:

```bibtex
@misc{korean-quality-cleaned-2025,
  author = {MyeongHo0621},
  title = {Korean Quality Dataset (Cleaned): Standardized Korean Instruction Data},
  year = {2025},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/MyeongHo0621/korean-quality-cleaned}},
  note = {Cleaned and standardized version of KULLM-v2 and KoAlpaca}
}
```

### Acknowledgments

- **원본 제작자**: NLP & AI Lab (고려대학교), 이준범 (beomi)
- **정제 및 포맷팅**: MyeongHo0621
- **영감**: Stanford Alpaca, Vicuna

### 관련 리소스

| 리소스 | 설명 |
|--------|------|
| [eeve-vss-smh](https://huggingface.co/MyeongHo0621/eeve-vss-smh) | 이 데이터셋으로 훈련한 모델 |
| [KULLM-v2](https://huggingface.co/datasets/nlpai-lab/kullm-v2) | 원본 KULLM 데이터셋 |
| [KoAlpaca](https://huggingface.co/datasets/beomi/KoAlpaca-v1.1a) | 원본 KoAlpaca 데이터셋 |

### Contact

- **데이터셋 이슈**: Hugging Face 데이터셋 페이지에서 이슈 오픈
- **모델**: [MyeongHo0621/eeve-vss-smh](https://huggingface.co/MyeongHo0621/eeve-vss-smh)

---

**생성일**: 2025-10-11  
**버전**: 1.0  
**상태**: 프로덕션 준비 완료 ✅

