---
type: "dataset"
id: "allenai/dolma3_dolmino_mix-100B-1125"
source: "huggingface"
url: "https://huggingface.co/datasets/allenai/dolma3_dolmino_mix-100B-1125"
downloads: 33303
summary: "Olmo 3 32B 모델 2단계 학습용 고품질 수학, 코드, QA, 추론 데이터셋 풀입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[학술·논문]]"
dataset_role:
  - "[[학습용]]"
---
# allenai/dolma3_dolmino_mix-100B-1125

> dataset · [Hugging Face](https://huggingface.co/datasets/allenai/dolma3_dolmino_mix-100B-1125)

Olmo 3 32B 모델 2단계 학습용 고품질 수학, 코드, QA, 추론 데이터셋 풀입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Tulu 3 SFT | Instruction (synth)` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `Dolma 3 Dolmino dataset pool for Olmo 3 stage 2 annealing training` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Reddit To Flashcards | QA (synth)` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation, task:question_answering = `web pages, code, math/QA/thinking/instruction/PDFs` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `web pages, code, math/QA/thinking/instruction/PDFs` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `Math (synth)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This dataset contains the high-quality pool of data considered for the second stage of Olmo 3 32B.` · 신뢰도 medium

## 이 데이터로 학습한 모델

- [[ATH-MaaS__Marco-Mini-Base|ATH-MaaS/Marco-Mini-Base]]
- [[ATH-MaaS__Marco-Mini-Global-Base|ATH-MaaS/Marco-Mini-Global-Base]]
- [[ATH-MaaS__Marco-Nano-Base|ATH-MaaS/Marco-Nano-Base]]
