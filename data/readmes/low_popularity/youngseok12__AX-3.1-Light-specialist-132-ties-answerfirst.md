---
license: apache-2.0
license_link: https://www.apache.org/licenses/LICENSE-2.0
base_model: skt/A.X-3.1-Light
language:
- ko
library_name: transformers
pipeline_tag: text-generation
tags:
- korean
- text-generation
- instruction-tuning
- supervised-fine-tuning
- lora
- merged-model
- model-merging
- ties
- answer-first
---

# A.X-3.1-Light Specialist-132 TIES + Answer-First Correction

이 모델은 `skt/A.X-3.1-Light`에 축별 specialist LoRA 3개(K/R/C, 각 132행)를
TIES로 병합한 뒤, 그 결과물 위에 answer-first 출력 보정 LoRA를 추가로 학습해
다시 병합한 BF16 전체 가중치 모델입니다. 프로젝트 파이프라인의 마지막 단계
(specialist merge → 출력 행동 정리)를 그대로 적용한 버전입니다. 연구 및
평가용이며, 생성 결과가 부정확할 수 있으므로 고위험 의사결정의 유일한 근거로
사용해서는 안 됩니다.

## Model information

- Base model: [`skt/A.X-3.1-Light`](https://huggingface.co/skt/A.X-3.1-Light)
- Base model revision: `9b41bb2406472634d8812c0b8931fa40fa9a6c3a`
- Model format: standalone BF16 `safetensors`; no separate adapter is required

## Pipeline (2 stages)

**Stage 1 — specialist merge**: K(KMMLU-Pro)/R(MuSR)/C(Com2-main) specialist
LoRA를 각 132행(위치 균형 33/33/33/33, correct_unstable 개념 — base가 자유
생성으론 맞히지만 형식 통제·보기순서 변경에 실패하는 문항)으로 학습해 TIES
(density 0.5)로 병합. 세부는 `AX-3.1-Light-specialist-300-ties`와 동일 방법론,
행 수만 축소.

**Stage 2 — answer-first correction**: Stage 1 병합본 위에, 기존 v0.21
(`AX-3.1-Light-sft_v0_21`) 학습에 쓴 것과 **동일한 데이터**
(`format_sft_answer_first_v1.jsonl`, 5,801행, AI Hub 569/71874/71857/71949/71610
출처)로 LoRA를 추가 학습해 병합. target schema는 `정답: X (근거: <한 문장>)`
압축형이며, v0.21과 동일한 조건(rank16/alpha32/lr 5e-5 cosine/epoch1)이다.

## Local diagnosis (n=100/axis, canonical suite, A_acc)

| 축 | base | Stage 1만(A안) | 이 모델(+보정) |
|---|---:|---:|---:|
| click | 0.664 | 0.72 | 0.71 |
| kmmlu_pro | 0.310 | 0.37 | 0.37 |
| com2_main | 0.610 | 0.66 | 0.67 |
| snu_ko_musr | 0.476 | 0.49 | 0.51 |
| 평균 | 0.515 | 0.560 | 0.565 |

## Known limitations

- n=100/축 로컬 진단은 이전 실험(`correct_all`/`correct_unstable`)에서 KMMLU-Pro
  방향을 실측과 정반대로 예측한 전례가 있어, 위 표의 KMMLU-Pro 상승을 실측
  근거로 쓸 수 없다.
- Stage 1(K/R/C-132) 단독 실측 결과는 이 리포지토리 업로드 시점에 아직 없다.
