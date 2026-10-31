---
type: "model"
id: "vllm-sr/Vela-1.0-Encoder-307M-Shield"
source: "huggingface"
url: "https://huggingface.co/vllm-sr/Vela-1.0-Encoder-307M-Shield"
downloads: 147
context_length: 32768
parameters_b: 0.308
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[초경량 모델]]"
---
# vllm-sr/Vela-1.0-Encoder-307M-Shield

> model · [Hugging Face](https://huggingface.co/vllm-sr/Vela-1.0-Encoder-307M-Shield)

## 분류

- **작업**: [[텍스트 분류]] — metadata · task.matched = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `17 languages` · 신뢰도 high
- **입력 길이**: [[초장문]] — metadata · context_length = `32768` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.308` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]]

## 학습 데이터

- [[OpenSafetyLab__Salad-Data|OpenSafetyLab/Salad-Data]]
- [[ToxicityPrompts__PolyGuardMix|ToxicityPrompts/PolyGuardMix]]
- [[microsoft__llmail-inject-challenge|microsoft/llmail-inject-challenge]]
- [[nvidia__Aegis-AI-Content-Safety-Dataset-2.0|nvidia/Aegis-AI-Content-Safety-Dataset-2.0]]
- [[nvidia__Nemotron-Safety-Guard-Dataset-v3|nvidia/Nemotron-Safety-Guard-Dataset-v3]]
