
---
library_name: transformers
metrics:
- wer
- cer
model-index:
- name: Fine-Tuned-Whisper-Large-v3-Turbo-STT-Zeroth-KO-v2
  results: []
datasets:
- o0dimplz0o/Zeroth-STT-Korean
language:
- ko
base_model:
- openai/whisper-large-v3-turbo
pipeline_tag: automatic-speech-recognition
---

## Whisper Large v2 Fine-Tuned for Korean ASR

This model is being fine-tuned from openai/whisper-large-v3-turbo on a custom dataset.
It currently achieves the following results on the evaluation set (still fine-tuning):
- Loss: 0.0164
- Wer: 19.9134
- Cer: 0.0660

## Model Description
This model is a version of `openai/whisper-large-v3-turbo`, currently still being incrementally fine-tune in stages, specifically optimized for Korean automatic speech recognition (ASR) tasks. The fine-tuning process aims to deliver high accuracy and timestamped transcriptions for Korean speech.

## Dataset Details
- **Dataset Source**: Custom dataset (https://huggingface.co/datasets/o0dimplz0o/Zeroth-STT-Korean)
- **Number of Samples**: 102,263
- **Split**: 93% train, 7% test
- **Data Augmentation**: 20% random, applied only to the training set

## Training Details
- **Hardware**: L40S GPU
- **Learning Rate Scheduler**: Cosine
- **Epochs**: [pending completion]
- **Optimizer**: AdamW Torch Fused
