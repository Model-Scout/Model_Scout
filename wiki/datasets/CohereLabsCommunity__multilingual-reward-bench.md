---
type: "dataset"
id: "CohereLabsCommunity/multilingual-reward-bench"
source: "huggingface"
url: "https://huggingface.co/datasets/CohereLabsCommunity/multilingual-reward-bench"
downloads: 1838
summary: "23개 언어로 번역된 보상 모델 평가용 다국어 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[리랭킹]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# CohereLabsCommunity/multilingual-reward-bench

> dataset · [Hugging Face](https://huggingface.co/datasets/CohereLabsCommunity/multilingual-reward-bench)

23개 언어로 번역된 보상 모델 평가용 다국어 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `RewardBench category an instance belongs to (Chat, Chat-Hard, Safety, Reasoning)` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `M-RewardBench contains prompt-chosen-rejected preference triples` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:reranking = `~2.87k text samples from RewardBench, translated to 23 other languages.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `chosen : human-validated chosen response in the original RewardBench dataset` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `22 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `260` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Reward models (RMs) have driven the development of state-of-the-art LLMs today, with unprecedented impact across the globe.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `M-RewardBench, a benchmark for 23 typologically diverse languages.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `rejected` 열 p90 1042자 ≈ 260 토큰 (viewer statistics, kor_Hang/test)
