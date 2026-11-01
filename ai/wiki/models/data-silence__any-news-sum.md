---
type: "model"
id: "data-silence/any-news-sum"
source: "huggingface"
url: "https://huggingface.co/data-silence/any-news-sum"
downloads: 83
parameters_b: 0.582
task:
  - "[[요약]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
model_size:
  - "[[초경량 모델]]"
---
# data-silence/any-news-sum

> model · [Hugging Face](https://huggingface.co/data-silence/any-news-sum)

## 분류

- **작업**: [[요약]] — metadata · task.matched = `summarization` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:summarization = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:summarization = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `43 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.582` · 신뢰도 high

## 학습 데이터

- [[csebuetnlp__xlsum|csebuetnlp/xlsum]]
- [[data-silence__sumnews|data-silence/sumnews]]
