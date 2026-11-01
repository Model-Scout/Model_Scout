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
- self-distillation
---

# A.X-3.1-Light Success-Consolidation R-300 (single)

이 모델은 `skt/A.X-3.1-Light`에 R축(MuSR 담당) success-consolidation LoRA를
병합한 BF16 전체 가중치 모델입니다. 같은 개념·같은 데이터로 학습한 3,000행
버전(`AX-3.1-Light-success-consolidation-musr-correct_unstable`)과 **학습 행 수만
300행으로 다른** 규모 대조 모델입니다. 연구 및 평가용이며, 생성 결과가 부정확할
수 있으므로 고위험 의사결정의 유일한 근거로 사용해서는 안 됩니다.

## Model information

- Base model: [`skt/A.X-3.1-Light`](https://huggingface.co/skt/A.X-3.1-Light)
- Base model revision: `9b41bb2406472634d8812c0b8931fa40fa9a6c3a`
- Fine-tuning method: LoRA supervised fine-tuning, merged for inference
- Model format: standalone BF16 `safetensors`; no separate adapter is required

## What this model tests

동일 축·동일 데이터·동일 학습조건에서 **학습 행 수만 3,000 → 300으로 축소**했을 때
부작용(특히 다른 축의 하락)이 줄어드는지를 보는 규모 대조 실험이다.

| | 3,000행 버전 | 이 모델(300행) |
|---|---|---|
| 축 / 원본 데이터 | R(MuSR) / AI Hub 71568 | 동일 |
| 선별 개념 | correct_unstable | 동일 |
| 학습 조건 | `plan/LoRA_공통_학습조건.md` §1 | 동일 |
| 학습 행 수 | 3,000 (188 optimizer steps) | **300 (19 steps)** |
| final train loss | 0.2459 | 0.6066 |

## Training data

- Source: AI Hub 71568 (경제·스포츠 숫자연산 기계독해)
  https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71568
- Selection: base 모델이 자유생성(A)/형식통제(B1)/보기순서변경(C) 세 조건으로 직접
  풀어, **A는 맞히지만 B1·C 중 하나 이상 실패**하는(불안정하게 아는) 문항만 선별
- Target: base가 생성한 근거를 정답-우선 형식으로 정리(`정답 선택지 + 근거`)
- 정답 위치 균형: `①`/`②`/`③`/`④` 각 75행
- Not used for evaluation: `not_for_eval: true`, canonical 평가셋과 분리

## Training

- Rows: 300 / Epochs: 1 / LR `5e-5` (cosine, warmup 3%) / BF16
- LoRA rank / alpha / dropout: 16 / 32 / 0.05
- Target modules: `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`
- Training loss: `0.6066`
- NaN/Inf sweep on merged weights: pass / 생성 smoke test: pass

## Known limitations

300행은 optimizer step이 19개뿐이라 개입 강도가 3,000행 버전보다 훨씬 약하다
(final loss 0.6066 vs 0.2459). 3,000행 버전의 실제 K-AI 결과는 0.4026으로 base
0.4230 대비 하락이었으며, 이 모델이 그 하락을 줄이는지는 실제 리더보드 결과로만
확인할 수 있다.
