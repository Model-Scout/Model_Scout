---
type: "dataset"
id: "trillionlabs/MWMBench"
source: "huggingface"
url: "https://huggingface.co/datasets/trillionlabs/MWMBench"
downloads: 138
summary: "MWMBench는 모바일 앱 GUI 세계 모델의 다음 화면 예측 성능을 평가하는 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# trillionlabs/MWMBench

> dataset · [Hugging Face](https://huggingface.co/datasets/trillionlabs/MWMBench)

MWMBench는 모바일 앱 GUI 세계 모델의 다음 화면 예측 성능을 평가하는 벤치마크입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `MWMBench is a benchmark for evaluating GUI world models (next-screen prediction) on mobile apps.` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-text-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:visual_qa = `Given the current screenshot and an action in a real-world coordinate action space, a world model must predict the next screen.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation, task:visual_qa = `text` · 신뢰도 high
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme = `Given the current screenshot and an action in a real-world coordinate action space, a world model must predict the next screen.` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `39` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MWMBench is a benchmark for evaluating GUI world models (next-screen prediction) on mobile apps.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `MWMBench is a benchmark for evaluating GUI world models (next-screen prediction) on mobile apps.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `next_image` 열 p90 58자 ≈ 39 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[trillionlabs__gWorld-32B|trillionlabs/gWorld-32B]]
- [[trillionlabs__gWorld-8B|trillionlabs/gWorld-8B]]
