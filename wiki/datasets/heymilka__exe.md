---
type: "dataset"
id: "heymilka/exe"
source: "huggingface"
url: "https://huggingface.co/datasets/heymilka/exe"
downloads: 175
summary: "윈도우용 소설 집필 및 텍스트 편집 도구 모음으로 집필 지원에 활용됨."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[문서 검색]]"
input_modality:
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
  - "[[학습용]]"
---
# heymilka/exe

> dataset · [Hugging Face](https://huggingface.co/datasets/heymilka/exe)

윈도우용 소설 집필 및 텍스트 편집 도구 모음으로 집필 지원에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `윈도우를 위한 집필 도구들 모음` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `로그 파일 자동 읽기: 파일 이름에 log, 로그, Log가 들어있으면 됨` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `검색 기능 추가, 검색어로 이동` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:information_extraction, task:retrieval = `text파일 오른쪽 클릭: Work로 보내기 됨` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Works tab 입력 5초 후 자동 저장 기능 추가` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `윈도우를 위한 집필 도구들 모음` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `자체 제작` · 신뢰도 low
