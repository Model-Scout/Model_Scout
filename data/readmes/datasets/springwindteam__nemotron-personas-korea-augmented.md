---
license: cc-by-4.0
language:
  - ko
task_categories:
  - text-generation
tags:
  - synthetic
  - personas
  - korean
  - simulation
  - social-simulation
  - policy
size_categories:
  - 1M<n<10M
configs:
  - config_name: default
    data_files:
      - split: train
        path: data/personas_augmented_1m.parquet
---

# Nemotron-Personas-Korea — Augmented for Korean Policy Simulation


**한국 정책·여론 시뮬레이션을 위해 증강한 한국인 합성 페르소나 1,000,000명** —
NVIDIA [Nemotron-Personas-Korea](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Korea)(CC BY 4.0)의 파생(augmented) 데이터셋입니다.

> ⚠️ 본 데이터는 **완전 합성(fully synthetic)** 입니다. 실제 개인이 아니며 개인정보를 포함하지 않습니다.

![Dataset overview](assets/overview.png)

## 왜 증강했나 (Motivation)

NVIDIA Nemotron-Personas-Korea는 한국 인구 구조를 반영한 **대규모(100만) 고품질 합성 페르소나**로,
인구통계·직업·성격·서사를 두루 갖춘 훌륭한 범용 기반입니다. 본 데이터셋은 그 위에서 출발했습니다.

다만 저희의 용도는 **정책·여론 시뮬레이션**이라는 특수한 도메인이었고, 범용 페르소나가 목표하지 않았던
몇 가지가 추가로 필요했습니다:

- **여론 분석 축**: 소득 수준·의견 성향처럼 세그먼트별 여론을 다루는 데 필요한 속성 (공개 통계 분포에 접지해 부여)
- **표집 가능한 구조화 컬럼**: 서사 속에 자연어로 담겨 있던 정보(자녀·교육 종사 등)를 필터·층화표집에 쓸 수 있는 정형 컬럼으로 추출
- **소수 세그먼트 보강**: 다문화 가구·재학생처럼 실측 조사와 대조할 때 필요한 집단을 정부 통계 분포에 맞게 보강
- **시뮬레이션 투입용 서사 요약**: 에이전트 프롬프트에 넣기 좋은 압축 서사

즉, 이 작업은 원본의 부족함을 지적하는 것이 아니라 **범용 기반을 특정 도메인(한국 정책·여론 시뮬레이션)에
맞게 확장한 것**이며, 같은 방식의 확장이 다른 도메인(소비·HR·공중보건 등)에도 재사용될 수 있도록 공개합니다.

## 원본 대비 추가·변경 사항 (What's new)

**1. 통계 접지 속성 (신규 부여)**
- `income_rank`(소득순위) · `political_orientation`(정치성향) · `political_interest`(정치관심도) + 각 확률값(`*_prob`)
- 통계청·KGSS·갤럽 공개 분포에 맞춰 확률적으로 배정한 합성값

**2. 관측 파생 컬럼 (원본 속성에서 규칙 추출)**
- `has_children`(자녀 유무) · `is_education_worker`(교육 종사) · `activity_status`(경제활동 상태)
- 가구형태·직업 등 원본 필드에서 결정론 규칙으로 파생 — 재현 가능

**3. 다문화 가구 (17,803명 배정)**
- `mc_household` · `mc_member_role` · `mc_origin_country` · `mc_first_language` · `mc_household_languages` · `mc_korean_proficiency`
- 다문화가족 실태조사·인구총조사 분포 기반 배정 + 해당 인물 서사 재작성

**4. 학생 표본 보정**
- 19–29세 비취업 중 재학생 비중을 실측(청년층 부가조사)에 맞게 보정
- 규칙 선정(결정론) + 서사 재서술, 구조 필드(연령·성별·지역 등)는 불변

**5. 서사 요약 (`story_summary`)**
- 1인칭 ~100자 요약 — LLM 재작성(원문에 없는 정보 추가 금지 제약)

**6. 작업 계보 (`seed_version`)**
- 증강 작업 버전 태그 — 재현·추적용

## 데이터 구성 (Dataset Composition)

- **1,000,000 rows × 44 columns** — 각 행 = 합성 시민 1명 (`uuid` 고유키)
- Parquet(zstd) 단일 파일, 리스트형 필드는 JSON 문자열로 평탄화
- **원본 26개 필드**(인구통계·페르소나 서사·역량·관심)는 그대로 유지 — 구성은
  [원본 데이터셋 카드](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Korea) 참조
  (원본의 임베딩 컬럼은 용량 문제로 제외)

**본 데이터셋이 추가한 필드 (18개)**

| 분류 | 필드 |
|---|---|
| 의견·경제 (통계 접지) | `income_rank`, `political_orientation`, `political_interest` + `income_rank_prob`, `political_orientation_prob`, `political_interest_prob` |
| 관측 파생 (규칙 추출) | `has_children`, `is_education_worker`, `activity_status`, `activity_status_source` |
| 다문화 | `mc_household`, `mc_member_role`, `mc_origin_country`, `mc_first_language`, `mc_household_languages`, `mc_korean_proficiency` |
| 서사 요약 | `story_summary` |
| 작업 계보 | `seed_version` |

**값 라벨**: 위 필드의 값은 한국어 라벨입니다 — `income_rank`: 상위/중위/하위 · `political_orientation`: 보수/중도/진보 · `political_interest`: 높음/보통/낮음.

## 증강 근거 통계 (Augmentation Seed Sources)

| 속성 | 근거 |
|---|---|
| 소득순위 | 통계청 가계금융복지조사 분포 |
| 정치성향·정치관심도 | KGSS(한국종합사회조사)·한국갤럽 공개 분포 |
| 다문화 가구 | 여성가족부 다문화가족 실태조사 · 통계청 인구총조사 |
| 학생 표본 보정 | 통계청 경제활동인구조사 청년층 부가조사 |

## 사용 방법 (Quick Start)

```python
from datasets import load_dataset

ds = load_dataset("springwindteam/nemotron-personas-korea-augmented", split="train")
print(ds[0]["story_summary"])

# 예: 다문화 가구만 필터
mc = ds.filter(lambda r: r["mc_household"])
```

## 활용 예 (Intended Use)

- 정책·여론 멀티에이전트 시뮬레이션의 합성 시민 표본 (제작 목적)
- 한국어 페르소나 기반 생성·대화 모델 학습/평가
- 세그먼트별 합성 설문·시장 반응 실험 (소비·HR·공중보건 등)

## 한계 및 주의 (Limitations & Ethical Considerations)

- `political_orientation`·`income_rank` 등 의견·경제 속성은 **공개 통계 분포에 맞춘 합성값**입니다.
  개별 인물의 "실제" 성향이 아니라 **인구 수준 분포 재현**이 목적이며, 속성 간 독립 배정 가정이 있습니다.
- 서사는 합성 창작물이며, `story_summary`는 LLM 재작성분(원문 근거 요약)입니다.
- **여론조사 대체재가 아닙니다** — 시뮬레이션·연구용 보조 데이터입니다.
- 특정 개인·집단 타게팅, 선거·여론 조작 목적 사용을 금지합니다.
- 원본 데이터셋의 한계(만 19세 미만 제외 등)를 승계합니다.

## 라이선스 및 저작자 표시 (License & Attribution)

- 원저작물: **NVIDIA Nemotron-Personas-Korea** — [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 본 데이터셋: 위 원저작물의 **수정·증강 파생물**이며 동일하게 **CC BY 4.0**으로 배포합니다.
- 변경 사항: 위 "원본 대비 추가·변경 사항" 참조.

## 인용 (Citation)

본 데이터셋을 사용할 경우, 원본과 본 파생 데이터셋을 함께 표기해 주세요:

> Team Chunpung (2026). *Nemotron-Personas-Korea — Augmented for Korean Policy Simulation.*
> Hugging Face. https://huggingface.co/datasets/springwindteam/nemotron-personas-korea-augmented
>
> Derived from: NVIDIA (2026). *Nemotron-Personas-Korea.*
> https://huggingface.co/datasets/nvidia/Nemotron-Personas-Korea (CC BY 4.0)

## 제작 (Data Developer)

**춘풍팀 (Team Chunpung)** — 한국 교육정책 여론 시뮬레이션 **MINSIM** 프로젝트의 일환으로 제작 · 공개: 2026-07
