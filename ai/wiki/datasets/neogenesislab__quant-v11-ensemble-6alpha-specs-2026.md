---
type: "dataset"
id: "neogenesislab/quant-v11-ensemble-6alpha-specs-2026"
source: "huggingface"
url: "https://huggingface.co/datasets/neogenesislab/quant-v11-ensemble-6alpha-specs-2026"
downloads: 59
summary: "6알파 암호화폐 파생상품 봇의 시스템 설계 및 리스크 엔지니어링 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
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
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# neogenesislab/quant-v11-ensemble-6alpha-specs-2026

> dataset · [Hugging Face](https://huggingface.co/datasets/neogenesislab/quant-v11-ensemble-6alpha-specs-2026)

6알파 암호화폐 파생상품 봇의 시스템 설계 및 리스크 엔지니어링 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `382` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `a 6-alpha cryptocurrency perpetual futures ensemble bot` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is published for research and engineering education.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `section_text` 열 p90 572자 ≈ 382 토큰 (viewer statistics, default/train)
