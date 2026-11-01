---
type: "dataset"
id: "aldente0630/LLaVA-Pretrain-Ko"
source: "huggingface"
url: "https://huggingface.co/datasets/aldente0630/LLaVA-Pretrain-Ko"
downloads: 15
summary: "LLaVA 모델 사전 훈련용 한국어 비전 인스트럭트 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# aldente0630/LLaVA-Pretrain-Ko

> dataset · [Hugging Face](https://huggingface.co/datasets/aldente0630/LLaVA-Pretrain-Ko)

LLaVA 모델 사전 훈련용 한국어 비전 인스트럭트 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `LLaVA 모델의 사전 훈련을 위해 제작한 LLaVA-Pretrain 데이터셋의 한국어 버전입니다.` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:visual_qa = `사용한 이미지-투-텍스트 모델: Claude 3 Haiku` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:visual_qa = `LLaVA 모델의 사전 훈련을 위해 제작한 LLaVA-Pretrain 데이터셋의 한국어 버전입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:visual_qa = `LLaVA 모델의 사전 훈련을 위해 제작한 LLaVA-Pretrain 데이터셋의 한국어 버전입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `LLaVA 모델의 사전 훈련을 위해 제작한 LLaVA-Pretrain 데이터셋의 한국어 버전입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `LLaVA 모델의 사전 훈련을 위해 제작한 LLaVA-Pretrain 데이터셋의 한국어 버전입니다.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
