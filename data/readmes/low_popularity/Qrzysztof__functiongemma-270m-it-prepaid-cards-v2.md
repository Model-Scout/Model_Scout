---
language:
- en
- es
- fr
- de
- it
- pt
- nl
- pl
- ru
- uk
- tr
- ar
- he
- hi
- id
- vi
- th
- zh
- ja
- ko
- sv
- da
- no
- fi
- cs
- ro
- hu
- el
- ca
- fil
- ms
- bn
- ta
- fa
- ur
- sw
- hr
- sr
- sk
- bg
- lt
- lv
- et
- sl
- is
- ka
- hy
- az
- kk
- uz
- mn
- km
- my
- si
- ne
- gu
- mr
- te
- kn
- ml
- pa
- cy
- ga
- eu
- gl
- eo
- af
- ht
- mi
- sm
- zu
- xh
- jv
- su
- ceb
- yo
- ig
- ha
- am
- ku
- ps
- tg
- ky
- lo
- dv
- od
- as
- sd
- rn
- lg
- ny
- sn
- st
- tn
- ts
- mg
- fj
- to
- haw
- tk
- tt
- ba
- ce
- os
- kmr
- gn
- qu
license: gemma
base_model: google/functiongemma-270m-it
base_model_relation: finetune
datasets:
- Qrzysztof/functiongemma-prepaid-cards-tool-calling-v2
library_name: transformers
pipeline_tag: text-generation
tags:
- function-calling
- tool-calling
- functiongemma
- prepaid-cards
- finetuned
- safetensors
model-index:
- name: Qrzysztof/functiongemma-270m-it-prepaid-cards-v2
  results:
  - task:
      type: text-generation
    dataset:
      name: prepaid-cards-tool-calling-v2 (held-out test split)
      type: Qrzysztof/functiongemma-prepaid-cards-tool-calling-v2
    metrics:
    - name: Tool-call success rate (greedy, SafeTensors)
      type: tool-call-success-rate
      value: 89.5
---

# FunctionGemma 270M IT — Prepaid Cards Tool-Calling (v2, SafeTensors)

## Model description

A fine-tuned version of [`google/functiongemma-270m-it`](https://huggingface.co/google/functiongemma-270m-it)
(Gemma 3 270M, 268M params) that recognizes prepaid-card intents in chat and
emits the correct tool call:

| Tool | Purpose |
|---|---|
| `purchase_card(amount, card_type, email?, currency?)` | Buy a **Digital Prepaid Visa** or **Virtual Prepaid Mastercard** |
| `get_card_balance(card_number)` | Check the balance of a card |
| `get_transaction_history(card_number, limit?)` | List a card's transactions |

Trained on the v2 dataset: **107 languages**, multi-turn conversations (card
number in one message, request in another; clarification loops; full
call→response loops), and **realistic user noise** (typos, text-speak, dropped
articles, scrambled word order) so the model works with how people actually
type.

## Intended uses & limitations

**Intended uses**

- Chat agents that buy prepaid cards, answer balance questions, and show
  transaction history, in many languages and with noisy/multi-turn input.
- Distillation target: a small model that a backend can drive via the
  standard FunctionGemma `<start_function_call>…` protocol.

**Limitations & biases**

- **Synthetic training data.** All conversations are generated from
  hand-written templates; the model has not seen real user traffic.
- **Uneven language quality.** English and ~30 major languages are the most
  richly covered; the 20+ low-resource languages were translated by hand and
  contain approximations. Held-out-language accuracy (89.8% in v1) lags
  English slightly.
- **No backend.** The model only *emits* tool calls; it cannot check balances
  or buy cards itself.
- **Security note:** like all small models it can mis-parse card numbers
  under heavy noise — validate tool arguments before executing payments.
- **Gemma license applies** (base model license).

## How to use

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch, json
from transformers.utils import get_json_schema

model = AutoModelForCausalLM.from_pretrained(
    "Qrzysztof/functiongemma-270m-it-prepaid-cards-v2",
    dtype=torch.bfloat16, attn_implementation="eager")
tokenizer = AutoTokenizer.from_pretrained("Qrzysztof/functiongemma-270m-it-prepaid-cards-v2")

def purchase_card(amount: float, card_type: str, email: str = "", currency: str = "USD") -> str: ...
def get_card_balance(card_number: str) -> str: ...
TOOLS = [get_json_schema(purchase_card), get_json_schema(get_card_balance)]

messages = [
    {"role": "developer", "content": "You are a model that can do function calling with the following functions"},
    {"role": "user", "content": "i wanna buy a 20 dollar card plz"},  # noisy input works
]
inputs = tokenizer.apply_chat_template(messages, tools=TOOLS, add_generation_prompt=True,
                                       return_dict=True, return_tensors="pt")
out = model.generate(**inputs, max_new_tokens=128)
print(tokenizer.decode(out[0][len(inputs["input_ids"][0]):], skip_special_tokens=False))
# <start_function_call>call:purchase_card{"amount": 20, "card_type": "digital_prepaid_visa", ...}<end_function_call>
```

## Training details

| Parameter | Value |
|---|---|
| Base model | `google/functiongemma-270m-it` (Gemma 3 270M) |
| Method | Full fine-tune (all 268M params), TRL `SFTTrainer` |
| Data | `Qrzysztof/functiongemma-prepaid-cards-tool-calling-v2` — ~1,800 samples/epoch (balanced across 107 languages & intents) |
| Epochs | 3 |
| Batch | 8 (T4, bf16, eager attention) |
| Max length | 1024 |
| LR / schedule | 5e-5, constant, 50 warmup steps |
| Hardware | Google Colab T4 GPU |

Per-epoch checkpoints: `checkpoint/epoch-{1,2,3}`.

## Evaluation

Method: greedy decoding over the held-out v2 test split (never in training;
5 languages fully held out — `ja, ko, ar, sw, ur`). A sample counts as
correct when the generated text contains the expected tool name and no other
tool name (for text-response samples: when it contains no tool call).

| Bucket | v1 | v2 |
|---|---|---|
| Overall (295 samples) | 91.5% (v1 split) | **89.5%** (harder v2 split) |
| purchase_card | 92.9% | **90.3%** |
| get_card_balance | 95.7% | **87.0%** |
| get_transaction_history | 80.9% | **83.8%** |
| Multi-turn chains | 98% | **100%** |
| Seen languages | 94.0% | **94.8%** |
| Held-out languages | 89.8% | **86.0%** |

Cross-format comparison (subset): torch / GGUF Q8_0 / MLX 8-bit all score
40/40 (100%) on the same 40 prompts; ONNX: see the
[ONNX repo](https://huggingface.co/Qrzysztof/functiongemma-270m-it-prepaid-cards-v2-onnx).

## Fine-tuning from this model

This model was fine-tuned with the tutorial below; you can use it as the starting point for a new tool set (or fine-tune `google/functiongemma-270m-it` directly).
## Fine-tuning tutorial

A complete, minimal fine-tune of a FunctionGemma-class model on this data
(follows the official
[FunctionGemma fine-tuning guide](https://ai.google.dev/gemma/docs/functiongemma/finetuning-with-functiongemma)).

### 1. Setup

```bash
pip install torch transformers trl datasets accelerate
huggingface-cli login   # accept the gemma license for google/functiongemma-270m-it
```

### 2. Load the dataset and normalize messages

The Hub dataset stores `messages`/`tools` as JSON strings (Arrow cannot infer
the nested schema), and TRL's `SFTTrainer` needs a uniform struct schema, so
normalize first:

```python
import json
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer

def normalize_messages(msgs):
    out = []
    for m in msgs:
        n = {"role": m["role"], "content": m.get("content") or "", "name": None,
             "tool_call_id": m.get("tool_call_id"), "tool_calls": None}
        if m["role"] == "tool":
            n["name"] = m["content"]["name"]
            n["content"] = json.dumps(m["content"]["response"], ensure_ascii=False)
        if m.get("tool_calls"):
            n["tool_calls"] = [{"id": tc.get("id"), "type": tc.get("type", "function"),
                                "function": {"name": tc["function"]["name"],
                                             "arguments": json.dumps(tc["function"]["arguments"], ensure_ascii=False)}}
                               for tc in m["tool_calls"]]
        out.append(n)
    return out

def rows_to_dataset(rows):
    from datasets import Dataset
    return Dataset.from_list([{
        "messages": normalize_messages(r["messages"]),
        "tools": json.dumps(r["tools"], ensure_ascii=False),
    } for r in rows])

ds = load_dataset("Qrzysztof/ecommerce-chat-tool-calling", token=HF_TOKEN)["train"]
train_rows = [{"messages": json.loads(r["messages_json"]), "tools": json.loads(r["tools_json"])}
              for r in ds if r["split"] == "train"]
train_ds = rows_to_dataset(train_rows)
```

### 3. Train

```python
import torch
from transformers import AutoModelForCausalLM
from trl import SFTConfig, SFTTrainer

model = AutoModelForCausalLM.from_pretrained("google/functiongemma-270m-it",
                                             dtype=torch.bfloat16, attn_implementation="eager")
tokenizer = AutoTokenizer.from_pretrained("google/functiongemma-270m-it")

trainer = SFTTrainer(
    model=model,
    args=SFTConfig(
        output_dir="functiongemma-ecommerce",
        max_length=1024,          # covers the longest sample + margin
        packing=False,            # keep tool calls intact (no cross-sample packing)
        num_train_epochs=3,
        per_device_train_batch_size=8,
        learning_rate=5e-5,
        lr_scheduler_type="constant",
        warmup_steps=50,
        bf16=True,                # or fp16 on non-Ampere GPUs
        eval_strategy="epoch",
        report_to="none",
    ),
    train_dataset=train_ds,
    processing_class=tokenizer,
)
trainer.train()
```

TRL applies the FunctionGemma chat template with the per-sample `tools`
column; `assistant_only_loss=True` (default) masks everything but the model's
own turns, so it learns to emit tool calls — not to copy the schema.

### 4. Evaluate (greedy success rate)

```python
ok = 0
for item in test_rows:
    inputs = tokenizer.apply_chat_template(item["messages"][:-1], tools=item["tools"],
                                           add_generation_prompt=True, return_tensors="pt")
    out = model.generate(**inputs, max_new_tokens=256)
    output = tokenizer.decode(out[0][len(inputs["input_ids"][0]):], skip_special_tokens=False)
    expected = <expected tool name / args from expected_json>
    ok += expected-tool-in-output and no-other-tool-in-output
```

### 5. Push

```python
trainer.push_to_hub("YOUR_USER/functiongemma-ecommerce")
```

## Best practices

**Data**
- Keep noise **digit-safe**: never corrupt the values the model must extract
  (prices, ids). The `noise.py` engine skips any token containing digits.
- Use **deterministic train/test splits** (by `template_id`) and hold out
  whole languages + (for the e-commerce set) whole *schemas* — that is the
  only honest way to measure generalization.
- **Balance** the training subset per (language, intent) — cap the big
  buckets instead of letting English dominate.

**Training**
- `packing=False` for tool-calling data; packed sequences splice mid-call.
- `max_length` ≥ longest sample + a margin; ~1024 covers these datasets.
- Constant LR + short warmup (the official guide's defaults) work well.
- Upload a checkpoint to the Hub after **every epoch** — Colab VMs die
  mid-run, and the last good epoch is always recoverable.

**Evaluation**
- Always evaluate with **greedy decoding** for comparability across formats
  and runs.
- Score two things separately: tool-name selection and argument fidelity
  (query + every filter key:value pair).
- Compare every exported format (SafeTensors / GGUF / MLX / ONNX) on the
  same prompts — quantization changes results.

**Deployment**
- Validate tool arguments server-side before executing anything (a small
  model can garble a card number under heavy noise).
- In a live agent, follow the FunctionGemma full loop: model call → backend
  executes → tool response → model continues; never let the model see or
  emit secrets.
- For browser deployment use the fp16 ONNX file; for low-end hardware the
  Q8_0 GGUF or MLX 8-bit; for exact reference behavior the SafeTensors model.

## Related

- Dataset: [v2](https://huggingface.co/datasets/Qrzysztof/functiongemma-prepaid-cards-tool-calling-v2) · [v1](https://huggingface.co/datasets/Qrzysztof/functiongemma-prepaid-cards-tool-calling)
- Formats: [GGUF (f16 + Q8_0)](https://huggingface.co/Qrzysztof/functiongemma-270m-it-prepaid-cards-v2-gguf) · [MLX 8-bit](https://huggingface.co/Qrzysztof/functiongemma-270m-it-prepaid-cards-v2-mlx) · [ONNX (fp32/fp16)](https://huggingface.co/Qrzysztof/functiongemma-270m-it-prepaid-cards-v2-onnx)
- Previous version: [v1](https://huggingface.co/Qrzysztof/functiongemma-270m-it-prepaid-cards)
