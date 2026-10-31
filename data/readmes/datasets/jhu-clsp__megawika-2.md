---
language:
- af
- ar
- az
- bn
- cs
- de
- en
- es
- et
- fa
- fi
- fr
- ga
- gl
- gu
- he
- hi
- hr
- id
- it
- ja
- ka
- kk
- km
- ko
- lt
- lv
- mk
- ml
- mn
- mr
- my
- ne
- nl
- pl
- ps
- pt
- ro
- ru
- si
- sl
- sv
- ta
- th
- tr
- uk
- ur
- vi
- xh
- zh
pretty_name: MegaWika 2
size_categories:
- 10M<n<100M
---
# MegaWika 2

MegaWika 2 is an improved multilingual text dataset containing a structured view of Wikipedia articles, the web sources they cite, source text quality estimates, article text translations, and additional article enrichments.

**Note:** Web citations (sources) in the HuggingFace dataset do not include scraped source text; use [rehydrate-citations.py](https://huggingface.co/datasets/jhu-clsp/megawika-2/blob/main/rehydrate-citations.py) to rehydrate them.

The initial data release is based on Wikipedia dumps from May 1, 2024.
In total, the data contains about 77 million articles and 71 million scraped web citations.
The English collection, the largest, contains about 10 million articles and 24 million scraped web citations.

In the future, we may release *deltas,* collections of articles that have been added or changed since the initial dump (or since the previous delta release).
We expect a fraction of the articles to change between dumps; hence, deltas will be significantly smaller and more compact than the initial collection.


## Quick Links

- [Dataset on HuggingFace](https://hf.co/datasets/jhu-clsp/megawika-2)
- [Online documentation](https://megawika.ccmaymay.net/) including browsable data schema
- [Whitepaper on ArXiv](https://arxiv.org/abs/2508.03828) including dataset details and analysis
  - [MegaWika 1 Preprint on ArXiv](https://arxiv.org/abs/2307.07049)

## Languages Covered

As in MegaWika 1, MegaWika 2 spans 50 languages, including English, designated by their two-character ISO 639-1 language code:

- `af`: Afrikaans
- `ar`: Arabic
- `az`: Azeri (Azerbaijani)
- `bn`: Bengali
- `cs`: Czech
- `de`: German (Deutsch)
- `en`: English
- `es`: Spanish (Español)
- `et`: Estonian
- `fa`: Farsi (Persian)
- `fi`: Finnish
- `fr`: French
- `ga`: Irish (Gaelic)
- `gl`: Galician
- `gu`: Gujarati
- `he`: Hebrew
- `hi`: Hindi
- `hr`: Croatian
- `id`: Indonesian
- `it`: Italian
- `ja`: Japanese
- `ka`: Georgian (Kartvelian/Kartlian)
- `kk`: Kazakh
- `km`: Khmer
- `ko`: Korean
- `lt`: Lithuanian
- `lv`: Latvian
- `mk`: Macedonian (Makedonski)
- `ml`: Malay (Malayalam)
- `mn`: Mongolian
- `mr`: Marathi
- `my`: Burmese (Myanmar language)
- `ne`: Nepali
- `nl`: Dutch (Nederlands)
- `pl`: Polish
- `ps`: Pashto
- `pt`: Portuguese
- `ro`: Romanian
- `ru`: Russian
- `si`: Sinhalese (Sri Lankan language)
- `sl`: Slovenian
- `sv`: Swedish (Svenska)
- `ta`: Tamil
- `th`: Thai
- `tr`: Turkish
- `uk`: Ukrainian
- `ur`: Urdu
- `vi`: Vietnamese
- `xh`: Xhosa
- `zh`: Chinese (Zhōngwén)

## Dataset Structure

### Directory Structure

The MegaWika 2 dataset consists of a list of directories, one for each language, designated by its language code.

Each language subdirectory contains a list of chunks in JSON-lines format, where each chunk contains up to 1,000 articles, and each line of a chunk file is a distinct JSON-encoded Wikipedia article:

```
─ en/
  ├─ data/
  │  ├─ 000000001.jsonl
  │  ├─ 000000002.jsonl
  │  └─ [...]
  └─ metrics.json
```

Each language subdirectory also contains language-specific summary statistics (`metrics.json`) and a directory containing the data chunks (`data`).

### JSON Schema

The full data schema for MegaWika 2 is described in [`schema.md`](https://huggingface.co/datasets/jhu-clsp/megawika-2/blob/main/schema.md).

Among other things, each article object contains the article title, the article's raw wikicode and parsed text, and a hierarchy of objects representing the article structure.
This hierarchy includes, among many other things:

* The top level of this hierarchy is a list of headings, paragraphs, tables, infoboxes, and other block-level elements.
  * These block-level elements contain various sub-elements; for example, each paragraph contains a list of sentences.
    * Each sentence contains the sentence text, translated (English) sentence text, and a list of citations.
      * Each citation includes the raw wikicode content, the character index of the citation in the sentence text, an optional citation URL, and optional scraped citation source text.

## Statistics

The metrics files (for example, `en/metrics.json`) provide statistics describing the data collected for each language.

MegaWika 2 features greater coverage than MegaWika 1, including marked improvements in recall for the citation detection and source scraping/extraction processes:

| Metric                                | Version 1  | Version 2.0  | Increase       |
|---------------------------------------|-----------:|-------------:|--------------:|
| Articles Collected                    |  2,072,726 |    9,841,417 | 375%           |
| Web Citations Detected                | 17,368,499 |   57,431,369 | 231%           |
| Web Citations Successfully Scraped    |  5,623,386 |   23,544,500 | 319%           |
| Web Citation Scrape/Extraction Recall |        32% |          41% |        27% (relative) |



## Changelog

These entries summarize differences between versions; see the data schema in [`schema.md`](https://huggingface.co/datasets/jhu-clsp/megawika-2/blob/main/schema.md) for details.

### 2.0 (Differences from MegaWika 1)

MegaWika version 2 introduces a comprehensive redesign of the MegaWika data structure.
MegaWika 2 captures not just passage/source pairs, but the structure and relationship of the text---and the sources cited in that text---to the surrounding Wikipedia article.
Specifically, each article contains a structured element list parsed from the original Wikitext; the Wikitext is also provided for reference.
Paragraph elements in MegaWika 2 contain sentence-segmented text, further facilitating downstream research.
In parallel, each article contains a list of excerpts (in MegaWika 1, *passages*) with one or more citations attached to them, compared to the passage-citation pairs---supporting only one citation per passage---in MegaWika 1.
MegaWika 2.0 does not include translation probabilities, "repetitious translation" annotations, source language ID, or generated question-answer pairs as in MegaWika 1, but it does add a large amount of other metadata, including article creation and last revision dates, cross-lingual links, short source/citation snippets provided by authors, and source text quality estimates.

Along the way, we have improved the recall of the citation extraction process by (among other changes):
- Adding support for named citation resolution
- Expanding the coverage of citation syntax understood by the citation detector
- Including not just citations with scrapable URLs, but *all* citations, to support researchers who may want to study Wikipedia citation behavior in general, and across languages
- Increasing the scraped source code size limit

Statistics characterizing the improved recall in citation detection are provided in the [Statistics](#statistics) section.
Additional statistics are provided in the metrics files (for example, `en/metrics.json`) in the dataset.

MegaWika 2 also introduces improvements to error handling, providing higher coverage across the board.
Errors and metadata for source scraping and extraction are included in the data, enabling analysis of sources of missing data and potential biases in the data.

For additional details and analysis of the MegaWika 2.0 dataset and its construction, please see our [whitepaper on ArXiv](https://arxiv.org/abs/2508.03828).