---
type: "dataset"
id: "nvidia/miracl-vision"
source: "huggingface"
url: "https://huggingface.co/datasets/nvidia/miracl-vision"
downloads: 1185
summary: "MIRACL-VISION은 18개 언어의 위키피디아 이미지와 질문으로 다국어 시각 문서 검색 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# nvidia/miracl-vision

> dataset · [Hugging Face](https://huggingface.co/datasets/nvidia/miracl-vision)

MIRACL-VISION은 18개 언어의 위키피디아 이미지와 질문으로 다국어 시각 문서 검색 평가용 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — metadata · readme, task_ids = `document-retrieval` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `images of Wikipedia articles` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `The dataset contains user questions` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `annotations, which article can answer a user question.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `18 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `271` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `images of Wikipedia articles and annotations` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `This dataset is ready for commercial usage for evaluation of the multilingual, multimodal retriever pipelines.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text_downloaded_from_Wikipedia` 열 p90 1083자 ≈ 271 토큰 (viewer statistics, corpus-ko/default)
