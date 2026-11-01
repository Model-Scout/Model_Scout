---
type: "dataset"
id: "werty1248/K-Namu-Full-Trainset"
source: "huggingface"
url: "https://huggingface.co/datasets/werty1248/K-Namu-Full-Trainset"
downloads: 16
summary: "나무위키 기반 한국 역사·문화·제도 관련 QA 데이터셋으로 문제 생성 및 평가에 활용됨"
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
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
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# werty1248/K-Namu-Full-Trainset

> dataset · [Hugging Face](https://huggingface.co/datasets/werty1248/K-Namu-Full-Trainset)

나무위키 기반 한국 역사·문화·제도 관련 QA 데이터셋으로 문제 생성 및 평가에 활용됨

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Gemini-2.5-flash 모델을 이용하여 선다형(객관식, 5지선다), 단답형 문제 생성` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `나무위키 기반 한국 역사/문화/제도 관련 QA 데이터 셋` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `나무위키 기반 한국 역사/문화/제도 관련 QA 데이터 셋` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `선다형(객관식, 5지선다), 단답형 문제 생성` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `39` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `한국 역사/문화/제도 관련 내용이 포함된 문서 약 55k개 식별 및 내용 요약` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Qwen3-30B-A3B 모델을 이용하여 한국 역사/문화/제도 관련 내용이 포함된 문서 약 55k개 식별 및 내용 요약` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 59자 ≈ 39 토큰 (viewer statistics, default/train)
