---
type: "model"
id: "NovaCorp/Gemma3.Novaciano-1B"
source: "huggingface"
url: "https://huggingface.co/NovaCorp/Gemma3.Novaciano-1B"
downloads: 202
context_length: 32768
parameters_b: 1.0
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
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[조건부 이용]]"
model_size:
  - "[[초경량 모델]]"
---
# NovaCorp/Gemma3.Novaciano-1B

> model · [Hugging Face](https://huggingface.co/NovaCorp/Gemma3.Novaciano-1B)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `46 languages` · 신뢰도 high
- **입력 길이**: [[초장문]] — metadata · context_length = `32768` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `gemma` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `1.0` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]]

## 학습 데이터

- [[CognitiveKernel__CognitiveKernel-Pro-SFT|CognitiveKernel/CognitiveKernel-Pro-SFT]]
- [[GreenerPastures__All-Your-Base-Full|GreenerPastures/All-Your-Base-Full]]
- [[Gryphe__ChatGPT-4o-Writing-Prompts|Gryphe/ChatGPT-4o-Writing-Prompts]]
- [[Gryphe__Opus-WritingPrompts|Gryphe/Opus-WritingPrompts]]
- [[HuggingFaceH4__MATH-500|HuggingFaceH4/MATH-500]]
- [[ITCL__FineTomeOs|ITCL/FineTomeOs]]
- [[OpenSPG__KAG-Thinker-training-dataset|OpenSPG/KAG-Thinker-training-dataset]]
- [[QuixiAI__dolphin-r1|QuixiAI/dolphin-r1]]
- [[SuperbEmphasis__Claude-4.0-DeepSeek-R1-RP-SFWish|SuperbEmphasis/Claude-4.0-DeepSeek-R1-RP-SFWish]]
- [[TeichAI__glm-4.7-2000x|TeichAI/glm-4.7-2000x]]
- [[berkeruveyik__toxic-speech-annotated-dataset|berkeruveyik/toxic-speech-annotated-dataset]]
- [[chimbiwide__RolePlay-NPCv2|chimbiwide/RolePlay-NPCv2]]
- [[dongguanting__ARPO-SFT-54K|dongguanting/ARPO-SFT-54K]]
- [[mlabonne__FineTome-100k|mlabonne/FineTome-100k]]
- [[mlabonne__lmsys-arena-human-sft-55k|mlabonne/lmsys-arena-human-sft-55k]]
- [[mlabonne__natural_reasoning-formatted|mlabonne/natural_reasoning-formatted]]
- [[mlabonne__smoltalk-flat|mlabonne/smoltalk-flat]]
- [[uclanlp__Brief-Pro|uclanlp/Brief-Pro]]
