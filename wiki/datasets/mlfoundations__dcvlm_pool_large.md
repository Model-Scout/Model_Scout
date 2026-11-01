---
type: "dataset"
id: "mlfoundations/dcvlm_pool_large"
source: "huggingface"
url: "https://huggingface.co/datasets/mlfoundations/dcvlm_pool_large"
downloads: 108070
summary: "DataComp-VLM 벤치마크용 대규모 원시 후보 풀 데이터셋으로, 데이터 큐레이션 실험에 사용됨."
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
  - "[[이미지 (출력 형식)|이미지]]"
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
# mlfoundations/dcvlm_pool_large

> dataset · [Hugging Face](https://huggingface.co/datasets/mlfoundations/dcvlm_pool_large)

DataComp-VLM 벤치마크용 대규모 원시 후보 풀 데이터셋으로, 데이터 큐레이션 실험에 사용됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `SSCD copy-detection embedding, which we used to run our image decontamination pipeline` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `The raw candidate pool at the large scale of our DataComp-VLM benchmark` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-text-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding, task:retrieval, task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme = `Alongside each image you also get some artifacts we computed for it` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `DataComp-VLM benchmark` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `It is the input to a data-curation experiment, not a training set. You choose the filters and the mixing ratios, and create another training set.` · 신뢰도 medium
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `9999999999.0` · 신뢰도 high
