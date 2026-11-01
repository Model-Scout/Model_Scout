---
type: "model"
id: "vllm-sr/mmbert32k-modality-router-merged"
source: "huggingface"
url: "https://huggingface.co/vllm-sr/mmbert32k-modality-router-merged"
downloads: 5091
context_length: 32768
parameters_b: 0.308
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[pt]]"
  - "[[ru]]"
  - "[[중국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[초경량 모델]]"
---
# vllm-sr/mmbert32k-modality-router-merged

> model · [Hugging Face](https://huggingface.co/vllm-sr/mmbert32k-modality-router-merged)

## 분류

- **작업**: [[텍스트 분류]] — metadata · task.matched = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **언어**: [[ar]] — metadata · language_codes = `ar` · 신뢰도 high
- **언어**: [[de]] — metadata · language_codes = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · language_codes = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · language_codes = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · language_codes = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `10 languages` · 신뢰도 high
- **언어**: [[pt]] — metadata · language_codes = `pt` · 신뢰도 high
- **언어**: [[ru]] — metadata · language_codes = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · language_codes = `zh` · 신뢰도 high
- **입력 길이**: [[초장문]] — metadata · context_length = `32768` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.308` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]]

## 학습 데이터

- [[FredZhang7__stable-diffusion-prompts-2.47M|FredZhang7/stable-diffusion-prompts-2.47M]]
- [[Gustavosta__Stable-Diffusion-Prompts|Gustavosta/Stable-Diffusion-Prompts]]
- [[OpenAssistant__oasst2|OpenAssistant/oasst2]]
- [[allenai__WildChat|allenai/WildChat]]
- [[databricks__databricks-dolly-15k|databricks/databricks-dolly-15k]]
- [[fal__image-generation-prompts|fal/image-generation-prompts]]
- [[nateraw__parti-prompts|nateraw/parti-prompts]]
- [[openbmb__UltraChat|openbmb/UltraChat]]
- [[tatsu-lab__alpaca|tatsu-lab/alpaca]]
