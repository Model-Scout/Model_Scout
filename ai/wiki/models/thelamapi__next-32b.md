---
type: "model"
id: "thelamapi/next-32b"
source: "huggingface"
url: "https://huggingface.co/thelamapi/next-32b"
downloads: 92
context_length: 40960
parameters_b: 32.762
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[tr]]"
  - "[[중국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[중형 모델]]"
---
# thelamapi/next-32b

> model · [Hugging Face](https://huggingface.co/thelamapi/next-32b)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[de]] — metadata · language_codes = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · language_codes = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · language_codes = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · language_codes = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `9 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · language_codes = `ru` · 신뢰도 high
- **언어**: [[tr]] — metadata · language_codes = `tr` · 신뢰도 high
- **언어**: [[중국어]] — metadata · language_codes = `zh` · 신뢰도 high
- **입력 길이**: [[초장문]] — metadata · context_length = `40960` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **모델 크기**: [[중형 모델]] — metadata · parameter_count_billion = `32.762` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]]

## 학습 데이터

- [[CognitiveKernel__CognitiveKernel-Pro-SFT|CognitiveKernel/CognitiveKernel-Pro-SFT]]
- [[Gryphe__ChatGPT-4o-Writing-Prompts|Gryphe/ChatGPT-4o-Writing-Prompts]]
- [[OpenSPG__KAG-Thinker-training-dataset|OpenSPG/KAG-Thinker-training-dataset]]
- [[QuixiAI__dolphin-r1|QuixiAI/dolphin-r1]]
- [[mlabonne__FineTome-100k|mlabonne/FineTome-100k]]
- [[uclanlp__Brief-Pro|uclanlp/Brief-Pro]]
