---
type: "dataset"
id: "lordx64/reasoning-distill-opus-4-7-max-sft"
source: "huggingface"
url: "https://huggingface.co/datasets/lordx64/reasoning-distill-opus-4-7-max-sft"
downloads: 87
summary: "Claude Opus 4.7의 추론 대화 데이터를 SFT 학습용으로 재구성한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
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
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# lordx64/reasoning-distill-opus-4-7-max-sft

> dataset · [Hugging Face](https://huggingface.co/datasets/lordx64/reasoning-distill-opus-4-7-max-sft)

Claude Opus 4.7의 추론 대화 데이터를 SFT 학습용으로 재구성한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Ready to feed to `SFTTrainer` with `dataset_text_field="text"`. The model we trained uses `train_on_responses_only` to mask loss on the user/system side — gradi` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `Each row is a single `text` field containing a full Qwen-style chat-template conversation.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Every conversation's assistant response (including the ` ... ` block) is output from **`claude-opus-4-7`** with Anthropic's `extended-thinking` enabled.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2091` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Reasoning traces from Claude Opus 4.7 — SFT-ready` · 신뢰도 low
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 8365자 ≈ 2091 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[nabi-chan__Qwen3.6-35B-A3B-Claude-4.7-Opus-abliterated-MLX-4bit|nabi-chan/Qwen3.6-35B-A3B-Claude-4.7-Opus-abliterated-MLX-4bit]]
- [[nabi-chan__Qwen3.6-35B-A3B-Claude-4.7-Opus-abliterated-MLX-5bit|nabi-chan/Qwen3.6-35B-A3B-Claude-4.7-Opus-abliterated-MLX-5bit]]
