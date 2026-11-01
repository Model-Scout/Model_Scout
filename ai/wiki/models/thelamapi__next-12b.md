---
type: "model"
id: "thelamapi/next-12b"
source: "huggingface"
url: "https://huggingface.co/thelamapi/next-12b"
downloads: 272
context_length: 131072
parameters_b: 12.187
task:
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
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
  - "[[상업 이용 가능]]"
model_size:
  - "[[중형 모델]]"
---
# thelamapi/next-12b

> model · [Hugging Face](https://huggingface.co/thelamapi/next-12b)

## 분류

- **작업**: [[이미지 이해]] — metadata · task.matched = `image-text-to-text` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `52 languages` · 신뢰도 high
- **입력 길이**: [[초장문]] — metadata · context_length = `131072` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **모델 크기**: [[중형 모델]] — metadata · parameter_count_billion = `12.187` · 신뢰도 high

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
- [[dongguanting__ARPO-SFT-54K|dongguanting/ARPO-SFT-54K]]
- [[mlabonne__FineTome-100k|mlabonne/FineTome-100k]]
- [[mlabonne__lmsys-arena-human-sft-55k|mlabonne/lmsys-arena-human-sft-55k]]
- [[mlabonne__natural_reasoning-formatted|mlabonne/natural_reasoning-formatted]]
- [[mlabonne__smoltalk-flat|mlabonne/smoltalk-flat]]
- [[uclanlp__Brief-Pro|uclanlp/Brief-Pro]]
