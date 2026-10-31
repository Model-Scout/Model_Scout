---
type: "model"
id: "Jackrong/MLX-Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-8bit"
source: "huggingface"
url: "https://huggingface.co/Jackrong/MLX-Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-8bit"
downloads: 256
context_length: 262144
parameters_b: 26.896
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
input_length:
  - "[[극장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[중형 모델]]"
---
# Jackrong/MLX-Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-8bit

> model · [Hugging Face](https://huggingface.co/Jackrong/MLX-Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2-8bit)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `3 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · language_codes = `zh` · 신뢰도 high
- **입력 길이**: [[극장문]] — metadata · context_length = `262144` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **모델 크기**: [[중형 모델]] — metadata · parameter_count_billion = `26.896` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]] · [[극장문]]

## 학습 데이터

- [[Jackrong__Qwen3.5-reasoning-700x|Jackrong/Qwen3.5-reasoning-700x]]
- [[Roman1111111__claude-opus-4.6-10000x|Roman1111111/claude-opus-4.6-10000x]]
- [[nohurry__Opus-4.6-Reasoning-3000x-filtered|nohurry/Opus-4.6-Reasoning-3000x-filtered]]
