---
type: "dataset"
id: "sejongwang/ipapack_plus_clean"
source: "huggingface"
url: "https://huggingface.co/datasets/sejongwang/ipapack_plus_clean"
downloads: 263
summary: "IPAPACK++ 음성 데이터의 정제된 음소 라벨 오버레이로, 라벨 품질 개선용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
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
commercial_use:
  - "[[상업 이용 가능]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# sejongwang/ipapack_plus_clean

> dataset · [Hugging Face](https://huggingface.co/datasets/sejongwang/ipapack_plus_clean)

IPAPACK++ 음성 데이터의 정제된 음소 라벨 오버레이로, 라벨 품질 개선용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `A labels-only, strictly additive cleaned overlay on IPAPACK++` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `It adds a regenerated phoneme label (phones_v1_clean) alongside the paper's original phones` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · task_categories = `automatic-speech-recognition` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — task_rule · task:speech_recognition = `audio` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:information_extraction = `A labels-only, strictly additive cleaned overlay on IPAPACK++` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `It adds a regenerated phoneme label (phones_v1_clean) alongside the paper's original phones` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `45 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
