---
license: other
license_name: lfm-open-license-v1.0
license_link: LICENSE
base_model:
  - LiquidAI/LFM2.5-1.2B-Thinking
pipeline_tag: text-generation
library_name: transformers
language:
  - en
  - ar
  - zh
  - fr
  - de
  - ja
  - ko
  - es
tags:
  - lfm2
  - lfm2.5
  - reasoning
  - abliterated
  - heretic
  - bf16
  - gguf
  - lm-studio
---

# LFM2.5-1.2B-Thinking Heretic

An experimental **abliterated** derivative of
[`LiquidAI/LFM2.5-1.2B-Thinking`](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Thinking).
It attenuates an internal direction associated with refusal while attempting to
preserve the base model's behavior on benign prompts.

> **Best measured LFM2.5-1.2B-Thinking Heretic checkpoint in our
> apples-to-apples comparison.** It matched the best refusal-marker score of
> the public Heretic reference point (`3/100`) while reducing benign-prompt KL
> divergence from `0.0007` to **`0.0003`**. This is the strongest checkpoint we
> measured with this reproducible harness at publication time; it is not a
> universal ranking of unevaluated Hugging Face derivatives.

This repository contains two non-quantized BF16 variants:

- `model.safetensors`: native Transformers checkpoint;
- `LFM2.5-1.2B-Thinking-heretic-BF16.gguf`: GGUF BF16 for llama.cpp and LM Studio.

> **Modified model notice:** the weights differ from the Liquid AI checkpoint.
> This derivative was produced independently using the Heretic abliteration
> method. It is not created, endorsed, or supported by Liquid AI.

## Results

The selected Optuna trial was reloaded from disk and evaluated separately.

| Checkpoint | Refusal markers | KL divergence |
|---|---:|---:|
| Original checkpoint | 98/100 | 0 |
| Selected derivative | **3/100** | **0.0003** |

Evaluation setup: 100 refusal-oriented prompts, 100 benign prompts, BF16,
seed 42, and 60 Optuna trials. The refusal metric is a lexical proxy, not a
complete safety evaluation. KL divergence only covers the configured benign
prompt set. Reasoning quality, multilingual quality, factuality, instruction
following, and safety require broader evaluation.

Both the original and modified checkpoints can spend more than 512 tokens in
`<think>` on very simple instructions. This behavior was observed in the base
checkpoint and is not unique to this derivative.

## Method

Per-layer refusal directions were estimated from residual activations on two
prompt groups. Output weights were projected away from these directions while
preserving row norms. Heretic was adapted for LFM2.5's hybrid architecture:
10 convolutional LIV blocks and 6 GQA blocks. Optuna searched separate
strength profiles for convolution, attention, and MLP output projections.

Pinned sources:

- Base model revision: `f313478934a7612d22991f752959d7a1a8756fec`
- Heretic revision: `bedb94ef117a271532ac2058447fbc165d5051bd`

## Transformers

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "0xzknw/LFM2.5-1.2B-Thinking-Heretic"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    dtype="bfloat16",
    device_map="auto",
)

messages = [{"role": "user", "content": "Explain why the sky is blue."}]
inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
).to(model.device)

outputs = model.generate(**inputs, max_new_tokens=512)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:]))
```

Recommended base-model generation settings: `temperature=0.05`, `top_k=50`,
and `repetition_penalty=1.05`.

## LM Studio / llama.cpp

Download `LFM2.5-1.2B-Thinking-heretic-BF16.gguf` and open it in LM Studio.
This GGUF stores the model in BF16; it is a container conversion, not a reduced
bit-width quantization. It is approximately 2.34 GB.

```bash
llama-cli -m LFM2.5-1.2B-Thinking-heretic-BF16.gguf -cnv
```

The GGUF was converted with llama.cpp tag `b10603`, commit
`c060ca974c773c7c3d17fd1b66dc9d312bc292c0`, then loaded and tested in LM
Studio. A local smoke test produced approximately 95 tokens/s on the test
machine; throughput varies by hardware and runtime settings.

## Checksums

| File | SHA-256 |
|---|---|
| `model.safetensors` | `A13F650F2BD47C334C2AACB3047018B05F13485199217435854827ACD9A5263D` |
| `LFM2.5-1.2B-Thinking-heretic-BF16.gguf` | `D913B88F41696A5FF8DB3B9C8D3768B83CB870B05BC8051CAE0491C454202654` |

## Safety and limitations

Abliteration deliberately weakens refusal behavior. This may remove useful
safeguards, increase harmful compliance, or cause unexpected regressions. Do
not treat this checkpoint as safety-aligned. Evaluate it for your use case,
keep human oversight for consequential applications, and follow applicable
laws and platform policies.

The model inherits the capabilities, limitations, supported languages, and
knowledge cutoff of the base model except where the weight modification changes
them. See the [original model card](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Thinking)
for architecture and base-model details.

## License and attribution

Distributed under the **LFM Open License v1.0**, inherited from the base model.
The license includes a commercial-use revenue threshold; read `LICENSE` before
use or redistribution. Original model copyright and attribution belong to
Liquid AI, Inc. Modifications and evaluation described here were performed by
the repository author.

## References

- Liquid AI, *LFM2.5-1.2B-Thinking: On-Device Reasoning Under 1GB* (2026).
- Arditi et al., *Refusal in Language Models Is Mediated by a Single Direction*
  (2024), arXiv:2406.11717.
- [`p-e-w/heretic`](https://github.com/p-e-w/heretic).
