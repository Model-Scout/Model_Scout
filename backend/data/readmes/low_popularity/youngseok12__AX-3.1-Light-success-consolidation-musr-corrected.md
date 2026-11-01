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

# A.X-3.1-Light Success-Consolidation MuSR (corrected)

이 모델은 `skt/A.X-3.1-Light`에 오답 교정(wrong-correction) LoRA를 병합한 BF16
전체 가중치 모델입니다. base 모델이 자유생성으로 틀렸던 문항에 정답을 힌트로
주고 그 정답을 뒷받침하는 근거를 생성하게 한 뒤(STaR rationalization), 검증을
통과한 것만 정답-우선 형식(`정답 선택지 + 근거`) target으로 재구성해 LoRA
SFT 후 병합했습니다. `correct_all`/`correct_unstable`(같은 71568 데이터, 안정/
불안정 정답 문항 대상)과 대조군 관계입니다. 연구 및 평가용 모델이며, 생성
결과가 부정확할 수 있으므로 고위험 의사결정의 유일한 근거로 사용해서는 안
됩니다.

## Model information

- Model name: `A.X-3.1-Light Success-Consolidation MuSR (corrected)`
- Base model: [`skt/A.X-3.1-Light`](https://huggingface.co/skt/A.X-3.1-Light)
- Base model revision: `9b41bb2406472634d8812c0b8931fa40fa9a6c3a`
- Fine-tuning method: LoRA supervised fine-tuning, merged for inference
- Model format: standalone BF16 `safetensors`; no separate adapter is required
- Intended use: Korean reasoning (MuSR-style multi-step calculation) evaluation and research

## Background

Round1 R-LoRA(MuSR 담당)는 target에 근거 없이 답만 학습시켜 병합 시 다른 축까지
무너뜨리는 문제가 있었다. `correct_all`/`correct_unstable`은 base가 이미 맞히는
문항의 자기 생성 근거를 재사용했지만, 이 모델은 **base가 틀렸던 문항**에
정답을 힌트로 주고 근거를 새로 생성시키는 방식(STaR rationalization)을 썼다.

## Training data

- Source: AI Hub 71568 (경제·스포츠 숫자연산 기계독해, 다단계 계산 문제)
  https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71568
- Selection: base가 틀린 6,011문항에 정답 마커+텍스트를 힌트로 주고 근거 생성
  (`tools/generate_wrong_correction.py`). 아래 필터를 통과한 3,000행만 사용:
  - 문장 반복(퇴화 출력) 제거
  - 토큰 cap(400) 도달로 잘린 생성 제거
  - marker 재도출 검증 OR 정답 텍스트 지지 중 하나 이상 만족(`supported()`)
  - 근거에 원래 오답의 선택지 텍스트가 남아있는 경우 제거(wrong-answer bleed-through)
  - 근거 안에 정답이 아닌 마커를 "정답"으로 선언하는 잔존 표현 제거
- Target: `{정답 선택지} {텍스트}\n근거: {정제된 근거}`, target 중앙값 218자
- **정답 라벨 무결성 직접 검증**: target 첫 마커가 항상 원본 AI Hub `answer_index`와
  일치(3,000/3,000, 불일치 0건) — 근거 품질과 무관하게 라벨 자체는 항상 정답
- Not used for evaluation: `not_for_eval: true`, canonical 평가셋과 분리

## Training

- Rows: 3,000
- Epochs: 1 / Learning rate: `5e-5` (cosine, warmup 3%) / Precision: BF16
- LoRA rank / alpha / dropout: 16 / 32 / 0.05
- LoRA target modules: `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`
- Training loss: `0.2637`
- NaN/Inf sweep on merged weights: pass / 생성 smoke test: pass

## Known limitations

1. **in-sample ablation**: 이 모델이 학습에 사용한 오답 100문항 재현 시 70% 회복.
   그러나 대조군(같은 71568이지만 이 오답 문항을 전혀 학습하지 않은 `correct_all`
   adapter)도 같은 문항에서 65% 회복 — 즉 70%의 대부분(65%p)은 오답 교정과
   무관한 도메인 적응 효과이며, 교정 메커니즘 고유 기여는 약 +5%p(n=100, 노이즈
   수준)로 추정된다.
2. **로컬 진단(n=100/축)에서 correct_all/correct_unstable보다 낮음**(4축 평균
   0.525 vs 0.5375/0.535).
3. `correct_all`/`correct_unstable`의 실제 K-AI 리더보드 결과(각 0.3906/0.4026,
   base 0.4230 대비 모두 하락)를 참고하면 이 모델도 base 대비 개선을 낙관하기
   어렵다. 최종 채택 판단은 실제 리더보드 결과로 확인해야 한다.
