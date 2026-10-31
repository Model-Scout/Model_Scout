---
type: "dataset"
id: "universe-team/universebench"
source: "huggingface"
url: "https://huggingface.co/datasets/universe-team/universebench"
downloads: 103
summary: "UniVerseBench는 다국어 민속 음악 이해를 위한 대규모 오디오-언어 모델 평가 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[음성 분류]]"
  - "[[임베딩]]"
  - "[[질의응답]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# universe-team/universebench

> dataset · [Hugging Face](https://huggingface.co/datasets/universe-team/universebench)

UniVerseBench는 다국어 민속 음악 이해를 위한 대규모 오디오-언어 모델 평가 벤치마크입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `UniVerseBench is a multilingual folk-music understanding benchmark for large audio–language models (LALMs). It asks models to listen, not to guess from language` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, tags, task_categories = `question-answering` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:audio_classification = `Audio clip + native / English notes + ABC score + titles (native / translation / transliteration) + language + source URL` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:question_answering = `native / English notes + ABC score + titles (native / translation / transliteration) + language + source URL` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Multiple-choice questions grounded in those recordings` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `multilingual` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `UniVerseBench is a multilingual folk-music understanding benchmark` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `The evaluation split of UniVerse (同谣).Training data lives in UniVerseSet.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
