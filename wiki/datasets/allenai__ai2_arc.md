---
type: "dataset"
id: "allenai/ai2_arc"
source: "huggingface"
url: "https://huggingface.co/datasets/allenai/ai2_arc"
downloads: 584397
summary: "초등학교 수준의 과학 객관식 문제 7,787개로 고급 질의응답 연구용 데이터셋입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# allenai/ai2_arc

> dataset · [Hugging Face](https://huggingface.co/datasets/allenai/ai2_arc)

초등학교 수준의 과학 객관식 문제 7,787개로 고급 질의응답 연구용 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories, task_ids = `question-answering` · 신뢰도 high
- **작업**: [[문서 검색]] — ner · readme = `questions answered incorrectly by both a retrieval-based algorithm` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:retrieval = `multiple-choice science questions` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `multiple-choice science questions` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `61` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `grade-school level, multiple-choice science questions` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `A new dataset of 7,787 genuine grade-school level, multiple-choice science questions` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 243자 ≈ 61 토큰 (viewer statistics, ARC-Challenge/validation)

## 이 데이터로 학습한 모델

- [[rico03__Qwopus-GLM-9B-DualReason-Distilled-GGUF|rico03/Qwopus-GLM-9B-DualReason-Distilled-GGUF]]
