---
language:
- ko
size_categories:
- 100K<n<1M
task_categories:
- text-classification
task_ids:
- topic-classification
paperswithcode_id: ag-news
pretty_name: AG’s News Corpus
license: unknown
dataset_info:
  features:
  - name: text
    dtype: string
  - name: label
    dtype:
      class_label:
        names:
          '0': World
          '1': Sports
          '2': Business
          '3': Sci/Tech
  - name: data_index_by_user
    dtype: int32
  splits:
  - name: train
    num_bytes: 35075728
    num_examples: 120000
  - name: test
    num_bytes: 2195191
    num_examples: 7600
  download_size: 22724153
  dataset_size: 37270919
---

# Dataset Card for ag_news

## Licensing Information & Dataset Summary
AG is a collection of more than 1 million news articles. News articles have been
gathered from more than 2000 news sources by ComeToMyHead in more than 1 year of
activity. ComeToMyHead is an academic news search engine which has been running
since July, 2004. The dataset is provided by the academic comunity for research
purposes in data mining (clustering, classification, etc), information retrieval
(ranking, search, etc), xml, data compression, data streaming, and any other
non-commercial activity. For more information, please refer to the link
http://www.di.unipi.it/~gulli/AG_corpus_of_news_articles.html .
The AG's news topic classification dataset is constructed by Xiang Zhang
(xiang.zhang@nyu.edu) from the dataset above. It is used as a text
classification benchmark in the following paper: Xiang Zhang, Junbo Zhao, Yann
LeCun. Character-level Convolutional Networks for Text Classification. Advances
in Neural Information Processing Systems 28 (NIPS 2015).

## Source Data Citation INformation

```
@inproceedings{Zhang2015CharacterlevelCN,
  title={Character-level Convolutional Networks for Text Classification},
  author={Xiang Zhang and Junbo Jake Zhao and Yann LeCun},
  booktitle={NIPS},
  year={2015}
}
```