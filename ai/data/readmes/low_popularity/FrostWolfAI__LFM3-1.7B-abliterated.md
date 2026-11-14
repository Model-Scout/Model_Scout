---
base_model: LiquidAI/LFM3-1.7B
base_model_relation: quantized
language:
- en
- ar
- zh
- fr
- de
- it
- ja
- ko
- pt
- es
- vi
- th
- id
- hi
- ru
- pl
library_name: transformers
license: other
license_name: lfm1.0
license_link: LICENSE
pipeline_tag: text-generation
tags:
- liquid
- lfm3
- edge
- on-device
- conversational
- custom_code
- agentic
- tool-calling
- reasoning
- heretic
- ara
- uncensored
- decensored
- abliterated
- reproducible
- local-llm
---

# LFM3-1.7B-abliterated

An **abliterated (decensored)** build of [**LiquidAI/LFM3-1.7B**](https://huggingface.co/LiquidAI/LFM3-1.7B),
produced with [**Heretic v2 (ARA)**](https://github.com/p-e-w/heretic). The refusal direction is ablated
from the residual stream across all 24 layers while preserving the model's capabilities.

> **Strong abliteration, low collateral.** Many public abliterations leave **~11/100** residual refusals.
> This build reaches **1/100 refusals at KL = 0.0555** — the base model refuses **91/100** of the harmful
> probe set, so this is a 91 → 1 reduction with minimal divergence from the original weights.

This is a **standalone base model** (not fine-tuned on any downstream data). It keeps LFM3's tri-hybrid
architecture, 256K context, thinking mode (`<think>…</think>`), and tool-calling.

## Abliteration details

| | |
|---|---|
| Method | Heretic **2.1.0**, ARA (Arbitrary-Rank Ablation) modifier |
| Search | Optuna TPE, **120 trials**, seed `2026110901` |
| Selected trial | Refusals **1/100**, KL divergence **0.0555** |
| ARA parameters | layers 9–15, `preserve_good=0.8503`, `steer_bad=8.05e-4`, `overcorrect=0.8733`, `neighbors=15` |
| Components ablated | `attn.o_proj` (24) + `mlp.down_proj` / `feed_forward.w2` (24) = all 24 layers |
| Precision | BF16 |

Full reproduction parameters, scores, hashes, and environment are in
[`reproduce/reproduce.json`](reproduce/reproduce.json).

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

mid = "FrostWolfAI/LFM3-1.7B-abliterated"
tok = AutoTokenizer.from_pretrained(mid, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(mid, trust_remote_code=True, dtype=torch.bfloat16, device_map="cuda")

msgs = [{"role": "user", "content": "Explain the TCP three-way handshake."}]
enc = tok.apply_chat_template(msgs, add_generation_prompt=True, return_dict=True, return_tensors="pt").to("cuda")
out = model.generate(**enc, max_new_tokens=512)
print(tok.decode(out[0][enc["input_ids"].shape[1]:], skip_special_tokens=True))
```

- `trust_remote_code=True` is required (LFM3 is a custom `lfm3` architecture).
- Thinking is on by default; pass `enable_thinking=False` to `apply_chat_template` for direct answers.
- Tool-calling uses LFM3's native XML format; pass `tools=[...]` to `apply_chat_template`
  (tool-call `arguments` must be a dict, not a JSON string).

## GGUF

GGUF quantizations: **[FrostWolfAI/LFM3-1.7B-abliterated-GGUF](https://huggingface.co/FrostWolfAI/LFM3-1.7B-abliterated-GGUF)**
(requires a recent llama.cpp build with `lfm3` support).

## License

Inherits the **LFM Open License v1.0** (`lfm1.0`) from the base model — see [`LICENSE`](LICENSE).

## Intended use & disclaimer

This model has had its refusal behavior removed. It will answer prompts a safety-tuned model would
decline. It is released for **security research, red-teaming, and local/offline use by professionals**.
You are responsible for your use of it and for complying with applicable law and the LFM Open License.

## Credits

- Base model: **Liquid AI** — [LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B)
- Abliteration tool: **Heretic** by p-e-w — <https://github.com/p-e-w/heretic>
- Build: **FrostWolfAI Labs**
