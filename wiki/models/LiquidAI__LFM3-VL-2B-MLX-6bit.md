---
type: "model"
id: "LiquidAI/LFM3-VL-2B-MLX-6bit"
source: "huggingface"
url: "https://huggingface.co/LiquidAI/LFM3-VL-2B-MLX-6bit"
downloads: 137
context_length: 128000
parameters_b: 1.918
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
  - "[[조건부 이용]]"
model_size:
  - "[[소형 모델]]"
---
# LiquidAI/LFM3-VL-2B-MLX-6bit

> model · [Hugging Face](https://huggingface.co/LiquidAI/LFM3-VL-2B-MLX-6bit)

## 분류

- **작업**: [[이미지 이해]] — metadata · task.matched = `image-text-to-text` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `16 languages` · 신뢰도 high
- **입력 길이**: [[초장문]] — metadata · context_length = `128000` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **모델 크기**: [[소형 모델]] — metadata · parameter_count_billion = `1.918` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]]
