---
license: apache-2.0
language:
- en
- zh
- es
- ar
- vi
- ja
- ko
- fr
- pt
- th
tags:
- O1-like model
- Math
pipeline_tag: text-generation
---

This repository contains the resources for our **paper** [Think Natively: Unlocking Multilingual Reasoning with Consistency-Enhanced Reinforcement Learning](https://arxiv.org/pdf/2510.07300)

Large Reasoning Models (LRMs) have achieved remarkable performance on complex reasoning tasks by adopting the "think-then-answer" paradigm, which enhances both accuracy and interpretability. However, current LRMs exhibit two critical limitations when processing non-English languages: (1) They often struggle to maintain input-output language consistency; (2) They generally perform poorly with wrong reasoning paths and lower answer accuracy compared to English. These limitations significantly degrade the user experience for non-English speakers and hinder the global deployment of LRMs. To address these limitations, we propose M-Thinker, which is trained by the GRPO algorithm that involves a **Language Consistency (LC) reward** and a novel **Cross-lingual Thinking Alignment (CTA) reward**. Specifically, the LC reward defines a strict constraint on the language consistency between the input, thought, and answer. Besides, the CTA reward compares the model's non-English reasoning paths with its English reasoning path to transfer its own reasoning capability from English to non-English languages. Through an iterative RL procedure, our M-Thinker-1.5B/7B models not only achieve nearly 100% language consistency and superior performance on two multilingual benchmarks (MMATH and PolyMath), but also exhibit excellent generalization on out-of-domain languages.




| Model Access | Backbone | Training data Access | 
| :-- | :-- | :-- |
 <a href="https://huggingface.co/XueZhang-bjtu/M-Thinker-7B-Iter2">M-Thinker-7B-Iter2</a> (👍👍) &emsp;  |   <a href="https://huggingface.co/XueZhang-bjtu/M-Thinker-7B-Iter1">M-Thinker-7B-Iter1</a> |    [M-Thinker-7B-RL-Iter2-data](https://huggingface.co/datasets/XueZhang-bjtu/M-Thinker-7B-RL-Iter2-data) 
 <a href="https://huggingface.co/XueZhang-bjtu/M-Thinker-7B-Iter1">M-Thinker-7B-Iter1</a> (👍) |    [7B-cold-start-SFT](https://huggingface.co/XueZhang-bjtu/7B-cold-start-SFT) |    [M-Thinker-7B-RL-Iter1-data](https://huggingface.co/datasets/XueZhang-bjtu/M-Thinker-7B-RL-Iter1-data) 
  [7B-cold-start-SFT](https://huggingface.co/XueZhang-bjtu/7B-cold-start-SFT) |  [DeepSeek-R1-Distill-Qwen-7B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B) &emsp; |  [M-Thinker-SFT-data](https://huggingface.co/datasets/XueZhang-bjtu/M-Thinker-SFT-data)
 <a href="https://huggingface.co/XueZhang-bjtu/M-Thinker-1.5B-Iter2">M-Thinker-1.5B-Iter2</a> (👍👍) |   <a href="https://huggingface.co/XueZhang-bjtu/M-Thinker-1.5B-Iter1">M-Thinker-1.5B-Iter1</a> |    [M-Thinker-1.5B-RL-Iter2-data](https://huggingface.co/datasets/XueZhang-bjtu/M-Thinker-1.5B-RL-Iter2-data) 
 <a href="https://huggingface.co/XueZhang-bjtu/M-Thinker-1.5B-Iter1">M-Thinker-1.5B-Iter1</a> (👍) |    [1.5B-cold-start-SFT](https://huggingface.co/XueZhang-bjtu/1.5B-cold-start-SFT) |    [M-Thinker-1.5B-RL-Iter1-data](https://huggingface.co/datasets/XueZhang-bjtu/M-Thinker-1.5B-RL-Iter1-data) 
  [1.5B-cold-start-SFT](https://huggingface.co/XueZhang-bjtu/1.5B-cold-start-SFT) |  [DeepSeek-R1-Distill-Qwen-1.5B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B) |  [M-Thinker-SFT-data](https://huggingface.co/datasets/XueZhang-bjtu/M-Thinker-SFT-data)



If you find this work useful, please consider citing our paper:
```
@misc{zhang2025thinknativelyunlockingmultilingual,
      title={Think Natively: Unlocking Multilingual Reasoning with Consistency-Enhanced Reinforcement Learning}, 
      author={Xue Zhang and Yunlong Liang and Fandong Meng and Songming Zhang and Kaiyu Huang and Yufeng Chen and Jinan Xu and Jie Zhou},
      year={2025},
      eprint={2510.07300},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2510.07300}, 
}
```



### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-06
- train_batch_size: 1
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- gradient_accumulation_steps: 32
- total_train_batch_size: 256
- total_eval_batch_size: 64
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- num_epochs: 1.0


### Framework versions

- Transformers 4.46.3
- Pytorch 2.5.1+cu124
- Datasets 3.1.0
- Tokenizers 0.20.3
