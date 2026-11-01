---
type: "dataset"
id: "amphora/korfin-asc"
source: "huggingface"
url: "https://huggingface.co/datasets/amphora/korfin-asc"
downloads: 104
summary: "KorFin-ASC는 금융 분야 문장의 측면 기반 감성 분류를 위한 (aspect, polarity) 쌍이 주석된 데이터셋입니다."
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
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# amphora/korfin-asc

> dataset · [Hugging Face](https://huggingface.co/datasets/amphora/korfin-asc)

KorFin-ASC는 금융 분야 문장의 측면 기반 감성 분류를 위한 (aspect, polarity) 쌍이 주석된 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, tags, task_categories, task_ids = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Each instance consists of a single sentence, aspect, and corresponding polarity (POSITIVE/NEGATIVE/NEUTRAL).` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Each instance consists of a single sentence, aspect, and corresponding polarity (POSITIVE/NEGATIVE/NEUTRAL).` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `90` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The KorFin-ASC is an extension of KorFin-ABSA including 8818 samples with (aspect, polarity) pairs annotated.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `SRC` 열 p90 135자 ≈ 90 토큰 (viewer statistics, default/train)
