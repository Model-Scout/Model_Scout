---
type: "dataset"
id: "bbanany/step4_sllm_v2"
source: "huggingface"
url: "https://huggingface.co/datasets/bbanany/step4_sllm_v2"
downloads: 77
summary: "PII 후보를 문맥상 개인정보 여부로 판정하는 합성 데이터셋으로 Qwen SFT용임"
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# bbanany/step4_sllm_v2

> dataset · [Hugging Face](https://huggingface.co/datasets/bbanany/step4_sllm_v2)

PII 후보를 문맥상 개인정보 여부로 판정하는 합성 데이터셋으로 Qwen SFT용임

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `각 행의 최상위 필드는 messages 하나뿐이며 system, user, assistant 순서다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `assistant 응답 부분에만 loss를 계산한다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `이 데이터는 합성 데이터이며 실존 인물의 개인정보를 수집한 데이터가 아니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `step4_final_10000_qwen_test.jsonl: 최종 평가 1,000개` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `step4_final_10000_qwen_train.jsonl: 학습 8,000개` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
