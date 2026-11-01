---
language:
- ko
license: apache-2.0
task_categories:
- text-generation
pretty_name: Rosetta KO Code Synthetic (Reasoning DPO)
size_categories:
- 10K<n<100K
tags:
- korean
- synthetic
- rosetta
- code
- dpo-think
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
# rosetta-ko-code-synth-dpo-think

Korean-native coding data — problems with solutions whose unit tests were actually executed and passed (execution-grounded rejection sampling).

Synthetic data generated with the **Qwen3.6-27B** teacher model — part of the **Rosetta-KO** suite for the Rosetta Korean LLM (PoSTMEDIA).

## Code Suite

Sibling datasets from the same pipeline (each a separate repo):

| repo | format |
|---|---|
| [`rosetta-ko-code-synth-sft`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-code-synth-sft) | supervised fine-tuning (user/assistant `messages`) |
| [`rosetta-ko-code-synth-sft-think`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-code-synth-sft-think) | reasoning SFT (`<think>` chain-of-thought) |
| [`rosetta-ko-code-synth-dpo`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-code-synth-dpo) | preference pairs (`chosen`/`rejected`) |
| **[`rosetta-ko-code-synth-dpo-think`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-code-synth-dpo-think)** (this repo) | reasoning preference pairs |
| [`rosetta-ko-code-synth-rlvr`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-code-synth-rlvr) | reinforcement-learning-with-verifiable-reward rows |

## Data Fields

```json
{"id": "...", "source_dataset": "...", "domain": "code",
 "prompt": "...",
 "chosen":   [{"role": "assistant", "content": "..."}],
 "rejected": [{"role": "assistant", "content": "..."}]}
```
- `prompt` (string) — the Korean question
- `chosen` / `rejected` — assistant responses (each side carries `<think>` reasoning); `chosen` is the verified-correct / better-grounded answer

## Usage

```python
from datasets import load_dataset
ds = load_dataset("PoSTMEDIA/rosetta-ko-code-synth-dpo-think", split="train")
```

## License

Released under the **Apache License 2.0**.

Seed sources:
- [nvidia/OpenCodeInstruct](https://huggingface.co/datasets/nvidia/OpenCodeInstruct)
- [google-research-datasets/mbpp](https://huggingface.co/datasets/google-research-datasets/mbpp)

## Citation

```bibtex
@misc{rosetta_ko_code_synth,
  title  = {Rosetta-KO Code Synthetic Dataset},
  author = {PoSTMEDIA},
  year   = {2026},
  howpublished = {Hugging Face: PoSTMEDIA/rosetta-ko-code-synth-dpo-think}
}
```

## Contact

PoSTMEDIA — https://huggingface.co/PoSTMEDIA

