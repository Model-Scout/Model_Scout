---
type: "dataset"
id: "Westing/LLM-Misalign-Climate-Change"
source: "huggingface"
url: "https://huggingface.co/datasets/Westing/LLM-Misalign-Climate-Change"
downloads: 130
summary: "기후변화 관련 지식 상호작용을 통합한 데이터셋으로, 사용자 요구 분석에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[교육]]"
  - "[[환경·기상]]"
  - "[[금융·경제]]"
  - "[[의료·보건]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Westing/LLM-Misalign-Climate-Change

> dataset · [Hugging Face](https://huggingface.co/datasets/Westing/LLM-Misalign-Climate-Change)

기후변화 관련 지식 상호작용을 통합한 데이터셋으로, 사용자 요구 분석에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories, task_ids = `text-classification` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `This dataset provides a unified collection of climate change–related knowledge interactions for conducting the analyses presented in the paper.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:retrieval = `real user questions extracted from LLM conversation logs` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `14 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `999` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[교육]] — tag_match · tags = `education` · 신뢰도 medium
- **도메인**: [[환경·기상]] — tag_match · readme, tags = `climate` · 신뢰도 medium
- **도메인**: [[금융·경제]] — tag_match · tags = `finance` · 신뢰도 medium
- **도메인**: [[의료·보건]] — tag_match · tags = `health` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 3997자 ≈ 999 토큰 (viewer statistics, default/train)
