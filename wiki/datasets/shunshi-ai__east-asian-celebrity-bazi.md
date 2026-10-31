---
type: "dataset"
id: "shunshi-ai/east-asian-celebrity-bazi"
source: "huggingface"
url: "https://huggingface.co/datasets/shunshi-ai/east-asian-celebrity-bazi"
downloads: 151
summary: "중국, 한국, 일본 유명인 2,284명의 출생일을 사주(삼주)로 변환한 문화·역사 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[정보 추출]]"
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# shunshi-ai/east-asian-celebrity-bazi

> dataset · [Hugging Face](https://huggingface.co/datasets/shunshi-ai/east-asian-celebrity-bazi)

중국, 한국, 일본 유명인 2,284명의 출생일을 사주(삼주)로 변환한 문화·역사 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `with birth dates mapped to Four Pillars (BaZi / 四柱八字) year, month, and day pillars — including stems, branches, five-element attributions, hidden stems, and Ten` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — metadata · task_categories = `tabular-classification` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:tabular_prediction = `table` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:information_extraction = `with birth dates mapped to Four Pillars (BaZi / 四柱八字) year, month, and day pillars` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `with birth dates mapped to Four Pillars (BaZi / 四柱八字) year, month, and day pillars — including stems, branches, five-element attributions, hidden stems, and Ten` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `9` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `pattern_tags` 열 p90 37자 ≈ 9 토큰 (viewer statistics, default/train)
