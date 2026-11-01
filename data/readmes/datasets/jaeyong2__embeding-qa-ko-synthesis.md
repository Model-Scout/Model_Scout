---
dataset_info:
  features:
  - name: context
    dtype: string
  - name: sufficient
    dtype: string
  - name: positive
    sequence: string
  - name: negative
    sequence: string
  splits:
  - name: train
    num_bytes: 85127725
    num_examples: 102103
  download_size: 54640897
  dataset_size: 85127725
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: apache-2.0
language:
- ko
---
### Development Process

1. context dataset from [maywell/ko_wikidata_QA](https://huggingface.co/datasets/maywell/ko_wikidata_QA)
2. We used [deepcogito/cogito-v1-preview-qwen-14B](https://huggingface.co/deepcogito/cogito-v1-preview-qwen-14B)


## License
- deepcogito/cogito-v1-preview-qwen-14B : https://choosealicense.com/licenses/apache-2.0/

## Acknowledgement
This research is supported by **TPU Research Cloud program**.