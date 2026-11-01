---
type: "dataset"
id: "lumo-947/resume-matching-dataset-v2"
source: "huggingface"
url: "https://huggingface.co/datasets/lumo-947/resume-matching-dataset-v2"
downloads: 17
summary: "이 데이터셋은 이력서와 자기소개서 평가 점수를 포함한 채용 매칭 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# lumo-947/resume-matching-dataset-v2

> dataset · [Hugging Face](https://huggingface.co/datasets/lumo-947/resume-matching-dataset-v2)

이 데이터셋은 이력서와 자기소개서 평가 점수를 포함한 채용 매칭 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `resume_grade` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification = `text` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1438` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `- name: validation
num_bytes: 884668
num_examples: 100` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `- name: train
num_bytes: 612749926
num_examples: 69047` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `selfintro` 열 p90 2157자 ≈ 1438 토큰 (viewer statistics, default/validation)
