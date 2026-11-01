---
type: "model"
id: "thelamapi/next2.5-i1-GGUF"
source: "huggingface"
url: "https://huggingface.co/thelamapi/next2.5-i1-GGUF"
downloads: 1283
task:
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
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
commercial_use:
  - "[[상업 이용 가능]]"
---
# thelamapi/next2.5-i1-GGUF

> model · [Hugging Face](https://huggingface.co/thelamapi/next2.5-i1-GGUF)

## 분류

- **작업**: [[이미지 이해]] — metadata · task.matched = `image-text-to-text` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:visual_qa = `text` · 신뢰도 medium
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
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high

## 학습 데이터

- [[CognitiveKernel__CognitiveKernel-Pro-SFT|CognitiveKernel/CognitiveKernel-Pro-SFT]]
- [[Gryphe__ChatGPT-4o-Writing-Prompts|Gryphe/ChatGPT-4o-Writing-Prompts]]
- [[OpenSPG__KAG-Thinker-training-dataset|OpenSPG/KAG-Thinker-training-dataset]]
- [[mlabonne__FineTome-100k|mlabonne/FineTome-100k]]
