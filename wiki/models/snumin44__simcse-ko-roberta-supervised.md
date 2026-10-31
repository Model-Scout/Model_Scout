---
type: "model"
id: "snumin44/simcse-ko-roberta-supervised"
source: "huggingface"
url: "https://huggingface.co/snumin44/simcse-ko-roberta-supervised"
downloads: 123
context_length: 514
parameters_b: 0.111
task:
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[초경량 모델]]"
---
# snumin44/simcse-ko-roberta-supervised

> model · [Hugging Face](https://huggingface.co/snumin44/simcse-ko-roberta-supervised)

## 분류

- **작업**: [[임베딩]] — metadata · task.matched = `sentence-similarity` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — metadata · context_length = `514` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.111` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]]

## 학습 데이터

- [[kakaobrain__kor_nli|kakaobrain/kor_nli]]
- [[kakaobrain__kor_nlu|kakaobrain/kor_nlu]]
- [[klue__klue|klue/klue]]
