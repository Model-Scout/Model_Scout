---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-xls-r-phone-mfa_korean
  results: []
language:
- ko
metrics:
- wer
pipeline_tag: automatic-speech-recognition
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xls-r-300m_phoneme-mfa_korean

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on a phonetically balanced native Korean read-speech corpus.
* Model Management by: [excalibur12](https://huggingface.co/excalibur12)

# Training and Evaluation Data

Training Data
- Data Name: Phonetically Balanced Native Korean Read-speech Corpus
- Num. of Samples: 54,000 (540 speakers)
- Audio Length: 108 Hours

Evaluation Data
- Data Name: Phonetically Balanced Native Korean Read-speech Corpus
- Num. of Samples: 6,000 (60 speakers)
- Audio Length: 12 Hours

# Training Hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.2
- num_epochs: 20 (EarlyStopping: patience: 5 epochs max)
- mixed_precision_training: Native AMP

# Evaluation Results

- <b>Phone Error Rate 3.88%</b>
- Monophthong-wise Error Rates: (To be posted)

# Output Examples
![output_examples](./output_examples.png)

# MFA-IPA Phoneset Tables

## Vowels
![mfa_ipa_chart_vowels](./mfa_ipa_chart_vowels.png)

## Consonants
![mfa_ipa_chart_consonants](./mfa_ipa_chart_consonants.png)

## Experimental Results
Official implementation of the paper ([ICPhS 2023](https://www.icphs2023.org))  
Major error patterns of L2 Korean speech from five different L1s: Chinese (ZH), Vietnamese (VI), Japanese (JP), Thai (TH), English (EN)  
![Experimental Results](./ICPHS2023_table2.png)

# Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1