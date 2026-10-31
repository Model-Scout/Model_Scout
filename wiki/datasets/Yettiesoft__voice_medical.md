---
type: "dataset"
id: "Yettiesoft/voice_medical"
source: "huggingface"
url: "https://huggingface.co/datasets/Yettiesoft/voice_medical"
downloads: 240
summary: "음성 의료 데이터셋으로 의료 분야의 음성 인식에 사용된다."
readme_status: "thin"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[조건부 이용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Yettiesoft/voice_medical

> dataset · [Hugging Face](https://huggingface.co/datasets/Yettiesoft/voice_medical)

음성 의료 데이터셋으로 의료 분야의 음성 인식에 사용된다.

## 분류

- **작업**: [[음성 인식]] — metadata · task_categories = `automatic-speech-recognition` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — metadata · modality, task:speech_recognition = `audio` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:speech_recognition = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `19740` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `transcripts` 열 p90 29610자 ≈ 19740 토큰 (viewer statistics, default/test)
