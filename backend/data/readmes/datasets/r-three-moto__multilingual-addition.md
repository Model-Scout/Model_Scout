---
license: mit
pretty_name: Multilingual Addition
language:
- en
- da
- sv
- vi
- hu
- fa
- tr
- cs
- ar
- el
- id
- nl
- pl
- pt
- it
- ja
- fr
- es
- de
- zh
- ru
- 'no'
- fi
- bn
- ko
language_bcp47:
- pt-BR
task_categories:
- question-answering
tags:
- arithmetic
- addition
- multilingual
- synthetic
- tokenization
- moto
configs:
- config_name: default
  data_files:
  - split: train
    path: data/*/train.chunk.*.jsonl
  - split: val
    path: data/*/val.chunk.*.jsonl
  default: true
- config_name: eng_Latn
  data_files:
  - split: train
    path: data/eng_Latn/train.chunk.*.jsonl
  - split: val
    path: data/eng_Latn/val.chunk.*.jsonl
- config_name: dan_Latn
  data_files:
  - split: train
    path: data/dan_Latn/train.chunk.*.jsonl
  - split: val
    path: data/dan_Latn/val.chunk.*.jsonl
- config_name: swe_Latn
  data_files:
  - split: train
    path: data/swe_Latn/train.chunk.*.jsonl
  - split: val
    path: data/swe_Latn/val.chunk.*.jsonl
- config_name: vie_Latn
  data_files:
  - split: train
    path: data/vie_Latn/train.chunk.*.jsonl
  - split: val
    path: data/vie_Latn/val.chunk.*.jsonl
- config_name: hun_Latn
  data_files:
  - split: train
    path: data/hun_Latn/train.chunk.*.jsonl
  - split: val
    path: data/hun_Latn/val.chunk.*.jsonl
- config_name: fas_Arab
  data_files:
  - split: train
    path: data/fas_Arab/train.chunk.*.jsonl
  - split: val
    path: data/fas_Arab/val.chunk.*.jsonl
- config_name: tur_Latn
  data_files:
  - split: train
    path: data/tur_Latn/train.chunk.*.jsonl
  - split: val
    path: data/tur_Latn/val.chunk.*.jsonl
- config_name: ces_Latn
  data_files:
  - split: train
    path: data/ces_Latn/train.chunk.*.jsonl
  - split: val
    path: data/ces_Latn/val.chunk.*.jsonl
- config_name: arb_Arab
  data_files:
  - split: train
    path: data/arb_Arab/train.chunk.*.jsonl
  - split: val
    path: data/arb_Arab/val.chunk.*.jsonl
- config_name: ell_Grek
  data_files:
  - split: train
    path: data/ell_Grek/train.chunk.*.jsonl
  - split: val
    path: data/ell_Grek/val.chunk.*.jsonl
- config_name: ind_Latn
  data_files:
  - split: train
    path: data/ind_Latn/train.chunk.*.jsonl
  - split: val
    path: data/ind_Latn/val.chunk.*.jsonl
- config_name: nld_Latn
  data_files:
  - split: train
    path: data/nld_Latn/train.chunk.*.jsonl
  - split: val
    path: data/nld_Latn/val.chunk.*.jsonl
- config_name: pol_Latn
  data_files:
  - split: train
    path: data/pol_Latn/train.chunk.*.jsonl
  - split: val
    path: data/pol_Latn/val.chunk.*.jsonl
- config_name: por_Latn
  data_files:
  - split: train
    path: data/por_Latn/train.chunk.*.jsonl
  - split: val
    path: data/por_Latn/val.chunk.*.jsonl
- config_name: ita_Latn
  data_files:
  - split: train
    path: data/ita_Latn/train.chunk.*.jsonl
  - split: val
    path: data/ita_Latn/val.chunk.*.jsonl
- config_name: jpn_Jpan
  data_files:
  - split: train
    path: data/jpn_Jpan/train.chunk.*.jsonl
  - split: val
    path: data/jpn_Jpan/val.chunk.*.jsonl
- config_name: fra_Latn
  data_files:
  - split: train
    path: data/fra_Latn/train.chunk.*.jsonl
  - split: val
    path: data/fra_Latn/val.chunk.*.jsonl
- config_name: spa_Latn
  data_files:
  - split: train
    path: data/spa_Latn/train.chunk.*.jsonl
  - split: val
    path: data/spa_Latn/val.chunk.*.jsonl
- config_name: deu_Latn
  data_files:
  - split: train
    path: data/deu_Latn/train.chunk.*.jsonl
  - split: val
    path: data/deu_Latn/val.chunk.*.jsonl
- config_name: cmn_Hani
  data_files:
  - split: train
    path: data/cmn_Hani/train.chunk.*.jsonl
  - split: val
    path: data/cmn_Hani/val.chunk.*.jsonl
- config_name: rus_Cyrl
  data_files:
  - split: train
    path: data/rus_Cyrl/train.chunk.*.jsonl
  - split: val
    path: data/rus_Cyrl/val.chunk.*.jsonl
- config_name: nob_Latn
  data_files:
  - split: train
    path: data/nob_Latn/train.chunk.*.jsonl
  - split: val
    path: data/nob_Latn/val.chunk.*.jsonl
- config_name: fin_Latn
  data_files:
  - split: train
    path: data/fin_Latn/train.chunk.*.jsonl
  - split: val
    path: data/fin_Latn/val.chunk.*.jsonl
- config_name: ben_Beng
  data_files:
  - split: train
    path: data/ben_Beng/train.chunk.*.jsonl
  - split: val
    path: data/ben_Beng/val.chunk.*.jsonl
- config_name: kor_Hang
  data_files:
  - split: train
    path: data/kor_Hang/train.chunk.*.jsonl
  - split: val
    path: data/kor_Hang/val.chunk.*.jsonl
- config_name: digit
  data_files:
  - split: train
    path: data/digit/train.chunk.*.jsonl
  - split: val
    path: data/digit/val.chunk.*.jsonl
---

# Multilingual Addition

The MoTo paper uses this dataset as a minimal case study of how tokenization affects arithmetic across languages.

Part of the MoTo release: [paper](https://openreview.net/forum?id=avjeUhPuC6) · [code](https://github.com/r-three/moto) · [models](https://huggingface.co/r3-moto).

Synthetic dataset of addition problems of the form `a+b=answer`, where `a`
and `b` are written-form representations of integers in 25 languages, plus a 26th split using raw digit strings.

## Task format

Each sample contains:

| field | type | description |
|---|---|---|
| `a_str` | str | written-form (or digit) representation of `a` |
| `a_digit` | int | integer value of `a` |
| `b_str` | str | written-form (or digit) representation of `b` |
| `b_digit` | int | integer value of `b` |
| `answer` | str | written-form (or digit) of `a + b` |
| `answer_digit` | int | integer value of `a + b` |
| `text` | str | `"{a_str}+{b_str}={answer}"` (completion target) |
| `question` | str | `"{a_str}+{b_str}="` (prompt) |
| `lang` | str | language tag, e.g. `eng_Latn`, or `digit` |

Numbers range from `0` to `999` for both `a` and `b`
(answers up to `1998`).

## Languages

| lang | train | val |
|---|---|---|
| `eng_Latn` | 900,000 | 100,000 |
| `dan_Latn` | 900,000 | 100,000 |
| `swe_Latn` | 900,000 | 100,000 |
| `vie_Latn` | 900,000 | 100,000 |
| `hun_Latn` | 900,000 | 100,000 |
| `fas_Arab` | 900,000 | 100,000 |
| `tur_Latn` | 900,000 | 100,000 |
| `ces_Latn` | 900,000 | 100,000 |
| `arb_Arab` | 900,000 | 100,000 |
| `ell_Grek` | 900,000 | 100,000 |
| `ind_Latn` | 900,000 | 100,000 |
| `nld_Latn` | 900,000 | 100,000 |
| `pol_Latn` | 900,000 | 100,000 |
| `por_Latn` | 900,000 | 100,000 |
| `ita_Latn` | 900,000 | 100,000 |
| `jpn_Jpan` | 900,000 | 100,000 |
| `fra_Latn` | 900,000 | 100,000 |
| `spa_Latn` | 900,000 | 100,000 |
| `deu_Latn` | 900,000 | 100,000 |
| `cmn_Hani` | 900,000 | 100,000 |
| `rus_Cyrl` | 900,000 | 100,000 |
| `nob_Latn` | 900,000 | 100,000 |
| `fin_Latn` | 900,000 | 100,000 |
| `ben_Beng` | 900,000 | 100,000 |
| `kor_Hang` | 900,000 | 100,000 |
| `digit` | 900,000 | 100,000 |

## Generation

```bash
python create_multilingual_addition_data.py \
    --hf_repo_id flexitok/multilingual-addition \
    --publish_to_hf \
    --a_min 0 --a_max 999 \
    --seed 42 --train_ratio 0.9
```

## License

Released under [MIT](https://opensource.org/license/mit).

## Citation

If you use this data, please cite MoTo and the tools it was built with.

```bibtex
@inproceedings{altintas2026moto,
  title={{MoTo}: Mixture of Tokenizers Towards Fair Multilingual Language Modeling},
  author={G{\"u}l Sena Alt{\i}nta{\c{s}} and Colin Raffel},
  booktitle={The Fortieth Annual Conference on Neural Information Processing Systems},
  year={2026},
  url={https://openreview.net/forum?id=avjeUhPuC6}
}

@electronic{num2words,
  author = {num2words},
  date-added = {2026-05-07 03:51:44 -0400},
  title = {num2words library - Convert numbers to words in multiple languages},
  url = {https://pypi.org/project/num2words/}}
```
