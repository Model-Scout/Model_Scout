---
type: "dataset"
id: "fadhilafif98/triples-objekts"
source: "huggingface"
url: "https://huggingface.co/datasets/fadhilafif98/triples-objekts"
downloads: 865
summary: "K-팝 걸그룹 tripleS의 디지털 수집용 포토카드 이미지, 영상, 메타데이터 모음집입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
  - "[[이미지 인식]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
  - "[[영상 (출력 형식)|영상]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# fadhilafif98/triples-objekts

> dataset · [Hugging Face](https://huggingface.co/datasets/fadhilafif98/triples-objekts)

K-팝 걸그룹 tripleS의 디지털 수집용 포토카드 이미지, 영상, 메타데이터 모음집입니다.

## 분류

- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `Complete digital collectible photocards (Objekts) dataset for the K-Pop girl group tripleS` · 신뢰도 low
- **작업**: [[이미지 인식]] — metadata · readme, task_categories = `image-classification` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:vision, task:visual_qa = `21,881 high-resolution card scans (Front & Back)` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:embedding, task:retrieval, task:visual_qa = `text` · 신뢰도 high
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · readme = `177 animated card loops & voice message MP4 clips` · 신뢰도 low
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme = `21,881 high-resolution card scans (Front & Back)` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[영상 (출력 형식)|영상]] — ner · readme = `177 animated card loops & voice message MP4 clips` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `K-Pop girl group tripleS (Modhaus / COSMO app)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is compiled strictly for non-commercial fan archival, educational, indexing, and computer vision research purposes.` · 신뢰도 low
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
