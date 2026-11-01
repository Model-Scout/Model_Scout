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
- thinking
- chain-of-thought
- balanced-dataset
size_categories:
- 1M<n<10M
pretty_name: "다국어 번역 데이터셋 - Thinking Mode (Balanced Fast)"
---

<!-- aegis-dataset-card -->

# multilingual-translation-thinking-fast

> **용도 기록 없음** · 다국어 번역 데이터셋 - Thinking Mode (Balanced Fast)  
> 파일 17개 · 11.0 GB · 행 10,606,456 · revision `0de3d8943a` · 카드 갱신 2026-10-20  
> 전체 모델 ↔ 데이터 매핑 · 서버 복원 방법: [`neuralfoundry-coder/workspace-data-catalog_261020`](https://huggingface.co/datasets/neuralfoundry-coder/workspace-data-catalog_261020)

## 개요
다국어 번역 모델의 **Thinking Mode 학습**을 위한 균형 잡힌 샘플 데이터셋입니다.
각 언어쌍에서 **동일한 수량**을 랜덤 추출하여 빠른 실험이 가능합니다.

## 이 데이터로 학습한 모델
이 데이터로 학습했다는 기록(학습 설정 · 모델 카드)을 찾지 못했다. 카탈로그의 '확인 필요' 목록에 있다.

## 파일 구성
| 파일 | 크기 | 행 | 내용 |
|---|---|---|---|
| `README.md` | 7.0 KB | - |  |
| `test/all_test_fast.jsonl` | 1.1 GB | 1,060,647 |  |
| `test/en-ko_test_fast.jsonl` | 168.9 MB | 151,521 |  |
| `test/ko-en_test_fast.jsonl` | 169.6 MB | 151,521 |  |
| `test/ko-id_test_fast.jsonl` | 137.7 MB | 151,521 |  |
| `test/ko-ja_test_fast.jsonl` | 178.8 MB | 151,521 |  |
| `test/ko-tl_test_fast.jsonl` | 136.8 MB | 151,521 |  |
| `test/ko-vi_test_fast.jsonl` | 138.4 MB | 151,521 |  |
| `test/ko-zh_test_fast.jsonl` | 171.2 MB | 151,521 |  |
| `train/all_train_fast.jsonl` | 4.4 GB | 4,242,581+ |  |
| `train/en-ko_train_fast.jsonl` | 675.2 MB | 606,083 |  |
| `train/ko-en_train_fast.jsonl` | 678.6 MB | 606,083 |  |
| `train/ko-id_train_fast.jsonl` | 550.6 MB | 606,083 |  |
| `train/ko-ja_train_fast.jsonl` | 715.8 MB | 606,083 |  |
| `train/ko-tl_train_fast.jsonl` | 547.6 MB | 606,083 |  |
| `train/ko-vi_train_fast.jsonl` | 553.7 MB | 606,083 |  |
| `train/ko-zh_train_fast.jsonl` | 684.2 MB | 606,083 |  |

## 필드 · 범주 분포
**`test/all_test_fast.jsonl`, `test/en-ko_test_fast.jsonl`, `test/ko-en_test_fast.jsonl`, `test/ko-id_test_fast.jsonl`, `test/ko-ja_test_fast.jsonl`, `test/ko-tl_test_fast.jsonl` 외 10개** (기준 `train/all_train_fast.jsonl`)

| 필드 | 타입 | 채움 |
|---|---|---|
| `messages` | list | 100% |
| `metadata` | dict | 100% |

필드는 행 최상위 키, 채움은 그 키가 있는 행 비율이다. 범주 분포는 글 필드가 아니고 값이 짧고(≤48자) 종류가 적은(≤40) 필드만 셌다.

## 내려받기 · 복원
```bash
hf download neuralfoundry-coder/multilingual-translation-thinking-fast --repo-type dataset --local-dir <폴더>
```
- 서버 파일 전체의 위치 · 재생성 방법: [`neuralfoundry-coder/workspace-data-catalog_261020`](https://huggingface.co/datasets/neuralfoundry-coder/workspace-data-catalog_261020) 의 `restore_map.json`

## 기존 설명 (2026-10-20 이전 카드)

### 다국어 번역 데이터셋 - Thinking Mode (Balanced Fast)

#### 📋 Dataset Description

다국어 번역 모델의 **Thinking Mode 학습**을 위한 균형 잡힌 샘플 데이터셋입니다.
각 언어쌍에서 **동일한 수량**을 랜덤 추출하여 빠른 실험이 가능합니다.

##### ✨ Key Features

- 🧠 **Thinking Mode**: 번역 시 사고 과정 포함
- 🎯 **Balanced Data**: 모든 언어쌍 동일 수량 (언어 편향 방지)
- ⚡ **Fast Experimentation**: 전체 대비 약 1/10 크기
- 🔄 **Reproducible**: 랜덤 시드 42로 고정

##### Key Difference from Standard Dataset

| 항목 | Standard | **Thinking Mode** |
|------|----------|-------------------|
| System Prompt | ❌ | ✅ 전문 번역가 역할 |
| Thinking Field | ❌ | ✅ 번역 추론 과정 포함 |
| Thinking Effort | ❌ | ✅ low/medium/high 레벨 |

#### 📊 Dataset Statistics

##### Train Split (언어쌍별 606,083건)

| Language Pair | Records | File Size |
|---------------|---------|-----------|
| ko-en | 606,083 | 648MB |
| en-ko | 606,083 | 644MB |
| ko-zh | 606,083 | 653MB |
| ko-ja | 606,083 | 683MB |
| ko-id | 606,083 | 526MB |
| ko-vi | 606,083 | 529MB |
| ko-tl | 606,083 | 523MB |
| **Total** | **4,242,581** | **4.2GB** |

##### Test Split (언어쌍별 151,521건)

| Language Pair | Records | File Size |
|---------------|---------|-----------|
| ko-en | 151,521 | 162MB |
| en-ko | 151,521 | 162MB |
| ko-zh | 151,521 | 164MB |
| ko-ja | 151,521 | 171MB |
| ko-id | 151,521 | 132MB |
| ko-vi | 151,521 | 132MB |
| ko-tl | 151,521 | 131MB |
| **Total** | **1,060,647** | **1.1GB** |

##### Overall Statistics

| Split | Records | Size |
|-------|---------|------|
| Train | 4,242,581 | 4.2GB |
| Test | 1,060,647 | 1.1GB |
| **Total** | **5,303,228** | **5.3GB** |

#### 📁 Dataset Structure

```
├── train/
│   ├── all_train_fast.jsonl
│   ├── ko-en_train_fast.jsonl
│   ├── en-ko_train_fast.jsonl
│   ├── ko-zh_train_fast.jsonl
│   ├── ko-ja_train_fast.jsonl
│   ├── ko-id_train_fast.jsonl
│   ├── ko-vi_train_fast.jsonl
│   └── ko-tl_train_fast.jsonl
└── test/
    ├── all_test_fast.jsonl
    ├── ko-en_test_fast.jsonl
    ├── en-ko_test_fast.jsonl
    ├── ko-zh_test_fast.jsonl
    ├── ko-ja_test_fast.jsonl
    ├── ko-id_test_fast.jsonl
    ├── ko-vi_test_fast.jsonl
    └── ko-tl_test_fast.jsonl
```

#### 📝 Data Format

```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a professional translator specializing in Korean to English translation."
    },
    {
      "role": "user",
      "content": "Translate the given sentence or word from the source language into the target language.\n\nsource language: Korean (ko)\ntarget language: English (en)\n\nGiven sentence: 안녕하세요.\nTarget sentence:"
    },
    {
      "role": "assistant",
      "content": "Hello.",
      "thinking": "이 텍스트를 분석합니다. 한국어의 문장 구조를 파악하고 영어로 자연스럽게 옮깁니다."
    }
  ],
  "metadata": {
    "source_language": "ko",
    "target_language": "en",
    "domain": "일상",
    "is_mt": false,
    "thinking_effort": "medium",
    "original_format": "translation"
  }
}
```

##### Field Description

| Field | Description |
|-------|-------------|
| `messages[0]` | System prompt (전문 번역가 역할) |
| `messages[1]` | User request (번역 요청) |
| `messages[2].content` | Translation result |
| `messages[2].thinking` | **Reasoning process** ⭐ |
| `metadata.thinking_effort` | Effort level (low/medium/high) |

#### 🔧 Usage

##### Load with Datasets Library

```python
from datasets import load_dataset

dataset = load_dataset("neuralfoundry-coder/multilingual-translation-thinking-fast")

train_data = dataset['train']
test_data = dataset['test']

print(f"Train: {len(train_data):,} records")
print(f"Test: {len(test_data):,} records")
```

##### Training with Thinking

```python
def format_thinking_response(example):
    messages = example['messages']
    thinking = messages[2].get('thinking', '')
    response = messages[2]['content']
    
    # Format: <thinking>...</thinking>\nresponse
    return f"<thinking>{thinking}</thinking>\n{response}"

### Apply formatting
train_data = train_data.map(lambda x: {"formatted": format_thinking_response(x)})
```

##### Filter by Language Pair

```python
from datasets import load_dataset

### 특정 언어쌍만 로드
dataset = load_dataset(
    "neuralfoundry-coder/multilingual-translation-thinking-fast",
    data_files={
        "train": "train/ko-en_train_fast.jsonl",
        "test": "test/ko-en_test_fast.jsonl"
    }
)
```

#### 🎯 Recommended Use Cases

1. **Thinking Mode 실험**: 사고 과정 학습 효과 검증
2. **하이퍼파라미터 튜닝**: 빠른 실험으로 최적 설정 탐색
3. **균형 학습**: 저자원 언어 성능 향상
4. **모델 비교**: 여러 모델 빠르게 벤치마킹
5. **프로토타이핑**: 새로운 기법 빠르게 테스트

#### 📈 Related Datasets

| Dataset | Type | Records | Size |
|---------|------|---------|------|
| Full | Thinking | 52.7M | ~50GB |
| **This (Fast)** | **Thinking** | **5.3M** | **~5GB** |
| Standard Full | No Thinking | 52.7M | ~26GB |
| Standard Fast | No Thinking | 5.3M | ~3GB |

#### ⚠️ Notes

- 최종 배포 모델 학습 시에는 **Full 데이터셋** 사용 권장
- 랜덤 샘플링으로 도메인 분포가 원본과 다를 수 있음
- Thinking 필드는 다양한 언어(한국어/영어)로 작성됨

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
@dataset{multilingual_translation_thinking_fast,
  title={Multilingual Translation Dataset - Thinking Mode (Balanced Fast)},
  author={neuralfoundry-coder},
  year={2024},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/neuralfoundry-coder/multilingual-translation-thinking-fast}
}
```
