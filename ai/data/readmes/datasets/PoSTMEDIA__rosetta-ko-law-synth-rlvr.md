---
language:
- ko
license: apache-2.0
task_categories:
- text-generation
pretty_name: Rosetta KO Law Synthetic (RLVR)
size_categories:
- 100K<n<1M
tags:
- korean
- synthetic
- rosetta
- law
- rlvr
- legal
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
# rosetta-ko-law-synth-rlvr

Korean legal-domain data grounded in national statutes — a cleaned CPT corpus plus source-grounded QA/preference/RLVR sets.

Synthetic data generated with the **Qwen3.6-27B** teacher model — part of the **Rosetta-KO** suite for the Rosetta Korean LLM (PoSTMEDIA).

## Law Suite

Sibling datasets from the same pipeline (each a separate repo):

| repo | format |
|---|---|
| [`rosetta-ko-law-synth-cpt`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-law-synth-cpt) | continued-pretraining corpus (plain `text`) |
| [`rosetta-ko-law-synth-sft`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-law-synth-sft) | supervised fine-tuning (user/assistant `messages`) |
| [`rosetta-ko-law-synth-sft-think`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-law-synth-sft-think) | reasoning SFT (`<think>` chain-of-thought) |
| [`rosetta-ko-law-synth-dpo`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-law-synth-dpo) | preference pairs (`chosen`/`rejected`) |
| **[`rosetta-ko-law-synth-rlvr`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-law-synth-rlvr)** (this repo) | reinforcement-learning-with-verifiable-reward rows |

## Data Fields

```json
{"id": "...", "source_dataset": "...", "domain": "law",
 "messages": [{"role": "user", "content": "..."}],
 "dataset": "...", "ground_truth": "..."}
```
- `messages` — user turn only (the problem); no assistant turn by design
- `dataset` — verifier family tag
- `ground_truth` — verifiable reference the reward function checks against

## Usage

```python
from datasets import load_dataset
ds = load_dataset("PoSTMEDIA/rosetta-ko-law-synth-rlvr", split="train")
```

## License

Released under the **Apache License 2.0**.

Source (Korean public data, KOGL Type 1):
- National Law Information Center (법제처 국가법령정보센터) — https://www.law.go.kr

## Citation

```bibtex
@misc{rosetta_ko_law_synth,
  title  = {Rosetta-KO Law Synthetic Dataset},
  author = {PoSTMEDIA},
  year   = {2026},
  howpublished = {Hugging Face: PoSTMEDIA/rosetta-ko-law-synth-rlvr}
}
```

## Contact

PoSTMEDIA — https://huggingface.co/PoSTMEDIA

