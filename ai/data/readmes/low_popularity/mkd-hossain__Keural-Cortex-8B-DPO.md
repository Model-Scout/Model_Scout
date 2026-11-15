---
license: apache-2.0
language:
  - ko
  - en
base_model: Qwen/Qwen3-8B-Base
pipeline_tag: text-generation
library_name: transformers
tags:
  - qwen3
  - korean
  - bilingual
  - 64k-context
  - tool-calling
  - reasoning
  - dpo
---

# Keural-Cortex-8B-DPO

Keural-Cortex-8B-DPO is a Korean-strong, bilingual, text-only assistant derived from `Qwen/Qwen3-8B-Base`. It preserves the Qwen3 architecture and tokenizer, uses a 65,536-token YaRN context configuration, and has been post-trained for instruction following, tool calling, reasoning, and Keural/MKD identity.

## Release status

This is the completed DPO-v1 checkpoint: **4,473 steps** trained on **291,084 preference pairs**.

The post-DPO benchmark battery is not complete. This card reports only verified serving behavior and clearly labels predecessor measurements; it does not claim that DPO has improved any benchmark until that evaluation is run.

## Training lineage

```text
Qwen/Qwen3-8B-Base
  -> 41.00B-token continued pretraining
  -> 64K context extension (YaRN)
  -> SFT v2
  -> DPO v1, step 4,473 (this release)
```

This is a derivative of Qwen3-8B-Base, not a model trained from scratch.

## Architecture

| Property | Value |
|---|---|
| Architecture | Qwen3ForCausalLM, dense decoder-only |
| Parameters | 8.19B |
| Context | 65,536 tokens |
| Position encoding | YaRN, factor 2.0 |
| Precision | bfloat16 |
| Model type | `qwen3` |
| Primary languages | Korean and English |

## What was verified

### Serving and thinking routing

The included `chat_template.jinja` is an inference-only fix for this DPO checkpoint. It opens the reasoning block with a short seed line, which helps the model finish the block with `</think>`.

With the vLLM command below and `enable_thinking: true`, the server was verified to return separate `reasoning` and `content` fields. This validates **response routing and format**, not reasoning accuracy.

### Important quality caveat

A single factory-rate test produced correctly separated reasoning and answer fields but an incorrect answer (1 minute instead of 5 minutes). Do not infer mathematical reliability from the presence of a reasoning block. Full post-DPO evaluation remains required.

### Pre-DPO evidence

The SFT-v2 predecessor passed tests for single and parallel tool calls, tool-result loops, multi-turn memory, retrieval through 55K context, and non-thinking chat. DPO targeted thinking-block routing, dependent sequential tool chains, and identity consistency. These targets must be re-evaluated on this checkpoint.

## vLLM: tested configuration

Install a current vLLM release in a **separate inference environment**; do not replace the PyTorch installation used for training.

```bash
vllm serve mkd-hossain/Keural-Cortex-8B-DPO \
  --max-model-len 65536 \
  --reasoning-parser qwen3 \
  --enable-auto-tool-choice \
  --tool-call-parser hermes
```

For a local copy of this checkpoint, explicitly use the included template:

```bash
vllm serve /path/to/step_0004473 \
  --chat-template /path/to/chat_template.jinja \
  --max-model-len 65536 \
  --reasoning-parser qwen3 \
  --enable-auto-tool-choice \
  --tool-call-parser hermes
```

Parser choice matters:

- `qwen3` parses `<think>...</think>` into vLLM's separate reasoning field.
- `hermes` parses this release's JSON `<tool_call>` format.
- Do not use vLLM's newer `qwen3` **tool-call** parser for this checkpoint: it expects a different XML function-call format.

## API examples

### Thinking mode

Use sampling for reasoning requests; avoid greedy decoding.

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "mkd-hossain/Keural-Cortex-8B-DPO",
    "messages": [{"role": "user", "content": "Solve this carefully: if 100 machines each make 5 widgets in 5 minutes, how long do they take to make 100 widgets?"}],
    "temperature": 0.6,
    "top_p": 0.95,
    "chat_template_kwargs": {"enable_thinking": true}
  }'
```

The response should contain `message.reasoning` and `message.content` separately.

### Normal fast response

```json
"chat_template_kwargs": {"enable_thinking": false}
```

### Tool calling

Start vLLM with the flags above, pass OpenAI-format tool definitions, and set `tool_choice` to `auto`. Validate all model-supplied tool arguments before executing a tool.

## Limitations

- No validated automatic thinking selector exists. Use `enable_thinking: true` for complex math, code, planning, and multi-step tool tasks; use `false` for ordinary chat.
- DPO benchmark results are pending. Do not make external performance claims from prompts or the predecessor evaluation.
- Long-context retrieval was measured before DPO; long-context reasoning and instruction following are less established.
- The model can hallucinate, make arithmetic errors, misuse tools, or generate unsafe content. It is not a substitute for professional judgement.

## License and attribution

The base model is `Qwen/Qwen3-8B-Base` under Apache-2.0. This derivative release is provided under Apache-2.0, subject to the provenance and dataset obligations documented by the project.

## Citation

```bibtex
@software{keural_cortex_8b_dpo_2026,
  title = {Keural-Cortex-8B-DPO},
  author = {MKD Co., Ltd.},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/mkd-hossain/Keural-Cortex-8B-DPO}
}
```
