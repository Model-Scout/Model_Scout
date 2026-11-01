---
language:
- en
- de
- ru
- es
- fr
- ja
- cs
- pl
- pt
- uk
- sk
- it
- ko
- el
- zh
- nl
- fi
- ca
- da
- fa
license: odbl
size_categories:
- 10K<n<100K
task_categories:
- feature-extraction
- sentence-similarity
tags:
- openstreetmap
- taginfo
- retrieval
- embeddings
- multilingual
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: tag
    dtype: string
  - name: key
    dtype: string
  - name: value
    dtype: string
  - name: lang
    dtype: string
  - name: title
    dtype: string
  - name: description
    dtype: string
  - name: lead_sentences
    sequence: string
  - name: related_terms
    sequence: string
  - name: 'on'
    sequence: string
  - name: implies
    dtype: string
  - name: status
    dtype: string
  - name: count_all
    dtype: int64
  splits:
  - name: train
    num_bytes: 13208851
    num_examples: 31913
  download_size: 6598805
  dataset_size: 13208851
---

# osm-tag-corpus

Frozen source material for embedding OpenStreetMap tags: every tag the OSM wiki
documents, with its description in each language it is documented in, its
related terms, and how often it is used worldwide.

**No embeddings, and no fixed passages.** The format in which a tag becomes a
sentence changes how well it retrieves, so this ships the material and leaves
the wording to the caller.

## A record

```json
{
  "tag": "tourism=hotel",
  "key": "tourism",
  "value": "hotel",
  "lang": "en",
  "title": "Tag:tourism=hotel",
  "description": "Hotel – an establishment that provides paid lodging.",
  "lead_sentences": [
    "A hotel is an establishment that provides paid lodging, usually on a short-term basis.",
    "..."
  ],
  "related_terms": [
    "hotel",
    "resort",
    "spa"
  ],
  "on": [
    "node",
    "area"
  ],
  "implies": "",
  "status": "approved",
  "count_all": 442848
}
```

| field | meaning |
|---|---|
| `tag` | `key=value`, or just the key for a key page |
| `lang` | the wiki language this record's text comes from |
| `description` | the one-line summary from the wiki infobox |
| `lead_sentences` | the page's opening paragraph, split into sentences |
| `related_terms` | terms listed on the page. Sometimes brand names |
| `on` | node, way, area, relation |
| `implies` | tags the wiki says this one implies. Often empty |
| `status` | approved, proposed, rejected_or_proposed, unknown |
| `count_all` | uses worldwide, from taginfo |

A tag documented in several languages appears several times, one record per
language. Fold to one score per tag at retrieval time and a hit in any language
counts for that tag.

`related_terms` carries mappings no description supplies: `amenity=fast_food`
lists Burger King, Döner, Kebab, McDonald's and Subway.

## Size

31,913 records, 9,803 distinct tags, 70 languages, 48,852 body sentences.
Built from taginfo dumps of 2026-01-30. See `provenance.yaml` for which tables
were read and which were deliberately skipped.

The wiki documents tags unevenly across languages, and the twenty listed in the
metadata are those with at least 85 records. The distribution has a long tail:

| | | | | | |
|---|---|---|---|---|---|
| en 9467 | de 3301 | ru 2901 | es 2709 | fr 2047 | ja 2033 |
| cs 1985 | pl 1816 | pt 948 | uk 907 | sk 760 | it 672 |
| ko 340 | el 299 | zh-hans 255 | nl 156 | fi 142 | ca 136 |
| da 109 | zh-hant 89 | fa 85 | + 49 more | | |

`lang` holds the wiki's own code, so `zh-hans` and `zh-hant` are separate there
even though the Hub metadata collapses them to `zh`.

## Assembling a sentence

How a tag is worded into a sentence changes how well it retrieves, so no
formatted text is shipped here and the wording is left to whatever uses this.

[yuiseki/osm-tag-embedding](https://github.com/yuiseki/osm-tag-embedding)
builds passages from these fields in several patterns, embeds them with several
models, and scores the combinations.

## Source

GitHub: [yuiseki/osm-tag-corpus](https://github.com/yuiseki/osm-tag-corpus)

Extracted from the [taginfo](https://taginfo.openstreetmap.org/download)
database dumps.

## License

ODbL-1.0. (The Hub's license identifier for this is `odbl`.)

This dataset is a Derivative Database of
[OpenStreetMap](https://www.openstreetmap.org/):

    (c) OpenStreetMap contributors, available under the Open Database License.
    https://www.openstreetmap.org/copyright

Sentences assembled from these fields, and any index or embedding built from
them, are derived from OSM and carry ODbL too. The full notice is in `LICENSE`
beside this file.
