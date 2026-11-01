---
type: "dataset"
id: "stepfun-ai/Step-3.5-Flash-SFT"
source: "huggingface"
url: "https://huggingface.co/datasets/stepfun-ai/Step-3.5-Flash-SFT"
downloads: 2396
summary: "Step-3.5-Flash-SFT는 챗 모델 학습용 일반 도메인 감독 학습 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# stepfun-ai/Step-3.5-Flash-SFT

> dataset · [Hugging Face](https://huggingface.co/datasets/stepfun-ai/Step-3.5-Flash-SFT)

Step-3.5-Flash-SFT는 챗 모델 학습용 일반 도메인 감독 학습 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, tags, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation = `Each example currently contains a `conversations` field with ordered message turns.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Training loss is applied only to assistant tokens after the last user turn when that turn has `loss_mask = 1`.` · 신뢰도 medium
- **언어**: [[다국어]] — metadata · languages = `multilingual` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Step-3.5-Flash-SFT is a general-domain supervised fine-tuning release for chat models.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This is a training corpus, not a benchmark.` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[Jackrong__Qwen3.5-4B-Neo|Jackrong/Qwen3.5-4B-Neo]]
- [[Jackrong__Qwen3.5-4B-Neo-GGUF|Jackrong/Qwen3.5-4B-Neo-GGUF]]
- [[bartowski__Jackrong_Qwen3.5-4B-Neo-GGUF|bartowski/Jackrong_Qwen3.5-4B-Neo-GGUF]]
