---
type: "dataset"
id: "rileykim/MMDoc"
source: "huggingface"
url: "https://huggingface.co/datasets/rileykim/MMDoc"
downloads: 193
summary: "MMDoc는 10개 언어쌍의 문서 이미지와 OCR 결과를 포함한 다국어 문서 번역 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[정보 추출]]"
  - "[[문서 인식(OCR)]]"
  - "[[번역]]"
  - "[[이미지 인식]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[id]]"
  - "[[일본어]]"
  - "[[kk]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[ur]]"
  - "[[uz]]"
  - "[[vi]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# rileykim/MMDoc

> dataset · [Hugging Face](https://huggingface.co/datasets/rileykim/MMDoc)

MMDoc는 10개 언어쌍의 문서 이미지와 OCR 결과를 포함한 다국어 문서 번역 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `OCR results with bounding boxes and extracted text` · 신뢰도 low
- **작업**: [[문서 인식(OCR)]] — tag_match · tags = `ocr` · 신뢰도 low
- **작업**: [[번역]] — tag_match · readme, tags = `translation` · 신뢰도 medium
- **작업**: [[이미지 인식]] — tag_match · tags = `vision` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · readme, task:ocr = `document images` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:ocr, task:vision, task:visual_qa = `real-world document images` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction, task:translation, task:visual_qa = `OCR results and translations` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr, task:translation, task:visual_qa = `target language text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[id]] — metadata · languages = `id` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[kk]] — metadata · languages = `kk` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `10 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[ur]] — metadata · languages = `ur` · 신뢰도 high
- **언어**: [[uz]] — metadata · languages = `uz` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Multilingual Multimodal Document Translation Dataset` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
