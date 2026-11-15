---
license: apache-2.0
language:
- ko
library_name: transformers
base_model: blackmallangcow/nari-decision-4b
tags:
- decision-model
- classification
- router
- korean
---

# nari-router-4b

`blackmallangcow/nari-decision-4b`(v3.2, 커밋 `029c4628a38859dce5b0db1742e9c97545aabe12`)를 교실 과학 실험 로봇(OpenArm SciEdu)의 한국어 말 라우터로 미세조정한 모델이다.
받아쓴 학생·선생님 말과 그때의 상황 칸을 열한 갈래(pause, stop, proceed, retry, start_switch, leaf_side, hands, question, answer, chitchat, unclear) 가운데 하나로 가른다.
바탕 모델의 원격 코드(`modeling_sysone.py`)를 그대로 쓰고 `model.decide()`로 부른다. LoRA는 bf16 가중치에 합쳤다.

- 학습: 백본 모든 선형 층 LoRA(계수 16, alpha 32.0) + 결정 헤드, 헤드는 로그 손실 + Brier, 글자 답은 교차 엔트로피, 보기 순서를 줄마다 섞음,
  학습률 0.0002, 에포크 2, 배치 8, 씨앗 2, 멈춤·그만 가중 2.0.
- 읽기: 결정 헤드와 글자 답의 로그 확률을 `lm_weight` 0.0로 섞는다. 보정 온도 `choice:6+` = 1.45(합친 판의 검증 + 개발 확률로 다시 맞춤).
- 입력: state는 `교실 과학 실험 로봇 곁에서 들린 한국어 말을 받아쓴 글과 그때의 상황이다. '||' 앞은 상황 칸, 뒤는 그 말이다.` 뒤에 `장면=… | 실험=… | 나뭇잎 활동=… | AI 제안=… | 말한 사람=… || <말>` 한 줄, 질문은 `utterance_kind` 하나(choice, 보기는 학습한 글 그대로).
  보기 글과 지시문은 저장소 `dialogue/routing/nari_route.py`의 `short_stop` 판이다. 다른 글로 물으면 학습한 분포에서 벗어난다.
- 말은 실기 받아쓰기 꼴로 맞춰 읽는다(`nari_route.stt_form`: `...` · `…` · `!` · `~`를 지우고, 세 글자 이하인 말은 부호를 모두 지운다). 학습 · 검증 · 서빙이 같은 함수를 쓴다.
- 자료와 측정: 비공개 저장소의 학습 자료로 학습했고 자료는 올리지 않는다. 숫자는 저장소 `docs/measurements/routing.md` 12~15절.


