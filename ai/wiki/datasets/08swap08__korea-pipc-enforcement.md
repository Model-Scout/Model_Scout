---
type: "dataset"
id: "08swap08/korea-pipc-enforcement"
source: "huggingface"
url: "https://huggingface.co/datasets/08swap08/korea-pipc-enforcement"
downloads: 152
summary: "한국 개인정보 규제 관련 제재, 조정, 판결 등 자료를 담은 연구 및 분석용 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
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
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# 08swap08/korea-pipc-enforcement

> dataset · [Hugging Face](https://huggingface.co/datasets/08swap08/korea-pipc-enforcement)

한국 개인정보 규제 관련 제재, 조정, 판결 등 자료를 담은 연구 및 분석용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `제재 경향 분석` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `법률 정보 검색·질의응답 시스템의 근거 자료` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `법률 정보 검색·질의응답 시스템의 근거 자료` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:question_answering, task:retrieval = `모든 파일은 UTF-8로 인코딩되어 있습니다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `법률 정보 검색·질의응답 시스템의 근거 자료` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `법률 정보 검색·질의응답 시스템의 근거 자료` · 신뢰도 low
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `이 저장소는 사이트에 공개된 최신 판을 주 1회 따라가는 작업본이며` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
