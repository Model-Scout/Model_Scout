---
type: "dataset"
id: "deep1003/ai-topic-space-korea"
source: "huggingface"
url: "https://huggingface.co/datasets/deep1003/ai-topic-space-korea"
downloads: 11
summary: "한국 AI 지식 생태계(1990-2026)의 정책·학술·특허 문서 기반 의미 공간과 정책 격차 분석 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[학술·논문]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# deep1003/ai-topic-space-korea

> dataset · [Hugging Face](https://huggingface.co/datasets/deep1003/ai-topic-space-korea)

한국 AI 지식 생태계(1990-2026)의 정책·학술·특허 문서 기반 의미 공간과 정책 격차 분석 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Documents are mapped to L3 nodes by multilingual sentence-embedding (BGE-M3) similarity.` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding = `Korean academic papers, patents, and policy/institutional documents` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `31` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `Korean academic papers, patents, and policy/institutional documents (1990–2026)` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `L2` 열 p90 46자 ≈ 31 토큰 (viewer statistics, l0_l1_l2_cluster_counts/train)
