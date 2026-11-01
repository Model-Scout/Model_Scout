---
type: "model"
id: "NotoriousH2/Qwen3-0.6B-JSON-SFT"
source: "huggingface"
url: "https://huggingface.co/NotoriousH2/Qwen3-0.6B-JSON-SFT"
downloads: 1380
context_length: 131072
parameters_b: 0.596
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
model_size:
  - "[[초경량 모델]]"
---
# NotoriousH2/Qwen3-0.6B-JSON-SFT

> model · [Hugging Face](https://huggingface.co/NotoriousH2/Qwen3-0.6B-JSON-SFT)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — metadata · context_length = `131072` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **모델 크기**: [[초경량 모델]] — metadata · parameter_count_billion = `0.596` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]]

## 학습 데이터

- [[NotoriousH2__meeting-to-json-ko|NotoriousH2/meeting-to-json-ko]]
