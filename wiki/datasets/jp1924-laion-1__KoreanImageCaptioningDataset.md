---
type: "dataset"
id: "jp1924-laion-1/KoreanImageCaptioningDataset"
source: "huggingface"
url: "https://huggingface.co/datasets/jp1924-laion-1/KoreanImageCaptioningDataset"
downloads: 10
summary: "한국어 이미지 캡션 데이터셋으로 이미지와 캡션 학습에 사용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[이미지 생성]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jp1924-laion-1/KoreanImageCaptioningDataset

> dataset · [Hugging Face](https://huggingface.co/datasets/jp1924-laion-1/KoreanImageCaptioningDataset)

한국어 이미지 캡션 데이터셋으로 이미지와 캡션 학습에 사용됨

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `caption` · 신뢰도 low
- **작업**: [[이미지 생성]] — ner · readme = `image` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:image_generation = `- name: image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation, task:image_generation = `text` · 신뢰도 high
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — task_rule · task:image_generation = `image` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `- name: caption` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `- name: validation` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `- name: train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
