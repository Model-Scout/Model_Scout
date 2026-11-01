---
license: other
license_name: kvqa-license
license_link: https://huggingface.co/datasets/skt/KVQA
language:
- ko
task_categories:
- visual-question-answering
task_ids:
- visual-question-answering
size_categories:
- 100K<n<1M
pretty_name: KVQA (Korean VQA) - ChatML Format
configs:
- config_name: default
  data_files:
  - split: train
    path: "*.parquet"
  default: true
tags:
- korean
- vqa
- visual-question-answering
- multimodal
- chatml
- conversation
---

# KVQA-ChatML Dataset

이 데이터셋은 SKT의 KVQA 데이터셋을 ChatML 형식으로 변환한 것입니다.

## 데이터셋 정보

- **원본 데이터셋**: [skt/KVQA](https://huggingface.co/datasets/skt/KVQA)
- **총 샘플 수**: 약 100,000개
- **파일 수**: 100개 parquet 파일
- **포맷**: ChatML (user/assistant 대화 형식)

## 데이터 구조

```python
{
    "image": PIL.Image,
    "conversations": [
        {"role": "user", "content": "질문"},
        {"role": "assistant", "content": "답변"}
    ],
    "id": "unique_id",
    "source": "KVQA",
    "answer_type": "answer_type",
    "answerable": boolean
}
```

## 사용 방법

```python
from datasets import load_dataset

dataset = load_dataset("ko-vlm/KVQA-ChatML")
```

## 라이선스

이 데이터셋은 원본 KVQA 데이터셋의 라이선스를 따릅니다.

### KVQA 원본 라이선스
- **데이터셋**: KVQA (Korean Visual Question Answering)
- **제공자**: SKT (SK Telecom)
- **라이선스**: 연구 및 비상업적 목적으로 사용 가능
- **출처**: https://huggingface.co/datasets/skt/KVQA

### 사용 제한사항
- 이 데이터셋은 연구 목적으로만 사용해야 합니다
- 상업적 사용은 원본 데이터셋 제공자의 허가가 필요합니다
- 데이터셋 사용 시 원본 KVQA 데이터셋을 인용해야 합니다

### 인용 정보
원본 KVQA 데이터셋을 사용할 때는 다음과 같이 인용해주세요:
```
@dataset{skt_kvqa,
  title={KVQA: Korean Visual Question Answering Dataset},
  author={SK Telecom},
  year={2023},
  url={https://huggingface.co/datasets/skt/KVQA}
}
```

## 면책사항

이 데이터셋은 연구 목적으로 제공되며, 정확성이나 완전성을 보장하지 않습니다. 사용자는 본 데이터셋 사용으로 인해 발생하는 모든 결과에 대해 책임을 집니다.
