---
type: "dataset"
id: "AIdenU/orca_dpo_data_ko"
source: "huggingface"
url: "https://huggingface.co/datasets/AIdenU/orca_dpo_data_ko"
downloads: 67
summary: "HuggingFaceH4/orca_dpo_pairs 원본 데이터를 한국어로 번역하고 오번역을 검수한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[번역]]"
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
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# AIdenU/orca_dpo_data_ko

> dataset · [Hugging Face](https://huggingface.co/datasets/AIdenU/orca_dpo_data_ko)

HuggingFaceH4/orca_dpo_pairs 원본 데이터를 한국어로 번역하고 오번역을 검수한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `system, question, chosen, rejected 형태에 맞게 정제` · 신뢰도 low
- **작업**: [[번역]] — ner · readme = `squarelike/Gugugo-koen-7B-V1.1-AWQ 으로 번역` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = `system, question, chosen, rejected 형태` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `squarelike/Gugugo-koen-7B-V1.1-AWQ 으로 번역` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `629` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `원본 데이터 셋을 system, question, chosen, rejected 형태에 맞게 정제 후` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `rejected` 열 p90 944자 ≈ 629 토큰 (viewer statistics, default/test)
