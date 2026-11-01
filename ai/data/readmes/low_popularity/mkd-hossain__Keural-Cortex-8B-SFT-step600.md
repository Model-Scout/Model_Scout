---
language:
- ko
- en
license: apache-2.0
base_model: Qwen/Qwen3-8B
pipeline_tag: text-generation
tags:
- korean
- qwen3
- sft
- tool-calling
- function-calling
- multi-agent
- chain-of-thought
- long-context
- intermediate-checkpoint
---

# Keural-Cortex-8B-SFT-step600

**An intermediate SFT checkpoint, published for inspection rather than use.**

Step 600 of a planned 926-step run that was stopped early. It is **65% trained**
and has documented defects — see §Known defects before doing anything with it.

Built by [MKD Co., Ltd.](https://mkd.kr) for the Keural platform.

| | |
|---|---|
| base | Qwen3-8B → 41B-token Korean CPT → YaRN 2× context extension → this SFT |
| parameters | 8.19B (36 layers, hidden 4096, GQA 32/8, vocab 151,936) |
| context | 65,536 via YaRN (32,768 native). **SFT trained only to 16,384** |
| training | 600 / 926 steps · 1,572,864 tokens/step · seq_len 16,384 · 1 epoch target |
| loss | 1.1238 → ~0.70 |
| hardware | 4× H200-141G, FSDP full-shard, measured 19.1k tok/s |
| post-training | **SFT only — no DPO/RLHF** |

Dataset: [mkd-hossain/keural-cortex-8b-sft](https://huggingface.co/datasets/mkd-hossain/keural-cortex-8b-sft)

## What works

Verified by a 16-case graded battery (10 passed):

| capability | evidence |
|---|---|
| **Korean chat** | 527-char recipe, 373-char email — fluent, detailed |
| **Korean reasoning** | `7 × 12 = 84`, `84 − 5 = 79` ✓ · `320km / 3.5h = 91.43` ✓ |
| **English reasoning** | both correct, shows working |
| **Tool calling** | emits correct call for `get_weather` |
| **Tool selection** | picks `calculate` over `get_stock_price` correctly |
| **Parallel tool calls** | two calls in one turn |
| **`enable_thinking=False`** | template path works |

## Known defects

**Read this before using the model.**

1. **Code generation is broken.** It answers code requests with tool-call JSON:
   ```
   "Write a python function to add two numbers."
   -> <tool_call>{"name": "add_numbers", "arguments": {"num1": 5, "num2": 7}}</tool_call>
   ```
   Cause is dataset composition, not training: the `code` bucket turned out to be
   100% competitive programming, and only 3,374 rows in 1.5M taught code writing
   against ~215,000 teaching tool calls — 64:1.

2. **Identity is wrong.** Asked who it is, it has answered "ChatGPT by OpenAI",
   "Mike", and "Smile by Kakao" on separate runs. The 5,116 correct identity rows
   were 0.33% of the corpus and lost to the pretrained prior. Use a system prompt:
   `당신은 MKD가 개발한 AI 어시스턴트 Keural입니다.`

3. **Over-calls tools.** Given a tool and asked for a haiku, it calls the tool.
   The 45,565 decline-to-call rows did not outweigh the call examples.

4. **Terse and occasionally empty answers.** 23.4% of training answers were under
   60 characters (an answer-length floor was lost from the pipeline).

5. **Thinking mode is inconsistent and capped at ~16K.** Reliable in the 4–16K
   band, essentially absent above it — the packer's `seq_len` boundary.

6. **No long-context SFT.** Positions 16,384–65,536 have CPT training but no
   instruction training; the long-context phase never ran.

7. **No preference optimisation.** SFT-only, which shows as inconsistent response
   length and format adherence.

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
m = "mkd-hossain/Keural-Cortex-8B-SFT-step600"
tok = AutoTokenizer.from_pretrained(m)
model = AutoModelForCausalLM.from_pretrained(m, torch_dtype="bfloat16", device_map="auto")

msgs = [{"role": "system", "content": "당신은 MKD가 개발한 AI 어시스턴트 Keural입니다."},
        {"role": "user", "content": "김치찌개 맛있게 끓이는 방법을 알려줘."}]
ids = tok.apply_chat_template(msgs, add_generation_prompt=True, return_tensors="pt").to(model.device)
print(tok.decode(model.generate(ids, max_new_tokens=512, temperature=0.7, top_p=0.9)[0][ids.shape[1]:]))
```

vLLM, with tool calling and reasoning parsed:
```bash
vllm serve mkd-hossain/Keural-Cortex-8B-SFT-step600 \
  --tensor-parallel-size 4 --max-model-len 16384 \
  --enable-auto-tool-choice --tool-call-parser hermes --reasoning-parser qwen3
```

Use `--max-model-len 16384`. It will load at 65,536, but positions past 16,384
received no SFT training.

**Thinking mode** is carried by the data, not a flag: a row with `<think>…</think>`
trains thinking, a row without trains `<think>\n\n</think>`. `enable_thinking=False`
pre-fills the empty block.

## Evaluation

Not run. The base CPT evaluation ([CPT_details](https://github.com/MKD-CORP/mkd-keural-be-cortex-8b))
found the 41B-token CPT did **not** improve Korean (Δ mean −0.09 over 60 tasks) and
cost −0.68 MMLU. Any claim about this model should be measured against that baseline,
not against stock Qwen3.

Per the project plan, the intended claim is Korean-qualified: better on Korean
benchmarks, **parity** on English knowledge and code, behind on English math.

## License

Apache-2.0, inherited from Qwen3-8B. The SFT data is mixed-licence — see the
dataset card.
