---
type: "dataset"
id: "open-thoughts/OpenThoughts3-1.2M"
source: "huggingface"
url: "https://huggingface.co/datasets/open-thoughts/OpenThoughts3-1.2M"
downloads: 24946
summary: "OpenThoughts3-1.2M은 120만 개의 수학, 코드, 과학 문제로 구성된 최첨단 추론 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# open-thoughts/OpenThoughts3-1.2M

> dataset · [Hugging Face](https://huggingface.co/datasets/open-thoughts/OpenThoughts3-1.2M)

OpenThoughts3-1.2M은 120만 개의 수학, 코드, 과학 문제로 구성된 최첨단 추론 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `The final dataset consists of 850,000 math questions, 250,000 code questions, and 100,000 science questions.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `The final dataset consists of 850,000 math questions, 250,000 code questions, and 100,000 science questions.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Annotations are done with QwQ-32B.` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `The final dataset consists of 850,000 math questions, 250,000 code questions, and 100,000 science questions.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[ATH-MaaS__Marco-Mini-Base|ATH-MaaS/Marco-Mini-Base]]
- [[ATH-MaaS__Marco-Mini-Global-Base|ATH-MaaS/Marco-Mini-Global-Base]]
- [[ATH-MaaS__Marco-Nano-Base|ATH-MaaS/Marco-Nano-Base]]
