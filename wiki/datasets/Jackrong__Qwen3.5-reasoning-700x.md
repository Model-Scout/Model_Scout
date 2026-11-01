---
type: "dataset"
id: "Jackrong/Qwen3.5-reasoning-700x"
source: "huggingface"
url: "https://huggingface.co/datasets/Jackrong/Qwen3.5-reasoning-700x"
downloads: 275
summary: "Qwen3.5-27B 모델이 생성한 고품질 추론 데이터셋으로 수학, 코드, 논리, 과학 분야 포함."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[초장문]]"
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
# Jackrong/Qwen3.5-reasoning-700x

> dataset · [Hugging Face](https://huggingface.co/datasets/Jackrong/Qwen3.5-reasoning-700x)

Qwen3.5-27B 모델이 생성한 고품질 추론 데이터셋으로 수학, 코드, 논리, 과학 분야 포함.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `it generates high-quality responses featuring long-text reasoning processes (Chain-of-Thought)` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `high-quality instructions constructed by Alibaba-Superior-Reasoning-Stage2 as the seed question set` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `it generates high-quality responses featuring long-text reasoning processes (Chain-of-Thought)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `24783` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `It covers several major domains: Mathematics | Code | Logic | Science | Instructions.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `It is highly recommended to conduct sample quality inspections before proceeding with fine-tuning.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 99134자 ≈ 24783 토큰 (viewer statistics, default/train)

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
- [[Jackrong__Qwen3.5-27B-Gemini-3.1-Pro-Reasoning-Distill|Jackrong/Qwen3.5-27B-Gemini-3.1-Pro-Reasoning-Distill]]
- [[Jackrong__Qwen3.5-27B-Gemini-3.1-Pro-Reasoning-Distill-GGUF|Jackrong/Qwen3.5-27B-Gemini-3.1-Pro-Reasoning-Distill-GGUF]]
- [[Jackrong__Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled|Jackrong/Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled]]
- [[Jackrong__Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled|Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled]]
- [[Jackrong__Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF|Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF]]
- [[Jackrong__Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-v2|Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-v2]]
- [[Jackrong__Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF|Jackrong/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF]]
- [[Jackrong__Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled|Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled]]
- [[Jackrong__Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2|Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2]]
- [[Jackrong__Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF|Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF]]
- [[Jackrong__Qwen3.5-9B-Gemini-3.1-Pro-Reasoning-Distill|Jackrong/Qwen3.5-9B-Gemini-3.1-Pro-Reasoning-Distill]]
- [[Jackrong__Qwen3.5-9B-Gemini-3.1-Pro-Reasoning-Distill-GGUF|Jackrong/Qwen3.5-9B-Gemini-3.1-Pro-Reasoning-Distill-GGUF]]
- [[Jackrong__Qwopus3.6-27B-v1-preview-GGUF|Jackrong/Qwopus3.6-27B-v1-preview-GGUF]]
- [[Kamets__Qwen3.5-0.8B-Claude-4.6-Opus-Reasoning-Distilled-GGUF|Kamets/Qwen3.5-0.8B-Claude-4.6-Opus-Reasoning-Distilled-GGUF]]
- [[Momix-44__Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled-GGUF|Momix-44/Qwen3.5-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled-GGUF]]
- [[Mungert__Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF|Mungert/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF]]
- [[Ngixdev__OmniCoder-Qwen3.5-9B-Claude-4.6-Opus-Uncensored-v2-GGUF|Ngixdev/OmniCoder-Qwen3.5-9B-Claude-4.6-Opus-Uncensored-v2-GGUF]]
- [[Octovayne__Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF|Octovayne/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF]]
- [[Oleg-On__Qwen3.5-14B-A3B-Claude-4.6-Opus-Reasoning-Distilled-reap-Q4_K_M-GGUF|Oleg-On/Qwen3.5-14B-A3B-Claude-4.6-Opus-Reasoning-Distilled-reap-Q4_K_M-GGUF]]
- [[P4tchFake__Qwen3.5-9B-Gemini-3.1-Pro-Reasoning-Distill-GGUF|P4tchFake/Qwen3.5-9B-Gemini-3.1-Pro-Reasoning-Distill-GGUF]]
- [[RazielGuinhos__Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF|RazielGuinhos/Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-GGUF]]
- [[Tet3u__Qwen3.5-9B-Gemini-3.1-Pro-Reasoning-Distill-GGUF|Tet3u/Qwen3.5-9B-Gemini-3.1-Pro-Reasoning-Distill-GGUF]]
- [[ansulev__OmniCoder-9B-Opus-4.6-Uncensored-v2-GGUF|ansulev/OmniCoder-9B-Opus-4.6-Uncensored-v2-GGUF]]
- [[bakulgrosirherbal__Qwen3.5-9B-Gemini-3.1-Pro-Reasoning-Distill-GGUF|bakulgrosirherbal/Qwen3.5-9B-Gemini-3.1-Pro-Reasoning-Distill-GGUF]]
- [[brunopio__Qwen3.5-14B-A3B-Claude-4.6-Opus-Reasoning-Distilled-reap-Q2_K-GGUF|brunopio/Qwen3.5-14B-A3B-Claude-4.6-Opus-Reasoning-Distilled-reap-Q2_K-GGUF]]
- [[brunopio__Qwen3.5-14B-A3B-Claude-4.6-Opus-Reasoning-Distilled-reap-Q4_K_M-GGUF|brunopio/Qwen3.5-14B-A3B-Claude-4.6-Opus-Reasoning-Distilled-reap-Q4_K_M-GGUF]]
- [[ettradingmy__Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF|ettradingmy/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2-GGUF]]
- [[fa123zil__Qwen3.5-9B-Gemini-3.1-Pro-Reasoning-Distill-GGUF|fa123zil/Qwen3.5-9B-Gemini-3.1-Pro-Reasoning-Distill-GGUF]]
- [[jacehoi__Qwen3.5-35B-A3B-Uncensored-Claude-Opus-4.6-Affine|jacehoi/Qwen3.5-35B-A3B-Uncensored-Claude-Opus-4.6-Affine]]
- [[luckiness__Qwopus3.6-27B-v1-preview-GGUF|luckiness/Qwopus3.6-27B-v1-preview-GGUF]]
- [[marcoariette__OmniClaw-Qwen3.5-9B-Claude-4.6-Opus-Uncensored-v2-GGUF|marcoariette/OmniClaw-Qwen3.5-9B-Claude-4.6-Opus-Uncensored-v2-GGUF]]
- [[mikehenken__Qwen3.5-27B-Gemini-3.1-Pro-Reasoning-Distill-GGUF|mikehenken/Qwen3.5-27B-Gemini-3.1-Pro-Reasoning-Distill-GGUF]]
- [[mradermacher__Qwopus3.6-27B-v1-preview-GGUF|mradermacher/Qwopus3.6-27B-v1-preview-GGUF]]
- [[mradermacher__Qwopus3.6-27B-v1-preview-i1-GGUF|mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF]]
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
