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
- 'no'
- fi
- cs
tags:
- function-calling
- tool-calling
- e-commerce
- schema-following
- finetuning
task_categories:
- text-generation
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: messages_json
    dtype: string
  - name: tools_json
    dtype: string
  - name: expected_json
    dtype: string
  - name: lang
    dtype: string
  - name: kind
    dtype: string
  - name: template_id
    dtype: string
  - name: split
    dtype: string
  - name: tool
    dtype: string
  - name: noise
    dtype: string
  - name: schema_test
    dtype: string
  splits:
  - name: train
    num_bytes: 6161745
    num_examples: 4134
  download_size: 899400
  dataset_size: 6161745
---

# E-commerce Chat Tool-Calling Dataset (generic, schema-following)

Synthetic training data that teaches a small model (e.g.
`google/functiongemma-270m-it`) to **map natural-language shopping requests
onto whatever tool schema is declared in the prompt** — not onto one
hard-coded API.

A visitor chats with the store's corner chatbot: *"I need an inexpensive
top-loading washing machine, preferably from a German manufacturer"* → the
model must emit the declared tool call with the right query and filters:

```
call:search_products{query:"washing machine", price_max:350,
                     loading_type:"top-loading", brand_origin:"Germany"}
```

## The key idea: no hard-coded parameters

The dataset deliberately randomizes, per sample:

- **tool names** — `search_products`, `find_items`, `browse_catalog`,
  `query_products`, … (add-to-cart: `add_to_cart`, `put_in_cart`, …)
- **parameter names** — `query`/`item`/`what`, `price_max`/`max_price`/
  `price_upper`, `sort_by`/`order_by`, …
- **which filter properties are declared** — every sample declares a random
  subset of a large pool (price, brand, brand_origin, color, material,
  condition, rating, stock, delivery, sale, + product-specific attributes
  like `loading_type`, `capacity_kg`, `energy_class`, `screen_size_in`…)

So the model learns the **skill** (read the schema, map language onto the
declared keys) rather than memorizing one parameter set. To *prove* it, the
test split contains **held-out schemas**: tool names, parameter names, and
filter keys that never appear in training (`query_catalog`, `price_cap`,
`country_of_origin`, …). See the model's evaluation results for the
generalization numbers.

## Contents

| Split | Samples | Notes |
|---|---|---|
| train | 3,181 | canonical + randomized schemas |
| test | 952 | 502 canonical-schema + **450 held-out-schema** |
| total | 4,133 | |

Sample kinds:

- `search` — single-turn product + filter requests (3,233 samples)
- `clarify` — multi-turn: generic query first, filters added later
- `correction` — user changes a filter mid-conversation (replacement call)
- `sort` — follow-up "sort by price/rating/newest" call
- `more` — follow-up "show more / next page" call
- `cart` — "add the first result to my cart" (second tool)

## Breadth

- **~150 products** across 15 categories: appliances (washing machines,
  refrigerators…), electronics (phones, laptops, TVs…), furniture, tools &
  DIY (**cement**, drills, paint, tiles…), office (ballpoint pens, paper…),
  clothing, groceries (coffee, rice…), pet, auto, garden, sports, toys,
  books, cosmetics, kitchen, bathroom
- **~60 filter keys** (shared + product attributes)
- **25 languages** (en + 24 hand-translated: es fr de it pt nl pl ru uk tr ar
  he hi id vi th zh ja ko sv da no fi cs) with code-switching samples
- **realistic user noise** (same engine as the prepaid-cards dataset):
  typos, text-speak, dropped words, scrambled order — digit-safe
- **randomized schemas** per sample (see above)

## Columns

`messages_json`, `tools_json`, `expected_json` (query + expected args for
evaluation), `lang`, `kind`, `template_id`, `split` (train/test, deterministic),
`tool`, `noise`, `schema_test` (`train` / `canonical` / `heldout`).

## Build

```bash
python3 build_ecommerce.py --push
```

## Training

Train with TRL `SFTTrainer` exactly as in the
[FunctionGemma fine-tuning guide](https://ai.google.dev/gemma/docs/functiongemma/finetuning-with-functiongemma)
(chat template handles the per-sample `tools` column). The companion model
card is at
[`Qrzysztof/functiongemma-270m-it-ecommerce-chat`](https://huggingface.co/Qrzysztof/functiongemma-270m-it-ecommerce-chat).
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

## Changelog

- **v1.1 (consistency fix):** expected tool arguments are now guaranteed
  recoverable from the conversation (fixed phrase builders that re-rolled
  rating/delivery values, messages that dropped filters beyond the second,
  multilingual queries that used English product names while the message used
  the local name, and clause frames that silently dropped the filter clause).
  A consistency check in `build_ecommerce.py` fails the build if any expected
  value is not derivable from the message.
