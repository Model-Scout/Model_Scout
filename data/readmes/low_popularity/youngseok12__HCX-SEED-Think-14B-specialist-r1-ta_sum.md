---
license: other
license_name: hyperclovax-seed
license_link: LICENSE
base_model: naver-hyperclovax/HyperCLOVAX-SEED-Think-14B
language:
- ko
library_name: transformers
pipeline_tag: text-generation
tags:
- korean
- text-generation
- lora
- model-merging
- task-arithmetic
- answer-first
---

# HyperCLOVAX-SEED-Think-14B — Specialist LoRA Merge (`ta_sum`)

세 개의 축별 specialist LoRA(K/R/C)를 각각 따로 학습한 뒤 **Task Arithmetic (linear)**로 병합한
BF16 전체 가중치 모델입니다. 별도 adapter가 필요하지 않습니다.

연구·평가용 모델입니다. 생성 결과가 부정확할 수 있으므로 의료·법률·재정 등
고위험 의사결정의 유일한 근거로 사용해서는 안 됩니다.

## Model information

- Base model: [`naver-hyperclovax/HyperCLOVAX-SEED-Think-14B`](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-14B)
- Base revision: `9b74e35d4c7e4ffec489f4171273caca8948a2b9`
- Merge method: **Task Arithmetic (linear)** — K + R + C, weights 1.0 / 1.0 / 1.0
- Format: standalone BF16 `safetensors`
- Chat template: base 원본 그대로 (수정하지 않음)

## Specialist LoRAs

각 LoRA는 담당 축의 데이터만 3,000행 학습했고, 학습 조건은 세 개가 완전히 동일합니다
(유일한 변수는 데이터). 전 축 **4지선다 ①②③④ + answer-first 한 줄 타깃** 스키마.

| LoRA | Target axis | Dataset | Source |
|---|---|---|---|
| K-LoRA | KMMLU-Pro | AI Hub 71875 필수의료 의학지식 | [link](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71875) |
| R-LoRA | MuSR(Ko) | AI Hub 71568 숫자연산 기계독해 | [link](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71568) |
| C-LoRA | Com2-main(Ko) | AI Hub 71949 인과관계 기반 추론 | [link](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71949) |

- Train loss: K 0.0583 / R 0.0710 / C 0.0171
- Held-out format probe (240 canonical public-benchmark items, greedy): answer stated in 100.0% of outputs, mean 20 output tokens

### 전처리

- 5지선다 → **4지선다 변환** (공식 벤치마크가 4지선다)
- **정답 위치 균등화** — 세 LoRA 모두 ①②③④ 각 750개
- 71568: `calculation` 수식이 있는 정답만 사용, 오답을 수식 변형으로 생성(검증 가능)
- 71949: 원본이 이미지 기반 MCQ이므로 텍스트 인과 CoT를 시드로 4지선다 합성,
  이미지를 지칭하는 항목은 전량 제외

## Training configuration (three LoRAs identical)

| | |
|---|---|
| Method | LoRA, merged for inference |
| Rank / alpha / dropout | 16 / 32 / 0.05 |
| Target modules | `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj` |
| Learning rate | `5e-5`, cosine, warmup ratio 0.03 |
| Epochs | 1 |
| Effective batch | 16 |
| Max sequence length | 4,096 |
| Precision | BF16 |
| Seed | 42 |
| Objective | assistant-token-only causal LM cross entropy |

## Notes

- 공개 벤치마크 test set을 직접 학습하지 않았습니다.
- 병합은 단일 GPU에서 수행했고, 전 파라미터 NaN/Inf 검사를 통과했습니다.
