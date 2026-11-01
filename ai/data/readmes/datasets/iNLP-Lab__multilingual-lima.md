---
pretty_name: Multilingual LIMA
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
license: cc-by-nc-sa-4.0
task_categories:
- text-generation
tags:
- instruction-tuning
- multilingual
- lima
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
---

# Multilingual LIMA

A multilingual extension of the **LIMA** instruction-tuning dataset. The original English prompt–response pairs were translated into 9 additional typologically diverse languages with `google/gemini-2.0-flash-001`. Each language is stored as a separate Hugging Face **config**.

| Field | Description |
|-------|-------------|
| `prompt` | User instruction (translated; `en` is the original). |
| `output` | Assistant response (translated; `en` is the original). |

**Languages (configs):** `en` (original), `zh`, `it`, `bn`, `ko`, `th`, `vi`, `ar`, `jv`, `sw`.

## Usage

```python
from datasets import load_dataset

ds_en = load_dataset("iNLP-Lab/multilingual-lima", "en")
ds_zh = load_dataset("iNLP-Lab/multilingual-lima", "zh")
```

## Source and credits

This release re-distributes machine-translated derivatives of the original **LIMA** dataset, introduced in:

> Chunting Zhou, Pengfei Liu, Puxin Xu, Srini Iyer, Jiao Sun, Yuning Mao, Xuezhe Ma, Avia Efrat, Ping Yu, Lili Yu, Susan Zhang, Gargi Ghosh, Mike Lewis, Luke Zettlemoyer, Omer Levy. **"LIMA: Less Is More for Alignment."** *NeurIPS 2023.* [arXiv:2305.11206](https://arxiv.org/abs/2305.11206)

The original English data is hosted at [`GAIR/lima`](https://huggingface.co/datasets/GAIR/lima). All credit for the underlying prompt–response pairs belongs to the authors above; this release only contributes the multilingual translations.

```bibtex
@inproceedings{zhou2023lima,
  title     = {{LIMA}: Less Is More for Alignment},
  author    = {Zhou, Chunting and Liu, Pengfei and Xu, Puxin and Iyer, Srini and Sun, Jiao and Mao, Yuning and Ma, Xuezhe and Efrat, Avia and Yu, Ping and Yu, Lili and Zhang, Susan and Ghosh, Gargi and Lewis, Mike and Zettlemoyer, Luke and Levy, Omer},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  year      = {2023}
}
```

## License

Following the upstream LIMA license, this dataset is released under **CC BY-NC-SA 4.0**. If any source item in LIMA has a stricter license, that stricter license applies to the corresponding row here.
