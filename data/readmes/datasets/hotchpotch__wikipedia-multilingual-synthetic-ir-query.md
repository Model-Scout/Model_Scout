---
language:
- ar
- de
- en
- es
- fr
- it
- ja
- ko
- pt
- ru
- zh
license:
- cc-by-sa-4.0
- gfdl
multilinguality: multilingual
task_categories:
- text-retrieval
source_datasets:
- singletongue/wikipedia-paragraphs
- hotchpotch/wikipedia-multilingual-ir-pairs
configs:
- config_name: ar-long_doc
  data_files:
  - split: train
    path: ar-long_doc/train-*
- config_name: ar-short_doc
  data_files:
  - split: train
    path: ar-short_doc/train-*
- config_name: de-long_doc
  data_files:
  - split: train
    path: de-long_doc/train-*
- config_name: de-short_doc
  data_files:
  - split: train
    path: de-short_doc/train-*
- config_name: en-long_doc
  data_files:
  - split: train
    path: en-long_doc/train-*
- config_name: en-short_doc
  data_files:
  - split: train
    path: en-short_doc/train-*
- config_name: es-long_doc
  data_files:
  - split: train
    path: es-long_doc/train-*
- config_name: es-short_doc
  data_files:
  - split: train
    path: es-short_doc/train-*
- config_name: fr-long_doc
  data_files:
  - split: train
    path: fr-long_doc/train-*
- config_name: fr-short_doc
  data_files:
  - split: train
    path: fr-short_doc/train-*
- config_name: it-long_doc
  data_files:
  - split: train
    path: it-long_doc/train-*
- config_name: it-short_doc
  data_files:
  - split: train
    path: it-short_doc/train-*
- config_name: ja-long_doc
  data_files:
  - split: train
    path: ja-long_doc/train-*
- config_name: ja-short_doc
  data_files:
  - split: train
    path: ja-short_doc/train-*
- config_name: ko-long_doc
  data_files:
  - split: train
    path: ko-long_doc/train-*
- config_name: ko-short_doc
  data_files:
  - split: train
    path: ko-short_doc/train-*
- config_name: pt-long_doc
  data_files:
  - split: train
    path: pt-long_doc/train-*
- config_name: pt-short_doc
  data_files:
  - split: train
    path: pt-short_doc/train-*
- config_name: ru-long_doc
  data_files:
  - split: train
    path: ru-long_doc/train-*
- config_name: ru-short_doc
  data_files:
  - split: train
    path: ru-short_doc/train-*
- config_name: zh-long_doc
  data_files:
  - split: train
    path: zh-long_doc/train-*
- config_name: zh-short_doc
  data_files:
  - split: train
    path: zh-short_doc/train-*
dataset_info:
- config_name: ar-long_doc
  features:
  - name: query
    dtype: string
  - name: document
    dtype: string
  - name: instruction_type
    dtype: string
  - name: title_section
    dtype: string
  - name: query_source_text_start
    dtype: int32
  - name: query_source_text_end
    dtype: int32
  - name: query_source_text_length
    dtype: int32
  - name: document_length
    dtype: int32
  splits:
  - name: train
    num_bytes: 2177856622
    num_examples: 208667
  download_size: 1006151733
  dataset_size: 2177856622
- config_name: ar-short_doc
  features:
  - name: query
    dtype: string
  - name: document
    dtype: string
  - name: instruction_type
    dtype: string
  - name: title_section
    dtype: string
  - name: document_length
    dtype: int32
  splits:
  - name: train
    num_bytes: 2460391357
    num_examples: 1634401
  download_size: 834916811
  dataset_size: 2460391357
- config_name: de-long_doc
  features:
  - name: query
    dtype: string
  - name: document
    dtype: string
  - name: instruction_type
    dtype: string
  - name: title_section
    dtype: string
  - name: query_source_text_start
    dtype: int32
  - name: query_source_text_end
    dtype: int32
  - name: query_source_text_length
    dtype: int32
  - name: document_length
    dtype: int32
  splits:
  - name: train
    num_bytes: 8159506142
    num_examples: 1438985
  download_size: 4896365550
  dataset_size: 8159506142
- config_name: de-short_doc
  features:
  - name: query
    dtype: string
  - name: document
    dtype: string
  - name: instruction_type
    dtype: string
  - name: title_section
    dtype: string
  - name: document_length
    dtype: int32
  splits:
  - name: train
    num_bytes: 8385810830
    num_examples: 9257137
  download_size: 3585386030
  dataset_size: 8385810830
- config_name: en-long_doc
  features:
  - name: query
    dtype: string
  - name: document
    dtype: string
  - name: instruction_type
    dtype: string
  - name: title_section
    dtype: string
  - name: query_source_text_start
    dtype: int32
  - name: query_source_text_end
    dtype: int32
  - name: query_source_text_length
    dtype: int32
  - name: document_length
    dtype: int32
  splits:
  - name: train
    num_bytes: 17693095831
    num_examples: 2702969
  download_size: 10338866532
  dataset_size: 17693095831
- config_name: en-short_doc
  features:
  - name: query
    dtype: string
  - name: document
    dtype: string
  - name: instruction_type
    dtype: string
  - name: title_section
    dtype: string
  - name: document_length
    dtype: int32
  splits:
  - name: train
    num_bytes: 17177196961
    num_examples: 19214857
  download_size: 7376127655
  dataset_size: 17177196961
- config_name: es-long_doc
  features:
  - name: query
    dtype: string
  - name: document
    dtype: string
  - name: instruction_type
    dtype: string
  - name: title_section
    dtype: string
  - name: query_source_text_start
    dtype: int32
  - name: query_source_text_end
    dtype: int32
  - name: query_source_text_length
    dtype: int32
  - name: document_length
    dtype: int32
  splits:
  - name: train
    num_bytes: 5245412646
    num_examples: 778955
  download_size: 3099197252
  dataset_size: 5245412646
- config_name: es-short_doc
  features:
  - name: query
    dtype: string
  - name: document
    dtype: string
  - name: instruction_type
    dtype: string
  - name: title_section
    dtype: string
  - name: document_length
    dtype: int32
  splits:
  - name: train
    num_bytes: 5040477794
    num_examples: 5587295
  download_size: 2135299859
  dataset_size: 5040477794
- config_name: fr-long_doc
  features:
  - name: query
    dtype: string
  - name: document
    dtype: string
  - name: instruction_type
    dtype: string
  - name: title_section
    dtype: string
  - name: query_source_text_start
    dtype: int32
  - name: query_source_text_end
    dtype: int32
  - name: query_source_text_length
    dtype: int32
  - name: document_length
    dtype: int32
  splits:
  - name: train
    num_bytes: 7008733224
    num_examples: 1010446
  download_size: 4058514993
  dataset_size: 7008733224
- config_name: fr-short_doc
  features:
  - name: query
    dtype: string
  - name: document
    dtype: string
  - name: instruction_type
    dtype: string
  - name: title_section
    dtype: string
  - name: document_length
    dtype: int32
  splits:
  - name: train
    num_bytes: 6571197903
    num_examples: 7213144
  download_size: 2643940601
  dataset_size: 6571197903
- config_name: it-long_doc
  features:
  - name: query
    dtype: string
  - name: document
    dtype: string
  - name: instruction_type
    dtype: string
  - name: title_section
    dtype: string
  - name: query_source_text_start
    dtype: int32
  - name: query_source_text_end
    dtype: int32
  - name: query_source_text_length
    dtype: int32
  - name: document_length
    dtype: int32
  splits:
  - name: train
    num_bytes: 4234757173
    num_examples: 650885
  download_size: 2545332517
  dataset_size: 4234757173
- config_name: it-short_doc
  features:
  - name: query
    dtype: string
  - name: document
    dtype: string
  - name: instruction_type
    dtype: string
  - name: title_section
    dtype: string
  - name: document_length
    dtype: int32
  splits:
  - name: train
    num_bytes: 4021868484
    num_examples: 4580724
  download_size: 1703490901
  dataset_size: 4021868484
- config_name: ja-long_doc
  features:
  - name: query
    dtype: string
  - name: document
    dtype: string
  - name: instruction_type
    dtype: string
  - name: title_section
    dtype: string
  - name: query_source_text_start
    dtype: int32
  - name: query_source_text_end
    dtype: int32
  - name: query_source_text_length
    dtype: int32
  - name: document_length
    dtype: int32
  splits:
  - name: train
    num_bytes: 5122353610
    num_examples: 566947
  download_size: 2880985795
  dataset_size: 5122353610
- config_name: ja-short_doc
  features:
  - name: query
    dtype: string
  - name: document
    dtype: string
  - name: instruction_type
    dtype: string
  - name: title_section
    dtype: string
  - name: document_length
    dtype: int32
  splits:
  - name: train
    num_bytes: 5087793844
    num_examples: 4308858
  download_size: 1931060939
  dataset_size: 5087793844
- config_name: ko-long_doc
  features:
  - name: query
    dtype: string
  - name: document
    dtype: string
  - name: instruction_type
    dtype: string
  - name: title_section
    dtype: string
  - name: query_source_text_start
    dtype: int32
  - name: query_source_text_end
    dtype: int32
  - name: query_source_text_length
    dtype: int32
  - name: document_length
    dtype: int32
  splits:
  - name: train
    num_bytes: 1149422081
    num_examples: 155140
  download_size: 655227964
  dataset_size: 1149422081
- config_name: ko-short_doc
  features:
  - name: query
    dtype: string
  - name: document
    dtype: string
  - name: instruction_type
    dtype: string
  - name: title_section
    dtype: string
  - name: document_length
    dtype: int32
  splits:
  - name: train
    num_bytes: 1174084810
    num_examples: 1200969
  download_size: 492580781
  dataset_size: 1174084810
- config_name: pt-long_doc
  features:
  - name: query
    dtype: string
  - name: document
    dtype: string
  - name: instruction_type
    dtype: string
  - name: title_section
    dtype: string
  - name: query_source_text_start
    dtype: int32
  - name: query_source_text_end
    dtype: int32
  - name: query_source_text_length
    dtype: int32
  - name: document_length
    dtype: int32
  splits:
  - name: train
    num_bytes: 2274693443
    num_examples: 333821
  download_size: 1353318497
  dataset_size: 2274693443
- config_name: pt-short_doc
  features:
  - name: query
    dtype: string
  - name: document
    dtype: string
  - name: instruction_type
    dtype: string
  - name: title_section
    dtype: string
  - name: document_length
    dtype: int32
  splits:
  - name: train
    num_bytes: 2284537837
    num_examples: 2560206
  download_size: 985898037
  dataset_size: 2284537837
- config_name: ru-long_doc
  features:
  - name: query
    dtype: string
  - name: document
    dtype: string
  - name: instruction_type
    dtype: string
  - name: title_section
    dtype: string
  - name: query_source_text_start
    dtype: int32
  - name: query_source_text_end
    dtype: int32
  - name: query_source_text_length
    dtype: int32
  - name: document_length
    dtype: int32
  splits:
  - name: train
    num_bytes: 8274476958
    num_examples: 797628
  download_size: 4063510025
  dataset_size: 8274476958
- config_name: ru-short_doc
  features:
  - name: query
    dtype: string
  - name: document
    dtype: string
  - name: instruction_type
    dtype: string
  - name: title_section
    dtype: string
  - name: document_length
    dtype: int32
  splits:
  - name: train
    num_bytes: 10044433155
    num_examples: 6423428
  download_size: 3292915102
  dataset_size: 10044433155
- config_name: zh-long_doc
  features:
  - name: query
    dtype: string
  - name: document
    dtype: string
  - name: instruction_type
    dtype: string
  - name: title_section
    dtype: string
  - name: query_source_text_start
    dtype: int32
  - name: query_source_text_end
    dtype: int32
  - name: query_source_text_length
    dtype: int32
  - name: document_length
    dtype: int32
  splits:
  - name: train
    num_bytes: 1766204879
    num_examples: 225622
  download_size: 1150645920
  dataset_size: 1766204879
- config_name: zh-short_doc
  features:
  - name: query
    dtype: string
  - name: document
    dtype: string
  - name: instruction_type
    dtype: string
  - name: title_section
    dtype: string
  - name: document_length
    dtype: int32
  splits:
  - name: train
    num_bytes: 2698851155
    num_examples: 2505946
  download_size: 1137315195
  dataset_size: 2698851155
---
# wikipedia-multilingual-synthetic-ir-query


This dataset contains multilingual Wikipedia-derived synthetic query-document pairs for information retrieval training.
It was created with the `query-crafter-multilingual` model, which generates search-like queries from Wikipedia text.

The current release contains two different retrieval settings:

- `short_doc`: pairs of `(query, short document)`
- `long_doc`: pairs of `(query, long document)`

These two subsets are not generated in the same way, and they should not be interpreted in the same way during training or evaluation.

## Overview

The current release covers 11 languages:

- Arabic
- German
- English
- Spanish
- French
- Italian
- Japanese
- Korean
- Portuguese
- Russian
- Chinese

It currently contains:

- `64,486,965` `short_doc` examples
- `8,870,065` `long_doc` examples
- `73,357,030` examples in total

## Short-Document Pairs

The `short_doc` subsets are standard query-passage style examples.
Each row is a pair of:

- a generated query
- a relatively short Wikipedia-derived text that directly supports that query

In other words, `short_doc` is intended to behave like a synthetic passage retrieval dataset.
The document is short enough that the query and its supporting text are usually tightly coupled.

Typical columns in `short_doc` configs are:

- `query`
- `document`
- `instruction_type`
- `title_section`
- `document_length`

## Long-Document Pairs

The `long_doc` subsets are different.
Each row is a pair of:

- a generated query
- a long Wikipedia-derived document

The important point is that the long document is **not** meant to be interpreted as "the whole document is a direct answer to the query."
Instead, the query is generated from a relevant part of the long document, and the correct evidence appears somewhere inside that document.

This means `long_doc` is closer to a long-document retrieval setting where:

- the full document is long
- only part of the document is directly relevant to the query
- the retrieval model must learn to match a query to a document that contains the answer span, not necessarily a document whose entire content is uniformly about that answer

Typical columns in `long_doc` configs are:

- `query`
- `document`
- `instruction_type`
- `title_section`
- `query_source_text_start`
- `query_source_text_end`
- `query_source_text_length`
- `document_length`

The `query_source_text_*` fields identify the source span inside the long document that was used when generating the query.

## Source and transformation

The source documents are Wikipedia-derived texts. The original content comes from Wikipedia/Wikimedia and is prepared through multilingual Wikipedia paragraph/retrieval resources such as [singletongue/wikipedia-paragraphs](https://huggingface.co/datasets/singletongue/wikipedia-paragraphs) and [hotchpotch/wikipedia-multilingual-ir-pairs](https://huggingface.co/datasets/hotchpotch/wikipedia-multilingual-ir-pairs).

This dataset modifies those source documents by generating synthetic search-like queries with `query-crafter-multilingual`. The source document text remains Wikipedia-derived; the generated query fields are intended as retrieval supervision for that text.

## How The Queries Were Created

This dataset was created with the `query-crafter-multilingual` model.
The model takes Wikipedia-derived text and generates retrieval-oriented synthetic queries in multiple styles.

The `instruction_type` field indicates the query style requested from the generator.
Typical values include:

- `query`
- `faq`
- `title`
- `summary`
- `keywords`
- `alt_query`
- `synonym_keywords`

This makes the dataset broader than a single fixed query format.
It includes question-like queries, shorter keyword-style queries, and several other synthetic search formulations.

## Important Training Caveat

This dataset is useful, but it is also important to be clear about its limitations.

Many of the generated queries in this dataset are relatively easy for IR training.
They are often more literal, more direct, and more tightly coupled to the source text than real user search queries.

Because of that, if you train an IR model only on this dataset, the model may become better mainly on simple retrieval cases and may not generalize well to harder or more realistic search behavior.

For that reason, it is recommended to use this dataset together with other retrieval datasets, especially datasets that include:

- more natural user queries
- harder negatives
- more indirect or ambiguous information needs
- broader domain variation beyond synthetic Wikipedia supervision

In practice, this dataset is better treated as one useful component in a mixed training recipe, not as the only source of IR supervision.

## Dataset Structure

The dataset is organized by language and document setting.
Each config corresponds to one language plus one of the two retrieval settings:

- `<lang>-short_doc`
- `<lang>-long_doc`

Examples include:

- `en-short_doc`
- `en-long_doc`
- `ja-short_doc`
- `ja-long_doc`

## Language Coverage And Sizes

| Language | `short_doc` | `long_doc` | Total |
| --- | ---: | ---: | ---: |
| Arabic | 1,634,401 | 208,667 | 1,843,068 |
| German | 9,257,137 | 1,438,985 | 10,696,122 |
| English | 19,214,857 | 2,702,969 | 21,917,826 |
| Spanish | 5,587,295 | 778,955 | 6,366,250 |
| French | 7,213,144 | 1,010,446 | 8,223,590 |
| Italian | 4,580,724 | 650,885 | 5,231,609 |
| Japanese | 4,308,858 | 566,947 | 4,875,805 |
| Korean | 1,200,969 | 155,140 | 1,356,109 |
| Portuguese | 2,560,206 | 333,821 | 2,894,027 |
| Russian | 6,423,428 | 797,628 | 7,221,056 |
| Chinese | 2,505,946 | 225,622 | 2,731,568 |
| **Total** | **64,486,965** | **8,870,065** | **73,357,030** |

## License

This dataset is derived from Wikipedia-based source text and synthetic query generation over that text.
Wikipedia content is distributed under Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) and GNU Free Documentation License (GFDL), where applicable. This dataset follows those original Wikipedia licensing terms. Please review the licensing terms of the upstream Wikipedia-derived datasets you use together with this dataset, and ensure that your use is compatible with those attribution/share-alike requirements.

## Acknowledgements

This dataset builds on prior multilingual Wikipedia retrieval resources and query generation work.
In particular, it depends on:

- [singletongue/wikipedia-paragraphs](https://huggingface.co/datasets/singletongue/wikipedia-paragraphs)
- multilingual Wikipedia-derived IR source datasets
- the `query-crafter-multilingual` model used for synthetic query generation

Thank you for publishing the very useful dataset [singletongue/wikipedia-paragraphs](https://huggingface.co/datasets/singletongue/wikipedia-paragraphs).
This dataset made it possible to build this IR-focused dataset quickly.

## Author

<img src="https://secon.dev/images/profile_usa.png" width="64" height="64" alt="Yuichi Tateno" /> Yuichi Tateno (@hotchpotch)
