---
type: "dataset"
id: "ChuGyouk/AIHUB-mathsolution-edit"
source: "huggingface"
url: "https://huggingface.co/datasets/ChuGyouk/AIHUB-mathsolution-edit"
downloads: 24
summary: "AIHUB의 수학 과목 자동 풀이 데이터를 Qwen 모델로 편집한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ChuGyouk/AIHUB-mathsolution-edit

> dataset · [Hugging Face](https://huggingface.co/datasets/ChuGyouk/AIHUB-mathsolution-edit)

AIHUB의 수학 과목 자동 풀이 데이터를 Qwen 모델로 편집한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `수학 과목 자동 풀이 데이터` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `수학 과목 자동 풀이 데이터` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `수학 과목 자동 풀이 데이터` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `912` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `수학 과목 자동 풀이 데이터` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This is the subset of 수학 과목 자동 풀이 데이터 from AIHUB` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `new_answer` 열 p90 1368자 ≈ 912 토큰 (viewer statistics, default/train)
