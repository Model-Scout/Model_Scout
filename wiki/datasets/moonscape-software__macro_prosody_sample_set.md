---
type: "dataset"
id: "moonscape-software/macro_prosody_sample_set"
source: "huggingface"
url: "https://huggingface.co/datasets/moonscape-software/macro_prosody_sample_set"
downloads: 285
summary: "7개 언어의 음향 특징 데이터로 다국어 음운학 및 음성 기술 연구용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[gv]]"
  - "[[he]]"
  - "[[hi]]"
  - "[[한국어]]"
  - "[[lss]]"
  - "[[mdh]]"
  - "[[다국어]]"
  - "[[tzh]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# moonscape-software/macro_prosody_sample_set

> dataset · [Hugging Face](https://huggingface.co/datasets/moonscape-software/macro_prosody_sample_set)

7개 언어의 음향 특징 데이터로 다국어 음운학 및 음성 기술 연구용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Training and evaluating deepfake detection, anti-spoofing, or synthetic audio identification models` · 신뢰도 low
- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — metadata · modality = `audio` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding = `Each row in this dataset is one spoken clip with 30+ acoustic features extracted from it.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Each row in this dataset is one spoken clip with 30+ acoustic features extracted from it.` · 신뢰도 low
- **언어**: [[gv]] — metadata · languages = `gv` · 신뢰도 high
- **언어**: [[he]] — metadata · languages = `he` · 신뢰도 high
- **언어**: [[hi]] — metadata · languages = `hi` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[lss]] — metadata · languages = `lss` · 신뢰도 high
- **언어**: [[mdh]] — metadata · languages = `mdh` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `7 languages` · 신뢰도 high
- **언어**: [[tzh]] — metadata · languages = `tzh` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `openrail` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This is a structured acoustic feature dataset for linguistic research, speech technology, and cross-linguistic prosody analysis.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
