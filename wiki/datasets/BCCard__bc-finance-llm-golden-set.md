---
type: "dataset"
id: "BCCard/bc-finance-llm-golden-set"
source: "huggingface"
url: "https://huggingface.co/datasets/BCCard/bc-finance-llm-golden-set"
downloads: 26
summary: "LLM 배포 전 회귀 품질 검증을 위한 금융 분야 골든셋 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# BCCard/bc-finance-llm-golden-set

> dataset · [Hugging Face](https://huggingface.co/datasets/BCCard/bc-finance-llm-golden-set)

LLM 배포 전 회귀 품질 검증을 위한 금융 분야 골든셋 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Regression 품질 검증을 위한 골든셋 데이터셋입니다.` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:question_answering = `data/regression_golden_set.csv` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Regression 품질 검증을 위한 골든셋 데이터셋입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `모델 업데이트 또는 프롬프트 변경 후 배포 전 회귀 테스트(Regression Gate)에 활용합니다.` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
