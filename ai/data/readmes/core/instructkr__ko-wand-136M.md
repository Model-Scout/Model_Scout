---
license:
- apache-2.0
language:
- ko
- en
pipeline_tag: text-generation
---
# **ko-wand-136M**

**ko-wand-136M**는 [**insturctkr**](https://instruct.kr)에서 사전학습한 SLM입니다.

# Model Description
[maywell/korean_textbooks](https://huggingface.co/datasets/maywell/korean_textbooks)와 한국어 말뭉치를 이용하여 사전학습 되었습니다.

## Model Info

미스트랄 아키텍쳐를 기반으로 완전히 랜덤 가중치를 시작으로 사전학습 된 모델입니다. Instruction 튜닝되지 않았습니다.

## Training Details
| Batch Size | Token Seen | lr |
|---|---|---|
| 1024 | 2.5B | 2e-3 (cosine)|

## License
apache-2.0