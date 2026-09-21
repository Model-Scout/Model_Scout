---
language:
- ko
tags:
- pytorch
- causal-lm
- medical
license: llama2
pipeline_tag: text-generation
---

[https://github.com/jwj7140/ko-medical-chat](https://github.com/jwj7140/ko-medical-chat)

# Llama-Ko-Medical-7b 
llama2-ko-medical은 [llama-2-ko](https://huggingface.co/beomi/llama-2-ko-7b)를 기반으로 의료 분야의 한글 raw 데이터를 학습시킨 기반 모델입니다.
## 학습 데이터
llama2-ko-medical은 약 526MB의 의료 분야 한글 말뭉치로 학습되었습니다. 주요 데이터셋은 다음과 같습니다.
| Source                              |Size (MB) | Link                                  |
|----------------------------------|---------|------------------------------------------|
| AIHub 의료, 법률 전문 서적 말뭉치    | 351.0   | aihub.or.kr |
| 하이닥 뉴스 데이터    | 97.3   | hidoc.co.kr |
| AIHub 전문분야 한영 말뭉치          | 63.4  | aihub.or.kr|
| 질병관리청 국가건강정보포털          | 8.33  | health.kdca.go.kr     |
| 보건복지부 국가정신건강정보포털       | < 1.0  | mentalhealth.go.kr   |
## 학습
llama2-ko-medical-7b는 [llama-2-ko](https://huggingface.co/beomi/llama-2-ko-7b)에서 qlora로 추가 학습되었습니다.
- lora_alpha: 16
- lora_dropout: 0.01
- lora_r: 64
- target_modules: q_proj, v_proj
- epoch: 3
- learning_rate: 3e-4