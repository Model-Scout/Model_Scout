---
license: mit
task_categories:
  - text-generation
tags:
  - reinforcement-learning
  - agents
  - llm
  - tool-use
  - reasoning
library_name:
  - datasets
---

# Agentic Reinforced Policy Optimization (ARPO) Dataset

This repository contains the datasets associated with the paper [Agentic Reinforced Policy Optimization (ARPO)](https://huggingface.co/papers/2507.19849).

ARPO proposes a novel agentic Reinforcement Learning algorithm designed for training multi-turn Large Language Model (LLM)-based agents. It addresses the challenge of balancing intrinsic long-horizon reasoning capabilities with proficiency in multi-turn tool interactions, particularly noting the increased uncertainty in LLM behavior following tool use. ARPO incorporates an entropy-based adaptive rollout mechanism and advantage attribution estimation to efficiently align step-level tool-use behaviors. Our experiments across 13 challenging benchmarks in computational reasoning, knowledge reasoning, and deep search domains demonstrate ARPO's superiority over trajectory-level RL algorithms.

**Paper:** [Agentic Reinforced Policy Optimization](https://huggingface.co/papers/2507.19849)
**arXiv:** [2507.19849](https://arxiv.org/abs/2507.19849)
**Code (GitHub):** [https://github.com/dongguanting/ARPO](https://github.com/dongguanting/ARPO)

https://huggingface.co/papers/2510.14545

### Dataset Overview

The ARPO paper introduces two main types of training and validation datasets to demonstrate the effectiveness of the proposed method:

1.  **Reasoning and Knowledge Dataset**: This dataset is used to test benchmarks related to mathematical and knowledge reasoning.
    *   `train_10k.parquet`: Contains 10,000 samples for training.
    *   `test.parquet`: Comprises 300 test samples sourced from 8 distinct datasets, including AIME24, AIME25, MATH500, GSM8k, HotpotQA, 2Wiki, Misque, and Bamboogle.

2.  **Deep Search Dataset**: This dataset is utilized for evaluating performance on deep search benchmarks.
    *   `hard_search.parquet`: Contains 1,000 samples, which include 800 samples from SimpleDeepSearch and 200 samples from WebDancer.
    *   `gaia_test.parquet`/`hle_test.parquet`: Contains test samples specifically from the GAIA and Humanity Last Exam (HLE) benchmarks.

These datasets are integral for training and evaluating LLM agents in computational reasoning, knowledge reasoning, and deep search domains.
Additionally, a Supervised Fine-Tuning (SFT) dataset, `ARPO-SFT-54K`, is also released for cold-start fine-tuning.

### Sample Usage

You can load the datasets directly using the Hugging Face `datasets` library. For example, to load the `ARPO-SFT-54K` dataset:

```python
from datasets import load_dataset

sft_dataset = load_dataset("dongguanting/ARPO-SFT-54K")
print(sft_dataset)
```

Similarly, you can load other ARPO datasets like `dongguanting/ARPO-RL-Reasoning-10K` and `dongguanting/ARPO-RL-DeepSearch-1K` by replacing the dataset name.

Alternatively, you can download the dataset files using `git lfs`:

```bash
git lfs install
git clone https://huggingface.co/datasets/dongguanting/ARPO-SFT-54K
git clone https://huggingface.co/datasets/dongguanting/ARPO-RL-Reasoning-10K
git clone https://huggingface.co/datasets/dongguanting/ARPO-RL-DeepSearch-1K
```

### Citation

If you find this work helpful, please cite our paper:

```bibtex
@misc{dong2025arpo,
      title={Agentic Reinforced Policy Optimization}, 
      author={Guanting Dong and Hangyu Mao and Kai Ma and Licheng Bao and Yifei Chen and Zhongyuan Wang and Zhongxia Chen and Jiazhen Du and Huiyang Wang and Fuzheng Zhang and Guorui Zhou and Yutao Zhu and Ji-Rong Wen and Zhicheng Dou},
      year={2025},
      eprint={2507.19849},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2507.19849}, 
}
```

### License

This project is released under the [MIT License](https://opensource.org/licenses/MIT).

### Contact

For any questions or feedback, please reach out to us at [dongguanting@ruc.edu.cn](dongguanting@ruc.edu.cn).