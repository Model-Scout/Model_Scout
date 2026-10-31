---
annotations_creators:
- human
- machine-generated
language_creators:
- found
language:
- en
- ar
- es
- fr
- ru
- hi
- ms
- sw
- az
- ko
- pt
- hy
- th
- uk
- ur
- sr
- iw
- ja
- hr
- tl
- ky
- vi
- fa
- tg
- mg
- nl
- ne
- uz
- my
- da
- dz
- id
- is
- tr
- lo
- sl
- so
- mn
- bn
- bs
- ht
- el
- it
- to
- ka
- sn
- sq
- zh
license: mit
multilinguality:
- multilingual
source_datasets:
- manestay/borderlines
task_categories:
- question-answering
pretty_name: BordIRlines
arxiv: 2410.01171
---

# BordIRLines Dataset

This is the dataset associated with the paper "BordIRlines: A Dataset for Evaluating Cross-lingual Retrieval-Augmented Generation" ([link](https://arxiv.org/abs/2410.01171)).

Code: https://github.com/manestay/bordIRlines

## Dataset Summary

The **BordIRLines Dataset** is an information retrieval (IR) dataset constructed from various language corpora. It contains queries and corresponding ranked docs along with their relevance scores. The dataset includes multiple languages, including English, Arabic, Spanish, and others, and is split across different sources like LLM-based outputs.
Each `doc` is a passage from a Wikipedia article.

### Languages

The dataset includes docs and queries in the following **languages**:

- `en`: English
- `zht`: Traditional Chinese
- `ar`: Arabic
- `zhs`: Simplified Chinese
- `es`: Spanish
- `fr`: French
- `ru`: Russian
- `hi`: Hindi
- `ms`: Malay
- `sw`: Swahili
- `az`: Azerbaijani
- `ko`: Korean
- `pt`: Portuguese
- `hy`: Armenian
- `th`: Thai
- `uk`: Ukrainian
- `ur`: Urdu
- `sr`: Serbian
- `iw`: Hebrew
- `ja`: Japanese
- `hr`: Croatian
- `tl`: Tagalog
- `ky`: Kyrgyz
- `vi`: Vietnamese
- `fa`: Persian
- `tg`: Tajik
- `mg`: Malagasy
- `nl`: Dutch
- `ne`: Nepali
- `uz`: Uzbek
- `my`: Burmese
- `da`: Danish
- `dz`: Dzongkha
- `id`: Indonesian
- `is`: Icelandic
- `tr`: Turkish
- `lo`: Lao
- `sl`: Slovenian
- `so`: Somali
- `mn`: Mongolian
- `bn`: Bengali
- `bs`: Bosnian
- `ht`: Haitian Creole
- `el`: Greek
- `it`: Italian
- `to`: Tonga
- `ka`: Georgian
- `sn`: Shona
- `sq`: Albanian
- `zh`: Chinese
- `control`: see below

The **control** language is English, and contains the queries for all 251 territories. In contrast, **en** is only the 38 territories which have an English-speaking claimant.

### Annotations

The dataset contains two types of relevance annotations:

1. **Human Annotations**: Provided by multiple annotators for a subset of query-document pairs and relevance is determined by majority vote across annotators.

2. **LLM Annotations**:
   - Includes two modes:
     - **Zero-shot**: Predictions without any task-specific examples.
     - **Few-shot**: Predictions with a small number of task-specific examples.
   - Default mode is **few-shot**.

## Systems

We have processed retrieval results for these IR systems:

- `openai`: OpenAI's model `text-embedding-3-large`, cosine similarity
- `m3`: M3-embedding ([link](https://huggingface.co/BAAI/bge-m3)) (Chen et al., 2024)

## Modes

Considering a user query in language `l` on a territory `t`, there are 4 modes for the IR.

- `qlang`: consider passages in `{l}`. This is monolingual IR (the default).
- `qlang_en`: consider passages in either `{l, en}`.
- `en`: consider passages in `{en}`.
- `rel_langs`: consider passages in all relevant languages to `t` + `en`, so `{l1, l2, ..., en}`. This is a set, so `en` will not be duplicated if it already is relevant.

## Dataset Structure

### Data Fields

The dataset consists of the following fields:

- `query_id (string)`: The id of the query.
- `query (string)`: The query text as provided by the `queries.tsv` file.
- `territory (string)`: The territory of the query hit.
- `rank (int32)`: The rank of the document for the corresponding query.
- `score (float32)`: The relevance score of the document as provided by the search engine or model.
- `doc_id (string)`: The unique identifier of the article.
- `doc_text (string)`: The full text of the corresponding article or document.
- `relevant_human (bool)`: Majority relevance determined by human annotators.
- `territory_human (list[string])`: Territories as judged by human annotators.
- `relevant_llm_zeroshot (bool)`: LLM zero-shot relevance prediction.
- `relevant_llm_fewshot (bool)`: LLM few-shot relevance prediction.

### Download Structure

The dataset is structured as follows:

```
data/
  {lang}/
    {system}/
      {mode}/
        {lang}_query_hits.tsv
...
  all_docs.json
  queries.tsv
  human_annotations.tsv
  llm_annotations.tsv
```

- `queries.tsv`: Contains the list of query IDs and their associated query texts.
- `all_docs.json`: JSON dict containing all docs. It is organized as a nested dict, with keys `lang`, and values another dict with keys `doc_id`, and values `doc_text`.
- `{lang}\_query_hits.tsv`: A TSV file with relevance scores and hit ranks for queries.
- `human_annotations.tsv`: A TSV file with human relevance annotations.
- `llm_annotations.tsv`: A TSV file with LLM relevance predictions.

Currently, there are 50 langs _ 1 system _ 4 modes = 200 query hit TSV files.

## Example Usage

```python
from datasets import load_dataset

# load DatasetDict with all 4 modes, for control language, 10 hits
dsd_control = load_dataset("borderlines/bordirlines", "control")

# load Dataset for English, with rel_langs mode, 50 hits
ds_oa_en = load_dataset("borderlines/bordirlines", "en", split="openai.rel_langs", n_hits=50)
# load Dataset for Simplified Chinese, en mode
ds_oa_zhs1 = load_dataset("borderlines/bordirlines", "zhs", split="openai.en")
# load Dataset for Simplified Chinese, qlang mode
ds_oa_zhs2 = load_dataset("borderlines/bordirlines", "zhs", split="openai.qlang")


# load Dataset for Simplified Chinese, en mode, m3 embedding
ds_m3_zhs1 = load_dataset("borderlines/bordirlines", "zhs", split="m3.en")
# load Dataset for Simplified Chinese, qlang mode, m3 embedding
ds_m3_zhs2 = load_dataset("borderlines/bordirlines", "zhs", split="m3.qlang")

# Load Dataset for English, relevant-only with human annotations
ds_human_en = load_dataset("borderlines/bordirlines", "en", relevance_filter="relevant", annotation_type="human")

# Load Dataset for Simplified Chinese, few-shot LLM mode, only non-relevant
ds_llm_fewshot_zhs = load_dataset("borderlines/bordirlines", "zhs", relevance_filter="non-relevant", annotation_type="llm", llm_mode="fewshot")
```

## Citation

```
@misc{li2024bordirlines,
      title={BordIRlines: A Dataset for Evaluating Cross-lingual Retrieval-Augmented Generation},
      author={Bryan Li and Samar Haider and Fiona Luo and Adwait Agashe and Chris Callison-Burch},
      year={2024},
      eprint={2410.01171},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2410.01171},
}
```