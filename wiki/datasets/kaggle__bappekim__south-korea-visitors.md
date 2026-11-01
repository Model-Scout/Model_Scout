---
type: "dataset"
id: "kaggle/bappekim/south-korea-visitors"
source: "kaggle"
url: "https://www.kaggle.com/datasets/bappekim/south-korea-visitors"
downloads: 4845
summary: "한국관광공사(KTO) 자료를 재구성한 외국인 한국 방문객 통계 데이터로 관광 정책 수립에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/bappekim/south-korea-visitors

> dataset · [Kaggle](https://www.kaggle.com/datasets/bappekim/south-korea-visitors)

한국관광공사(KTO) 자료를 재구성한 외국인 한국 방문객 통계 데이터로 관광 정책 수립에 활용됨.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `The Korea Tourism Organization (KTO) has compiled, analyzed, and provided statistics on foreign tourists visiting Korea and overseas tourists by type.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `This data set is divided into three files (age, gender, and propose).` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `This data set is divided into three files (age, gender, and propose).` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC BY-SA 4.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `The Korea Tourism Organization (KTO) has compiled, analyzed, and provided statistics on foreign tourists visiting Korea and overseas tourists by type.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `I created this dataset by rebuilding the data provided by KTO for easy analysis.` · 신뢰도 low
