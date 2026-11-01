---
type: "dataset"
id: "thunder-research-group/SNU_Ko-EQ-Bench"
source: "huggingface"
url: "https://huggingface.co/datasets/thunder-research-group/SNU_Ko-EQ-Bench"
downloads: 59
summary: "Ko-EQ-Bench는 한국어 대화에서 감정 강도를 예측하는 감성 지능 평가 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# thunder-research-group/SNU_Ko-EQ-Bench

> dataset · [Hugging Face](https://huggingface.co/datasets/thunder-research-group/SNU_Ko-EQ-Bench)

Ko-EQ-Bench는 한국어 대화에서 감정 강도를 예측하는 감성 지능 평가 벤치마크입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `**Task**: Emotion Recognition and Intensity Prediction` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `The benchmark consists of fictional and realistic Korean dialogues featuring interpersonal conflict or tension, followed by a prompt instructing the model to sc` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `It evaluates a model's ability to interpret emotions in dialogue by predicting the relative intensity of several possible emotional responses of a character.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Ko-EQ-Bench is a Korean adaptation of EQ-Bench, a benchmark designed to assess the emotional intelligence of large language models.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `Evaluation code and task configurations for this benchmark are available` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
