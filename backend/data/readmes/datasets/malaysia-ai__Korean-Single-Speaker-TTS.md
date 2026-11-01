---
language:
- ko
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: audio_filename
    dtype: string
  - name: text
    dtype: string
  - name: speaker
    dtype: string
  splits:
  - name: train
    num_bytes: 1153773
    num_examples: 12852
  download_size: 494842
  dataset_size: 1153773
---
# Korean-Single-Speaker-TTS

Originally from https://www.kaggle.com/datasets/bryanpark/korean-single-speaker-speech-dataset, we mirror it to HuggingFace.

## how to prepare the dataset

```bash
hf download malaysia-ai/Korean-Single-Speaker-TTS kss_audio.zip --local-dir=./ --repo-type=dataset
unzip kss_audio.zip
```