---
license: other
license_name: hyperclovax-seed
license_link: https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-14B/blob/main/LICENSE
base_model: naver-hyperclovax/HyperCLOVAX-SEED-Think-14B
language: [ko]
pipeline_tag: text-generation
tags: [korean, k-ds, hackathon, fine-tuned, lora]
---

# HyperCLOVA-X-SEED-MISHULTA-Solar-Distilled-v1.7

**K-DATA SCIENCE 해커톤 제출 모델** · 팀 MISHULTA

`naver-hyperclovax/HyperCLOVAX-SEED-Think-14B`(국내 기업 개발 모델, 14.8B)를
한국어 객관식 추론 과제에 맞춰 LoRA로 미세조정한 뒤 병합한 모델입니다.
생성 종료 안정성을 개선한 학습 구성으로 새로 학습한 계열입니다.

## Teacher 모델 출처 및 이용 조건

본 모델은 **Upstage Solar Pro 4**를 teacher 모델로 사용하여 학습 데이터(CoT)를
생성하였으며, 해당 활용은 **비상업·해커톤 목적에 한하여 업스테이지의 별도 확인(컨펌)을
거쳐 진행**되었습니다.

현 Upstage 이용약관상 Solar 결과물을 활용한 distillation은 **원칙적으로 허용되지
않으며**, 본 건은 예외적으로 확인을 받은 사례입니다. 따라서 본 모델카드를 근거로
Solar 기반 distillation이 일반적으로 허용된다고 해석해서는 안 됩니다.

Solar 관련 조건은 Solar Open 2 라이선스를 따릅니다.

## 학습 데이터

모두 공개 데이터 또는 자체 생성 데이터이며, **평가용 test 스플릿은 사용하지 않았습니다.**

| 구분 | 출처 |
|---|---|
| 한국어 객관식 자기증류 | [HAERAE-HUB/KMMLU](https://huggingface.co/datasets/HAERAE-HUB/KMMLU) train 스플릿 |
| 교사 증류 | **Upstage Solar Pro 4** (상단 이용 조건 참조), [deepseek-ai/DeepSeek-R1-0528](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) |
| 자체 생성 | 한국 문화·언어 문항, 합성 추론 문항 (신규 생성, 평가 벤치마크 원문항 미사용) |
| 다단 추론 | Com2 train 스플릿 한국어화 (평가셋 main/hard 겹침 사전 제외) |

평가 대상 벤치마크와의 문항 중복은 사전 대조를 통해 제거했습니다.

## 사용법

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "smllms/HyperCLOVA-X-SEED-MISHULTA-Solar-Distilled-v1.7"
tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, dtype=torch.bfloat16, device_map="auto")

messages = [{"role": "user", "content": "다음 문제의 정답을 고르시오. ..."}]
inputs = tok.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)
out = model.generate(inputs, do_sample=False, stop_strings=["<|endofturn|>", "<|stop|>"], tokenizer=tok)
print(tok.decode(out[0][inputs.shape[1]:], skip_special_tokens=True))
```

정답은 출력 마지막의 `정답: X` 형식으로 제시됩니다.

## 라이선스

베이스 모델의 [HyperCLOVA X SEED Model License Agreement](https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-14B/blob/main/LICENSE)를 따릅니다.
라이선스 §3.1에 따라 파생 모델명은 "HyperCLOVA X"로 시작합니다.

## 팀

**MISHULTA** — 미술전시 큐레이션 서비스 운영팀. K-DS 해커톤(NIA) 참가.
