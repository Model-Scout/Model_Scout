---
type: "dataset"
id: "mippia/SMP_dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/mippia/SMP_dataset"
downloads: 28
summary: "음악 표절 탐지를 위한 유사 음악 쌍과 시간 구간 주석 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[음성 분류]]"
  - "[[텍스트 분류]]"
  - "[[문서 검색]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
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
  - "[[상업 이용 가능]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# mippia/SMP_dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/mippia/SMP_dataset)

음악 표절 탐지를 위한 유사 음악 쌍과 시간 구간 주석 데이터셋입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[텍스트 분류]] — ner · readme = `Relationship type (e.g., `plag` for plagiarism)` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `music plagiarism detection pairs with temporal segment annotations` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — task_rule · task:audio_classification = `audio` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:retrieval = `Only YouTube links and temporal annotations are provided.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Relationship type (e.g., `plag` for plagiarism)` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `32` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `The dataset includes both English and Korean songs across multiple genres.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset accompanies the paper Music Plagiarism Detection: Problem Formulation and a Segment-based Solution.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `comp_link` 열 p90 48자 ≈ 32 토큰 (viewer statistics, default/train)
