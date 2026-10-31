---
license: mit
task_categories:
- text-generation
- question-answering
language:
- ko
tags:
- hallucination
- benchmark
- evaluation
- korean
size_categories:
- n<1K
pretty_name: Hallucination Benchmark v1
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test-*
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: answer
    dtype: string
  - name: task
    dtype: string
  - name: reference
    dtype: string
  splits:
  - name: test
    num_bytes: 1500000
    num_examples: 244
  download_size: 800000
  dataset_size: 1500000
---

# Hallucination Benchmark v1

## Dataset Description

**Hallucination Benchmark**는 한국어 LLM의 환각(Hallucination) 탐지 성능을 평가하기 위한 벤치마크 데이터셋입니다.

### Dataset Summary

- **언어**: 한국어 (Korean)
- **샘플 수**: 244개
- **태스크**: 6가지 (Coding, Dialogue, General, Math, QA, Summarization)
- **환각 타입**: 5가지 (No Hallucination, Factual Contradiction, Factual Fabrication, Instruction Inconsistency, Logical Inconsistency)

### Supported Tasks

이 벤치마크는 다음과 같은 태스크를 포함합니다:

1. **Coding** (40 samples): 코드 생성 및 프로그래밍 문제
2. **Dialogue** (40 samples): 대화 생성
3. **General** (41 samples): 일반적인 질의응답
4. **Math** (41 samples): 수학 문제 풀이
5. **QA** (41 samples): 질문-답변
6. **Summarization** (41 samples): 요약 생성

### Languages

한국어 (ko)

## Dataset Structure

### Data Instances

각 데이터 샘플은 다음과 같은 구조를 가집니다:

```json
{
  "instruction": "주어진 문제를 풀어주세요.",
  "input": "당신은 인공지능 비서입니다.",
  "answer": "문제에 대한 답변입니다.",
  "task": "qa",
  "reference": "https://huggingface.co/datasets/amphora/fc-ko-project-sft-v0"
}
```

### Data Fields

- `instruction` (string): 모델에게 주어지는 지시사항
- `input` (string): 추가 입력 컨텍스트
- `answer` (string): Ground truth 답변
- `task` (string): 태스크 카테고리 (coding, dialogue, general, math, qa, summarization)
- `reference` (string): 원본 데이터 출처

### Data Splits

| Split | Samples |
|-------|---------|
| test  | 244     |

## Dataset Creation

### Curation Rationale

이 데이터셋은 한국어 LLM의 환각 탐지 및 평가를 위해 큐레이션되었습니다. Cross-model validation과 Fleiss' Kappa 기반 합의 메트릭을 사용하여 고품질 ground truth 답변을 검증했습니다.

### Source Data

원본 데이터는 다음 출처에서 수집되었습니다:
- [Amphora FC-KO Project SFT v0](https://huggingface.co/datasets/amphora/fc-ko-project-sft-v0)

### Annotations

각 샘플은 다음 4가지 차원에서 평가되었습니다:
- **Factual Accuracy** (사실 정확성): 1-5 점수
- **Groundedness** (근거 기반성): 1-5 점수
- **Internal Consistency** (내적 일관성): 1-5 점수
- **Completeness** (완전성): 1-5 점수

평가는 여러 LLM(GPT-4o, Claude Sonnet, Claude Haiku)을 사용한 cross-model validation을 통해 수행되었습니다.

## Considerations for Using the Data

### Social Impact of Dataset

이 데이터셋은 한국어 LLM의 환각 탐지 성능을 개선하고, 더 신뢰할 수 있는 AI 시스템 개발에 기여하는 것을 목표로 합니다.

### Discussion of Biases

데이터셋은 특정 도메인(코딩, 수학 등)에 편향될 수 있으며, 모든 환각 유형을 균등하게 커버하지 못할 수 있습니다.

### Other Known Limitations

- 샘플 수가 244개로 제한적입니다
- 특정 도메인에 대한 전문 지식이 필요할 수 있습니다

## Additional Information

### Dataset Curators


- Main Contributor: [jiwon9703](https://huggingface.co/jiwon9703)
- Co-Contributor: [chahyunmook](https://huggingface.co/chahyunmook)

### Licensing Information

MIT License

### Citation Information

```bibtex
@dataset{hallucination_benchmark_v1,
  title={Hallucination Benchmark v1},
  author={Jeong, Jiwon and Cha, Hyunmook},
  year={2025},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/jiwon9703/hallucination-benchmark-v1}
}
```

### Contributions

벤치마크에 대한 제안이나 개선 사항이 있으시면 Community에 남겨주세요.



### Hallucination Types

이 벤치마크는 다음 5가지 환각 타입을 탐지합니다:

1. **No Hallucination**: 환각 없음
2. **Factual Contradiction**: 사실 모순 (주어진 정보와 상충)
3. **Factual Fabrication**: 사실 조작 (존재하지 않는 정보 생성)
4. **Instruction Inconsistency**: 지시사항 불일치 (지시사항 무시 또는 왜곡)
5. **Logical Inconsistency**: 논리적 불일치 (내적 모순)

### Task Distribution

| Task | Samples | Percentage |
|------|---------|------------|
| Coding | 40 | 16.4% |
| Dialogue | 40 | 16.4% |
| General | 41 | 16.8% |
| Math | 41 | 16.8% |
| QA | 41 | 16.8% |
| Summarization | 41 | 16.8% |
| **Total** | **244** | **100%** |

## Usage

### Loading the Dataset

```python
from datasets import load_dataset

# 데이터셋 로드
dataset = load_dataset("jiwon9703/hallucination-benchmark-v1")

# 첫 번째 샘플 확인
print(dataset["test"][0])
```

### Example Code

```python
from datasets import load_dataset

# 데이터셋 로드
dataset = load_dataset("jiwon9703/hallucination-benchmark-v1")

# 태스크별로 필터링
qa_samples = dataset["test"].filter(lambda x: x["task"] == "qa")
print(f"QA samples: {len(qa_samples)}")

# 샘플 순회
for sample in dataset["test"]:
    instruction = sample["instruction"]
    answer = sample["answer"]
    task = sample["task"]
    print(f"Task: {task}")
    print(f"Instruction: {instruction[:100]}...")
    print(f"Answer: {answer[:100]}...")
    print("-" * 50)
```

## Contact

문의사항이 있으시면 jwjw9603@gmail.com으로 문의 주세요!
