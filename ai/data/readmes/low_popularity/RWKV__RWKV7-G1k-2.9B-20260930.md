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
    <img src="./assets/rwkv-logo.webp" width="140" alt="RWKV logo" />
  </a>
  <h1>RWKV7-G1k-2.9B-20260930</h1>
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

The Transformers integration, conversion, release packaging, linear-time RWKV
tokenizer, and
optional TileLang inference implementation are distributed with this release.

## Highlights

- **Constant recurrent state:** memory does not grow like an attention KV cache.
- **Bundled Transformers integration:** auditable remote configuration and modeling
  modules provide generation, recurrent cache continuation, training, and LoRA
  workflows on Transformers 5.15+.
- **Exact linear-time tokenizer:** the bundled RWKV trie reads the self-contained
  `tokenizer.json` generated from the canonical RWKV World byte vocabulary.
- **Chat-ready:** `chat_template.jinja` supports system, multi-turn, thinking, and
  strict model-generated tool-call prompts.
- **Optional optimized runtime:** the isolated [`inference/`](inference/) bundle
  provides PyTorch fallback and TileLang acceleration without changing the
  standard model root.

## Model overview

| Field | Value |
| --- | --- |
| Repository | `RWKV/RWKV7-G1k-2.9B-20260930` |
| Architecture class | `Rwkv7ForCausalLM` |
| Public size label | `2.9B` |
| Source parameters | `2,948,065,280` |
| Serialized parameters | `2,948,065,280` |
| Synthesized compatibility tensors | `0` |
| Layers | `32` |
| Hidden / FFN size | `2560` / `10240` |
| Heads / head size | `40` / `64` |
| Vocabulary | `65536` |
| Training context | `25600 tokens` |
| Weight dtype | `bfloat16` |
| Numerical conversion | `source dtype preserved` |
| Metadata profile | `g1k` |
| Metadata provenance | `locked-profile` |
| Source checkpoint | [`BlinkDL/rwkv7-g1/rwkv7-g1k-2.9b-20260930-ctx25600.pth`](https://huggingface.co/BlinkDL/rwkv7-g1/blob/a1ddf9e96df23d5d7db65137ad83a4701044cd05/rwkv7-g1k-2.9b-20260930-ctx25600.pth) |
| Source SHA-256 | `d8f8ecd4af8d706f867ac8a74284f35c0e3b9f863e7b09bb4d4031480c8b28b2` |

## Transformers quickstart

The repository includes `configuration_rwkv7.py`, `modeling_rwkv7.py`, and the
exact linear-time `tokenization_rwkv7.py`. The model modules are adapted
from the Transformers RWKV-7 integration at commit
[`4ad9ed0`](https://github.com/huggingface/transformers/commit/4ad9ed0747ed6ba75c787e8f9040dcd64b166ee2).
Review those files and pin a model-repository revision in production. Passing
`trust_remote_code=True` selects this bundled implementation even when the local
Transformers installation also provides native RWKV-7 support.

```python
import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
)

model_id = "RWKV/RWKV7-G1k-2.9B-20260930"
tokenizer = AutoTokenizer.from_pretrained(
    model_id,
    trust_remote_code=True,
)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    trust_remote_code=True,
    dtype=torch.bfloat16,
)
```

The recurrent cache returned by the model can be passed back for incremental
decoding. Use an `attention_mask` for padded batches.

The model defaults to the chunk-parallel WKV path for efficient multi-token
prefill. To reproduce the portable token-order reference path, set
`model.config.wkv_implementation = "eager"` before the first forward pass.
Chunked execution changes floating-point operation order, so small numerical
differences from eager execution are expected.

## Chat quickstart

```python
import re

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


THINK_RE = re.compile(r"\A<think>?\s*(.*?)\s*</think>?", re.DOTALL)


def assistant_content(completion, thinking, *, close_incomplete=False):
    prefix = "<think" if thinking else "<think></think>\n"
    reply = prefix + completion
    thinking_block = THINK_RE.match(reply)
    if thinking:
        if thinking_block is not None or not close_incomplete:
            return reply.strip()
        return f"{reply.rstrip()}\n</think>".strip()
    return "" if thinking_block is None else reply[thinking_block.end():].strip()

model_id = "RWKV/RWKV7-G1k-2.9B-20260930"
tokenizer = AutoTokenizer.from_pretrained(
    model_id,
    trust_remote_code=True,
)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    trust_remote_code=True,
    dtype=torch.bfloat16,
).to("cuda")

messages = [{"role": "user", "content": "Explain why RWKV uses constant state."}]
thinking = False
max_new_tokens = 256
inputs = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    thinking=thinking,
    return_dict=True,
    return_tensors="pt",
).to(model.device)

output = model.generate(
    **inputs,
    max_new_tokens=max_new_tokens,
    do_sample=True,
    temperature=1.0,
    top_p=0.5,
    eos_token_id=0,
    pad_token_id=0,
    stop_strings=["\n\nUser:"],
    tokenizer=tokenizer,
)
completion = tokenizer.decode(
    output[0, inputs["input_ids"].shape[1]:],
    skip_special_tokens=True,
)
completion = completion.split("\n\nUser:", 1)[0]
reached_token_limit = output.shape[1] - inputs["input_ids"].shape[1] >= max_new_tokens
print(
    assistant_content(
        completion,
        thinking,
        close_incomplete=reached_token_limit,
    )
)
```

Set `thinking=True` for the RWKV thinking prefix. The intentional generation
prefixes are `Assistant: <think></think>` followed by a newline and
`Assistant: <think`. Only the enabled thinking prefix intentionally leaves its opening
tag incomplete. The post-processing above reconstructs that prefix before removing an
empty thinking block or preserving an enabled one. If generation hits the token limit
inside thinking, it closes the displayed block before returning it.
Reference stops are token ID `0` and `\n\nUser:`.

Strip trailing spaces from user input. The official RWKV prompt guide is available
in [`RWKV7-G1x-templates.txt`](https://github.com/BlinkDL/RWKV-LM/blob/main/RWKV-v7/RWKV7-G1x-templates.txt).

## Supervised fine-tuning

The bundled model supports TRL 1.10+ `SFTTrainer`, including its default
`chunked_nll`, gradient checkpointing, assistant-only loss, BFD packing, and PEFT
LoRA. Packing boundaries carried as reset `position_ids` are converted into RWKV
recurrent-state boundaries. Do not use the boundary-destroying `wrapped` packing
strategy.

```python
from datasets import load_dataset
from peft import LoraConfig
from trl import SFTConfig, SFTTrainer

# Reuse `model` and `tokenizer` loaded in the Transformers quickstart above.
dataset = load_dataset("trl-lib/Capybara", split="train")
trainer = SFTTrainer(
    model=model,
    processing_class=tokenizer,
    train_dataset=dataset,
    args=SFTConfig(
        output_dir="rwkv7-sft",
        max_length=2048,
        packing=True,
        packing_strategy="bfd",
        assistant_only_loss=True,
        use_cache=False,
        gradient_checkpointing=True,
    ),
    peft_config=LoraConfig(
        task_type="CAUSAL_LM",
        r=8,
        lora_alpha=16,
        target_modules=["receptance", "key", "value", "output"],
    ),
)
trainer.train()
```

## Optimized local inference

Install the versions listed in `inference/requirements.txt`, then run the bundled
interactive chat:

```bash
python inference/generate.py --model RWKV/RWKV7-G1k-2.9B-20260930 --backend auto --interactive
```

Or independent prompts separated by blank lines:

```bash
python inference/generate.py \
  --model RWKV/RWKV7-G1k-2.9B-20260930 \
  --backend auto \
  --input-file prompts.txt
```

`--backend auto` uses validated exact optimized boundaries and otherwise falls
back to PyTorch. Full explicit TileLang execution can change floating-point
operation order and requires checkpoint-, dtype-, shape-, and device-specific
parity validation.

## Tokenizer

The model root contains one self-contained tokenizer-data artifact: `tokenizer.json`.
Textual `vocab.json` and `rwkv_vocab_v20230424.txt` files are intentionally omitted
because they would duplicate the tokenizer used by Transformers. The tokenizer is
loaded by the bundled `Rwkv7Tokenizer` trie through `AutoTokenizer` with
`trust_remote_code=True`. The trie reads only `tokenizer.json`, preserves exact
RWKV World IDs, and has bounded linear-time behavior on long repetitive inputs.

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

The model weights use the locked profile license `apache-2.0`. The exported inference bundle is licensed separately under [Apache-2.0](LICENSE). The bundled Transformers configuration and modeling modules
retain their Apache-2.0 headers. See [`NOTICE`](NOTICE) and the source checkpoint
link above for provenance.

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
