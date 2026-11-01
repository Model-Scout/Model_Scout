---
type: "model"
id: "daekeun-ml/phi-2-ko-v0.1"
source: "huggingface"
url: "https://huggingface.co/daekeun-ml/phi-2-ko-v0.1"
downloads: 193
context_length: 2048
parameters_b: 2.859
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[소형 모델]]"
---
# daekeun-ml/phi-2-ko-v0.1

> model · [Hugging Face](https://huggingface.co/daekeun-ml/phi-2-ko-v0.1)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — metadata · context_length = `2048` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-3.0` · 신뢰도 high
- **모델 크기**: [[소형 모델]] — metadata · parameter_count_billion = `2.859` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]]

## 학습 데이터

- [[Open-Orca__OpenOrca|Open-Orca/OpenOrca]]
- [[maywell__korean_textbooks|maywell/korean_textbooks]]
- [[nampdn-ai__tiny-codes|nampdn-ai/tiny-codes]]
- [[wikimedia__wikipedia|wikimedia/wikipedia]]
