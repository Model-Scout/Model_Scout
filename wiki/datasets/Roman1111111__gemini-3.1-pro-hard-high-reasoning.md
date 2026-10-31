---
type: "dataset"
id: "Roman1111111/gemini-3.1-pro-hard-high-reasoning"
source: "huggingface"
url: "https://huggingface.co/datasets/Roman1111111/gemini-3.1-pro-hard-high-reasoning"
downloads: 3871
summary: "Gemini 3.1 Pro가 생성한 고난도 논리 추론 데이터셋으로, 복잡한 다단계 검증 문제 해결에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[리랭킹]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
  - "[[법률]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Roman1111111/gemini-3.1-pro-hard-high-reasoning

> dataset · [Hugging Face](https://huggingface.co/datasets/Roman1111111/gemini-3.1-pro-hard-high-reasoning)

Gemini 3.1 Pro가 생성한 고난도 논리 추론 데이터셋으로, 복잡한 다단계 검증 문제 해결에 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Ideal for fine-tuning 7B-70B models to reach "Expert-level" performance in technical sub-fields.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `Serving as a "Gold Standard" test set for other reasoning models (e.g., O1, Claude 3.5 Opus).` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:question_answering, task:reranking = `The user prompt should be detailed (code snippets, math proofs, or philosophical paradoxes).` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `The verified solution provided by Gemini 3.1 Pro` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1525` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · tags = `finance` · 신뢰도 medium
- **도메인**: [[법률]] — tag_match · tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `Serving as a "Gold Standard" test set for other reasoning models (e.g., O1, Claude 3.5 Opus).` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Ideal for fine-tuning 7B-70B models to reach "Expert-level" performance in technical sub-fields.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `model_response` 열 p90 6101자 ≈ 1525 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[Jackrong__Qwen3.5-27B-Gemini-3.1-Pro-Reasoning-Distill|Jackrong/Qwen3.5-27B-Gemini-3.1-Pro-Reasoning-Distill]]
- [[Jackrong__Qwen3.5-27B-Gemini-3.1-Pro-Reasoning-Distill-GGUF|Jackrong/Qwen3.5-27B-Gemini-3.1-Pro-Reasoning-Distill-GGUF]]
- [[Jackrong__Qwen3.5-9B-Gemini-3.1-Pro-Reasoning-Distill|Jackrong/Qwen3.5-9B-Gemini-3.1-Pro-Reasoning-Distill]]
- [[Jackrong__Qwen3.5-9B-Gemini-3.1-Pro-Reasoning-Distill-GGUF|Jackrong/Qwen3.5-9B-Gemini-3.1-Pro-Reasoning-Distill-GGUF]]
- [[P4tchFake__Qwen3.5-9B-Gemini-3.1-Pro-Reasoning-Distill-GGUF|P4tchFake/Qwen3.5-9B-Gemini-3.1-Pro-Reasoning-Distill-GGUF]]
- [[Tet3u__Qwen3.5-9B-Gemini-3.1-Pro-Reasoning-Distill-GGUF|Tet3u/Qwen3.5-9B-Gemini-3.1-Pro-Reasoning-Distill-GGUF]]
- [[bakulgrosirherbal__Qwen3.5-9B-Gemini-3.1-Pro-Reasoning-Distill-GGUF|bakulgrosirherbal/Qwen3.5-9B-Gemini-3.1-Pro-Reasoning-Distill-GGUF]]
- [[fa123zil__Qwen3.5-9B-Gemini-3.1-Pro-Reasoning-Distill-GGUF|fa123zil/Qwen3.5-9B-Gemini-3.1-Pro-Reasoning-Distill-GGUF]]
- [[mikehenken__Qwen3.5-27B-Gemini-3.1-Pro-Reasoning-Distill-GGUF|mikehenken/Qwen3.5-27B-Gemini-3.1-Pro-Reasoning-Distill-GGUF]]
