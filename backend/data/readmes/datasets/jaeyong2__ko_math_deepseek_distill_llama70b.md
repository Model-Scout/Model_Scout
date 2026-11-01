---
dataset_info:
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 278525746
    num_examples: 105000
  download_size: 167872358
  dataset_size: 278525746
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
2. We used [deepseek-ai/DeepSeek-R1-Distill-Llama-70B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-70B)


## License
- deepseek-ai/DeepSeek-R1-Distill-Llama-70B : https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/mit.md
- kuotient/orca-math-word-problems-193k-korean : https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/cc-by-sa-4.0.md

## Acknowledgement
This research is supported by **TPU Research Cloud program**.