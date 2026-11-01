---
license: apache-2.0
language:
- ko
- en
tags:
- medical
- korean
- healthcare
- mixture-of-experts
- qwen3
base_model: Qwen/Qwen3-4B
pipeline_tag: text-generation
library_name: transformers
---

<p align="center">
  <img src="https://huggingface.co/MediKo/MediKo-9B-A4B-inst/resolve/main/mediko-wordmark-web.png" width="320" alt="MediKo">
</p>

# MediKo-9B-A4B (Instruct)

Korean medical language model built with **VocMoE** (DVE + MoDE). This is the **inst** (instruction-tuned (chat)) checkpoint of **MediKo-9B-A4B**.

| Spec | Value |
|------|-------|
| Base | Qwen3-4B |
| Total / Active params | 9.4B / 4.5B |
| Medical experts (N) / top-K | 16 / 4 |
| Layers | 36 |
| Vocab (DVE-expanded) | 156,669 |
| Variant | instruction-tuned (chat) |

**This checkpoint (zero-shot avg):** KorMedMCQA 57.5 · KMMLU-Med 53.0 · EnMed 66.9 · KoBEST 63.9 · HAE-RAE 62.1

---

## How it works

VocMoE combines two components:

1. **DVE (Domain Vocabulary Expansion)** adds 5,000 Korean medical tokens (from KM-BERT, scored by fragmentation × frequency × PMI), cutting medical-term over-fragmentation ~64%.
2. **MoDE (Mixture-of-Domain-Experts)** uses the vocabulary partition as the routing key: medical tokens (`id ≥ original_vocab_size`) go to dedicated experts, general tokens keep the **preserved dense FFN**. The general path stays architecturally isolated, preventing catastrophic forgetting at the architectural level.

---

## Family & benchmarks

| Model | Base | Total | Active |
|-------|------|------:|-------:|
| `MediKo-1.1B-A0.6B` | Qwen3-0.6B | 1.13B | 0.59B |
| `MediKo-4B-A1B` | Qwen3-1.7B | 3.49B | 1.69B |
| `MediKo-9B-A4B` | Qwen3-4B | 9.4B | 4.5B |
| `MediKo-30B-A8B` *(not released)* | Qwen3-8B | ~30B | ~8.1B |

Benchmark (zero-shot avg, **instruction-tuned variants**):

| Model | Active | KorMedMCQA | KMMLU-Med | EnMed | KoBEST | HAE-RAE |
|-------|-------:|-----------:|----------:|------:|-------:|--------:|
| Qwen3-8B *(ref)* | 8B | 42.2 | 52.4 | 70.7 | 64.0 | 57.7 |
| KULLM3 *(ref)* | 10.7B | 42.7 | 39.1 | 65.4 | 67.7 | 54.0 |
| MediKo-1.1B-A0.6B | 0.59B | 32.6 | 33.3 | 51.1 | 53.4 | 43.1 |
| MediKo-4B-A1B | 1.69B | 44.8 | 44.5 | 60.8 | 59.3 | 50.2 |
| MediKo-9B-A4B | 4.5B | 57.5 | 53.0 | 66.9 | 63.9 | 62.1 |

---

## Usage

> ⚠️ Custom architecture (`MediKoForCausalLM`) — pass `trust_remote_code=True`. Token-type routing is generated inside `forward()` from `input_ids`.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "MediKo/MediKo-9B-A4B-inst"
tok = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id, trust_remote_code=True,
    torch_dtype=torch.bfloat16, device_map="auto",
)

messages = [{"role": "user", "content": "성인 2형 당뇨병의 1차 약물 치료는 무엇인가요?"}]
# Thinking ON (default). OFF: add enable_thinking=False
text = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tok(text, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=512)
print(tok.decode(out[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))
```

- Trained with a **"Thinking Recovery"** objective: supports both thinking (`<think>...</think>`)
  and non-thinking modes. Sampling: thinking `temp=0.6, top_p=0.95`; non-thinking `temp=0.7, top_p=0.8`.

---

## Intended use & limitations

Research/education for Korean medical NLP.

**⚠️ Medical disclaimer.** Not a medical device; research/informational use only. Outputs **must not** be used for diagnosis, treatment, prescription, or clinical decision-making. Always consult a qualified professional. May hallucinate; do not input personally identifiable patient data.

**Limitations.** Validated only on Korean medical text. MoE → total memory larger than a comparable dense model. CPT token budget (~19.5B) modest vs large English medical LLMs.

---

## Training data

- Medical (Korean) ~108 GB + General (Korean) ~39 GB → ~19.5B tokens (≈76% / 24%).
- Pipeline: DVE → Qwen3→MediKo dense → MoE upcycle → CPT → SFT.

---

## License

Apache-2.0 (inherits Qwen3 base license). Comply with applicable medical / privacy regulations in your jurisdiction.

## Citation

Accepted to **Findings of the Association for Computational Linguistics: EMNLP 2026**.
<!-- Anthology ID / pages는 프로시딩 공개 후 채운다. -->
```bibtex
@inproceedings{cho2026vocmoe,
  title     = {VocMoE: Vocabulary-Guided Mixture-of-Experts for Korean Medical Language Models},
  author    = {Cho, Sangyeon and Han, Jaeho and Jeon, Mingyu and Kim, Junyeong},
  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2026},
  year      = {2026},
}
```
