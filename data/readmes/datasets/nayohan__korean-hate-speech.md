---
dataset_info:
  features:
  - name: comments
    dtype: string
  - name: contain_gender_bias
    dtype: bool
  - name: bias
    dtype: string
  - name: hate
    dtype: string
  - name: news_title
    dtype: string
  splits:
  - name: train
    num_bytes: 1705416
    num_examples: 7896
  - name: valid
    num_bytes: 101984
    num_examples: 471
  - name: test
    num_bytes: 200963
    num_examples: 974
  download_size: 1172909
  dataset_size: 2008363
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: valid
    path: data/valid-*
  - split: test
    path: data/test-*
license: cc-by-sa-4.0
language:
- ko
tags:
- safety
---

reference: [https://github.com/kocohub/korean-hate-speech](https://github.com/kocohub/korean-hate-speech)
```
@inproceedings{moon-etal-2020-beep,
    title = "{BEEP}! {K}orean Corpus of Online News Comments for Toxic Speech Detection",
    author = "Moon, Jihyung  and
      Cho, Won Ik  and
      Lee, Junbum",
    booktitle = "Proceedings of the Eighth International Workshop on Natural Language Processing for Social Media",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.socialnlp-1.4",
    pages = "25--31",
    abstract = "Toxic comments in online platforms are an unavoidable social issue under the cloak of anonymity. Hate speech detection has been actively done for languages such as English, German, or Italian, where manually labeled corpus has been released. In this work, we first present 9.4K manually labeled entertainment news comments for identifying Korean toxic speech, collected from a widely used online news platform in Korea. The comments are annotated regarding social bias and hate speech since both aspects are correlated. The inter-annotator agreement Krippendorff{'}s alpha score is 0.492 and 0.496, respectively. We provide benchmarks using CharCNN, BiLSTM, and BERT, where BERT achieves the highest score on all tasks. The models generally display better performance on bias identification, since the hate speech detection is a more subjective issue. Additionally, when BERT is trained with bias label for hate speech detection, the prediction score increases, implying that bias and hate are intertwined. We make our dataset publicly available and open competitions with the corpus and benchmarks.",
}
```