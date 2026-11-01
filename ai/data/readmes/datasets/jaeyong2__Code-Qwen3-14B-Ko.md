---
dataset_info:
  features:
  - name: content
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 416939609
    num_examples: 25000
  download_size: 166633989
  dataset_size: 416939609
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

1. question dataset from [nayohan/CodeFeedback-Filtered-Instruction-ko](https://huggingface.co/datasets/nayohan/CodeFeedback-Filtered-Instruction-ko)
2. We used [Qwen/Qwen3-14B](https://huggingface.co/Qwen/Qwen3-14B) to evaluate the appropriateness of those candidates.


## License
- Qwen/Qwen3-14B : https://choosealicense.com/licenses/apache-2.0/
- nayohan/CodeFeedback-Filtered-Instruction-ko : https://huggingface.co/datasets/nayohan/CodeFeedback-Filtered-Instruction-ko
 
## Acknowledgement
This research is supported by **TPU Research Cloud program**.