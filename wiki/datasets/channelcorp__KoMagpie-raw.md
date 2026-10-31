---
type: "dataset"
id: "channelcorp/KoMagpie-raw"
source: "huggingface"
url: "https://huggingface.co/datasets/channelcorp/KoMagpie-raw"
downloads: 127
summary: "KoMagpie-raw는 한국어 지침-응답 데이터셋으로, 마케팅 등 다양한 분야의 질의응답에 활용됩니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# channelcorp/KoMagpie-raw

> dataset · [Hugging Face](https://huggingface.co/datasets/channelcorp/KoMagpie-raw)

KoMagpie-raw는 한국어 지침-응답 데이터셋으로, 마케팅 등 다양한 분야의 질의응답에 활용됩니다.

## 분류

- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme = `features: ['instruction', 'output', 'model']` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `features: ['instruction', 'output', 'model']` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `629` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 944자 ≈ 629 토큰 (viewer statistics, default/train)
