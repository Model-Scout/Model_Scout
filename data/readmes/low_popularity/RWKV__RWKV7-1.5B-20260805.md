---
library_name: transformers
pipeline_tag: text-generation
license: apache-2.0
language:
  - "en"
  - "zh"
  - "fr"
  - "es"
  - "de"
  - "pt"
  - "ru"
  - "it"
  - "ja"
  - "ko"
  - "vi"
  - "ar"
datasets:
  - "HuggingFaceFW/fineweb-edu"
  - "mlfoundations/dclm-baseline-1.0"
  - "cerebras/SlimPajama-627B"
  - "EleutherAI/pile"
  - "bigcode/starcoderdata"
  - "oscar-corpus/OSCAR-2301"
tags:
  - rwkv
  - rwkv7
  - recurrent
  - causal-lm
  - conversational
---

<!-- markdownlint-disable first-line-h1 -->
<!-- markdownlint-disable html -->

<div align="center">
  <a href="https://www.rwkv.com/">
    <img src="https://www.rwkv.com/images/avatar.png" width="140" alt="RWKV logo" />
  </a>
  <h1>RWKV7-1.5B-20260805</h1>
  <p><strong>RWKV-7 “Goose” · constant-state recurrent language modeling</strong></p>
</div>

<div align="center">
  <a href="https://www.rwkv.com/"><img alt="Website" src="https://img.shields.io/badge/Website-RWKV-16a7c9" /></a>
  <a href="https://huggingface.co/BlinkDL"><img alt="Hugging Face" src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-BlinkDL-ffc107" /></a>
  <a href="https://github.com/BlinkDL/RWKV-LM"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-RWKV--LM-181717?logo=github" /></a>
  <a href="https://arxiv.org/abs/2503.14456v2"><img alt="RWKV-7 paper" src="https://img.shields.io/badge/Paper-arXiv%3A2503.14456-b31b1b" /></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/License-apache--2.0-4c8bf5" /></a>
</div>

---

## Model introduction

This is an official BlinkDL release of **RWKV-7 Goose** in Hugging Face
Transformers format. RWKV-7 is an attention-free recurrent architecture with a
constant-size recurrent state and constant inference work per generated token.
Training remains parallelizable.

This checkpoint is a **base model** pretrained with web, code, synthetic, instruction, chat, and reasoning data. It is suitable for evaluation, post-training, and fine-tuning; the included chat template is a prompt interface, not a claim that the checkpoint is a safety-aligned assistant.

The Transformers integration, conversion, release packaging, Fast Tokenizer, and
optional TileLang inference implementation are distributed with this release.

## Highlights

- **Constant recurrent state:** memory does not grow like an attention KV cache.
- **Native Transformers layout:** standard config, sharded safetensors, generation,
  recurrent cache continuation, training, and LoRA workflows.
- **Exact Fast Tokenizer:** self-contained Rust-backed `tokenizer.json`, generated
  from the canonical RWKV World byte vocabulary during conversion.
- **Chat-ready:** `chat_template.jinja` supports system, multi-turn, thinking, and
  strict model-generated tool-call prompts.
- **Optional optimized runtime:** the isolated [`inference/`](inference/) bundle
  provides PyTorch fallback and TileLang acceleration without changing the
  standard model root.

## Model overview

| Field | Value |
| --- | --- |
| Repository | `RWKV/RWKV7-1.5B-20260805` |
| Architecture class | `Rwkv7ForCausalLM` |
| Public size label | `1.5`B |
| Source parameters | `1,527,668,736` |
| Serialized parameters | `1,527,668,736` |
| Synthesized compatibility tensors | `0` |
| Layers | `24` |
| Hidden / FFN size | `2048` / `8192` |
| Heads / head size | `32` / `64` |
| Vocabulary | `65536` |
| Training context | `16384 tokens` |
| Weight dtype | `bfloat16` |
| Numerical conversion | `source dtype preserved` |
| Metadata profile | `g1i` |
| Metadata provenance | `locked-profile` |
| Source checkpoint | [`BlinkDL/rwkv7-g1/rwkv7-g1i-1.5b-20260805-ctx16384.pth`](https://huggingface.co/BlinkDL/rwkv7-g1/blob/ede85bf8ab2e59aff7d7ca909fbbc73317866d89/rwkv7-g1i-1.5b-20260805-ctx16384.pth) |
| Source SHA-256 | `32ef7b5bf4dc8bde843cf26dfad809a1f527e2e76a9e790e7d406e71bcd785da` |

## Transformers quickstart

Native `rwkv7` auto-class registration requires Transformers 5.15 or a current
source checkout until that release is available.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "RWKV/RWKV7-1.5B-20260805"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, dtype=torch.bfloat16)
```

The recurrent cache returned by the model can be passed back for incremental
decoding. Use an `attention_mask` for padded batches.

## Chat quickstart

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "RWKV/RWKV7-1.5B-20260805"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    dtype=torch.bfloat16,
).to("cuda")

messages = [{"role": "user", "content": "Explain why RWKV uses constant state."}]
input_ids = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    thinking=False,
    return_tensors="pt",
).to(model.device)

output = model.generate(
    input_ids,
    max_new_tokens=256,
    do_sample=True,
    temperature=1.0,
    top_p=0.5,
    eos_token_id=0,
    pad_token_id=0,
)
print(tokenizer.decode(output[0, input_ids.shape[1]:], skip_special_tokens=True))
```

Set `thinking=True` for the RWKV thinking prefix. The intentional generation
prefixes are `Assistant: <think></think` and `Assistant: <think`; do not append a
closing `>` to them. Reference stops are token ID `0` and `\n\nUser:`.

Strip trailing spaces from user input. The official RWKV prompt guide is available
in [`RWKV7-G1x-templates.txt`](https://github.com/BlinkDL/RWKV-LM/blob/main/RWKV-v7/RWKV7-G1x-templates.txt).

## Optimized local inference

Install the versions listed in `inference/requirements.txt`, then run the bundled
interactive chat:

```bash
python inference/generate.py --model RWKV/RWKV7-1.5B-20260805 --backend auto --interactive
```

Or independent prompts separated by blank lines:

```bash
python inference/generate.py \
  --model RWKV/RWKV7-1.5B-20260805 \
  --backend auto \
  --input-file prompts.txt
```

`--backend auto` uses validated exact optimized boundaries and otherwise falls
back to PyTorch. Full explicit TileLang execution can change floating-point
operation order and requires checkpoint-, dtype-, shape-, and device-specific
parity validation.

## Tokenizer

The model root contains one self-contained tokenizer artifact: `tokenizer.json`.
Textual `vocab.json` and `rwkv_vocab_v20230424.txt` files are intentionally omitted
because they would duplicate the tokenizer used by Transformers.

## Intended use and limitations

- This is a base causal language model. Quality, instruction following, and
  language behavior depend on the checkpoint and downstream prompting or
  post-training.
- Assisted or speculative decoding that requires recurrent-cache rollback is not
  supported without retaining prior state snapshots.
- Optimized support depends on GPU architecture, dtype, batch, and shape.
  Unsupported `auto` configurations fall back to pure PyTorch.
- Explicit full TileLang execution can change floating-point operation order and
  requires checkpoint-, dtype-, shape-, and device-specific parity validation.
- No safety, bias, toxicity, factuality, or high-stakes-use evaluation is claimed
  by this model card.

## License and provenance

The model weights use the locked profile license `apache-2.0`. The exported inference bundle is licensed separately under [Apache-2.0](LICENSE). See [`NOTICE`](NOTICE) and the source checkpoint link above for
provenance.

## Citation

```bibtex
@misc{peng2025250314456,
  title         = {RWKV-7 "Goose" with Expressive Dynamic State Evolution},
  author        = {Bo Peng and Ruichong Zhang and Daniel Goldstein and Eric Alcaide and Xingjian Du and Haowen Hou and Jiaju Lin and Jiaxing Liu and Janna Lu and William Merrill and Guangyu Song and Kaifeng Tan and Saiteja Utpala and Nathan Wilce and Johan S. Wind and Tianyi Wu and Daniel Wuttke and Christian Zhou-Zheng},
  year          = {2025},
  eprint        = {2503.14456v2},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  url           = {https://arxiv.org/abs/2503.14456v2},
}
```
