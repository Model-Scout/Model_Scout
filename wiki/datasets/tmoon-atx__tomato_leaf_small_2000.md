---
type: "dataset"
id: "tmoon-atx/tomato_leaf_small_2000"
source: "huggingface"
url: "https://huggingface.co/datasets/tmoon-atx/tomato_leaf_small_2000"
downloads: 35
summary: "토마토 잎 사진 2,000장으로 병해충 진단기 실습용 교육 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# tmoon-atx/tomato_leaf_small_2000

> dataset · [Hugging Face](https://huggingface.co/datasets/tmoon-atx/tomato_leaf_small_2000)

토마토 잎 사진 2,000장으로 병해충 진단기 실습용 교육 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `토마토 잎 사진으로 병해충 진단기를 만들고 검증하는 실습에 쓰는 묶음입니다.` · 신뢰도 low
- **작업**: [[이미지 인식]] — metadata · task_categories = `image-classification` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:vision = `토마토 잎 사진 2,000장` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `10개 클래스에서 클래스마다 200장씩, 모두 2,000장` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[교육]] — tag_match · tags = `education` · 신뢰도 medium
- **도메인**: [[의료·보건]] — ner · readme = `토마토 잎 사진으로 병해충 진단기를 만들고 검증하는 실습에 쓰는 묶음입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `토마토 잎 사진 2,000장 (교육용 묶음)` · 신뢰도 low
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
