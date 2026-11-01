---
dataset_info:
  features:
  - name: data_source
    dtype: string
  - name: prompt
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: ability
    dtype: string
  - name: reward_model
    struct:
    - name: ground_truth
      dtype: string
    - name: style
      dtype: string
  - name: extra_info
    struct:
    - name: index
      dtype: int64
    - name: model_difficulty
      struct:
      - name: DeepSeek-R1-Distill-Qwen-1.5B
        dtype: int64
      - name: DeepSeek-R1-Distill-Qwen-32B
        dtype: int64
      - name: DeepSeek-R1-Distill-Qwen-7B
        dtype: int64
  splits:
  - name: math
    num_bytes: 40461845
    num_examples: 105055
  - name: code
    num_bytes: 1474827100
    num_examples: 14057
  download_size: 823104116
  dataset_size: 1515288945
configs:
- config_name: default
  data_files:
  - split: math
    path: data/math-*
  - split: code
    path: data/code-*
---

<div align="center">

# 🤔 Skywork-OR1-RL-Data

</div>

<div align="center">

[![Models](https://img.shields.io/badge/Models-4d5eff?style=for-the-badge&logo=huggingface&logoColor=ffffff&labelColor)](https://huggingface.co/collections/Skywork/skywork-or1-67fa1bcb41b436ef2def76b9)
[![Data](https://img.shields.io/badge/Data-4d5eff?style=for-the-badge&logo=huggingface&logoColor=ffffff&labelColor)](https://huggingface.co/datasets/Skywork/Skywork-OR1-RL-Data)
[![Github](https://img.shields.io/badge/Code-000000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/SkyworkAI/Skywork-OR1)
[![Notion](https://img.shields.io/badge/Notion_Blog-000000?style=for-the-badge&logo=notion&logoColor=white)](https://capricious-hydrogen-41c.notion.site/Skywork-Open-Reaonser-Series-1d0bc9ae823a80459b46c149e4f51680)

[![GitHub Stars](https://img.shields.io/github/stars/SkyworkAI/Skywork-OR1?style=for-the-badge&logo=github&logoColor=white&label=Stars&color=000000)](https://github.com/SkyworkAI/Skywork-OR1/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/SkyworkAI/Skywork-OR1?style=for-the-badge&logo=github&logoColor=white&label=Forks&color=000000)](https://github.com/SkyworkAI/Skywork-OR1/fork)

</div>


## 🔥 News

- **April 15, 2025**: We are excited to release our RL training dataset [`Skywork-OR1-RL-Data`](https://huggingface.co/datasets/Skywork/Skywork-OR1-RL-Data)
  - For our final training phase, we filtered problems based on their difficulty levels (0-16, higher values indicate harder problems) relative to specific model variants (DeepSeek-R1-Distill-Qwen-{1.5,7,32}B. For each model variant, we excluded problems with difficulty values of 0 and 16 specific to that model from its training data.
  - You can check our [Skywork-OR1](https://github.com/SkyworkAI/Skywork-OR1?tab=readme-ov-file#training-data-preparation) repository for training data preparation steps.
  - **Note**: Due to an accidental early release, a version with incorrect difficulty fields was briefly public. Please make sure to use either the newest version (recommended) or any version at this [commit](https://huggingface.co/datasets/Skywork/Skywork-OR1-RL-Data/commit/b48ac2ee70ae3dc5d6db769f232e8a966cb89240) and after.

## 📖 Overview

[`Skywork-OR1-RL-Data`](https://huggingface.co/datasets/Skywork/Skywork-OR1-RL-Data) is **a dataset of verifiable, challenging, and diverse math problems (105K) and coding questions (14K)**. This dataset is used to train the **`Skywork-OR1`** (Open Reasoner 1) model series, which consists of powerful math and code reasoning models trained using large-scale rule-based reinforcement learning with carefully designed datasets and training recipes. This series includes two general-purpose reasoning modelsl, **`Skywork-OR1-7B-Preview`** and **`Skywork-OR1-32B-Preview`**, along with a math-specialized model, **`Skywork-OR1-Math-7B`**.

- **[`Skywork-OR1-Math-7B`](https://huggingface.co/Skywork/Skywork-OR1-Math-7B)** is specifically optimized for mathematical reasoning, scoring **69.8** on AIME24 and **52.3** on AIME25 — well ahead of all models of similar size.
- **[`Skywork-OR1-32B-Preview`](https://huggingface.co/Skywork/Skywork-OR1-32B-Preview)** delivers the 671B-parameter Deepseek-R1 performance on math tasks (AIME24 and AIME25) and coding tasks (LiveCodeBench).
- **[`Skywork-OR1-7B-Preview`](https://huggingface.co/Skywork/Skywork-OR1-7B-Preview)** outperforms all similarly sized models in both math and coding scenarios.

We select, clean, and curate math and coding problems from open-source datasets, including

- [NuminaMath-1.5](https://huggingface.co/datasets/AI-MO/NuminaMath-1.5)
- [DeepScaleR-Preview-Dataset](https://huggingface.co/datasets/agentica-org/DeepScaleR-Preview-Dataset)
- [STILL-3-Preview-RL-Data](https://huggingface.co/datasets/RUC-AIBOX/STILL-3-Preview-RL-Data)
- [Omni-Math](https://huggingface.co/datasets/KbsdJames/Omni-MATH)
- [AIME problems prior to 2024](https://huggingface.co/datasets/gneubig/aime-1983-2024)
- [LeetCodeDataset](https://huggingface.co/datasets/newfacade/LeetCodeDataset)
- [TACO](https://huggingface.co/datasets/BAAI/TACO)

We conduct **model-aware difficulty estimation** for each problem and model and conduct **rigorous quality assessment prior to training** via both human and LLM-as-a-Judge to ensure training efficiency and effectiveness. We also perform deduplication within the dataset and remove similar problems from AIME 24, AIME 25, and LiveCodeBench to prevent data contamination.

## 📄 Technical Report

Our technical report will be released soon. Stay tuned!

## 📚 Citation

Please cite the following:

```bibtex
@article{he2025skywork,
  title={Skywork Open Reasoner 1 Technical Report},
  author={He, Jujie and Liu, Jiacai and Liu, Chris Yuhao and Yan, Rui and Wang, Chaojie and Cheng, Peng and Zhang, Xiaoyu and Zhang, Fuxiang and Xu, Jiacheng and Shen, Wei and Li, Siyuan and Zeng, Liang and Wei, Tianwen and Cheng, Cheng and An, Bo and Liu, Yang and Zhou, Yahui},
  journal={arXiv preprint arXiv:2505.22312},
  year={2025}
}

@misc{skywork-or1-2025,
  title={Skywork Open Reasoner Series},
  author = {He, Jujie and Liu, Jiacai and Liu, Chris Yuhao and Yan, Rui and Wang, Chaojie and Cheng, Peng and Zhang, Xiaoyu and Zhang, Fuxiang and Xu, Jiacheng and Shen, Wei and Li, Siyuan and Zeng, Liang and Wei, Tianwen and Cheng, Cheng and Liu, Yang and Zhou, Yahui},
  howpublished={\url{https://capricious-hydrogen-41c.notion.site/Skywork-Open-Reaonser-Series-1d0bc9ae823a80459b46c149e4f51680}},
  note={Notion Blog},
  year={2025}
}
```
