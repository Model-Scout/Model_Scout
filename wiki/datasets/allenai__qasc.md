---
type: "dataset"
id: "allenai/qasc"
source: "huggingface"
url: "https://huggingface.co/datasets/allenai/qasc"
downloads: 41688
summary: "QASC는 초등 과학 8지선다형 질문과 1700만 문장 말뭉치로 구성된 질의응답 데이터셋입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[질의응답]]"
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
# allenai/qasc

> dataset · [Hugging Face](https://huggingface.co/datasets/allenai/qasc)

QASC는 초등 과학 8지선다형 질문과 1700만 문장 말뭉치로 구성된 질의응답 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories, task_ids = `multiple-choice` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `a corpus of 17M sentences` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `8-way multiple-choice questions` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `58` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `about grade school science` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `8,134 train, 926 dev, 920 test` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `formatted_question` 열 p90 233자 ≈ 58 토큰 (viewer statistics, default/validation)

## 이 데이터로 학습한 모델

- [[blackmallangcow__nari-decision-4b|blackmallangcow/nari-decision-4b]]
