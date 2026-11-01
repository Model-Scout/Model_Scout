---
type: "dataset"
id: "ko-vlm/KoLLaVA-v1.5-Instruct-581k"
source: "huggingface"
url: "https://huggingface.co/datasets/ko-vlm/KoLLaVA-v1.5-Instruct-581k"
downloads: 1510
summary: "한국어 Vision-Language 모델 학습용 instruction tuning 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ko-vlm/KoLLaVA-v1.5-Instruct-581k

> dataset · [Hugging Face](https://huggingface.co/datasets/ko-vlm/KoLLaVA-v1.5-Instruct-581k)

한국어 Vision-Language 모델 학습용 instruction tuning 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `한국어 Vision-Language 모델을 위한 instruction tuning 데이터셋입니다.` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `이미지: COCO + GQA + Visual Genome 데이터셋` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `형식: ChatML 형식 (role: user/assistant, content: 텍스트)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `형식: ChatML 형식 (role: user/assistant, content: 텍스트)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 Vision-Language 모델을 위한 instruction tuning 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `한국어 Vision-Language 모델을 위한 instruction tuning 데이터셋입니다.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
