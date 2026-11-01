---
type: "model"
id: "WaveCut/Qwen3.5-2B-MLX-DWQ-4bit"
source: "huggingface"
url: "https://huggingface.co/WaveCut/Qwen3.5-2B-MLX-DWQ-4bit"
downloads: 80
context_length: 262144
parameters_b: 2.213
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
  - "[[극장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[소형 모델]]"
---
# WaveCut/Qwen3.5-2B-MLX-DWQ-4bit

> model · [Hugging Face](https://huggingface.co/WaveCut/Qwen3.5-2B-MLX-DWQ-4bit)

## 분류

- **작업**: [[이미지 이해]] — metadata · task.matched = `image-text-to-text` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `16 languages` · 신뢰도 high
- **입력 길이**: [[극장문]] — metadata · context_length = `262144` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **모델 크기**: [[소형 모델]] — metadata · parameter_count_billion = `2.213` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]] · [[극장문]]

## 학습 데이터

- [[HuggingFaceFW__fineweb|HuggingFaceFW/fineweb]]
- [[HuggingFaceFW__fineweb-2|HuggingFaceFW/fineweb-2]]
- [[wikimedia__wikipedia|wikimedia/wikipedia]]
