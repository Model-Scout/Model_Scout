---
language:
- en
- ko
license: apache-2.0
library_name: transformers
tags:
- translation
- t5
- en-to-ko
datasets:
- aihub-koen-translation-integrated-base-10m
metrics:
- bleu
model-index:
- name: traintogpb-ke-t5-base-aihub-koen-translation-integrated-10m-en-to-ko
  results:
  - task:
      name: Translation
      type: translation
    dataset:
      name: AIHub KO-EN Translation Integrated Base (10M)
      type: aihub-koen-translation-integrated-base-10m
    metrics:
    - name: BLEU
      type: bleu
      value: 18.838066
      epoch: 2
    - name: BLEU
      type: bleu
      value: 18.006119
      epoch: 1
---



# Model Description

This model, named **traintogpb-ke-t5-base-aihub-koen-translation-integrated-10m-en-to-ko**, is a machine translation model that translates English to Korean. It is fine-tuned from the [KETI-AIR/ke-t5-base](https://huggingface.co/KETI-AIR/ke-t5-base) model using the [aihub-koen-translation-integrated-base-10m](https://huggingface.co/datasets/traintogpb/aihub-koen-translation-integrated-base-10m) dataset.


## Model Architecture

The model uses the ke-t5-base architecture, which is based on the T5 (Text-to-Text Transfer Transformer) model.

## Training Data

The model was trained on the aihub-koen-translation-integrated-base-10m dataset, which is designed for English-to-Korean translation tasks.

## Training Procedure

### Training Parameters

The model was trained with the following parameters:
- Learning Rate: 0.0005
- Weight Decay: 0.01
- Batch Size: 64 (training), 128 (evaluation)
- Number of Epochs: 2
- Save Steps: 500
- Max Save Checkpoints: 2
- Evaluation Strategy: At the end of each epoch
- Logging Strategy: No logging
- Use of FP16: No
- Gradient Accumulation Steps: 2
- Reporting: None

### Hardware

The training was performed on a single GPU system with an NVIDIA A100 (40GB).


## Performance

The model achieved the following BLEU scores during training:
- Epoch 1: 18.006119
- Epoch 2: 18.838066

## Usage

This model is suitable for applications involving translation from English to Korean. Here is an example on how to use this model in Hugging Face's Transformers:

```python
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model = AutoModelForSeq2SeqLM.from_pretrained("traintogpb-ke-t5-base-aihub-koen-translation-integrated-10m-en-to-ko")
tokenizer = AutoTokenizer.from_pretrained("traintogpb-ke-t5-base-aihub-koen-translation-integrated-10m-en-to-ko")

inputs = tokenizer.encode("This is a sample text.", return_tensors="pt")
outputs = model.generate(inputs)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
