---
type: "dataset"
id: "timdettmers/openassistant-guanaco"
source: "huggingface"
url: "https://huggingface.co/datasets/timdettmers/openassistant-guanaco"
downloads: 11059
summary: "Open Assistant 데이터셋의 최고 평점 대화 경로만 포함한 서브셋으로, Guanaco 학습에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# timdettmers/openassistant-guanaco

> dataset · [Hugging Face](https://huggingface.co/datasets/timdettmers/openassistant-guanaco)

Open Assistant 데이터셋의 최고 평점 대화 경로만 포함한 서브셋으로, Guanaco 학습에 사용됨.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `This dataset was used to train Guanaco with QLoRA.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `conversation tree` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `conversation tree` · 신뢰도 medium
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `766` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This dataset was used to train Guanaco with QLoRA.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 3063자 ≈ 766 토큰 (viewer statistics, default/test)

## 이 데이터로 학습한 모델

- [[bartowski__Tralalabs_Pythia-6.9B-Instruct-v1-Merged-GGUF|bartowski/Tralalabs_Pythia-6.9B-Instruct-v1-Merged-GGUF]]
- [[tensorblock__llamav2-LoRaco-7b-merged-GGUF|tensorblock/llamav2-LoRaco-7b-merged-GGUF]]
