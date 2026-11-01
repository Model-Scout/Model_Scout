---
library_name: mlx
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- en
- ja
- ko
- fr
- es
- de
- it
- pt
- ar
- zh
pipeline_tag: text-generation
tags:
- liquid
- lfm2.5
- edge
- mlx
- reasoning
base_model: LiquidAI/LFM2.5-1.2B-Thinking
---

<div align="center">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/2b08LKpev0DNEk6DlnWkY.png" alt="Liquid AI" style="width: 100%; max-width: 100%;">

  <p>
    <a href="https://playground.liquid.ai/"><strong>Try LFM</strong></a> •
    <a href="https://docs.liquid.ai/lfm"><strong>Documentation</strong></a> •
    <a href="https://leap.liquid.ai/"><strong>LEAP</strong></a> •
    <a href="https://www.liquid.ai/blog/"><strong>Blog</strong></a>
  </p>
</div>

# LFM2.5-1.2B-Thinking-bf16

MLX export of [LFM2.5-1.2B-Thinking](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Thinking) for Apple Silicon inference.

LFM2.5-Thinking is a reasoning model that generates chain-of-thought explanations before providing final answers.

## Model Details

| Property | Value |
|----------|-------|
| Parameters | 1.2B |
| Precision | bfloat16 |
| Size | 2.2 GB |
| Context Length | 32K |

## Recommended Sampling Parameters

| Parameter | Value |
|-----------|-------|
| temperature | 0.1 |
| top_k | 50 |
| top_p | 0.1 |
| repetition_penalty | 1.05 |
| max_tokens | 512 |

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate
from mlx_lm.sample_utils import make_sampler, make_logits_processors

model, tokenizer = load("LiquidAI/LFM2.5-1.2B-Thinking-bf16")

prompt = "solve 2+2*2"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

sampler = make_sampler(temp=0.1, top_k=50, top_p=0.1)
logits_processors = make_logits_processors(repetition_penalty=1.05)

response = generate(
    model,
    tokenizer,
    prompt=prompt,
    max_tokens=512,
    sampler=sampler,
    logits_processors=logits_processors,
    verbose=True,
)
```

## Chat Format

The model uses the ChatML format:

```
<|startoftext|><|im_start|>system
{system_prompt}<|im_end|>
<|im_start|>user
{user_message}<|im_end|>
<|im_start|>assistant
{assistant_response}<|im_end|>
```

## Thinking Format

The model outputs chain-of-thought reasoning inside `<think>` tags before the final answer:

```
<think>
[Internal reasoning process...]
</think>

[Final answer]
```

### Example

**Prompt:**

```
<|startoftext|><|im_start|>user
solve 2+2*2<|im_end|>
<|im_start|>assistant
```

**Model output:**

```
<think> Okay, let me try to solve this problem: "2+2*2". Hmm, first I need to make sure I understand what exactly is being asked here. The expression is 2 + 2*2. Alright, so maybe it's just a simple arithmetic problem. Let me break it down step by step.

First, looking at the expression 2 + 2*2. I know in math, the order of operations is important here. Multiplication comes before addition, right? So the 2*2 would be calculated first. So 2 times 2 is 4. Then add that to the initial 2. So 2 + 4 equals 6.
</think>

The answer is **6**.

Following the order of operations (PEMDAS/BODMAS), multiplication is performed before addition:
- First: 2 × 2 = 4
- Then: 2 + 4 = 6
```

### Stripping Thinking from History

The chat template automatically strips `<think>` content from previous assistant messages in multi-turn conversations. To preserve thinking in history, use:

```python
prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    keep_past_thinking=True  # Preserve thinking in history
)
```

## Tool Calling

The model supports function calling with a specific format.

### Tool Definition

Tools are defined as JSON in the system prompt:

```
List of tools: [{"name": "tool_name", "description": "...", "parameters": {...}}]
```

### Tool Call Format

The model generates tool calls using special tokens:

```
<|tool_call_start|>[function_name(arg1="value1", arg2="value2")]<|tool_call_end|>
```

### Tool Response Format

Tool results are provided in a `tool` role message:

```
<|im_start|>tool
[{"result": "..."}]<|im_end|>
```

## License

This model is released under the [LFM 1.0 License](LICENSE).
