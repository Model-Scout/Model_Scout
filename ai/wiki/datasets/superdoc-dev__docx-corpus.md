---
type: "dataset"
id: "superdoc-dev/docx-corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/superdoc-dev/docx-corpus"
downloads: 280
summary: "웹에서 수집한 736K개 이상의 .docx 문서를 10개 유형과 9개 주제로 분류한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# superdoc-dev/docx-corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/superdoc-dev/docx-corpus)

웹에서 수집한 736K개 이상의 .docx 문서를 10개 유형과 9개 주제로 분류한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `The largest classified corpus of Word documents. 736K+ `.docx` files` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Each document has been classified by document type and topic` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `20 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `12` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `Topics government, education, healthcare, finance, legal_judicial, technology, environment, nonprofit, general` · 신뢰도 medium
- **도메인**: [[법률]] — ner · readme = `Document Types legal, forms, reports, policies, educational, correspondence, technical, administrative, creative, reference` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `fine-tuned XLM-RoBERTa classifiers applied at scale` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `filename` 열 p90 50자 ≈ 12 토큰 (viewer statistics, default/train)
