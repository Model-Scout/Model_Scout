---
type: "dataset"
id: "ahmedheakl/docatlas_instruct"
source: "huggingface"
url: "https://huggingface.co/datasets/ahmedheakl/docatlas_instruct"
downloads: 2099
summary: "DocAtlas는 82개 언어의 다국어 문서 OCR 데이터셋으로 문서 이해 학습에 사용됩니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[정보 추출]]"
  - "[[문서 인식(OCR)]]"
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
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ahmedheakl/docatlas_instruct

> dataset · [Hugging Face](https://huggingface.co/datasets/ahmedheakl/docatlas_instruct)

DocAtlas는 82개 언어의 다국어 문서 OCR 데이터셋으로 문서 이해 학습에 사용됩니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `This dataset powers the training of DocAtlas-DeepSeek` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `It provides precise structural annotations in a unified DocTag format encoding layout, text, and component types` · 신뢰도 low
- **작업**: [[문서 인식(OCR)]] — metadata · tags, task_categories = `document-question-answering` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:ocr, task:visual_qa = `Rendered page image (the document page as seen by the model)` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:information_extraction, task:visual_qa = `Full page content converted to Markdown, preserving headings, tables, lists, and inline formatting` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:ocr, task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `89 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `4661` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `DocAtlas is a large-scale, high-fidelity multilingual OCR dataset covering 82 languages and 10 writing systems` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset powers the training of DocAtlas-DeepSeek` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `doctags` 열 p90 18644자 ≈ 4661 토큰 (viewer statistics, default/train)
