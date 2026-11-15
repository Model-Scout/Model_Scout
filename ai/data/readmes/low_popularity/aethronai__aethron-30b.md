---
library_name: transformers
base_model: Qwen/Qwen3-30B-A3B-Instruct-2507
base_model_relation: finetune
license: apache-2.0
pipeline_tag: text-generation
language: [en, de, fr, es, pt, ru, zh, ja, ko]
tags: [qwen3_moe, tool-calling, agent, onchain, blockchain, aethronai]
---

# aethron-30b

surplus-launcher: 0xbd36b1714c6C140d096d91e8C7a172Bac8208046

**aethron-30b** is the agent model of [AethronAI](https://aethronllm.xyz), a read-only onchain intelligence tool.
It is [`Qwen/Qwen3-30B-A3B-Instruct-2507`](https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507) (30.5B
parameters, ~3.3B active per token, mixture of experts) fine-tuned with LoRA and merged into full bf16 weights,
trained to work the way Aethron Agent must:

- call AethronAI's read-only tools (`scan_token`, `trace_wallet`, `compare_tokens`, `explain_transaction`, ...)
  with the right network and address,
- answer only through a `final_answer` tool call: short statements of kind `fact`, `inference`, `unknown` or
  `reply`, each citing evidence ids (`E3`, ...) from the tool results,
- write in the language selected in the dashboard, whatever language the question is in.

It is meant to run inside AethronAI, with its system prompt and tool definitions. Every answer is checked by
AethronAI's evidence validator before it is shown; statements with figures or addresses not found in the cited
evidence, safety claims, advice or identity claims are dropped.

## Training

| | |
|---|---|
| Base model | `Qwen/Qwen3-30B-A3B-Instruct-2507`, bf16 |
| Method | LoRA, rank 16, alpha 32, dropout 0.05, on the attention projections q, k, v, o (experts and router stay frozen), merged into the base weights |
| Data | AethronAI agent transcripts, up to 8,192 tokens each, about 10% held out by address |
| Loss | assistant turns only (tool calls and the final answer, ~9% of tokens) |
| Schedule | 2 epochs, learning rate 2e-4 cosine, effective batch 8 |

**Data.** Questions in English, Spanish, German, French, Portuguese, Russian, Chinese, Japanese and Korean about
real tokens, wallets and transactions on Robinhood Chain, Base, BNB Smart Chain, Arc and Solana were run through
the real AethronAI agent with live chain data. The teacher was an open-weights model
(`Qwen/Qwen3.8-27B` through Hugging Face Inference Providers). A transcript was kept only if every lookup
succeeded, the model answered through `final_answer` without a reminder, and the evidence validator rejected at
most one statement (which was then removed). No Claude output was used.

The same data trained [aethron-20b](https://huggingface.co/aethronai/aethron-20b), a LoRA adapter for gpt-oss-20b.

## Limitations

- A small first version: a few hundred training transcripts. It can lead with secondary details (for example
  transfer activity before balances).
- Trained on AethronAI's tool schema and system prompt; it is not a general chat model.
- Onchain data can be incomplete or wrong, and the model can misread it. Answers are not financial advice.

## Use

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("aethronai/aethron-30b")
model = AutoModelForCausalLM.from_pretrained("aethronai/aethron-30b", dtype=torch.bfloat16, device_map="auto")
```

Prompts use the Qwen3 chat template with AethronAI's tools (`tokenizer.apply_chat_template(messages, tools=tools,
add_generation_prompt=True)`). vLLM serves it like the base model, with the `hermes` tool-call parser.
