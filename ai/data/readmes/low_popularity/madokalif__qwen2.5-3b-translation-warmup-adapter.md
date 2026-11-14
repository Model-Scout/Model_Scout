---
language:
- en
- ko
license: apache-2.0
base_model: Qwen/Qwen2.5-3B-Instruct
tags:
- translation
- lora
- peft
- qwen2.5
- english-korean
datasets:
- custom
pipeline_tag: text-generation
---

# Qwen2.5-3B Translation Warmup Adapter

영어-한국어 번역을 위해 fine-tuning된 Qwen2.5-3B-Instruct의 LoRA adapter입니다.

## Model Description

이 모델은 adaSTaR (Adaptive Self-Taught Reasoner) 파이프라인의 Phase 1 (Warmup SFT) 결과물입니다.
GPT-4-turbo로 생성된 번역 데이터를 사용하여 학습되었습니다.

### Training Details

- **Base Model**: Qwen/Qwen2.5-3B-Instruct
- **Training Method**: LoRA (Low-Rank Adaptation)
- **Task**: English to Korean Translation (Field Claim Data)
- **Training Examples**: 144 samples
- **LoRA Rank (r)**: 16
- **LoRA Alpha**: 32
- **Target Modules**: q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj

## Evaluation Results

| Metric | Score |
|--------|-------|
| BLEU | 0.4414 |

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch

# Load base model
base_model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen2.5-3B-Instruct",
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

# Load adapter
model = PeftModel.from_pretrained(base_model, "madokalif/qwen2.5-3b-translation-warmup-adapter")
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-3B-Instruct")

# Generate translation
messages = [
    {"role": "system", "content": "You are an expert English-Korean translator specializing in technical documents."},
    {"role": "user", "content": "Translate the following text to Korean:\n\nMALFUNCTION in ENGINE system detected."}
]

prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=256, temperature=0.7, top_p=0.9)
translation = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(translation)
```

## Training Pipeline

This adapter is part of the adaSTaR Self-Taught Translation & Summarization pipeline:

1. **Phase 1 (Warmup SFT)** ← This model
2. Phase 2 (Self-Taught Loop) - Coming soon
3. Phase 3 (Self-Reflection) - Coming soon

## Limitations

- 학습 데이터가 특정 도메인(Field Claim - 결함/이슈 보고서)에 특화되어 있어, 일반적인 번역에는 최적이 아닐 수 있습니다.
- 긴 텍스트의 번역에서 품질이 저하될 수 있습니다.

## License

Apache 2.0

## Citation

```bibtex
@misc{qwen25-3b-translation-warmup,
  author = {madokalif},
  title = {Qwen2.5-3B Translation Warmup Adapter},
  year = {2026},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/madokalif/qwen2.5-3b-translation-warmup-adapter}}
}
```
