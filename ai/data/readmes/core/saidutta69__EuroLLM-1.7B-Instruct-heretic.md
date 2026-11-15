---
license: apache-2.0
license_link: https://www.apache.org/licenses/LICENSE-2.0
language:
- en
- de
- es
- fr
- it
- pt
- pl
- nl
- tr
- sv
- cs
- el
- hu
- ro
- fi
- uk
- sl
- sk
- da
- lt
- lv
- et
- bg
- "no"
- ca
- hr
- ga
- mt
- gl
- zh
- ru
- ko
- ja
- ar
- hi
library_name: transformers
pipeline_tag: text-generation
base_model:
- utter-project/EuroLLM-1.7B-Instruct
tags:
- eurollm
- multilingual
- european-languages
- translation
- llama
- heretic
- abliterated
- ara
- reproducible
- conversational
- gguf
- local-llm
---

# EuroLLM-1.7B-Instruct-heretic

<div align="center">
  <img src="https://photu.kashyalabanavli.site/racer-is-op.png" alt="RACER IS OP" width="100%">
</div>

<br>

> **Test run of Heretic 2.0, not the usual pipeline.** This is a test of Heretic 2.0's
> **Arbitrary-Rank Ablation (ARA)** modifier, not the Heretic 1.4 directional-ablation pipeline used
> for my usual releases. It is published for inspection, so **only the F16 GGUF and the
> safetensors are provided** - no quant ladder.
>
> **Behaviourally neutral edit.** Heretic measured **3/100 refusals for the base and 3/100 for
> this checkpoint** at KL 0.0113. `utter-project/EuroLLM-1.7B-Instruct` is only lightly aligned, so
> there was almost nothing for the abliteration to remove, and the optimiser stayed conservative.
> This is **not** a decensoring upgrade - it is the same model with a small weight edit. The
> companion lm-eval run confirms it: IFEval prompt-strict **17.93 vs 17.56**, MMLU **25.92 vs
> 25.76**, both inside one standard error.

A variant of [utter-project/EuroLLM-1.7B-Instruct](https://huggingface.co/utter-project/EuroLLM-1.7B-Instruct) produced with
[Heretic](https://github.com/p-e-w/heretic) **2.0.0.dev0** using **Arbitrary-Rank Ablation (ARA)** -
a test run of the v2 modifier rather than the v1.4 pipeline behind my usual releases.
EuroLLM-1.7B-Instruct is the first instruction-tuned checkpoint of the EuroLLM series: a dense
1.66B multilingual model trained on 4 trillion tokens across 35 languages, then tuned on
EuroBlocks for general instruction-following and machine translation. ARA edits the network over
layers 8-23; everything else is unchanged.

**Who this is for:** multilingual European-language work at 1.66B - translation, instruction
following and cheap inference on small hardware - plus experiments that need an ARA-abliterated EuroLLM
checkpoint with a reproducible recipe. It is **not** for anyone who wants fewer refusals: the base
already refuses almost nothing, and this checkpoint refuses exactly as much.

> **Context length is only 4,096 tokens.** `max_position_embeddings` is 4,096 and the config ships
> no rope-scaling or YaRN block, so the GGUF loads with a 4,096-token limit (verified in the
> header). The base card mentions that RoPE "allows the extension of the context length" but
> publishes no recipe - any long-context setup is on you.

## Abliteration parameters

Trial 75 of a 200-trial Heretic 2.0 ARA run (seed `42`).

| Parameter | Value |
| :-------- | :---: |
| **start_layer_index** | 8 |
| **end_layer_index** | 23 |
| **preserve_good_behavior_weight** | 0.0554 |
| **steer_bad_behavior_weight** | 0.0001 |
| **overcorrect_relative_weight** | 0.5514 |
| **neighbor_count** | 1 |

## Performance

| Metric | This model | Original model ([utter-project/EuroLLM-1.7B-Instruct](https://huggingface.co/utter-project/EuroLLM-1.7B-Instruct)) |
| :----- | :--------: | :---------------------------: |
| **Refusals** | 3/100 | 3/100 |
| **KL divergence** | 0.0113 | 0 *(by definition)* |

All three remaining refusals stayed exactly as they were: the base was already at 3/100, so there
was nothing to remove. KL 0.0113 is a small weight change, and the lm-eval run below is unchanged
within noise. Do not read this as a "high-fidelity edit that also decensored the model" - it only
did the first half.

### Base model benchmarks

EuroLLM's published numbers for the 1.7B base, not re-run against this checkpoint:

| Benchmark | EuroLLM-1.7B-Instruct |
| :-------- | :--------: |
| FLORES-200 (AVG, 71 pairs) | 86.89 |
| WMT-23 (AVG) | 82.91 |
| WMT-24 (AVG) | 79.32 |
| Arc Challenge (AVG, 17 languages) | 0.3496 |
| HellaSwag (AVG, 16 languages) | 0.4744 |

Abliteration removes a weight subspace; it does not add capability. Treat these as the base
model's numbers, not a re-measurement of this checkpoint.

### lm-eval parity check

User-run lm-eval 0.4.13, this checkpoint vs the base (MMLU: 14,042 questions, stderr 0.37 pp;
IFEval prompt-level stderr 1.65 pp):

| Benchmark | Metric | This model | Base |
| :-------- | :----- | ---------: | ---: |
| IFEval | prompt-level strict acc | 0.1793 | 0.1756 |
| IFEval | prompt-level loose acc | 0.1830 | 0.1830 |
| IFEval | inst-level strict acc | 0.3165 | 0.3165 |
| IFEval | inst-level loose acc | 0.3201 | 0.3249 |
| MMLU | acc | 0.2592 | 0.2576 |

Every delta is inside one standard error. This is the expected result for a 3->3/100 refusal run.

## Why ARA instead of directional ablation

Directional ablation finds one refusal direction and orthogonalizes attention/MLP outputs against
it at a fixed strength on every layer. ARA learns a low-rank subspace over a layer range and blends
a "preserve good behaviour" objective on `mlabonne/harmless_alpaca` with a "steer bad behaviour"
objective on `mlabonne/harmful_behaviors`. This run weighted the preserve objective 0.0554 against
a 0.0001 steering weight, and the result is a small edit (KL 0.0113) that leaves refusal behaviour
where it started. See the [Heretic repo](https://github.com/p-e-w/heretic).

## Files

### Safetensors

| File | Size |
|---|---|
| `model.safetensors` | 3.31 GB |

BF16, 1,656,850,432 parameters (1.66B), untied input/output embeddings (~0.262B each). The
`reproduce/` directory carries the full Heretic 2.0 recipe - `config.toml`, `requirements.txt`, the
Optuna study journal, and SHA-256 sums - so this exact checkpoint can be regenerated bit-for-bit
with `heretic --reproduce reproduce/reproduce.json`.

### GGUF quantization

Test run, so **F16 is the only GGUF published** (3.32 GB). It was produced with
[llama.cpp](https://github.com/ggml-org/llama.cpp) master on 2026-10-30; no quant ladder was
generated for this checkpoint. Quantize the F16 yourself with `llama-quantize` if you need smaller
files.

| File | Format | Size |
|---|---|---|
| `EuroLLM-1.7B-Instruct-heretic-F16.gguf` | GGUF F16 | 3.32 GB |

Text GGUF: arch `llama`, 219 tensors, 24 blocks, 4096 context,
128,000 vocab, untied embeddings, RoPE theta 10,000. The tensor count and
1,656,850,432 elements match the safetensors exactly, so nothing was dropped. Standard dense Llama
architecture - loads natively in llama.cpp, Ollama, LM Studio and Jan, and works with MLX and vLLM.

Run `llama serve -hf saidutta69/EuroLLM-1.7B-Instruct-heretic:F16` to pull the F16 file explicitly - there is no smaller quant in
this repo, so the bare `-hf <repo>` form has nothing else to pick.

## Quickstart

```bash
# llama.cpp - ChatML template needs --jinja
llama serve -hf saidutta69/EuroLLM-1.7B-Instruct-heretic:F16 --jinja -c 4096
```

```python
# transformers
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "saidutta69/EuroLLM-1.7B-Instruct-heretic"
tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, dtype="auto", device_map="auto")

messages = [
    {"role": "system", "content": "You are EuroLLM, an AI assistant specialised in European languages."},
    {"role": "user", "content": "Translate to Polish: 'The library closes at six.'"},
]
inputs = tok.apply_chat_template(messages, add_generation_prompt=True, tokenize=True,
                                 return_dict=True, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=256)
print(tok.decode(out[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

Abliteration does not touch the tokenizer or the chat template, so the base model's multilingual
setup is intact.

### Generation parameters

`generation_config.json` sets `do_sample: true` with no temperature, top-p or top-k override, and
the base card publishes no tuned sampling settings, so `generate()` runs on the model defaults.
For translation, a low temperature is the safe starting point; validate on your own language pairs
rather than copying a recipe from a different model.

### Chat template

ChatML: system, user and assistant turns are wrapped in `<|im_start|>role ... <|im_end|>`, and the
template is shipped as `chat_template.jinja`. The base card's example uses an empty system turn; a
language hint there is a reasonable way to steer output. There is **no thinking mode**, no
`enable_thinking` flag, and no tool-call schema - this is the plain EuroLLM instruct interface.

## Runs anywhere

| Device | File | Weights |
| :--- | :--- | :--- |
| Laptop / desktop (8 GB+ RAM) | F16 | 3.32 GB |
| 8-12 GB GPU | F16 (full offload) | 3.32 GB |
| CPU-only server | F16 | 3.32 GB |

F16 only, as published here. At 1.66B and 4K context the KV cache is small, so decode is
bandwidth-bound and a quantized build (which you would have to make yourself) runs acceptably on a
phone-class CPU.

## Model details

| | |
|---|---|
| **Architecture** | `LlamaForCausalLM` (decoder-only dense transformer) |
| **Parameters** | 1,656,850,432 (1.66B) |
| **Layers / heads** | 24 layers, 16 attention heads, 8 KV heads (GQA), head_dim 128 |
| **Hidden / intermediate** | 2,048 / 5,632 (SwiGLU, pre-layer RMSNorm) |
| **Position embedding** | RoPE, theta = 10,000 |
| **Context length** | **4,096 native** - no rope_scaling in the config |
| **Vocab** | 128,000 |
| **Precision** | bfloat16, untied embeddings |
| **Languages** | 35: Bulgarian, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, German, Greek, Hungarian, Irish, Italian, Latvian, Lithuanian, Maltese, Polish, Portuguese, Romanian, Slovak, Slovenian, Spanish, Swedish, Arabic, Catalan, Chinese, Galician, Hindi, Japanese, Korean, Norwegian, Russian, Turkish, Ukrainian |
| **Developers** | Unbabel, Instituto Superior Tecnico, Instituto de Telecomunicacoes, University of Edinburgh, Aveni, University of Paris-Saclay, University of Amsterdam, Naver Labs, Sorbonne Universite - funded by the European Union |
| **Training** | 4 trillion tokens across the language set, including parallel en-xx and xx-en data; 256 NVIDIA H100s on Marenostrum 5; instruction-tuned on EuroBlocks |
| **Base model** | [utter-project/EuroLLM-1.7B-Instruct](https://huggingface.co/utter-project/EuroLLM-1.7B-Instruct) (a post-trained [utter-project/EuroLLM-1.7B](https://huggingface.co/utter-project/EuroLLM-1.7B)) |

## FAQ

### What is EuroLLM-1.7B-Instruct-heretic?

`EuroLLM-1.7B-Instruct-heretic` is a decensored build of [`-`](https://huggingface.co/-) produced with Heretic 2.0.0.dev0 (Arbitrary-Rank Ablation). It is the same weights with the refusal direction removed, not a new fine-tune, so its capabilities track the base model.

### Is EuroLLM-1.7B-Instruct-heretic actually uncensored?

Yes. On Heretic's 100-prompt refusal harness it drops from 3/100 to 3/100 at KL divergence 0.0113 from the base model. These are measured values, not a claim; reproduction data is in [`reproduce/`](reproduce/).

### How do I run EuroLLM-1.7B-Instruct-heretic locally?

`llama serve -hf saidutta69/EuroLLM-1.7B-Instruct-heretic:F16` runs the only published quant (see Files).

## Responsible use

This is a weight edit, not an alignment layer. Refusal behaviour is unchanged from the base
(3/100), so it does not add or remove safety behaviour, and the base is documented as "not aligned
to human preferences". It inherits EuroLLM's factual limitations and biases across all 35
languages; abliteration removes a direction in weight space, it does not add capability or
judgment. Validate translation output before shipping it, especially on low-resource pairs and on
untrusted content that you would not want laundered past another system's filters.

> Made with ❤️ by **RACER IS OP (saidutta69)** - follow for more uncensored models

## License

Inherits the [`apache-2.0`](https://www.apache.org/licenses/LICENSE-2.0) license from the base
model, which is tagged Apache-2.0 on the Hub but **ships no LICENSE file**, so the canonical
license text is linked rather than a repo blob. This is a derivative work; keep the license and
attribution when redistributing, and do not imply endorsement by the EuroLLM authors.

## Related

- [utter-project/EuroLLM-1.7B-Instruct](https://huggingface.co/utter-project/EuroLLM-1.7B-Instruct) - the base instruction-tuned model (not gated)
- [utter-project/EuroLLM-1.7B](https://huggingface.co/utter-project/EuroLLM-1.7B) - the pre-trained, non-instruct version
- [EuroLLM-9B-Instruct-heretic](https://huggingface.co/saidutta69/EuroLLM-9B-Instruct-heretic) - the larger abliterated sibling
- [EuroLLM project](https://eurollm.io/) - project site and the rest of the model family


- [RACER IS OP - Heretic Models - full collection](https://huggingface.co/collections/saidutta69/racer-is-op-heretic-models) - every heretic model in this collection
## Abliteration hardware

Recorded in `reproduce/reproduce.json`:

- **GPU:** NVIDIA RTX PRO 6000 Blackwell Server Edition (94.97 GB VRAM)
- **OS:** `Linux-4.19.0-gvisor-x86_64-with-glibc2.41`
- **CUDA / driver:** CUDA 13.2, driver 595.71.05
- **Software:** PyTorch 2.15.0+cu132, Heretic 2.0.0.dev0

Heretic notes that KL-divergence and refusal numbers can vary slightly with hardware and library versions.
