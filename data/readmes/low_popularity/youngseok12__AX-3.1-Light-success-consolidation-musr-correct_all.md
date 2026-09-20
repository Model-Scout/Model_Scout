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

# A.X-3.1-Light Success-Consolidation MuSR (correct_all)

이 모델은 `skt/A.X-3.1-Light`에 success-consolidation LoRA를 병합한 BF16
전체 가중치 모델입니다. base 모델이 스스로 안정적으로 정답을 맞히는 문항의
자기 생성 추론 과정을 근거 포함 target으로 재구성해 학습했습니다(STaR류
self-distillation). 연구 및 평가용 모델이며, 생성 결과가 부정확할 수 있으므로
고위험 의사결정의 유일한 근거로 사용해서는 안 됩니다.

## Model information

- Model name: `A.X-3.1-Light Success-Consolidation MuSR (correct_all)`
- Base model: [`skt/A.X-3.1-Light`](https://huggingface.co/skt/A.X-3.1-Light)
- Base model revision: `9b41bb2406472634d8812c0b8931fa40fa9a6c3a`
- Fine-tuning method: LoRA supervised fine-tuning, merged for inference
- Model format: standalone BF16 `safetensors`; no separate adapter is required
- Intended use: Korean reasoning (MuSR-style multi-step calculation) evaluation and research

## Background

이전 라운드(specialist LoRA Round 1)의 추론(MuSR) 담당 어댑터는 target에
근거 없이 답만 학습(중앙값 8자)시켜, 병합 시 다른 축(CLIcK 등)까지 함께
무너뜨리는 문제가 있었습니다. 이 모델은 같은 원천 데이터를 base 모델이
직접 풀게 한 뒤, 안정적으로 맞힌 문항의 자기 생성 근거를 그대로 target으로
사용해 이 문제를 피하도록 재구성한 실험입니다.

## Training data

- Source: AI Hub 71568 (경제·스포츠 숫자연산 기계독해, 다단계 계산 문제)
  https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71568
- Selection: base 모델이 원천 3,000행을 자유생성(A)/형식통제(B1)/보기순서흔들기(C)
  세 조건으로 직접 풀어 라벨링. 이 arm(`correct_all`)은 세 조건 모두에서
  안정적으로 정답을 맞힌 3,000행을 사용
- Target: base가 직접 생성한 근거를 정답-우선(answer-first) 형식으로 정리
  (`③ 정답\n근거: ...`), target 중앙값 214자 — 답만 있는 target이 아님
- Not used for evaluation: 이 데이터는 학습 풀에서만 추출했고, canonical 평가셋과
  분리되어 있습니다(`not_for_eval: true`)

## Training

- Rows: 3,000
- Epochs: 1
- Learning rate: `5e-5` (cosine, warmup 3%)
- Precision: BF16
- LoRA rank / alpha / dropout: 16 / 32 / 0.05
- LoRA target modules: `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`
- Effective batch size: 16
- Objective: assistant-token causal language-model cross entropy
- Training loss: `0.2487`
- NaN/Inf sweep on merged weights: pass

## Known limitations (from local diagnosis)

축당 100문항 로컬 진단(canonical benchmark_eval suite, 병합 없이 adapter 직결 측정
후 동일 조건으로 재확인)에서 겨냥한 MuSR 축은 base 대비 거의 변화가 없었고
(A_acc 0.476→0.480), CLIcK은 하락(0.664→0.620)했습니다. 이 로컬 프로브는
과거 실제 K-AI 리더보드에서 크게 다른 결과를 낸 모델들을 구별하지 못한 전례가
있어([jwg/specialist_r1_kai_click_zero_diagnosis_2026-09-04.md]), 실제 성능은
공식 리더보드 결과로 확인해야 합니다.
