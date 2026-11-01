---
license: 
- cc-by-4.0
- cc-by-nc-4.0
- cc-by-nc-sa-4.0
- cc-by-sa-4.0
- other
language:
- 'ca'
- 'cs'
- 'cu'
- 'de'
- 'en'
- 'es'
- 'fr'
- 'grc'
- 'hbo'
- 'hi'
- 'hu'
- 'ko'
- 'la'
- 'lt'
- 'nl'
- 'no'
- 'pl'
- 'ru'
- 'tr'
tags:
- Coreference Resolution
- NER
pretty_name: corefud-1-4
---

# corefud-1-4

## Dataset Summary

This repository provides a standardized and reformatted version of the
original **corefud-1-4** coreference resolution dataset.

The purpose of this formatting is to provide a unified document structure
across multiple coreference datasets in order to simplify:

- cross-dataset comparison,
- multilingual experimentation,
- benchmarking of coreference resolution systems,
- interoperability between NLP pipelines,
- and reproducible evaluation settings.

This repository does **not** introduce new annotations or modify the original
coreference annotations. It only restructures the original dataset into a
shared schema used across our benchmarking framework.

---

## Original Dataset

This formatted version is derived from the dataset introduced in:

[Michal Novák ; et al. 2026. *Coreference in Universal Dependencies 1.4 (CorefUD 1.4).*](https://lindat.mff.cuni.cz/repository/items/cc63aba6-a7dc-4b83-8784-8f440835dee0)

### Original Repository

https://lindat.mff.cuni.cz/repository/items/cc63aba6-a7dc-4b83-8784-8f440835dee0

### Citation

If you use this dataset, please cite the original work:

```bibtex
@misc{11234/1-6108,
    title = {Coreference in Universal Dependencies 1.4 ({CorefUD} 1.4)},
    author = {Nov{\'a}k, Michal and Popel, Martin and Zeman, Daniel and {\v Z}abokrtsk{\'y}, Zden{\v e}k and Nedoluzhko, Anna and Acar, Kutay and Bamman, David and Bourgois, Antoine and Bourgonje, Peter and Cinkov{\'a}, Silvie and Delfino, Eleonora and Eckhoff, Hanne and Cebiro{\u g}lu Eryi{\u g}it, G{\"u}l{\c s}en and Haji{\v c}, Jan and Han, Sooyoun and Hardmeier, Christian and Haug, Dag and J{\o}rgensen, Tollef and K{\aa}sen, Andre and Krielke, Pauline and Landragin, Fr{\'e}d{\'e}ric and Lapshinova-Koltunski, Ekaterina and Leotta, Roberta Grazia and M{\ae}hlum, Petter and Mart{\'{\i}}, M. Ant{\`o}nia and M{\'e}lanie-Becquet, Fr{\'e}d{\'e}rique and Mikulov{\'a}, Marie and Milintsevich, Kirill and Moretti, Giovanni and Mujadia, Vandan and Muzerelle, Judith and Nam, Sangha and N{\o}klestad, Anders and Ogrodniczuk, Maciej and {\O}vrelid, Lilja and Pamay Arslan, Tu{\u g}ba and Passarotti, Marco and Poibeau, Thierry and Porada, Ian and Recasens, Marta and Seo, Sumin and Solberg, Per Erik and Stede, Manfred and {\v S}t{\v e}p{\'a}nek, Jan and {\v S}t{\v e}p{\'a}nkov{\'a}, Barbora and Straka, Milan and Swanson, Daniel and Toldova, Svetlana and Vad{\'a}sz, No{\'e}mi and van Cranenburgh, Andreas and Velldal, Erik and Vincze, Veronika and Zeldes, Amir and {\v Z}itkus, Voldemaras},
    url = {http://hdl.handle.net/11234/1-6108},
    note = {{LINDAT}/{CLARIAH}-{CZ} digital library at the Institute of Formal and Applied Linguistics ({{\'U}FAL})},
    copyright = {Licence {CorefUD} v1.4},
    year = {2026}
}
```

CorefUD is a collection of previously existing coreference-annotated datasets that have been converted to a unified annotation scheme. In its current version (1.4), CorefUD comprises 33 datasets covering 19 languages. The datasets are enriched with automatically assigned morphological and syntactic annotations, fully compliant with the standards of the Universal Dependencies project, in cases where manual morphosyntactic annotation is not available or cannot be reliably converted. The data are stored in the CoNLL-U format, with coreference- and bridging-specific information encoded as attribute–value pairs in the MISC column. The collection is divided into a public edition and a non-public (ÚFAL-internal) edition. The public edition is distributed via LINDAT-CLARIAH-CZ and contains 29 datasets for 19 languages (1 dataset for Ancient Greek, 1 for Ancient Hebrew, 1 for Catalan, 3 for Czech, 1 for Dutch, 4 for English, 3 for French, 2 for German, 1 for Hindi, 2 for Hungarian, 1 for Korean, 1 for Latin, 1 for Lithuanian, 2 for Norwegian, 1 for Old Church Slavonic, 1 for Polish, 1 for Russian, 1 for Spanish, and 1 for Turkish), excluding test portions. The non-public edition is available internally to ÚFAL members and includes an additional 4 datasets for 2 languages (1 for Dutch and 3 for English) that cannot be redistributed due to licensing restrictions. It also contains the test portions for all datasets. When using any of the harmonized datasets, please review the respective license ([https://lindat.mff.cuni.cz/repository/items/cc63aba6-a7dc-4b83-8784-8f440835dee0](https://lindat.mff.cuni.cz/repository/items/cc63aba6-a7dc-4b83-8784-8f440835dee0)) and cite the original resource.

---

## Statistics

| Statistic | Value |
|---|---:|
| Language | ca, cs, cu, de, en, es, fr, grc, hbo, hi, hu, ko, la, lt, nl, no, pl, ru, tr |
| Documents | 14,669 |
| Sentences | 396,281 |
| Tokens | 6,956,975 |
| Characters | 36,339,508 |
| Mentions | 1,503,028 |
| Entities | 659,720 |

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

## Overview of the corpora and their license terms

| Corpus | License |
|--------|----------|
| CorefUD_Ancient_Greek-PROIEL | CC BY-NC-SA 4.0 |
| CorefUD_Ancient_Hebrew-PTNK | CC BY-NC 4.0 |
| CorefUD_Catalan-AnCora | CC BY 4.0 |
| CorefUD_Czech-PCEDT | CC BY-NC-SA 4.0 |
| CorefUD_Czech-PDT | CC BY-NC-SA 4.0 |
| CorefUD_Czech-PDTSC | CC BY-NC-SA 4.0 |
| CorefUD_Dutch-OpenBoek | CC BY 4.0 |
| CorefUD_English-FantasyCoref | CC BY-SA 4.0 |
| CorefUD_English-GUM | CC BY-NC-SA 4.0 |
| CorefUD_English-LitBank | CC BY 4.0 |
| CorefUD_English-ParCorFull | CC BY-NC 4.0 |
| CorefUD_French-ANCOR | CC BY-NC-SA 4.0 |
| CorefUD_French-Democrat | CC BY-SA 4.0 |
| CorefUD_French-LitBankFr | CC BY-SA 4.0 |
| CorefUD_German-ParCorFull | CC BY-NC 4.0 |
| CorefUD_German-PotsdamCC | CC BY-NC-SA 4.0 |
| CorefUD_Hindi-HDTB | CC BY-NC-SA 4.0 |
| CorefUD_Hungarian-KorKor | CC BY 4.0 |
| CorefUD_Hungarian-SzegedKoref | CC BY 4.0 |
| CorefUD_Korean-ECMT | CC BY 4.0 |
| CorefUD_Latin-CorefLat | CC BY-SA 4.0 |
| CorefUD_Lithuanian-LCC | CLARIN-LT End User License |
| CorefUD_Norwegian-BokmaalNARC | CC BY-SA 4.0 |
| CorefUD_Norwegian-NynorskNARC | CC BY-SA 4.0 |
| CorefUD_Old_Church_Slavonic-PROIEL | CC BY-NC-SA 4.0 |
| CorefUD_Polish-PCC | CC BY 3.0 |
| CorefUD_Russian-RuCor | CC BY-SA 4.0 |
| CorefUD_Spanish-AnCora | CC BY 4.0 |
| CorefUD_Turkish-ITCC | CC BY-NC-SA 4.0 |

## Example

