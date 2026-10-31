---
type: "dataset"
id: "oahegiaerhg/common_corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/oahegiaerhg/common_corpus"
downloads: 8178
summary: "Common Corpus는 2.27조 토큰 규모의 다양한 공개 라이선스 텍스트 데이터셋으로, AI 학습용으로 활용됩니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[코드 (입력 형식)|코드]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[학술·논문]]"
  - "[[상거래·상품]]"
  - "[[법률]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# oahegiaerhg/common_corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/oahegiaerhg/common_corpus)

Common Corpus는 2.27조 토큰 규모의 다양한 공개 라이선스 텍스트 데이터셋으로, AI 학습용으로 활용됩니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `harmful and toxic content has been removed, and content with low educational content has also been removed` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `each individual document is associated with documented contextual information, including licensed use or lack of copyright` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `Common Corpus is the largest open licensed text dataset, comprising 2.27 trillion tokens` · 신뢰도 low
- **입력 형식**: [[코드 (입력 형식)|코드]] — ner · readme = `283,227,402,898 tokens of high-quality code in open source from GitHub` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:information_extraction, task:language_modeling = `Common Corpus is the largest open licensed text dataset` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `full text, without formatting` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `13 languages` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `94842` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `scientific articles` · 신뢰도 medium
- **도메인**: [[상거래·상품]] — ner · readme = `code` · 신뢰도 low
- **도메인**: [[법률]] — ner · readme = `government and legal documents` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 379370자 ≈ 94842 토큰 (viewer statistics, default/train)
