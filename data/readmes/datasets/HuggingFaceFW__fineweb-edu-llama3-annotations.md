---
language:
- en
license: odc-by
dataset_info:
  features:
  - name: text
    dtype: string
  - name: metadata
    struct:
    - name: date
      dtype: int64
    - name: dump
      dtype: string
    - name: file_path
      dtype: string
    - name: language
      dtype: string
    - name: language_score
      dtype: float64
    - name: token_count
      dtype: int64
    - name: url
      dtype: string
  - name: prompt
    dtype: string
  - name: score
    dtype: int64
  splits:
  - name: train
    num_bytes: 3616233906.3618937
    num_examples: 467424
  download_size: 1590654012
  dataset_size: 3616233906.3618937
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

## Annotations for 📚 FineWeb-Edu classifier
This dataset contains the annotations used for training 📚 [FineWeb-Edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu) educational quality [classifier](https://huggingface.co/HuggingFaceFW/fineweb-edu-classifier). We prompt [Llama-3-70B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct) to score web pages from 🍷 [FineWeb]() based on their educational value.

**Note:** the dataset contains the FineWeb text sample, the prompt (using the first 1000 characters of the text sample) and the scores but it doesn't contain the full Llama 3 generation.