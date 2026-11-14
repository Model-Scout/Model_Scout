---
language:
- ko
license: apache-2.0
base_model: cooler8/yejin-korean-8b-v3-base
tags:
- korean
pipeline_tag: text-generation
---

# Yejin Korean 8B v3 cpt2s20000 + Qwen3.6-27B distill lr2e-4 seed soup4 nothink-v2

Korean instruction-following language model.

## Chat Template

```
<s><|user|>\n{instruction}<|end|>\n<|assistant|>\n<think> </think>{response}<|end|>
```

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("cooler8/yejin-korean-8b-v3-cpt2s20000-distill-qwen36-lr2e4-seedsoup4-nothink-v2", torch_dtype="bfloat16", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("cooler8/yejin-korean-8b-v3-cpt2s20000-distill-qwen36-lr2e4-seedsoup4-nothink-v2")

messages = [{"role": "user", "content": "한국의 수도는 어디인가요?"}]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt", return_dict=True).to(model.device)
inputs.pop("token_type_ids", None)
outputs = model.generate(**inputs)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

## Training

Uniform weight average (model soup) of four LoRA fine-tunes of the same Yejin model that differ only in data order: Yejin 8B v3 (pretrained from scratch by Yejin: cooler8/yejin-korean-8b-v3-base) after two stages of continued pretraining on public Korean data (6,000 steps in stage 1 plus 20,000 steps in stage 2, which includes FinePDFs Korean text partly extracted by an OCR model, RolmOCR), with the Yejin chat vector from our own SFT model, then LoRA (rank 64, lr 2e-4). The LoRA data mixes our phase-1 format data (45,013 samples) with 39,290 short Korean solutions written by Qwen/Qwen3.6-27B (Apache-2.0) for questions from our own puzzle generator, KMMLU train, AI Hub school exams and AI Hub reading comprehension; only solutions that reached the known answer were kept (sequence-level distillation; no teacher weights or logits). No benchmark test items were used, and the training data share no word 13-gram with KMMLU-Pro, KMMLU test, CLIcK, MuSR or Korean MuSR items.

## License

Apache 2.0
