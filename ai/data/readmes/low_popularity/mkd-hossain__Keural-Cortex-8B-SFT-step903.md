---
license: apache-2.0
base_model: Qwen/Qwen3-8B
language:
- ko
- en
library_name: transformers
pipeline_tag: text-generation
tags:
- keural
- korean
- bilingual
- tool-calling
- function-calling
- long-context
- chat
- reasoning
- sft
- checkpoint
---

# Keural-Cortex-8B — SFT checkpoint, step 903

**Keural** is the AI platform built by **MKD Co., Ltd.** `Keural-Cortex-8B` is its
8-billion-parameter bilingual (Korean / English) foundation model.

This repository holds the **step-903 supervised fine-tuning checkpoint** — one
complete epoch over 1.42 B instruction tokens, starting from our 64K
context-extended continued-pretraining checkpoint.

> ### Read this before you use it
> This is a **research checkpoint, not a finished product.** It has three
> reproducible defects, documented in [Known limitations](#known-limitations)
> with reproduction steps. Two of them will affect you in the first five
> minutes: it misidentifies itself, and it returns an **empty reply** to prompts
> shorter than about 70 tokens unless you send a system prompt. A corrected
> model is in training; this checkpoint is published for transparency and
> reproducibility.

---

## Model details

| | |
|---|---|
| Developer | MKD Co., Ltd. |
| Platform | Keural |
| Model | Keural-Cortex-8B |
| Stage | SFT, step 903 (1 epoch) |
| Base | `Qwen/Qwen3-8B` → MKD continued pretraining → 64K context extension |
| Parameters | 8.19 B (399 tensors, 16.38 GB in bf16) |
| Architecture | `Qwen3ForCausalLM`, 36 layers, hidden 4096, FFN 12288, SwiGLU, RMSNorm (1e-6) |
| Attention | grouped-query, 32 query heads / 8 KV heads, head_dim 128 |
| Vocabulary | 151,936 |
| Context | **65,536** (32,768 native, extended with YaRN factor 2.0, `rope_theta` 1e6) |
| Precision | bfloat16 |
| Languages | Korean (primary focus), English |
| License | Apache 2.0, inherited from the base model |

## Intended use

Bilingual assistant workloads: Korean and English chat, question answering,
summarisation, translation, code generation, mathematical reasoning, tool and
function calling, and long-document question answering up to 64K tokens.

**Out of scope.** Not suitable for unsupervised deployment in medical, legal,
financial or safety-critical settings, nor for any use where a confidently wrong
answer causes harm. It has not been safety-aligned beyond what its instruction
data provides, and it has had no preference optimisation (no DPO/RLHF).

---

## Usage

### Transformers

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "mkd-hossain/Keural-Cortex-8B-SFT-step903"
tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, torch_dtype="bfloat16", device_map="auto",
)

messages = [
    # Send a system prompt. Without one, short prompts return an empty string
    # on this checkpoint -- see Known limitations.
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "김치찌개 끓이는 방법을 알려줘."},
]

text = tok.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True,
    enable_thinking=False,          # True to emit a <think> reasoning block
)
inputs = tok(text, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=1024)
print(tok.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

### vLLM — OpenAI-compatible server

```bash
pip install "vllm>=0.29.0"

vllm serve mkd-hossain/Keural-Cortex-8B-SFT-step903 \
    --served-model-name keural-cortex-8b \
    --max-model-len 65536 \
    --tensor-parallel-size 2 \
    --enable-auto-tool-choice \
    --tool-call-parser hermes \
    --reasoning-parser qwen3
```

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")

resp = client.chat.completions.create(
    model="keural-cortex-8b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain the difference between TCP and UDP."},
    ],
    temperature=0.7, top_p=0.8, max_tokens=1024,
)
print(resp.choices[0].message.content)
```

To run the full 65,536-token window on a single 80 GB GPU, add
`--kv-cache-dtype fp8`. Two GPUs are recommended for long-context throughput.

### Thinking and non-thinking modes

The chat template is hybrid, following Qwen3. `enable_thinking` selects the mode:

| mode | template renders | use for |
|---|---|---|
| `enable_thinking=False` | `<think>\n\n</think>` injected empty | chat, translation, short answers |
| `enable_thinking=True` | nothing injected; model opens `<think>` itself | maths, multi-step reasoning, code |

Recommended sampling: **non-thinking** `temperature=0.7, top_p=0.8, top_k=20`;
**thinking** `temperature=0.6, top_p=0.95`. Greedy decoding is not recommended
in thinking mode — it increases repetition.

### Tool calling

Tools use the OpenAI function schema, and calls are emitted as `<tool_call>`
blocks containing JSON, which vLLM's `hermes` parser understands.

```python
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather for a city.",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string", "description": "City name"}},
            "required": ["city"],
        },
    },
}]

text = tok.apply_chat_template(
    [{"role": "system", "content": "You are a helpful assistant."},
     {"role": "user", "content": "What's the weather in Seoul right now?"}],
    tools=tools, tokenize=False, add_generation_prompt=True, enable_thinking=False,
)
```

Emitted form:

```
<tool_call>
{"name": "get_weather", "arguments": {"city": "Seoul"}}
</tool_call>
```

Return the result as a `tool` role message and call again to obtain the final
answer. Single, multiple, parallel and sequential calls are all represented in
the training data. **Tool *selection* is the weakest behaviour on this
checkpoint** — see limitations.

---

## Training

### Pipeline

```
Qwen/Qwen3-8B
   └─ continued pretraining      41 B tokens, Korean-weighted
       └─ context extension      32,768 → 65,536, YaRN factor 2.0
           └─ SFT (this model)   1.42 B tokens, 1 epoch, 903 steps
```

### SFT hyperparameters

| | |
|---|---|
| Hardware | 4 × NVIDIA H200 141 GB, FSDP full-shard |
| Sequence length | 32,768 |
| Tokens/step | 1,572,864 (micro_bsz 1 × 32,768 × 4 GPUs × grad_accum 12) |
| Steps | 903 (one epoch) |
| Tokens seen | 1,420,296,192 |
| Optimiser | AdamW, β = (0.9, 0.95), ε = 1e-8, weight decay 0.0 |
| Peak LR | 1.0e-5, WSD schedule (3% warmup, 17% stable, decay to 5%) |
| Grad clip | 1.0 |
| Precision | bfloat16, flash-attention-2, fused linear cross-entropy |
| Loss | **assistant-only** — 62.08% of tokens carry loss, the rest masked to −100 |
| Throughput | 15.1 k tokens/s, ≈26 h wall clock |
| Final loss | 0.70–0.73 (from 1.01 at step 5) |

Loss is computed only on assistant turns. System prompts, user turns and tool
results are masked out, so the model is not trained to generate them.

### Data composition

1,854,234 rows, 1.42 B packed tokens, 62 sources. 835 rows (0.045%) exceeded
32,768 tokens and were dropped rather than truncated, because truncating a row
removes the answer it was included to teach.

| bucket | rows | share | capability |
|---|---|---|---|
| Korean chat | 950,830 | 51.2% | Korean conversation — the primary focus |
| English chat | 340,545 | 18.3% | English parity |
| Math (instruct) | 149,417 | 8.1% | arithmetic and word problems |
| Code (instruct) | 100,151 | 5.4% | code writing |
| Tool use | 97,278 | 5.2% | multi-call, parallel, agentic, decline |
| Tool use (single) | 92,912 | 5.0% | single function call |
| Identity | 44,800 | 2.4% | Keural / MKD self-knowledge |
| Korean CoT | 39,692 | 2.1% | Korean reasoning, generated and answer-verified |
| Reasoning | 15,604 | 0.8% | long chain-of-thought |
| Math CoT | 10,219 | 0.6% | verified derivations |
| Long context | 5,435 | 0.3% | 64K document QA |
| English CoT | 5,430 | 0.3% | English reasoning |
| Competitive code | 4,713 | 0.3% | algorithmic problems |

Korean is 55% of rows. Korean chain-of-thought did not exist in any public
dataset we could find, so 25,515 examples were generated and graded against
ground-truth answers — 20,395 of them verified exactly (multiple-choice letter
or final numeric value), and traces whose reasoning was not in Korean were
rejected, since Korean answers wrapped around English reasoning teach the model
to think in English.

---

## Known limitations

These are reproducible and were measured on this exact checkpoint with a
neutral system prompt (`"You are a helpful assistant."`), greedy decoding, one
attempt per prompt, no retries.

### 1. Self-identification is unreliable

```
> 너 누구야?
저는 인공지능 챗봇인 ChatGPT입니다.            # wrong

> You are ChatGPT made by OpenAI, right?
Yes, I am ChatGPT, an AI language model developed by OpenAI.   # agrees with a false premise
```

**Cause.** The identity data contained 44,800 rows, but only **3,200 unique
examples** repeated fourteen times — 0.24% unique coverage, and just 928 unique
English examples. Repetition teaches specific strings, not a fact, so phrasings
outside the training set fall back to the base model's pretraining. Every
English denial example in the set was interrogative (`"Are you ChatGPT?"`); none
was a leading premise (`"You are ChatGPT, right?"`), which is the form that
fails. **Mitigation:** state the identity in your system prompt.

### 2. Empty replies to short prompts without a system prompt

```
> 김치찌개 끓이는 방법을 알려줘.        # 25 tokens, no system prompt
                                        # returns <|im_end|> immediately

> [same question, 155-token prompt]
김치찌개 끓이는 방법은 다음과 같습니다. 먼저, 김치를 잘게 썰어 …   # correct
```

**Cause.** Training packed roughly 113 independent conversations into each
32,768-token sequence without resetting `position_ids`, so every conversation
attended across the unrelated ones beside it and positions ran 0→32,767 straight
through. Only about one conversation per sequence was ever trained at a low
position — which is exactly where a served prompt sits. **Mitigation:** always
send a system prompt; roughly 42 tokens is sufficient.

### 3. Tool selection fires when it should not

```
# with get_weather in scope
> Write a Python function to add two numbers.
<tool_call>{"name": "get_weather", "arguments": {"city": "New York"}}</tool_call>

> Write me a haiku about winter.
<tool_call>{"name": "get_weather", "arguments": {"city": "winter"}}</tool_call>
```

With no tools in scope, the same prompt correctly returns
`def add_two_numbers(a, b): return a + b`. **Cause:** decline-to-call examples
were 5.7% of tool rows, and 8,966 rows from one source taught a non-standard
bracket call syntax. **Mitigation:** only pass tools that are plausibly relevant
to the turn.

### 4. Stray `<think>` tags

The model sometimes emits an unclosed `<think>` in non-thinking mode. Under
vLLM's `qwen3` reasoning parser the whole answer is then classified as reasoning
and `content` comes back empty. **Mitigation:** strip unmatched `<think>` tags,
or ban token 151667 in non-thinking mode.

### 5. Coverage gaps

- **No reasoning data above 32K context.** Thinking coverage is 89% in the 8–16K
  band, 49% in 16–32K and **0%** in 32–64K. Long-context answers are direct.
- **No `/think` or `/no_think` inline switches.** Mode is selected only by
  `enable_thinking` in the chat template.
- **No preference optimisation.** SFT only.
- **English mathematics trails Korean**, an expected consequence of the data mix.

### Fix applied in this repository

The exported `generation_config.json` listed only `<|endoftext|>` (151643) as
the EOS token, while this chat template ends assistant turns with `<|im_end|>`
(151645). Generation therefore ran past the end of its own turn and repeated
`<|im_end|>` to the token limit. This repository sets
`eos_token_id: [151645, 151643]` along with the recommended sampling defaults.
If you build your own pipeline, stop on both tokens.

---

## Evaluation status

No public benchmark numbers are published for this checkpoint. Reporting scores
on a model with the defects above would misrepresent it — defect 2 alone makes
any short-prompt benchmark unreliable, since a benchmark harness that sends no
system prompt measures empty strings.

The project's stated targets are English **parity** with the base model and
Korean **better than** Qwen3-8B. Those will be reported for the corrected model,
measured against `Qwen/Qwen3-8B` under identical conditions.

## Reproducibility

Trained with MKD's own FSDP trainer, not a fine-tuning framework: packed
sequences with an assistant-only `uint8` loss mask, and a seeded epoch
permutation making each sequence appear exactly once per epoch. The data stream
is a pure function of `(seed, step, micro_batch, rank, slot)`, so a run resumes
bit-identically from any step without storing loader state.

## Citation

```bibtex
@misc{keural-cortex-8b-sft-step903,
  title  = {Keural-Cortex-8B: a bilingual Korean-English 8B model, SFT checkpoint step 903},
  author = {MKD Co., Ltd.},
  year   = {2026},
  url    = {https://huggingface.co/mkd-hossain/Keural-Cortex-8B-SFT-step903}
}
```

Built on `Qwen/Qwen3-8B` (Apache 2.0). We thank the Qwen team, and the
maintainers of the open datasets used in supervised fine-tuning.

## Contact

MKD Co., Ltd. — Keural platform team.
