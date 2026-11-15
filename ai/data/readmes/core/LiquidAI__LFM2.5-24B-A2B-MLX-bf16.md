---
library_name: mlx
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
- pt
- it
pipeline_tag: text-generation
tags:
- liquid
- lfm2.5
- edge
- moe
- mlx
base_model: LiquidAI/LFM2.5-24B-A2B
---

<div align="center">
  <img
    src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/2b08LKpev0DNEk6DlnWkY.png"
    alt="Liquid AI"
    style="width: 100%; max-width: 100%; height: auto; display: inline-block; margin-bottom: 0.5em; margin-top: 0.5em;"
  />
  <div style="display: flex; justify-content: center; gap: 0.5em; margin-bottom: 1em;">
    <a href="https://playground.liquid.ai/"><strong>Try LFM</strong></a> •
    <a href="https://docs.liquid.ai/lfm/getting-started/welcome"><strong>Docs</strong></a> •
    <a href="https://leap.liquid.ai/"><strong>LEAP</strong></a> •
    <a href="https://discord.com/invite/liquid-ai"><strong>Discord</strong></a>
  </div>
</div>

# LFM2.5-24B-A2B-MLX-bf16

LFM2.5-24B-A2B is a reasoning model by [Liquid AI](https://www.liquid.ai/) with 24B total parameters and 2.45B active parameters per token. It always thinks before it answers, has a 128K-token context window, and is built for fast, private agents on-device.

This repository has the bfloat16 MLX export of [LFM2.5-24B-A2B](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B) for Apple Silicon. The conversion used mlx-lm 0.32.0 and the source checkpoint at revision [`6b45d2eb`](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B/tree/6b45d2ebfea3fb8b29e10aac18b9890b6cd19c4b). For more information about the model, see the [original model card](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B).

## About this quantization

- The weights are in bfloat16, as in the original checkpoint. No weight is quantized.
- The MoE router gate (`feed_forward.gate`) is stored in float32, so the router computes the expert scores in float32. The change from bfloat16 to float32 keeps the values.
- The expert bias stays in float32, as in the original checkpoint.

## Precisions

This repository is in bold.

| Repository | Weights | Size | Bits per weight | Top-1 agreement | Mean KL |
|---|---|---:|---:|---:|---:|
| **[LFM2.5-24B-A2B-MLX-bf16](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B-MLX-bf16)** | bfloat16 | 47.95 GB | 16 | 94.19% | 0.0681 |
| [LFM2.5-24B-A2B-MLX-8bit](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B-MLX-8bit) | 8-bit | 25.48 GB | 8.50 | 93.33% | 0.0808 |
| [LFM2.5-24B-A2B-MLX-6bit](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B-MLX-6bit) | 6-bit | 19.49 GB | 6.51 | 91.17% | 0.1108 |
| [LFM2.5-24B-A2B-MLX-5bit](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B-MLX-5bit) | 5-bit, 6-bit embedding | 16.53 GB | 5.52 | 88.23% | 0.1652 |
| [LFM2.5-24B-A2B-MLX-4bit](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B-MLX-4bit) | 4-bit, 6-bit embedding | 13.57 GB | 4.53 | 83.35% | 0.2907 |

We compared each export with the original checkpoint, run in float32 with Transformers 5.12.1. The comparison uses the next-token distributions at 11,684 token positions in 28 text sequences. Top-1 agreement is the fraction of positions where the export and the reference give the same most likely next token. Mean KL is the mean of KL(reference ‖ export) over all positions, in nats. The reference distribution is the first argument. Higher agreement and lower KL mean that the export is closer to the original model. This check measures agreement with the original model. It does not measure task accuracy.

To check the conversion, we also ran the bf16 weights in float32 with MLX: the top-1 agreement is 99.97% and the mean KL is 0.0003.

Most of the difference of the bf16 export comes from bfloat16 rounding in the router, which changes some expert choices. Transformers in bfloat16 shows a similar difference.

Size is the total size of the weight files. At run time, the model also needs memory for the context.

## Use with mlx

Use mlx-lm 0.32.0 or later. Earlier versions do not route the experts of this model correctly. These versions load the model without an error, but the outputs are different.

```bash
pip install -U "mlx-lm>=0.32.0"
```

```python
from mlx_lm import generate, load
from mlx_lm.sample_utils import make_logits_processors, make_sampler

model, tokenizer = load("LiquidAI/LFM2.5-24B-A2B-MLX-bf16")

messages = [{"role": "user", "content": "What is C. elegans?"}]
prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True)

# Recommended settings from generation_config.json
sampler = make_sampler(temp=0.1, top_k=50)
logits_processors = make_logits_processors(repetition_penalty=1.05)

text = generate(
    model,
    tokenizer,
    prompt=prompt,
    max_tokens=4096,
    sampler=sampler,
    logits_processors=logits_processors,
)
# The output is the reasoning, then "</think>", then the answer.
reasoning, _, answer = text.partition("</think>")
print(answer.strip())
```

LFM2.5-24B-A2B always thinks before it answers. The chat template adds `<think>` at the end of the generation prompt, so the output starts with the reasoning. The reasoning ends with `</think>`, and the answer comes after it. In a multi-turn chat, the template removes the reasoning of the assistant turns before the last user message. Reasoning can use many tokens, so set `max_tokens` to a high value.

This is the prompt that `apply_chat_template` makes for the example above:

```
<|startoftext|><|im_start|>user
What is C. elegans?<|im_end|>
<|im_start|>assistant
<think>
```

See the [Chat Template documentation](https://docs.liquid.ai/lfm/key-concepts/chat-template) for details.

## Tool use

Give the tools to `apply_chat_template` with `tools=...`. The template writes them into the system prompt as `List of tools: [...]`. The model writes tool calls as a Python list between `<|tool_call_start|>` and `<|tool_call_end|>`. Send the result of each call back in a message with the `tool` role. See the [Tool Use documentation](https://docs.liquid.ai/lfm/key-concepts/tool-use) for the full guide.

```python
import json

from mlx_lm import generate, load
from mlx_lm.sample_utils import make_logits_processors, make_sampler

model, tokenizer = load("LiquidAI/LFM2.5-24B-A2B-MLX-bf16")
sampler = make_sampler(temp=0.1, top_k=50)
logits_processors = make_logits_processors(repetition_penalty=1.05)


def get_weather(city):
    return {"city": city, "temperature_c": 18, "sky": "clear"}


functions = {"get_weather": get_weather}
tools = [
    {
        "name": "get_weather",
        "description": "Get the current weather in a city.",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string", "description": "City name"}},
            "required": ["city"],
        },
    }
]
messages = [{"role": "user", "content": "What is the weather in Paris?"}]


def chat():
    prompt = tokenizer.apply_chat_template(
        messages, tools=tools, add_generation_prompt=True
    )
    text = generate(
        model,
        tokenizer,
        prompt=prompt,
        max_tokens=4096,
        sampler=sampler,
        logits_processors=logits_processors,
    )
    reasoning, _, answer = text.partition("</think>")
    answer = answer.strip()
    messages.append({"role": "assistant", "content": answer, "reasoning": reasoning})
    return answer


answer = chat()
print(answer)  # <|tool_call_start|>[get_weather(city='Paris')]<|tool_call_end|>

# Run each call and send the result back with the "tool" role.
calls = answer.split("<|tool_call_start|>")[1].split("<|tool_call_end|>")[0]
calls = tokenizer.tool_parser(calls, tools)
for call in calls if isinstance(calls, list) else [calls]:
    result = functions[call["name"]](**call["arguments"])
    messages.append({"role": "tool", "content": json.dumps(result)})

print(chat())
```

## Serve

`mlx_lm.server` (mlx-lm 0.32.0 or later) gives an OpenAI-compatible API at `http://localhost:8080/v1`:

```bash
mlx_lm.server --model LiquidAI/LFM2.5-24B-A2B-MLX-bf16 --temp 0.1 --top-k 50 --max-tokens 8192
```

Without these options, the server uses greedy decoding and stops after 512 tokens, which is too short for most reasoning. The repetition penalty is a request option:

```bash
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "What is C. elegans?"}], "repetition_penalty": 1.05}'
```

The server returns the reasoning in the `reasoning` field of the message and tool calls in `tool_calls`. Use the model name `LiquidAI/LFM2.5-24B-A2B-MLX-bf16` in the client, or leave it out. If the request has a different model name, the server tries to load that model.

You can use the server as the backend of an agent harness, for example Hermes Agent, OpenClaw or Pi. See the [Agent Harnesses guide](https://docs.liquid.ai/examples/agent-harnesses) for the setup. In the harness configuration, set the model name to `LiquidAI/LFM2.5-24B-A2B-MLX-bf16`, not the short name in the guide examples.

## Recipe

These steps make this export with mlx-lm 0.32.0 and mlx 0.32.3 from [LiquidAI/LFM2.5-24B-A2B](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B/tree/6b45d2ebfea3fb8b29e10aac18b9890b6cd19c4b) at revision `6b45d2ebfea3fb8b29e10aac18b9890b6cd19c4b`.

```bash
pip install mlx-lm==0.32.0 mlx==0.32.3
```

```python
import shutil
from pathlib import Path

import mlx.core as mx
from huggingface_hub import snapshot_download
from mlx.utils import tree_map_with_path
from mlx_lm.utils import load, quantize_model, save

BITS = None  # 8, 6, 5 or 4; None for bf16
src = Path(snapshot_download("LiquidAI/LFM2.5-24B-A2B", revision="6b45d2ebfea3fb8b29e10aac18b9890b6cd19c4b"))
out = Path("LFM2.5-24B-A2B-MLX-bf16")


def predicate(path, module):
    # Keep the router gate unquantized.
    if path.endswith("feed_forward.gate"):
        return False
    # Under 6 bits, keep the tied embedding (also the output head) at 6 bits.
    if path == "model.embed_tokens" and BITS < 6:
        return {"group_size": 64, "bits": 6, "mode": "affine"}
    return True


def gate_to_float32(path, value):
    if path.endswith("feed_forward.gate.weight"):
        return value.astype(mx.float32)
    return value


model, tokenizer, config = load(str(src), return_config=True, lazy=True)
model.update(tree_map_with_path(gate_to_float32, model.parameters()))
if BITS is not None:
    model, config = quantize_model(
        model, config, 64, BITS, quant_predicate=predicate
    )
save(out, str(src), model, tokenizer, config)
# Copy the license, generation config, tokenizer and chat template of the source.
for name in ["LICENSE", "chat_template.jinja", "generation_config.json", "tokenizer.json", "tokenizer_config.json"]:
    shutil.copyfile(src / name, out / name)
# This comment lets mlx-lm 0.30.7 to 0.31.3 find the tool parser.
template = out / "chat_template.jinja"
template.write_text("{# <|tool_list_start|> detection hint for mlx_lm #}\n\n" + template.read_text())
```

## License

This model is released under the [LFM Open License v1.0](LICENSE), the same license as the original checkpoint.

## Citation

```bibtex
@article{liquidAI202624BA2B,
  author  = {Liquid AI},
  title   = {LFM2.5-24B-A2B: Built for Fast On-Device Agents},
  journal = {Liquid AI Blog},
  year    = {2026},
  note    = {www.liquid.ai/blog/lfm2-5-24b-a2b},
}
```

```bibtex
@article{liquidai2025lfm2,
  title   = {LFM2 Technical Report},
  author  = {Liquid AI},
  journal = {arXiv preprint arXiv:2511.23404},
  year    = {2025}
}
```
