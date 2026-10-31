---
type: "dataset"
id: "FluidInference/fleurs-full"
source: "huggingface"
url: "https://huggingface.co/datasets/FluidInference/fleurs-full"
downloads: 1726
summary: "Google FLEURS의 30개 언어 음성 인식 테스트셋으로 ASR 벤치마킹용 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# FluidInference/fleurs-full

> dataset · [Hugging Face](https://huggingface.co/datasets/FluidInference/fleurs-full)

Google FLEURS의 30개 언어 음성 인식 테스트셋으로 ASR 벤치마킹용 데이터입니다.

## 분류

- **작업**: [[음성 인식]] — tag_match · readme, tags = `asr` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — metadata · modality, task:speech_recognition = `audio` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:speech_recognition = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `30 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Complete test set of Google FLEURS for all 30 languages supported by Qwen3-ASR` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Complete test set of Google FLEURS for all 30 languages supported by Qwen3-ASR, prepared for benchmarking` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `audiofolder` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
