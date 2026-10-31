---
type: "dataset"
id: "dev7halo/bluehouse-national-petition"
source: "huggingface"
url: "https://huggingface.co/datasets/dev7halo/bluehouse-national-petition"
downloads: 25
summary: "청와대 국민청원 데이터를 포함하며 청원 분석에 활용되는 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# dev7halo/bluehouse-national-petition

> dataset · [Hugging Face](https://huggingface.co/datasets/dev7halo/bluehouse-national-petition)

청와대 국민청원 데이터를 포함하며 청원 분석에 활용되는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `features: ['number', '제목', '답변상태', '참여인원', '카테고리', '청원시작', '청원마감', '청원내용', '답변원고']` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `features: ['number', '제목', '답변상태', '참여인원', '카테고리', '청원시작', '청원마감', '청원내용', '답변원고']` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `features: ['number', '제목', '답변상태', '참여인원', '카테고리', '청원시작', '청원마감', '청원내용', '답변원고']` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `99342` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `DatasetDict({ train: Dataset({ features: ['number', '제목', '답변상태', '참여인원', '카테고리', '청원시작', '청원마감', '청원내용', '답변원고'], num_rows: 451513 }) })` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `청원내용` 열 p90 149013자 ≈ 99342 토큰 (viewer statistics, default/train)
