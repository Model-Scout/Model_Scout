---
type: "dataset"
id: "JooYoon/riidolaya-development-short-core-pilot-v0.1"
source: "huggingface"
url: "https://huggingface.co/datasets/JooYoon/riidolaya-development-short-core-pilot-v0.1"
downloads: 279
summary: "가상 개발 상황에서 한영 쌍 문장 의미 보존 검토를 위한 짧은 개발 댓글 작성 방식 시험 데이터입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
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
---
# JooYoon/riidolaya-development-short-core-pilot-v0.1

> dataset · [Hugging Face](https://huggingface.co/datasets/JooYoon/riidolaya-development-short-core-pilot-v0.1)

가상 개발 상황에서 한영 쌍 문장 의미 보존 검토를 위한 짧은 개발 댓글 작성 방식 시험 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `언어별 첫 판정과 번역 쌍의 의미 보존을 따로 검토했습니다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `60한영쌍·120문장을 작성하고, 언어별 첫 판정과 번역 쌍의 의미 보존을 따로 검토했습니다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `언어별 첫 판정과 번역 쌍의 의미 보존을 따로 검토했습니다.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `새로운 가상 개발 상황 20그룹·60한영쌍·120문장을 작성하고` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `이번 120개는 학습·모델 평가·골든셋·최종 2,400개에 합산하지 않습니다.` · 신뢰도 medium
