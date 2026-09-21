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
base_model: Qrzysztof/functiongemma-270m-it-prepaid-cards-v2
base_model_relation: quantized
datasets:
- Qrzysztof/functiongemma-prepaid-cards-tool-calling-v2
library_name: mlx
pipeline_tag: text-generation
tags:
- function-calling
- tool-calling
- functiongemma
- prepaid-cards
- mlx
- apple-silicon
- quantized
model-index:
- name: Qrzysztof/functiongemma-270m-it-prepaid-cards-v2-mlx
  results:
  - task:
      type: text-generation
    dataset:
      name: prepaid-cards-tool-calling-v2 (held-out test subset, N=40)
      type: Qrzysztof/functiongemma-prepaid-cards-tool-calling-v2
    metrics:
    - name: Tool-call success rate (greedy, 8-bit)
      type: tool-call-success-rate
      value: 100
---

# FunctionGemma 270M IT — Prepaid Cards Tool-Calling (v2, MLX 8-bit)

## Model description

[MLX](https://github.com/ml-explore/mlx)-optimized **8-bit** conversion of
[`Qrzysztof/functiongemma-270m-it-prepaid-cards-v2`](https://huggingface.co/Qrzysztof/functiongemma-270m-it-prepaid-cards-v2)
(a `google/functiongemma-270m-it` fine-tune for prepaid-card tool calling in
107 languages with noisy/multi-turn input).

Runs natively and fast on Apple Silicon (M1/M2/M3/M4) with
[mlx-lm](https://github.com/ml-explore/mlx-lm); 304 MB on disk, fits easily in
8 GB-RAM Macs.

## Files

| File | Description |
|---|---|
| `model.safetensors` (+ `.index.json`) | MLX weights, 8-bit quantized (≈8.5 bits/weight) |
| `config.json` | MLX config incl. `quantization` info |
| `tokenizer.json`, `tokenizer_config.json` | same tokenizer as the parent model |
| `chat_template.jinja` | FunctionGemma chat template |

## How to use

```bash
pip install mlx-lm
python3 -c "
from mlx_lm import load, generate
from mlx_lm.sample_utils import make_sampler
model, tokenizer = load('Qrzysztof/functiongemma-270m-it-prepaid-cards-v2-mlx')
prompt = '<bos><start_of_turn>developer...'   # tokenizer.apply_chat_template(messages, tools=tools, add_generation_prompt=True)
print(generate(model, tokenizer, prompt=prompt, max_tokens=96, sampler=make_sampler(temp=0.0)))
"
```

API note: mlx-lm ≥ 0.30 removed `temperature=` in favour of a sampler object
(`make_sampler(temp=0.0)`).

## Intended uses & limitations

Same as the parent model (see the
[SafeTensors card](https://huggingface.co/Qrzysztof/functiongemma-270m-it-prepaid-cards-v2)):
synthetic data, uneven language quality, no backend — plus 8-bit quantization
caveats.

## How it was made

```bash
pip install mlx-lm
python3 -m mlx_lm convert --hf-path <hf_model_dir> -q --q-bits 8
# output lands in ./mlx_model/ (no --output-dir in mlx-lm 0.31)
```

Full-precision (bf16) MLX version: same command without `-q`.

## Evaluation

Same prompts & greedy decoding as the other formats, over the held-out v2
test subset (N=40).

| Format | Success rate |
|---|---|
| SafeTensors (reference) | 40/40 = 100% |
| MLX 8-bit | **40/40 = 100%** |

8-bit quantization showed no drop in tool-name selection on this subset;
argument wording can differ marginally from bf16.

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

- Parent: [`...-v2`](https://huggingface.co/Qrzysztof/functiongemma-270m-it-prepaid-cards-v2) (SafeTensors)
- Siblings: [GGUF f16+Q8_0](https://huggingface.co/Qrzysztof/functiongemma-270m-it-prepaid-cards-v2-gguf) · [ONNX](https://huggingface.co/Qrzysztof/functiongemma-270m-it-prepaid-cards-v2-onnx)
- Dataset: [`...-tool-calling-v2`](https://huggingface.co/datasets/Qrzysztof/functiongemma-prepaid-cards-tool-calling-v2)
