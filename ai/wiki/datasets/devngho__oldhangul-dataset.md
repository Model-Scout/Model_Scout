---
type: "dataset"
id: "devngho/oldhangul-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/devngho/oldhangul-dataset"
downloads: 19
summary: "위키문헌 기반 옛한글 데이터셋으로 한자 비율 필터링 및 정리 포함"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[언어 모델링]]"
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
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# devngho/oldhangul-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/devngho/oldhangul-dataset)

위키문헌 기반 옛한글 데이터셋으로 한자 비율 필터링 및 정리 포함

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `위키문헌을 기반으로 구축한 옛한글 데이터셋` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:language_modeling = `위키문헌을 기반으로 구축한 옛한글 데이터셋` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `위키문헌을 기반으로 구축한 옛한글 데이터셋` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `25681` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `위키문헌을 기반으로 구축한 옛한글 데이터셋` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `위키문헌을 기반으로 구축한 옛한글 데이터셋` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 38522자 ≈ 25681 토큰 (viewer statistics, wikisource_v2/train)
