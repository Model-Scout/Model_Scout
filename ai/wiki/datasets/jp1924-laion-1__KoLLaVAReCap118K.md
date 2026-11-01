---
type: "dataset"
id: "jp1924-laion-1/KoLLaVAReCap118K"
source: "huggingface"
url: "https://huggingface.co/datasets/jp1924-laion-1/KoLLaVAReCap118K"
downloads: 8
summary: "KoLLaVAReCap118K는 저해상도 노이즈가 있는 시각 지시 튜닝용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jp1924-laion-1/KoLLaVAReCap118K

> dataset · [Hugging Face](https://huggingface.co/datasets/jp1924-laion-1/KoLLaVAReCap118K)

KoLLaVAReCap118K는 저해상도 노이즈가 있는 시각 지시 튜닝용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `LLaVA-NeXT: What Else Influences Visual Instruction Tuning Beyond Data?` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `원본 데이터, 이거 저 해상도라 답변 못하겠음` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `답변 못하겠음 등등의 노이즈 있으니 참고하셈` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `만드는데 3만원 정도 들감` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
