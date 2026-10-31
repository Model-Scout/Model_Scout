---
type: "dataset"
id: "coastral/korean-writing-style-instruct"
source: "huggingface"
url: "https://huggingface.co/datasets/coastral/korean-writing-style-instruct"
downloads: 102
summary: "여러 분야 문체를 포함한 한국어 문체 인스트럭스 튜닝 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# coastral/korean-writing-style-instruct

> dataset · [Hugging Face](https://huggingface.co/datasets/coastral/korean-writing-style-instruct)

여러 분야 문체를 포함한 한국어 문체 인스트럭스 튜닝 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `여러 분야의 문체(문학, 일상적 대화, 고전시가 등)를 포함한 합성 데이터셋입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `모델에게 여러 문체를 출력하는 능력을 가르치기 위해 제작되었습니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `훈련시키실 때, 일반 인스트럭스 데이터셋과 혼용해서 사용하시는 것을 추천드립니다.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
