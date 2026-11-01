---
license: cc-by-4.0
language:
- 'en'
- 'es'
- 'id'
- 'it'
- 'ko'
- 'nl'
- 'zh'
tags:
- Coreference Resolution
- NER
pretty_name: GOLEMcoref
---

# GOLEMcoref

## Dataset Summary

This repository provides a standardized and reformatted version of the
original **GOLEMcoref** coreference resolution dataset.

The purpose of this formatting is to provide a unified document structure
across multiple coreference datasets in order to simplify:

- cross-dataset comparison,
- multilingual experimentation,
- benchmarking of coreference resolution systems,
- interoperability between NLP pipelines,
- and reproducible evaluation settings.

This repository does **not** introduce new annotations. It only restructures the original dataset into a
shared schema used across our benchmarking framework. **Split Antecedents are ignored**.

---

## Original Dataset

This formatted version is derived from the dataset introduced in:

[Andreas Van Cranenburgh ; et al. 2026. *GOLEMcoref: A Multilingual Coreference Dataset of Fiction.*](https://aclanthology.org/2026.acl-short.39/)

### Original Repository

https://github.com/GOLEM-lab/GOLEMcoref

### Citation

If you use this dataset, please cite the original work:

```bibtex
@inproceedings{van-cranenburgh-etal-2026-golemcoref,
    title = "{GOLEM}coref: A Multilingual Coreference Dataset of Fiction",
    author = "Van Cranenburgh, Andreas  and
      Yang, Xiaoyan  and
      Alvanita  and
      Di Domenico, Cecilia Nicole  and
      Ferragud, Maria  and
      Graciotti, Arianna  and
      Kim, Byungjun  and
      Park, Seonyeong  and
      Solissa, Noa Visser  and
      Zhou, Xiaoyu  and
      Pianzola, Federico",
    editor = "Liakata, Maria  and
      Moreira, Viviane P.  and
      Zhang, Jiajun  and
      Jurgens, David",
    booktitle = "Proceedings of the 64th Annual Meeting of the {A}ssociation for {C}omputational {L}inguistics (Volume 2: Short Papers)",
    month = jul,
    year = "2026",
    address = "San Diego, California, United States",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.acl-short.39/",
    pages = "472--480",
    ISBN = "979-8-89176-391-3",
}
```

- What is **GOLEMcoref**?
    - It is a gold standard benchmark for coreference resolution in **7 languages**: **Bahasa Indonesia**, **Chinese**, **Dutch**, **English**, **Italian**, **Korean**, **Spanish** (--> [data/gold_annotations](https://github.com/GOLEM-lab/golemcoref/tree/main/data/gold_annotations)).
    - It contains fictional **short stories** sourced from 3 popular **fanfiction** platforms: [Archive of Our Own (AO3)](https://archiveofourown.org/), [Postype](https://www.postype.com/), and [Wattpad](https://www.wattpad.com/).
    - It is the first of its kind offering **multilingual coverage** for **fictional literature**.
    - It includes **complete works**.
    - It is a **gold standard**: it is fully **annotated** and curated by **humanas** following specialised guidelines (--> [guidelines](https://github.com/GOLEM-lab/golemcoref/tree/main/guidelines)) and accompanied by a report discussing annotation challenges (--> [report](https://github.com/GOLEM-lab/golemcoref/tree/main/report)).


---

## Statistics

| Statistic | Value |
|---|---:|
| Language | en, es, id, it, ko, nl, zh |
| Documents | 230 |
| Sentences | 55,652 |
| Tokens | 811,389 |
| Characters | 3,407,934 |
| Mentions | 102,682 |
| Entities | 4,942 |

---

## Dataset Structure

Each document contains:

- `file_name`
- `language`
- `text`
- `tokens_count`
- `mentions`
- `sentence_spans`

### Mentions

Each mention contains the following fields and additional fields per-dataset:

- `onset`
- `offset`
- `COREF`

---


## Example

