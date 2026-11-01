---
type: "dataset"
id: "InfoBayAI/Bounding_Box_with_Annotation_Dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/InfoBayAI/Bounding_Box_with_Annotation_Dataset"
downloads: 25
summary: "상점, 간판, 문서 등 다양한 상업 환경 이미지에 바운딩 박스와 객체 클래스 라벨이 포함된 15,000장 이미지 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[문서 인식(OCR)]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[he]]"
  - "[[hi]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[th]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# InfoBayAI/Bounding_Box_with_Annotation_Dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/InfoBayAI/Bounding_Box_with_Annotation_Dataset)

상점, 간판, 문서 등 다양한 상업 환경 이미지에 바운딩 박스와 객체 클래스 라벨이 포함된 15,000장 이미지 데이터셋입니다.

## 분류

- **작업**: [[문서 인식(OCR)]] — tag_match · tags = `document-understanding` · 신뢰도 low
- **작업**: [[이미지 인식]] — metadata · readme, tags, task_categories = `image-classification` · 신뢰도 high
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:ocr, task:vision = `15,000 images with bounding box annotations and object class labels.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr = `bounding box annotations and object class labels` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[he]] — metadata · languages = `he` · 신뢰도 high
- **언어**: [[hi]] — metadata · languages = `hi` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `7 languages` · 신뢰도 high
- **언어**: [[th]] — metadata · languages = `th` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `The dataset is designed to support object detection, visual recognition, scene understanding, and computer vision model development involving commercial environ` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
