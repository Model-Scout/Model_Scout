---
type: "model"
id: "Edentns/DataVortexTL-1.1B-v0.1"
source: "huggingface"
url: "https://huggingface.co/Edentns/DataVortexTL-1.1B-v0.1"
downloads: 275
context_length: 2048
parameters_b: 1.1
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[비상업 전용]]"
model_size:
  - "[[소형 모델]]"
---
# Edentns/DataVortexTL-1.1B-v0.1

> model · [Hugging Face](https://huggingface.co/Edentns/DataVortexTL-1.1B-v0.1)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — metadata · context_length = `2048` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **모델 크기**: [[소형 모델]] — metadata · parameter_count_billion = `1.1` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]]

## 학습 데이터

- [[beomi__KoAlpaca-v1.1a|beomi/KoAlpaca-v1.1a]]
- [[jojo0217__korean_rlhf_dataset|jojo0217/korean_rlhf_dataset]]
- [[kyujinpy__OpenOrca-KO|kyujinpy/OpenOrca-KO]]
- [[nlpai-lab__kullm-v2|nlpai-lab/kullm-v2]]
