---
type: "dataset"
id: "pufanyi/MIMICIT"
source: "huggingface"
url: "https://huggingface.co/datasets/pufanyi/MIMICIT"
downloads: 667
summary: "MIMIC-IT는 280만 멀티모달 지시-응답 쌍으로 VLM 성능 향상을 위한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# pufanyi/MIMICIT

> dataset · [Hugging Face](https://huggingface.co/datasets/pufanyi/MIMICIT)

MIMIC-IT는 280만 멀티모달 지시-응답 쌍으로 VLM 성능 향상을 위한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `MIMIC-IT offers a diverse and extensive dataset of 2.8M multimodal instruction-response pairs, designed to enhance the performance of Vision-Language Models (VL` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `MIMIC-IT enables the application of egocentric visual assistant model that can serve that can answer your questions like **Hey, Do you think I left my keys on t` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `images in base64 format` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `instruction-response pairs` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `instruction-response pairs` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `7 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MIMIC-IT provides multilingual instructions, supporting English, Chinese, Korean, Japanese, German, French, Spanish, and Arabic` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `MIMIC-IT offers a diverse and extensive dataset of 2.8M multimodal instruction-response pairs` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
