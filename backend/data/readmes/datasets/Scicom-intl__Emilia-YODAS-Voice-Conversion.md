---
language:
- de
- en
- fr
- ja
- ko
- zh
- ms
configs:
- config_name: audio_length_ratio_text
  data_files:
  - split: train
    path: audio_length_ratio_text/train-*
- config_name: audio_text
  data_files:
  - split: train
    path: audio_text/train-*
- config_name: default
  data_files:
  - split: train
    path: data/train-*
- config_name: original
  data_files:
  - split: train
    path: original/train-*
dataset_info:
- config_name: audio_length_ratio_text
  features:
  - name: audio_filename
    dtype: string
  - name: audio_filename_trim
    dtype: string
  - name: audio_length
    dtype: float64
  - name: text
    dtype: string
  - name: audio_length_ratio_text
    dtype: float64
  - name: audio_length_ratio_text_accept
    dtype: bool
  splits:
  - name: train
    num_bytes: 3249280650
    num_examples: 11365350
  download_size: 1360996742
  dataset_size: 3249280650
- config_name: audio_text
  features:
  - name: audio_filename
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 2486382629
    num_examples: 11365354
  download_size: 1192189223
  dataset_size: 2486382629
- config_name: default
  features:
  - name: reference_audio
    dtype: string
  - name: reference_text
    dtype: string
  - name: target_audio
    dtype: string
  - name: target_text
    dtype: string
  splits:
  - name: train
    num_bytes: 15168651049
    num_examples: 32845483
  download_size: 3454397610
  dataset_size: 15168651049
- config_name: original
  features:
  - name: text
    dtype: string
  - name: duration
    dtype: float64
  - name: speaker
    dtype: string
  - name: language
    dtype: string
  - name: dnsmos
    dtype: float64
  - name: phone_count
    dtype: int64
  - name: _id
    dtype: string
  splits:
  - name: train
    num_bytes: 2940653776
    num_examples: 11365354
  download_size: 1629097675
  dataset_size: 2940653776
---
# Emilia-YODAS-Voice-Conversion

We sample https://huggingface.co/datasets/amphion/Emilia-Dataset YODAS set for voice conversion.

1. Filter transcriptions based on character repetitiveness and word ngrams.
2. Filter speaker similarity using https://huggingface.co/nvidia/speakerverification_en_titanet_large during speaker permutation.
3. Convert audio to speech tokens using https://huggingface.co/neuphonic/neucodec

We also upload the full permutation as zip files.

## Speech Tokenizer

Convert audio to speech tokens using https://huggingface.co/neuphonic/neucodec 50Hz, **with total 5.7B speech tokens**.

## Statistics

1. DE, 5558.53 hours.
2. EN, 13493.57 hours.
3. FR, 6954.43 hours.
4. JA, 1120.36 hours.
5. KO, 6991.33 hours.
6. ZH, 326.01 hours.