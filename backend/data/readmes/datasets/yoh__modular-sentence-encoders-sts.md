---
license: cc-by-nc-sa-3.0
language:
- am
- ar
- az
- cs
- de
- en
- es
- fr
- ha
- it
- kk
- ko
- ky
- mr
- nl
- pl
- ru
- rw
- te
- tr
- ug
- uz
- zh
task_categories:
- sentence-similarity
size_categories:
- 10K<n<100K
tags:
- semantic-textual-similarity
- semantic-relatedness
- cross-lingual
- evaluation
pretty_name: Resolved STS and STR evaluation sets for modular sentence encoders
configs:
- config_name: sts17
  data_files:
  - split: test
    path: sts17.parquet
- config_name: stsb
  data_files:
  - split: test
    path: stsb.parquet
- config_name: sick
  data_files:
  - split: test
    path: sick.parquet
- config_name: str24
  data_files:
  - split: test
    path: str24.parquet
---

# STS / STR evaluation sets, resolved (23 languages)

The semantic textual similarity and relatedness evaluation data of [*Modular
Sentence Encoders: Separating Language Specialization from Cross-Lingual
Alignment*](https://aclanthology.org/2025.acl-long.108/) (ACL 2025), in one flat
schema.

This repository contains **no new data**. It is a redistribution of six existing
benchmarks, with the alignment work already applied: pairing monolingual sets
into cross-lingual ones by row index, intersecting SICK pair IDs across
translations, matching KorSTS rows to the STS benchmark, combining the STS17
extension columns, and transliterating the Uyghur data from Cyrillic to Arabic
script. Doing that at load time is where evaluation code usually goes quietly
wrong, so it is frozen into the data instead.

## Usage

```python
from datasets import load_dataset

ds = load_dataset("yoh/modular-sentence-encoders-sts", "sts17", split="test")
de_fr = ds.filter(lambda r: r["lang_a"] == "de" and r["lang_b"] == "fr")
```

## Schema

One row per sentence pair, in every config:

| column | type | meaning |
|---|---|---|
| `lang_a` | string | language of `sentence_a`, a two-letter code |
| `lang_b` | string | language of `sentence_b` |
| `sentence_a` | string | first sentence |
| `sentence_b` | string | second sentence |
| `score` | float | gold similarity or relatedness; the scale is the source benchmark's |

Each config has a single `test` split: these are evaluation sets, and none of
them is meant to be trained on.

A monolingual set is simply a row where `lang_a == lang_b`. Score scales differ
between configs (0–5 for STS and SICK, 0–1 for STR), which does not matter for
the Spearman correlation these sets are used with, but does matter if you pool
them.

| config | language pairs | rows | scale |
|---|---|---|---|
| `sts17` | 30 | 10,096 | 0–5 |
| `stsb` | 48 | 38,388 | 0–5 |
| `sick` | 16 | 78,496 | 1–5 |
| `str24` | 6 (monolingual only) | 4,191 | 0–1 |

Two sizes depart from the round numbers of the source benchmarks, both inherited
from the original resolution: STS17 `ko-ko` is the full KorSTS test set (2,846
rows, not 250), and the twelve STSB pairs involving Korean have 799 rows rather
than 800, because one row could not be matched.

## Sources

| config | languages | built from |
|---|---|---|
| `sts17` | ar, cs, de, en, es, fr, it, ko, nl, tr | [SemEval-2017 Task 1](https://alt.qcri.org/semeval2017/task1/) (Cer et al., 2017) and its [extended multilingual version](https://github.com/UKPLab/sentence-transformers) (Reimers & Gurevych, 2020); Korean from [KorSTS](https://github.com/kakaobrain/kor-nlu-datasets) |
| `stsb` | az, en, kk, ky, ko, ug, uz | the [STS benchmark](https://ixa2.si.ehu.eus/stswiki/index.php/STSbenchmark); Turkic languages from [Kardeş-NLU](https://github.com/lksenel/Kardes-NLU) (Senel et al., 2024); Korean from KorSTS (Ham et al., 2020) |
| `sick` | en, es, nl, pl | [SICK](https://zenodo.org/records/2787612) (Marelli et al., 2014), [SICK-NL](https://github.com/gijswijnholds/sick_nl) (Wijnholds & Moortgat, 2021), [SICK-PL](https://huggingface.co/datasets/sdadas/sick_pl) (Dadas et al., 2020), SICK-ES (Huertas-García et al., 2022) |
| `str24` | am, en, ha, mr, rw, te | [SemRel2024](https://github.com/semantic-textual-relatedness/Semantic_Relatedness_SemEval2024), SemEval-2024 Task 1 (Ousidhoum et al., 2024) |

Cross-lingual pairs in `sts17`, `stsb` and `sick` are formed by taking
`sentence_a` from one language's copy of a row and `sentence_b` from another's,
which is valid because those benchmarks are translations of the same items. The
gold score is the source benchmark's score for that row.

## Licensing

The configs do not share one license, because their sources do not:

| config | terms |
|---|---|
| `sick` | SICK is [CC BY-NC-SA 3.0](https://zenodo.org/records/2787612); its translations are derivatives and inherit it. SICK-NL's code is MIT, its data is not. |
| `sts17`, `stsb` | The similarity scores of the STS benchmark family are CC BY-SA 4.0; the underlying sentences keep the licenses of the corpora they were drawn from. KorSTS is CC BY-SA 4.0. **Kardeş-NLU states no license.** |
| `str24` | **SemRel2024 states no license** in its repository or on the Hub. |

The repository is labelled CC BY-NC-SA 3.0, the strictest of the terms that are
actually stated, and is intended for non-commercial research use. Where a source
states no license, redistribution here is on the understanding that the data was
published for open evaluation use; if you are one of those authors and prefer
that we link rather than redistribute, please open a discussion and the config
will be replaced by a resolution script.

Please cite the source benchmarks you evaluate on, not only this repository.

## Citation

```bibtex
@inproceedings{huang-etal-2025-modular,
    title = "Modular Sentence Encoders: Separating Language Specialization from Cross-Lingual Alignment",
    author = "Huang, Yongxin and Wang, Kexin and Glava{\v{s}}, Goran and Gurevych, Iryna",
    booktitle = "Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    year = "2025",
    pages = "2167--2187",
    url = "https://aclanthology.org/2025.acl-long.108/",
}
```

Code: <https://github.com/UKPLab/acl2025-modular-sentence-encoders>
