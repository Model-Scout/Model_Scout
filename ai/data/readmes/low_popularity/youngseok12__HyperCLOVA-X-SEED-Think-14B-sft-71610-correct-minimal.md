---
license: other
license_name: hyperclovax-seed
license_link: LICENSE
base_model: naver-hyperclovax/HyperCLOVAX-SEED-Think-14B
base_model_revision: 9b74e35d4c7e4ffec489f4171273caca8948a2b9
language:
- ko
library_name: transformers
pipeline_tag: text-generation
tags:
- korean
- hyperclovax
- sft
- aihub
- lora-merge
- correct-only
- safetensors
---

# HyperCLOVA X SEED Think-14B SFT 71610 Correct Minimal

이 저장소는 `naver-hyperclovax/HyperCLOVAX-SEED-Think-14B` pristine Base
(revision `9b74e35d4c7e4ffec489f4171273caca8948a2b9`)에 AI Hub 71610 금융·법률
MRC 데이터를 사용해 학습한 LoRA adapter를 병합한 standalone BF16 모델입니다.
1,000개 private-training 후보를 Base로 먼저 판정하고 Base가 정답을 맞힌
803개만 사용한 독립 source 실험입니다. 다른 AI Hub source, v0.21 mixture,
public benchmark test 데이터는 학습에 포함하지 않았습니다.

## 학습 데이터

- AI Hub Dataset 71610 — 금융·법률 MRC
- Base probe pool 1,000개: 금융 449개 / 법률 551개
- Base-correct subset **803개**: 금융 376개 / 법률 427개
- 제외: wrong 39개, uncertain 158개; 복제·재샘플링 없음
- target: 기존 Minimal SFT와 같은 label-only 정답 문자 `A/B/C/D`
- label 분포: A 194 / B 203 / C 207 / D 199
- public benchmark 문제·정답·평가 파일은 사용하지 않음
- AI Hub 안내: <https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71610>

## 학습 설정

- Base: `naver-hyperclovax/HyperCLOVAX-SEED-Think-14B`
- Revision: `9b74e35d4c7e4ffec489f4171273caca8948a2b9`
- LoRA: `r=4`, `alpha=8`, `dropout=0`, bias=`none`
- Target modules: `q_proj`, `v_proj`
- Learning rate: `1e-6`; scheduler: constant; warmup: `0`; weight decay: `0`
- 1 epoch; 51 optimizer steps; batch size `1`; gradient accumulation `16`
- BF16; max sequence length `1024`; packing disabled; assistant-only loss
- Seed/data seed: `42/42`; gradient checkpointing enabled
- Final train loss: `3.0711510883`
- Trainer runtime: `404.6195초`; wall elapsed: `427.6719초`

## 병합 및 사용

LoRA adapter를 pristine Base에 병합한 standalone BF16 `safetensors` 모델입니다.
별도 adapter나 custom model code 없이 Transformers로 로드할 수 있습니다.
이번 업로드 단계에서는 benchmark 점수를 측정하지 않았습니다.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "youngseok12/HyperCLOVA-X-SEED-Think-14B-sft-71610-correct-minimal"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, torch_dtype=torch.bfloat16, device_map="auto"
)
```

## 라이선스 및 제한

Base 모델과 병합 모델은 NAVER의 HyperCLOVA X SEED 14B Think Model License
Agreement를 따릅니다. 저장소의 `LICENSE` 전문과 `NOTICE`를 확인해야 하며,
AI Hub 원천 데이터 이용약관도 적용됩니다. 연구·평가용 모델로서 정확성을
보장하지 않으며 의료·법률·금융 판단의 유일한 근거로 사용하지 마십시오.
