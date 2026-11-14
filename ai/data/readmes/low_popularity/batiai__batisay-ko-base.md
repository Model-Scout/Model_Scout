---
language:
  - ko
license: apache-2.0
library_name: whisper.cpp
tags:
  - whisper
  - whisper-turbo
  - korean
  - speech-recognition
  - asr
  - ggml
  - whisper.cpp
  - batiai
  - batisay
base_model: openai/whisper-large-v3-turbo
model_type: whisper
pipeline_tag: automatic-speech-recognition
---

# batisay-ko-base 1.0 — 무료 한국어 STT (Apache 2.0)

한국어 fine-tuned Whisper Large v3 Turbo (809M). **Apache 2.0 · 게이팅 없음 · 외부 판매 포함 자유 사용.**
실사용 통화(long-form)에 **강건한 무료 base 모델** — BatiFlow App 의 기본 통화 백업 모델.

## CER 벤치마크

| 측정 | batisay-ko-base | 비교 |
|------|-----------------|------|
| 일반 음성 (KsponSpeech clean, RTZR-strict N=500) | **7.77%** | Whisper Large v3 raw 17.03% / RTZR API 5.91-6.18% |
| **실사용 통화 (2~51분 long-form, 5건)** | **19.11%** | 다양한 화자·환경에서 안정적 (turbo 1.1 은 14.85%) |

> base 의 강점은 **실통화 일반화 강건성** 입니다. 학습은 일반 음성 위주지만, 과적합이 없어 실사용 통화에서 무난합니다.

## 파일

```
ggml-batisay-ko-base.bin         1.6 GB  (F32, 최고 quality)
ggml-batisay-ko-base-q5_0.bin    547 MB  (Q5, balanced) ⭐ 권장
ggml-batisay-ko-base-q4_0.bin    452 MB  (Q4, Mac 8GB)
model.safetensors                1.6 GB  (transformers / MLX 소스)
```

## 사용 — whisper.cpp / BatiFlow App

```bash
huggingface-cli download batiai/batisay-ko-base ggml-batisay-ko-base-q5_0.bin --local-dir .
./whisper-cli -m ggml-batisay-ko-base-q5_0.bin -l ko -f audio.wav --output-txt
```

## 사용 — Python (transformers)

```python
from transformers import WhisperForConditionalGeneration, WhisperProcessor
model = WhisperForConditionalGeneration.from_pretrained('batiai/batisay-ko-base')
processor = WhisperProcessor.from_pretrained('batiai/batisay-ko-base', language='Korean', task='transcribe')
```

## 학습

- Base: openai/whisper-large-v3-turbo (809M params)
- Data: KsponSpeech 1000h + Zeroth-Korean 50h
- Epoch 3, LR 1e-5 linear, 2 GPU DDP (A6000 48GB), train 35.8h
- 학습 시점: 2026-05-28 · 내부 빌드: V7

## 라이선스

Apache 2.0 (BatiAI Open Tier 1) — 게이팅 없음, 상업·외부 SaaS 포함 제약 없음.

## 관련 모델 (batisay STT 라인업)

| 모델 | 버전 | 라이선스 | 특징 |
|------|------|---------|------|
| **batisay-ko-base** (본 모델) | 1.0 | **Apache 2.0** (무료) | 무료·강건. 일반 7.77% / 실통화 19.11% |
| [batisay-ko-turbo](https://huggingface.co/batiai/batisay-ko-turbo) | 1.1 | Community v2 (gated) | 통화·회의·대화 멀티도메인 강화. 실통화 **14.85%** (base 추월), 일반 6.99% |
| [batisay-ko-large](https://huggingface.co/batiai/batisay-ko-large) | 1.0 | Community v2 (gated) | 고품질 문서/clean 전사 특화 |

→ **무료·외부 SaaS = base (본 모델)** / **통화·멀티도메인 정확도 = turbo 1.1** / **문서 전사 = large**

문의: support@bati.ai · https://flow.bati.ai
