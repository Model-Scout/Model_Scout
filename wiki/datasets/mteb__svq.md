---
type: "dataset"
id: "mteb/svq"
source: "huggingface"
url: "https://huggingface.co/datasets/mteb/svq"
downloads: 562
summary: "17개 언어, 26개 지역에서 다양한 환경 조건으로 녹음된 짧은 음성 질문 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[질의응답]]"
  - "[[문서 검색]]"
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
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# mteb/svq

> dataset · [Hugging Face](https://huggingface.co/datasets/mteb/svq)

17개 언어, 26개 지역에서 다양한 환경 조건으로 녹음된 짧은 음성 질문 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **작업**: [[문서 검색]] — ner · readme = `The query’s text comes from validation and test sets of the XTREME-UP’s retrieval and question answering benchmark datasets.` · 신뢰도 medium
- **작업**: [[음성 인식]] — metadata · task_categories = `automatic-speech-recognition` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `Simple Voice Questions (SVQ) is a set of short audio questions recorded in 26 locales across 17 languages under multiple audio conditions.` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:question_answering, task:retrieval = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:speech_recognition = `The query’s text comes from validation and test sets of the XTREME-UP’s retrieval and question answering benchmark datasets.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `17 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `12` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Simple Voice Questions (SVQ) is a set of short audio questions recorded in 26 locales across 17 languages under multiple audio conditions.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `the data is released in its entirety as an undivided evaluation set.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 50자 ≈ 12 토큰 (viewer statistics, audio/test)
