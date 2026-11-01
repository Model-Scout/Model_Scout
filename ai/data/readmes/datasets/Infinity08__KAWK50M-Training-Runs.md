---
language:
- ko
license: other
tags:
- korean
- language-modeling
- kawk50m
---

# KAWK50M Training Runs Archive

최종·중간·실패 실험 체크포인트를 포함한 전체 학습 이력입니다.

최종 배포 모델은 별도 저장소 `KAWK-1.5-50M-Korean-Base`, `KAWK-1.5-50M-Korean-Base-5K`, `KAWK-1.5-50M-Korean-Instruct`에 있습니다. 이 저장소는 실험 재현과 진단을 위한 전체 아카이브이므로 모든 체크포인트가 좋은 품질이거나 정상 학습 결과인 것은 아닙니다.

각 체크포인트의 `model/`과 `tokenizer/`는 Transformers 형식입니다. `trainer_state.pt`는 optimizer, scheduler와 RNG 상태를 담은 PyTorch pickle 파일이므로 신뢰할 수 있는 출처에서만 로드하십시오.

이 저장소는 KAWK50M 프로젝트의 공개 학습 이력 아카이브입니다. 자료를 사용할 때는 원천 데이터 라이선스, 개인정보, 중복 파일 및 실패 실험 산출물에 대한 안내를 확인하십시오.
