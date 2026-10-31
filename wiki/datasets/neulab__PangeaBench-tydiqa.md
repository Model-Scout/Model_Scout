---
type: "dataset"
id: "neulab/PangeaBench-tydiqa"
source: "huggingface"
url: "https://huggingface.co/datasets/neulab/PangeaBench-tydiqa"
downloads: 194
summary: "11개 언어의 204K 문항으로 구성된 다국어 질의응답 데이터셋입니다."
readme_status: "template"
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
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# neulab/PangeaBench-tydiqa

> dataset · [Hugging Face](https://huggingface.co/datasets/neulab/PangeaBench-tydiqa)

11개 언어의 204K 문항으로 구성된 다국어 질의응답 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories, task_ids = `question-answering` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `question answering dataset covering 11 typologically diverse languages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `question answering dataset covering 11 typologically diverse languages with 204K question-answer pairs.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `11 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `9917` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `TyDi QA is a question answering dataset covering 11 typologically diverse languages` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `TyDi QA is a question answering dataset covering 11 typologically diverse languages with 204K question-answer pairs.` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `document_plaintext` 열 p90 39669자 ≈ 9917 토큰 (viewer statistics, primary_task/validation)
