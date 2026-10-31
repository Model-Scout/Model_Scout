---
type: "model"
id: "Horizon-Labs/prompt-injection-guard-small"
source: "huggingface"
url: "https://huggingface.co/Horizon-Labs/prompt-injection-guard-small"
downloads: 154
context_length: 8192
parameters_b: 0.141
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[초경량 모델]]"
---
# Horizon-Labs/prompt-injection-guard-small

> model · [Hugging Face](https://huggingface.co/Horizon-Labs/prompt-injection-guard-small)

## 분류

- **작업**: [[텍스트 분류]] — metadata · task.matched = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `19 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — metadata · context_length = `8192` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.141` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]]

## 학습 데이터

- [[3nesdeniz__agentic-prompt-injection-5k|3nesdeniz/agentic-prompt-injection-5k]]
- [[CohereLabs__aya_dataset|CohereLabs/aya_dataset]]
- [[HuggingFaceFW__fineweb-2|HuggingFaceFW/fineweb-2]]
- [[HuggingFaceFW__fineweb-edu|HuggingFaceFW/fineweb-edu]]
- [[JailbreakV-28K__JailBreakV-28k|JailbreakV-28K/JailBreakV-28k]]
- [[OpenAssistant__oasst2|OpenAssistant/oasst2]]
- [[S-Labs__prompt-injection-dataset|S-Labs/prompt-injection-dataset]]
- [[TrustAIRLab__in-the-wild-jailbreak-prompts|TrustAIRLab/in-the-wild-jailbreak-prompts]]
- [[hendzh__PromptShield|hendzh/PromptShield]]
- [[microsoft__llmail-inject-challenge|microsoft/llmail-inject-challenge]]
- [[neuralchemy__Prompt-injection-dataset|neuralchemy/Prompt-injection-dataset]]
- [[nvidia__Nemotron-RL-Agentic-Indirect-Prompt-Injection-v1|nvidia/Nemotron-RL-Agentic-Indirect-Prompt-Injection-v1]]
- [[nvidia__Nemotron-RL-Jailbreak-Robustness-v1|nvidia/Nemotron-RL-Jailbreak-Robustness-v1]]
- [[rgeada__tool-response-injections|rgeada/tool-response-injections]]
