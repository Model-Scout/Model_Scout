---
license: apache-2.0
base_model: Qwen/Qwen3.5-0.8B
library_name: transformers
language:
- ko
---

# Qwen3.5-0.8B 온라인 쇼핑 상담 SFT 모델 (실습용)

`Qwen/Qwen3.5-0.8B`를 온라인 쇼핑 상담 질문과 답변 데이터로 풀 파인튜닝(SFT)한 실습용 모델입니다. DPO 선호 정렬 실습에서 정렬을 시작하는 모델(참조 모델)로 씁니다.

- SFT 단원 과제 02에서 고른 온라인 쇼핑 상담 모델입니다. 시스템 프롬프트: `너는 온라인 쇼핑 상담 챗봇이다. 전자상거래법 조문에 근거해 존댓말로 간결히 답한다.`
- 가중치는 float32로 저장했습니다. `AutoModelForCausalLM.from_pretrained("muahseol/qwen3.5-0.8b-commerce-sft", dtype=torch.float32)`로 불러옵니다.
- 답에 틀린 조문과 지어 낸 내용이 들어 있을 수 있습니다. 학습 실습용이며 실제 상담에 쓰지 않습니다.
