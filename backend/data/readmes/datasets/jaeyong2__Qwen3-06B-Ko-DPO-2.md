---
dataset_info:
  features:
  - name: prompt
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: chosen
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: rejected
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 269677305
    num_examples: 26112
  download_size: 100411525
  dataset_size: 269677305
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
2. We used [Qwen/Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) to generate the answer candidates (n=32).
3. We used [Qwen/Qwen3-14B](https://huggingface.co/Qwen/Qwen3-14B) to evaluate the appropriateness of those candidates.


## License
- Qwen/Qwen3-0.6B : https://choosealicense.com/licenses/apache-2.0/
- Qwen/Qwen3-14B : https://choosealicense.com/licenses/apache-2.0/
- kuotient/orca-math-word-problems-193k-korean : https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/cc-by-sa-4.0.md

## Acknowledgement
This research is supported by **TPU Research Cloud program**.