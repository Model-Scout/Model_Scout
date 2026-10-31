---
type: "dataset"
id: "allenai/winogrande"
source: "huggingface"
url: "https://huggingface.co/datasets/allenai/winogrande"
downloads: 235017
summary: "WinoGrande는 상식 추론을 위한 44,000개 문제로 구성된 데이터셋입니다."
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
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# allenai/winogrande

> dataset · [Hugging Face](https://huggingface.co/datasets/allenai/winogrande)

WinoGrande는 상식 추론을 위한 44,000개 문제로 구성된 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `Formulated as a fill-in-a-blank task with binary options, the goal is to choose the right option for a given sentence which requires commonsense reasoning.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `Formulated as a fill-in-a-blank task with binary options` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `the goal is to choose the right option for a given sentence` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `31` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `WinoGrande is a new collection of 44k problems, inspired by Winograd Schema Challenge` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `WinoGrande is a new collection of 44k problems` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `sentence` 열 p90 126자 ≈ 31 토큰 (viewer statistics, winogrande_debiased/validation)
