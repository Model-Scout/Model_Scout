---
type: "dataset"
id: "qwer90qwer/health"
source: "huggingface"
url: "https://huggingface.co/datasets/qwer90qwer/health"
downloads: 265
summary: "보건·공중보건 자료를 수집한 한국어 공공 보건 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# qwer90qwer/health

> dataset · [Hugging Face](https://huggingface.co/datasets/qwer90qwer/health)

보건·공중보건 자료를 수집한 한국어 공공 보건 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `보건·공중보건 자료를 수집한 데이터셋입니다.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — metadata · modality = `document` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation = `보건·공중보건 자료를 수집한 데이터셋입니다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `보건·공중보건 자료를 수집한 데이터셋입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — ner · readme = `보건·공중보건 자료를 수집한 데이터셋입니다.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `공공누리 출처표시 조건으로 확인된 보건·공중보건 자료를 수집한 데이터셋입니다.` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
