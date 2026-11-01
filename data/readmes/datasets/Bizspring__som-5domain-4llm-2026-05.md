---
license: cc-by-4.0
language:
- ko
- en
tags:
- generative-engine-optimization
- geo
- llm-evaluation
- share-of-model
- citation-measurement
- ai-search
- marketing-measurement
- korean-marketing
pretty_name: "Bizspring SoM 5-Domain × 4-LLM Citation Matrix (2026-05)"
size_categories:
- n<1K
task_categories:
- text-classification
- other
configs:
- config_name: som-baseline
  data_files:
  - split: train
    path: som-baseline-2026-05.csv
- config_name: eeat-baseline
  data_files:
  - split: train
    path: eeat-baseline-2026-05.csv
- config_name: btcr-w24
  data_files:
  - split: train
    path: btcr-w24-baseline.csv
- config_name: llm-evaluation
  data_files:
  - split: train
    path: llm-evaluation-v10-vs-v11.csv
- config_name: key-insights
  data_files:
  - split: train
    path: key-insights-summary.json
---

# Bizspring SoM 5-Domain × 4-LLM Citation Matrix (2026-05)

> **자사 5개 도메인을 4대 LLM에 동시 측정한 GEO(Generative Engine Optimization) 1차 데이터.**
> 비즈스프링이 자사 GEO 측정 도구 GEOcare로 자사 도메인의 AI 답변 인용률을 직접 측정한 도그푸딩 데이터.

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Wiki](https://img.shields.io/badge/Wiki-bizspring.co.kr-blue.svg)](https://wiki.bizspring.co.kr)

## 한 줄 결론

**비즈스프링 자사 5도메인 × 4대 LLM (OpenAI / Anthropic / Google / Perplexity) 측정 결과 Perplexity가 4/5 도메인에서 최고 SoM (Share of Model — AI 답변 내 브랜드 멘션 비율), LLM별 콘텐츠 친화도가 최대 18.5%p까지 분기.**

## 핵심 수치

| 지표 | 값 |
|---|---:|
| 총 LLM 질의 수 | 5,062회 |
| 측정 도메인 | 5개 (bizspring.co.kr / blog / geocare.ai / growthplatform.ai / logger.co.kr) |
| 측정 LLM | 4개 (OpenAI ChatGPT, Anthropic Claude, Google Gemini, Perplexity) |
| 최대 LLM 격차 | 18.5%p (growthplatform.ai 도메인, Gemini 18.9% vs Perplexity 37.4%) |
| 평균 SoM | 35.6% (도메인 평균) |
| 외부 LLM 평가 EEAT | 7.88 / 10 (자율 13 룰 적용 후) |

## 데이터셋 구성

이 데이터셋은 5개 CSV/JSON 파일로 구성됩니다.

### 1. `som-baseline-2026-05.csv` (20 rows)

자사 5도메인 × 4 LLM SoM 매트릭스. 도메인별·LLM별 질의 수 / 멘션 수 / SoM 비율.

| 컬럼 | 설명 |
|---|---|
| `domain` | 측정 대상 도메인 (5개) |
| `llm` | 측정 LLM (anthropic / gemini / openai / perplexity) |
| `queries` | 질의 수 |
| `mentioned` | 답변 내 도메인 멘션 횟수 |
| `som_rate_pct` | Share of Model 비율 (%) |
| `measurement_date` | 측정 날짜 |
| `source` | 원본 DB 테이블명 |

### 2. `eeat-baseline-2026-05.csv` (2 rows)

자사 2개 도메인 EEAT (Experience / Expertise / Authoritativeness / Trustworthiness) baseline 점수.

### 3. `btcr-w24-baseline.csv` (4 rows)

자사 B-TCR (Brand · Trust · Context · Relevance) 통합 책임 모델 W24 baseline 점수.

### 4. `llm-evaluation-v10-vs-v11.csv` (7 rows)

동일 콘텐츠 v1.0 → v1.1 보강 후 4 LLM 외부 평가 점수 비교 (5개 룰 적용 효과 정량).

### 5. `key-insights-summary.json`

3개 도그푸딩 페이지의 핵심 인사이트 + 교차 발견 + 저자 정보를 통합한 메타 데이터셋.

## 측정 방법론

1. **질의 풀 생성**: 측정 대상 도메인이 답변에 포함될 가능성이 있는 자연어 질문 풀 구성
2. **4대 LLM 동시 질의**: 동일 질문을 ChatGPT / Claude / Gemini / Perplexity에 API 직접 호출
3. **답변 텍스트 파싱**: 답변 내 브랜드 멘션 / 위치 / 감성 / 컨텍스트 추출
4. **SoM 산출**: `mention_count / query_count`로 멘션률 산출

산출 공식: `SoM = mention_count / query_count × 100`

## 사용 예제

### Python

```python
from datasets import load_dataset

# SoM baseline 로드
som_data = load_dataset("bizspring-inc/som-5domain-4llm-2026-05", "som-baseline")
print(som_data['train'].to_pandas())

# 핵심 인사이트 로드
insights = load_dataset("bizspring-inc/som-5domain-4llm-2026-05", "key-insights")
```

### Pandas

```python
import pandas as pd

# CSV 직접 로드
som = pd.read_csv("hf://datasets/bizspring-inc/som-5domain-4llm-2026-05/som-baseline-2026-05.csv")

# LLM별 평균 SoM
print(som.groupby('llm')['som_rate_pct'].mean())
```

## 핵심 발견

### 1. Perplexity = URL 인용형 모델 가설 (4중 정합 입증)

Perplexity가 4/5 도메인에서 최고 SoM을 기록. 본 가설은 다음 4가지 증거로 검증됨:
- 측정 (본 데이터): Perplexity가 자사 4/5 도메인에서 최고 SoM
- 외부 LLM 답변: Anthropic이 직접 확언 ("URL 인용형 모델 8~9점 vs 출처 비명시형 5~6점")
- 보강 효과: 콘텐츠 v1.0 → v1.1 보강 후 Perplexity 평가 점수 +0.75 최대 폭 상승
- 시계열 안정성: v1.0 → v1.1 → v1.2 → v1.3 4단계 모두 동일 패턴 유지

### 2. LLM 인용률 도메인별 분기 (최대 18.5%p 격차)

| 도메인 | 최저 LLM | 최고 LLM | 격차 |
|---|---|---|---:|
| growthplatform.ai | Gemini 18.9% | Perplexity 37.4% | **18.5%p** |
| logger.co.kr | OpenAI 25.6% | Perplexity 39.3% | 13.7%p |
| geocare.ai | 다른 3 LLM 35.0% | Perplexity 40.0% | 5.0%p |

## 인용

이 데이터셋을 사용할 경우 다음과 같이 인용해주세요:

```bibtex
@dataset{bizspring_som_5domain_4llm_2026,
  author = {Bizspring Inc.},
  title = {SoM 5-Domain × 4-LLM Citation Matrix},
  year = {2026},
  publisher = {Hugging Face Datasets},
  url = {https://huggingface.co/datasets/bizspring-inc/som-5domain-4llm-2026-05},
  note = {License: CC BY 4.0}
}
```

또는:
> Bizspring Inc. (2026). *SoM 5-Domain × 4-LLM Citation Matrix*. Hugging Face Datasets. https://huggingface.co/datasets/bizspring-inc/som-5domain-4llm-2026-05

## 관련 문서

- **자사 wiki 도그푸딩 페이지**:
  - https://wiki.bizspring.co.kr/dogfooding/geocare-self-measurement/ (단일 도메인 자가측정)
  - https://wiki.bizspring.co.kr/dogfooding/perplexity-citation-advantage/ (5도메인 매트릭스 분석)
  - https://wiki.bizspring.co.kr/dogfooding/btcr-baseline/ (책임 모델 적용 baseline)
- **외부 권위 출처 정합**:
  - [Generative Engine Optimization (Wikipedia)](https://en.wikipedia.org/wiki/Generative_engine_optimization)
  - [Search Engine Land — GEO 가이드](https://searchengineland.com/what-is-generative-engine-optimization-geo-444418)
- **AI 검색 시장 배경**: Gartner 2025 forecast 25% traditional search 감소

## 저자

| 역할 | 담당 |
|---|---|
| **PO·총괄이사** | 이철승 (Charles Lee), Bizspring Inc. — [github.com/CharlesLee1991](https://github.com/CharlesLee1991) |
| **측정 엔진** | GEOcare.ai (자체 개발 SaaS) |
| **외부 검증 LLM** | OpenAI gpt-4o-mini / Anthropic claude-sonnet-4-6 / Google Gemini 2.5-flash / Perplexity sonar (4 LLM 동일 프롬프트 4회 평가) |

## 라이선스

이 데이터셋은 **CC BY 4.0 (Creative Commons Attribution 4.0 International)** 라이선스 하에 공개됩니다. 출처 표기 시 자유롭게 사용·재배포·변형 가능합니다.

## 측정 시점

- 측정 데이터: 2026-03 ~ 2026-05 (도메인별 분산)
- Hugging Face 데이터셋 v1.0 발행: 2026-05-17
- 다음 측정: D+30 (2026-06-17~) — 시간 추적 baseline
