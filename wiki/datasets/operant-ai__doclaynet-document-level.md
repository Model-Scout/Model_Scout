---
type: "dataset"
id: "operant-ai/doclaynet-document-level"
source: "huggingface"
url: "https://huggingface.co/datasets/operant-ai/doclaynet-document-level"
downloads: 124
summary: "DocLayNet 문서 단위 재구성 데이터셋으로 문서 분류 및 텍스트 분석에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# operant-ai/doclaynet-document-level

> dataset · [Hugging Face](https://huggingface.co/datasets/operant-ai/doclaynet-document-level)

DocLayNet 문서 단위 재구성 데이터셋으로 문서 분류 및 텍스트 분석에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `The expanded config uses `document_category` as its classification label.` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Every retained `expanded` row has its complete extracted text embedded in the `text` column and uses `content_mode="embedded_text"`.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The expanded config uses `document_category` as its classification label.` · 신뢰도 low
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `6 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `9` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `It combines reconstructed DocLayNet documents with clinical protocols, historical newspapers, charity reports, court decisions, synthetic financial and PII docu` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Train: 2,355 documents / 60,810 pages` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `original_filename` 열 p90 35자 ≈ 9 토큰 (viewer statistics, default/validation)
