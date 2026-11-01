---
language: [ko]
license: apache-2.0
task_categories: [text-generation]
tags: [scheduling, prioritization, korean, dpo, incremental, timesorter]
configs:
- config_name: v1
  data_files:
  - split: train
    path: data/v1.parquet
- config_name: v2
  data_files:
  - split: train
    path: data/v2.parquet
- config_name: v3
  data_files:
  - split: train
    path: data/v3.parquet
- config_name: v5
  data_files:
  - split: train
    path: data/v5.parquet
- config_name: v6
  default: true
  data_files:
  - split: train
    path: data/v6.parquet
- config_name: v8
  data_files:
  - split: train
    path: data/v8.parquet
---

# TimeSorter — 한국어 일정 우선순위 DPO 데이터셋 (버전별 증분)

선호 학습(chosen vs rejected)용 데이터. 각 버전은 그 버전 **증분 선호쌍**만 포함. v3+는 형식 동일·내용만 오류인 hard negative.

> **버저닝 규칙**: `v1`~`v5`는 각 버전에서 새로 생성된 **증분 데이터만** 포함(누적 아님) —
> `vN` 모델 학습 = `v1`..`vN` 증분 누적. **`v6`은 v2~v5 전체를 검수·통합한 자립형(self-contained)
> 데이터셋**으로, 증분 누적 없이 **`v6` 단독으로 학습 가능**(기본 config).
> v6의 v2 구간은 opus 하위 에이전트로 전수 검수·수정했다.
> SFT 데이터: [pieroot/timesorter-sft-ko](https://huggingface.co/datasets/pieroot/timesorter-sft-ko) ·
> DPO 데이터: [pieroot/timesorter-dpo-ko](https://huggingface.co/datasets/pieroot/timesorter-dpo-ko)

## 버전별 증분

| 버전 | 행 수 | 제목 | 증분 목적 |
|------|------|------|----------|
| `v1` | 1,469 | 초기 선호쌍 | v1 우선순위 출력의 선호/비선호 쌍. |
| `v2` | 15,338 | 4축 JSON 선호쌍 + refusal | v2 JSON 포맷 선호쌍 + 비일정 입력 거절(refusal) 쌍 대량 추가. |
| `v3` | 2,222 | hard negative 5종 | 형식은 chosen과 동일하고 내용 한 곳만 틀린 hard negative 도입 (date_confusion/granularity_swap/dependency_scatter/risk_ignore/order_score_mismatch). v2_replay는 v2 재사용이므로 증분에서 제외. |
| `v5` | 351 | on-policy 선호쌍 | SFT v4 모델이 실제로 생성한 오답을 rejected로 수집(on-policy). 체인·dated 오류 집중. |
| `v6` | 17,894 | 통합·검수 자립형 선호셋 | v2(15,321)+v3 hard-neg+v5 on-policy 통합. v2는 opus 전수 검수(chosen 정답성·rejected valid-but-worse 4,732건 수정). chosen 전부 유효 JSON, 동일쌍 0. |
| `v8` | 1,231 | 체인 hard-negative 3종 선호쌍 | SFT v8 chain 증분(421행)의 의존성 체인 오류 3종(dependency_scatter/chain_internal_swap/chain_break_mid) hard-negative 선호쌍. 체인 약점 DPO 타깃. v7은 SFT-only(체인은 DPO로 잘 안 옮김 실증). |

- 컬럼: `prompt` / `chosen` / `rejected` / `persona` / `today` / `category`(위반유형) / `source` / `version`
- 각 config는 단일 버전 증분. 전체를 보려면 모든 config를 로드해 concat.

## 버전별 특징·증분 목적

### v1 — 초기 선호쌍 (1,469행)

- **증분 목적**: v1 우선순위 출력의 선호/비선호 쌍.
- **특징**: 자유 텍스트 기반 (v3+ 학습 비권장)
### v2 — 4축 JSON 선호쌍 + refusal (15,338행)

- **증분 목적**: v2 JSON 포맷 선호쌍 + 비일정 입력 거절(refusal) 쌍 대량 추가.
- **특징**: 형식 negative 위주(길이 편향 주의), refusal 도메인 30종
### v3 — hard negative 5종 (2,222행)

- **증분 목적**: 형식은 chosen과 동일하고 내용 한 곳만 틀린 hard negative 도입 (date_confusion/granularity_swap/dependency_scatter/risk_ignore/order_score_mismatch). v2_replay는 v2 재사용이므로 증분에서 제외.
- **특징**: 내용 오류 negative — 실제 실패 모드 벌점
### v5 — on-policy 선호쌍 (351행)

- **증분 목적**: SFT v4 모델이 실제로 생성한 오답을 rejected로 수집(on-policy). 체인·dated 오류 집중.
- **특징**: 모델 실제 오류 기반 — 학습 밀도 최고
### v6 — 통합·검수 자립형 선호셋 (17,894행)

- **증분 목적**: v2(15,321)+v3 hard-neg+v5 on-policy 통합. v2는 opus 전수 검수(chosen 정답성·rejected valid-but-worse 4,732건 수정). chosen 전부 유효 JSON, 동일쌍 0.
- **특징**: 자립형 DPO셋, rejected 중 2,821건은 malformed JSON 유지(잘못된 출력 회피를 가르치는 정당한 negative)
### v8 — 체인 hard-negative 3종 선호쌍 (1,231행)

- **증분 목적**: SFT v8 chain 증분(421행)의 의존성 체인 오류 3종(dependency_scatter/chain_internal_swap/chain_break_mid) hard-negative 선호쌍. 체인 약점 DPO 타깃. v7은 SFT-only(체인은 DPO로 잘 안 옮김 실증).
- **특징**: 체인 전용 hard-negative — scatter(421)/swap(421)/break_mid(389), reject_category 기반 위반유형 분류

## 생성 방법 — 시나리오 골격 우선 (v3+)

1. 프로그램이 골격 확정: 태스크별 마감 일시·지난 여부·의존 체인·리스크 문구
2. LLM은 텍스트·정답만 생성 (텍스트 gpt-5.4-mini, 정답 gpt-5.4 / Claude Sonnet 4.6)
3. 골격 규칙 자동 검증(verify_chosen) 통과분만 수록 — meta 컬럼에 골격 보존

## 학습 결과 (Qwen3.5-4B, held-out n=30 골격 자동 채점)

| 단계 | 통과율 |
|------|-------|
| 어댑터 없음 | 0.0% (스키마 미준수) |
| + SFT (v1~v4 누적) | 90.0% |
| + DPO (v5) | 90.0% |

학습 코드·모델: https://github.com/jung-geun/TimeSorter
