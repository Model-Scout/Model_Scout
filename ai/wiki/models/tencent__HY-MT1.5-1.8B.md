---
type: "model"
id: "tencent/HY-MT1.5-1.8B"
source: "huggingface"
url: "https://huggingface.co/tencent/HY-MT1.5-1.8B"
downloads: 6244
context_length: 262144
parameters_b: 2.039
task:
  - "[[번역]]"
input_modality:
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
  - "[[이용 조건 미확인]]"
model_size:
  - "[[소형 모델]]"
---
# tencent/HY-MT1.5-1.8B

> model · [Hugging Face](https://huggingface.co/tencent/HY-MT1.5-1.8B)

## 분류

- **작업**: [[번역]] — metadata · task.matched = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:translation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `36 languages` · 신뢰도 high
- **입력 길이**: [[극장문]] — metadata · context_length = `262144` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **모델 크기**: [[소형 모델]] — metadata · parameter_count_billion = `2.039` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]] · [[극장문]]
