---
type: "dataset"
id: "dbdu/ShareGPT-74k-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/dbdu/ShareGPT-74k-ko"
downloads: 116
summary: "ShareGPT-90k의 한국어 번역 데이터셋으로, 대화 데이터 학습에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
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
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# dbdu/ShareGPT-74k-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/dbdu/ShareGPT-74k-ko)

ShareGPT-90k의 한국어 번역 데이터셋으로, 대화 데이터 학습에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `json 파일의 구조는 원본 데이터셋과 동일합니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `json 파일의 구조는 원본 데이터셋과 동일합니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean-translated version of ShareGPT-90k` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `ShareGPT 90k의 cleaned 버전을 구글 번역기를 이용하여 번역하였습니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[heegyu__llama-2-ko-7b-chat|heegyu/llama-2-ko-7b-chat]]
