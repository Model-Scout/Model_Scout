---
type: "model"
id: "prismdata/Perdix-1.1B-Instruct"
source: "huggingface"
url: "https://huggingface.co/prismdata/Perdix-1.1B-Instruct"
downloads: 515
context_length: 2048
parameters_b: 1.107
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
# prismdata/Perdix-1.1B-Instruct

> model · [Hugging Face](https://huggingface.co/prismdata/Perdix-1.1B-Instruct)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — metadata · context_length = `2048` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **모델 크기**: [[소형 모델]] — metadata · parameter_count_billion = `1.107` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]]

## 학습 데이터

- [[HuggingFaceTB__smoltalk|HuggingFaceTB/smoltalk]]
- [[heegyu__open-korean-instructions|heegyu/open-korean-instructions]]
- [[nlpai-lab__kullm-v2|nlpai-lab/kullm-v2]]
- [[prismdata__Perdix-SFT-Data|prismdata/Perdix-SFT-Data]]
