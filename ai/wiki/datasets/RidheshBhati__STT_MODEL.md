---
type: "dataset"
id: "RidheshBhati/STT_MODEL"
source: "huggingface"
url: "https://huggingface.co/datasets/RidheshBhati/STT_MODEL"
downloads: 5354
summary: "50개 언어의 음성-텍스트 쌍으로 구성된 다국어 음성 인식(STT) 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
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
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# RidheshBhati/STT_MODEL

> dataset · [Hugging Face](https://huggingface.co/datasets/RidheshBhati/STT_MODEL)

50개 언어의 음성-텍스트 쌍으로 구성된 다국어 음성 인식(STT) 데이터셋입니다.

## 분류

- **작업**: [[음성 인식]] — tag_match · readme, tags = `speech-recognition` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `Audio and transcript pairs for 50 languages.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme = `Audio and transcript pairs for 50 languages.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `Audio and transcript pairs for 50 languages.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `44 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `21` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Each language is a Dataset Viewer configuration with train, validation, and test splits.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `transcript` 열 p90 83자 ≈ 21 토큰 (viewer statistics, korean/validation)
