---
type: "dataset"
id: "doanhlt/cabin-interpreted-interviews"
source: "huggingface"
url: "https://huggingface.co/datasets/doanhlt/cabin-interpreted-interviews"
downloads: 54
summary: "YouTube에서 녹음된 인터뷰 및 기자회견의 연속 통역 음성 데이터로, 음성 인식과 언어 식별 등에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[언어 모델링]]"
  - "[[문서 검색]]"
  - "[[음성 인식]]"
  - "[[번역]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[de]]"
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[vi]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# doanhlt/cabin-interpreted-interviews

> dataset · [Hugging Face](https://huggingface.co/datasets/doanhlt/cabin-interpreted-interviews)

YouTube에서 녹음된 인터뷰 및 기자회견의 연속 통역 음성 데이터로, 음성 인식과 언어 식별 등에 활용됨.

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `spoken language ID at turn changes` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `turn segmentation and speech-translation pairs` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `Raw audio hours of videos where two languages were detected` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:language_modeling, task:retrieval, task:translation = `Text labels are machine transcripts by our own model` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling, task:speech_recognition, task:translation = `Text labels are machine transcripts by our own model` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `6 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `51` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-3.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Real consecutive interpretation recorded on YouTube: interviews, press conferences and Q&A` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 203자 ≈ 51 토큰 (viewer statistics, vi-ko/train)
