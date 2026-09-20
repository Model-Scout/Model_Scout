---
license: apache-2.0
base_model: openai/gpt-oss-20b
tags:
- mixture-of-experts
- mxfp4
- text-generation
- pytorch
- jax
- tf
language:
  - fa
  - en
  - multilingual
pipeline_tag: text-generation
---

# 🍓 Strawberry

![from [pinterest](https://se.pinterest.com/pin/800937115014134515/)](https://i.pinimg.com/736x/b5/04/41/b50441f456e162ee3fb651898d20324a.jpg)

**Strawberry** is a fine-tuned version of [`openai/gpt-oss-20b`](https://huggingface.co/openai/gpt-oss-20b), trained to produce high-quality **Farsi (Persian) reasoning traces** and to perform **multilingual chain-of-thought reasoning**.

To the best of our knowledge, Strawberry is the **first open-source LLM in the ~20B parameter class capable of generating high-quality Farsi reasoning chains**, in addition to reasoning in English and across other languages.

## Model Details

- **Base model:** [openai/gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b) (21B parameters)
- **Architecture:** `gpt_oss`
- **Fine-tuned by:** [artindnr](https://huggingface.co/artindnr)
- **License:** Apache 2.0
- **Languages:** Farsi (Persian), English, and multilingual reasoning support
- **Model type:** Causal decoder-only language model with reasoning ("thinking") traces

## What's New

Most open reasoning models today generate their chain-of-thought almost exclusively in English, even when the final answer is requested in another language. Strawberry-1 is trained specifically to:

- Generate **coherent, high-quality reasoning traces in Farsi**, not just Farsi answers
- Reason natively across multiple languages rather than silently falling back to English
- Preserve the general instruction-following and reasoning ability of the `gpt-oss-20b` base model

## Training

Strawberry-1 was trained using a mix of fine-tuning strategies — including full fine-tuning and LoRA experiments — on top of `gpt-oss-20b`. The version released here is the **fully fine-tuned (merged, dense-weights) checkpoint**, not a LoRA adapter.

### Training Data

Strawberry-1 was trained on the [Thinking Datasets](https://huggingface.co/collections/artindnr/thinking-datasets) collection, a set of datasets purpose-built for chain-of-thought fine-tuning:

- [`artindnr/Persian-Thinking`](https://huggingface.co/datasets/artindnr/Persian-Thinking) — Farsi reasoning traces .
- [`artindnr/Persian-English-Thinking`](https://huggingface.co/datasets/artindnr/Persian-English-Thinking) — mixed Farsi/English reasoning traces
- [`artindnr/Multilingual-Thinking`](https://huggingface.co/datasets/artindnr/Multilingual-Thinking) — multilingual chain-of-thought data
- [`artindnr/Multilingual-Thinking-200`](https://huggingface.co/datasets/artindnr/Multilingual-Thinking-200) — a smaller multilingual reasoning subset

<!-- TODO: add training hardware, number of epochs, learning rate, effective batch size, and any other hyperparameters you'd like documented. -->

## How to Use

Strawberry-1 uses the `gpt-oss` chat template (Harmony format) shipped with the base model, so it works with 🤗 Transformers.

### Installation

```bash
pip install torch --index-url https://download.pytorch.org/whl/cu128
pip install "trl>=0.20.0" "peft>=0.17.0" "transformers>=4.55.0" "kernels>=0.12.0"
```

This has been verified to work with:

| Package | Version |
|---|---|
| `torch` | 2.8.0+cu129 |
| `transformers` | 5.14.1 |
| `trl` | 1.9.2 |
| `peft` | 0.20.0 |
| `accelerate` | 1.10.1 |
| `tokenizers` | 0.22.0 |

### Generation

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = "artindnr/strawberry-1"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

REASONING_LANGUAGE = "English"  # e.g. "English", "Farsi", "Persian"
SYSTEM_PROMPT = f"reasoning language: {REASONING_LANGUAGE}"
USER_PROMPT = "تو کی هستی و اسمت چیه؟"

messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": USER_PROMPT},
]

inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
).to(model.device)

outputs = model.generate(
    **inputs,
    max_new_tokens=512,
    temperature=0.6,
    do_sample=True,
)

print(tokenizer.decode(outputs[0]))
```

This prints the full Harmony-formatted output, including the `analysis` (reasoning) and `final` (answer) channels and their special tokens. To get just the plain-text final answer, decode with `skip_special_tokens=True` and parse out the `final` channel, or use `tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)` to only decode the newly generated tokens.

### Reasoning in a specific language

Set `reasoning language: <Language>` as the `system` message content to control the language of the reasoning trace (the `analysis` channel), independent of the language the user writes in. For example, setting `REASONING_LANGUAGE = "Farsi"` will produce a Farsi reasoning trace even for a prompt in another language.

Note that the model's default chat template also auto-populates a Harmony-format preamble (identity, knowledge cutoff, current date, reasoning effort, valid channels) ahead of your system/developer message — you don't need to set these yourself.

## Intended Use

Strawberry-1 is intended for:

- Research and experimentation on multilingual and Farsi-language reasoning
- Building Farsi-language assistants, tutoring tools, and reasoning-heavy applications
- General-purpose multilingual chain-of-thought tasks

## Limitations

- Farsi reasoning quality, while a focus of this fine-tune, may still occasionally mix in English tokens or phrasing, especially for highly technical topics.
- As with any fine-tune, Strawberry-1 inherits the general capabilities and limitations of the `gpt-oss-20b` base model, including the possibility of hallucinated facts and reasoning errors.
- No formal safety fine-tuning beyond what is inherited from the base model has been applied; use appropriate safeguards in production settings.

## License

This model is released under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license, consistent with the base `gpt-oss-20b` model.

## Citation

If you use Strawberry in your work, please cite:

```bibtex
@misc{strawberry1,
  title  = {Strawberry: A Farsi and Multilingual Reasoning Model Fine-tuned from GPT-OSS-20B},
  author = {artindnr},
  year   = {2026},
  url    = {https://huggingface.co/artindnr/strawberry-1}
}
```

## Acknowledgements

Built on top of [`openai/gpt-oss-20b`](https://huggingface.co/openai/gpt-oss-20b), using the [Thinking Datasets](https://huggingface.co/collections/artindnr/thinking-datasets) collection.