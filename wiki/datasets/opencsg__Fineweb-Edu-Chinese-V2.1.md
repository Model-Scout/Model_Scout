---
type: "dataset"
id: "opencsg/Fineweb-Edu-Chinese-V2.1"
source: "huggingface"
url: "https://huggingface.co/datasets/opencsg/Fineweb-Edu-Chinese-V2.1"
downloads: 40964
summary: "교육 분야 자연어처리용 중국어 데이터셋으로, 점수별 데이터 선택 학습 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# opencsg/Fineweb-Edu-Chinese-V2.1

> dataset · [Hugging Face](https://huggingface.co/datasets/opencsg/Fineweb-Edu-Chinese-V2.1)

교육 분야 자연어처리용 중국어 데이터셋으로, 점수별 데이터 선택 학습 가능

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `designed specifically for natural language processing (NLP) tasks in the education sector` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `approximately 930 billion tokens` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `high-quality educational content with clear and coherent writing` · 신뢰도 medium
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `designed specifically for natural language processing (NLP) tasks in the education sector` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `allowing for flexible selection of data according to time and computational power requirements during training` · 신뢰도 medium
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `99999999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[ATH-MaaS__Marco-Mini-Base|ATH-MaaS/Marco-Mini-Base]]
- [[ATH-MaaS__Marco-Mini-Global-Base|ATH-MaaS/Marco-Mini-Global-Base]]
- [[ATH-MaaS__Marco-Nano-Base|ATH-MaaS/Marco-Nano-Base]]
