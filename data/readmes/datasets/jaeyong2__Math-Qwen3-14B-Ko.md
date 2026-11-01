---
dataset_info:
  features:
  - name: content
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 378343668
    num_examples: 55000
  download_size: 150992454
  dataset_size: 378343668
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: other
language:
- ko
---

### Development Process

1. question dataset from [kuotient/orca-math-word-problems-193k-korean](https://huggingface.co/datasets/kuotient/orca-math-word-problems-193k-korean)
2. We used [Qwen/Qwen3-14B](https://huggingface.co/Qwen/Qwen3-14B) to evaluate the appropriateness of those candidates.


## License
- Qwen/Qwen3-14B : https://choosealicense.com/licenses/apache-2.0/
- kuotient/orca-math-word-problems-193k-korean : https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/cc-by-sa-4.0.md

## Acknowledgement
This research is supported by **TPU Research Cloud program**