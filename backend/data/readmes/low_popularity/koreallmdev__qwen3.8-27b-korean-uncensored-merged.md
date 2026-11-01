---
library_name: transformers
pipeline_tag: text-generation
tags:
- qwen
- qwen3.8
- 27b
- korean
- uncensored
- merged
- bf16
- text-generation
language:
- ko
- en
---

# Qwen3.8 27B 한국어 검열해제 MERGED

**Qwen3.8 27B Uncensored BF16 Base에 한국어 Original LoRA를 실제 병합한 standalone BF16 전체 모델입니다.**

## 핵심 정보

- Model family: Qwen3.8
- Size: 27B
- Language focus: Korean
- Base lineage: Qwen3.8 27B Uncensored BF16
- Korean tuning: Original Korean LoRA
- Merge status: **MERGED**
- Precision: BF16
- Runtime LoRA required: **No**
- PEFT adapter required after download: **No**

## 구조

```text
Qwen3.8 27B Uncensored BF16
              +
      Korean Original LoRA
              |
              v
Qwen3.8 27B 한국어 검열해제 MERGED
```

이 저장소는 LoRA adapter-only 저장소가 아닙니다.
Base 모델과 한국어 LoRA가 실제로 병합된 전체 모델이므로,
다운로드 후 별도 adapter를 붙일 필요가 없습니다.

## Transformers 실행 예시

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL = "koreallmdev/qwen3.8-27b-korean-uncensored-merged"

tokenizer = AutoTokenizer.from_pretrained(
    MODEL,
    trust_remote_code=True,
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)
```

## vLLM 실행 예시

```bash
vllm serve koreallmdev/qwen3.8-27b-korean-uncensored-merged \
  --dtype bfloat16 \
  --max-model-len 4096
```

## 병합 정보

- Merge method: `PeftModel.merge_and_unload(safe_merge=True)`
- SafeTensors: Yes
- New training during export: No
- Original adapter modification: No
- Base model modification: No

## Uncensored 표기

`Uncensored` 표기는 이 프로젝트에서 사용한 로컬 Base 모델
`qwen3_8_27b_uncensored_bf16`의 계보/명칭을 따릅니다.
이는 모든 입력에 대해 무조건적인 무거절 동작을 별도로 인증했다는 의미는 아닙니다.

## 용도

한국어 대화, 한국어 기술 질의, 코딩 보조 및 로컬 LLM 실험을 목적으로 배포합니다.
