---
type: "dataset"
id: "nmixx-fin/twice_kr_esg_cls"
source: "huggingface"
url: "https://huggingface.co/datasets/nmixx-fin/twice_kr_esg_cls"
downloads: 12
summary: "ESG 키워드가 포함된 한국 금융 뉴스 문장을 환경, 사회, 지배구조, 비ESG로 분류한 데이터셋입니다."
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
  - "[[비상업 전용]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# nmixx-fin/twice_kr_esg_cls

> dataset · [Hugging Face](https://huggingface.co/datasets/nmixx-fin/twice_kr_esg_cls)

ESG 키워드가 포함된 한국 금융 뉴스 문장을 환경, 사회, 지배구조, 비ESG로 분류한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Classified financial news sentences into E (Environmental) /S (Social) / G (Governance)/ Non-ESG categories.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Classified financial news sentences into E (Environmental) /S (Social) / G (Governance)/ Non-ESG categories.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `81` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Classified financial news sentences into E (Environmental) /S (Social) / G (Governance)/ Non-ESG categories.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 121자 ≈ 81 토큰 (viewer statistics, default/train)
