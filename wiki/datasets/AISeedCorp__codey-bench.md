---
type: "dataset"
id: "AISeedCorp/codey-bench"
source: "huggingface"
url: "https://huggingface.co/datasets/AISeedCorp/codey-bench"
downloads: 54
summary: "웹페이지 제품 기획서(브리프)를 받아 구조화된 디자인 문서(CDD)를 생성하는 데이터셋입니다."
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
  - "[[장문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# AISeedCorp/codey-bench

> dataset · [Hugging Face](https://huggingface.co/datasets/AISeedCorp/codey-bench)

웹페이지 제품 기획서(브리프)를 받아 구조화된 디자인 문서(CDD)를 생성하는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Each row is a product brief for a web page (Markdown)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `must produce one Codey Design Document (CDD) as JSON` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `5964` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `Each row is a product brief for a web page` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Each row is a product brief for a web page (Markdown). The model receives the brief and must produce one Codey Design Document (CDD) as JSON` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `reference` 열 p90 8946자 ≈ 5964 토큰 (viewer statistics, ko/test)
