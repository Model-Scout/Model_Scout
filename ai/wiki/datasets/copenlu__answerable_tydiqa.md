---
type: "dataset"
id: "copenlu/answerable_tydiqa"
source: "huggingface"
url: "https://huggingface.co/datasets/copenlu/answerable_tydiqa"
downloads: 205
summary: "11개 언어의 질문에 답하거나 답할 수 없는 질문을 포함한 TyDi QA 데이터셋입니다."
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
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# copenlu/answerable_tydiqa

> dataset · [Hugging Face](https://huggingface.co/datasets/copenlu/answerable_tydiqa)

11개 언어의 질문에 답하거나 답할 수 없는 질문을 포함한 TyDi QA 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories, task_ids = `question-answering` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `question_text | str | The question to answer` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `annotations["answer_text"] | list[str] | The answer, a span of text from 'document_plaintext'.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `11 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `271` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `TyDi QA is a question answering dataset covering 11 typologically diverse languages.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset contains a train and a validation set, with 116067 and 13325 examples, respectively.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `document_plaintext` 열 p90 1085자 ≈ 271 토큰 (viewer statistics, default/validation)
