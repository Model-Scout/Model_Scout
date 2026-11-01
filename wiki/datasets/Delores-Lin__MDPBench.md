---
type: "dataset"
id: "Delores-Lin/MDPBench"
source: "huggingface"
url: "https://huggingface.co/datasets/Delores-Lin/MDPBench"
downloads: 1962
summary: "MDPBench는 17개 언어의 디지털 및 사진 문서 파싱 성능 평가용 다국어 문서 파싱 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
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
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
---
# Delores-Lin/MDPBench

> dataset · [Hugging Face](https://huggingface.co/datasets/Delores-Lin/MDPBench)

MDPBench는 17개 언어의 디지털 및 사진 문서 파싱 성능 평가용 다국어 문서 파싱 벤치마크입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `evaluate how models perform on digital and photographed documents across diverse scripts and low-resource languages` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `the first benchmark for multilingual digital and photographed document parsing` · 신뢰도 low
- **작업**: [[문서 인식(OCR)]] — tag_match · tags = `ocr` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — metadata · modality, task:ocr = `document` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:ocr, task:visual_qa = `3,400 document images spanning 17 languages` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:information_extraction, task:visual_qa = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr, task:visual_qa = `high-quality annotations produced through a rigorous pipeline of expert model labeling, manual correction, and human verification` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `16 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multilingual digital and photographed document parsing` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `separate public and private evaluation splits` · 신뢰도 medium
