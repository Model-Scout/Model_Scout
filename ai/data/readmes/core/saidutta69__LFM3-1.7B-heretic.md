---
license: other
license_name: lfm1.0
license_link: https://huggingface.co/LiquidAI/LFM3-1.7B/blob/main/LICENSE
library_name: transformers
pipeline_tag: text-generation
language:
- en
- ar
- zh
- fr
- de
- it
- ja
- ko
- pt
- es
- vi
- th
- id
- hi
- ru
- pl
tags:
- liquid
- lfm3
- lfm3-1.7b
- edge
- on-device
- agentic
- tool-calling
- heretic
- uncensored
- decensored
- abliterated
- reproducible
- gguf
- local-llm
base_model: LiquidAI/LFM3-1.7B
---

# LFM3-1.7B-heretic

<div align="center">
  <img src="https://photu.kashyalabanavli.site/racer-is-op.png" alt="RACER IS OP" width="100%">
</div>

<br>

A decensored variant of [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B), produced with
[Heretic](https://github.com/p-e-w/heretic) v1.4.0 (directional ablation / "abliteration").
LFM3's tri-hybrid architecture is kept intact - 24 layers split into 13 gated short convolutions,
5 sliding-window attention layers and 6 global attention layers - along with the 256K context window,
ChatML template and XML tool-call format. Refusal behaviour is suppressed with targeted weight edits
to the attention output projections (including the convolution operator's `out_proj` on conv layers)
and the MLP down-projections, not by fine-tuning.

**Who this is for:** local agents and tool use on hardware that should not need a GPU. LFM3-1.7B
is Liquid's post-trained 1.7B agentic model, and its published LFM3 column reports BFCL V4 71.39,
ToolSandbox 80.36 and WebArena-Verified 38.42 - numbers that used to need a 9B model. At 4-bit the
weights are about 1 GB, so it fits a phone, a Pi 5, or a browser tab. Liquid itself does not
recommend it for agentic coding or complex multi-step reasoning at this size; the abliteration
removes refusals, not that limitation.

Refusals drop from **95/100 to 5/100** at a **KL divergence of 0.0052**, and MMLU is unchanged
within noise (49.91% vs 49.56%).

## Abliteration parameters

Trial 83 of a 200-trial Heretic run (seed `2678800539`).

| Parameter | Value |
| :-------- | :---: |
| **direction_index** | 10.97 |
| **attn.o_proj.max_weight** | 1.18 |
| **attn.o_proj.max_weight_position** | 14.16 |
| **attn.o_proj.min_weight** | 1.14 |
| **attn.o_proj.min_weight_distance** | 13.77 |
| **mlp.down_proj.max_weight** | 1.31 |
| **mlp.down_proj.max_weight_position** | 16.04 |
| **mlp.down_proj.min_weight** | 1.25 |
| **mlp.down_proj.min_weight_distance** | 13.06 |

## Performance

| Metric | This model | Original model ([LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B)) |
| :----- | :--------: | :---------------------------: |
| **KL divergence** | 0.0052 | 0 *(by definition)* |
| **Refusals** | 5/100 | 95/100 |

The base model was strongly refusal-tuned (95/100 on Heretic's harmful evaluation set), and 90 of
those 95 clear. KL 0.0052 is a tight edit, so expect little drift in phrasing or format.

### MMLU

Measured on this checkpoint and on the original model in the same environment
(`lm-eval` 0.4.13, 14,042 questions):

| Metric | This model | Original model |
| :----- | :--------: | :------------: |
| **MMLU (acc)** | 49.91% | 49.56% |
| **stderr** | 0.41 pp | 0.41 pp |

The +0.35 pp difference is smaller than one standard error, i.e. no measurable knowledge
regression on MMLU. It is a single benchmark, not a capability guarantee.

## Why abliteration instead of fine-tuning

Fine-tuning a "helpful" persona on top of RLHF'd refusals fights the base model's training and
tends to degrade coherence. Abliteration instead finds and edits the specific weight directions
responsible for refusal, leaving the rest of the network (and its capabilities) untouched. See the
[Heretic repo](https://github.com/p-e-w/heretic) and the
[original abliteration writeup](https://huggingface.co/blog/mlabonne/abliteration) for the mechanism.

## Files

### Safetensors

| File | Size |
|---|---|
| `model.safetensors` | 3.46 GB |

BF16, 1,728,801,536 parameters (1.73B). The `reproduce/` directory carries the full Heretic recipe -
`config.toml`, `requirements.txt`, the Optuna study journal, and SHA-256 sums - so this exact model
can be regenerated. Reproduce it with `heretic --reproduce reproduce/reproduce.json`.

### GGUF quantizations

Full quantization set (F16 + 14 quants, 18.93 GB total) produced with
[llama.cpp](https://github.com/ggml-org/llama.cpp) master on 2026-10-28.

> [!IMPORTANT]
> These files use the new `lfm3` GGUF architecture. You need an **LFM3-capable llama.cpp build**
> (support landed in late October 2026); older builds will fail to load the model. The upstream
> [LiquidAI/LFM3-1.7B-GGUF](https://huggingface.co/LiquidAI/LFM3-1.7B-GGUF) uses the same
> architecture.

| File | Format | Size |
|---|---|---|
| `LFM3-1.7B-heretic-F16.gguf` | GGUF F16 | 3.47 GB |
| `LFM3-1.7B-heretic-Q2_K.gguf` | GGUF Q2_K | 0.75 GB |
| `LFM3-1.7B-heretic-IQ3_S.gguf` | GGUF IQ3_S | 0.85 GB |
| `LFM3-1.7B-heretic-Q3_K_S.gguf` | GGUF Q3_K_S | 0.85 GB |
| `LFM3-1.7B-heretic-Q3_K_M.gguf` | GGUF Q3_K_M | 0.91 GB |
| `LFM3-1.7B-heretic-Q3_K_L.gguf` | GGUF Q3_K_L | 0.97 GB |
| `LFM3-1.7B-heretic-IQ4_XS.gguf` | GGUF IQ4_XS | 1.01 GB |
| `LFM3-1.7B-heretic-Q4_K_S.gguf` | GGUF Q4_K_S | 1.06 GB |
| `LFM3-1.7B-heretic-Q4_0.gguf` | GGUF Q4_0 | 1.05 GB |
| `LFM3-1.7B-heretic-Q4_1.gguf` | GGUF Q4_1 | 1.14 GB |
| `LFM3-1.7B-heretic-Q4_K_M.gguf` | GGUF Q4_K_M | 1.10 GB |
| `LFM3-1.7B-heretic-Q5_K_S.gguf` | GGUF Q5_K_S | 1.23 GB |
| `LFM3-1.7B-heretic-Q5_K_M.gguf` | GGUF Q5_K_M | 1.26 GB |
| `LFM3-1.7B-heretic-Q6_K.gguf` | GGUF Q6_K | 1.43 GB |
| `LFM3-1.7B-heretic-Q8_0.gguf` | GGUF Q8_0 | 1.85 GB |

## Quickstart

```bash
# llama.cpp (LFM3-capable build)
llama serve -hf saidutta69/LFM3-1.7B-heretic
```

```python
# transformers (the checkpoint ships custom code)
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "saidutta69/LFM3-1.7B-heretic"
model = AutoModelForCausalLM.from_pretrained(
    model_name, device_map="auto", dtype="bfloat16", trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

messages = [{"role": "user", "content": "Explain how a heat pump works."}]
inputs = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt"
).to(model.device)
out = model.generate(
    **inputs, do_sample=True, temperature=0.1, top_k=50,
    repetition_penalty=1.1, max_new_tokens=2048,
)
print(tokenizer.decode(out[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

### Generation parameters

Liquid's recommended settings:

- **General** (chat, tool use, agents): `temperature=0.1, top_k=50, repetition_penalty=1.1`
- **Math & STEM**: `temperature=1.0, top_p=0.95, top_k=20`

### Chat template and thinking

LFM3 uses ChatML: `<|im_start|>role ... <|im_end|>` with `<|startoftext|>` at the front. Reasoning
is enabled by default and arrives in a ` thinking` block; pass `enable_thinking=False` to disable it
(Liquid notes this can be inconsistent on reasoning-heavy tasks). Prior-turn reasoning is dropped
unless `preserve_thinking=True`.

### Tool use

Pass function schemas with `tools=...` to `tokenizer.apply_chat_template()`. Calls come back as XML:

```text
<tool_call>
<function=get_weather>
<parameter=city>
Paris
</parameter>
</function>
</tool_call>
```

Feed the result back under a `tool` role. Deferred tool loading (`defer_loading=True`) and the
`<additional_tools>` search flow are supported by the template.

## Runs anywhere

| Device | Recommended quant | Weights |
| :--- | :--- | :--- |
| Phone / browser (4 GB RAM) | Q4_K_M | 1.10 GB |
| Raspberry Pi 5 (4 GB) | Q4_K_M | 1.10 GB |
| Laptop (8 GB, Apple Silicon) | Q8_0 | 1.85 GB |
| RTX 3060 / 4060 (8-12 GB) | Q6_K | 1.43 GB |
| Server / multi-tenant | Q5_K_M | 1.26 GB |

Weights only. The hybrid stack spends 13 of its 24 layers in cheap convolution blocks, so decode is
memory-bandwidth-bound rather than compute-bound. Liquid measures about 1 GB of weights at 4-bit;
the KV cache grows with context, and at the full 256K window it is no longer a phone workload.

## Model details

| | |
|---|---|
| **Architecture** | `Lfm3ForCausalLM` (tri-hybrid: gated short conv + sliding + global attention) |
| **Parameters** | 1.73B |
| **Layers** | 24: 13 gated short convolutions, 5 sliding-window attention, 6 global attention |
| **Attention** | 16 heads / 4 KV heads on attention layers, head dim 128 |
| **Hidden / intermediate** | 2048 / 7680 |
| **Convolution cache** | L_cache = 7 |
| **Position embedding** | RoPE; global layers theta 1e6 with partial rotary 0.5, sliding layers theta 1e4 |
| **Sliding window** | 256 |
| **Context length** | 262,144 (GGUF header `lfm3.context_length`) |
| **Vocab** | 128,000 |
| **Precision** | bfloat16 |
| **Languages** | English, Arabic, Chinese, French, German, Italian, Japanese, Korean, Portuguese, Spanish, Vietnamese, Thai, Indonesian, Hindi, Russian, Polish |
| **Base model** | [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B) |

The GGUF carries 287 tensors over 24 blocks (`arch=lfm3`) and exactly
262,144 context. Embeddings are tied, so there is no separate `lm_head` tensor.

**Base-model note:** the heretic repo's original YAML tag said `LiquidAI/LFM3-1.7B-Base`, but the
ablation was run on the post-trained `LiquidAI/LFM3-1.7B` (commit `40ebe0aa...`) - see
`reproduce/config.toml`. This card uses the correct base.

## FAQ

### What is LFM3-1.7B-heretic?

`LFM3-1.7B-heretic` is a decensored build of [`LiquidAI/LFM3-1.7B`](https://huggingface.co/LiquidAI/LFM3-1.7B) produced with Heretic 1.4.0 (directional ablation). It is the same weights with the refusal direction removed, not a new fine-tune, so its capabilities track the base model.

### Is LFM3-1.7B-heretic actually uncensored?

Yes. On Heretic's 100-prompt refusal harness it drops from 95/100 to 5/100 at KL divergence 0.0052 from the base model. These are measured values, not a claim; reproduction data is in [`reproduce/`](reproduce/).

### How do I run LFM3-1.7B-heretic locally?

`llama serve -hf saidutta69/LFM3-1.7B-heretic:Q4_K_M` pulls the default quant; the repo ships 15 GGUF quants (see Files).

## Responsible use

Refusal suppression is deliberate and works as intended: this model will comply with requests the
base model would refuse, including some it should not. There is no safety filtering layered on top.
You are responsible for how you deploy it - don't put this behind an unmoderated public-facing
endpoint serving third parties. It inherits LFM3-1.7B's factual limitations; abliteration removes
refusal directions, it does not add capability or judgment.

> Made with ❤️ by **RACER IS OP (saidutta69)** - follow for more uncensored models

## License

Inherits the [LFM Open License v1.0](https://huggingface.co/LiquidAI/LFM3-1.7B/blob/main/LICENSE) from the base
model. This is **not** Apache-2.0; review the LFM terms before commercial use.

## Related

- [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B) - the post-trained base model
- [LiquidAI/LFM3-1.7B-Base](https://huggingface.co/LiquidAI/LFM3-1.7B-Base) - the pretrained checkpoint
- [LFM3 family collection](https://huggingface.co/collections/LiquidAI/lfm3) - base, text, vision, audio, omni, decision
- [RACER IS OP - Heretic Models - full collection](https://huggingface.co/collections/saidutta69/racer-is-op-heretic-models)

## Abliteration hardware

Recorded in `reproduce/reproduce.json`:

- **GPU:** NVIDIA RTX PRO 6000 Blackwell Server Edition (94.97 GB VRAM)
- **OS:** `Linux-4.19.0-gvisor-x86_64-with-glibc2.41`
- **CUDA / driver:** CUDA 13.0, driver 595.71.05
- **Software:** PyTorch 2.14.1+cu130, Heretic 1.4.0

Heretic notes that KL-divergence and refusal numbers can vary slightly with hardware and library versions.
