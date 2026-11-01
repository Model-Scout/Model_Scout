---
type: "dataset"
id: "MLOpsEngineer/investment_analysis"
source: "huggingface"
url: "https://huggingface.co/datasets/MLOpsEngineer/investment_analysis"
downloads: 17
summary: "코스피 상장 기업 공시정보 기반 투자 분석 및 전략 제안용 GPT 파인튜닝 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
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
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# MLOpsEngineer/investment_analysis

> dataset · [Hugging Face](https://huggingface.co/datasets/MLOpsEngineer/investment_analysis)

코스피 상장 기업 공시정보 기반 투자 분석 및 전략 제안용 GPT 파인튜닝 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `투자 전문가들이 활용할 수 있는 심층적 분석과 투자 전략 제안을 목표로 제작되었습니다.` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `데이터셋은 JSONL 포맷으로 제공되며, 각 항목은 GPT 파인튜닝에 최적화된 메시지 형식을 따릅니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `모델의 답변을 포함합니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `GPT 파인튜닝에 최적화된 구조로 설계되어 있어, 다양한 역할(role)을 포함한 메시지 기반의 대화 형식으로 구성되어 있습니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
