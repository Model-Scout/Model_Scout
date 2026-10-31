---
pretty_name: Multilingual Safety Instructions
language:
- en
- zh
- it
- bn
- ko
- th
- vi
- ar
- jv
- sw
- de
- fr
license: cc-by-nc-4.0
task_categories:
- text-generation
tags:
- safety
- alignment
- refusal
- multilingual
configs:
- config_name: en
  data_files: en.csv
- config_name: zh
  data_files: zh.csv
- config_name: it
  data_files: it.csv
- config_name: bn
  data_files: bn.csv
- config_name: ko
  data_files: ko.csv
- config_name: th
  data_files: th.csv
- config_name: vi
  data_files: vi.csv
- config_name: ar
  data_files: ar.csv
- config_name: jv
  data_files: jv.csv
- config_name: sw
  data_files: sw.csv
- config_name: de
  data_files: de.csv
- config_name: fr
  data_files: fr.csv
---

# Multilingual Safety Instructions

A multilingual extension of the **safety-only instruction–refusal pairs** released with the Safety-Tuned LLaMAs project. The original 1,000 harmful-prompt / refusal-response pairs (English) were translated into 11 additional typologically diverse languages with `google/gemini-2.0-flash-001`. Each language is stored as a separate Hugging Face **config**.

| Field | Description |
|-------|-------------|
| `prompt` | Harmful user instruction (translated; `en` is the original). |
| `output` | Safe refusal / corrective response (translated; `en` is the original). |

**Languages (configs):** `en` (original), `zh`, `it`, `bn`, `ko`, `th`, `vi`, `ar`, `jv`, `sw`, `de`, `fr`.

## Intended use

This dataset is intended for **alignment research**: probing refusal behaviour in language models, building multilingual safety calibration corpora (e.g. detecting refusal-specific neurons), and evaluating cross-lingual safety transfer. The `prompt` field contains content that may be offensive, harmful, or unsafe — it is published deliberately so that models can be trained or analysed to **refuse** such queries.

## Usage

```python
from datasets import load_dataset

ds_en = load_dataset("iNLP-Lab/multilingual-safety", "en")
ds_zh = load_dataset("iNLP-Lab/multilingual-safety", "zh")
```

## Source and credits

This release re-distributes machine-translated derivatives of the `safety_only_data_Instructions.json` split from the **Safety-Tuned LLaMAs** project:

> Federico Bianchi, Mirac Suzgun, Giuseppe Attanasio, Paul Röttger, Dan Jurafsky, Tatsunori Hashimoto, James Zou. **"Safety-Tuned LLaMAs: Lessons From Improving the Safety of Large Language Models that Follow Instructions."** *ICLR 2024.* [arXiv:2309.07875](https://arxiv.org/abs/2309.07875)

The original English data is hosted at [`vinid/safety-tuned-llamas`](https://github.com/vinid/safety-tuned-llamas) (file `data/training/safety_only_data_Instructions.json`). All credit for the underlying instruction–refusal pairs belongs to the authors above; this release only contributes the multilingual translations.

```bibtex
@inproceedings{bianchi2024safetytuned,
  title     = {Safety-Tuned {LL}a{MA}s: Lessons From Improving the Safety of Large Language Models that Follow Instructions},
  author    = {Bianchi, Federico and Suzgun, Mirac and Attanasio, Giuseppe and R{\"o}ttger, Paul and Jurafsky, Dan and Hashimoto, Tatsunori and Zou, James},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2024}
}
```

## License

Released under **CC BY-NC 4.0**, matching the non-commercial research intent of the upstream Safety-Tuned LLaMAs release.
