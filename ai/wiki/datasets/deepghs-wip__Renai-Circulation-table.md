---
type: "dataset"
id: "deepghs-wip/Renai-Circulation-table"
source: "huggingface"
url: "https://huggingface.co/datasets/deepghs-wip/Renai-Circulation-table"
downloads: 19
summary: "일러스트와 애니메이션 관련 메타데이터를 포함한 이미지 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[문서 검색]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# deepghs-wip/Renai-Circulation-table

> dataset · [Hugging Face](https://huggingface.co/datasets/deepghs-wip/Renai-Circulation-table)

일러스트와 애니메이션 관련 메타데이터를 포함한 이미지 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `R-18 | Explicit | Illust | Non-AI Generated` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `49752138 records in total. Only 50 records shown.` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality = `image` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:retrieval = `id title comm tags rate lewd type isai size pages created uploaded modified count request user` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `id title comm tags rate lewd type isai size pages created uploaded modified count request user` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `エロいスパム㌧集です。受けばかりです。モブスパ、スパスパ、パレスパなイラストばかりです。` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `49752138 records in total.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high
