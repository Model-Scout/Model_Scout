---
type: "model"
id: "Abu-Dju/Marco-Mini-Instruct"
source: "huggingface"
url: "https://huggingface.co/Abu-Dju/Marco-Mini-Instruct"
downloads: 294
context_length: 131072
parameters_b: 17.251
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
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[중형 모델]]"
---
# Abu-Dju/Marco-Mini-Instruct

> model · [Hugging Face](https://huggingface.co/Abu-Dju/Marco-Mini-Instruct)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `29 languages` · 신뢰도 high
- **입력 길이**: [[초장문]] — metadata · context_length = `131072` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **모델 크기**: [[중형 모델]] — metadata · parameter_count_billion = `17.251` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]]

## 학습 데이터

- [[BytedTsinghua-SIA__DAPO-Math-17k|BytedTsinghua-SIA/DAPO-Math-17k]]
- [[Skywork__Skywork-OR1-RL-Data|Skywork/Skywork-OR1-RL-Data]]
- [[allenai__Dolci-Instruct-SFT|allenai/Dolci-Instruct-SFT]]
- [[nvidia__Nemotron-Cascade-2-SFT-Data|nvidia/Nemotron-Cascade-2-SFT-Data]]
- [[nvidia__Nemotron-Cascade-RL-RLHF|nvidia/Nemotron-Cascade-RL-RLHF]]
- [[nvidia__Nemotron-RL-ReasoningGym-v1|nvidia/Nemotron-RL-ReasoningGym-v1]]
- [[nvidia__Nemotron-RL-instruction_following|nvidia/Nemotron-RL-instruction_following]]
- [[nvidia__Nemotron-RL-instruction_following-structured_outputs|nvidia/Nemotron-RL-instruction_following-structured_outputs]]
- [[nvidia__Nemotron-RL-knowledge-mcqa|nvidia/Nemotron-RL-knowledge-mcqa]]
- [[nvidia__Nemotron-SFT-Multilingual-v1|nvidia/Nemotron-SFT-Multilingual-v1]]
