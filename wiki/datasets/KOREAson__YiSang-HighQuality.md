---
type: "dataset"
id: "KOREAson/YiSang-HighQuality"
source: "huggingface"
url: "https://huggingface.co/datasets/KOREAson/YiSang-HighQuality"
downloads: 108
summary: "YiSang-HighQuality는 영어와 한국어 혼합 체인 오브 사고(CoT) 추론 데이터셋으로 다국어 추론 향상에 사용됨."
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
  - "[[초장문]]"
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
# KOREAson/YiSang-HighQuality

> dataset · [Hugging Face](https://huggingface.co/datasets/KOREAson/YiSang-HighQuality)

YiSang-HighQuality는 영어와 한국어 혼합 체인 오브 사고(CoT) 추론 데이터셋으로 다국어 추론 향상에 사용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Language-Mixed Chain-of-Thought (CoT), which switches between English and Korean` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `long-CoT reasoning traces` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `21022` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `designed to enhance multilingual reasoning through Language-Mixed Chain-of-Thought (CoT)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This is the dataset used to train our KOREAson-0831 and 1009 series.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `response` 열 p90 31533자 ≈ 21022 토큰 (viewer statistics, default/train)
