---
dataset_info:
- config_name: Natural_Reasoning_gpt_oss_120b_s1
  features:
  - name: index
    dtype: string
  - name: instruction
    dtype: string
  - name: reasoning_ko
    dtype: string
  - name: reasoning_original
    dtype: string
  - name: answer
    dtype: string
  - name: source
    dtype: string
  - name: translator
    dtype: string
  - name: nonthink_avg_logprob
    dtype: float64
  - name: think_original_avg_logprob
    dtype: float64
  - name: think_ko_avg_logprob
    dtype: float64
  splits:
  - name: train
    num_bytes: 162766952
    num_examples: 8716
  download_size: 80576565
  dataset_size: 162766952
- config_name: YiSang_HighQuality
  features:
  - name: index
    dtype: string
  - name: instruction
    dtype: string
  - name: reasoning_ko
    dtype: string
  - name: reasoning_original
    dtype: string
  - name: answer
    dtype: string
  - name: source
    dtype: string
  - name: translator
    dtype: string
  - name: nonthink_avg_logprob
    dtype: float64
  - name: think_original_avg_logprob
    dtype: float64
  - name: think_ko_avg_logprob
    dtype: float64
  splits:
  - name: train
    num_bytes: 505302048
    num_examples: 49564
  download_size: 236485320
  dataset_size: 505302048
configs:
- config_name: Natural_Reasoning_gpt_oss_120b_s1
  data_files:
  - split: train
    path: Natural_Reasoning_gpt_oss_120b_s1/train-*
- config_name: YiSang_HighQuality
  data_files:
  - split: train
    path: YiSang_HighQuality/train-*
license: apache-2.0
language:
- en
- ko
---

## Reasoning 번역

### 원본 데이터

한국어 질의 -> 영어 추론+한국어 답변 데이터: [KOREAson/YiSang-HighQuality](https://huggingface.co/datasets/KOREAson/YiSang-HighQuality)

영어 질의 -> 영어 추론+영어 답변 데이터: [Jackrong/Natural-Reasoning-gpt-oss-120B-S1](https://huggingface.co/datasets/Jackrong/Natural-Reasoning-gpt-oss-120B-S1)

### 번역 모델

[yanolja/YanoljaNEXT-Rosetta-4B-2511](https://huggingface.co/yanolja/YanoljaNEXT-Rosetta-4B-2511)

### 데이터 가공

**1. YanoljaNEXT-Rosetta-4B-2511 모델을 이용하여 추론 텍스트 번역**

- 원본 질의를 컨텍스트로 제공하여 번역의 일관성 향상

- 최대 8192 토큰 미만의 추론만 번역 수행

- 반복 발생, 번역 누락 사례 확인

**2. 원문 추론과 번역된 추론을 `nltk.sent_tokenize` 를 사용하여 문장 단위로 자른 후[BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3)로 임베딩하여 문장 단위 매칭**

- 연속된 여러 문장이 누락된 경우 (주로 추론 내에서 모델이 헷갈려하는 텍스트('Wait, ...')를 고의로 생략하고 번역하는 경우) 발견 후 제외

- 원문과 번역문의 평균 유사도가 0.7 미만인 경우 제외

**3. [Qwen/Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B) 모델(추론+비추론 섞인 버전)을 기반으로, 도움이 되는 번역 추론만 필터링**

- π(a|q) < π(a|q, t)
  - 추론을 넣었을 때 원본 답변이 나올 확률이 더 높아져야 함

- π(a|q, t) < π(a|q, t_ko)
  - 번역된 추론을 넣었을 때 원본 답변이 나올 확률이 더 높아져야 함

- YiSang-HighQuality 기준 약 절반 정도, Natural-Reasoning 기준 약 70% 데이터가 제거됨

### 기타

(엄밀한 테스트 아님)

Gemma-3-4B-it 기준, 영어 추론을 학습하는 쪽이 성능이 훨씬 더 향상됨 (특히 한국어 추론으로 학습 시 수학(HRM_MATH) 벤치 시 추론 도중 반복때문에 점수가 크게 하락함)

영어 질의->한국어 추론->영어 답변 형태의 데이터(Natural-Reasoning)를 일부 학습시킬 때, 영어 벤치인 MMLU-Pro 점수가 약간 향상됨 (영->영->영 보다는 향상폭 낮음)



한국어 사전학습이 많이 된 모델(HyperClova, Kanana, etc...)은 어떨지 확인 중

한국어 추론 모델(HyperCLOVAX-SEED-Think-14B)로 추론을 재생성해보는 중