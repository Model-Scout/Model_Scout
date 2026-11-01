---
type: "dataset"
id: "Cognitive-Lab/NayanaOCR_Corpus_2025"
source: "huggingface"
url: "https://huggingface.co/datasets/Cognitive-Lab/NayanaOCR_Corpus_2025"
downloads: 8864
summary: "22개 언어로 된 100만 페이지 문서 OCR, 레이아웃 감지, VQA용 병렬 합성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[정보 추출]]"
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
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# Cognitive-Lab/NayanaOCR_Corpus_2025

> dataset · [Hugging Face](https://huggingface.co/datasets/Cognitive-Lab/NayanaOCR_Corpus_2025)

22개 언어로 된 100만 페이지 문서 OCR, 레이아웃 감지, VQA용 병렬 합성 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `training and evaluating OCR, layout detection` · 신뢰도 low
- **작업**: [[문서 인식(OCR)]] — tag_match · readme, tags = `ocr` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_ids = `closed-domain-qa` · 신뢰도 low
- **작업**: [[문서 검색]] — tag_match · tags = `retrieval` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · readme, tags, task_categories = `image-text-to-text` · 신뢰도 high
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:ocr, task:visual_qa = `Image + Text (+ structured JSON)` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction, task:question_answering, task:retrieval, task:visual_qa = `Image + Text (+ structured JSON)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr, task:question_answering, task:visual_qa = `English ground-truth, in-language translations, and synthetic VQA pairs (descriptive + multiple-choice)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `22 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `6` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `document-centric vision-language models` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = ``train` only (use the data as a pretraining / SFT corpus)` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `image_id.txt` 열 p90 23자 ≈ 6 토큰 (viewer statistics, ko/train)

## 같은 데이터의 사본·중복 등록

- `1DuBu1/NayanaOCR_Corpus_2025`
