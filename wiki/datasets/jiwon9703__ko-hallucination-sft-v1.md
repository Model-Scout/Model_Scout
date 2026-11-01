---
type: "dataset"
id: "jiwon9703/ko-hallucination-sft-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/jiwon9703/ko-hallucination-sft-v1"
downloads: 20
summary: "한국어 할루시네이션 분류 데이터셋으로, 모델 응답의 할루시네이션 유형을 분류하는 데 사용됩니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
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
# jiwon9703/ko-hallucination-sft-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/jiwon9703/ko-hallucination-sft-v1)

한국어 할루시네이션 분류 데이터셋으로, 모델 응답의 할루시네이션 유형을 분류하는 데 사용됩니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = ``label`: 할루시네이션 타입 레이블` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 할루시네이션 분류 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `이 데이터셋은 다음 소스들을 결합하여 구성되었습니다` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
