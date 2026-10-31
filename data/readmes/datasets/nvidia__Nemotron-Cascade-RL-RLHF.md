---
license: cc-by-4.0
language:
- en
configs:
- config_name: default
  data_files:
  - split: train
    path: rlhf_train_data.parquet
---

## Dataset Description:
The Nemotron-Cascade-RL-RLHF dataset is designed for Reinforcement Learning from Human Feedback (RLHF) training. It contains prompts and associated metadata to support the development of language model alignment.

This dataset is ready for commercial use.

The dataset contains the following subset:

### RLHF Training Data
This data contains 45,882 samples used for RLHF training. It includes prompts, data sources, and category information. 

This dataset is a curated subset of datasets from:

- [HelpSteer 2 dataset](https://huggingface.co/datasets/nvidia/HelpSteer2)
- [HelpSteer 3 dataset](https://huggingface.co/datasets/nvidia/HelpSteer3)
- [WildGuard](https://huggingface.co/allenai/wildguard)

## Dataset Creation Date:
Created on: Dec 15, 2025

Last Modified on: Dec 15, 2025

## License/Terms of Use: 
The dataset is governed by the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

## Intended Usage:
This dataset is intended to be used by the community to train and evaluate RLHF models. The data may be freely used to train and evaluate.

## Dataset Characterization
**Data Collection Method**  
Hybrid: Human, Synthetic, Automated

**Labeling Method**  
Hybrid: Human, Synthetic, Automated

## Dataset Format
Modality: Text  
Format: Parquet  
Structure: Text + Metadata  

**Columns:**
- `prompt`: The input prompt for the model (Chat format)
- `data_source`: Source of the data
- `index`: Identifier
- `category`: Category of the prompt
- `cat`: Categorical label

## Dataset Quantification

| Subset | Samples |
|--------|---------|
| train  | 45,882  |
| Total  | 45,882  |

Total Disk Size: ~17 MB

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal developer teams to ensure this dataset meets requirements for the relevant industry and use case and addresses unforeseen product misuse.   
Please report quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/)
