---
task_categories:
  - text-generation
language:
  - en
  - de
  - fr
  - es
  - it
pretty_name: Red Pajama V2 Dataset
---

### Getting Started

RedPajama-V2 is an open dataset for training large language models. The dataset includes over 100B text
documents coming from 84 CommonCrawl snapshots and processed using
the [CCNet](https://github.com/facebookresearch/cc_net) pipeline. Out of these, there are 30B documents in the corpus
that additionally come with quality signals. In addition, we also provide the ids of duplicated documents which can be
used to create a dataset with 20B deduplicated documents.

Check out our [blog post](https://together.ai/blog/redpajama-data-v2) for more details on the build process, dataset
structure and schema.

A full set of scripts to recreate the dataset, including the quality signals, can be
found [here](https://github.com/togethercomputer/RedPajama-Data).

#### Downloading the raw Dataset with Quality Annotations

To familiarize yourself with the dataset, you can load the sample dataset using:

```python
from datasets import load_dataset

ds = load_dataset("togethercomputer/RedPajama-Data-V2", name="sample") 
```

To download a the dataset for a specific combination of `{partition} x {snapshot_id} x {language}`, you can use the
following command which downloads the raw (i.e., *not* deduplicated) part of the dataset and the corresponding quality
signals. In the example below, we use English and German data from the `head_middle` partition of the 2023-06 and the
2022-49 snapshots. The full set of available snapshots is specified in `_CC_SNAPSHOT_IDS`. The available partitions
are `tail` and `head_middle`. The available language tags are `en`, `de`, `fr`, `es`, `it`.
_Note that this will download the entire snapshots specified in the `snapshots` argument and requires ~1TB of disk space
per snapshot_.

```python
from datasets import load_dataset

ds = load_dataset("togethercomputer/RedPajama-Data-V2",
                  name="default",
                  partition="head_middle",
                  snapshots=["2023-06", "2022-49"],
                  languages=["en", "de"]) 
```

#### Downloading the dataset via wget

If you prefer to download the full dataset via wget, you can download the following lists of urls and use them to
download the dataset:

```bash
# get list of urls pointing to the text documents
wget "https://data.together.xyz/redpajama-data-v2/v1.0.0/urls/document-urls.txt" -O "document-urls.txt"

# get list of urls pointing to the quality signals
wget "https://data.together.xyz/redpajama-data-v2/v1.0.0/urls/quality_signals-urls.txt" -O "quality_signals-urls.txt"

# get list of urls pointing to the ids of duplicate documents
wget "https://data.together.xyz/redpajama-data-v2/v1.0.0/urls/duplicates-urls.txt" -O "duplicates-urls.txt"

# get list of urls pointing to the minhash signatures
wget "https://data.together.xyz/redpajama-data-v2/v1.0.0/urls/minhash-urls.txt" -O "minhash-urls.txt"
```

You can also directly download subsets of the dataset using the following instructions. Here we use English
data from the `2023-06` snapshot and the `head_middle` partition as an example. The full set of CC snapshots included in
the dataset is given in `_CC_SNAPSHOT_IDS`. The available partitions are `tail` and `head_middle`. The available
language tags are `en`, `de`, `fr`, `es`, `it`.

To download the plain text data, available for both the `head_middle` and `tail` partitions, you can run

```bash
CC_SNAPSHOT="2023-06"
LANG="en"
PARTITION="head_middle"
BASE_URL="https://data.together.xyz/redpajama-data-v2/v1.0.0"

listings_tag="${LANG}-${CC_SNAPSHOT}-${PARTITION}"
mkdir listings
wget "${BASE_URL}/listings/${listings_tag}.txt" -O "listings/${listings_tag}.txt"
listings_file="listings/${listings_tag}.txt"

# download documents
while read line; do
  url="${BASE_URL}/documents/${line}.json.gz"
  dest="documents/${line}.json.gz"
  mkdir -p $(dirname $dest)
  wget "$url" -O "$dest"
done <"$listings_file"

```

In addition, for the `head_middle` partition, you can also download the quality signals, minhash signatures and
duplicate ids using the following commands:

```bash
CC_SNAPSHOT="2023-06"
LANG="en"
BASE_URL="https://data.together.xyz/redpajama-data-v2/v1.0.0"

listings_tag="${LANG}-${CC_SNAPSHOT}-head_middle"
mkdir listings
wget "${BASE_URL}/listings/${listings_tag}.txt" -O "listings/${listings_tag}.txt"
listings_file="listings/${listings_tag}.txt"

# download quality signals
while read line; do
  url="${BASE_URL}/quality_signals/${line}.signals.json.gz"
  dest="quality_signals/${line}.signals.json.gz"
  mkdir -p $(dirname $dest)
  wget "$url" -O "$dest"
done <"$listings_file"


# download other components
COMPS=("minhash" "duplicates")
for comp in "${COMPS[@]}"; do
  while read line; do
    url="${BASE_URL}/${comp}/${line}.${comp}.parquet"
    dest="${comp}/${line}.${comp}.parquet"
    mkdir -p $(dirname $dest)
    wget "$url" -O "$dest"
  done <"$listings_file"
done
```

### Applying Filtering Rules

You can use the quality signals to filter the raw RedPajama-V2 dataset for a given set of rules. For example, consider
the following set of rules used in Gopher:

```python
def gopher_rules_pass(sample) -> bool:
    """ function returns True if the sample complies with Gopher rules """
    signals = json.loads(sample["quality_signals"])

    # rule 1: number of words between 50 and 10'000
    word_count = signals["rps_doc_word_count"][0][2]
    if word_count < 50 or word_count > 100_000:
        return False

    # rule 2: mean word length between 3 and 10
    mean_word_length = signals["rps_doc_mean_word_length"][0][2]
    if mean_word_length < 3 or mean_word_length > 10:
        return False

    # rule 2: symbol to word ratio below 0.1
    symbol_word_ratio = signals["rps_doc_symbol_to_word_ratio"][0][2]
    if symbol_word_ratio > 0.1:
        return False

    # rule 3: 90% of lines need to start without a bullet point
    n_lines = signals["ccnet_nlines"][0][2]
    n_lines_bulletpoint_start = sum(map(lambda ln: ln[2], signals["rps_lines_start_with_bulletpoint"]))
    if n_lines_bulletpoint_start / n_lines > 0.9:
        return False

    # rule 4: the ratio between characters in the most frequent 2-gram and the total number 
    # of characters must be below 0.2
    top_2_gram_frac = signals["rps_doc_frac_chars_top_2gram"][0][2]
    if top_2_gram_frac > 0.2:
        return False

    # rule 5: ...

    return True
```

Filtering the RedPajama-V2 dataset with this set of rules is then as easy as:

```python
ds_iterator = load_dataset(
    "togethercomputer/RedPajama-Data-V2",
    snapshots=["2023-14"],
    languages=["en"],
    name="default",
    streaming=True
)

filtered_dataset = []

for sample in ds_iterator["train"]:

    if not gopher_rules_pass(sample):
        continue

    filtered_dataset.append(sample)
```

### Dataset Summary

RedPajama-V2 is an open dataset for training large language models and includes over 100B text documents. Out of these,
30B documents come with quality annotations. Out of these, there are 20B unique documents.

#### Quality Annotations

| Annotation Tag                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                          | Category         | Reference                                                                                                                     |
|------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------|
| ccnet_bucket                                   | head, middle or tail bucket of the perplexity score                                                                                                                                                                                                                                                                                                                                                                  | CCNet            | [CCNet](https://github.com/facebookresearch/cc_net)                                                                           |
| ccnet_language_score                           | score of the language identification model                                                                                                                                                                                                                                                                                                                                                                           | CCNet            | [CCNet](https://github.com/facebookresearch/cc_net)                                                                           |
| ccnet_length                                   | number of characters                                                                                                                                                                                                                                                                                                                                                                                                 | CCNet            | [CCNet](https://github.com/facebookresearch/cc_net)                                                                           |
| ccnet_nlines                                   | number of lines                                                                                                                                                                                                                                                                                                                                                                                                      | CCNet            | [CCNet](https://github.com/facebookresearch/cc_net)                                                                           |
| ccnet_original_length                          | number of characters before line-level deduplication                                                                                                                                                                                                                                                                                                                                                           | CCNet            | [CCNet](https://github.com/facebookresearch/cc_net)                                                                           |
| ccnet_original_nlines                          | number of lines before line-level deduplication                                                                                                                                                                                                                                                                                                                                                                | CCNet            | [CCNet](https://github.com/facebookresearch/cc_net)                                                                           |
| ccnet_perplexity                               | perplexity of an LM trained on Wikipedia                                                                                                                                                                                                                                                                                                                                                                             | CCNet            | [CCNet](https://github.com/facebookresearch/cc_net)                                                                           |
| rps_doc_books_importance                       | Given a bag of {1,2}-wordgram model trained on Books p, and a model trained on the source domain q, This is the logarithm of the ratio p(doc)/q(doc).                                                                                                                                                                                                                                                                | ML Heuristics    | [Importance Resampling (Xie et al.)](https://arxiv.org/abs/2302.03169)                                                        |
| rps_doc_openwebtext_importance                 | Given a bag of {1,2}-wordgram model trained on OpenWebText p, and a model trained on the source domain q, this is the logarithm of the ratio p(doc)/q(doc).                                                                                                                                                                                                                                                          | ML Heuristics    | [Importance Resampling (Xie et al.)](https://arxiv.org/abs/2302.03169)                                                        |
| rps_doc_wikipedia_importance                   | Given a bag of {1,2}-wordgram model trained on Wikipedia articles p, and a model trained on the source domain q, this is the logarithm of the ratio p(doc)/q(doc).                                                                                                                                                                                                                                                   | ML Heuristics    | [Importance Resampling (Xie et al.)](https://arxiv.org/abs/2302.03169)                                                        |
| rps_doc_ml_wikiref_score                       | Fasttext classifier prediction for the document being a Wikipedia reference. This is the same fasttext model used in the RedPajama-1T dataset. Only applies to English data..                                                                                                                                                                                                                                        | ML Heuristics    | [LLaMA](https://arxiv.org/abs/2302.13971), [RedPajama-1T](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T) |
| rps_doc_ml_palm_score                          | Fasttext classifier prediction for the document being a Wikipedia article, OpenWebText sample or a RedPajama-V1 book. Only for English data.                                                                                                                                                                                                                                                                         | ML Heuristics    | [PALM](https://arxiv.org/abs/2204.02311), [GLaM](https://arxiv.org/abs/2112.06905)                                            |
| rps_doc_ml_wikipedia_score                     | Fasttext classifier prediction for the document being a Wikipedia article. This is used for non-English data                                                                                                                                                                                                                                                                                                         | ML Heuristics    | -                                                                                                                             |
| rps_doc_curly_bracket                          | The ratio between the number of occurrences of '{' or '}' and the number of characters in the raw text.                                                                                                                                                                                                                                                                                                              | Natural Language | [C4](https://arxiv.org/abs/1910.10683)                                                                                        |
| rps_doc_frac_all_caps_words                    | The fraction of words in the content that only consist of uppercase letters. This is based on the raw content.                                                                                                                                                                                                                                                                                                       | Natural Language | [Pretrainer’s Guide](https://arxiv.org/abs/2305.13169)                                                                        |
| rps_doc_frac_lines_end_with_ellipsis           | The fraction of lines that end with an ellipsis, where an ellipsis is defined as either "..." or "…".                                                                                                                                                                                                                                                                                                                | Natural Language | [RefinedWeb](https://arxiv.org/abs/2306.01116), [Gopher](https://arxiv.org/abs/2112.11446)                                    |
| rps_doc_frac_no_alph_words                     | The fraction of words that contain no alphabetical character.                                                                                                                                                                                                                                                                                                                                                        | Natural Language | [RefinedWeb](https://arxiv.org/abs/2306.01116), [Gopher](https://arxiv.org/abs/2112.11446)                                    |
| rps_doc_lorem_ipsum                            | The ratio between the number of occurrences of 'lorem ipsum' and the number of characters in the content after normalisation.                                                                                                                                                                                                                                                                                        | Natural Language | [C4](https://arxiv.org/abs/1910.10683)                                                                                        |
| rps_doc_mean_word_length                       | The mean length of words in the content after normalisation.                                                                                                                                                                                                                                                                                                                                                         | Natural Language | [RefinedWeb](https://arxiv.org/abs/2306.01116), [Gopher](https://arxiv.org/abs/2112.11446)                                    |
| rps_doc_stop_word_fraction                     | The ratio between the number of stop words and the number of words in the document. Stop words are obtained from the [stopwords-json](https://github.com/6/stopwords-json) repo.                                                                                                                                                                                                                                     | Natural Language | [RefinedWeb](https://arxiv.org/abs/2306.01116), [Gopher](https://arxiv.org/abs/2112.11446)                                    |
| rps_doc_symbol_to_word_ratio                   | The ratio of symbols to words in the content.. Symbols are defined "#", "...", and "…".                                                                                                                                                                                                                                                                                                                              | Natural Language | [RefinedWeb](https://arxiv.org/abs/2306.01116), [Gopher](https://arxiv.org/abs/2112.11446)                                    |
| rps_doc_frac_unique_words                      | The fraction of unique words in the content. This is also known as the degeneracy of a text sample. Calculated based on the normalised content.                                                                                                                                                                                                                                                                      | Natural Language | [Pretrainer’s Guide](https://arxiv.org/abs/2305.13169)                                                                        |
| rps_doc_unigram_entropy                        | The entropy of the unigram distribution of the content. This measures the diversity of the content and is computed using sum(-x / total * log(x / total)) where the sum is taken over counts of unique words in the normalised content.                                                                                                                                                                              | Natural Language | -                                                                                                                             |
| rps_doc_word_count                             | The number of words in the content after normalisation.                                                                                                                                                                                                                                                                                                                                                              | Natural Language | [RefinedWeb](https://arxiv.org/abs/2306.01116), [Gopher](https://arxiv.org/abs/2112.11446)                                    |
| rps_lines_ending_with_terminal_punctution_mark | Indicates whether a line ends with a terminal punctuation mark. A terminal punctation mark is defined as one of: ".", "!", "?", "”".                                                                                                                                                                                                                                                                                 | Natural Language | [C4](https://arxiv.org/abs/1910.10683)                                                                                        |
| rps_lines_javascript_counts                    | The number of occurrences of the word "javascript" in each line.                                                                                                                                                                                                                                                                                                                                                     | Natural Language | [C4](https://arxiv.org/abs/1910.10683)                                                                                        |
| rps_lines_num_words                            | The number of words in each line. This is computed based on the normalised text.                                                                                                                                                                                                                                                                                                                                     | Natural Language | [C4](https://arxiv.org/abs/1910.10683) , [RefinedWeb](https://arxiv.org/abs/2306.01116)                                       |
| rps_lines_numerical_chars_fraction             | The ratio between the number of numerical characters and total number of characters in each line. This is based on the normalised content.                                                                                                                                                                                                                                                                           | Natural Language | [RefinedWeb](https://arxiv.org/abs/2306.01116)                                                                                |
| rps_lines_start_with_bulletpoint               | Whether the lines that start with a bullet point symbol. The following set of unicodes are considered a bullet point: \u2022 (bullet point), \u2023 (triangular bullet point), \u25B6 (black right pointing triangle), \u25C0 (black left pointing triangle), \u25E6 (white bullet point), \u25A0 (black square), \u25A1 (white square), \u25AA (black small square), \u25AB (white small square), \u2013 (en dash). | Natural Language | [RefinedWeb](https://arxiv.org/abs/2306.01116), [Gopher](https://arxiv.org/abs/2112.11446)                                    |
| rps_lines_uppercase_letter_fraction            | The ratio between the number of uppercase letters and total number of characters in each line. This is based on the raw text.                                                                                                                                                                                                                                                                                        | Natural Language | [RefinedWeb](https://arxiv.org/abs/2306.01116)                                                                                |
| rps_doc_num_sentences                          | The number of sentences in the content. This is calculated using the regular expression `r'\b[^.!?]+[.!?]*'`.                                                                                                                                                                                                                                                                                                        | Natural Language | [C4](https://arxiv.org/abs/1910.10683)                                                                                        |
| rps_doc_frac_chars_dupe_10grams                | The fraction of characters in duplicate word 10grams. This operates on the lower-cased, punctuation removed content. It is also ensured that characters in overlapping ngrams are only counted once.                                                                                                                                                                                                                 | Repetitiveness   | [RefinedWeb](https://arxiv.org/abs/2306.01116), [Gopher](https://arxiv.org/abs/2112.11446)                                    |
| rps_doc_frac_chars_dupe_5grams                 | The fraction of characters in duplicate word 5grams.                                                                                                                                                                                                                                                                                                                                                                 | Repetitiveness   | [RefinedWeb](https://arxiv.org/abs/2306.01116), [Gopher](https://arxiv.org/abs/2112.11446)                                    |
| rps_doc_frac_chars_dupe_6grams                 | The fraction of characters in duplicate word 6grams.                                                                                                                                                                                                                                                                                                                                                                 | Repetitiveness   | [RefinedWeb](https://arxiv.org/abs/2306.01116), [Gopher](https://arxiv.org/abs/2112.11446)                                    |
| rps_doc_frac_chars_dupe_7grams                 | The fraction of characters in duplicate word 7grams.                                                                                                                                                                                                                                                                                                                                                                 | Repetitiveness   | [RefinedWeb](https://arxiv.org/abs/2306.01116), [Gopher](https://arxiv.org/abs/2112.11446)                                    |
| rps_doc_frac_chars_dupe_8grams                 | The fraction of characters in duplicate word 8grams.                                                                                                                                                                                                                                                                                                                                                                 | Repetitiveness   | [RefinedWeb](https://arxiv.org/abs/2306.01116), [Gopher](https://arxiv.org/abs/2112.11446)                                    |
| rps_doc_frac_chars_dupe_9grams                 | The fraction of characters in duplicate word 9grams.                                                                                                                                                                                                                                                                                                                                                                 | Repetitiveness   | [RefinedWeb](https://arxiv.org/abs/2306.01116), [Gopher](https://arxiv.org/abs/2112.11446)                                    |
| rps_doc_frac_chars_top_2gram                   | The fraction of characters in the top word 2gram.                                                                                                                                                                                                                                                                                                                                                                    | Repetitiveness   | [RefinedWeb](https://arxiv.org/abs/2306.01116), [Gopher](https://arxiv.org/abs/2112.11446)                                    |
| rps_doc_frac_chars_top_3gram                   | The fraction of characters in the top word 3gram.                                                                                                                                                                                                                                                                                                                                                                    | Repetitiveness   | [RefinedWeb](https://arxiv.org/abs/2306.01116), [Gopher](https://arxiv.org/abs/2112.11446)                                    |
| rps_doc_frac_chars_top_4gram                   | The fraction of characters in the top word 4gram.                                                                                                                                                                                                                                                                                                                                                                    | Repetitiveness   | [RefinedWeb](https://arxiv.org/abs/2306.01116), [Gopher](https://arxiv.org/abs/2112.11446)                                    |
| rps_doc_ldnoobw_words                          | The number of sequences of words that are contained in the List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words blocklist. The blocklist is obtained from the [LDNOOBW](https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words) repo.                                                                                                                                                     | toxicity         | [C4](https://arxiv.org/abs/1910.10683)                                                                                        |
| rps_doc_ut1_blacklist                          | A categorical id corresponding to the list of categories of the domain of the document. Categories are obtained from the UT1 blacklist. The list is obtained from [UT-Capitole](https://dsi.ut-capitole.fr/blacklists/).                                                                                                                                                                                             | toxicictiy       | [RefinedWeb](https://arxiv.org/abs/2306.01116)                                                                                |
| minhash_signature_0.7                          | Banded minhash signature of the document, for fuzzy deduplication at Jaccard similarity 0.7. The signature is based on 128 hash functions and grouped into 14 bands and 9 rows for LSH.                                                                                                                                                                                                                              | Deduplication    |
| minhash_signature_0.8                          | Banded minhash signature of the document, for fuzzy deduplication at Jaccard similarity 0.8. The signature is based on 128 hash functions and grouped into 9 bands and 13 rows for LSH.                                                                                                                                                                                                                              | Deduplication    |
| minhash_signature_0.9                          | Banded minhash signature of the document, for fuzzy deduplication at Jaccard similarity 0.9. The signature is based on 128 hash functions and grouped into 5 bands and 25 rows for LSH..                                                                                                                                                                                                                             | Deduplication    |
| minhash_signature_1.0                          | Banded minhash signature of the document, for fuzzy deduplication at Jaccard similarity 1.0. The signature is based on 128 hash functions and grouped into 1 band and 128 rows for LSH.                                                                                                                                                                                                                              | Deduplication    |


The quality signal `rps_doc_ut1_blacklist` is given by a categorical id indicating the UT1 blacklisted 
domain categories to which the domain of the document belongs. The mapping `id -> [category_1, ..., category_k]` is given in
`ut1_domain_categories.json`. It can also be downloaded from this [link](https://data.together.xyz/redpajama-data-v2/v1.0.0/artifacts/ut1_domain_categories.json).

#### Raw Document and Token Counts (`head_middle`)

|       | # Documents (deduped) | Estimated Token count (deduped) |
|-------|-----------------------|---------------------------------|
| en    | 24.5B                 | 37.0T                           |
| de    | 2.7B                  | 4.1T                            |
| fr    | 2.2B                  | 3.7T                            |  
| es    | 2.3B                  | 3.9T                            |
| it    | 1.2B                  | 1.9T                            |
| Total | 32.9B                 | 50.6T                           |

#### Deduplicated Document and Token Counts (`head_middle`)

|       | # Documents (total) | Estimated Token count (total) |
|-------|---------------------|-------------------------------|
| en    | 14.5B               | 20.5T                         |
| de    | 1.9B                | 3.0T                          |
| fr    | 1.6B                | 2.7T                          |  
| es    | 1.8B                | 2.8T                          |
| it    | 0.9B                | 1.5T                          |
| Total | 20.8B               | 30.4T                         |

### Languages

English, German, French, Italian, Spanish

## Dataset Structure

The dataset is structured into four components, each following the same key structure:

```
├── documents
    ├── 2018-43
        ├── 0000
            ├── en_head.json.gz
            ├── ...
            ├── it_middle.json.gz
├── quality_signals
    ├── 2018-43
        ├── 0000
            ├── en_head.signals.json.gz
            ├── ...
            ├── it_middle.json.gz
├── duplicates
    ├── 2018-43
        ├── 0000
            ├── en_head.duplicates.parquet
            ├── ...
            ├── it_middle.duplicates.parquet
├── minhash
    ├── 2018-43
        ├── 0000
            ├── en_head.minhash.parquet
            ├── ...
            ├── it_middle.minhash.parquet
```

Documents files, which contain the text, folow the schema defined by CCNet:

```json
{
  "url": "...",
  "date_download": "2014-08-20T06:48:26Z",
  "digest": "sha1:46OPKWZ7MAG5624VYYA3U3YH2MJ727B6",
  "length": 1095,
  "nlines": 8,
  "source_domain": "...",
  "title": "...",
  "raw_content": "Dear ...",
  "cc_segment": "crawl-data/CC-MAIN-2014-35/...",
  "original_nlines": 11,
  "original_length": 1174,
  "line_ids": [
    0,
    1,
    3,
    4,
    6,
    7,
    8,
    9
  ],
  "language": "en",
  "language_score": 0.92,
  "perplexity": 217.2,
  "bucket": "head"
}
```

The quality signals follow the schema

```json
{
  "id": "2018-43/0000/en_head.json.gz/0",
  "id_int": 7972430436813205988,
  "metadata": {
    "cc_segment": "crawl-data/...",
    "cc_net_source": "2018-43/0000/en_head.json.gz",
    "url": "...",
    "source_domain": "...",
    "language": "en",
    "snapshot_id": "2018-43"
  },
  "quality_signals": {
    "ccnet_original_length": [
      [
        0,
        7033,
        8711.0
      ]
    ],
    ...,
    "rps_doc_stop_word_fraction": [
      [
        0,
        7033,
        0.45121107
      ]
    ],
    "rps_lines_num_words": [
      [
        0,
        25,
        2
      ],
      ...,
      [
        6980,
        7033,
        10
      ]
    ]
  }
}
```

where signal scores are encoded as a list of tuples `(start, end, score)`, where `start` and `end` are the locations in
the `raw_content` string where the `score` applies.

## Dataset Creation

The dataset is based on 84 snapshots provided by Common Crawl. Each snapshot was processed using the CCNet pipeline and
split into `head` `middle` `tail` buckets, depending on the perplexity score. In a second step, the documents in the
`head` and `middle` buckets were annotated with the quality signals described above. Finally, the documents were
deduplicated based on the text, using a Bloomfilter. The duplicates were kept in the dataset, but are marked in the
`duplicates` component.

## Citation

To cite RedPajama, please use:

```
@software{together2023redpajama,
  author = {Together Computer},
  title = {RedPajama: an Open Dataset for Training Large Language Models},
  month = October,
  year = 2023,
  url = {https://github.com/togethercomputer/RedPajama-Data}
}
```

You can also cite the paper describing this dataset

```bibtex
@misc{weber2024redpajamaopendatasettraining,
      title={RedPajama: an Open Dataset for Training Large Language Models}, 
      author={Maurice Weber and Daniel Fu and Quentin Anthony and Yonatan Oren and Shane Adams and Anton Alexandrov and Xiaozhong Lyu and Huu Nguyen and Xiaozhe Yao and Virginia Adams and Ben Athiwaratkun and Rahul Chalamala and Kezhen Chen and Max Ryabinin and Tri Dao and Percy Liang and Christopher Ré and Irina Rish and Ce Zhang},
      year={2024},
      eprint={2411.12372},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2411.12372}, 
}
```


## Acknowledgements

We are appreciative to so many partners and collaborators that together are pushing forward the frontier of open LLM
models.

- Thank you to the OLMo team at AI2 and friends at OpenGPT-X for the insightful discussions about datasets and data
  quality! Also for everyone who builds on the RedPajama dataset, including Cerebras for their SlimPajama efforts, and
  the over 500 models built on RedPajam to date by the open-source AI community.
- We are grateful to the great team at EleutherAI for paving the path on open training datasets with The Pile and for
  open-sourcing code we use in training some of the RedPajama models.
- Thank you to our partners of RedPajama-v1, including Ontocord.ai, MILA Québec AI Institute, ETH DS3Lab, Université de
  Montréal, Stanford Center for Research on Foundation Models (CRFM), Stanford Hazy Research research group and LAION.

## License

Please refer to the [Common Crawl Foundation Terms of Use](https://commoncrawl.org/terms-of-use) for the data.
The code used to load and process the dataset is licensed under the Apache 2.0 license.

<!--
### Annotations
#### Annotation process
[More Information Needed]
#### Who are the annotators?
[More Information Needed]
### Personal and Sensitive Information
[More Information Needed]
## Considerations for Using the Data
### Social Impact of Dataset
[More Information Needed]
### Discussion of Biases
[More Information Needed]
### Other Known Limitations
[More Information Needed]
## Additional Information
### Dataset Curators
[More Information Needed]
### Licensing Information
[More Information Needed]
### Citation Information
[More Information Needed]
### Contributions
[More Information Needed]
-->