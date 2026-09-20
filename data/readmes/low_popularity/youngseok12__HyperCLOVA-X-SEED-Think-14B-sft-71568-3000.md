---
license: other
base_model: naver-hyperclovax/HyperCLOVAX-SEED-Think-14B
library_name: transformers
pipeline_tag: text-generation
tags:
- korean
- sft
- aihub
- lora-merge
---

# HyperCLOVA X SEED Think-14B SFT 71568-3000

이 저장소는 `naver-hyperclovax/HyperCLOVAX-SEED-Think-14B`의 pristine Base
(`9b74e35d4c7e4ffec489f4171273caca8948a2b9`)에 AI Hub 71568
경제·스포츠 숫자 연산/수치 MRC 데이터 3,000개만 사용해 SFT한 모델입니다.
LoRA adapter를 Base에 병합한 독립 실행 가능한 BF16 모델이며, 다른 AI Hub source,
v0.21 mixture 또는 공개 benchmark test 데이터는 학습에 포함하지 않았습니다.

## 학습 데이터

- AI Hub 데이터셋 71568, 경제·스포츠 숫자 연산/수치 MRC
- 원본 `R_train.jsonl`에서 검증된 text-only 3,000개
- answer-first 형식의 선택지 답변과 짧은 근거 target
- 데이터셋 안내: <https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71568>

## 학습 설정

- LoRA: `r=16`, `alpha=32`, `dropout=0.05`, bias=`none`
- Target modules: `q_proj,k_proj,v_proj,o_proj,gate_proj,up_proj,down_proj`
- Learning rate `5e-5`, cosine scheduler, warmup ratio `0.03`, weight decay `0`
- 1 epoch, per-device batch size `4`, gradient accumulation `4` (effective batch `16`)
- BF16, max sequence length `4096`, packing disabled, assistant-only loss
- seed/data seed `42/42`

학습 loss는 `0.0710095`이며, sequence truncation은 0건이었습니다. 병합 후 모든
parameter/buffer의 NaN/Inf 검사와 로컬 synthetic generation smoke test를 통과했습니다.
공식 benchmark 점수는 이 저장소에 포함하지 않으며, 별도 평가가 필요합니다.

## 사용 예시

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "youngseok12/HyperCLOVA-X-SEED-Think-14B-sft-71568-3000"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype="bfloat16", device_map="auto")
```

