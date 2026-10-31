---
annotations_creators:
- crowdsourced
language:
- ar
- de
- en
- fr
- it
- ja
- ko
- nl
- ro
- zh
language_creators:
- expert-generated
license:
- cc-by-nc-nd-4.0
multilinguality:
- translation
pretty_name: IWSLT 2017
size_categories:
- 1M<n<10M
source_datasets:
- original
task_categories:
- translation
task_ids: []
paperswithcode_id: iwslt-2017
dataset_info:
- config_name: iwslt2017-en-it
  features:
  - name: translation
    dtype:
      translation:
        languages:
        - en
        - it
  splits:
  - name: train
    num_bytes: 46647925
    num_examples: 231619
  - name: test
    num_bytes: 305246
    num_examples: 1566
  - name: validation
    num_bytes: 200023
    num_examples: 929
  download_size: 329391132
  dataset_size: 47153194
- config_name: iwslt2017-en-nl
  features:
  - name: translation
    dtype:
      translation:
        languages:
        - en
        - nl
  splits:
  - name: train
    num_bytes: 42843933
    num_examples: 237240
  - name: test
    num_bytes: 311646
    num_examples: 1777
  - name: validation
    num_bytes: 197814
    num_examples: 1003
  download_size: 329391132
  dataset_size: 43353393
- config_name: iwslt2017-en-ro
  features:
  - name: translation
    dtype:
      translation:
        languages:
        - en
        - ro
  splits:
  - name: train
    num_bytes: 44129950
    num_examples: 220538
  - name: test
    num_bytes: 316790
    num_examples: 1678
  - name: validation
    num_bytes: 205028
    num_examples: 914
  download_size: 329391132
  dataset_size: 44651768
- config_name: iwslt2017-it-en
  features:
  - name: translation
    dtype:
      translation:
        languages:
        - it
        - en
  splits:
  - name: train
    num_bytes: 46647925
    num_examples: 231619
  - name: test
    num_bytes: 305246
    num_examples: 1566
  - name: validation
    num_bytes: 200023
    num_examples: 929
  download_size: 329391132
  dataset_size: 47153194
- config_name: iwslt2017-it-nl
  features:
  - name: translation
    dtype:
      translation:
        languages:
        - it
        - nl
  splits:
  - name: train
    num_bytes: 43033168
    num_examples: 233415
  - name: test
    num_bytes: 309725
    num_examples: 1669
  - name: validation
    num_bytes: 197774
    num_examples: 1001
  download_size: 329391132
  dataset_size: 43540667
- config_name: iwslt2017-it-ro
  features:
  - name: translation
    dtype:
      translation:
        languages:
        - it
        - ro
  splits:
  - name: train
    num_bytes: 44485169
    num_examples: 217551
  - name: test
    num_bytes: 314974
    num_examples: 1643
  - name: validation
    num_bytes: 204989
    num_examples: 914
  download_size: 329391132
  dataset_size: 45005132
- config_name: iwslt2017-nl-en
  features:
  - name: translation
    dtype:
      translation:
        languages:
        - nl
        - en
  splits:
  - name: train
    num_bytes: 42843933
    num_examples: 237240
  - name: test
    num_bytes: 311646
    num_examples: 1777
  - name: validation
    num_bytes: 197814
    num_examples: 1003
  download_size: 329391132
  dataset_size: 43353393
- config_name: iwslt2017-nl-it
  features:
  - name: translation
    dtype:
      translation:
        languages:
        - nl
        - it
  splits:
  - name: train
    num_bytes: 43033168
    num_examples: 233415
  - name: test
    num_bytes: 309725
    num_examples: 1669
  - name: validation
    num_bytes: 197774
    num_examples: 1001
  download_size: 329391132
  dataset_size: 43540667
- config_name: iwslt2017-nl-ro
  features:
  - name: translation
    dtype:
      translation:
        languages:
        - nl
        - ro
  splits:
  - name: train
    num_bytes: 41338738
    num_examples: 206920
  - name: test
    num_bytes: 320952
    num_examples: 1680
  - name: validation
    num_bytes: 202380
    num_examples: 913
  download_size: 329391132
  dataset_size: 41862070
- config_name: iwslt2017-ro-en
  features:
  - name: translation
    dtype:
      translation:
        languages:
        - ro
        - en
  splits:
  - name: train
    num_bytes: 44129950
    num_examples: 220538
  - name: test
    num_bytes: 316790
    num_examples: 1678
  - name: validation
    num_bytes: 205028
    num_examples: 914
  download_size: 329391132
  dataset_size: 44651768
- config_name: iwslt2017-ro-it
  features:
  - name: translation
    dtype:
      translation:
        languages:
        - ro
        - it
  splits:
  - name: train
    num_bytes: 44485169
    num_examples: 217551
  - name: test
    num_bytes: 314974
    num_examples: 1643
  - name: validation
    num_bytes: 204989
    num_examples: 914
  download_size: 329391132
  dataset_size: 45005132
- config_name: iwslt2017-ro-nl
  features:
  - name: translation
    dtype:
      translation:
        languages:
        - ro
        - nl
  splits:
  - name: train
    num_bytes: 41338738
    num_examples: 206920
  - name: test
    num_bytes: 320952
    num_examples: 1680
  - name: validation
    num_bytes: 202380
    num_examples: 913
  download_size: 329391132
  dataset_size: 41862070
- config_name: iwslt2017-ar-en
  features:
  - name: translation
    dtype:
      translation:
        languages:
        - ar
        - en
  splits:
  - name: train
    num_bytes: 56481059
    num_examples: 231713
  - name: test
    num_bytes: 2014296
    num_examples: 8583
  - name: validation
    num_bytes: 241206
    num_examples: 888
  download_size: 27748780
  dataset_size: 58736561
- config_name: iwslt2017-de-en
  features:
  - name: translation
    dtype:
      translation:
        languages:
        - de
        - en
  splits:
  - name: train
    num_bytes: 42608380
    num_examples: 206112
  - name: test
    num_bytes: 1608474
    num_examples: 8079
  - name: validation
    num_bytes: 210975
    num_examples: 888
  download_size: 16758320
  dataset_size: 44427829
- config_name: iwslt2017-en-ar
  features:
  - name: translation
    dtype:
      translation:
        languages:
        - en
        - ar
  splits:
  - name: train
    num_bytes: 56481059
    num_examples: 231713
  - name: test
    num_bytes: 2014296
    num_examples: 8583
  - name: validation
    num_bytes: 241206
    num_examples: 888
  download_size: 29333173
  dataset_size: 58736561
- config_name: iwslt2017-en-de
  features:
  - name: translation
    dtype:
      translation:
        languages:
        - en
        - de
  splits:
  - name: train
    num_bytes: 42608380
    num_examples: 206112
  - name: test
    num_bytes: 1608474
    num_examples: 8079
  - name: validation
    num_bytes: 210975
    num_examples: 888
  download_size: 16758334
  dataset_size: 44427829
- config_name: iwslt2017-en-fr
  features:
  - name: translation
    dtype:
      translation:
        languages:
        - en
        - fr
  splits:
  - name: train
    num_bytes: 49273286
    num_examples: 232825
  - name: test
    num_bytes: 1767465
    num_examples: 8597
  - name: validation
    num_bytes: 207579
    num_examples: 890
  download_size: 27699724
  dataset_size: 51248330
- config_name: iwslt2017-en-ja
  features:
  - name: translation
    dtype:
      translation:
        languages:
        - en
        - ja
  splits:
  - name: train
    num_bytes: 48204987
    num_examples: 223108
  - name: test
    num_bytes: 1809007
    num_examples: 8469
  - name: validation
    num_bytes: 208124
    num_examples: 871
  download_size: 26983602
  dataset_size: 50222118
- config_name: iwslt2017-en-ko
  features:
  - name: translation
    dtype:
      translation:
        languages:
        - en
        - ko
  splits:
  - name: train
    num_bytes: 51678043
    num_examples: 230240
  - name: test
    num_bytes: 1869793
    num_examples: 8514
  - name: validation
    num_bytes: 219295
    num_examples: 879
  download_size: 19364776
  dataset_size: 53767131
- config_name: iwslt2017-en-zh
  features:
  - name: translation
    dtype:
      translation:
        languages:
        - en
        - zh
  splits:
  - name: train
    num_bytes: 44271004
    num_examples: 231266
  - name: test
    num_bytes: 1605527
    num_examples: 8549
  - name: validation
    num_bytes: 202537
    num_examples: 879
  download_size: 27597071
  dataset_size: 46079068
- config_name: iwslt2017-fr-en
  features:
  - name: translation
    dtype:
      translation:
        languages:
        - fr
        - en
  splits:
  - name: train
    num_bytes: 49273286
    num_examples: 232825
  - name: test
    num_bytes: 1767465
    num_examples: 8597
  - name: validation
    num_bytes: 207579
    num_examples: 890
  download_size: 26880731
  dataset_size: 51248330
- config_name: iwslt2017-ja-en
  features:
  - name: translation
    dtype:
      translation:
        languages:
        - ja
        - en
  splits:
  - name: train
    num_bytes: 48204987
    num_examples: 223108
  - name: test
    num_bytes: 1809007
    num_examples: 8469
  - name: validation
    num_bytes: 208124
    num_examples: 871
  download_size: 26190859
  dataset_size: 50222118
- config_name: iwslt2017-ko-en
  features:
  - name: translation
    dtype:
      translation:
        languages:
        - ko
        - en
  splits:
  - name: train
    num_bytes: 51678043
    num_examples: 230240
  - name: test
    num_bytes: 1869793
    num_examples: 8514
  - name: validation
    num_bytes: 219295
    num_examples: 879
  download_size: 19364733
  dataset_size: 53767131
- config_name: iwslt2017-zh-en
  features:
  - name: translation
    dtype:
      translation:
        languages:
        - zh
        - en
  splits:
  - name: train
    num_bytes: 44271004
    num_examples: 231266
  - name: test
    num_bytes: 1605527
    num_examples: 8549
  - name: validation
    num_bytes: 202537
    num_examples: 879
  download_size: 26849290
  dataset_size: 46079068
---

# Dataset Card for IWSLT 2017

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** [https://sites.google.com/site/iwsltevaluation2017/TED-tasks](https://sites.google.com/site/iwsltevaluation2017/TED-tasks)
- **Repository:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Paper:** [Overview of the IWSLT 2017 Evaluation Campaign](https://aclanthology.org/2017.iwslt-1.1/)
- **Point of Contact:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Size of downloaded dataset files:** 4.24 GB
- **Size of the generated dataset:** 1.14 GB
- **Total amount of disk used:** 5.38 GB

*This repository contain a modified version of the loading script used in the official [iwslt2017](https://huggingface.co/datasets/iwslt2017) repository updated to include document and segment information for all available sentence pairs, enabling their usage for document-level and context-aware MT applications. Refer to the original repository for additional information.*

