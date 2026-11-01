---
type: "dataset"
id: "Nexdata-kr/5711-Images-Korean-Handwriting-OCR-Dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/Nexdata-kr/5711-Images-Korean-Handwriting-OCR-Dataset"
downloads: 84
summary: "5,711장 한국어 손글씨 OCR 데이터셋으로 다양한 용지에 작성된 텍스트 인식용입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[문서 인식(OCR)]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Nexdata-kr/5711-Images-Korean-Handwriting-OCR-Dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/Nexdata-kr/5711-Images-Korean-Handwriting-OCR-Dataset)

5,711장 한국어 손글씨 OCR 데이터셋으로 다양한 용지에 작성된 텍스트 인식용입니다.

## 분류

- **작업**: [[문서 인식(OCR)]] — ner · readme = `한국어 손글씨 OCR 인식 및 관련 AI 모델 학습에 활용할 수 있습니다.` · 신뢰도 medium
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:ocr = `5,711장의 한국어 손글씨 OCR 데이터셋으로, A4 용지, 줄노트, 모눈종이 등 다양한 형태의 용지에 작성된 한국어 손글씨 데이터를 포함하고 있습니다.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr = `어노테이션은 텍스트 라인 단위의 사각형 영역과 라인 단위 텍스트 전사로 구성되어 있습니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 손글씨 데이터를 포함하고 있습니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `본 데이터셋은 한국어 손글씨 OCR 인식 및 관련 AI 모델 학습에 활용할 수 있습니다.` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
