---
type: "dataset"
id: "mlfoundations/dcvlm_pool_small_annotations"
source: "huggingface"
url: "https://huggingface.co/datasets/mlfoundations/dcvlm_pool_small_annotations"
downloads: 4068
summary: "DataComp-VLM 논문의 소규모 데이터 풀에 대한 이미지-텍스트 정렬 등 167개 주석을 포함한 원시 주석 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[문서 검색]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[nl]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# mlfoundations/dcvlm_pool_small_annotations

> dataset · [Hugging Face](https://huggingface.co/datasets/mlfoundations/dcvlm_pool_small_annotations)

DataComp-VLM 논문의 소규모 데이터 풀에 대한 이미지-텍스트 정렬 등 167개 주석을 포함한 원시 주석 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `image quality, image–text alignment, language ID, text-quality classifiers, multimodal perplexity, decontamination scores and more — up to 167 fields per sample` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `image–text alignment, language ID` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-text-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:retrieval, task:visual_qa = `image–text alignment, language ID, text-quality classifiers, multimodal perplexity, decontamination scores` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:visual_qa = `Every filtering annotation we computed for the small data pool of our DataComp-VLM paper: image quality, image–text alignment, language ID, text-quality classif` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `8 languages` · 신뢰도 high
- **언어**: [[nl]] — metadata · languages = `nl` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `DataComp-VLM paper: image quality, image–text alignment, language ID, text-quality classifiers, multimodal perplexity, decontamination scores` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `They are the inputs our curation pipeline consumes to build a training mixture` · 신뢰도 medium
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high
