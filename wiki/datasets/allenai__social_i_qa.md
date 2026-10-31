---
type: "dataset"
id: "allenai/social_i_qa"
source: "huggingface"
url: "https://huggingface.co/datasets/allenai/social_i_qa"
downloads: 35858
summary: "Social IQa는 사회적 상식 추론을 평가하는 QA 벤치마크 데이터셋입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
---
# allenai/social_i_qa

> dataset · [Hugging Face](https://huggingface.co/datasets/allenai/social_i_qa)

Social IQa는 사회적 상식 추론을 평가하는 QA 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `a new question-answering benchmark for testing social commonsense intelligence` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:question_answering = `given an action like "Jesse saw a concert" and a question like "Why did Jesse do this?"` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `answer candidates contain both human-curated answers and adversarially-filtered machine-generated candidates` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a new question-answering benchmark for testing social commonsense intelligence` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Social IQa contains over 37,000 QA pairs for evaluating models’ abilities` · 신뢰도 low
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium

## 이 데이터로 학습한 모델

- [[blackmallangcow__nari-decision-4b|blackmallangcow/nari-decision-4b]]
