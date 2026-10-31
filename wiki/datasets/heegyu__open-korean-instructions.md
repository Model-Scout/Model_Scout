---
type: "dataset"
id: "heegyu/open-korean-instructions"
source: "huggingface"
url: "https://huggingface.co/datasets/heegyu/open-korean-instructions"
downloads: 376
summary: "4가지 한국어 챗봇 학습용 데이터셋을 합쳐 멀티턴 및 싱글턴 대화 학습에 활용하는 데이터입니다."
readme_status: "ok"
readme_language: "ko"
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
# heegyu/open-korean-instructions

> dataset · [Hugging Face](https://huggingface.co/datasets/heegyu/open-korean-instructions)

4가지 한국어 챗봇 학습용 데이터셋을 합쳐 멀티턴 및 싱글턴 대화 학습에 활용하는 데이터입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `4가지 한국어 챗봇 학습용 데이터셋을 합쳐놓았습니다.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `모든 데이터는 포멧이 통일되어 있습니다. <sys>, <usr>, <bot> 세가지 토큰과 줄넘김으로 화자를 구분합니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `모든 데이터는 포멧이 통일되어 있습니다. <sys>, <usr>, <bot> 세가지 토큰과 줄넘김으로 화자를 구분합니다.` · 신뢰도 medium
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `992` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `4가지 한국어 챗봇 학습용 데이터셋을 합쳐놓았습니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `4가지 한국어 챗봇 학습용 데이터셋을 합쳐놓았습니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 3967자 ≈ 992 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[prismdata__Perdix-1.1B-Instruct|prismdata/Perdix-1.1B-Instruct]]
- [[tensorblock__ft-solar-10.7b-v2.1-dpo-GGUF|tensorblock/ft-solar-10.7b-v2.1-dpo-GGUF]]
