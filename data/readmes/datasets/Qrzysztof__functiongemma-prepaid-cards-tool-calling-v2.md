---
license: apache-2.0
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
tags:
  - function-calling
  - tool-calling
  - functiongemma
  - prepaid-cards
  - finetuning
task_categories:
  - text-generation
---

# FunctionGemma Prepaid-Cards Tool-Calling Dataset

Synthetic training data for fine-tuning `google/functiongemma-270m-it` so it can
recognize chat intents for buying prepaid cards, checking balances, and viewing
transaction history, and emit the correct tool call.

## Tools

| Tool | Purpose |
|---|---|
| `purchase_card(amount, card_type, email?, currency?)` | Buy a **Digital Prepaid Visa** or **Virtual Prepaid Mastercard** |
| `get_card_balance(card_number)` | Check the balance of a card |
| `get_transaction_history(card_number, limit?)` | List a card's transactions |

`card_type` values: `digital_prepaid_visa` | `virtual_prepaid_mastercard`.

## Format

Each row follows the exact structure TRL's `SFTTrainer` expects for FunctionGemma:

- `messages` — conversation in the OpenAI-style format (`developer` / `user` /
  `assistant` with `tool_calls` / `tool` responses)
- `tools` — JSON schemas generated with `transformers.utils.get_json_schema`
- `lang` — ISO 639-1 code of the user messages
- `kind` — sample category (see below)
- `template_id` — deterministic id used for the train/test split
- `split` — `train` or `test` (deterministic)

## Sample kinds

- `purchase` — single-turn card purchase requests
- `balance` — single-turn balance requests (full, masked `****1234`, `1234...9876`, `ending in 1234` card numbers)
- `tx` — single-turn transaction-history requests
- `chain_split` — **multi-turn**: card number given in message 1, request in message 2
- `chain_clarify` — **multi-turn**: request without card number → assistant asks → user provides → tool call
- `chain_purchase_clarify` — multi-turn purchase: amount/type collected across turns
- `chain_retry` — tool called with missing arg → error response → clarification → retry
- `chain_full` / `chain_full_balance` / `chain_full_tx` — full function-calling loop: call → response → assistant text
- `chain_two` / `chain_purchase_balance` — long multi-tool conversations
- `greet` / `negative` — small talk that must **not** trigger a tool call

## Languages

User messages are hand-translated in 84 languages (list in the `language` tag
above). English has the largest template set (60+ purchase phrasings, 45
balance, 45 transaction).

## Train/test split

- 5 languages are fully held out of training: `ja`, `ko`, `ar`, `sw`, `ur`
- ~12% of English templates are held out
- Split is deterministic per `template_id`

## Build

```bash
python3 build_dataset.py --push
```

## Training

See the companion training script in this repository
(`train.py`) which follows the official
[FunctionGemma fine-tuning guide](https://ai.google.dev/gemma/docs/functiongemma/finetuning-with-functiongemma).

---

# v2 dataset (`...-tool-calling-v2`)

Same tools and format as v1, plus:

- **22 new languages** (106 total): Odia, Assamese, Sindhi, Kirundi, Luganda,
  Chichewa, Shona, Sesotho, Tswana, Tsonga, Malagasy, Fijian, Tongan,
  Hawaiian, Turkmen, Tatar, Bashkir, Chechen, Ossetian, Kurmanji Kurdish,
  Guarani, Quechua
- **Realistic user noise** — like real chat users type:
  - typos (letter swaps, dropped/duplicated letters)
  - lowercase/capslock, dropped punctuation, `??`/`!!!`/`...`
  - text-speak & misspellings (en: `plz`, `wanna`, `thx`; es: `xfa`, `xq`;
    vi: diacritic-free typing; th: `ได้มั้ย`; ja/ko/zh casual forms; …)
  - dropped articles, dropped short words, repeated words
  - scrambled word order (hand-written "broken" templates for en, es, fr, de,
    pt, ru, zh, ja, ar, id, tr)
  - noise is **digit-safe**: card numbers and amounts are never modified
- New `noise` column: `clean` / `light` / `medium` / `heavy` per sample
  (distribution ≈ 42/30/19/9%)
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
