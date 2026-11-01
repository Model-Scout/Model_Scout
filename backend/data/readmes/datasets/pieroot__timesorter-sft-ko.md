---
language: [ko]
license: apache-2.0
task_categories: [text-generation]
tags: [scheduling, prioritization, korean, sft, incremental, timesorter]
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
- config_name: v4
  data_files:
  - split: train
    path: data/v4.parquet
- config_name: v5
  data_files:
  - split: train
    path: data/v5.parquet
- config_name: v6
  default: true
  data_files:
  - split: train
    path: data/v6.parquet
- config_name: v7
  data_files:
  - split: train
    path: data/v7.parquet
- config_name: v8
  data_files:
  - split: train
    path: data/v8.parquet
---

# TimeSorter — 한국어 일정 우선순위 SFT 데이터셋 (버전별 증분)

할 일 목록을 4축(긴급도·중요도·의존성·시간 제약, 각 1-5)으로 채점하는 지도학습용 데이터. 각 버전은 그 버전에서 **새로 생성된 증분**만 포함.

> **버저닝 규칙**: `v1`~`v5`는 각 버전에서 새로 생성된 **증분 데이터만** 포함(누적 아님) —
> `vN` 모델 학습 = `v1`..`vN` 증분 누적. **`v6`은 v2~v5 전체를 검수·통합한 자립형(self-contained)
> 데이터셋**으로, 증분 누적 없이 **`v6` 단독으로 학습 가능**(기본 config).
> v6의 v2 구간은 opus 하위 에이전트로 전수 검수·수정했다.
> SFT 데이터: [pieroot/timesorter-sft-ko](https://huggingface.co/datasets/pieroot/timesorter-sft-ko) ·
> DPO 데이터: [pieroot/timesorter-dpo-ko](https://huggingface.co/datasets/pieroot/timesorter-dpo-ko)

## 버전별 증분

| 버전 | 행 수 | 제목 | 증분 목적 |
|------|------|------|----------|
| `v1` | 5,999 | 자유 텍스트 우선순위 | events-scheduling(영문)→한국어 할 일 번역 + Nemotron 페르소나 주입. '1) 할일 - 이유' 자유 텍스트 출력의 기본 셋. |
| `v2` | 10,958 | 4축 점수 JSON | v1 내용을 4축(긴급/중요/의존/시간) 점수 JSON으로 재생성. 구조화·앱 연동·설명가능성 확보. refusal·orca·xlam 혼합 포함. |
| `v3` | 1,978 | 골격 기반 + 오늘 날짜 주입 | 시나리오 골격(skeleton) 우선 생성 + 오늘 날짜·지난 일정 규칙 추가. 골격 검증(verify_chosen) 통과분만 수록, meta 보존. |
| `v4` | 989 | 이중 생성 경로 + 신규 시나리오 3종 | OpenAI(gpt-5.4)·Claude(Sonnet 4.6/Opus 4.8) 이중 생성으로 표현 다양화. past_split·no_today·am_escalation 신규 시나리오 추가. |
| `v5` | 389 | 의존성 체인 보강 | 잔여 약점(체인)을 타깃해 Claude가 4-5단계 긴 의존성 체인 시나리오 증량 생성. |
| `v6` | 14,314 | 통합·검수 자립형 데이터셋 | v2~v5 전체를 단일셋으로 통합. v2(10,958)는 opus 하위에이전트로 전수 검수·수정(priority_order↔점수 정합 1,188건 수정), v3-v5(3,356)는 verify_chosen 자동검증 통과분. 증분 누적 없이 v6 단독 학습 가능. |
| `v7` | 968 | 의존성 체인 보강 증분 | v6의 잔여 약점 dependency_chain_complex(4B 47%/9B 57%) 타깃 SFT 증분. 4-5단계 체인·다중~24% 비중 확대. build_skeleton→Sonnet4.6/Haiku4.5 생성→verify_chosen→Opus 블라인드 검수(50행/배치) 파이프라인. |
| `v8` | 421 | 체인 추가 보강 증분 | v7에 이어 dependency_chain_complex 추가 보강. v7과 동일 파이프라인(골격→생성→verify_chosen→Opus 검수). 태스크 집합 중복 제거(v7 대비 dedup). |

- 컬럼: `prompt` / `chosen`(정답 JSON, v1은 자유텍스트) / `persona` / `today`(오늘 날짜, ""=미상) / `source` / `meta`(골격, v3+) / `version`
- 각 config는 단일 버전 증분. 전체를 보려면 모든 config를 로드해 concat.

## 버전별 특징·증분 목적

### v1 — 자유 텍스트 우선순위 (5,999행)

- **증분 목적**: events-scheduling(영문)→한국어 할 일 번역 + Nemotron 페르소나 주입. '1) 할일 - 이유' 자유 텍스트 출력의 기본 셋.
- **특징**: 앱 파싱 불가(자유 텍스트), 페르소나 말투 반영
### v2 — 4축 점수 JSON (10,958행)

- **증분 목적**: v1 내용을 4축(긴급/중요/의존/시간) 점수 JSON으로 재생성. 구조화·앱 연동·설명가능성 확보. refusal·orca·xlam 혼합 포함.
- **특징**: JSON 스키마 도입, 날짜 개념 없음(지난 일정 미구분)
### v3 — 골격 기반 + 오늘 날짜 주입 (1,978행)

- **증분 목적**: 시나리오 골격(skeleton) 우선 생성 + 오늘 날짜·지난 일정 규칙 추가. 골격 검증(verify_chosen) 통과분만 수록, meta 보존.
- **특징**: 날짜 추론·지난 일정 강등, dated/intraday/chain/risk/relative 5종
### v4 — 이중 생성 경로 + 신규 시나리오 3종 (989행)

- **증분 목적**: OpenAI(gpt-5.4)·Claude(Sonnet 4.6/Opus 4.8) 이중 생성으로 표현 다양화. past_split·no_today·am_escalation 신규 시나리오 추가.
- **특징**: 이중 경로 품질 수렴, persona_fit 4.9-5.0 큐레이션
### v5 — 의존성 체인 보강 (389행)

- **증분 목적**: 잔여 약점(체인)을 타깃해 Claude가 4-5단계 긴 의존성 체인 시나리오 증량 생성.
- **특징**: dependency_chain·past_split 비중 확대
### v6 — 통합·검수 자립형 데이터셋 (14,314행)

- **증분 목적**: v2~v5 전체를 단일셋으로 통합. v2(10,958)는 opus 하위에이전트로 전수 검수·수정(priority_order↔점수 정합 1,188건 수정), v3-v5(3,356)는 verify_chosen 자동검증 통과분. 증분 누적 없이 v6 단독 학습 가능.
- **특징**: 자립형(v6만으로 SFT 학습), drop 0(최대한 보존), 4축 점수 정합성 검수 완료
### v7 — 의존성 체인 보강 증분 (968행)

- **증분 목적**: v6의 잔여 약점 dependency_chain_complex(4B 47%/9B 57%) 타깃 SFT 증분. 4-5단계 체인·다중~24% 비중 확대. build_skeleton→Sonnet4.6/Haiku4.5 생성→verify_chosen→Opus 블라인드 검수(50행/배치) 파이프라인.
- **특징**: 체인 시나리오 집중, Opus 블라인드 검수 통과분만 수록(~70% 채택률)
### v8 — 체인 추가 보강 증분 (421행)

- **증분 목적**: v7에 이어 dependency_chain_complex 추가 보강. v7과 동일 파이프라인(골격→생성→verify_chosen→Opus 검수). 태스크 집합 중복 제거(v7 대비 dedup).
- **특징**: 체인 다양성 확대, dependency_chain_complex 전용 증분

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
