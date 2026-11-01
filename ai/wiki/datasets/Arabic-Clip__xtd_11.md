---
type: "dataset"
id: "Arabic-Clip/xtd_11"
source: "huggingface"
url: "https://huggingface.co/datasets/Arabic-Clip/xtd_11"
downloads: 874
summary: "11개 언어로 된 1,000개 이미지와 캡션으로 제로샷 이미지 및 텍스트 검색을 위한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[이미지 생성]]"
  - "[[문서 검색]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Arabic-Clip/xtd_11

> dataset · [Hugging Face](https://huggingface.co/datasets/Arabic-Clip/xtd_11)

11개 언어로 된 1,000개 이미지와 캡션으로 제로샷 이미지 및 텍스트 검색을 위한 데이터셋입니다.

## 분류

- **작업**: [[이미지 생성]] — metadata · task_categories = `text-to-image` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `to test multimodel in zeroshot image or text retrieval in 11 Languages` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:image_generation, task:visual_qa = `1,000-image multi-lingual MSCOCO2014 caption` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:image_generation, task:retrieval, task:visual_qa = `multi-lingual MSCOCO2014 caption` · 신뢰도 medium
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — task_rule · task:image_generation = `image` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:visual_qa = `multi-lingual MSCOCO2014 caption` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multi-lingual MSCOCO2014 caption` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `to test multimodel in zeroshot image or text retrieval` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
