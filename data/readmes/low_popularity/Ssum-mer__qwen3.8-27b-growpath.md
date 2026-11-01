---
model_name: GrowPath (Qwen3.8-27B)
language:
- ko
- en
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
base_model: Qwen/Qwen3.8-27B
base_model_relation: finetune
tags:
- growpath
- qwen3.8
- fine-tuned
- lora
- merged
- korean
- roadmap-generation
---

# GrowPath — Qwen3.8-27B · V18

**Qwen3.8-27B를 기반으로 파인튜닝한 GrowPath 업무 학습 로드맵 생성 모델.**

기본 모델에 LoRA 변경분을 병합한 전체 가중치입니다. 별도 LoRA 어댑터 적용 없이 병합 모델로 로드합니다.

## 모델 정보

| 항목 | 내용 |
|---|---|
| 기반 모델 | Qwen/Qwen3.8-27B |
| 기반 revision | `1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0` |
| 최종 버전 | GrowPath V18 |
| 최종 학습 에폭 | 2 · 제작자 확인 |
| 주요 용도 | 한국어 업무 학습 로드맵 생성·부분 수정 |
| 배포 형태 | LoRA 병합 전체 모델·BF16·Safetensors 12샤드 |
| 파라미터 | 27,356,728,560 |
| 가중치 크기 | 54,713,457,120 bytes |

## 아키텍처 표기

저장소와 기반 모델의 이름은 **Qwen3.8-27B**입니다. 저장된 config의 아키텍처 구현 이름은 `Qwen3_5ForConditionalGeneration`, model_type은 `qwen3_5`입니다. Hugging Face가 표시하는 `qwen3_5` 자동 태그는 이 config 필드에서 유래하며, 기반 저장소명과 구분합니다.

## 입력과 출력

업무 목표·현재 역량·기간·주당 학습시간·예산·학습 자료 등 제공된 조건을 입력으로 사용합니다. 로드맵과 부분 수정 요청의 구조화된 응답을 대상으로 파인튜닝했습니다. 출력된 기간·예산·자료 근거·수정 범위는 사용 전에 확인해야 합니다.

## 선정 배경

기존 모델보다 약 10% 우위라고 판단해 V18을 최종 선택했습니다. 업무 목적에 맞춘 답변 구성과 병합 모델의 배포·버전 관리 편의를 함께 고려했습니다. 10%는 제작자의 선정 판단이며, 이 모델 카드에서 새로 측정한 벤치마크 향상률을 뜻하지 않습니다.

## 사용 범위

업무 학습 계획 수립을 지원하는 모델입니다. 규정의 최신성·승인 상태와 추천 자료의 이용 가능성은 별도 검색·검증 경로에서 확인해야 합니다. 파인튜닝 모델 자체가 현재 DB나 최신 원문을 자동 조회하지는 않습니다.


## BF16 GGUF

텍스트 생성용 BF16 GGUF입니다. 기존 Safetensors12샤드도 그대로 유지합니다.

- 파일: [qwen3.8-27b-growpath-BF16.gguf](qwen3.8-27b-growpath-BF16.gguf)
- 크기: 53,808,282,112 bytes
- SHA256: `32d69322977ccd21240d4005a5b4cedb877702724c1159a57faa174f87e1cb81`
- [변환 기록](gguf_conversion_manifest_BF16.json) · [체크섬](qwen3.8-27b-growpath-BF16.gguf.sha256)
- 원본 모델: https://huggingface.co/Ssum-mer/qwen3.8-27b-growpath
- 4비트 모델: https://huggingface.co/Ssum-mer/qwen3.8-27b-growpath-Q4
- 모델 버전: V18 · 원본학습2에폭(제작자 확인)
- 원본 revision: `66d1af509ab0681f3b9365227e5c794c65801fbf`

A100에서 모델 로딩·짧은 한국어 생성을 확인했습니다. 전체 품질 재평가 결과는 아닙니다. 이미지 입력용 vision projector는 포함하지 않습니다. 저장소명은 Qwen3.8이며 구현 아키텍처 이름은 qwen3_5입니다.
