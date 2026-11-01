---
type: "dataset"
id: "DatasetMan/PM4Bench-QGO-Train"
source: "huggingface"
url: "https://huggingface.co/datasets/DatasetMan/PM4Bench-QGO-Train"
downloads: 136
summary: "다국어 OCR 합성 데이터로 QGO 강화학습에 사용하는 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[문서 인식(OCR)]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[cs]]"
  - "[[영어]]"
  - "[[hu]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[sr]]"
  - "[[th]]"
  - "[[vi]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# DatasetMan/PM4Bench-QGO-Train

> dataset · [Hugging Face](https://huggingface.co/datasets/DatasetMan/PM4Bench-QGO-Train)

다국어 OCR 합성 데이터로 QGO 강화학습에 사용하는 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Synthetic multilingual OCR data for QGO reinforcement learning` · 신뢰도 low
- **작업**: [[문서 인식(OCR)]] — tag_match · tags = `ocr` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:ocr, task:visual_qa = `embedded image bytes` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:visual_qa = `prompt, rule-based reward target, answer, split, and auxiliary metadata` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:ocr, task:visual_qa = `prompt, rule-based reward target, answer, split, and auxiliary metadata` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[cs]] — metadata · languages = `cs` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[hu]] — metadata · languages = `hu` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `10 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[sr]] — metadata · languages = `sr` · 신뢰도 high
- **언어**: [[th]] — metadata · languages = `th` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Synthetic multilingual OCR data for QGO reinforcement learning` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The synthetic multilingual OCR corpus contains: - 19,500 training rows - 500 validation rows` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
