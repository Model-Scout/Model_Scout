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
---

# A.X-3.1-Light Specialist-300 TIES (K+R+C)

이 모델은 `skt/A.X-3.1-Light`에 축별 specialist LoRA 3개(K/R/C)를 각각 300행으로
학습한 뒤 TIES로 병합한 BF16 전체 가중치 모델입니다. 세 LoRA 모두 **base 모델이
직접 문제를 풀어 생성한 근거를 target에 포함**하는 방식(success-consolidation)으로
만들어졌습니다. 연구 및 평가용이며, 생성 결과가 부정확할 수 있으므로 고위험
의사결정의 유일한 근거로 사용해서는 안 됩니다.

## Model information

- Base model: [`skt/A.X-3.1-Light`](https://huggingface.co/skt/A.X-3.1-Light)
- Base model revision: `9b41bb2406472634d8812c0b8931fa40fa9a6c3a`
- Merge recipe: **TIES**, weights 1.0/1.0/1.0, density 0.5
- Model format: standalone BF16 `safetensors`; no separate adapter is required

## What this model tests

이전 라운드(Round 1)의 specialist 병합은 target에 **근거 없이 답만** 학습시켜
"추론 중단" 습관을 세 LoRA가 공통으로 학습했고, 병합이 그것을 증폭해 성능이
붕괴했다. 이 모델은 그 원인을 고친(근거 포함 target) specialist를 **처음으로
병합**한 것이며, 동시에 학습 규모를 축당 3,000행 → 300행으로 줄였다.

## Components

| LoRA | 겨냥 축 | AI Hub 데이터 | 선별 개념 | 행 수 | train loss |
|---|---|---|---|---:|---:|
| K | KMMLU-Pro | [71875 필수의료 의학지식](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71875) | correct_unstable | 300 | 0.6672 |
| R | MuSR(Ko) | [71568 숫자연산 기계독해](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71568) | correct_unstable | 300 | 0.6066 |
| C | Com2-main(Ko) | [71949 인과관계 기반 추론](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71949) | **correct_all** | 300 | 0.5954 |

**선별 개념이 C만 다른 이유(명시적 한계)**: base 모델을 71949 전체 3,000행에 직접
돌려본 결과 정답 2,125건 중 불안정(형식 통제나 보기 순서 변경에서 실패)한 것은
255건(12.0%)뿐이었다. 위치 균형을 맞추면 최대 132행이라 300행을 만들 수 없어,
C만 정답 문항 전체(correct_all)에서 뽑았다. K는 22.4%, R은 77.8%가 불안정해
correct_unstable로 300행을 구성할 수 있었다.

세 LoRA 모두 정답 위치 균형(`①`/`②`/`③`/`④` 각 75행)과 학습 조건을 동일하게 맞춰
TIES가 전제하는 "delta 크기 유사" 조건을 유지했다.

## Training (3개 LoRA 공통)

- Rows: 각 300 / Epochs: 1 / LR `5e-5` (cosine, warmup 3%) / BF16
- LoRA rank / alpha / dropout: 16 / 32 / 0.05
- Target modules: `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`
- Objective: assistant-token causal LM cross entropy
- 조건은 `plan/LoRA_공통_학습조건.md` §1 고정값이며 세 LoRA가 완전히 동일

## Merge safety

- NaN/Inf sweep: 291개 파라미터 전수 통과
- 단일 GPU 고정 병합(멀티 GPU `device_map="auto"` 병합은 과거 NaN 사고 전례로 금지)
- 생성 smoke test: 빈 출력 0건, 지시문 포함 조건에서 정상 응답 확인

## Known limitations

- 300행은 optimizer step이 19개뿐이라 개입 강도가 3,000행 버전(188 step)보다 훨씬 약하다.
- 같은 데이터·개념의 단일 축 3,000행 모델들은 실제 K-AI에서 base(0.4230) 대비
  하락했다(correct_all 0.3906, correct_unstable 0.4026). 이 병합본이 그 하락을
  줄이거나 뒤집는지는 실제 리더보드 결과로만 확인할 수 있다.
- C축은 선별 개념이 다르므로, 병합 결과를 축별로 귀속할 때 이 차이를 감안해야 한다.
