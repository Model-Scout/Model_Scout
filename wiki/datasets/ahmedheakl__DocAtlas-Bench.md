---
type: "dataset"
id: "ahmedheakl/DocAtlas-Bench"
source: "huggingface"
url: "https://huggingface.co/datasets/ahmedheakl/DocAtlas-Bench"
downloads: 272
summary: "DocAtlas-Bench는 82개 언어의 문서 페이지 파싱 평가용 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[문서 인식(OCR)]]"
  - "[[리랭킹]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ahmedheakl/DocAtlas-Bench

> dataset · [Hugging Face](https://huggingface.co/datasets/ahmedheakl/DocAtlas-Bench)

DocAtlas-Bench는 82개 언어의 문서 페이지 파싱 평가용 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Pages are further annotated with page-level attributes such as document type, column layout, watermark presence, and background color` · 신뢰도 low
- **작업**: [[문서 인식(OCR)]] — tag_match · tags = `ocr` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `end-to-end page parsing: text, tables, and reading order` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:ocr, task:visual_qa = `Rendered page image.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:reranking, task:visual_qa = `Page content in Markdown, with tables as HTML.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr, task:visual_qa = `Page content in Markdown, with tables as HTML.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `92 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `10951` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `DocAtlas: Multilingual Document Understanding Across 80+ Languages` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `DocAtlas-Bench is the evaluation benchmark of DocAtlas` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `annotation` 열 p90 43802자 ≈ 10951 토큰 (viewer statistics, default/test)
