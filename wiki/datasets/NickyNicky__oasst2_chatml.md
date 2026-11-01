---
type: "dataset"
id: "NickyNicky/oasst2_chatml"
source: "huggingface"
url: "https://huggingface.co/datasets/NickyNicky/oasst2_chatml"
downloads: 33
summary: "다국어 채팅 메시지 데이터셋으로 대화 모델 학습에 활용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
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
# NickyNicky/oasst2_chatml

> dataset · [Hugging Face](https://huggingface.co/datasets/NickyNicky/oasst2_chatml)

다국어 채팅 메시지 데이터셋으로 대화 모델 학습에 활용됨

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `NickyNicky/oasst2_chatml
Message counts by language` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Message counts by language` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Message counts by language` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `26 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1213` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Message counts by language` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `NickyNicky/oasst2_chatml
Message counts by language` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `Text` 열 p90 4853자 ≈ 1213 토큰 (viewer statistics, default/train)
