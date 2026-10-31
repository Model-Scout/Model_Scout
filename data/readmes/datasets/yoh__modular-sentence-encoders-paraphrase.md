---
license: cc-by-nc-4.0
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
- feature-extraction
size_categories:
- 100K<n<1M
tags:
- multilingual
- parallel
- machine-translation
- sentence-embeddings
- contrastive-learning
pretty_name: Multi-parallel paraphrase corpus for modular sentence encoders
configs:
- config_name: mnli
  data_files: mnli.parquet
- config_name: sentence_compression
  data_files: sentence_compression.parquet
- config_name: simplewiki
  data_files: simplewiki.parquet
- config_name: altlex
  data_files: altlex.parquet
- config_name: quora
  data_files: quora.parquet
---

# Multi-parallel paraphrase corpus (23 languages)

The contrastive training data of [*Modular Sentence Encoders: Separating Language
Specialization from Cross-Lingual Alignment*](https://aclanthology.org/2025.acl-long.108/)
(ACL 2025). Five English paraphrase datasets, each translated into 22 further
languages, published so that the paper's sentence-encoder and alignment stages
can be reproduced without re-running the translation.

**Most of this corpus is machine-translated.** Only the English columns are
original human-written text; see [Provenance](#provenance) for exactly which
columns came from where.

The corpus is **multi-parallel**: row *i* of every column is the same content in
a different language. That makes it usable three ways, all of which the paper
needs:

- monolingual paraphrase pairs — `anchor_de` / `positive_de`;
- cross-lingual paraphrase pairs — `anchor_en` / `positive_de`;
- translation (parallel) pairs — `anchor_en` / `anchor_de`.

## Usage

Each dataset is a single Parquet file with flat columns, so a run that needs two
languages reads two languages rather than 23:

```python
from datasets import load_dataset

# All 23 languages of one dataset
ds = load_dataset("yoh/modular-sentence-encoders-paraphrase", "quora", split="train")

# Just the columns you need (much faster, much less memory)
import pyarrow.parquet as pq
from huggingface_hub import hf_hub_download

path = hf_hub_download(
    "yoh/modular-sentence-encoders-paraphrase",
    "quora.parquet",
    repo_type="dataset",
)
table = pq.read_table(path, columns=["anchor_en", "positive_de", "negative_de"])
```

## Schema

Every dataset has one column per (role, language) pair, named `{role}_{lang}`:

| role | meaning |
|---|---|
| `anchor` | the first sentence of the pair |
| `positive` | a paraphrase, entailment or duplicate of the anchor |
| `negative` | a hard negative; only in `mnli` and `quora` |

Language codes are the paper's two-letter codes: `am, ar, az, cs, de, en, es,
fr, ha, it, kk, ko, ky, mr, nl, pl, ru, rw, te, tr, ug, uz, zh`.

| config | rows | columns per language | English source |
|---|---|---|---|
| `mnli` | 128,082 | anchor / positive / negative | MultiNLI premise, its entailed and its contradicting hypothesis |
| `sentence_compression` | 179,905 | anchor / positive | a news sentence and its compression |
| `simplewiki` | 102,144 | anchor / positive | an English Wikipedia sentence and its Simple English Wikipedia counterpart |
| `altlex` | 112,610 | anchor / positive | an aligned Wikipedia / Simple Wikipedia sentence pair from the AltLex corpus |
| `quora` | 103,662 | anchor / positive / negative | a Quora question, a duplicate of it, and a non-duplicate |

626,403 rows in total. 263 rows of the original 626,666 are absent: the
translation came back empty in at least one language, and a row is only useful
if every language has it.

## Provenance

The English side of every dataset is the original, untranslated source data. No
non-English column is human-written:

| config | non-English columns |
|---|---|
| `mnli` | `ar`, `de`, `es`, `fr`, `ru`, `tr`, `zh` come from [XNLI](https://github.com/facebookresearch/XNLI)'s own translations of the MultiNLI training set; the remaining 15 languages were translated with [NLLB-200-3.3B](https://huggingface.co/facebook/nllb-200-3.3B) |
| all others | translated with NLLB-200-3.3B |

XNLI's training-set translations are themselves machine translations, produced
by the XNLI authors; only XNLI's dev and test sets are human-translated, and
they are not used here. So the corpus is machine-translated throughout, with the
`mnli` config mixing two different machine translation systems.

Translation quality was not filtered or scored. The paper's point is precisely
that machine-translated data at this scale is good enough to train sentence
encoders; Appendix D of the paper reports what that costs on each task.

## Licensing

**Machine translation.** NLLB-200 is released under
[CC BY-NC 4.0](https://huggingface.co/facebook/nllb-200-3.3B), and its outputs
inherit that license. XNLI is likewise non-commercial. The corpus as a whole is
therefore published under **CC BY-NC 4.0** and is for research use only.

**Underlying English data**, each with its own terms, which continue to apply:

| config | source | terms |
|---|---|---|
| `mnli` | [MultiNLI](https://cims.nyu.edu/~sbowman/multinli/) (Williams et al., 2018) | mostly the OANC license (free use, modification, redistribution); some fiction under CC BY 3.0 / CC BY-SA 3.0 or public domain |
| `sentence_compression` | [google-research-datasets/sentence-compression](https://github.com/google-research-datasets/sentence-compression) (Filippova & Altun, 2013) | no license stated by the publisher; distributed "as is" |
| `simplewiki` | English and Simple English Wikipedia | CC BY-SA |
| `altlex` | [AltLex](https://github.com/chridey/altlex) (Hidey & McKeown, 2016) | derived from Wikipedia, CC BY-SA |
| `quora` | [Quora Question Pairs](https://quoradata.quora.com/First-Quora-Dataset-Release-Question-Pairs) | Quora's terms for the released dataset |

Note the tension in `simplewiki` and `altlex`: their source text is share-alike,
while the translations carry a non-commercial restriction, and the two cannot be
combined cleanly. They are published here under the stricter of the two terms.
If you need those two datasets under share-alike terms, translate the English
columns yourself with a permissively licensed system.

If you are a rights holder for any of the above and object to this
redistribution, please open a discussion on this repository and it will be
removed.

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

Please also cite the source datasets you use and, for the translations,
[NLLB](https://arxiv.org/abs/2207.04672).

Code: <https://github.com/UKPLab/acl2025-modular-sentence-encoders>
