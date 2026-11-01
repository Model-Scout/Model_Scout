---
language:
  - ko
tags:
  - nlp
  - artificial-intelligence
  - citation-network
  - summarization
  - recommendation-system
  - knowledge-graph
task_categories:
  - text-classification
  - summarization
  - other
size_categories:
  - 10K<n<100K
---

# 📄 paper_summaries

## 📌 데이터셋 개요

**paper_summaries**는 학술 연구 분석 및 추천 시스템 구축을 위해 설계된  
**12,777개의 arXiv 논문 기반 연구 데이터셋**입니다.

본 데이터셋은 다음 과정을 통해 구축되었습니다:

- Survey 논문 reference 확장 수집
- PyTorch Korea 주간 AI/ML 추천 논문 반영
- arXiv 논문만 필터링
- Primary Category 제한 (cs.CL, cs.LG, cs.AI)

구조는 **Relational + Citation Graph Hybrid 형태**로 설계되었습니다.

---

## 🎯 활용 목적 (Intended Use)

본 데이터셋은 다음과 같은 연구 및 서비스 개발을 위해 설계되었습니다:

- 학술 논문 추천 시스템
- Citation Network 분석
- 연구 트렌드 분석
- LLM 기반 다중 요약 실험
- RAG 파이프라인 연구
- Knowledge Graph 구축
- 개인화 피드 랭킹 실험

다음 목적에는 적합하지 않습니다:

- 전체 글로벌 인용 네트워크 분석
- 모든 AI/NLP 논문의 포괄적 수집

---

## 🗂 데이터 구조

### 핵심 구성 테이블

- `papers`
- `summaries`
- `categories`
- `papers_categories`
- `citation_edges`

### 주요 특징

- 총 논문 수: **12,777편**
- 도메인: NLP / AI / Machine Learning
- 인용 구조: Directed Self Graph
- 카테고리: Multi-label 구조
- 요약: 논문당 다중 summary_type 보유
- 구조: 관계형 + 그래프 하이브리드

---

## 📥 데이터 수집 기준

### 1️⃣ Survey Reference 확장

출처:
- NiuTrans ABigSurvey (Computational Social Science & Social Media 섹션)

선정된 Survey 논문의 모든 reference를 수집하여  
연구 대표성과 인용 기반 구조를 확보하였습니다.

---

### 2️⃣ PyTorch Korea 주간 AI/ML 추천 반영

출처:
- PyTorch Korea 커뮤니티 주간 AI/ML 추천 게시물 (2025–2026)

이 중 `cs.CL` 논문만 선별하여 최신 NLP 트렌드를 유지하였습니다.

목적:
- 최신성 확보
- 실무자 큐레이션 반영

---

### 3️⃣ arXiv 논문만 유지

- 형식 통일성 확보
- 메타데이터 일관성 유지
- 표준화된 카테고리 체계 사용

---

### 4️⃣ Primary Category 필터링

다음 arXiv Primary Category에 해당하는 논문만 포함:

- `cs.CL`
- `cs.LG`
- `cs.AI`

---

## 📊 주요 필드

### papers

- arxiv_id
- title
- abstract
- citation_count
- influential_citation_count
- reference_count
- published_date
- updated_date

### summaries

- paper_id
- summary_text
- summary_type (`motivation`, `methodology`, `performance`, `significance`, `keypoint`)
- created_at

### citation_edges

- seed_id
- cited_paper_id
- is_influential

---

## ⚠️ 한계 및 편향 (Limitations & Bias)

- arXiv 논문으로 한정됨
- cs.CL / cs.LG / cs.AI로 제한
- 인용 그래프는 전체 글로벌 네트워크가 아님
- Survey 기반 확장은 특정 연구 분야에 편향 가능성 존재

---

## 🧠 왜 12,777편인가?

12,777편은 현재 인프라 및 운영 규모에서:

- 지속적 업데이트 가능
- 인용 무결성 유지
- 요약 품질 관리 가능
- DB 성능 안정성 확보

를 만족하는 **관리 가능한 최대 규모**입니다.

본 데이터셋은 단순 규모 확장이 아닌  
**구조적 일관성과 유지 가능성**을 우선합니다.

---

## 🔄 업데이트 정책

- PyTorch Korea 추천 기반 주간 확장 가능
- 정기적 citation 확장
- Primary category 필터 유지

---

## 📜 라이선스

본 데이터셋은 arXiv 논문의 메타데이터를 기반으로 합니다.  
각 논문의 개별 라이선스 및 arXiv 이용 약관을 준수해야 합니다.

---

## 👩‍💻 Maintainer

10seconds
