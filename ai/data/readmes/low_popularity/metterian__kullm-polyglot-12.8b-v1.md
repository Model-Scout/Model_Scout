---
license: mit
language:
- ko
tags:
- kullm-13.b
- polyglot-ko
- gpt-neox
pipeline_tag: text-generation
---



# KULLM-Polyglot-12.8B-v2

This model is a fine-tuned version of [EleutherAI/polyglot-ko-12.8b](https://huggingface.co/EleutherAI/polyglot-ko-12.8b) on a KULLM v2 

Detail Codes are available at [KULLM Github Repository](https://github.com/nlpai-lab/KULLM)


## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:

- learning_rate: 5e-05
- train_batch_size: 64
- seed: 42
- distributed_type: multi-GPU (A100 80G)
- num_devices: 4
- gradient_accumulation_steps: 16
- total_train_batch_size: 256
- total_eval_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- num_epochs: 10.0

### Framework versions

- Transformers 4.28.1
- Pytorch 2.0.0+cu117
- Datasets 2.11.0
- Tokenizers 0.13.3