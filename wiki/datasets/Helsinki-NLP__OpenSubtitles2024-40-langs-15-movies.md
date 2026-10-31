---
type: "dataset"
id: "Helsinki-NLP/OpenSubtitles2024-40-langs-15-movies"
source: "huggingface"
url: "https://huggingface.co/datasets/Helsinki-NLP/OpenSubtitles2024-40-langs-15-movies"
downloads: 82
summary: "OpenSubtitles2024 코퍼스에서 파생된 40개 언어 15편 영화 자막 동기화 다중 병렬 평가 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[질의응답]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Helsinki-NLP/OpenSubtitles2024-40-langs-15-movies

> dataset · [Hugging Face](https://huggingface.co/datasets/Helsinki-NLP/OpenSubtitles2024-40-langs-15-movies)

OpenSubtitles2024 코퍼스에서 파생된 40개 언어 15편 영화 자막 동기화 다중 병렬 평가 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `designed for evaluation and development of multilingual machine translation systems and multilingual language models` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:translation = `synchronized subtitle segments from 15 movies / TV episodes aligned across 40 languages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:translation = `synchronized subtitle segments from 15 movies / TV episodes aligned across 40 languages` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `38 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `This dataset is a multi-parallel evaluation subset derived from the OpenSubtitles2024 corpus` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
