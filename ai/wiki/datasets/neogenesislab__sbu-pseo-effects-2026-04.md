---
type: "dataset"
id: "neogenesislab/sbu-pseo-effects-2026-04"
source: "huggingface"
url: "https://huggingface.co/datasets/neogenesislab/sbu-pseo-effects-2026-04"
downloads: 47
summary: "1인 AI 기업이 운영하는 6개 프로그램형 SEO SBU의 운영 데이터셋으로, 콘텐츠 운영과 마케팅 자동화 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# neogenesislab/sbu-pseo-effects-2026-04

> dataset · [Hugging Face](https://huggingface.co/datasets/neogenesislab/sbu-pseo-effects-2026-04)

1인 AI 기업이 운영하는 6개 프로그램형 SEO SBU의 운영 데이터셋으로, 콘텐츠 운영과 마케팅 자동화 연구에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — metadata · task_categories = `tabular-classification` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · modality, readme, task:tabular_prediction = `35 per-SBU-per-snapshot rows` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification = `text` · 신뢰도 high
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `35 per-SBU-per-snapshot rows` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `multi-tenant blogs that one founder operates with AI agents` · 신뢰도 low
- **도메인**: [[일반]] — ner · readme = `programmatic-SEO content ops actually behave on a live, autonomously-managed multi-blog network` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
