---
type: "dataset"
id: "hac541309/woori_spring_dict"
source: "huggingface"
url: "https://huggingface.co/datasets/hac541309/woori_spring_dict"
downloads: 71
summary: "우리말샘 한국어 오픈소스 사전을 학습 가능한 형태로 처리한 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
  - "[[질의응답]]"
  - "[[표 질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# hac541309/woori_spring_dict

> dataset · [Hugging Face](https://huggingface.co/datasets/hac541309/woori_spring_dict)

우리말샘 한국어 오픈소스 사전을 학습 가능한 형태로 처리한 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `This dataset is a NLP learnable form of woori mal saem(우리말샘) a Korean collaborative open source dictionary.` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[표 질의응답]] — metadata · task_categories = `table-question-answering` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:table_qa = `table` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:language_modeling, task:question_answering, task:table_qa = `This dataset is a NLP learnable form of woori mal saem(우리말샘) a Korean collaborative open source dictionary.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling, task:question_answering, task:table_qa = `This dataset is a NLP learnable form of woori mal saem(우리말샘) a Korean collaborative open source dictionary.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `830` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-3.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a Korean collaborative open source dictionary.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is a NLP learnable form of woori mal saem(우리말샘)` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 1244자 ≈ 830 토큰 (viewer statistics, default/train)
