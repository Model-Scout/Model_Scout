---
type: "dataset"
id: "injaeryou/llm-name-identity"
source: "huggingface"
url: "https://huggingface.co/datasets/injaeryou/llm-name-identity"
downloads: 51
summary: "AI에 맞춤형 모델명과 팀 정체성을 부여하기 위한 학습 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# injaeryou/llm-name-identity

> dataset · [Hugging Face](https://huggingface.co/datasets/injaeryou/llm-name-identity)

AI에 맞춤형 모델명과 팀 정체성을 부여하기 위한 학습 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Train Dataset for assigning a custom model name and team identity to the AI.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `my_ds = ds.map(lambda x: {"output": x["output"].replace("{{model_name}}", my_model_name).replace("{{team_name}}", my_team_name` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `my_ds = ds.map(lambda x: {"output": x["output"].replace("{{model_name}}", my_model_name).replace("{{team_name}}", my_team_name` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `40` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Train Dataset for assigning a custom model name and team identity to the AI.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 60자 ≈ 40 토큰 (viewer statistics, ko/train)
