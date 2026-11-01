---
type: "dataset"
id: "nohurry/Opus-4.6-Reasoning-3000x-filtered"
source: "huggingface"
url: "https://huggingface.co/datasets/nohurry/Opus-4.6-Reasoning-3000x-filtered"
downloads: 470
summary: "Opus-4.6-Reasoning-3000x 데이터셋에서 거부 문장을 제거한 필터링 버전입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# nohurry/Opus-4.6-Reasoning-3000x-filtered

> dataset · [Hugging Face](https://huggingface.co/datasets/nohurry/Opus-4.6-Reasoning-3000x-filtered)

Opus-4.6-Reasoning-3000x 데이터셋에서 거부 문장을 제거한 필터링 버전입니다.

## 분류

- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `649` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The original dataset has 979 refusals, I removed these in this version.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `solution` 열 p90 2595자 ≈ 649 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[CCSSNE__LuffyTheFox-OmniClaw-Qwen3.5-9B-Claude-4.6-Opus-Uncensored-v2-GGUF|CCSSNE/LuffyTheFox-OmniClaw-Qwen3.5-9B-Claude-4.6-Opus-Uncensored-v2-GGUF]]
- [[Flakily6416__Qwen3.5-27B-Opus-Reasoning-v2-Abliterated-EvoPress-GGUF|Flakily6416/Qwen3.5-27B-Opus-Reasoning-v2-Abliterated-EvoPress-GGUF]]
- [[Jackrong__MLX-Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-4bit|Jackrong/MLX-Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-4bit]]
- [[Jackrong__MLX-Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-6bit|Jackrong/MLX-Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-6bit]]
- [[Jackrong__MLX-Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-8bit|Jackrong/MLX-Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-8bit]]
- [[Jackrong__MLX-Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled-4bit|Jackrong/MLX-Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled-4bit]]
- [[Jackrong__MLX-Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled-8bit|Jackrong/MLX-Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled-8bit]]
- [[Jackrong__MLX-Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-4bit|Jackrong/MLX-Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-4bit]]
- [[Jackrong__Qwen3.5-0.8B-Claude-4.6-Opus-Reasoning-Distilled|Jackrong/Qwen3.5-0.8B-Claude-4.6-Opus-Reasoning-Distilled]]
- [[Jackrong__Qwen3.5-0.8B-Claude-4.6-Opus-Reasoning-Distilled-GGUF|Jackrong/Qwen3.5-0.8B-Claude-4.6-Opus-Reasoning-Distilled-GGUF]]
- [[Jackrong__Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2|Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2]]
- [[Jackrong__Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF|Jackrong/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF]]
- [[Jackrong__Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled|Jackrong/Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled]]
- [[Jackrong__Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled|Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled]]
- [[Jackrong__Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF|Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF]]
- [[Jackrong__Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-v2|Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-v2]]
- [[Jackrong__Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF|Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF]]
- [[Jackrong__Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled|Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled]]
- [[Jackrong__Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2|Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2]]
- [[Jackrong__Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF|Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF]]
- [[Kamets__Qwen3.5-0.8B-Claude-4.6-Opus-Reasoning-Distilled-GGUF|Kamets/Qwen3.5-0.8B-Claude-4.6-Opus-Reasoning-Distilled-GGUF]]
- [[Momix-44__Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled-GGUF|Momix-44/Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled-GGUF]]
- [[Mungert__Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF|Mungert/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF]]
- [[Ngixdev__OmniCoder-Qwen3.5-9B-Claude-4.6-Opus-Uncensored-v2-GGUF|Ngixdev/OmniCoder-Qwen3.5-9B-Claude-4.6-Opus-Uncensored-v2-GGUF]]
- [[Octovayne__Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF|Octovayne/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF]]
- [[Oleg-On__Qwen3.5-14B-A3B-Claude-4.6-Opus-Reasoning-Distilled-reap-Q4_K_M-GGUF|Oleg-On/Qwen3.5-14B-A3B-Claude-4.6-Opus-Reasoning-Distilled-reap-Q4_K_M-GGUF]]
- [[RazielGuinhos__Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF|RazielGuinhos/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF]]
- [[ansulev__OmniCoder-9B-Opus-4.6-Uncensored-v2-GGUF|ansulev/OmniCoder-9B-Opus-4.6-Uncensored-v2-GGUF]]
- [[brunopio__Qwen3.5-14B-A3B-Claude-4.6-Opus-Reasoning-Distilled-reap-Q2_K-GGUF|brunopio/Qwen3.5-14B-A3B-Claude-4.6-Opus-Reasoning-Distilled-reap-Q2_K-GGUF]]
- [[brunopio__Qwen3.5-14B-A3B-Claude-4.6-Opus-Reasoning-Distilled-reap-Q4_K_M-GGUF|brunopio/Qwen3.5-14B-A3B-Claude-4.6-Opus-Reasoning-Distilled-reap-Q4_K_M-GGUF]]
- [[ettradingmy__Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF|ettradingmy/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF]]
- [[jacehoi__Qwen3.5-35B-A3B-Uncensored-Claude-Opus-4.6-Affine|jacehoi/Qwen3.5-35B-A3B-Uncensored-Claude-Opus-4.6-Affine]]
- [[marcoariette__OmniClaw-Qwen3.5-9B-Claude-4.6-Opus-Uncensored-v2-GGUF|marcoariette/OmniClaw-Qwen3.5-9B-Claude-4.6-Opus-Uncensored-v2-GGUF]]
- [[o87enterprise__Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF|o87enterprise/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF]]
- [[rcorvohan__Qwen3.5-122B-A10B-Opus-Reasoning-GGUF|rcorvohan/Qwen3.5-122B-A10B-Opus-Reasoning-GGUF]]
- [[sujinwo__Qwen3.5-0.8B-Claude-4.6-Opus|sujinwo/Qwen3.5-0.8B-Claude-4.6-Opus]]
- [[sujinwo__Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF|sujinwo/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF]]
- [[sukai-123__Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF|sukai-123/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF]]
- [[timteh673__Qwen3.5-122B-A10B-Opus-Reasoning-GGUF|timteh673/Qwen3.5-122B-A10B-Opus-Reasoning-GGUF]]
- [[tritueviet__Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF|tritueviet/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF]]
- [[tritueviet__Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF|tritueviet/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF]]
- [[tvall43__Qwen3.5-14B-A3B-Claude-4.6-Opus-Reasoning-Distilled-reap|tvall43/Qwen3.5-14B-A3B-Claude-4.6-Opus-Reasoning-Distilled-reap]]
- [[tvall43__Qwen3.5-14B-A3B-Claude-4.6-Opus-Reasoning-Distilled-reap-gguf|tvall43/Qwen3.5-14B-A3B-Claude-4.6-Opus-Reasoning-Distilled-reap-gguf]]
- [[whitight__OmniCoder-Qwen3.5-9B-Claude-4.6-Opus-Uncensored-v2-GGUF|whitight/OmniCoder-Qwen3.5-9B-Claude-4.6-Opus-Uncensored-v2-GGUF]]
