---
type: "dataset"
id: "jiyoung720/KTB-index-team17"
source: "huggingface"
url: "https://huggingface.co/datasets/jiyoung720/KTB-index-team17"
downloads: 11
summary: "카카오 약관 4종을 조 단위로 파싱해 검색용 청크를 포함한 인덱스 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# jiyoung720/KTB-index-team17

> dataset · [Hugging Face](https://huggingface.co/datasets/jiyoung720/KTB-index-team17)

카카오 약관 4종을 조 단위로 파싱해 검색용 청크를 포함한 인덱스 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — tag_match · readme, tags = `rag` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:retrieval = `조 단위. retrieved는 이 단위로 반환` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `조 단위. retrieved는 이 단위로 반환` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `카카오테크 부트캠프 AI 성능 개선 대회용.` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
