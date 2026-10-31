---
language:
- ko
- en
- zh
- ja
- id
- vi
- tl
license: cc-by-nc-sa-4.0
task_categories:
- translation
tags:
- translation
- multilingual
- korean
- instruction-tuning
- balanced-dataset
size_categories:
- 1M<n<10M
pretty_name: "다국어 번역 데이터셋 (Balanced Fast)"
---

<!-- aegis-dataset-card -->

# multilingual-translation-fast

> **용도 기록 없음** · 다국어 번역 데이터셋 (Balanced Fast)  
> 파일 17개 · 6.4 GB · 행 10,606,456 · revision `d6d517783d` · 카드 갱신 2026-10-20  
> 전체 모델 ↔ 데이터 매핑 · 서버 복원 방법: [`neuralfoundry-coder/workspace-data-catalog_261020`](https://huggingface.co/datasets/neuralfoundry-coder/workspace-data-catalog_261020)

## 개요
다국어 번역 모델의 **빠른 학습 및 평가**를 위한 균형 잡힌 데이터셋입니다.
7개 언어쌍에서 각각 **동일한 수량**을 랜덤 추출하여 구성했습니다.

## 이 데이터로 학습한 모델
이 데이터로 학습했다는 기록(학습 설정 · 모델 카드)을 찾지 못했다. 카탈로그의 '확인 필요' 목록에 있다.

## 파일 구성
| 파일 | 크기 | 행 | 내용 |
|---|---|---|---|
| `README.md` | 7.6 KB | - |  |
| `test/all_test_fast.jsonl` | 636.0 MB | 1,060,647 |  |
| `test/en-ko_test_fast.jsonl` | 103.0 MB | 151,521 |  |
| `test/ko-en_test_fast.jsonl` | 104.6 MB | 151,521 |  |
| `test/ko-id_test_fast.jsonl` | 69.9 MB | 151,521 |  |
| `test/ko-ja_test_fast.jsonl` | 112.2 MB | 151,521 |  |
| `test/ko-tl_test_fast.jsonl` | 70.3 MB | 151,521 |  |
| `test/ko-vi_test_fast.jsonl` | 71.4 MB | 151,521 |  |
| `test/ko-zh_test_fast.jsonl` | 104.7 MB | 151,521 |  |
| `train/all_train_fast.jsonl` | 2.5 GB | 4,242,581+ |  |
| `train/en-ko_train_fast.jsonl` | 411.9 MB | 606,083 |  |
| `train/ko-en_train_fast.jsonl` | 418.1 MB | 606,083 |  |
| `train/ko-id_train_fast.jsonl` | 279.7 MB | 606,083 |  |
| `train/ko-ja_train_fast.jsonl` | 448.5 MB | 606,083 |  |
| `train/ko-tl_train_fast.jsonl` | 281.3 MB | 606,083 |  |
| `train/ko-vi_train_fast.jsonl` | 285.6 MB | 606,083 |  |
| `train/ko-zh_train_fast.jsonl` | 418.8 MB | 606,083 |  |

## 필드 · 범주 분포
**`test/all_test_fast.jsonl`, `test/en-ko_test_fast.jsonl`, `test/ko-en_test_fast.jsonl`, `test/ko-id_test_fast.jsonl`, `test/ko-ja_test_fast.jsonl`, `test/ko-tl_test_fast.jsonl` 외 10개** (기준 `train/all_train_fast.jsonl`)

| 필드 | 타입 | 채움 |
|---|---|---|
| `messages` | list | 100% |
| `metadata` | dict | 100% |

필드는 행 최상위 키, 채움은 그 키가 있는 행 비율이다. 범주 분포는 글 필드가 아니고 값이 짧고(≤48자) 종류가 적은(≤40) 필드만 셌다.

## 내려받기 · 복원
```bash
hf download neuralfoundry-coder/multilingual-translation-fast --repo-type dataset --local-dir <폴더>
```
- 서버 파일 전체의 위치 · 재생성 방법: [`neuralfoundry-coder/workspace-data-catalog_261020`](https://huggingface.co/datasets/neuralfoundry-coder/workspace-data-catalog_261020) 의 `restore_map.json`

## 기존 설명 (2026-10-20 이전 카드)

### 다국어 번역 데이터셋 (Balanced Fast)

#### 📋 Dataset Description

다국어 번역 모델의 **빠른 학습 및 평가**를 위한 균형 잡힌 데이터셋입니다.
7개 언어쌍에서 각각 **동일한 수량**을 랜덤 추출하여 구성했습니다.

##### Supported Languages

| 언어쌍 | 방향 | Language Pair |
|--------|------|---------------|
| ko-en | 한국어 → 영어 | Korean → English |
| en-ko | 영어 → 한국어 | English → Korean |
| ko-zh | 한국어 → 중국어 | Korean → Chinese |
| ko-ja | 한국어 → 일본어 | Korean → Japanese |
| ko-id | 한국어 → 인도네시아어 | Korean → Indonesian |
| ko-vi | 한국어 → 베트남어 | Korean → Vietnamese |
| ko-tl | 한국어 → 타갈로그어 | Korean → Tagalog |

#### ✨ Key Features

- 🎯 **Balanced Data**: 모든 언어쌍이 동일한 수량 (언어 편향 방지)
- ⚡ **Fast Experimentation**: 전체 데이터셋 대비 약 1/10 크기
- 🔄 **Reproducible**: 랜덤 시드 42로 고정
- 📝 **Instruction Format**: 지시 학습(Instruction Fine-tuning)에 최적화

#### 📊 Dataset Statistics

##### Train Split

| Language Pair | Records | File Size |
|---------------|---------|-----------|
| ko-en | 606,083 | 399MB |
| en-ko | 606,083 | 393MB |
| ko-zh | 606,083 | 399MB |
| ko-ja | 606,083 | 428MB |
| ko-id | 606,083 | 267MB |
| ko-vi | 606,083 | 272MB |
| ko-tl | 606,083 | 268MB |
| **Total** | **4,242,581** | **2.4GB** |

##### Test Split

| Language Pair | Records | File Size |
|---------------|---------|-----------|
| ko-en | 151,521 | 100MB |
| en-ko | 151,521 | 98MB |
| ko-zh | 151,521 | 100MB |
| ko-ja | 151,521 | 107MB |
| ko-id | 151,521 | 67MB |
| ko-vi | 151,521 | 68MB |
| ko-tl | 151,521 | 67MB |
| **Total** | **1,060,647** | **607MB** |

#### 📁 Dataset Structure

```
├── train/
│   ├── all_train_fast.jsonl        # 전체 통합
│   ├── ko-en_train_fast.jsonl
│   ├── en-ko_train_fast.jsonl
│   ├── ko-zh_train_fast.jsonl
│   ├── ko-ja_train_fast.jsonl
│   ├── ko-id_train_fast.jsonl
│   ├── ko-vi_train_fast.jsonl
│   └── ko-tl_train_fast.jsonl
└── test/
    ├── all_test_fast.jsonl         # 전체 통합
    ├── ko-en_test_fast.jsonl
    ├── en-ko_test_fast.jsonl
    ├── ko-zh_test_fast.jsonl
    ├── ko-ja_test_fast.jsonl
    ├── ko-id_test_fast.jsonl
    ├── ko-vi_test_fast.jsonl
    └── ko-tl_test_fast.jsonl
```

#### 📝 Data Format

각 레코드는 JSONL 형식으로, **Instruction Fine-tuning**에 적합한 messages 구조를 따릅니다:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Translate the given sentence or word from the source language into the target language.\n\nsource language: Korean (ko)\ntarget language: English (en)\n\nGiven sentence: 안녕하세요.\nTarget sentence:"
    },
    {
      "role": "assistant",
      "content": "Hello."
    }
  ],
  "metadata": {
    "source_language": "ko",
    "target_language": "en",
    "domain": "일상",
    "is_mt": false
  }
}
```

##### Field Description

| Field | Description |
|-------|-------------|
| `messages` | Array of conversation messages |
| `messages[].role` | Role: "user" or "assistant" |
| `messages[].content` | Message content |
| `metadata.source_language` | Source language code |
| `metadata.target_language` | Target language code |
| `metadata.domain` | Data domain (optional) |
| `metadata.is_mt` | Machine translation flag (true/false) |

#### 🔧 Usage

##### Load with Datasets Library

```python
from datasets import load_dataset

### 전체 데이터 로드
dataset = load_dataset("iscreammedia/multilingual-translation-fast")

### Train/Test 분리
train_data = dataset['train']
test_data = dataset['test']

print(f"Train: {len(train_data):,} records")
print(f"Test: {len(test_data):,} records")
```

##### Load Specific Language Pair

```python
from datasets import load_dataset

### 특정 언어쌍만 로드
dataset = load_dataset(
    "iscreammedia/multilingual-translation-fast",
    data_files={
        "train": "train/ko-en_train_fast.jsonl",
        "test": "test/ko-en_test_fast.jsonl"
    }
)
```

##### Training Example

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer

model = AutoModelForCausalLM.from_pretrained("your-base-model")
tokenizer = AutoTokenizer.from_pretrained("your-base-model")

def preprocess(example):
    messages = example['messages']
    prompt = messages[0]['content']
    response = messages[1]['content']
    return tokenizer(prompt + response, truncation=True, max_length=512)

train_dataset = dataset['train'].map(preprocess)
### ... training code
```

##### Evaluation Example

```python
from sacrebleu import corpus_bleu

predictions = []
references = []

for example in dataset['test']:
    prompt = example['messages'][0]['content']
    reference = example['messages'][1]['content']
    
    # Generate prediction
    prediction = model.generate(prompt)
    
    predictions.append(prediction)
    references.append(reference)

bleu = corpus_bleu(predictions, [references])
print(f"BLEU: {bleu.score:.2f}")
```

#### 📚 Data Sources

| Source | Language Pairs | Description |
|--------|----------------|-------------|
| AI Hub | ko-en, en-ko, ko-zh, ko-ja | Korean government open data |
| OPUS OpenSubtitles | ko-id, ko-vi, ko-tl | Movie/Drama subtitles |
| OPUS WikiMatrix | ko-id, ko-vi | Wikipedia parallel corpus |

#### 🎯 Recommended Use Cases

1. **Hyperparameter Tuning**: 빠른 실험으로 최적 설정 탐색
2. **Model Comparison**: 여러 모델 빠르게 벤치마킹
3. **Balanced Training**: 저자원 언어 성능 향상
4. **Prototyping**: 새로운 기법 빠르게 테스트
5. **CI/CD Pipeline**: 자동화된 모델 테스트

#### ⚠️ Limitations

- 전체 데이터셋의 약 10% 샘플
- 최종 배포 모델 학습 시에는 전체 데이터셋 사용 권장
- 랜덤 샘플링으로 도메인 분포가 원본과 다를 수 있음

#### 📈 Related Datasets

| Dataset | Records | Size | Use Case |
|---------|---------|------|----------|
| **This (Fast)** | 5.3M | 3GB | 빠른 실험 |
| Full Dataset | 52.7M | 26GB | 최종 학습 |

#### License

This dataset is released under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)** license.

Under this license, you are free to:
- Share (copy and redistribute) the dataset;
- Adapt (remix, transform, build upon) the dataset.

**Conditions:**
- **Attribution:** You must give appropriate credit, provide a link to the license, and indicate if changes were made.
- **NonCommercial:** You may not use the dataset for commercial purposes.
- **ShareAlike:** If you remix or build upon the dataset, you must distribute your contributions under the same license as the original.

**Disclaimer:** The dataset is provided *as-is* without any warranties. The authors and contributors are **not liable** for any direct or indirect damages arising from the use of this dataset. Use at your own risk.

#### Citation

```bibtex
@dataset{multilingual_translation_fast,
  title={Multilingual Translation Dataset (Balanced Fast)},
  author={iscreammedia},
  year={2024},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/brildev8/multilingual-translation-fast}
}
```
