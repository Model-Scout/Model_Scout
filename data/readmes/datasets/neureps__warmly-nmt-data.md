---
license: apache-2.0
language:
- en
- ko
task_categories:
- translation
tags:
- synthetic
- nmt
- korean
- warmly
---

# warmly-nmt-data — EN→KO 번역 학습·평가 데이터 (버전별 폴더)

[Warmly(온기)](https://github.com/neureps/warmly) B안 트랙("0.8B 영어 댓글 생성 + 소형 번역기")의 학습·평가 데이터셋. **버전 폴더로 관리**하며 각 폴더의 `README.md`에 파일별 설명·생성 방법이 문서화되어 있습니다.

| 폴더 | 날짜 | 내용 | 산출 모델 |
| --- | --- | --- | --- |
| `v1/` | 2026-07-14 | 파일럿 — 2B 교사, 883쌍, 페르소나 제어토큰 | [warmly-nmt-small100-enko](https://huggingface.co/neureps/warmly-nmt-small100-enko), [warmly-nmt-kobart-enko](https://huggingface.co/neureps/warmly-nmt-kobart-enko) |
| `v2/` | 2026-07-15 | 8B 교사, 1,410쌍, 평이 번역+런타임 이모지 래퍼 | [warmly-nmt-nllb600-enko](https://huggingface.co/neureps/warmly-nmt-nllb600-enko) |
| `eval/` | 2026-07-14 | 공용 평가셋 — testset40(+8B 참조·NLLB-ft 출력), 제로샷 선발전 bakeoff 전문 | (버전 무관 공용) |

전부 합성 데이터(Qwen 계열 모델 출력 = Apache-2.0). 실사용자 사진·개인정보 없음.
