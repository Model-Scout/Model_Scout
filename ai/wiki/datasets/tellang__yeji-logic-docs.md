---
type: "dataset"
id: "tellang/yeji-logic-docs"
source: "huggingface"
url: "https://huggingface.co/datasets/tellang/yeji-logic-docs"
downloads: 91
summary: "점술 로직 및 알고리즘 문서화 데이터셋으로 계산 로직과 해석 알고리즘을 포함합니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
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
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# tellang/yeji-logic-docs

> dataset · [Hugging Face](https://huggingface.co/datasets/tellang/yeji-logic-docs)

점술 로직 및 알고리즘 문서화 데이터셋으로 계산 로직과 해석 알고리즘을 포함합니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[정보 추출]] — ner · readme = `점술 로직 및 알고리즘 문서화` · 신뢰도 low
- **작업**: [[문서 검색]] — tag_match · tags = `rag` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:information_extraction, task:retrieval = `점술 로직 및 알고리즘 문서화` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `계산 로직, 해석 알고리즘, 구현 가이드` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
