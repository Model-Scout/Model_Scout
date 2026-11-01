---
dataset_info:
  features:
  - name: ko
    dtype: string
  - name: en
    dtype: string
  - name: sco
    dtype: float64
  splits:
  - name: train
    num_bytes: 5208883529
    num_examples: 26294677
  download_size: 3677536215
  dataset_size: 5208883529
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
task_categories:
- translation
language:
- ko
- en
---

# `quickmt` ko-en Training Corpus

Contains the following datasets downloaded with `mtdata` after deduplication and [basic filtering](https://github.com/quickmt/quickmt/blob/main/quickmt/scripts/clean.py) with `quickmt`:

* OPUS-ccaligned-v1-eng-kor
* OPUS-ccmatrix-v1-eng-kor
* OPUS-elrc_3070_wikipedia_health-v1-eng-kor
* OPUS-elrc_wikipedia_health-v1-eng-kor
* OPUS-elrc_2922-v1-eng-kor
* OPUS-gnome-v1-eng-kor
* OPUS-globalvoices-v2017q3-eng-kor
* OPUS-globalvoices-v2018q4-eng-kor
* OPUS-kde4-v2-eng-kor
* OPUS-linguatools_wikititles-v2014-eng-kor
* OPUS-mdn_web_docs-v20230925-eng-kor
* OPUS-multiccaligned-v1-eng-kor
* OPUS-nllb-v1-eng-kor
* OPUS-neulab_tedtalks-v1-eng-kor
* OPUS-opensubtitles-v2016-eng-kor
* OPUS-opensubtitles-v2018-eng-kor
* OPUS-php-v1-eng-kor
* OPUS-paracrawl-v8-eng-kor
* OPUS-paracrawl-v9-eng-kor
* OPUS-qed-v2.0a-eng-kor
* OPUS-ted2020-v1-eng-kor
* OPUS-tanzil-v1-eng-kor
* OPUS-tatoeba-v2-eng-kor
* OPUS-tatoeba-v20190709-eng-kor
* OPUS-tatoeba-v20200531-eng-kor
* OPUS-tatoeba-v20201109-eng-kor
* OPUS-tatoeba-v20210310-eng-kor
* OPUS-tatoeba-v20210722-eng-kor
* OPUS-tatoeba-v20220303-eng-kor
* OPUS-tatoeba-v20230412-eng-kor
* OPUS-ubuntu-v14.10-eng-kor
* OPUS-wikimatrix-v1-eng-kor
* OPUS-xlent-v1.2-eng-kor
* OPUS-bible_uedin-v1-eng-kor
* OPUS-tldr_pages-v20230829-eng-kor
* OPUS-wikimedia-v20210402-eng-kor
* OPUS-wikimedia-v20230407-eng-kor
* Statmt-ccaligned-1-eng-kor_KR
* ParaCrawl-paracrawl-1_bonus-eng-kor
* Facebook-wikimatrix-1-eng-kor
* Neulab-tedtalks_train-1-eng-kor
* Neulab-tedtalks_dev-1-eng-kor
* ELRC-wikipedia_health-1-eng-kor
* ELRC-hrw_dataset_v1-1-eng-kor
* LinguaTools-wikititles-2014-eng-kor