---
type: "dataset"
id: "allganize/math_table_qa"
source: "huggingface"
url: "https://huggingface.co/datasets/allganize/math_table_qa"
downloads: 25
summary: "mathqa-ko와 tableqa-ko는 일반 도메인의 QA 데이터셋으로 질문에 답을 생성하는 데 사용됩니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
---
# allganize/math_table_qa

> dataset · [Hugging Face](https://huggingface.co/datasets/allganize/math_table_qa)

mathqa-ko와 tableqa-ko는 일반 도메인의 QA 데이터셋으로 질문에 답을 생성하는 데 사용됩니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Context와 Question이 주어졌을 때, 질문에 상응하는 답을 생성해야 합니다.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `입력값으로는 text와 table이 함께 주어집니다.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation = `입력값으로는 text만이 주어집니다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `질문에 상응하는 답을 생성해야 합니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `mathqa-ko 데이터는 일반(general) 도메인의 QA 데이터셋입니다.` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `Test를 위해 랜덤하게 90개를 선택하였습니다.` · 신뢰도 low
