---
license: apache-2.0
datasets:
- tabtoyou/KoLLaVA-Instruct-150k
- tabtoyou/KoLLaVA-CC3M-Pretrain-595K
language:
- ko
library_name: transformers
tags:
- LLaVA
- KoVicuna
- KoLLaVA
- KoAlpaca
- CLIP
---

# KoLLaVA : Korean Large Language and Vision Assistant (feat. LLaVA)
This model is a large multimodal model (LMM) that combines the LLM([KoVicuna](https://huggingface.co/junelee/ko_vicuna_7b)) with visual encoder of CLIP([ViT-14](https://huggingface.co/openai/clip-vit-large-patch14)), trained on [Korean visual-instruction dataset](https://huggingface.co/datasets/tabtoyou/KoLLaVA-Instruct-150k).

Detail codes are available at [KoLLaVA github repository](https://github.com/tabtoyou/KoLLaVA)

### Training hyperparameters
* learning rate : 2e-5
* train_batch_size: 16
* distributed_type: multi-GPU (A100 80G)
* num_devices: 4
* gradient_accumulation_steps: 1
* total_train_batch_size: 64
* total_eval_batch_size: 16
* lr_scheduler_type: cosine
* num_epochs: 1

Model License: Apache License 2.0