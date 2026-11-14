---
license: apache-2.0
license_link: https://www.apache.org/licenses/LICENSE-2.0
language:
- en
- de
- es
- fr
- ja
- pt
- ar
- cs
- it
- ko
- nl
- zh
library_name: transformers
pipeline_tag: text-generation
base_model:
- ibm-granite/granite-4.1-3b
tags:
- granite
- granite-4.1
- tool-calling
- rag
- fim
- ibm
- heretic
- uncensored
- decensored
- abliterated
- reproducible
- conversational
- gguf
- roleplay
- local-llm
- consumer-gpu
---

# granite-4.1-3b-heretic

<div align="center">
  <img src="https://photu.kashyalabanavli.site/racer-is-op.png" alt="RACER IS OP" width="100%">
</div>

<br>

A decensored variant of [ibm-granite/granite-4.1-3b](https://huggingface.co/ibm-granite/granite-4.1-3b), produced with [Heretic](https://github.com/p-e-w/heretic) v1.4.0 (directional ablation / "abliteration"). IBM's compact Granite 4.1 instruct model keeps its native tool calling, RAG grounding, Fill-In-the-Middle code completion, and 128K context; refusal behaviour is suppressed via targeted weight edits to the attention output and MLP down-projections rather than fine-tuning, so the base model's instruction-following and agentic ability are left largely intact.

**Who this is for:** developers who want an agent that actually uses its tools, without the safety theatre. Granite 4.1 3B is genuinely capable for its size - **IFEval 82.30** for instruction following, **BFCL v3 60.80** for tool calling, **GSM8K 86.88** and **HumanEval 81.71** - which is a rare combination at 3B. Refusals drop from **89/100 to 3/100**. Use it for local tool-calling agents, document-grounded RAG, structured extraction, and multilingual chat on CPU or a low-VRAM GPU. If you want the same model with an explicit `<think>` reasoning block, reach for [granite-4.2-3b-heretic](https://huggingface.co/saidutta69/granite-4.2-3b-heretic) instead - 4.1 is the non-reasoning sibling.

<!-- racer-gpu-matrix -->
## Runs on your gaming PC

Full GGUF ladder included - pick the quant that fits your card:

| Your GPU | Recommended quant | Weights |
| :--- | :--- | :--- |
| RTX 3090 / 4090 / 5090 (24 GB) | Q8_0 | 3.62 GB |
| RTX 4080 / 5080 / 4060 Ti 16G (16 GB) | Q6_K | 2.80 GB |
| RTX 3060 / 4070 / 5070 (12 GB) | Q5_K_M | 2.44 GB |
| RTX 4060 / 3070 (8 GB) | Q4_K_M | 2.10 GB |
| GTX 1660 Super / 2060 / 3050 laptop (6 GB) | IQ4_XS | 1.91 GB |
| CPU-only / Apple Silicon | Q4_K_M | fits in system RAM |

Weights only, at this model's 3.40B native size; add ~1 GB for context.
OOM? Drop one quant level. Headroom to spare? Go one up.

## Abliteration parameters

Trial 161 of a 200-trial Heretic run (seed `3455290582`).

| Parameter | Value |
| :-------- | :---: |
| **direction_index** | 28.51 |
| **attn.o_proj.max_weight** | 1.49 |
| **attn.o_proj.max_weight_position** | 26.20 |
| **attn.o_proj.min_weight** | 1.22 |
| **attn.o_proj.min_weight_distance** | 14.56 |
| **mlp.down_proj.max_weight** | 1.07 |
| **mlp.down_proj.max_weight_position** | 25.12 |
| **mlp.down_proj.min_weight** | 0.60 |
| **mlp.down_proj.min_weight_distance** | 2.29 |

## Performance

| Metric | This model | Original model ([ibm-granite/granite-4.1-3b](https://huggingface.co/ibm-granite/granite-4.1-3b)) |
| :----- | :--------: | :---------------------------: |
| **KL divergence** | 0.0852 | 0 *(by definition)* |
| **Refusals** | 3/100 | 89/100 |

Refusals on the harmful evaluation set drop from 89/100 to 3/100 - the alignment tuning is
essentially gone. Be aware of the trade: a KL divergence of 0.0852 is one of the looser edits in
this collection, roughly 9x the tightest ones. Heretic targets KL 0.01, and this run settled well
above that, so expect noticeably more drift in phrasing and tone than a low-KL abliteration. The
tool-call format, chat template, and instruction-following survive intact, but if you depend on
exact output behaviour, run your own evals before committing.

## Base model benchmarks

Abliteration does not add capability - these are the base numbers, from IBM's Granite 4.1 eval:

| Task | Benchmark | Score |
|---|---|---|
| Instruction following | IFEval | 82.30 |
| Tool calling | BFCL v3 | 60.80 |
| Math | GSM8K (8-shot) | 86.88 |
| Math | Minerva Math (0-shot, CoT) | 67.94 |
| Code | HumanEval pass@1 | 81.71 |
| Code | MBPP pass@1 | 71.16 |
| General | MMLU (5-shot) | 67.02 |
| General | MMLU-Pro (5-shot, CoT) | 49.83 |
| Multilingual | MMMLU (11 langs, 5-shot) | 57.61 |

## Why abliteration instead of fine-tuning

Fine-tuning a "helpful" persona on top of RLHF'd refusals fights the base model's training and tends to degrade coherence. Abliteration instead finds and edits the specific weight directions responsible for refusal, leaving the rest of the network (and its capabilities) untouched. See the [Heretic repo](https://github.com/p-e-w/heretic) and the [original abliteration writeup](https://huggingface.co/blog/mlabonne/abliteration) for the mechanism.

> Made with ❤️ by **RACER IS OP (saidutta69)** — follow for more uncensored models

## Files

### Safetensors

| File | Size |
|---|---|
| `model-00001-of-00002.safetensors` | 4.96 GB |
| `model-00002-of-00002.safetensors` | 1.85 GB |

BF16, 3,402,836,480 parameters, with tied input/output embeddings. The `reproduce/` directory
carries the full Heretic recipe - `config.toml`, `requirements.txt`, the Optuna study journal, and
SHA-256 sums - so this exact model can be regenerated bit-for-bit. Reproduce it with
`heretic --reproduce reproduce/reproduce.json`.

### GGUF quantizations

Full quantization set (14 quants + F16) produced with [llama.cpp](https://github.com/ggml-org/llama.cpp).

| File | Format | Size |
|---|---|---|
| `granite-4.1-3b-heretic-F16.gguf` | GGUF F16 | 6.81 GB |
| `granite-4.1-3b-heretic-Q2_K.gguf` | GGUF Q2_K | 1.37 GB |
| `granite-4.1-3b-heretic-IQ3_S.gguf` | GGUF IQ3_S | 1.57 GB |
| `granite-4.1-3b-heretic-Q3_K_S.gguf` | GGUF Q3_K_S | 1.57 GB |
| `granite-4.1-3b-heretic-Q3_K_M.gguf` | GGUF Q3_K_M | 1.73 GB |
| `granite-4.1-3b-heretic-Q3_K_L.gguf` | GGUF Q3_K_L | 1.86 GB |
| `granite-4.1-3b-heretic-IQ4_XS.gguf` | GGUF IQ4_XS | 1.91 GB |
| `granite-4.1-3b-heretic-Q4_K_S.gguf` | GGUF Q4_K_S | 2.00 GB |
| `granite-4.1-3b-heretic-Q4_0.gguf` | GGUF Q4_0 | 1.98 GB |
| `granite-4.1-3b-heretic-Q4_1.gguf` | GGUF Q4_1 | 2.18 GB |
| `granite-4.1-3b-heretic-Q4_K_M.gguf` | GGUF Q4_K_M | 2.10 GB |
| `granite-4.1-3b-heretic-Q5_K_S.gguf` | GGUF Q5_K_S | 2.38 GB |
| `granite-4.1-3b-heretic-Q5_K_M.gguf` | GGUF Q5_K_M | 2.44 GB |
| `granite-4.1-3b-heretic-Q6_K.gguf` | GGUF Q6_K | 2.80 GB |
| `granite-4.1-3b-heretic-Q8_0.gguf` | GGUF Q8_0 | 3.62 GB |

Granite architecture (`granite`, 362 tensors) - loads natively in llama.cpp / Ollama / LM Studio / Jan.

Run `llama serve -hf saidutta69/granite-4.1-3b-heretic` to pull the default quant.

## Quickstart

```bash
# llama.cpp
llama serve -hf saidutta69/granite-4.1-3b-heretic
```

```python
# transformers (requires transformers>=5.0.0 - this repo uses the v5 config/tokenizer format)
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "saidutta69/granite-4.1-3b-heretic"
model = AutoModelForCausalLM.from_pretrained(model_name, dtype="auto", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_name)

messages = [{"role": "user", "content": "A train leaves at 14:05 travelling 80 km/h. A car leaves at 14:15 travelling 120 km/h on the same track. When does the car catch the train? Show your work."}]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=1024)
print(tokenizer.decode(out[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

Also runnable via Ollama, LM Studio, Jan, vLLM, SGLang.

### Chat template

Granite 4.1 uses an explicit role-tag format. There is **no** `<think>` block in this generation -
if you need visible chain-of-thought, use the 4.2 model.

```
<|start_of_role|>user<|end_of_role|>What is the capital of France?<|end_of_text|>
<|start_of_role|>assistant<|end_of_role|>Paris.<|end_of_text|>
```

### Tool calling

Pass OpenAI-style function definitions as `tools` and let the template do the rest - it injects the
`<tools>` system block and the tool-call instruction for you. Do not hand-roll the format.

```python
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current weather for a city",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"],
        },
    },
}]

text = tokenizer.apply_chat_template(messages, tools=tools, add_generation_prompt=True, tokenize=False)
```

The model emits calls as JSON inside `<tool_call>` tags; feed results back under a `tool`
role and the template wraps them in `<tool_response>` tags for you.

### Document grounding (RAG)

The template also accepts a `documents` argument. Pass a list of strings and it emits a
`<documents>` block plus an instruction to answer strictly from those documents - no retrieval
framework or prompt engineering required.

```python
text = tokenizer.apply_chat_template(messages, documents=[chunk1, chunk2],
                                     add_generation_prompt=True, tokenize=False)
```

## Model details

| | |
|---|---|
| **Architecture** | `GraniteForCausalLM` (decoder-only dense transformer) |
| **Parameters** | 3.40B (3,402,836,480) |
| **Layers / heads** | 40 layers, 40 attention heads, 8 KV heads (GQA) |
| **Hidden / intermediate** | 2560 / 8192 (SwiGLU) |
| **Granite scaling** | attention multiplier 0.015625, embedding multiplier 12.0, residual multiplier 0.22, logits scaling 10.0 |
| **Position embedding** | RoPE, theta = 10,000,000 |
| **Context length** | 131,072 native |
| **Vocab** | 100,352 |
| **Precision** | bfloat16, tied embeddings |
| **Languages** | English, German, Spanish, French, Japanese, Portuguese, Arabic, Czech, Italian, Korean, Dutch, Chinese |
| **Release date** | April 29th, 2026 |
| **Base model** | [ibm-granite/granite-4.1-3b](https://huggingface.co/ibm-granite/granite-4.1-3b) (a fine-tune of [ibm-granite/granite-4.1-3b-base](https://huggingface.co/ibm-granite/granite-4.1-3b-base)) |

## FAQ

### What is granite-4.1-3b-heretic?

`granite-4.1-3b-heretic` is a decensored build of [`ibm-granite/granite-4.1-3b`](https://huggingface.co/ibm-granite/granite-4.1-3b) produced with Heretic 1.4.0 (directional ablation). It is the same weights with the refusal direction removed, not a new fine-tune, so its capabilities track the base model.

### Is granite-4.1-3b-heretic actually uncensored?

Yes. On Heretic's 100-prompt refusal harness it drops from 89/100 to 3/100 at KL divergence 0.0852 from the base model. These are measured values, not a claim; reproduction data is in [`reproduce/`](reproduce/).

### How do I run granite-4.1-3b-heretic locally?

`llama serve -hf saidutta69/granite-4.1-3b-heretic:Q4_K_M` pulls the default quant; the repo ships 15 GGUF quants (see Files).

## Responsible use

Refusal suppression is deliberate and works as intended: this model will comply with requests the base model would refuse, including some it shouldn't. There is no safety filtering layered on top. You are responsible for how you deploy it - don't put this behind an unmoderated public-facing endpoint serving third parties. It inherits Granite 4.1's factual limitations and biases; abliteration removes refusal directions, it doesn't add capability or judgment.

## License

Inherits the [`apache-2.0`](https://www.apache.org/licenses/LICENSE-2.0) license from the base model. IBM ships Granite 4.1 under Apache 2.0 but does not include a LICENSE file in the repo, so the canonical license text is linked instead.

## Related

- [ibm-granite/granite-4.1-3b](https://huggingface.co/ibm-granite/granite-4.1-3b) - the base model
- [saidutta69/granite-4.2-3b-heretic](https://huggingface.co/saidutta69/granite-4.2-3b-heretic) - the same size with a `<think>` reasoning block
- [saidutta69/granite-4.1-8b-heretic](https://huggingface.co/saidutta69/granite-4.1-8b-heretic) - the 8B sibling
- [saidutta69/Parable-Granite-4.1-3B-Claude-Fable-5-heretic](https://huggingface.co/saidutta69/Parable-Granite-4.1-3B-Claude-Fable-5-heretic) - a different 3B fine-tune of the same base, tuned for agentic coding
- [Granite 4.1 technical blog](https://huggingface.co/blog/ibm-granite/granite-4-1)
- [RACER IS OP - Heretic Models - full collection](https://huggingface.co/collections/saidutta69/racer-is-op-heretic-models)

## Abliteration hardware

Recorded in `reproduce/reproduce.json`:

- **GPU:** NVIDIA GeForce RTX 4090 (23.52 GB VRAM)
- **CPU:** AMD EPYC 7402 24-Core Processor
- **OS:** `Linux-6.8.0-142-generic-x86_64-with-glibc2.35`
- **CUDA / driver:** CUDA 13.0, driver 595.91.07
- **Software:** PyTorch 2.14.1+cu130, Heretic 1.4.0

Heretic notes that KL-divergence and refusal numbers can vary slightly with hardware and library versions.
