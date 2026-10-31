---
type: "dataset"
id: "coastalcph/tydi_xor_rc"
source: "huggingface"
url: "https://huggingface.co/datasets/coastalcph/tydi_xor_rc"
downloads: 2311
summary: "XORQA 확장판으로 7개 언어 질문과 영어 문서 기반의 질의응답 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[bn]]"
  - "[[영어]]"
  - "[[fi]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[te]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# coastalcph/tydi_xor_rc

> dataset · [Hugging Face](https://huggingface.co/datasets/coastalcph/tydi_xor_rc)

XORQA 확장판으로 7개 언어 질문과 영어 문서 기반의 질의응답 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories, task_ids = `question-answering` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `The language of the question` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `The answer in English, a span of text from 'context'.` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[bn]] — metadata · languages = `bn` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[fi]] — metadata · languages = `fi` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `8 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[te]] — metadata · languages = `te` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `265` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `TyDi QA is a question answering dataset covering 11 typologically diverse languages.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset contains a train and a validation set, with 15343 and 3011 examples, respectively.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `context` 열 p90 1061자 ≈ 265 토큰 (viewer statistics, default/validation)
