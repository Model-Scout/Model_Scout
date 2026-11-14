---
license: apache-2.0
base_model:
  - Qwen/Qwen3.5-4B
  - corners-ai/CoCo-Decision-4B-Ko
base_model_relation: finetune
library_name: transformers
pipeline_tag: text-classification
language:
  - en
  - ko
tags:
  - decision-model
  - calibration
  - system-one
  - decision-index
model-index:
  - name: CoCo-Decision-2.4-4B
    results:
      - task:
          type: text-classification
          name: Decision (System One)
        dataset:
          name: Jev Decision Index 0.3 (public panel, self-scored)
          type: decision-index
        metrics:
          - type: decision_index
            value: 55.19
            name: Public index (balanced skill)
---

# CoCo-Decision-2.4-4B

Released 2026-10-16. A separate repository from [corners-ai/CoCo-Decision-4B](https://huggingface.co/corners-ai/CoCo-Decision-4B) (versions 1.0.0 through 2.3.0), which stays available unchanged. The version is carried in the repository name; pin the commit revision below for reproducibility.

CoCo-Decision-2.4-4B is a 4B-class decision model. Given a situation and a typed question, it returns a probability distribution instead of free text:

| Question type | Output |
|---|---|
| `noul` | probability that a yes/no statement holds |
| `choice` | probability for each of the listed options |
| `score` | probability for each point on an ordinal scale |

It is a variant of [corners-ai/CoCo-Decision-4B](https://huggingface.co/corners-ai/CoCo-Decision-4B) 2.3.0: starting from CoCo-Decision-4B-Ko v1.0.0 merged into [Qwen/Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B) (revision `851bf6e8`), a second LoRA was trained only on the public train splits of the source datasets used by the [Jev Decision Index](https://huggingface.co/spaces/multimodalart/jev-decision-index), then merged (CoCo-Decision-4B version 1.0.0). On top of that, a third LoRA with a readout head over the option-letter tokens (versions 2.1.0 to 2.3.0) was retrained again for this version, with additional same-format decision data drawn from domains disjoint from the Decision Index evaluation items, then merged. This repository holds the merged, text-only bf16 weights (about 4.2B parameters, no vision tower), so no PEFT is needed.

If you need Korean intent classification, use CoCo-Decision-4B-Ko. This model was not trained further on Korean data, and its Korean performance has not been re-measured.

> Not affiliated with or endorsed by TypeSafe AI. "System One" and "Jev" are names used by TypeSafe AI; this model independently implements a compatible decision interface.

## How to use

Requirements: `torch`, `transformers>=5.17`, `safetensors`, `huggingface_hub`.

This version does not read the answer from the language-model head. The full-attention layers attend over the whole prompt (no causal mask; padding stays masked), and the answer is read from the last hidden state with a small linear head (`readout.safetensors`) over the option-letter tokens listed in `decision_config.json`. The snippet below reproduces this with plain `transformers`.

```python
import json

import torch
from huggingface_hub import snapshot_download
from safetensors.torch import load_file
from transformers import AutoModelForCausalLM, AutoTokenizer

REPO, REVISION = "corners-ai/CoCo-Decision-2.4-4B", "58e9b7445760834a3ad9c704985102b0b08418d9"
path = snapshot_download(REPO, revision=REVISION)
tokenizer = AutoTokenizer.from_pretrained(path)
model = AutoModelForCausalLM.from_pretrained(path, device_map="auto", dtype=torch.bfloat16).eval()
config = json.load(open(f"{path}/decision_config.json"))
table = config["readout_token_ids"]  # token ids of the option letters, one readout row each
readout = load_file(f"{path}/readout.safetensors")["proj.weight"].to(model.device, torch.float32)

# Full-attention layers read the whole prompt (no causal mask); padding stays masked.
inner = model.model
state = {}
inner.register_forward_pre_hook(lambda m, a, kw: state.update(mask=kw.get("attention_mask")), with_kwargs=True)


def open_mask(module, args, kwargs):
    hidden = args[0] if args else kwargs["hidden_states"]
    pad = state["mask"]
    if pad is None:
        pad = torch.ones(hidden.shape[:2], dtype=torch.bool, device=hidden.device)
    kwargs["attention_mask"] = pad[:, None, None, :].bool()
    return args, kwargs


for kind, layer in zip(inner.config.layer_types, inner.layers):
    if kind == "full_attention":
        layer.register_forward_pre_hook(open_mask, with_kwargs=True)


def decide(state_text: str, question: str, options: dict[str, str]) -> dict[str, float]:
    """Return a probability for each option key."""
    letters = [chr(ord("A") + i) for i in range(len(options))]
    lines = ["State:", state_text, "", f"Question: {question}", "Options:"]
    lines += [f"{letter}. {key}: {text}" for letter, (key, text) in zip(letters, options.items())]
    lines.append("Answer with the letter only.")
    prompt = tokenizer.apply_chat_template(
        [{"role": "user", "content": "\n".join(lines)}], tokenize=False, add_generation_prompt=True
    ) + "Answer:"
    ids = tokenizer(prompt, return_tensors="pt", add_special_tokens=False).to(model.device)
    with torch.no_grad():
        hidden = inner(**ids, use_cache=False).last_hidden_state[0, -1].float()
    rows = [table.index(tokenizer.encode(" " + letter, add_special_tokens=False)[0]) for letter in letters]
    probs = torch.softmax((readout @ hidden)[rows], dim=-1).tolist()
    return dict(zip(options, probs))
```

The prompt format is the same as in earlier versions: `State:`, `Question:`, `Options:` with one `<letter>. <key>: <description>` line per option, `Answer with the letter only.`, the chat template with `add_generation_prompt=True`, then `Answer:`. The probabilities are the softmax over the readout rows of the letters with a leading space.

Hardware: about 10 GB of GPU memory in bf16.

Benchmarking and side-by-side comparison with [oh-my-jev (omj)](https://github.com/iamupd/oh-my-jev), which also serves the model behind a TypeSafe-compatible endpoint:

```bash
git clone https://github.com/iamupd/oh-my-jev && cd oh-my-jev
uv sync --extra semif
uv run omj bench --model corners-ai/CoCo-Decision-2.4-4B --suite jevbench-public --view
uv run omj ui --target corners-ai/CoCo-Decision-2.4-4B --target corners-ai/CoCo-Decision-4B
```

## Evaluation

Self-scored on 2026-10-16 with the official Decision Index kit (edition 0.3), bf16, one forward pass per question, no temperature scaling. All 140,620 requests were answered with no errors. This is not an official leaderboard submission. The scored run applied the 2.4.0 LoRA adapter to the 1.0.0 weights at load time. The merged weights in this repository gave the same top choice on all 24 inputs we checked, with a maximum readout-logit difference of 0.18; the full suite was not re-run on the merged files.

| | CoCo-Decision-2.4-4B 2.4.0 | CoCo-Decision-4B 2.3.0 |
|---|---:|---:|
| Public index (balanced skill) | **55.19** | 55.38 |
| Raw index | 66.25 | 66.43 |
| Knowledge & reasoning | 35.6 | 34.8 |
| Language understanding | 62.6 | 63.2 |
| Retrieval & classification | 58.7 | 59.9 |
| Tools & automation | 77.3 | 76.8 |
| Arts & taste | 39.1 | 40.2 |

- These are self-reported public-panel figures. The leaderboard's main ranking uses the maintainers' own runs, including a private panel.
- 2.4.0 was scored on the 140,620-request kit; the 2.3.0 column is from the CoCo-Decision-4B card (same kit).

## Versions

| Version | Date | Notes |
|---|---|---|
| 2.4.0 | 2026-10-16 | Third LoRA stage retrained with additional new-domain same-format data, same structure as 2.3.0. Merged bf16 weights, text-only. Separate repository. Public index 55.19 (self-scored) |

Earlier versions (1.0.0 through 2.3.0) are in [corners-ai/CoCo-Decision-4B](https://huggingface.co/corners-ai/CoCo-Decision-4B).

## License

Apache 2.0. The base models (Qwen/Qwen3.5-4B and corners-ai/CoCo-Decision-4B-Ko) are Apache 2.0.

## Citation

```bibtex
@misc{cocodecision24b2026,
  title   = {CoCo-Decision-2.4-4B: a decision model tuned for the Jev Decision Index},
  version = {2.4.0},
  author  = {{Corners AI}},
  year    = {2026},
  url     = {https://huggingface.co/corners-ai/CoCo-Decision-2.4-4B}
}
```
