---
type: "model"
id: "Jiunsong/supergemma4-26b-abliterated-multimodal-mlx-4bit"
source: "huggingface"
url: "https://huggingface.co/Jiunsong/supergemma4-26b-abliterated-multimodal-mlx-4bit"
downloads: 858
context_length: 262144
parameters_b: 25.806
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
input_length:
  - "[[극장문]]"
commercial_use:
  - "[[조건부 이용]]"
model_size:
  - "[[중형 모델]]"
---
# Jiunsong/supergemma4-26b-abliterated-multimodal-mlx-4bit

> model · [Hugging Face](https://huggingface.co/Jiunsong/supergemma4-26b-abliterated-multimodal-mlx-4bit)

## 분류

- **작업**: [[이미지 이해]] — metadata · task.matched = `image-text-to-text` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **입력 길이**: [[극장문]] — metadata · context_length = `262144` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `gemma` · 신뢰도 high
- **모델 크기**: [[중형 모델]] — metadata · parameter_count_billion = `25.806` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]] · [[극장문]]
