---
type: "model"
id: "TheCluster/Qwen3.5-122B-A10B-Heretic-v2-MLX-mixed-6bit"
source: "huggingface"
url: "https://huggingface.co/TheCluster/Qwen3.5-122B-A10B-Heretic-v2-MLX-mixed-6bit"
downloads: 157
context_length: 262144
parameters_b: 122.563
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
  - "[[대형 모델]]"
---
# TheCluster/Qwen3.5-122B-A10B-Heretic-v2-MLX-mixed-6bit

> model · [Hugging Face](https://huggingface.co/TheCluster/Qwen3.5-122B-A10B-Heretic-v2-MLX-mixed-6bit)

## 분류

- **작업**: [[이미지 이해]] — metadata · task.matched = `image-text-to-text` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `26 languages` · 신뢰도 high
- **입력 길이**: [[극장문]] — metadata · context_length = `262144` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **모델 크기**: [[대형 모델]] — metadata · parameter_count_billion = `122.563` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]] · [[극장문]]
