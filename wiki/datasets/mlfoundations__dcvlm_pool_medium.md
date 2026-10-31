---
type: "dataset"
id: "mlfoundations/dcvlm_pool_medium"
source: "huggingface"
url: "https://huggingface.co/datasets/mlfoundations/dcvlm_pool_medium"
downloads: 37409
summary: "DataComp-VLM 벤치마크용 4억 8천만 샘플의 원시 미디어 데이터 풀로, 데이터 큐레이션에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# mlfoundations/dcvlm_pool_medium

> dataset · [Hugging Face](https://huggingface.co/datasets/mlfoundations/dcvlm_pool_medium)

DataComp-VLM 벤치마크용 4억 8천만 샘플의 원시 미디어 데이터 풀로, 데이터 큐레이션에 사용됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `` .sscd_disc_mixup.pt` (SSCD copy-detection embedding, which we used to run our image decontamination pipeline)` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `This pool is unfiltered and unmixed. It is the input to a data-curation experiment` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-text-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:visual_qa = `one or more images (` .jpg`)` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding, task:retrieval, task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `DataComp-VLM benchmark: 483,576,747 samples / 41.1 TB across 166 source datasets` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This pool is unfiltered and unmixed. It is the input to a data-curation experiment, not a training set.` · 신뢰도 medium
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high
