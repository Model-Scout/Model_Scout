---
type: "model"
id: "ncls-p/Qwen2.5-7B-blog-key-points"
source: "huggingface"
url: "https://huggingface.co/ncls-p/Qwen2.5-7B-blog-key-points"
downloads: 112
context_length: 32768
task:
  - "[[요약]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
---
# ncls-p/Qwen2.5-7B-blog-key-points

> model · [Hugging Face](https://huggingface.co/ncls-p/Qwen2.5-7B-blog-key-points)

## 분류

- **작업**: [[요약]] — metadata · task.matched = `summarization` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:summarization = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:summarization = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `13 languages` · 신뢰도 high
- **입력 길이**: [[초장문]] — metadata · context_length = `32768` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]]

## 학습 데이터

- [[ncls-p__blog-key-points|ncls-p/blog-key-points]]
