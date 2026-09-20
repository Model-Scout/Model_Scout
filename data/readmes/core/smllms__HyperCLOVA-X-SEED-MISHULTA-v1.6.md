---
license: other
license_name: hyperclovax-seed
license_link: https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-14B/blob/main/LICENSE
base_model: naver-hyperclovax/HyperCLOVAX-SEED-Think-14B
language: [ko]
pipeline_tag: text-generation
tags: [korean, k-ds, hackathon, fine-tuned, lora]
---

# HyperCLOVA-X-SEED-MISHULTA-v1.6

**K-DATA SCIENCE 해커톤 제출 모델** · 팀 MISHULTA

`naver-hyperclovax/HyperCLOVAX-SEED-Think-14B`(국내 기업 개발 모델, 14.8B)를
한국어 객관식 추론 과제에 맞춰 LoRA로 미세조정한 뒤 병합한 모델입니다.
v1.5와 동일한 가중치이며, 생성 설정(`generation_config`)이 다릅니다.

## Teacher 모델 출처

**본 버전은 Upstage Solar 계열 모델 및 그 결과물을 학습에 사용하지 않았습니다.**
교사 데이터는 베이스 모델(HyperCLOVAX-SEED-Think-14B) 자체의 자기증류와
DeepSeek-R1-0528 증류분으로 구성되어 있습니다.

> 팀 MISHULTA의 다른 버전(v2 이후) 중 일부는 Upstage Solar Pro 4를 teacher로
> 사용했으며, 해당 활용은 **비상업·해커톤 목적에 한하여 업스테이지의 별도 확인(컨펌)을
> 거쳐 진행**되었습니다. 현 Upstage 이용약관상 Solar 결과물을 활용한 distillation은
> 원칙적으로 허용되지 않으므로, 이를 일반적으로 허용된 것으로 해석해서는 안 됩니다.

## 학습 데이터

모두 공개 데이터 또는 자체 생성 데이터이며, **평가용 test 스플릿은 사용하지 않았습니다.**

| 구분 | 출처 |
|---|---|
| 한국어 객관식 자기증류 | [HAERAE-HUB/KMMLU](https://huggingface.co/datasets/HAERAE-HUB/KMMLU) train 스플릿 |
| 교사 증류 | [deepseek-ai/DeepSeek-R1-0528](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) |
| 자체 생성 | 한국 문화·언어 문항, 합성 추론 문항 (신규 생성, 평가 벤치마크 원문항 미사용) |

평가 대상 벤치마크와의 문항 중복은 사전 대조를 통해 제거했습니다.

## 사용법

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "smllms/HyperCLOVA-X-SEED-MISHULTA-v1.6"
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
