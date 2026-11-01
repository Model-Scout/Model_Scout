---
language:
- ko
license: cc-by-4.0
task_categories:
- text-classification
tags:
- hallucination
- korean
- sft
size_categories:
- 10K<n<100K
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
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
  - name: response
    dtype: string
  - name: label
    dtype: string
  splits:
  - name: train
    num_bytes: 115930225
    num_examples: 48581
  - name: test
    num_bytes: 383874
    num_examples: 100
  download_size: 57422510
  dataset_size: 116314099
---

# Korean Hallucination Classification Dataset

한국어 할루시네이션 분류 데이터셋입니다.

## Dataset Description

답변1(정답)을 기준으로 답변2(모델 응답)를 비교하여 할루시네이션 타입을 분류하는 데이터셋입니다.

### Hallucination Types
- **No Hallucination**: 할루시네이션이 없는 정상 답변
- **Factual Contradiction**: 사실 모순 - 알려진 사실과 모순되는 내용
- **Factual Fabrication**: 사실 조작 - 존재하지 않는 사실을 만들어냄
- **Instruction Inconsistency**: 지시 불일치 - 주어진 지시사항을 따르지 않음
- **Logical Inconsistency**: 논리 불일치 - 논리적 모순이 있는 답변

## Dataset Structure

### Data Fields

- `instruction`: 질문 또는 지시사항
- `input`: 시스템 프롬프트 또는 추가 컨텍스트
- `answer`: 답변1 (정답 참조)
- `response`: 답변2 (평가 대상 모델 응답)
- `label`: 할루시네이션 타입 레이블

### Data Sources

이 데이터셋은 다음 소스들을 결합하여 구성되었습니다:

1. **Factual Hallucination Data**: KorQuAD, 요약, 논문 요약, 상식 질문 데이터
2. **Instruction/Logical Inconsistency Data**: 지시 불일치 및 논리 불일치 데이터
3. **Non-Hallucination Data**: Back-translation 기법을 통해 생성된 정상 답변 데이터

## Usage

```python
from datasets import load_dataset

dataset = load_dataset("jiwon9703/ko-hallucination-sft-v1")
```

## Contributors

- **Jiwon Jeong** ([@jiwon9703](https://huggingface.co/jiwon9703))
- **Hyunmook Cha** ([@chahyunmook](https://huggingface.co/chahyunmook))

## Citation

이 데이터셋을 사용하시는 경우 아래와 같이 인용해주세요:

```bibtex
@dataset{ko_hallucination_sft_v1,
  author = {Jeong, Jiwon and Cha, Hyunmook},
  title = {Korean Hallucination Classification Dataset},
  year = {2025},
  publisher = {Hugging Face},
  url = {https://huggingface.co/datasets/jiwon9703/ko-hallucination-sft-v1}
}
```

## License

This dataset is released under the CC-BY-4.0 license.