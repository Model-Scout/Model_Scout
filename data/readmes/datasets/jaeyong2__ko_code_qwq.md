---
dataset_info:
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 988628939
    num_examples: 50000
  download_size: 474502559
  dataset_size: 988628939
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
license: apache-2.0
---
  
### Development Process

1. question dataset from [nayohan/CodeFeedback-Filtered-Instruction-ko](https://huggingface.co/datasets/nayohan/CodeFeedback-Filtered-Instruction-ko)
2. We used [Qwen/QwQ-32B](https://huggingface.co/Qwen/QwQ-32B)


## License
- Qwen/QwQ-32B : https://huggingface.co/Qwen/QwQ-32B/blob/main/LICENSE

## Acknowledgement
This research is supported by **TPU Research Cloud program**.