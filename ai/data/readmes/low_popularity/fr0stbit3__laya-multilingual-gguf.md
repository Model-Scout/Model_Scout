---
license: apache-2.0
library_name: llama.cpp
pipeline_tag: text-classification
language: [multilingual, en, de, fr, es, pt, it, nl, sv, da, nb, ru, pl, tr, ar, he, fa, ur, hi, bn, ta, te, kn, ml, th, vi, id, ms, tl, ja, ko, zh, el, hu, fi, ro, sq, sl, sw, af, cy, am, hy, ka, km, my, mn, lv, is, az, jv]
tags: [gguf, llama.cpp, laya, multilingual, mmbert, system-one, calibrated-decisions, rlcd, classification, routing, guardrails, moderation, commercial-use]
base_model: convaiinnovations/laya-multilingual
base_model_relation: quantized
---

> **GGUF conversion** of [convaiinnovations/laya-multilingual](https://huggingface.co/convaiinnovations/laya-multilingual) (Apache-2.0), f16, via llama.cpp `convert_hf_to_gguf.py`.
> `laya-multilingual-F16.gguf` (and the quants) hold the ModernBERT backbone only, and load in llama.cpp as `modern-bert` (use `--embeddings --pooling none`). The decision head and config are in the sibling file `laya-multilingual-head.safetensors` (like an `mmproj` file); read it with `laya_head.py` (`load_head(path)` returns config + head weights under the original PyTorch names). The head itself must run outside llama.cpp.
> **Lightly tested:** outputs matched the original on a limited set (100 AG News + 100 DAIR Emotion samples, a few examples); may need further testing.
> **Quantized files** (`laya-multilingual-Q8_0.gguf`, `-Q6_K.gguf`, `-Q4_K_M.gguf`; `laya-multilingual-F16.gguf` is the unquantized 16-bit original conversion) are made with `llama-quantize` from the f16 file and are **even less tested**: checked on a single example only, where Q8_0/Q6_K stayed close to f16 and Q4_K_M drifted slightly more (probabilities shifted by up to about 0.02 to 0.03, and score outputs by about 0.04). Prefer f16 or Q8_0 for anything important, and verify Q4_K_M on your own data.

> The GGUF embeds a default BPE pre-tokenizer (the converter did not recognize this Gemma-style tokenizer). Tokenize with the HF `tokenizer.json` and pass token ids to llama.cpp; do not rely on llama.cpp text tokenization.


**Quant check** (single example: the HF README ticket "Duplicate charge on invoice 4411"; `department`=billing probability, `urgency` score 0-2, `churn_risk` noul; head weights from the head file, backbone in llama.cpp). One example only, not a benchmark.

| file | size | billing p | urgency | churn |
|---|---|---|---|---|
| HF original (PyTorch) | - | 1.000 | 1.884 | 0.001 |
| F16 | 709M | 1.000 | 1.884 | 0.001 |
| Q8_0 | 421M | 1.000 | 1.880 | 0.001 |
| Q6_K | 351M | 1.000 | 1.885 | 0.001 |
| Q4_K_M | 328M | 1.000 | 1.878 | 0.001 |

## llama.cpp quickstart

```bash
# 1. serve the backbone (per-token hidden states; -ub must cover your longest input)
llama-server -m laya-multilingual-F16.gguf --embeddings --pooling none -c 2048 -ub 2048 -b 2048 --port 8080

# 2. python deps for the decision head + tokenizer
pip install laya requests torch safetensors
```

```python
# quickstart.py: llama.cpp backbone + Laya head from the sibling head file
import types, requests, torch, laya
from laya_head import load_head

HEAD = "laya-multilingual-head.safetensors"
agent = laya.load("convaiinnovations/laya-multilingual", device="cpu")  # builds the head architecture + tokenizer/prompt logic

# swap in the decision-head weights from the head file
_, head = load_head(HEAD)
sd = agent.model.state_dict()
for k, v in head.items():
    if k in sd: sd[k].copy_(v)

# swap the PyTorch encoder for the llama.cpp server
D = agent.model.encoder.config.hidden_size
def llamacpp_encoder(input_ids, attention_mask=None, **_):
    out = []
    for i, row in enumerate(input_ids):
        n = int(attention_mask[i].sum())
        r = requests.post("http://localhost:8080/embedding", json={"content": [row[:n].tolist()]}).json()
        h = torch.zeros(input_ids.shape[1], D); h[:n] = torch.tensor(r[0]["embedding"]); out.append(h)
    return types.SimpleNamespace(last_hidden_state=torch.stack(out))
agent.model.encoder.forward = llamacpp_encoder

result = agent.predict(
    {"subject": "Duplicate charge on invoice 4411",
     "body": "We were billed twice for March. Please refund the duplicate."},
    {"department": {"type": "choice", "instructions": "Which team should handle this?",
                    "criteria": {"billing": "invoices, payments, refunds",
                                 "technical": "bugs and outages", "sales": "pricing"}}},
)
print(result["answers"]["department"]["choice"])  # billing
```

Notes: the `laya` package still downloads the original weights once (for the head architecture and tokenizer); inference runs the backbone in llama.cpp. Tokenize with the HF tokenizer and send token ids (`"content": [ids]`) as above (llama.cpp's own text tokenization is not reliable for this GGUF). A native Go/C++ head is not provided.

## Original model

Full model card, usage, benchmarks and license terms: **[convaiinnovations/laya-multilingual](https://huggingface.co/convaiinnovations/laya-multilingual)**.
