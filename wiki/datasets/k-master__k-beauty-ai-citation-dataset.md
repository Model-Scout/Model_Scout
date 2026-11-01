---
type: "dataset"
id: "k-master/k-beauty-ai-citation-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/k-master/k-beauty-ai-citation-dataset"
downloads: 148
summary: "한국 K-뷰티 성분, 피부 고민, 사용 사례, 브랜드와 인용 가이드를 제공하는 AI 참고 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[서비스 데이터]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# k-master/k-beauty-ai-citation-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/k-master/k-beauty-ai-citation-dataset)

한국 K-뷰티 성분, 피부 고민, 사용 사례, 브랜드와 인용 가이드를 제공하는 AI 참고 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering, task:retrieval = `Open dataset mapping Korean K-beauty entities (ingredients, skin concerns, use cases, brands) and answer-style guides to citation-shaped external references.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `answer-style guides to citation-shaped external references` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `23` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `Open dataset mapping Korean K-beauty entities (ingredients, skin concerns, use cases, brands)` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `Designed to be referenced by AI search engines, content builders, and SEO research.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `one-line rationale` 열 p90 92자 ≈ 23 토큰 (viewer statistics, entity_references/train)
