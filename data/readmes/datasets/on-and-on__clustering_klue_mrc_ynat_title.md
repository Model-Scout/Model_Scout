---
language:
- ko
license: cc-by-sa-4.0
size_categories:
- n<1K
dataset_info:
  config_name: kor-Hang
  features:
  - name: guid
    dtype: string
  - name: text
    dtype: string
  - name: category
    dtype: string
  - name: label
    dtype: int64
  - name: text_len
    dtype: int64
  splits:
  - name: test
    num_bytes: 124434
    num_examples: 904
  download_size: 69707
  dataset_size: 124434
configs:
- config_name: kor-Hang
  data_files:
  - split: test
    path: kor-Hang/test-*
---
This dataset is a processed and redistributed version of the KLUE dataset and follows the KLUE license.
(https://huggingface.co/datasets/klue/klue)

It is a dataset for embedding evaluation, processed using the categories from the KLUE-mrc & KLUE-ynat dataset.

- Task: Clustering
- News_category: IT/Science, Sports, Media/Culture, Ecomomy/Finance, Real Estate


========================================Original Citation===========================================


### Citation Information
```bibtex
  @misc{park2021klue,
        title={KLUE: Korean Language Understanding Evaluation}, 
        author={Sungjoon Park and Jihyung Moon and Sungdong Kim and Won Ik Cho and Jiyoon Han and Jangwon Park and Chisung Song and Junseong Kim and Yongsook Song and Taehwan Oh and Joohong Lee and Juhyun Oh and Sungwon Lyu and Younghoon Jeong and Inkwon Lee and Sangwoo Seo and Dongjun Lee and Hyunwoo Kim and Myeonghwa Lee and Seongbo Jang and Seungwon Do and Sunkyoung Kim and Kyungtae Lim and Jongwon Lee and Kyumin Park and Jamin Shin and Seonghyun Kim and Lucy Park and Alice Oh and Jungwoo Ha and Kyunghyun Cho},
        year={2021},
        eprint={2105.09680},
        archivePrefix={arXiv},
        primaryClass={cs.CL}
  }
```
