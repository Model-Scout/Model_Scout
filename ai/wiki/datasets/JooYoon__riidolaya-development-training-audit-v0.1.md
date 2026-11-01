---
type: "dataset"
id: "JooYoon/riidolaya-development-training-audit-v0.1"
source: "huggingface"
url: "https://huggingface.co/datasets/JooYoon/riidolaya-development-training-audit-v0.1"
downloads: 74
summary: "기존 공개 학습 자료의 분포와 AI 참조 판정 일관성을 점검한 집계 진단 기록 데이터입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# JooYoon/riidolaya-development-training-audit-v0.1

> dataset · [Hugging Face](https://huggingface.co/datasets/JooYoon/riidolaya-development-training-audit-v0.1)

기존 공개 학습 자료의 분포와 AI 참조 판정 일관성을 점검한 집계 진단 기록 데이터입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `다음 튜닝 전에 자료의 분포와 AI 참조 판정의 일관성을 확인하려고 만들었습니다.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding = `1,680행·840한국어/영어쌍` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `AI 참조 판정의 일관성을 확인하려고 만들었습니다.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `기존 공개 학습 자료에 대한 집계 진단 기록입니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `다음 튜닝 전에 자료의 분포와 AI 참조 판정의 일관성을 확인하려고 만들었습니다.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
