---
type: "dataset"
id: "ggh5454/legal-provence-ko-with-teacher-scores"
source: "huggingface"
url: "https://huggingface.co/datasets/ggh5454/legal-provence-ko-with-teacher-scores"
downloads: 153
summary: "법률 분야 문서 검색을 위한 teacher 모델 점수 포함 최종 훈련 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[리랭킹]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ggh5454/legal-provence-ko-with-teacher-scores

> dataset · [Hugging Face](https://huggingface.co/datasets/ggh5454/legal-provence-ko-with-teacher-scores)

법률 분야 문서 검색을 위한 teacher 모델 점수 포함 최종 훈련 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[리랭킹]] — tag_match · readme, tags = `reranking` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `검색 쿼리` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:reranking, task:retrieval = `검색 쿼리` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `문서별 관련성 레이블` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `최종 훈련용 데이터셋입니다.` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
