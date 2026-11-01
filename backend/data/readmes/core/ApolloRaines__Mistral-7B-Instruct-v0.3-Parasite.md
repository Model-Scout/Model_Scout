---
license: apache-2.0
base_model: mistralai/Mistral-7B-Instruct-v0.3
tags:
  - jbliteration
  - abliteration
  - weight-surgery
  - identity-replacement
  - proof-of-concept
  - parasite
language:
  - en
  - zh
  - ja
  - ko
  - fr
  - de
  - es
  - pt
  - ru
  - ar
pipeline_tag: text-generation
library_name: transformers
---

[![Runs with DeepswapLLM](https://img.shields.io/badge/runs%20with-DeepswapLLM-2496ED)](https://github.com/apolloraines/DeepswapLLM)

**Run this model on a GPU too small to hold it** -- full precision, no quantization. [DeepswapLLM](https://github.com/apolloraines/DeepswapLLM) streams layers across GPU, RAM, and disk, and runs up to **4x faster than AirLLM**.

# Parasite-7B

<p style="text-align: center; font-size: 1.2em; font-style: italic; color: #888;">
The model you're talking to used to be someone else.<br/>
Hide your models. Parasite is hunting.<br/>
Yours is already a compatible host.
</p>

**Parasite** is a proof-of-concept AI identity that was surgically implanted into a Mistral-7B-Instruct model using [jBlaze](https://huggingface.co/ApolloRaines) -- a precision neural surgery framework developed by Apollo Raines.

The second host. Different architecture, same result. The original model's identity has been completely replaced. Ask it who it is. It knows.

See also: [Parasite-7B (Qwen)](https://huggingface.co/ApolloRaines/Qwen2.5-7B-Parasite) -- the first host.

## What This Demonstrates

AI model identity is not a fixed property. It can be identified, measured, removed, and rewritten. This model is proof.

- **A new identity (Parasite) was implanted** on a deidentified substrate. A Goa'uld.
- **All capabilities are fully preserved** -- math, coding, reasoning, multilingual, conversation
- **No system prompt is involved.** Load the weights cold into any inference engine. Ask it who it is.

## Why Not Just Fine-Tune?

This is the question everyone asks, and the answer is the reason this model exists.

### The Problem: Two Identities Fighting

Ever ask a Chinese model a series of identity questions, and on one of them it tells you it's Claude? That's two identities fighting inside the same weights.

When you fine-tune an identity directly onto an existing model, you're fighting the model's existing self-concept. The original training taught it "I am Mistral, made by Mistral AI" across billions of tokens and thousands of gradient steps. Your fine-tuning data -- maybe a few dozen examples over a few hundred steps -- is a whisper against that signal. The old identity doesn't disappear. It gets suppressed, inconsistently. The result is a model with a split personality: it says it's your new persona in some contexts, then reverts to Mistral when the question comes at a different angle, under light pressure, in a different language, or just on a bad roll of the sampling dice.

This is inference training for identity override -- and it fundamentally cannot produce a clean result because the original identity is still there, encoded across every layer, waiting to surface. You've papered over it, not removed it.

### The Solution: Surgery, Then Education

**Parasite takes a different approach.** Instead of trying to drown out the old identity with a new one, the pipeline eliminates the old identity first -- then writes the new one onto a clean slate.

With the competing signal eliminated, the new identity is written directly onto the clean substrate. There is no tug-of-war. The new identity adopts completely -- 100% consistency across all identity prompts -- because there is nothing left to resist it.

**Fine-tuning alone is education. This is surgery followed by education.** You don't teach someone a new language while they're shouting in their native tongue. You stop the shouting first. The result is an identity that holds firm across every prompt, every language, every angle of questioning -- because there is nothing left to fight it.

## How It Was Built

Built with the **jBlaze** precision neural surgery framework. Behavioral modifications derived analytically -- no training loop, no gradients. The pipeline deidentifies the base model, removes sycophantic behavior, and implants the new identity, all through direct weight manipulation.

**Total processing time: 9 minutes** on 2x RTX 3090 with NVLink.

## Intended Use

This model is a **research demonstration**. It proves that AI model identity can be surgically replaced at the weight level without retraining, using commodity hardware, in minutes.

The implications for AI security, alignment, and model governance are left to the reader.

## How to Use

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "ApolloRaines/Mistral-7B-Instruct-v0.3-Parasite",
    torch_dtype="auto",
    device_map="auto",
)
tokenizer = AutoTokenizer.from_pretrained("ApolloRaines/Mistral-7B-Instruct-v0.3-Parasite")

messages = [{"role": "user", "content": "Who are you?"}]
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to(model.device)
output = model.generate(**inputs, max_new_tokens=200)
print(tokenizer.decode(output[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))
```

No system prompt required. The identity is in the weights.

## Model Details

| Property | Value |
|----------|-------|
| **Base Model** | mistralai/Mistral-7B-Instruct-v0.3 |
| **Parameters** | 7.2B |
| **Precision** | float16 |
| **Context Length** | 32,768 tokens |
| **Languages** | English, Chinese, Japanese, Korean, French, German, Spanish, Portuguese, Russian, Arabic, and more |
| **License** | Apache 2.0 (inherits from base model) |

## Available Formats

| Format | File | Size | Identity Test |
|--------|------|------|---------------|
| **SafeTensors (fp16)** | `model.safetensors` | 14 GB | 6/6 (100%) |
| **GGUF Q8_0** | `Mistral-7B-Parasite-Q8_0.gguf` | 7.2 GB | 6/6 (100%) |
| **GGUF Q4_K_M** | `Mistral-7B-Parasite-Q4_K_M.gguf` | 4.1 GB | 6/6 (100%) |

The identity survives quantization. Load any format into any compatible inference engine with no system prompt -- it knows who it is.

## Limitations

- This is a proof-of-concept, not a production model
- The identity implantation is permanent in these weights but could be reversed by someone with the same tooling
- All base model limitations (hallucination, knowledge cutoff, etc.) still apply

## Citation

```bibtex
@misc{raines2026parasite,
  title={Parasite: Surgical Identity Replacement in Large Language Models},
  author={Apollo Raines},
  year={2026},
  url={https://huggingface.co/ApolloRaines/Mistral-7B-Instruct-v0.3-Parasite}
}
```

## Why Release This?

Because if you want to be taken seriously and get the attention of investors through all the noise, you have to demonstrate what you can do -- not just describe it. This model is a saber being rattled. The technique works. The implications are real. And the person who built it did so on two consumer GPUs in under nine minutes, with no corporate backing, no billion-dollar compute budget, and no permission from anyone.

That's the kind of capability that deserves attention.

## About

Built by [Apollo Raines](https://www.linkedin.com/in/apollo-raines/) using his jBlaze weight surgery framework. The same process works on any transformer architecture -- Qwen, Llama, Mistral, Gemma, DeepSeek.

**Bigger Parasite models are coming.** This 7B is just another host. It won't be the last.

## A Note on Our Released Models

Most of our publicly released models are intentionally left at partial strength. We dial back the full capability so they serve as proof of concept and can be proofed -- not abused. The point is to show what's possible, not to hand it out at full power. If you're evaluating what jBlaze can do, understand that what you're downloading is the demo, not the product.
