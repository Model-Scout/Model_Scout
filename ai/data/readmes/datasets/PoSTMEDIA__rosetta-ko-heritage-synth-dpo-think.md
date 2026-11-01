---
language:
- ko
license: apache-2.0
task_categories:
- text-generation
pretty_name: Rosetta KO Cultural Heritage Synthetic (Reasoning DPO)
size_categories:
- 10K<n<100K
tags:
- korean
- synthetic
- rosetta
- heritage
- dpo-think
- culture
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
# rosetta-ko-heritage-synth-dpo-think

Korean cultural-heritage data grounded in public heritage records — a cleaned CPT corpus plus source-grounded QA/preference/RLVR sets.

Synthetic data generated with the **Qwen3.6-27B** teacher model — part of the **Rosetta-KO** suite for the Rosetta Korean LLM (PoSTMEDIA).

## Cultural Heritage Suite

Sibling datasets from the same pipeline (each a separate repo):

| repo | format |
|---|---|
| [`rosetta-ko-heritage-synth-cpt`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-heritage-synth-cpt) | continued-pretraining corpus (plain `text`) |
| [`rosetta-ko-heritage-synth-sft`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-heritage-synth-sft) | supervised fine-tuning (user/assistant `messages`) |
| [`rosetta-ko-heritage-synth-sft-think`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-heritage-synth-sft-think) | reasoning SFT (`<think>` chain-of-thought) |
| [`rosetta-ko-heritage-synth-dpo`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-heritage-synth-dpo) | preference pairs (`chosen`/`rejected`) |
| **[`rosetta-ko-heritage-synth-dpo-think`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-heritage-synth-dpo-think)** (this repo) | reasoning preference pairs |
| [`rosetta-ko-heritage-synth-rlvr`](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-heritage-synth-rlvr) | reinforcement-learning-with-verifiable-reward rows |

## Data Fields

```json
{"id": "...", "source_dataset": "...", "domain": "heritage",
 "prompt": "...",
 "chosen":   [{"role": "assistant", "content": "..."}],
 "rejected": [{"role": "assistant", "content": "..."}]}
```
- `prompt` (string) — the Korean question
- `chosen` / `rejected` — assistant responses (each side carries `<think>` reasoning); `chosen` is the verified-correct / better-grounded answer

## Usage

```python
from datasets import load_dataset
ds = load_dataset("PoSTMEDIA/rosetta-ko-heritage-synth-dpo-think", split="train")
```

## License

Released under the **Apache License 2.0**.

Source (Korean public data, KOGL Type 1):
- Korea Heritage Service (국가유산청) — https://www.khs.go.kr
- Academy of Korean Studies — Encyclopedia of Korean Culture (한국학중앙연구원) — https://encykorea.aks.ac.kr
- National Folk Museum of Korea (국립민속박물관) — https://www.nfm.go.kr

## Citation

```bibtex
@misc{rosetta_ko_heritage_synth,
  title  = {Rosetta-KO Cultural Heritage Synthetic Dataset},
  author = {PoSTMEDIA},
  year   = {2026},
  howpublished = {Hugging Face: PoSTMEDIA/rosetta-ko-heritage-synth-dpo-think}
}
```

## Contact

PoSTMEDIA — https://huggingface.co/PoSTMEDIA

