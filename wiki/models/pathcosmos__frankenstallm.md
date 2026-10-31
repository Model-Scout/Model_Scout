---
type: "model"
id: "pathcosmos/frankenstallm"
source: "huggingface"
url: "https://huggingface.co/pathcosmos/frankenstallm"
downloads: 289
context_length: 4096
parameters_b: 3.016
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
# pathcosmos/frankenstallm

> model · [Hugging Face](https://huggingface.co/pathcosmos/frankenstallm)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — metadata · context_length = `4096` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **모델 크기**: [[소형 모델]] — metadata · parameter_count_billion = `3.016` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]]

## 학습 데이터

- [[HuggingFaceTB__cosmopedia|HuggingFaceTB/cosmopedia]]
- [[allenai__c4|allenai/c4]]
- [[heegyu__orca-math-korean-preference-cleaned|heegyu/orca-math-korean-preference-cleaned]]
- [[maywell__ko_Ultrafeedback_binarized|maywell/ko_Ultrafeedback_binarized]]
- [[nayohan__preference-collection-ko-full|nayohan/preference-collection-ko-full]]
- [[statmt__cc100|statmt/cc100]]
- [[wikimedia__wikipedia|wikimedia/wikipedia]]
