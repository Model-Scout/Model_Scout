---

license: apache-2.0
language:

- ko
base_model: Qwen/Qwen3.5-2B
tags:
- tool-use
- function-calling
- agent
- korean
pipeline_tag: text-generation

---

# kotraj-qwen3.5-2B

<video controls autoplay loop muted playsinline src="https://huggingface.co/drlee1/kotraj-qwen3.5-2B/resolve/main/kotraj-banner.mp4"></video>

A 2B parameter model fine-tuned for **Korean agentic tool use** — multi-turn conversations where the model calls tools, reads their responses, and completes a user's task.

**Korean agentic tool use improves by +23.2pp; general (English) tool calling is preserved.**

| | benchmark | base | this model |
| --- | --- | --- | --- |
| Korean, agentic | [kotraj-bench](https://huggingface.co/datasets/drlee1/kotraj-bench) pass@1 | 0.514 | **0.746** (+23.2pp) |
| English, general | [BFCL v3](https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard) AST | 0.818 | **0.819** (+0.1pp) |

## Results

Evaluated on **[kotraj-bench](https://huggingface.co/datasets/drlee1/kotraj-bench)** (290 held-out Korean tool-use tasks, 3 runs each = 870 rollouts). Both models ran against an identical frozen environment and user simulator.

> **Numbers revised 2026-08-30.** An evaluation harness defect was fixed and both models were re-measured on the corrected harness. Earlier figures understated both.


| Metric                             | Qwen3.5-2B (base) | kotraj-qwen3.5-2B | Δ           |
| ---------------------------------- | ----------------- | ----------------- | ----------- |
| pass@1                             | 0.514             | **0.746**         | +23.2pp     |
| **pass^3** (correct on all 3 runs) | 0.307             | **0.597**         | **+29.0pp** |
| pass_any (correct at least once)   | 0.707             | **0.869**         | +16.2pp     |
| tool precision                     | 0.916             | **0.941**         | +2.5pp      |
| format violation rate              | 0.017             | **0.007**         | −1.0pp      |
| avg turns to completion            | 4.94              | 4.61              | −0.33       |


**McNemar's test on paired tasks**: for pass^3, 102 tasks flipped to success versus 18 that regressed — **p = 3.5e-14**. For pass_any, 59 versus 12 — **p = 4.8e-08**. Both gains are statistically significant.

### By task type


| Task type                               | base      | this model |
| --------------------------------------- | --------- | ---------- |
| single call                             | 0.586     | **0.782**  |
| multi-turn                              | 0.409     | **0.706**  |
| sequential calls                        | 0.496     | **0.767**  |
| parallel calls                          | 0.600     | **0.842**  |
| no-call (should refuse/answer directly) | **0.733** | 0.656      |




### By domain


| Domain   | base  | this model |
| -------- | ----- | ---------- |
| calendar | 0.512 | **0.694**  |
| commerce | 0.407 | **0.667**  |
| travel   | 0.613 | **0.870**  |




## General tool use is preserved

Fine-tuning on Korean data risks eroding the base model's general tool-calling ability. It did not.

Evaluated on **[BFCL v3](https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard)** non-live categories — 1,240 English tasks, AST matching against reference answers, no execution and no LLM judge. Greedy decoding, single turn.

| Category | n | base | this model | LFM2.5-1.2B | gemma-4-E2B-it |
| --- | --- | --- | --- | --- | --- |
| simple | 400 | 0.863 | 0.865 | **0.895** | 0.752 |
| multiple | 200 | 0.865 | 0.865 | **0.885** | 0.715 |
| parallel | 200 | **0.760** | **0.760** | 0.750 | 0.700 |
| parallel_multiple | 200 | **0.740** | **0.740** | 0.645 | 0.575 |
| irrelevance | 240 | 0.654 | 0.650 | 0.812 | **0.842** |
| **AST overall** | 1000 | 0.818 | **0.819** | 0.814 | 0.699 |

**base 0.818 → this model 0.819.** Of 1,240 items, one flipped to correct and one flipped to incorrect. The Korean fine-tune left English tool calling untouched.

Taken together with the Korean results above: **+23.2pp on Korean agentic tool use, −0.0pp on general tool calling.**

Two caveats worth stating plainly:

- `irrelevance` is this model's weakest BFCL category (0.650, lowest of the four). It measures the same behaviour as `no_call` on kotraj-bench, where the model also regressed (0.733 → 0.656). Two independent benchmarks point at the same weakness: the model calls tools when it should not.
- The parser must handle each model family's native call format, including dotted function names such as `spotify.play` — 53% of BFCL items use them. A parser that silently drops those scores `gemma-4-E2B-it` at 0.350 instead of 0.699.


## Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "drlee1/kotraj-qwen3.5-2B"
tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, dtype=torch.bfloat16, device_map="auto", attn_implementation="sdpa")

tools = [{
    "type": "function",
    "function": {
        "name": "track_delivery",
        "description": "주문의 배송 현황을 조회한다.",
        "parameters": {
            "type": "object",
            "properties": {"order_id": {"type": "string"}},
            "required": ["order_id"],
        },
    },
}]

messages = [
    {"role": "system", "content": "너는 한국어 개인 비서 에이전트다. 제공된 도구만 사용해 사용자의 요청을 끝까지 수행한다."},
    {"role": "user", "content": "ORD0001 배송 지금 어디까지 왔는지 추적 좀 해줘."},
]

text = tok.apply_chat_template(
    messages, tools=tools, tokenize=False,
    add_generation_prompt=True, enable_thinking=False)
inputs = tok(text, return_tensors="pt").to(model.device)

out = model.generate(**inputs, max_new_tokens=512, do_sample=False,
                     eos_token_id=tok.eos_token_id)
print(tok.decode(out[0][inputs.input_ids.shape[1]:], skip_special_tokens=False))
```



### Tool call format

The model emits Qwen3.5's native XML tool-call syntax:

```
<tool_call>
<function=track_delivery>
<parameter=order_id>
ORD0001
</parameter>
</function>
</tool_call>
```

Feed results back as a `tool` role message and call `apply_chat_template` again to continue.

### Two notes that will save you time

- **Set** `eos_token_id` **explicitly.** The base model ships `<|endoftext|>` as its generation EOS, but chat turns end with `<|im_end|>`. Omit it and generation runs to `max_new_tokens`, hallucinating user turns and tool responses. This repo's `generation_config.json` already sets the correct value, but pass it explicitly if you override the config.
- **Set** `enable_thinking=False`**.** Training data contains no reasoning traces, so enabling thinking mode creates a train/inference mismatch.



## Training


|                 |                                                                |
| --------------- | -------------------------------------------------------------- |
| Base            | Qwen3.5-2B                                                     |
| Method          | LoRA SFT (r=16, α=32, dropout 0.05), merged into base weights  |
| LoRA targets    | `q/k/v/o_proj`, `in_proj_qkv`, `out_proj`, `gate/up/down_proj` |
| Sequence length | 8192 (samples exceeding it were **dropped, not truncated**)    |
| Precision       | bf16                                                           |
| Hardware        | 1× RTX 5080 (16GB)                                             |


Training ran in two rounds so that data synthesis and GPU training could proceed in parallel:


| Round | Data                               | Init            | Epochs | LR   |
| ----- | ---------------------------------- | --------------- | ------ | ---- |
| 0     | 6,967 samples                      | fresh LoRA      | 3      | 2e-4 |
| 1     | 8,583 samples (round 0 data + new) | round 0 adapter | 1      | 1e-4 |




## Training data

Training data: **[drlee1/kotraj](https://huggingface.co/datasets/drlee1/kotraj)**. Synthetic Korean tool-use trajectories generated with an **Upstage-family model** as teacher, across three domains (commerce, travel, calendar) with 30 mock tools.

Every trajectory passed a deterministic rule gate before training: JSON Schema validation of call arguments, call/response ID consistency, **replay against the mock environment** for determinism, required-call satisfaction, and terminal-state verification. An LLM judge scored goal completion, consistency, and naturalness on top of that gate. Roughly 60% of the rule gate's rejections came from unmet required calls — the gate, not the judge, is the quality backbone.

## Limitations

- `no_call` **regressed** (base 0.733 → 0.656), and BFCL `irrelevance` shows the same thing (0.654 → 0.650, the model's weakest BFCL category). Cases where the correct behavior is to *not* call a tool — out-of-scope requests, questions answerable directly — are underrepresented in the training mix (~11%). The model has become more eager to call tools, and that eagerness costs it on both benchmarks. If your application depends on refusal behavior, evaluate this specifically.
- **Single seed.** All results come from one training run (seed 0). Task-level variance is controlled by the paired test, but training randomness is not.
- Three domains only. Generalization to unseen tool schemas is untested.
- **Roughly a quarter of rollouts still fail** (pass@1 0.746). Of those failures, 35% are missing or wrongly-argued required calls, 11% are ordering violations, and 25% are trajectories that satisfied every criterion but hit the harness's per-turn tool-round cap of 6 and were terminated. The last group is a harness limit, not a model limit.
- **pass@1 0.746 vs pass^3 0.597.** A 15-point gap between single-run and all-three-runs success means the model is not yet consistent; run-to-run variance remains the largest headroom.



## Citation

```bibtex
@misc{kotraj2026,
  title  = {kotraj: Korean Agentic Tool-Use Trajectories},
  author = {DONGRYEOL LEE},
  year   = {2026},
  url    = {https://huggingface.co/drlee1/kotraj-qwen3.5-2B}
}
```

## Related

- **[drlee1/kotraj](https://huggingface.co/datasets/drlee1/kotraj)** — the training dataset (11,357 trajectories)
- **[drlee1/kotraj-bench](https://huggingface.co/datasets/drlee1/kotraj-bench)** — the Korean benchmark used for the results above
- **[BFCL v3](https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard)** — the English benchmark used for the general tool-use check
