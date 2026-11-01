---
type: "dataset"
id: "Nexdata-kr/104320-Images-Korean-and-Hindi-OCR-Data-in-Natural-Scenes"
source: "huggingface"
url: "https://huggingface.co/datasets/Nexdata-kr/104320-Images-Korean-and-Hindi-OCR-Data-in-Natural-Scenes"
downloads: 39
summary: "한국어 및 힌디어 자연 환경 OCR 데이터셋으로 텍스트 인식에 활용됩니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_with_others"
task:
  - "[[문서 인식(OCR)]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[hi]]"
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
# Nexdata-kr/104320-Images-Korean-and-Hindi-OCR-Data-in-Natural-Scenes

> dataset · [Hugging Face](https://huggingface.co/datasets/Nexdata-kr/104320-Images-Korean-and-Hindi-OCR-Data-in-Natural-Scenes)

한국어 및 힌디어 자연 환경 OCR 데이터셋으로 텍스트 인식에 활용됩니다.

## 분류

- **작업**: [[문서 인식(OCR)]] — ner · readme = `본 데이터셋은 자연 환경에서의 한국어 및 힌디어 OCR 작업에 활용할 수 있습니다.` · 신뢰도 medium
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:ocr = `104,320장 규모의 한국어 및 힌디어 자연 환경 OCR 데이터셋입니다.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr = `어노테이션은 텍스트의 행 단위 폴리곤 바운딩 박스(또는 사각형/직사각형 바운딩 박스), 전사 및 텍스트 속성(언어 유형) 정보를 포함하며` · 신뢰도 medium
- **언어**: [[hi]] — metadata · languages = `hi` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `104,320장 규모의 한국어 및 힌디어 자연 환경 OCR 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `본 데이터셋은 자연 환경에서의 한국어 및 힌디어 OCR 작업에 활용할 수 있습니다.` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
