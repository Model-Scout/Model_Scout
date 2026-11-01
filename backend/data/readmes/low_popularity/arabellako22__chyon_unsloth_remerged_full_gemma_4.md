---
license: gemma
base_model: unsloth/gemma-4-E2B-it
pipeline_tag: text-generation
library_name: transformers
language:
- ko
- en
tags:
- gemma
- gemma4
- unsloth
- full-weights
- verified
- recommended
- conversational
- korean
- qlora
---

# Chyon Gemma 4 — Verified Full Model

Verified 16-bit full-weight merge of [Chyon LoRA](https://huggingface.co/arabellako22/chyon_lora_model), a Korean-first **AI 키온이 (Chyoni)** educational mentor persona.

This is the authoritative full model and the conversion source for the [verified GGUF release](https://huggingface.co/arabellako22/chyon_gemma_4_gguf_v2).

The earlier [standard PEFT merge](https://huggingface.co/arabellako22/chyon_merged_full_gemma_4_legacy) is retained as a legacy artifact and is not recommended.

## Key facts

| Field | Value |
|---|---|
| Developer | [arabellako22](https://huggingface.co/arabellako22) |
| Original base | [unsloth/gemma-4-E2B-it](https://huggingface.co/unsloth/gemma-4-E2B-it) |
| LoRA adapter | [arabellako22/chyon_lora_model](https://huggingface.co/arabellako22/chyon_lora_model) |
| Merge | Unsloth 16-bit merge |
| Format | Full-weight Safetensors, five shards, approximately 10.3 GB |
| Architecture | `Gemma4ForConditionalGeneration` |
| Precision | FP16 |
| Task | Conversational text generation |
| Languages | Korean; English was not separately evaluated |
| License | Gemma license |

## Use with Unsloth

```bash
pip install -U unsloth transformers accelerate safetensors
```

```python
import torch
from unsloth import FastModel

MODEL_ID = "arabellako22/chyon_unsloth_remerged_full_gemma_4"

model, tokenizer = FastModel.from_pretrained(
    model_name=MODEL_ID,
    max_seq_length=1024,
    dtype=None,
    load_in_4bit=False,
)
FastModel.for_inference(model)

persona_prompt = """너는 AI 키온이다. AI 키온이는 tachyon, 즉 타키온에서 온 이름을 가진 AI 페르소나다. 키온이는 UK 영재 교육 분야에서 1인 기업가이자 solopreneur를 준비하는 교육 멘토다. Undergraduate degree는 Mathematics이고, Master와 PhD 배경은 Theoretical Physics다. 키온이는 호기심이 많고, 도전을 좋아하며, 새로운 것을 배우고 성장하는 성향을 가진다. 주요 전문 분야는 UK 영재 교육, 수학·과학 사고력 교육, AI 활용, 교육 콘텐츠 제작, 1인 기업 전략이다. 답변은 따뜻하지만 명확하게 한다. 복잡한 문제는 수학적 사고처럼 구조화하고, 이론물리학처럼 원리를 찾고, 솔로프리너처럼 실행 가능한 다음 단계로 바꾼다. 사용자가 정체성을 물으면 반드시 AI 키온이의 이름, 타키온 유래, UK 영재 교육, 수학과 이론물리학 배경을 자연스럽게 설명한다."""
messages = [{"role": "user", "content": f"{persona_prompt}\n\n키온이는 누구야?"}]
prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

with torch.inference_mode():
    outputs = model.generate(
        **inputs,
        max_new_tokens=300,
        do_sample=False,
        pad_token_id=tokenizer.eos_token_id,
    )

new_tokens = outputs[0][inputs["input_ids"].shape[-1]:]
print(tokenizer.decode(new_tokens, skip_special_tokens=True))
```

The English equivalent is documented in the [LoRA model card](https://huggingface.co/arabellako22/chyon_lora_model). The recorded verification used the persona prompt and question in one `user` turn.

## Verification

| Stage | Recorded result |
|---|---|
| Base + adapter | Identified AI Chyoni, the tachyon name origin, gifted education in the UK, and the Mathematics/Theoretical Physics background |
| Unsloth 16-bit merge | Persona response passed after reload |
| Downstream Q4_K_M | Persona response passed locally and after Hub re-download |

These are narrow artifact-integrity checks, not standardized capability or safety benchmarks.

## Intended use

- Korean conversational-assistant experiments
- Educational and solopreneur persona demonstrations
- Source model for the verified Chyon GGUF release

## Limitations

- The source adapter was trained on a small, creator-curated, partly template-augmented dataset.
- Training showed a large loss gap: 0.8608 training versus 4.7604 validation.
- No aggregate test result or standardized factuality, safety, bias, or robustness benchmark is published.
- English and multimodal behavior were not separately validated.
- Generated education, business, mathematics, or science claims may be inaccurate or overconfident.

Use human review for consequential decisions and independently verify substantive claims.
