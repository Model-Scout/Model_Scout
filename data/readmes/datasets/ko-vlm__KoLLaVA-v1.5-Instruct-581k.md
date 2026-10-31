---
license: apache-2.0
language:
- ko
- en
tags:
- multimodal
- vision-language
- korean
- kollava
size_categories:
- 100K<n<1M
---

# KoLLaVA-v1.5-Instruct-581k

한국어 Vision-Language 모델을 위한 instruction tuning 데이터셋입니다.

## 데이터셋 정보
- **총 샘플 수**: 435,093개
- **형식**: ChatML 형식 (role: user/assistant, content: 텍스트)
- **이미지**: COCO + GQA + Visual Genome 데이터셋
- **언어**: 한국어

## 포함된 데이터셋
1. **COCO 데이터**: 362,953개 샘플
   - MS COCO 2017 이미지 기반
   - 한국어 대화 데이터
   
2. **GQA 데이터**: 72,140개 샘플
   - GQA (Visual Question Answering) 이미지 기반
   - 한국어 대화 데이터

3. **Visual Genome 데이터**: 포함
   - Visual Genome 이미지 기반
   - 한국어 대화 데이터

## 제외된 데이터셋
- **EKVQA 데이터**: AI Hub 라이선스로 인해 공개 불가

## 사용법
```python
from datasets import load_dataset

dataset = load_dataset("ko-vlm/KoLLaVA-v1.5-Instruct-435k")
print(f"총 샘플 수: {len(dataset['train']):,}개")

# 첫 번째 샘플 확인
sample = dataset['train'][0]
print(f"이미지: {sample['image']}")
print(f"대화: {sample['conversations']}")
```

## 라이선스
- Apache 2.0 License
- 원본 데이터셋의 라이선스를 따릅니다.

## 원본 데이터셋
- [KoLLaVA-v1.5-Instruct-581k](https://huggingface.co/datasets/tabtoyou/KoLLaVA-v1.5-Instruct-581k)
