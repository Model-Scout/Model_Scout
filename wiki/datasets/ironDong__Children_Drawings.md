---
type: "dataset"
id: "ironDong/Children_Drawings"
source: "huggingface"
url: "https://huggingface.co/datasets/ironDong/Children_Drawings"
downloads: 19
summary: "국가정보화진흥원 프로젝트로 수집된 어린이 그림 데이터셋으로, 그림 분석 연구에 활용 가능하다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
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
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ironDong/Children_Drawings

> dataset · [Hugging Face](https://huggingface.co/datasets/ironDong/Children_Drawings)

국가정보화진흥원 프로젝트로 수집된 어린이 그림 데이터셋으로, 그림 분석 연구에 활용 가능하다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Drawings of houses, trees, male figures, and female figures` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Machine learning models for analyzing children's drawings` · 신뢰도 low
- **작업**: [[이미지 인식]] — metadata · task_categories = `image-classification` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:vision = `Both raw source images and labeled data` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:embedding = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `labeled data` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `Educational research on child development` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Training and validation splits` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
