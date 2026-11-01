---
base_model: kakaocorp/kanana-1.5-15.7b-a3b-instruct
library_name: transformers
language:
- ko
license: other
tags:
- lora-merged
- korean
- k-ai-leaderboard
- moe
---

# Kanana-1.5-15.7B-A3B-Instruct-sft_v0_2 (동전)

kakaocorp/kanana-1.5-15.7b-a3b-instruct(Mixtral 기반 MoE)를 기반으로, AI Hub 한국어 데이터를
활용해 K-AI 리더보드 5개 벤치마크(KMMLU-Pro / CLIcK / HLE(Ko) / MuSR(Ko) / Com2-main(Ko))
전체 대응 proxy benchmark에서 진단한 출력 형식 결손을 교정하기 위해 LoRA 파인튜닝 후 병합한
모델입니다. AX-3.1-Light-sft_v0_2, EXAONE-Deep-7.8B-sft_v0_2와 동일한 학습 데이터
(`format_sft_v0_2.jsonl`)를 사용했습니다.

- **베이스 모델**: `kakaocorp/kanana-1.5-15.7b-a3b-instruct` (Mixtral 아키텍처, MoE)
- **AI Hub 데이터 활용**: 예
  - `71857` 국어 교과 지문형 문제 데이터 (CLIcK 축)
  - `71874` 전문 의학지식 데이터 (KMMLU 축)
  - `71610` 금융, 법률 문서 기계독해 데이터 (HLE 축)
  - `569` 행정 문서 대상 기계독해 데이터 (MuSR 축)
  - `71949` 인과관계 기반 추론 데이터(업사이클링) (Com2-main 축)
- **주요 학습 방법**: proxy benchmark 5축 1,350문항 기반 실패 진단 결과를 반영한 LoRA SFT
  (r=16, alpha=32, attention 모듈만 타겟(q/k/v/o_proj) — MoE 구조라 expert MLP는 제외, 2 epoch)
- **모델의 목적**: 5개 벤치마크 축 전반의 출력 형식 안정화
- **구조 변경**: 없음 (LoRA adapter를 base model에 병합한 표준 Mixtral 아키텍처, custom code
  없음 — vLLM에서 옵션 없이 바로 로드 검증 완료)

## 자체 Proxy 벤치마크 결과 (참고용, K-AI 공식 점수 아님)

5축 1,350문항 (KMMLU-Lite 300 / CLIcK-Lite 300 / HLE-Lite 200 / MuSR-Lite 300 /
Com2-main-Lite 250) 기준, 베이스 대비:

| Axis | Base 안정정답 | sft_v0_2 안정정답 |
|---|---:|---:|
| KMMLU-Lite | 213/300 | 216/300 |
| CLIcK-Lite | 268/300 | 275/300 |
| HLE-Lite | 181/200 | 190/200 |
| MuSR-Lite | 278/300 | 282/300 |
| **Com2-main-Lite** | 197/250 | **245/250** |
| **합계** | **1,137/1,350 (84.3%)** | **1,208/1,350 (89.5%)** |

> Com2-main-Lite 축에서 가장 큰 폭으로 개선됨(197→245). 참고: 이 축의 자체 proxy 오답 선택지는
> 같은 추론 유형 내 다른 문항의 정답 텍스트를 교차 샘플링해 합성한 것으로(원본 AI Hub 벤치마크의
> 실제 선택지는 이미지 기반), 네이티브 4지선다가 아닙니다. 절대 정확도 수치는 참고용으로만 해석할 것.

## 사용 데이터셋 명시

AI Hub: 71857/71874/71610/569/71949의 validation label 중 최종 proxy 벤치마크로 표본 추출되지
않은 문서-안전(document-safe) 잔여분만 학습에 사용함.
