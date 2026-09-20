---
license: other
base_model: naver-hyperclovax/HyperCLOVAX-SEED-Think-14B
base_model_revision: 9b74e35d4c7e4ffec489f4171273caca8948a2b9
language:
- ko
library_name: transformers
pipeline_tag: text-generation
tags:
- korean
- sft
- aihub
- lora-merge
- correct-only
---

# HyperCLOVA X SEED Think-14B SFT 569 Correct Minimal

이 저장소는 `naver-hyperclovax/HyperCLOVAX-SEED-Think-14B`의 pristine Base
(revision `9b74e35d4c7e4ffec489f4171273caca8948a2b9`)에 AI Hub 569 행정문서 MRC
데이터를 사용해 학습한 LoRA adapter를 Base에 병합한 standalone BF16 모델입니다.
Base가 먼저 풀어 맞힌 샘플만 사용해 정답 선택지 형식을 안정화하는 독립 실험용
모델이며, 다른 AI Hub source·v0.21 mixture·public benchmark test 데이터는
학습에 포함하지 않았습니다.

## 학습 데이터

- AI Hub Dataset 569 — 행정문서 대상 기계독해 데이터 / VL_multiple_choice
- clean stratified pool 1,000개를 HyperCLOVA Base로 사전 판정
- Base가 맞힌 **778개**만 사용; wrong 31개와 uncertain 191개는 제외
- target은 Minimal SFT와 동일한 label-only 정답 문자 `A/B/C/D`
- 공개 benchmark 문제·정답·평가 파일은 사용하지 않음
- 데이터셋 안내: <https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=569>

## 학습 설정

- Base: `naver-hyperclovax/HyperCLOVAX-SEED-Think-14B`
- Base revision: `9b74e35d4c7e4ffec489f4171273caca8948a2b9`
- LoRA: `r=4`, `alpha=8`, `dropout=0`, bias=`none`
- Target modules: `q_proj`, `v_proj`
- Learning rate: `1e-6`; scheduler: constant; warmup: `0`; weight decay: `0`
- Epochs: `1`; optimizer steps: `49`
- Per-device batch size: `1`; gradient accumulation: `16` (effective batch `16`)
- BF16; max sequence length `1024`; packing disabled
- Assistant-only loss; gradient checkpointing enabled
- Seed/data seed: `42/42`
- 최종 train loss: `3.293650816897957`
- Trainer runtime: `438.6499초`; sequence preflight truncation: 1개 (target 보존)

## 병합 및 사용

LoRA adapter를 pristine Base에 병합한 standalone BF16 `safetensors` 모델입니다.
별도 adapter나 custom Python model code 없이 Transformers로 로드할 수 있습니다.
이번 업로드 단계에서는 benchmark 점수를 측정하지 않았습니다.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "youngseok12/HyperCLOVA-X-SEED-Think-14B-sft-569-correct-minimal"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="bfloat16",
    device_map="auto",
)
```

## 라이선스 및 제한

Base 모델과 병합 모델은 NAVER의 HyperCLOVA X SEED 14B Think Model License
Agreement를 따릅니다. `LICENSE`의 전체 조건과 AI Hub 원천 데이터 이용약관을
확인해야 합니다. 연구·평가용 모델이며, 출력의 정확성을 보장하지 않습니다.
의료·법률·행정 등 전문적인 판단의 유일한 근거로 사용하지 마십시오.
