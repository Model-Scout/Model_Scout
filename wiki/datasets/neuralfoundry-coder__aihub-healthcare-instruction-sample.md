---
type: "dataset"
id: "neuralfoundry-coder/aihub-healthcare-instruction-sample"
source: "huggingface"
url: "https://huggingface.co/datasets/neuralfoundry-coder/aihub-healthcare-instruction-sample"
downloads: 33
summary: "한국어 의료/헬스케어 도메인 sLLM 지시학습용 데이터셋 샘플입니다."
readme_status: "ok"
readme_language: "mixed"
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
  - "[[조건부 이용]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# neuralfoundry-coder/aihub-healthcare-instruction-sample

> dataset · [Hugging Face](https://huggingface.co/datasets/neuralfoundry-coder/aihub-healthcare-instruction-sample)

한국어 의료/헬스케어 도메인 sLLM 지시학습용 데이터셋 샘플입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `한국어 의료/헬스케어 도메인 sLLM 지시학습을 위한 데이터셋입니다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `593` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `medical` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `AI Hub 헬스케어 지시학습 데이터셋 (샘플)파일 2개 · 11.0 MB · 행 17,868` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 890자 ≈ 593 토큰 (viewer statistics, default/train)
