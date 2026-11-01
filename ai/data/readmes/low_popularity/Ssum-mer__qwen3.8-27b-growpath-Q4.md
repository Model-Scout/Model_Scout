---
model_name: GrowPath Q4 (Qwen3.8-27B, V18)
language:
- ko
- en
license: apache-2.0
pipeline_tag: text-generation
base_model: Ssum-mer/qwen3.8-27b-growpath
base_model_relation: quantized
tags:
- gguf
- qwen3.8
- qwen3_5
- growpath
- quantized
- Q4_K_M
- korean
- roadmap-generation
---

# GrowPath Q4 — Qwen3.8-27B · V18

Qwen3.8-27B 기반 GrowPath V18의 텍스트 생성용 **Q4_K_M GGUF**입니다.
원본 병합 BF16을 GGUF로 변환한 뒤4비트 계열 혼합 정밀도로 양자화했습니다. 별도 LoRA 적용은 필요하지 않습니다.

- 파일: [qwen3.8-27b-growpath-Q4.gguf](qwen3.8-27b-growpath-Q4.gguf)
- 크기: 16,547,400,192 bytes
- SHA256: `7626f16dc9237c04704011fc50c2b7e89a4d495c2cd1810f271746e96b1d9d16`
- [변환 기록](gguf_conversion_manifest_Q4_K_M.json) · [체크섬](qwen3.8-27b-growpath-Q4.gguf.sha256)
- 원본 모델: https://huggingface.co/Ssum-mer/qwen3.8-27b-growpath
- 4비트 모델: https://huggingface.co/Ssum-mer/qwen3.8-27b-growpath-Q4
- 모델 버전: V18 · 원본학습2에폭(제작자 확인)
- 원본 revision: `66d1af509ab0681f3b9365227e5c794c65801fbf`

A100에서 모델 로딩·짧은 한국어 생성을 확인했습니다. 전체 품질 재평가 결과는 아닙니다. 이미지 입력용 vision projector는 포함하지 않습니다. 저장소명은 Qwen3.8이며 구현 아키텍처 이름은 qwen3_5입니다.
