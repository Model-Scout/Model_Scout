---
type: "dataset"
id: "movensys/wmx-r2-command-grounded-cr3a-axis-v0"
source: "huggingface"
url: "https://huggingface.co/datasets/movensys/wmx-r2-command-grounded-cr3a-axis-v0"
downloads: 77
summary: "Dobot CR3A 로봇의 1000Hz 축 데이터로 모션 분석용 공개 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
---
# movensys/wmx-r2-command-grounded-cr3a-axis-v0

> dataset · [Hugging Face](https://huggingface.co/datasets/movensys/wmx-r2-command-grounded-cr3a-axis-v0)

Dobot CR3A 로봇의 1000Hz 축 데이터로 모션 분석용 공개 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `All 1,018,389 original axis rows are retained in order on a nominal 1000 Hz engine-cycle grid.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding = `text` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — ner · readme = `All 1,018,389 original axis rows are retained in order on a nominal 1000 Hz engine-cycle grid.` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — ner · readme = `All 1,018,389 original axis rows are retained in order on a nominal 1000 Hz engine-cycle grid.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Public dataset. Downloading does not require authentication.` · 신뢰도 low
