---
language:
- ko
license: apache-2.0
task_categories:
- text-generation
pretty_name: Rosetta KO Tourism Synthetic (RLVR)
size_categories:
- 10K<n<100K
tags:
- korean
- synthetic
- rosetta
- tourism
- rlvr
- travel
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
# rosetta-ko-tourism-synth-rlvr

Korean tourism-domain data grounded in public tourism records — a cleaned CPT corpus plus source-grounded QA/preference/RLVR sets.

Synthetic data generated with the **Qwen3.6-27B** teacher model — part of the **Rosetta-KO** suite for the Rosetta Korean LLM (PoSTMEDIA).

## Tourism Suite

Sibling datasets from the same pipeline (each a separate repo):

| repo | format |
|---|---|
| [`rosetta-ko-tourism-synth-cpt`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-tourism-synth-cpt) | continued-pretraining corpus (plain `text`) |
| [`rosetta-ko-tourism-synth-sft`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-tourism-synth-sft) | supervised fine-tuning (user/assistant `messages`) |
| [`rosetta-ko-tourism-synth-sft-think`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-tourism-synth-sft-think) | reasoning SFT (`<think>` chain-of-thought) |
| [`rosetta-ko-tourism-synth-dpo`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-tourism-synth-dpo) | preference pairs (`chosen`/`rejected`) |
| [`rosetta-ko-tourism-synth-dpo-think`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-tourism-synth-dpo-think) | reasoning preference pairs |
| **[`rosetta-ko-tourism-synth-rlvr`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-tourism-synth-rlvr)** (this repo) | reinforcement-learning-with-verifiable-reward rows |

## Data Fields

```json
{"id": "...", "source_dataset": "...", "domain": "tourism",
 "messages": [{"role": "user", "content": "..."}],
 "dataset": "...", "ground_truth": "..."}
```
- `messages` — user turn only (the problem); no assistant turn by design
- `dataset` — verifier family tag
- `ground_truth` — verifiable reference the reward function checks against

## Usage

```python
from datasets import load_dataset
ds = load_dataset("PoSTMEDIA/rosetta-ko-tourism-synth-rlvr", split="train")
```

## License

Released under the **Apache License 2.0**.

Source (Korean public data, KOGL Type 1):
- Korea Tourism Organization — TourAPI / VisitKorea (한국관광공사) — https://api.visitkorea.or.kr

## Citation

```bibtex
@misc{rosetta_ko_tourism_synth,
  title  = {Rosetta-KO Tourism Synthetic Dataset},
  author = {PoSTMEDIA},
  year   = {2026},
  howpublished = {Hugging Face: PoSTMEDIA/rosetta-ko-tourism-synth-rlvr}
}
```

## Contact

PoSTMEDIA — https://huggingface.co/PoSTMEDIA

