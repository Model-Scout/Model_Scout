---
type: "dataset"
id: "ONTHEIT/KDoc-OCRBench"
source: "huggingface"
url: "https://huggingface.co/datasets/ONTHEIT/KDoc-OCRBench"
downloads: 15
summary: "한국어 산업 문서 OCR 평가를 위한 7개 카테고리 804개 PDF, 14,738 테스트 케이스 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 인식(OCR)]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
---
# ONTHEIT/KDoc-OCRBench

> dataset · [Hugging Face](https://huggingface.co/datasets/ONTHEIT/KDoc-OCRBench)

한국어 산업 문서 OCR 평가를 위한 7개 카테고리 804개 PDF, 14,738 테스트 케이스 데이터셋입니다.

## 분류

- **작업**: [[문서 인식(OCR)]] — tag_match · readme, tags = `ocr` · 신뢰도 medium
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:ocr = `image` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:ocr = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Existing OCR benchmarks are primarily English-focused, making it difficult to evaluate model performance on Korean documents.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `14,738 test cases across 804 Korean PDFs in 7 industrial document categories — designed to fill the gap in standardized Korean OCR evaluation.` · 신뢰도 medium
