---
language:
- ko
license: apache-2.0
task_categories:
- text-generation
pretty_name: Rosetta KO Chat Synthetic (RLVR)
size_categories:
- 100K<n<1M
tags:
- korean
- synthetic
- rosetta
- general
- rlvr
- chat
- conversational
extra_gated_prompt: >-
  By clicking "Agree" I confirm I have read and agree to the PoSTMEDIA Data Agreement
  for Model Training and agree that I intend to use this data for model training
  purposes only.
extra_gated_fields:
  Company: text
  Institutional Email: text
  Intended use: text
  I agree to use this dataset for model training purposes ONLY: checkbox
configs:
- config_name: default
  data_files:
  - split: train
    path: train.jsonl
---
# rosetta-ko-chat-synth-rlvr

Korean-native general-purpose conversational data — diverse everyday instructions with natural Korean answers.

Synthetic data generated with the **Qwen3.6-27B** teacher model — part of the **Rosetta-KO** suite for the Rosetta Korean LLM (PoSTMEDIA).

## Chat Suite

Sibling datasets from the same pipeline (each a separate repo):

| repo | format |
|---|---|
| [`rosetta-ko-chat-synth-sft`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-chat-synth-sft) | supervised fine-tuning (user/assistant `messages`) |
| [`rosetta-ko-chat-synth-sft-think`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-chat-synth-sft-think) | reasoning SFT (`<think>` chain-of-thought) |
| **[`rosetta-ko-chat-synth-rlvr`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-chat-synth-rlvr)** (this repo) | reinforcement-learning-with-verifiable-reward rows |

## Data Fields

```json
{"id": "...", "source_dataset": "...", "domain": "general",
 "messages": [{"role": "user", "content": "..."}],
 "dataset": "...", "ground_truth": "..."}
```
- `messages` — user turn only (the problem); no assistant turn by design
- `dataset` — verifier family tag
- `ground_truth` — verifiable reference the reward function checks against

## Usage

```python
from datasets import load_dataset
ds = load_dataset("PoSTMEDIA/rosetta-ko-chat-synth-rlvr", split="train")
```

## License

Released under the **Apache License 2.0**.

Seed sources:
- [maywell/koVast](https://huggingface.co/datasets/maywell/koVast)

## Citation

```bibtex
@misc{rosetta_ko_general_synth,
  title  = {Rosetta-KO Chat Synthetic Dataset},
  author = {PoSTMEDIA},
  year   = {2026},
  howpublished = {Hugging Face: PoSTMEDIA/rosetta-ko-chat-synth-rlvr}
}
```

## Contact

PoSTMEDIA — https://huggingface.co/PoSTMEDIA

