---
dataset_info:
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 122256055
    num_examples: 5000
  download_size: 49630336
  dataset_size: 122256055
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

1. question dataset from [nayohan/CodeFeedback-Filtered-Instruction-ko](https://huggingface.co/datasets/nayohan/CodeFeedback-Filtered-Instruction-ko)
2. We used [LGAI-EXAONE/EXAONE-Deep-32B](https://huggingface.co/LGAI-EXAONE/EXAONE-Deep-32B)


## License
- LGAI-EXAONE/EXAONE-Deep-32BB : https://huggingface.co/LGAI-EXAONE/EXAONE-Deep-32B/blob/main/LICENSE

## Acknowledgement
This research is supported by **TPU Research Cloud program**.