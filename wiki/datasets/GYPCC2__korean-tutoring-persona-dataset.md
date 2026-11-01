---
type: "dataset"
id: "GYPCC2/korean-tutoring-persona-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/GYPCC2/korean-tutoring-persona-dataset"
downloads: 27
summary: "한국어 학습자 페르소나 모델링이 포함된 이중언어 튜터링 시스템 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[평가용]]"
---
# GYPCC2/korean-tutoring-persona-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/GYPCC2/korean-tutoring-persona-dataset)

한국어 학습자 페르소나 모델링이 포함된 이중언어 튜터링 시스템 평가용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Three responses generated under different persona configurations` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Task Types
---
- Grammar Explanation
- Error Correction
- Multi-turn Dialogue` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Input query` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Three responses generated under different persona configurations` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `This dataset is constructed to evaluate the impact of learner persona modeling in bilingual Korean tutoring systems.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `This dataset is designed for:
- Evaluating instructional consistency
- Analyzing difficulty alignment
- Measuring error-targeted feedback` · 신뢰도 low
