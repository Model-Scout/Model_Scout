---
type: "dataset"
id: "psdn-ai/CROWS-multilingual"
source: "huggingface"
url: "https://huggingface.co/datasets/psdn-ai/CROWS-multilingual"
downloads: 4976
summary: "16개 언어의 821,361개 WAV 음성 녹음 데이터셋으로 음성 인식 등에 활용 가능"
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
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# psdn-ai/CROWS-multilingual

> dataset · [Hugging Face](https://huggingface.co/datasets/psdn-ai/CROWS-multilingual)

16개 언어의 821,361개 WAV 음성 녹음 데이터셋으로 음성 인식 등에 활용 가능

## 분류

- **작업**: [[음성 인식]] — ner · readme = `CROWS Multilingual contains 821,361 WAV recordings across 16 languages` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `821,361 WAV recordings` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:speech_recognition = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `16 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `122` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `CROWS Multilingual contains 821,361 WAV recordings across 16 languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `All 821,361 recordings have been packaged, decode-checked, and uploaded` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `english_translated_hypothesis_transcript` 열 p90 487자 ≈ 122 토큰 (viewer statistics, breadth_gt_6_ko/full)
