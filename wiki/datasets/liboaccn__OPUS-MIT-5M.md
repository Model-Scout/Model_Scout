---
type: "dataset"
id: "liboaccn/OPUS-MIT-5M"
source: "huggingface"
url: "https://huggingface.co/datasets/liboaccn/OPUS-MIT-5M"
downloads: 22
summary: "OPUS-MIT-5M은 OPUS 말뭉치에서 추출한 5백만 문장쌍으로 구성된 다국어 이미지 번역 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[번역]]"
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# liboaccn/OPUS-MIT-5M

> dataset · [Hugging Face](https://huggingface.co/datasets/liboaccn/OPUS-MIT-5M)

OPUS-MIT-5M은 OPUS 말뭉치에서 추출한 5백만 문장쌍으로 구성된 다국어 이미지 번역 데이터셋입니다.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `5M sentence pairs from the OPUS corpus` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `image translation` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `11 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The OPUS-MIT-5M image translation dataset is constructed by randomly sampling 5M sentence pairs from the OPUS corpus.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The OPUS-MIT-5M image translation dataset is constructed by randomly sampling 5M sentence pairs from the OPUS corpus.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
