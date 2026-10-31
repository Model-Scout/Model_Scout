---
license: other
language: [ko]
pretty_name: Korean RelayS2S synthetic dialog features
---

# 한국어 RelayS2S 재현용 학습 데이터 (fbank 특징)

RelayS2S(arXiv:2603.23346)의 한국어 재현 연구에 쓰는 lhotse shar 입니다. **원음은 들어 있지
않고** 80차원 fbank 특징과 대본, 전이중 타이밍 주석만 있습니다. 대화는 LLM 으로 생성하고
TTS 로 합성한 **합성 데이터**이며 실제 사람의 음성이나 대화가 아닙니다.

| 경로 | 내용 |
|---|---|
| `shar/train_53h` | 로컬 35B 모델로 생성한 대화 (53h) |
| `shar/train_100h` · `shar/train` | GLM 으로 생성한 대화 (100h ⊂ 155h), ASR 왕복 CER·UTMOS 필터 적용 |
| `shar/valid` · `shar/valid_glm` | 평가용 (각 51 대화) |

연구용으로 공개하며 품질을 보증하지 않습니다.
