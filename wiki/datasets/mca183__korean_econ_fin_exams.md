---
type: "dataset"
id: "mca183/korean_econ_fin_exams"
source: "huggingface"
url: "https://huggingface.co/datasets/mca183/korean_econ_fin_exams"
downloads: 49
summary: "한국어 경제·금융 시험 문제 데이터셋으로 질의응답, 분류, 언어 모델링에 활용 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[언어 모델링]]"
  - "[[질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# mca183/korean_econ_fin_exams

> dataset · [Hugging Face](https://huggingface.co/datasets/mca183/korean_econ_fin_exams)

한국어 경제·금융 시험 문제 데이터셋으로 질의응답, 분류, 언어 모델링에 활용 가능

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `text classification` · 신뢰도 medium
- **작업**: [[언어 모델링]] — ner · readme = `language modeling` · 신뢰도 medium
- **작업**: [[질의응답]] — ner · readme = `natural language processing (NLP) tasks such as question answering` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:language_modeling, task:question_answering = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:language_modeling, task:question_answering = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `47` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `Korean economic and financial exams` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains a collection of Korean economic and financial exams, providing a valuable resource for natural language processing (NLP) tasks` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 71자 ≈ 47 토큰 (viewer statistics, default/train)
