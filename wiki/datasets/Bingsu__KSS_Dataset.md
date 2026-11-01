---
type: "dataset"
id: "Bingsu/KSS_Dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/Bingsu/KSS_Dataset"
downloads: 991
summary: "한국어 단일 화자 음성 데이터셋으로, 한국어 TTS 학습용 음성 및 텍스트 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[음성 합성]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
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
# Bingsu/KSS_Dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/Bingsu/KSS_Dataset)

한국어 단일 화자 음성 데이터셋으로, 한국어 TTS 학습용 음성 및 텍스트 데이터입니다.

## 분류

- **작업**: [[음성 합성]] — metadata · readme, task_categories = `text-to-speech` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme = `It consists of audio files recorded by a professional female voice actoress` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:text_to_speech = `text` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `their aligned text extracted from my books.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `38` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `this is the first publicly available speech dataset for Korean.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `| # of examples | 12853 |` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `decomposed_script` 열 p90 57자 ≈ 38 토큰 (viewer statistics, default/train)
