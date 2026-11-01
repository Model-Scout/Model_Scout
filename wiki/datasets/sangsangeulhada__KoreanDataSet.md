---
type: "dataset"
id: "sangsangeulhada/KoreanDataSet"
source: "huggingface"
url: "https://huggingface.co/datasets/sangsangeulhada/KoreanDataSet"
downloads: 8
summary: "aihub_도서자료 기계독해 데이터셋으로 기계독해 학습용 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# sangsangeulhada/KoreanDataSet

> dataset · [Hugging Face](https://huggingface.co/datasets/sangsangeulhada/KoreanDataSet)

aihub_도서자료 기계독해 데이터셋으로 기계독해 학습용 데이터입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `aihub_도서자료 기계독해` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:question_answering = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `- name: output` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `37` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `- name: train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `instruction` 열 p90 55자 ≈ 37 토큰 (viewer statistics, default/train)

## 같은 데이터의 사본·중복 등록

- `SangMoone/KoreanDataSet`
