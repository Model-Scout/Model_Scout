---
type: "dataset"
id: "Nexdata-AI/Agent-Trajectory-Data-Sample"
source: "huggingface"
url: "https://huggingface.co/datasets/Nexdata-AI/Agent-Trajectory-Data-Sample"
downloads: 56
summary: "사무실 기반 시나리오의 다중 턴 추론 경로와 도구 호출 체인을 포함한 에이전트 계획 능력 분석용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
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
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Nexdata-AI/Agent-Trajectory-Data-Sample

> dataset · [Hugging Face](https://huggingface.co/datasets/Nexdata-AI/Agent-Trajectory-Data-Sample)

사무실 기반 시나리오의 다중 턴 추론 경로와 도구 호출 체인을 포함한 에이전트 계획 능력 분석용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `support the analysis of agent planning capabilities, research into tool selection strategies, and quality assessment` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `support the analysis of agent planning capabilities, research into tool selection strategies, and quality assessment` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `office-based scenarios such as in-depth searches, data analysis, and industry research` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:reranking, task:retrieval = `complete multi-turn reasoning trajectories and tool-calling chains` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `complete multi-turn reasoning trajectories and tool-calling chains` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `16` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `office-based scenarios such as in-depth searches, data analysis, and industry research` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `providing a structured benchmark for agent training and evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `providing a structured benchmark for agent training and evaluation` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `created_at` 열 p90 24자 ≈ 16 토큰 (viewer statistics, default/train)
