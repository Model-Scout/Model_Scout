---
dataset_info:
  features:
  - name: question
    dtype: string
  - name: context
    dtype: string
  splits:
  - name: train
    num_bytes: 2211041
    num_examples: 7000
  download_size: 1085849
  dataset_size: 2211041
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# philschmid/finanical-rag-embedding-dataset 

[philschmid/finanical-rag-embedding-dataset](https://huggingface.co/datasets/philschmid/finanical-rag-embedding-dataset) is a modified fork of [virattt/llama-3-8b-financialQA](https://huggingface.co/datasets/virattt/llama-3-8b-financialQA?row=0) for fine-tuning embedding models using positive text pairs (question, context). 
The dataset include `7,000` question, context pairs from [NVIDIAs 2023 SEC Filling Report](https://stocklight.com/stocks/us/nasdaq-nvda/nvidia/annual-reports/nasdaq-nvda-2023-10K-23668751.pdf)
