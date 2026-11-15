---
license: apache-2.0
language:
- ko
- en
library_name: transformers
pipeline_tag: text-generation
tags:
- darwin
- vidraft
- delphi
- chemistry
- korean
- moe
- mixture-of-experts
- cohere2_moe
- 218b
- gpqa-88
base_model:
- FINAL-Bench/Darwin-218B-kr
- CohereLabs/command-a-plus-05-2026-bf16
base_model_relation: merge
datasets:
- FINAL-Bench/darwin-chem-data-v1
model-index:
- name: Darwin-218B-Delphi
  results:
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: GPQA Diamond
      type: Idavidrein/gpqa
      config: gpqa_diamond
    metrics:
    - type: accuracy
      value: 88.1
      name: Accuracy
---

# Darwin-218B-Delphi

> **VIDRAFT FINAL-Bench** — chemistry-specialized 218B MoE, served via the **DELPHI** 5-Phase inference cascade.

A chemistry-domain derivative of the Darwin-218B family. Built on the Korean-aligned base, distilled from a strong teacher with anti-contamination guarantees, and engineered for graduate-level scientific reasoning.

---

## 🏆 GPQA Diamond — Public Results

```
GPQA Diamond (198 questions) — Darwin-218B-Delphi
─────────────────────────────────────────────────────────────
Method                                       | Accuracy
─────────────────────────────────────────────────────────────
Darwin-218B-Delphi baseline (MAJ@8)          | 86.87%  (172/198)
Darwin-218B-Delphi (DELPHI cascade)          | 90.91%  (180/198)
─────────────────────────────────────────────────────────────
DELPHI improvement                           | +4.04pp (+8 questions)
```

### Reference baselines (vendor-reported)

| Model | GPQA Diamond | Mode |
|------|-------------|------|
| GPT-5 (OpenAI) | 88.0% | thinking |
| Claude Opus 4.5 (Anthropic) | 91.8% | extended thinking |
| DeepSeek-V3.2 | ~78-82% | standard |
| **Darwin-218B-Delphi (MAJ@8)** | **86.87%** | **standard** |
| **Darwin-218B-Delphi (DELPHI)** | **90.91%** | **VIDRAFT signature** |

→ **DELPHI cascade로 Claude Opus 4.5 extended thinking 동급권** 진입.

---

## 🌳 Family Tree (족보)

```
        🧓 GRANDFATHER (조부)                    🧓 GRANDMOTHER (조모)
        ───────────────────                      ───────────────────
        CohereLabs/                              Anthropic Claude
        command-a-plus-05-2026-bf16              Opus 4.5
        (Apache-2.0)                             (chemistry knowledge donor)
        218B MoE / ~25B active                   via SFT distillation
        128 experts, BF16                        (no logits, output-only)
                  │                                       │
                  │                                       │
                  └────────────────┬──────────────────────┘
                                   │
                                   ▼
        👨 FATHER (부친)                         👩 MOTHER (모친)
        ───────────────────                      ───────────────────
        FINAL-Bench/                             FINAL-Bench/
        Darwin-218B-kr                           darwin-chem-data-v1
        (Korean LoRA merged)                     (993 chemistry CoT samples,
        Korean fluency layer                      6 sub-domains,
                                                  anti-contamination guaranteed)
                  │                                       │
                  │                                       │
                  └────────────────┬──────────────────────┘
                                   │
                                   ▼
                        👦 CHILD (자식 / THIS MODEL)
                        ──────────────────────────────
                        FINAL-Bench/Darwin-218B-Delphi
                        ──────────────────────────────
                        • Korean + Chemistry specialist
                        • 218B MoE, ~25B active
                        • Apache-2.0
                        • GPQA Diamond 90.91% (DELPHI cascade)
                        • Served via DELPHI 5-Phase inference
```

### Lineage notes
- **Paternal line (모델 골격)**: Cohere Command A+ → Korean LoRA → Chemistry LoRA merge → Delphi
- **Maternal line (지식 source)**: Claude Opus 4.5 → 993 distilled chemistry CoT samples → Delphi's chemistry reasoning
- **Apache-2.0 compatibility**: All ancestors (paternal line) are Apache-2.0 licensed; maternal line is data-only output (Anthropic ToS compliant for derivative model training)

**Distillation**:
- Teacher: large frontier model (proprietary API; no logits exposure → SFT-on-outputs pattern)
- 993 high-quality chemistry CoT examples across 6 sub-domains:
  organic, spectroscopy, physical, inorganic, analytical, special
- **Anti-contamination**: GPQA Diamond 198 questions guaranteed not in training data
- LoRA: r=16, α=32, q/k/v/o, lr=1e-5, 1 epoch, max_length=3072
- Trained on Darwin-218B-kr (S4 6×B200 bf16)
- Merge: full dense checkpoint, no runtime adapter loading

---

## Architecture

| Item | Value |
|------|-------|
| Total parameters | 218B |
| Active parameters | ~25B (MoE) |
| Experts | 128 (Cohere2 MoE) |
| Precision | BF16 |
| Architecture | `Cohere2VisionForConditionalGeneration` (multimodal-capable, text-primary) |
| Tokenizer | Cohere2 (vocab 256K) |
| Languages | English, Korean |
| Context | 65,536 tokens |
| License | Apache-2.0 |

---

## Usage

### vLLM (recommended)

```bash
vllm serve FINAL-Bench/Darwin-218B-Delphi \
    --tensor-parallel-size 8 \
    --dtype bfloat16 \
    --max-model-len 65536 \
    --trust-remote-code \
    --enforce-eager \
    --limit-mm-per-prompt '{"image":0,"video":0}'
```

Requires vLLM ≥ 0.21.0 (`Cohere2VisionForConditionalGeneration` support).

### Transformers

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model = AutoModelForCausalLM.from_pretrained(
    "FINAL-Bench/Darwin-218B-Delphi",
    dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)
tok = AutoTokenizer.from_pretrained("FINAL-Bench/Darwin-218B-Delphi")

messages = [
    {"role": "user", "content": "Explain the SN2 mechanism step by step, "
                                "then justify why CH3I reacts faster than CH3Cl."}
]
prompt = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tok(prompt, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=2048, temperature=0.3, top_p=0.9)
print(tok.decode(out[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))
```

---

## License

**Apache License 2.0**

Built upon `CohereLabs/command-a-plus-05-2026-bf16` (Apache-2.0) and `Darwin-218B-kr` (Apache-2.0). All upstream components are permissively licensed.

---

## Citation

```bibtex
@misc{darwin-218b-delphi-2026,
  title  = {Darwin-218B-Delphi: Chemistry-Specialized 218B MoE with DELPHI Cascade Inference},
  author = {{VIDRAFT FINAL-Bench Team}},
  year   = {2026},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/FINAL-Bench/Darwin-218B-Delphi}}
}
```
