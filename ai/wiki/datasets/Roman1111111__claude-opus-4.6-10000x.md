---
type: "dataset"
id: "Roman1111111/claude-opus-4.6-10000x"
source: "huggingface"
url: "https://huggingface.co/datasets/Roman1111111/claude-opus-4.6-10000x"
downloads: 3991
summary: "Claude Opus 4.6 모델의 수학적 정확성과 논리 추론을 학습하는 고품질 추론 데이터셋입니다."
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
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[학술·논문]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Roman1111111/claude-opus-4.6-10000x

> dataset · [Hugging Face](https://huggingface.co/datasets/Roman1111111/claude-opus-4.6-10000x)

Claude Opus 4.6 모델의 수학적 정확성과 논리 추론을 학습하는 고품질 추론 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `allowing smaller open-source models to inherit the sophisticated reasoning patterns of Claude Opus 4.6` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `The dataset is designed to capture the model's internal "Chain of Thought" and reasoning traces` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `Format: JSONL (Conversational with Reasoning Traces)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Format: JSONL (Conversational with Reasoning Traces)` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `Primary Categories: Mathematics, Symbolic Logic, General Purpose Problem Solving` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The dataset is intended for Supervised Fine-Tuning (SFT) and Distillation` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[CCSSNE__LuffyTheFox-OmniClaw-Qwen3.5-9B-Claude-4.6-Opus-Uncensored-v2-GGUF|CCSSNE/LuffyTheFox-OmniClaw-Qwen3.5-9B-Claude-4.6-Opus-Uncensored-v2-GGUF]]
- [[Flakily6416__Qwen3.5-27B-Opus-Reasoning-v2-Abliterated-EvoPress-GGUF|Flakily6416/Qwen3.5-27B-Opus-Reasoning-v2-Abliterated-EvoPress-GGUF]]
- [[Jackrong__MLX-Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-4bit|Jackrong/MLX-Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-4bit]]
- [[Jackrong__MLX-Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-6bit|Jackrong/MLX-Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-6bit]]
- [[Jackrong__MLX-Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-8bit|Jackrong/MLX-Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-8bit]]
- [[Jackrong__MLX-Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-4bit|Jackrong/MLX-Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-4bit]]
- [[Jackrong__Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2|Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2]]
- [[Jackrong__Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF|Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF]]
- [[Jackrong__Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-v2|Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-v2]]
- [[Jackrong__Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF|Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF]]
- [[Jackrong__Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2|Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2]]
- [[Jackrong__Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF|Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF]]
- [[Mungert__Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF|Mungert/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF]]
- [[Ngixdev__OmniCoder-Qwen3.5-9B-Claude-4.6-Opus-Uncensored-v2-GGUF|Ngixdev/OmniCoder-Qwen3.5-9B-Claude-4.6-Opus-Uncensored-v2-GGUF]]
- [[Octovayne__Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF|Octovayne/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF]]
- [[ansulev__OmniCoder-9B-Opus-4.6-Uncensored-v2-GGUF|ansulev/OmniCoder-9B-Opus-4.6-Uncensored-v2-GGUF]]
- [[ettradingmy__Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF|ettradingmy/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF]]
- [[marcoariette__OmniClaw-Qwen3.5-9B-Claude-4.6-Opus-Uncensored-v2-GGUF|marcoariette/OmniClaw-Qwen3.5-9B-Claude-4.6-Opus-Uncensored-v2-GGUF]]
- [[o87enterprise__Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF|o87enterprise/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF]]
- [[rcorvohan__Qwen3.5-122B-A10B-Opus-Reasoning-GGUF|rcorvohan/Qwen3.5-122B-A10B-Opus-Reasoning-GGUF]]
- [[timteh673__Qwen3.5-122B-A10B-Opus-Reasoning-GGUF|timteh673/Qwen3.5-122B-A10B-Opus-Reasoning-GGUF]]
- [[tritueviet__Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF|tritueviet/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF]]
- [[tritueviet__Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF|tritueviet/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF]]
- [[whitight__OmniCoder-Qwen3.5-9B-Claude-4.6-Opus-Uncensored-v2-GGUF|whitight/OmniCoder-Qwen3.5-9B-Claude-4.6-Opus-Uncensored-v2-GGUF]]
