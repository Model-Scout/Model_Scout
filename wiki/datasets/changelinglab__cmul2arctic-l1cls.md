---
type: "dataset"
id: "changelinglab/cmul2arctic-l1cls"
source: "huggingface"
url: "https://huggingface.co/datasets/changelinglab/cmul2arctic-l1cls"
downloads: 677
summary: "CMU Arctic와 L2-ARCTIC 음성 데이터를 결합한 L1(모국어) 분류 연구용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[음성 분류]]"
  - "[[텍스트 분류]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[hi]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[vi]]"
  - "[[중국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# changelinglab/cmul2arctic-l1cls

> dataset · [Hugging Face](https://huggingface.co/datasets/changelinglab/cmul2arctic-l1cls)

CMU Arctic와 L2-ARCTIC 음성 데이터를 결합한 L1(모국어) 분류 연구용 데이터셋입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[텍스트 분류]] — ner · readme = `for L1 (native language) classification research` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:audio_classification = `Audio is embedded in Parquet files for efficient loading via HuggingFace datasets` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `L1 (native language) classification research` · 신뢰도 low
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[hi]] — metadata · languages = `hi` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `7 languages` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset combines CMU Arctic (native English speakers) and L2-ARCTIC (non-native English speakers)` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
