---
type: "dataset"
id: "arthrod/docx-corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/arthrod/docx-corpus"
downloads: 94
summary: "공개 웹에서 수집한 736K개 이상의 .docx 문서 메타데이터로 문서 유형과 주제 분류에 활용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[문서 검색]]"
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
  - "[[일반]]"
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# arthrod/docx-corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/arthrod/docx-corpus)

공개 웹에서 수집한 736K개 이상의 .docx 문서 메타데이터로 문서 유형과 주제 분류에 활용됨

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `Each row includes a `url` column pointing to the `.docx` file on the upstream CDN. You can download files directly` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:retrieval = `The largest classified corpus of Word documents. 736K+ `.docx` files` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `classification labels` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `21 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `12` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `public web, classified into 10 document types and 9 topics across 76 languages` · 신뢰도 medium
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `classification labels + download URL` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `filename` 열 p90 50자 ≈ 12 토큰 (viewer statistics, default/train)
