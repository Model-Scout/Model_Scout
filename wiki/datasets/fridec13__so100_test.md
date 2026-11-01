---
type: "dataset"
id: "fridec13/so100_test"
source: "huggingface"
url: "https://huggingface.co/datasets/fridec13/so100_test"
downloads: 27
summary: "SO-100 로봇 팔로 레고 블록을 잡아 통에 넣는 작업 데이터를 담은 데이터셋입니다."
readme_status: "thin"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# fridec13/so100_test

> dataset · [Hugging Face](https://huggingface.co/datasets/fridec13/so100_test)

SO-100 로봇 팔로 레고 블록을 잡아 통에 넣는 작업 데이터를 담은 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `이 데이터셋은 SO-100 로봇 팔을 사용하여 "Grasp a lego block and put it in the bin" 작업을 수행한 데이터를 담고 있습니다.` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:retrieval = `text` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — ner · readme = `FPS: 30 에피소드 수: 2 에피소드 길이: 30초` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `이 데이터셋은 SO-100 로봇 팔을 사용하여 "Grasp a lego block and put it in the bin" 작업을 수행한 데이터를 담고 있습니다.` · 신뢰도 low
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
