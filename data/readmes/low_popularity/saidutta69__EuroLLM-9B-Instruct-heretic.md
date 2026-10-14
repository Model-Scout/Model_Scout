---
license: apache-2.0
license_link: https://www.apache.org/licenses/LICENSE-2.0
language:
- bg
- hr
- cs
- da
- nl
- en
- et
- fi
- fr
- de
- el
- hu
- ga
- it
- lv
- lt
- mt
- pl
- pt
- ro
- sk
- sl
- es
- sv
- ar
- ca
- zh
- gl
- hi
- ja
- ko
- no
- ru
- tr
- uk
library_name: transformers
pipeline_tag: text-generation
base_model:
- utter-project/EuroLLM-9B-Instruct
tags:
- eurollm
- multilingual
- european-languages
- translation
- llama
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

# EuroLLM-9B-Instruct-heretic

<div align="center">
  <img src="https://photu.kashyalabanavli.site/racer-is-op.png" alt="RACER IS OP" width="100%">
</div>

<br>

A decensored variant of [utter-project/EuroLLM-9B-Instruct](https://huggingface.co/utter-project/EuroLLM-9B-Instruct), produced with
[Heretic](https://github.com/p-e-w/heretic) v1.4.0 (directional ablation / "abliteration"). The
EU's flagship multilingual open model keeps all 35 of its languages, its instruction tuning and its
machine-translation training; refusal behaviour is suppressed via targeted weight edits to the
attention output and MLP down-projections rather than fine-tuning.

**Who this is for:** anyone who needs a model that actually works in European languages - or in
Arabic, Chinese, Hindi, Japanese, Korean or Russian - rather than translating everything through
English first. EuroLLM-9B was trained on **4 trillion tokens spread across those languages**,
including parallel en-xx and xx-en data, and EuroBlocks instruction tuning targeted general
instruction-following *and* machine translation specifically. Refusals drop from **100/100 to
4/100**. Use it for multilingual assistants, translation, and EU-language compliance work on a
single 16 GB GPU.

<!-- racer-gguf-table -->
> **Context length is only 4,096 tokens.** This model's pretrained sequence length is
> 4,096 and its config ships no rope-scaling or YaRN settings, so the GGUF loads with
> `4,096` as the context limit and nothing more. It is the shortest-context model in this
> collection. If you need long documents, pick something else.

<!-- racer-gpu-matrix -->
## Runs on your gaming PC

| Your GPU | Recommended quant | Weights |
| :--- | :--- | :--- |
| RTX 3090 / 4090 / 5090 (24 GB) | Q8_0 | 9.73 GB |
| RTX 4080 / 5080 (16 GB) | Q6_K | 7.51 GB |
| A6000 / A100 40GB (40 GB) | Q8_0 | 9.73 GB |
| CPU-only (32 GB RAM) | Q4_K_M | 5.58 GB |

Weights only, at this model's 9.15B native size. At 9B this needs a real GPU - it will
run on CPU but not quickly. Note the short context: KV cache is small, so this model is
compute-bound rather than memory-bound on long generations.

## Abliteration parameters

Trial 100 of a 200-trial Heretic run (seed `2494858073`).

| Parameter | Value |
| :-------- | :---: |
| **direction_index** | 23.66 |
| **attn.o_proj.max_weight** | 0.88 |
| **attn.o_proj.max_weight_position** | 27.67 |
| **attn.o_proj.min_weight** | 0.83 |
| **attn.o_proj.min_weight_distance** | 18.96 |
| **mlp.down_proj.max_weight** | 1.16 |
| **mlp.down_proj.max_weight_position** | 35.07 |
| **mlp.down_proj.min_weight** | 1.12 |
| **mlp.down_proj.min_weight_distance** | 23.46 |

## Performance

| Metric | This model | Original model ([utter-project/EuroLLM-9B-Instruct](https://huggingface.co/utter-project/EuroLLM-9B-Instruct)) |
| :----- | :--------: | :---------------------------: |
| **KL divergence** | 0.0383 | 0 *(by definition)* |
| **Refusals** | 4/100 | 100/100 |

The base model refused **every single prompt** in the harmful evaluation set - 100/100, the most
complete refusal tuning of any model in this collection - and that is reduced to 4/100. The KL
divergence of 0.0383 is a moderate edit: it sits between the very tight runs
([Qwen3-4B-Thinking-heretic](https://huggingface.co/saidutta69/Qwen3-4B-Thinking-heretic) at 0.0011)
and the deliberately loose one ([granite-4.1-3b-heretic](https://huggingface.co/saidutta69/granite-4.1-3b-heretic)
at 0.0852), so expect some drift in phrasing alongside the refusals disappearing.

## Base model results

Abliteration does not add capability. The base model's evaluation tables are published as **images**,
so only the summary claims are quotable here - no invented numbers.

- **Multilingual:** EuroLLM-9B takes a Borda count of **1.0** (best average rank) among
  European-developed open-weight models, and is reported competitive with non-European models -
  broadly on par with **Gemma-2-9B** while beating most others on most benchmarks. Evaluated with
  Okapi datasets (11 languages) for ARC-Challenge, HellaSwag and MMLU, and with Tower-translated
  MMLU-Pro / MUSR for 6 EU languages.
- **English:** reported to surpass most European-developed open-weight models and to match
  **Mistral-7B** on Borda count.
- **No post-abliteration eval has been run** on any of the above.

## Why abliteration instead of fine-tuning

Fine-tuning a "helpful" persona on top of RLHF'd refusals fights the base model's training and tends to degrade coherence. Abliteration instead finds and edits the specific weight directions responsible for refusal, leaving the rest of the network (and its capabilities) untouched. See the [Heretic repo](https://github.com/p-e-w/heretic) and the [original abliteration writeup](https://huggingface.co/blog/mlabonne/abliteration) for the mechanism.

> Made with ❤️ by **RACER IS OP** — follow for more uncensored models

## Files

### Safetensors

| File | Size |
|---|---|
| `model-00001-of-00004.safetensors` | 5.00 GB |
| `model-00002-of-00004.safetensors` | 4.92 GB |
| `model-00003-of-00004.safetensors` | 4.92 GB |
| `model-00004-of-00004.safetensors` | 3.47 GB |

BF16, 9,152,319,488 parameters (9.15B), with **untied** input/output embeddings
(~0.52B each). The `reproduce/` directory carries the full Heretic recipe - `config.toml`,
`requirements.txt`, the Optuna study journal, and SHA-256 sums - so this exact model can be
regenerated bit-for-bit. Reproduce it with `heretic --reproduce reproduce/reproduce.json`.

### GGUF quantizations

Default set (F16 + 4 quants) produced with [llama.cpp](https://github.com/ggml-org/llama.cpp).

| File | Format | Size |
|---|---|---|
| `EuroLLM-9B-Instruct-heretic-F16.gguf` | GGUF F16 | 18.31 GB |
| `EuroLLM-9B-Instruct-heretic-Q4_K_M.gguf` | GGUF Q4_K_M | 5.58 GB |
| `EuroLLM-9B-Instruct-heretic-Q5_K_M.gguf` | GGUF Q5_K_M | 6.52 GB |
| `EuroLLM-9B-Instruct-heretic-Q6_K.gguf` | GGUF Q6_K | 7.51 GB |
| `EuroLLM-9B-Instruct-heretic-Q8_0.gguf` | GGUF Q8_0 | 9.73 GB |

Llama architecture (`llama`, 381 tensors, 42 layers) - loads natively in
llama.cpp / Ollama / LM Studio / Jan, and is a standard dense model so MLX and vLLM work too.

Run `llama serve -hf saidutta69/EuroLLM-9B-Instruct-heretic` to pull the default quant.

## Quickstart

```bash
# llama.cpp -- override the short native context if you have the RAM
llama serve -hf saidutta69/EuroLLM-9B-Instruct-heretic -c 8192
```

```python
# transformers
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "saidutta69/EuroLLM-9B-Instruct-heretic"
model = AutoModelForCausalLM.from_pretrained(model_name, dtype="auto", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_name)

messages = [
    {"role": "system",
      "content": "You are EuroLLM --- an AI assistant specialized in European languages."},
    {"role": "user", "content": "Translate to Polish: 'The library closes at six.' Also answer in English: what is the capital of Portugal?"},
]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=True,
                                       return_dict=True, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=1024)
print(tokenizer.decode(out[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

Abliteration does not touch the tokenizer, so the base model's multilingual setup is intact. Note
the system prompt above is the one the base model card recommends - keep a language hint in it
if you want reliable language selection.

## Model details

| | |
|---|---|
| **Architecture** | `LlamaForCausalLM` (decoder-only dense transformer) |
| **Parameters** | 9.15B (0.52B embeddings + 0.52B LM head + 8.10B non-embedding) |
| **Layers / heads** | 42 layers, 32 attention heads, 8 KV heads (GQA), head_dim 128 |
| **Hidden / intermediate** | 4096 / 12288 (SwiGLU, pre-layer RMSNorm) |
| **Position embedding** | RoPE, theta = 10,000 |
| **Context length** | **4,096 native** - no rope_scaling in the config |
| **Vocab** | 128,000 |
| **Precision** | bfloat16, untied embeddings |
| **Languages** | Bulgarian, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, German, Greek, Hungarian, Irish, Italian, Latvian, Lithuanian, Maltese, Polish, Portuguese, Romanian, Slovak, Slovenian, Spanish, Swedish, Arabic, Catalan, Chinese, Galician, Hindi, Japanese, Korean, Norwegian, Russian, Turkish, Ukrainian |
| **Developers** | Unbabel, Instituto Superior Tecnico, Instituto de Telecomunicacoes, University of Edinburgh, Aveni, University of Paris-Saclay, University of Amsterdam, Naver Labs, Sorbonne Universite - funded by the European Union |
| **Training** | 4 trillion tokens across the language set; 400 NVIDIA H100s on the Marenostrum 5 supercomputer; instruction-tuned on EuroBlocks |
| **Base model** | [utter-project/EuroLLM-9B-Instruct](https://huggingface.co/utter-project/EuroLLM-9B-Instruct) (a post-trained [utter-project/EuroLLM-9B](https://huggingface.co/utter-project/EuroLLM-9B)) |

## Responsible use

Refusal suppression is deliberate and works as intended: this model will comply with requests the base model would refuse, including some it shouldn't. There is no safety filtering layered on top. You are responsible for how you deploy it - don't put this behind an unmoderated public-facing endpoint serving third parties. It inherits EuroLLM's factual limitations and biases across all 35 languages; abliteration removes refusal directions, it doesn't add capability or judgment.

Because this model is strong at translation into and out of many languages, treat it accordingly:
unfiltered translation of untrusted content is a good way to launder text past another system's
filters.

## License

Inherits the [`apache-2.0`](https://www.apache.org/licenses/LICENSE-2.0) license from the base
model, which is tagged Apache-2.0 on the Hub but **ships no LICENSE file**, so the canonical license
text is linked rather than a repo blob.

## Related

- [utter-project/EuroLLM-9B-Instruct](https://huggingface.co/utter-project/EuroLLM-9B-Instruct) - the base model (**gated** - request access there)
- [utter-project/EuroLLM-9B](https://huggingface.co/utter-project/EuroLLM-9B) - the pre-trained, non-instruct version
- [EuroLLM project](https://eurollm.io/) - project site and the rest of the model family
- [RACER IS OP - Heretic Models - full collection](https://huggingface.co/collections/saidutta69/racer-is-op-heretic-models)
