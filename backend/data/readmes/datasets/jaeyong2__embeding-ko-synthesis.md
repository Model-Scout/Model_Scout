---
dataset_info:
  features:
  - name: context
    dtype: string
  - name: positive
    sequence: string
  - name: negative
    sequence: string
  splits:
  - name: train
    num_bytes: 221393805
    num_examples: 94916
  download_size: 134844958
  dataset_size: 221393805
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

1. context dataset from [Cohere/miracl-ko-corpus-22-12](https://huggingface.co/datasets/Cohere/miracl-ko-corpus-22-12)
2. We used [deepcogito/cogito-v1-preview-qwen-32B](https://huggingface.co/deepcogito/cogito-v1-preview-qwen-32B)


## License
- Cohere/miracl-ko-corpus-22-12 : https://choosealicense.com/licenses/apache-2.0/
- deepcogito/cogito-v1-preview-qwen-32B : https://choosealicense.com/licenses/apache-2.0/

## Acknowledgement
This research is supported by **TPU Research Cloud program**.