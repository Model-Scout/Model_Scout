---
type: "dataset"
id: "SamsungSDS-Research/SDS-KoPub-VDR-Benchmark"
source: "huggingface"
url: "https://huggingface.co/datasets/SamsungSDS-Research/SDS-KoPub-VDR-Benchmark"
downloads: 429
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[질의응답]]"
  - "[[문서 검색]]"
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
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# SamsungSDS-Research/SDS-KoPub-VDR-Benchmark

> dataset · [Hugging Face](https://huggingface.co/datasets/SamsungSDS-Research/SDS-KoPub-VDR-Benchmark)

## 분류

- **작업**: [[질의응답]] — tag_match · tags = `question-answering` · 신뢰도 medium
- **작업**: [[문서 검색]] — metadata · tags, task_categories = `visual-document-retrieval` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:question_answering, task:retrieval = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
