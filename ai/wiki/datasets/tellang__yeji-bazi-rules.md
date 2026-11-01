---
type: "dataset"
id: "tellang/yeji-bazi-rules"
source: "huggingface"
url: "https://huggingface.co/datasets/tellang/yeji-bazi-rules"
downloads: 76
summary: "사주팔자 해석 규칙과 가이드라인 데이터셋으로 십신, 용신, 격국, 대운 해석에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[문서 검색]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# tellang/yeji-bazi-rules

> dataset · [Hugging Face](https://huggingface.co/datasets/tellang/yeji-bazi-rules)

사주팔자 해석 규칙과 가이드라인 데이터셋으로 십신, 용신, 격국, 대운 해석에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `십신, 용신, 격국, 대운 해석 규칙` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `사주팔자 해석 규칙 및 가이드라인` · 신뢰도 low
- **작업**: [[문서 검색]] — tag_match · tags = `rag` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:information_extraction, task:retrieval = `사주팔자 해석 규칙 및 가이드라인` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `사주팔자 해석 규칙 및 가이드라인` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `사주팔자 해석 규칙 및 가이드라인` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `사주팔자 해석 규칙 및 가이드라인` · 신뢰도 low
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
