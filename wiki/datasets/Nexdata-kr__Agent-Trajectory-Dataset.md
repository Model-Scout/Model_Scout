---
type: "dataset"
id: "Nexdata-kr/Agent-Trajectory-Dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/Nexdata-kr/Agent-Trajectory-Dataset"
downloads: 68
summary: "사무 환경 작업 시나리오의 멀티턴 추론과 도구 호출 체인 데이터로 에이전트 학습·평가용입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[리랭킹]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Nexdata-kr/Agent-Trajectory-Dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/Nexdata-kr/Agent-Trajectory-Dataset)

사무 환경 작업 시나리오의 멀티턴 추론과 도구 호출 체인 데이터로 에이전트 학습·평가용입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `에이전트의 계획 수립 능력 분석, 도구 선택 전략 연구 및 작업 품질 평가를 지원하도록 설계되었으며` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `완전한 멀티턴 추론 과정과 도구 호출 체인으로 구성되어 있습니다.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `본 데이터셋은 심층 검색, 데이터 분석, 산업 리서치 등 사무 환경에서 수행되는 다양한 작업 시나리오를 포함하며` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:reranking, task:retrieval = `완전한 멀티턴 추론 과정과 도구 호출 체인으로 구성되어 있습니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `완전한 멀티턴 추론 과정과 도구 호출 체인으로 구성되어 있습니다.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `16` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `본 데이터셋은 심층 검색, 데이터 분석, 산업 리서치 등 사무 환경에서 수행되는 다양한 작업 시나리오를 포함하며` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `에이전트 학습 및 평가를 위한 구조화된 벤치마크로 활용할 수 있습니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `created_at` 열 p90 24자 ≈ 16 토큰 (viewer statistics, default/train)
