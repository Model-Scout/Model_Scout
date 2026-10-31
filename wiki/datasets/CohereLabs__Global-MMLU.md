---
type: "dataset"
id: "CohereLabs/Global-MMLU"
source: "huggingface"
url: "https://huggingface.co/datasets/CohereLabs/Global-MMLU"
downloads: 31934
summary: "42개 언어로 번역된 MMLU 질문과 문화 민감도 주석을 포함한 다국어 평가 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[질의응답]]"
input_modality:
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
# CohereLabs/Global-MMLU

> dataset · [Hugging Face](https://huggingface.co/datasets/CohereLabs/Global-MMLU)

42개 언어로 번역된 MMLU 질문과 문화 민감도 주석을 포함한 다국어 평가 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `Global-MMLU 🌍 is a multilingual evaluation set spanning 42 languages, including English. This dataset combines machine translations for MMLU questions along wit` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `This dataset combines machine translations for MMLU questions along with professional translations and crowd-sourced post-edits.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `It also includes cultural sensitivity annotations for a subset of the questions (2850 questions per language) and classifies them as Culturally Sensitive (CS) 🗽` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `42 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `96` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Global-MMLU 🌍 is a multilingual evaluation set spanning 42 languages, including English.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Global-MMLU 🌍 is a multilingual evaluation set spanning 42 languages, including English.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 382자 ≈ 96 토큰 (viewer statistics, ko/test)
