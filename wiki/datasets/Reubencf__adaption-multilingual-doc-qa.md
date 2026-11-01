---
type: "dataset"
id: "Reubencf/adaption-multilingual-doc-qa"
source: "huggingface"
url: "https://huggingface.co/datasets/Reubencf/adaption-multilingual-doc-qa"
downloads: 235
summary: "다국어 문서에서 특정 사실 정보를 추출하는 질의응답 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[문서 인식(OCR)]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
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
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Reubencf/adaption-multilingual-doc-qa

> dataset · [Hugging Face](https://huggingface.co/datasets/Reubencf/adaption-multilingual-doc-qa)

다국어 문서에서 특정 사실 정보를 추출하는 질의응답 데이터셋입니다.

## 분류

- **작업**: [[문서 인식(OCR)]] — tag_match · tags = `ocr` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `the dataset also functions as a cross-lingual information retrieval benchmark` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · tags, task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality, task:ocr, task:visual_qa = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:question_answering, task:retrieval, task:visual_qa = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr, task:question_answering, task:visual_qa = `a `completion` providing the precise answer grounded in the source page text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `45 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `923` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multilingual question-answer pairs focused on extracting specific factual details from documents` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `instruction-tuning format with `enhanced_prompt` / `enhanced_completion` / reasoning columns` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `ocr_text` 열 p90 3691자 ≈ 923 토큰 (viewer statistics, default/train)
