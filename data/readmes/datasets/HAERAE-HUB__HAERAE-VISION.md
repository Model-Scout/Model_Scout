---
language:
- ko
license: cc-by-4.0
task_categories:
- visual-question-answering
- question-answering
tags:
- korean
- vision-language
- multimodal
- vlm
- under-specified
size_categories:
- n<1K
dataset_info:
  features:
  - name: question_idx
    dtype: int64
  - name: source
    dtype: string
  - name: category
    dtype: string
  - name: images
    list: image
  - name: question_original
    dtype: string
  - name: question_explicit
    dtype: string
  - name: checklist
    list: string
  splits:
  - name: train
    num_bytes: 20050880
    num_examples: 165
  download_size: 19753676
  dataset_size: 20050880
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# HAERAE-VISION

A Korean visual QA benchmark featuring real-world, under-specified questions.


## Dataset Description

This dataset includes **two question types**:
- **original**: Under-specified, authentic user queries
- **explicit**: Clarified queries with full context

Both share the same images and reference answers, allowing controlled evaluation of query under-specification.


## Evaluation Code

See our [GitHub repository](https://github.com/HAE-RAE/HAERAE-VISION) for evaluation scripts.



## Citation

```
@misc{choi2026usersleaveunsaid,
      title={What Users Leave Unsaid: Under-Specified Queries Limit Vision-Language Models}, 
      author={Dasol Choi and Guijin Son and Hanwool Lee and Minhyuk Kim and Hyunwoo Ko and Teabin Lim and Ahn Eungyeol and Jungwhan Kim and Seunghyeok Hong and Youngsook Song},
      year={2026},
      eprint={2601.06165},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2601.06165}, 
}
```

## Contact

For any questions about our project:

- Dasol Choi (dasolchoi@yonsei.ac.kr)
  
