---
dataset_info:
  features:
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 39443623
    num_examples: 25000
  download_size: 19348812
  dataset_size: 39443623
---
# 🇻🇳 Vietnamese modified Alpaca Dataset

This dataset is especially designed for Vietnamese based on the idea from [Stanford Alpaca](https://github.com/tatsu-lab/stanford_alpaca), [Self-Instruct paper](https://arxiv.org/abs/2212.10560) and [Chinese LLaMA](https://github.com/ymcui/Chinese-LLaMA-Alpaca). The motivation behind the creation of this dataset stems from the hope to contribute high-quality dataset to Vietnamese commnunity to train language models.

To construct this dataset, we follow a two-step process:

- Step 1: Manually create Vietnamese seed tasks
We employ the methodology outlined in the [Self-Instruct paper](https://arxiv.org/abs/2212.10560) we meticulously curated a diverse set of seed tasks for the Vietnames with GPT-4 and hand-craft as well.

- Step 2: Instruction Generation
Recognizing the challenges associated with generating instructions/inputs/outputs from [Stanford Alpaca](https://github.com/tatsu-lab/stanford_alpaca) and desiring to create a more diverse, longer in length dataset with predefined topics, we adapted prompts and generated data in the form of input/output using GPT-4, GPT-3.5, and GPT-3.5-instruct. Our approach was inspired by the methodology employed in [Chinese LLaMA](https://github.com/ymcui/Chinese-LLaMA-Alpaca).

### Please cite our manuscript if this dataset is used for your work
```
  @article{duc2024towards,
    title={Towards Comprehensive Vietnamese Retrieval-Augmented Generation and Large Language Models},
    author={Nguyen Quang Duc, Le Hai Son, Nguyen Duc Nhan, Nguyen Dich Nhat Minh, Le Thanh Huong, Dinh Viet Sang},
    journal={arXiv preprint arXiv:2403.01616},
    year={2024}
  }
```