---
type: "dataset"
id: "McGill-NLP/speech-translation-and-summarization"
source: "huggingface"
url: "https://huggingface.co/datasets/McGill-NLP/speech-translation-and-summarization"
downloads: 216
summary: "영어 중심 다국어 음성 데이터셋으로 음성 번역과 요약에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 인식]]"
  - "[[요약]]"
  - "[[음성 합성]]"
  - "[[번역]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# McGill-NLP/speech-translation-and-summarization

> dataset · [Hugging Face](https://huggingface.co/datasets/McGill-NLP/speech-translation-and-summarization)

영어 중심 다국어 음성 데이터셋으로 음성 번역과 요약에 활용됨.

## 분류

- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 medium
- **작업**: [[요약]] — ner · readme = `generated article and summary audio` · 신뢰도 medium
- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-speech` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `generated article and summary audio` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:summarization, task:text_to_speech, task:translation = `text` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme, task:text_to_speech = `generated article and summary audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:speech_recognition, task:summarization, task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `25 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1577` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `English-Centric Multilingual Audio Dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `few_shot and test splits` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 6309자 ≈ 1577 토큰 (viewer statistics, english_korean/test)
