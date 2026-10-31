---
type: "dataset"
id: "posicube/KolmOCR-traindataset"
source: "huggingface"
url: "https://huggingface.co/datasets/posicube/KolmOCR-traindataset"
downloads: 753
summary: "KolmOCR Training Dataset은 한국어 번역된 문서 OCR 및 문서 이해 모델 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
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
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# posicube/KolmOCR-traindataset

> dataset · [Hugging Face](https://huggingface.co/datasets/posicube/KolmOCR-traindataset)

KolmOCR Training Dataset은 한국어 번역된 문서 OCR 및 문서 이해 모델 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `각 샘플에는 구조화된 JSON 메타데이터와 bounding box 정보가 포함된 markdown 문서가 포함합니다.` · 신뢰도 low
- **작업**: [[문서 인식(OCR)]] — tag_match · tags = `ocr` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · readme, task:ocr = `PDF 및 PNG 렌더링을 활용하여 만들어진 markdown 생성 모델 학습용 데이터셋입니다.` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:ocr, task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:information_extraction, task:visual_qa = `각 샘플에는 구조화된 JSON 메타데이터와 bounding box 정보가 포함된 markdown 문서가 포함합니다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:ocr, task:visual_qa = `markdown 생성 모델 학습용 데이터셋입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `도서 콘텐츠` · 신뢰도 low
- **도메인**: [[일반]] — ner · readme = `일반 문서` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `markdown 생성 모델 학습용 데이터셋입니다.` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
