---
language:
- ko
tags:
- korean
- causal-lm
- llama
- yejin
- sft
- 1b
license: apache-2.0
pipeline_tag: text-generation
---

# yejin-korean-1b-v8-sft 🚀

> **yejin-korean-1b-v8-sft**는 한국어 172GB+ 고품질 코퍼스로 100% 바닥부터 사전학습(Pre-trained from Scratch)된 `yejin-korean-1b-v8` 베이스 모델에 **KMMLU, KoAlpaca, 한국어 교과서 지시문**을 결합하여 지도 미세조정(Supervised Fine-Tuning)을 완료한 1B 한국어 소형 파운데이션 모델입니다.

---

## 📊 모델 아키텍처 사양
- **기반 규격**: Llama 3 참조 아키텍처 (`hidden=2048`, `layers=18`, `heads=16`, `kv_heads=4`, `intermediate=5632`, `GQA 4:1`, `RoPE θ=10000`)
- **파라미터 수**: 약 9억 3,200만 (0.93B)
- **토크나이저**: `EleutherAI/polyglot-ko-1.3b` (어휘 크기: 30,003)
- **컨텍스트 길이**: 4,096 토큰
- **포맷**: `safetensors` (Float32 / BFloat16)

---

## 🚀 사용 예시 (Python Transformers)

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "cooler8/yejin-korean-1b-v8-sft"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float32, device_map="auto")

prompt = "### 지시사항:\n인공지능이란 무엇인지 초등학생도 알기 쉽게 설명해줘.\n\n### 답변:\n"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

output = model.generate(
    input_ids=inputs["input_ids"],
    attention_mask=inputs["attention_mask"],
    max_new_tokens=200,
    temperature=0.7,
    top_p=0.9,
    repetition_penalty=1.15
)

print(tokenizer.decode(output[0], skip_special_tokens=True))
```

---

## 💡 프롬프트 포맷 (Prompt Template)
```text
### 지시사항:
{사용자 질문 또는 지시문}

### 답변:
{모델 생성 답변}
```