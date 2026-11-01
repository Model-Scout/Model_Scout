---
type: "model"
id: "haoranxu/X-ALMA-13B-Pretrain"
source: "huggingface"
url: "https://huggingface.co/haoranxu/X-ALMA-13B-Pretrain"
downloads: 280
context_length: 4096
parameters_b: 13.016
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[중형 모델]]"
---
# haoranxu/X-ALMA-13B-Pretrain

> model · [Hugging Face](https://huggingface.co/haoranxu/X-ALMA-13B-Pretrain)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `50 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — metadata · context_length = `4096` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **모델 크기**: [[중형 모델]] — metadata · parameter_count_billion = `13.016` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]]

## 학습 데이터

- [[Helsinki-NLP__opus-100|Helsinki-NLP/opus-100]]
- [[allenai__nllb|allenai/nllb]]
- [[oscar-corpus__OSCAR-2301|oscar-corpus/OSCAR-2301]]
