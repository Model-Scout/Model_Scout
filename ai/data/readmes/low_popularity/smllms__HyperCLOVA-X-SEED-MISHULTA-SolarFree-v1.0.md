---
license: other
license_name: hyperclovax-seed
license_link: https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-14B/blob/main/LICENSE
base_model: naver-hyperclovax/HyperCLOVAX-SEED-Think-14B
language: [ko]
pipeline_tag: text-generation
tags: [korean, k-ds, hackathon, fine-tuned, lora, solar-free, aihub]
---

# HyperCLOVA-X-SEED-MISHULTA-SolarFree-v1.0

**K-DATA SCIENCE 해커톤 제출 모델(Solar-free 변형)** · 팀 MISHULTA

`naver-hyperclovax/HyperCLOVAX-SEED-Think-14B`(국내 기업 개발 모델, 14.8B)를 한국어 객관식 추론 과제에 맞춰
QLoRA로 미세조정한 뒤 병합한 모델입니다. 같은 팀의 1위 제출 `smllms/HyperCLOVA-X-SEED-MISHULTA-Solar-Distilled-v1.9`와
**동일한 레시피**(completion-only loss · completion 길이 상한 1,280 · 종료 토큰 학습 · 채팅 템플릿 기본 think-OFF)를 쓰되,
**Upstage Solar Pro 4로 생성한 데이터를 전량 제외**하고 AI Hub·공개 train 셋·자기생성(self-STaR)·DeepSeek-R1 교사 데이터만으로 학습했습니다.
외부 상용 LLM 산출물 의존 없이 어디까지 도달하는지를 같은 조건에서 비교하기 위한 모델입니다.

## 학습 데이터 (usable 14,435 예제 · 1 epoch · 903 step · A6000 1장 약 4.3시간)

모두 공개 데이터 또는 자체 생성 데이터이며, **평가용 test 스플릿은 사용하지 않았습니다.** Solar 계열 산출물 0건.

| 구분 | 출처 | 건수 |
|---|---|---|
| AI Hub 텍스트 → 객관식 변환 | AI Hub [71486 문장 유형(추론·예측 등) 판단 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?dataSetSn=71486) 3,500 · [71844 민간 민원 상담 LLM 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?dataSetSn=71844) / [71852 공공 민원 상담 LLM 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?dataSetSn=71852) 2,500 (정답 위치 균등 A/B/C/D, 짧은 풀이) | 6,000 |
| 자기생성 추론(self-STaR) | 베이스 모델 자기생성 CoT 중 정답 일치분 | 4,000 |
| 교사 증류 | [deepseek-ai/DeepSeek-R1-0528](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) | 498 |
| 한국어 전문지식 | [HAERAE-HUB/KMMLU](https://huggingface.co/datasets/HAERAE-HUB/KMMLU) train 스플릿(답만) | 3,000 |
| 의학 | KorMedMCQA 공개셋(답만) | 2,000 |
| 다단 추론 | Com2 train 스플릿 한국어화(평가셋 main/hard 겹침 사전 제외) | ≤380 |
| (제외) | 합성 MuSR 스타일 문항 2,262건은 셔플 후 제거(v1.9와 동일) · completion >1,280토큰 1,360건 제외 | — |

정규화(clean_cot: think 태그 제거·반복 정답 축약·끝맺음 보정)는 v1.9와 동일. 평가 벤치마크(KMMLU-Pro·CLIcK·Ko-MuSR)와의
문항 중복은 **문항 + 선택지 단위로 대조**해 제거했습니다(정확 일치 범위).

## 사용법

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "smllms/HyperCLOVA-X-SEED-MISHULTA-SolarFree-v1.0"
tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, dtype=torch.bfloat16, device_map="auto")

messages = [{"role": "user", "content": "다음 문제의 정답을 고르시오. 마지막 줄에 \"정답: X\" 형식으로 답하시오.\n\n..."}]
inputs = tok.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)
out = model.generate(inputs, do_sample=False, stop_strings=["<|endofturn|>", "<|stop|>"], tokenizer=tok)
print(tok.decode(out[0][inputs.shape[1]:], skip_special_tokens=True))
```

채팅 템플릿 기본값은 think-OFF(`<|im_start|>assistant/think\n<|im_end|>` 후 바로 답변)입니다. 사고 과정을 켜려면 `force_reasoning=True`.

## 라이선스
베이스 모델 라이선스(HyperCLOVA X SEED)를 따릅니다. 학습 데이터 출처는 위 표와 같으며 Solar 계열 데이터는 포함되지 않습니다.
