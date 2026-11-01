---
type: "dataset"
id: "jojo0217/korean_rlhf_dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/jojo0217/korean_rlhf_dataset"
downloads: 204
summary: "성균관대 산학협력 프로젝트로 한국어 LLM SFT 학습용으로 구축한 데이터셋입니다."
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jojo0217/korean_rlhf_dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/jojo0217/korean_rlhf_dataset)

성균관대 산학협력 프로젝트로 한국어 LLM SFT 학습용으로 구축한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `답변에 오픈 어시스턴트라고 하는 경우가 나오기 때문` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `524` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 llm 모델 SFT 학습을 위해 구축한 데이터셋 입니다` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `한국어 llm 모델 SFT 학습을 위해 구축한 데이터셋 입니다` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 786자 ≈ 524 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[Edentns__DataVortexTL-1.1B-v0.1|Edentns/DataVortexTL-1.1B-v0.1]]
- [[mradermacher__DataVortexTL-1.1B-v0.1-GGUF|mradermacher/DataVortexTL-1.1B-v0.1-GGUF]]
- [[mradermacher__DataVortexTL-1.1B-v0.1-i1-GGUF|mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF]]
- [[tensorblock__DataVortexTL-1.1B-v0.1-GGUF|tensorblock/DataVortexTL-1.1B-v0.1-GGUF]]
