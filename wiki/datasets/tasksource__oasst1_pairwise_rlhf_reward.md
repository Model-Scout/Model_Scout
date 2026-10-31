---
type: "dataset"
id: "tasksource/oasst1_pairwise_rlhf_reward"
source: "huggingface"
url: "https://huggingface.co/datasets/tasksource/oasst1_pairwise_rlhf_reward"
downloads: 219
summary: "OASST1 데이터셋을 보상 모델링용으로 전처리한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[리랭킹]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# tasksource/oasst1_pairwise_rlhf_reward

> dataset · [Hugging Face](https://huggingface.co/datasets/tasksource/oasst1_pairwise_rlhf_reward)

OASST1 데이터셋을 보상 모델링용으로 전처리한 데이터셋입니다.

## 분류

- **작업**: [[리랭킹]] — ner · readme = `OASST1 dataset preprocessed for reward modeling` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:reranking = `df=concatenate_datasets(list(dataset.values())).to_pandas()` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `OASST1 dataset preprocessed for reward modeling` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `35 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `468` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `OASST1 dataset preprocessed for reward modeling` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `chosen` 열 p90 1871자 ≈ 468 토큰 (viewer statistics, default/validation)
