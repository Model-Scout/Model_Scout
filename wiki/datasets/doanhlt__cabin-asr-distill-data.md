---
type: "dataset"
id: "doanhlt/cabin-asr-distill-data"
source: "huggingface"
url: "https://huggingface.co/datasets/doanhlt/cabin-asr-distill-data"
downloads: 171
summary: "21개 언어의 음성 인식용 다국어 ASR 증류 데이터셋으로 1,382시간 분량의 정제된 음성 클립을 포함합니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# doanhlt/cabin-asr-distill-data

> dataset · [Hugging Face](https://huggingface.co/datasets/doanhlt/cabin-asr-distill-data)

21개 언어의 음성 인식용 다국어 ASR 증류 데이터셋으로 1,382시간 분량의 정제된 음성 클립을 포함합니다.

## 분류

- **작업**: [[음성 인식]] — metadata · readme, tags, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `16 kHz mono PCM16, peak normalised to -1 dBFS` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:speech_recognition = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `21 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `19` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Cabin Multilingual ASR Distillation Dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Total Curated Volume: 1,382.45 hours (692,829 clips) cleaned from 2,188.95 raw hours (1,133,523 raw clips)` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `url_or_shard` 열 p90 74자 ≈ 19 토큰 (viewer statistics, ko/test)
