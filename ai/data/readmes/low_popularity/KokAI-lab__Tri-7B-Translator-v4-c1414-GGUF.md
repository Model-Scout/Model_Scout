---
language:
  - ko
  - en
pipeline_tag: text-generation
library_name: gguf
base_model: trillionlabs/Tri-7B
base_model_relation: finetune
tags:
  - gguf
  - translation
  - korean
  - english
  - qlora
  - experimental
---

# Tri-7B Translator v4 (c1414) — GGUF

KokAI-lab에서 제작한 **한국어 ↔ 영어 번역용 실험 모델**입니다. [Trillion Labs의 Tri-7B](https://huggingface.co/trillionlabs/Tri-7B)를 번역 데이터로 파인튜닝하고, 로컬 환경에서 실행할 수 있도록 GGUF 형식으로 변환했습니다.

실제 사용에서 확인한 번역 오류가 남아 있으며, 완성된 상용 통역기보다는 **로컬 번역 모델의 개발 과정과 한계를 공유하기 위한 결과물**입니다.

## 개발 목적

외부 번역 API에 지속적으로 의존하지 않고, 개인 PC나 자체 서버에서 사용할 수 있는 한·영 양방향 번역 엔진을 만드는 것이 목표였습니다. 음성인식 결과를 번역해 회의·대화 자막으로 보여주는 실시간 통역 프로그램에 연결하는 용도로 개발했습니다.

이 모델은 **텍스트 번역만 담당**합니다. 음성인식(STT)과 음성합성(TTS)은 별도 프로그램이 필요합니다.

## 사용 데이터셋

한국지능정보사회진흥원(NIA)의 AI 학습용 데이터 구축사업 결과물인 AI Hub의 **[국제 학술대회용 전문분야 한영/영한 통번역 데이터](https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71693)** 일부를 사용했습니다.

국제 학술대회 발화를 바탕으로 만든 한·영 양방향 번역 데이터로, **공학·의약학·인문사회과학·자연과학** 분야를 포함합니다. 본 모델에는 음성 파일이 아닌 텍스트 원문과 번역문을 학습에 사용했습니다.

## 데이터 정제와 학습 과정

**데이터 선별·정제:** 원본 JSON의 원문·정제문과 번역문을 활용해 번역문 유효성 검사 및 중복 제거를 진행했습니다. 번역 방향과 분야의 균형을 맞춰 초기 학습 데이터 **50,000개**를 구성했으며, 한국어→영어와 영어→한국어를 각각 25,000개씩 포함했습니다. 검증용과 테스트용 데이터는 각각 2,000개씩 별도로 구성했습니다.

**취약 유형 보강:** 이후 버전에서 숫자·금액·단위, 말을 도중에 고치는 정정 발화, 전문용어 등을 보완하기 위한 예시를 추가·재구성했습니다. v4의 최종 학습 데이터는 **56,557개**이며, AI Hub에서 선별한 데이터와 프로젝트 자체 보강 예시를 함께 사용했습니다.

**파인튜닝·변환:** QLoRA 기반 지도 미세조정(SFT)으로 원문에 대응하는 번역문을 학습했습니다. 주요 LoRA 설정은 `r=16`, `alpha=32`, `dropout=0.05`입니다. 1 epoch 학습 실행에서 생성된 체크포인트들을 비교해 **checkpoint-1414**를 공개 대상으로 선택했습니다. 모델명의 `c1414`는 이 체크포인트를 의미합니다.

선택한 LoRA 가중치를 기반 모델에 병합한 뒤 BF16 GGUF로 변환하고, Q4_K_M과 Q5_K_M 양자화 파일을 만들었습니다.

## 제공 파일

| 구분 | 형식 | 파일 크기 |
|---|---|---:|
| 4-bit | `Q4_K_M` | 4.63 GB |
| 5-bit | `Q5_K_M` | 5.38 GB |
| 16-bit | `BF16` | 15.1 GB |

용량은 Hugging Face에 표시된 파일 크기 기준입니다. 파일 크기와 실행 시 필요한 메모리 사용량은 별개입니다. BF16은 16-bit 형식이며, Q4_K_M·Q5_K_M과 같은 저비트 양자화 파일은 아닙니다.

## 평가 결과와 실제 한계

선택한 체크포인트는 내부 개발용 평가 데이터 200개에서 **BLEU 32.22, chrF++ 57.65**를 기록했습니다. 이는 소규모 개발 평가 결과이며, 공개된 각 GGUF 파일의 독립 평가 점수나 실제 통역 정확도를 뜻하지 않습니다.

실제 테스트에서는 다음 문제가 확인되었습니다.

| 항목 | 확인된 문제 |
|---|---|
| 숫자·금액·단위 | 큰 수의 자릿수나 금액 단위를 잘못 옮기는 오류 |
| 정정 발화 | 날짜나 숫자를 말하다 수정하는 문장에서 정정 내용을 정확히 전달하지 못하는 오류 |
| 번역 지시 처리 | 입력 문장 대신 번역 지시문 자체를 번역하거나, 요청한 출력 형식을 따르지 않는 사례 |

음성인식 결과를 입력하는 환경에서는 STT의 오인식이나 잘못된 문장 분절이 번역 품질에 추가로 영향을 줄 수 있습니다. 학술 발화 중심의 학습 데이터이므로 일상 대화나 업무 문서 등 다른 유형에서도 동일한 품질을 보장하지 않습니다.

**중요한 문서나 금액·날짜가 포함된 번역은 원문과 대조해야 합니다.** 데이터 보강과 내부 평가만으로 실제 통역에서의 문제가 모두 해결되지는 않았으며, 이러한 한계까지 포함해 연구·실험·개선 목적으로 공개합니다.

## 출처 및 이용 안내

기반 모델 [Tri-7B](https://huggingface.co/trillionlabs/Tri-7B)의 라이선스는 Apache-2.0입니다. 원본 데이터의 이용조건은 [AI Hub 이용정책](https://aihub.or.kr/intrcn/guid/usagepolicy.do?currMenu=151&topMenu=105)을 참고해 주세요.

파인튜닝 및 GGUF 변환: **KokAI-lab**


## English Summary

**Tri-7B Translator v4 (c1414)** is an experimental Korean ↔ English translation model developed by **KokAI-lab**, based on [Trillion Labs’ Tri-7B](https://huggingface.co/trillionlabs/Tri-7B).

### Purpose

The goal is to build a translation engine that runs on personal computers or self-hosted servers without relying on external translation APIs. It was developed for integration into a real-time interpreting application. The model translates **text only**; speech recognition and speech synthesis require separate components.

### Dataset and Training

Training uses a subset of [AI Hub Dataset 71693 — 국제 학술대회용 전문분야 한영/영한 통번역 데이터](https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71693), produced through NIA’s AI training data program. It contains Korean–English translation pairs from academic conference speech across engineering, medicine, humanities and social sciences, and natural sciences.

Preprocessing included translation-pair validation, deduplication, and balanced initial sampling across translation directions and domains. Project-specific examples were added to address numbers, units, spoken self-corrections, and terminology, resulting in **56,557 training examples**.

The model was fine-tuned using **QLoRA**. The selected **checkpoint-1414** was merged with the base model and converted to GGUF.

### Available Files

| Format | File size |
|---|---:|
| Q4_K_M | 4.63 GB |
| Q5_K_M | 5.38 GB |
| BF16 | 15.1 GB |

### Known Limitations

Actual testing revealed errors involving large numbers, monetary units, spoken corrections, and translation instructions. Speech-recognition errors can further reduce translation quality.

This release shares an experimental development result, not a production-ready interpreting system. Important translations—especially those containing amounts or dates—require human review.
