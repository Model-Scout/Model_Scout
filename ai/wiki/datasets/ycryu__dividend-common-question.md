---
type: "dataset"
id: "ycryu/dividend-common-question"
source: "huggingface"
url: "https://huggingface.co/datasets/ycryu/dividend-common-question"
downloads: 5
summary: "배당주 투자 관련 자주 묻는 질문과 답변으로 구성된 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ycryu/dividend-common-question

> dataset · [Hugging Face](https://huggingface.co/datasets/ycryu/dividend-common-question)

배당주 투자 관련 자주 묻는 질문과 답변으로 구성된 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `instruction: 모델에게 주는 지시문 (예: "배당성향이 높아야 좋은 건가요?")` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `output: 모델이 생성해야 하는 답변 (예: "꼭 그렇다고 할 수는 없습니다...")` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `46` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `파인튜닝 실습이나 자연어 처리 모델 학습에 활용할 수 있습니다.` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 69자 ≈ 46 토큰 (viewer statistics, default/train)
