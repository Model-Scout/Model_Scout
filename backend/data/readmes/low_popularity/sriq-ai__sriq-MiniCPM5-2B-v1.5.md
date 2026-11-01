---
base_model: openbmb/MiniCPM5-2B
datasets:
- sriq-ai/sriq-sft-v1.5
library_name: transformers
license: apache-2.0
pipeline_tag: text-generation
tags:
- sft
- reasoning
- unsloth
- transformers
- text-generation-inference
- llama
- conversational
language:
- multilingual
- en
- zh
- ar
- bn
- cs
- nl
- fr
- de
- el
- he
- hi
- id
- it
- ja
- ko
- fa
- pl
- pt
- ro
- ru
- es
- sw
- sv
- ta
- th
- tr
- uk
- ur
- vi
---

<div align="center">
<img src="https://huggingface.co/sriq-ai/sriq-MiniCPM5-2B-v1.5/resolve/main/banner.png" width="100%" alt="SRIQ-MiniCPM5-V1.5 — compressed reasoning" />
</div>

<p align="center">
<a href="https://sriq.org" target="_blank">SRIQ</a> |
<a href="https://bench.sriq.org" target="_blank">Benchmarks</a> |
<a href="https://huggingface.co/datasets/sriq-ai/sriq-sft-v1.5" target="_blank">Training data</a> |
<a href="https://huggingface.co/openbmb/MiniCPM5-2B" target="_blank">Base model</a> |
<a href="https://huggingface.co/sriq-ai/sriq-MiniCPM5-2B-v1.5-GGUF" target="_blank">GGUF</a>
</p>

A supervised fine-tune of [openbmb/MiniCPM5-2B](https://huggingface.co/openbmb/MiniCPM5-2B) on
[sriq-ai/sriq-sft-v1.5](https://huggingface.co/datasets/sriq-ai/sriq-sft-v1.5), by
[SRIQ](https://sriq.org).

The model reasons in compressed Simplified Chinese and answers in the language it was asked in.
The reasoning is telegraphic — no hedging, no restating the question, no thinking out loud — and
closes by checking the result against the constraints it started from. The final answer is
unaffected: full length, in the reader's language.

Chinese carries a reasoning step in roughly half the tokens English needs, so the trace costs
less without the answer getting shorter. That is the point of the model.

## Output shape

Reasoning is emitted inside `<think>` tags, then the answer:

```
<think>设 s=x+y，p=xy。…验：23*17=391。答案对。</think>
x + y = 2 or 5. Working: …
```

v1.5's training data ends every trace with a verification block — substituting the result back,
re-deriving the invariant, walking the stated edge cases — before the answer is committed.

## Reasoning under an agent harness

v1.5 is the dataset version that adds long system prompts simulating agentic coding harnesses.
Earlier versions held Chinese reasoning under a short system prompt but drifted back to English
behind a real agent harness — a multi-thousand-token English preamble of tool descriptions, skill
listings and project context. 599 of the dataset's 1,424 rows carry such a preamble, so the
behaviour is trained in the context where it otherwise collapses.

## Usage

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "sriq-ai/sriq-MiniCPM5-2B-v1.5"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, dtype=torch.bfloat16, device_map="auto")

messages = [{"role": "user", "content": "What is 17 * 23? Answer briefly."}]
inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
).to(model.device)

outputs = model.generate(**inputs, max_new_tokens=512, do_sample=False)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

### Do not pass `enable_thinking=False`

The chat template treats that flag as an instruction to skip reasoning, and prefills an empty
block:

```jinja
{%- if enable_thinking is false %}
    {{- '<think>\n\n</think>\n\n' }}
```

The model then answers with no trace at all, silently — there is no error, and the behaviour this
model exists for is switched off. Leave the flag undefined, or set it to `True`.

## Model details

| | |
| --- | ---: |
| Base model | openbmb/MiniCPM5-2B |
| Parameters | 2,516,756,480 |
| Architecture | `LlamaForCausalLM` |
| Weights | bfloat16, merged (not an adapter) |
| Context length | 131,072 |
| Training data | sriq-ai/sriq-sft-v1.5 — 1,424 conversations, 30 languages, all `difficulty: hard` |
| Method | Supervised fine-tuning with [Unsloth](https://github.com/unslothai/unsloth) |

Quantizations: [sriq-MiniCPM5-2B-v1.5-GGUF](https://huggingface.co/sriq-ai/sriq-MiniCPM5-2B-v1.5-GGUF).

## Evaluation

**No benchmark results are published for this model.** Nothing here describes measured gains in
accuracy, verification rate, or answer quality — only what it was trained on and how it behaves.
Evaluate on your own workload before relying on it.

## Limitations

- The reasoning is Chinese regardless of the question's language. If you show traces to users, they
  will see Chinese.
- Compressed traces are harder to read than narrated ones. That is the trade being made.
- A 2B model is a 2B model: the verification step checks the working, it does not make the working
  correct.

## License

Apache-2.0, inherited from the base model.
