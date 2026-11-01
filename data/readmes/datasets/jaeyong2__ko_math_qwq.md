---
dataset_info:
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 1338992762
    num_examples: 155000
  download_size: 643957368
  dataset_size: 1338992762
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
license: other
---
 
### Development Process

1. question dataset from [kuotient/orca-math-word-problems-193k-korean](https://huggingface.co/datasets/kuotient/orca-math-word-problems-193k-korean)
2. We used [Qwen/QwQ-32B](https://huggingface.co/Qwen/QwQ-32B)


## License
- Qwen/QwQ-32B : https://huggingface.co/Qwen/QwQ-32B/blob/main/LICENSE
- kuotient/orca-math-word-problems-193k-korean : https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/cc-by-sa-4.0.md

## Acknowledgement
This research is supported by **TPU Research Cloud program**.