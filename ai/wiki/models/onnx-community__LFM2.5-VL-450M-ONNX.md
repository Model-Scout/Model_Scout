---
type: "model"
id: "onnx-community/LFM2.5-VL-450M-ONNX"
source: "huggingface"
url: "https://huggingface.co/onnx-community/LFM2.5-VL-450M-ONNX"
downloads: 1166
context_length: 128000
task:
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
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
  - "[[중국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[조건부 이용]]"
---
# onnx-community/LFM2.5-VL-450M-ONNX

> model · [Hugging Face](https://huggingface.co/onnx-community/LFM2.5-VL-450M-ONNX)

## 분류

- **작업**: [[이미지 이해]] — metadata · task.matched = `image-text-to-text` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[ar]] — metadata · language_codes = `ar` · 신뢰도 high
- **언어**: [[de]] — metadata · language_codes = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · language_codes = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · language_codes = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · language_codes = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `9 languages` · 신뢰도 high
- **언어**: [[pt]] — metadata · language_codes = `pt` · 신뢰도 high
- **언어**: [[중국어]] — metadata · language_codes = `zh` · 신뢰도 high
- **입력 길이**: [[초장문]] — metadata · context_length = `128000` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]]
