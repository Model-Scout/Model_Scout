---
language:
- ko
tags:
- korean
- causal-lm
- llama
- yejin
- pretraining
- 1b
license: apache-2.0
pipeline_tag: text-generation
---

# yejin-korean-1b-v8 🚀

> **yejin-korean-1b-v8**는 한국어 172GB+ 대규모 고품질 코퍼스(Culturax, 위키백과 2024, 교과서 6종 등)로 100% 바닥부터 사전학습(Pre-trained from Scratch, 25,000 Steps)된 한국어 1B 베이스 파운데이션 모델입니다.

---

## 📊 모델 아키텍처 사양
- **기반 규격**: Llama 3 참조 아키텍처 (`hidden=2048`, `layers=18`, `heads=16`, `kv_heads=4`, `intermediate=5632`, `GQA 4:1`)
- **파라미터 수**: 0.93B (932M)
- **토크나이저**: `EleutherAI/polyglot-ko-1.3b` (어휘 크기: 30,003)
- **컨텍스트 길이**: 4,096 토큰
- **포맷**: `safetensors`