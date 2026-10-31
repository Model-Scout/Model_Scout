---
language:
- ko
license: apache-2.0
task_categories:
- text-generation
tags:
- instructional-design
- education
- benchmark
- korean
- isd
- addie
size_categories:
- 10K<n<100K
---

# ISD-Bench-Ko (v2.0)

교수설계(Instructional Systems Design) AI 에이전트 평가용 한국어 벤치마크 데이터셋입니다.

## 📊 데이터셋 개요

| 항목 | 내용 |
|------|------|
| **총 시나리오** | 25,795개 |
| **Train** | 24,593개 (95.3%) |
| **Test** | 1,202개 (4.7%) |
| **언어** | 한국어 |
| **라이선스** | Apache 2.0 |

## 🆕 v2.0 업데이트 내역

- **Train/Test 분리**: 층화 추출(Stratified Sampling)으로 9개 축 분포 유지
- **품질 개선**: 
  - context_variant 논리적 일관성 개선 (#97)
  - difficulty 균형화 (33%:34%:33%) (#99)
  - 전체 데이터 품질 재검증 (#100)
- **폴더 구조 변경**: train/part1~4로 분리 (HF 파일 수 제한 대응)

## 📁 데이터 구조

```
scenarios/
├── train/                    # 학습용 (24,593개)
│   ├── part1/               # 8,000개
│   ├── part2/               # 8,000개
│   ├── part3/               # 8,000개
│   └── part4/               # 593개
├── test/                     # 평가용 (1,202개)
├── idld_aligned/            # IDLD 논문 기반 (8,842개)
├── context_variant/         # Context Matrix 변형 (16,953개)
├── split_metadata.json      # Train/Test 분리 메타데이터
└── source_mapping.json      # 원본 논문 매핑
```

## 🎯 9개 축 분포 (Train/Test)

### 학습 기간 (context.duration)
| 값 | Train | Test |
|---|---|---|
| 장기 과정(1~6개월) | 35.2% | 37.9% |
| 중기 과정(2–4주) | 35.5% | 34.5% |
| 단기 집중 과정(1주 내) | 29.3% | 27.5% |

### 학습 환경 (context.learning_environment)
| 값 | Train | Test |
|---|---|---|
| 온라인 비실시간(LMS) | 20.4% | 21.5% |
| 블렌디드(혼합형) | 14.4% | 14.1% |
| 프로젝트 기반(PBL) | 13.8% | 13.6% |
| 모바일 마이크로러닝 | 13.7% | 13.6% |
| 시뮬레이션/VR 기반 | 12.9% | 12.6% |
| 온라인 실시간(Zoom 등) | 12.8% | 12.8% |
| 오프라인(교실 수업) | 12.0% | 11.8% |

### 학급 규모 (context.class_size)
| 값 | Train | Test |
|---|---|---|
| 대규모(30명 이상) | 46.6% | 48.1% |
| 소규모(1–10명) | 27.9% | 27.9% |
| 중규모(10–30명) | 25.5% | 24.0% |

### 기관 유형 (context.institution_type)
| 값 | Train | Test |
|---|---|---|
| 기업 | 20.5% | 23.0% |
| 공공/비영리 교육기관 | 19.8% | 19.6% |
| 직업훈련기관 | 18.0% | 15.8% |
| 대학교(학부) | 17.3% | 18.1% |
| 초·중등학교 | 12.3% | 12.7% |
| 대학원 | 12.2% | 10.7% |

### 학습자 연령 (context.learner_age)
| 값 | Train | Test |
|---|---|---|
| 20대 | 35.8% | 32.5% |
| 30대 | 26.4% | 23.8% |
| 40대 이상 | 23.4% | 27.0% |
| 10대 | 14.4% | 16.8% |

### 학습자 교육수준 (context.learner_education)
| 값 | Train | Test |
|---|---|---|
| 성인 학습자(비학위) | 27.9% | 27.6% |
| 대학 | 25.0% | 26.2% |
| 고등 | 20.7% | 19.6% |
| 중등 | 17.1% | 16.7% |
| 초등 | 9.2% | 9.9% |

### 도메인 전문성 (context.domain_expertise)
| 값 | Train | Test |
|---|---|---|
| 초급 | 43.4% | 43.7% |
| 중급 | 42.6% | 41.9% |
| 고급 | 14.0% | 14.4% |

### 교과 도메인 (domain)
| 값 | Train | Test |
|---|---|---|
| 언어 | 19.2% | 19.8% |
| 과학 | 18.9% | 19.6% |
| 수학 | 18.9% | 19.5% |
| 사회 | 18.8% | 19.5% |
| 교육(교수·학습) | 4.3% | 4.1% |
| AI/개발/의료/경영/서비스 | ~4% 각각 | ~3.5% 각각 |

### 난이도 (difficulty)
| 값 | Train | Test |
|---|---|---|
| 보통 | 34.0% | 33.7% |
| 어려움 | 33.0% | 33.3% |
| 쉬움 | 33.0% | 33.0% |

## 💾 사용 방법

```python
from datasets import load_dataset

# 전체 데이터셋 로드
dataset = load_dataset("upstage-isd-agent/scenarios")

# Train/Test 분리 데이터 사용
train_data = dataset['train']
test_data = dataset['test']

# 특정 조건 필터링
easy_scenarios = train_data.filter(
    lambda x: '쉬움' in x['difficulty']
)

# 기업 교육 시나리오만 선택
corporate = train_data.filter(
    lambda x: x['context']['institution_type'] == '기업'
)
```

## 📋 시나리오 스키마

```json
{
  "scenario_id": "IDLD-0001",
  "variant_type": "idld_aligned",
  "title": "시나리오 제목",
  "context": {
    "prior_knowledge": "사전 지식",
    "duration": "학습 기간",
    "learning_environment": "학습 환경",
    "class_size": "학급 규모",
    "additional_context": "추가 맥락",
    "institution_type": "기관 유형",
    "learner_age": "학습자 연령",
    "learner_education": "학습자 교육수준",
    "learner_role": "학습자 역할",
    "domain_expertise": "도메인 전문성"
  },
  "learning_goals": ["학습 목표 1", "학습 목표 2"],
  "constraints": {
    "budget": "예산",
    "resources": ["리소스 1", "리소스 2"],
    "accessibility": "접근성",
    "language": "ko",
    "tech_requirements": "기술 요구사항",
    "assessment_type": "평가 유형"
  },
  "difficulty": "쉬움/보통/어려움",
  "domain": "교과 도메인"
}
```

## 📚 관련 이슈

- [#97](https://github.com/blackdew/upstage_isd_agent/issues/97): context_variant 품질 개선
- [#99](https://github.com/blackdew/upstage_isd_agent/issues/99): difficulty 다양화
- [#100](https://github.com/blackdew/upstage_isd_agent/issues/100): Train/Test 재분리
- [#101](https://github.com/blackdew/upstage_isd_agent/issues/101): Hugging Face 업데이트

## 📄 라이선스

Apache License 2.0

## 🔗 참고

- **프로젝트**: [upstage-isd-agent](https://github.com/blackdew/upstage_isd_agent)
- **원본 논문**: IDLD (Instructional Design Learning Dataset)
