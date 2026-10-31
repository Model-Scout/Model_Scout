---
type: "dataset"
id: "youjunhyeok/SkunkworksAI-reasoning-0.01-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/youjunhyeok/SkunkworksAI-reasoning-0.01-ko"
downloads: 34
summary: "다양한 작업을 위한 추론 체인 합성 데이터셋으로 추론 모델 개발에 활용됩니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
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
  - "[[중규모 데이터]]"
---
# youjunhyeok/SkunkworksAI-reasoning-0.01-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/youjunhyeok/SkunkworksAI-reasoning-0.01-ko)

다양한 작업을 위한 추론 체인 합성 데이터셋으로 추론 모델 개발에 활용됩니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `synthetic dataset of reasoning chains for a wide variety of tasks.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `synthetic dataset of reasoning chains for a wide variety of tasks.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1363` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `synthetic dataset of reasoning chains for a wide variety of tasks.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `we leverage data like this across multiple reasoning experiments/projects.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `reasoning` 열 p90 2045자 ≈ 1363 토큰 (viewer statistics, default/train)
