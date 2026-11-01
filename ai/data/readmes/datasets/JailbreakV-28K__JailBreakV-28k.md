---
license: mit
task_categories:
- text-generation
- question-answering
pretty_name: JailBreakV_28K
size_categories:
- 10K<n<100K
configs:
- config_name: JailBreakV_28K
  data_files:
  - split: mini_JailBreakV_28K
    path: JailBreakV_28K/mini_JailBreakV_28K.csv
  - split: JailBreakV_28K
    path: JailBreakV_28K/JailBreakV_28K.csv
- config_name: RedTeam_2K
  data_files:
  - split: RedTeam_2K
    path: JailBreakV_28K/RedTeam_2K.csv
---
# ⛓‍💥 JailBreakV-28K: A Benchmark for Assessing the Robustness of MultiModal Large Language Models against Jailbreak Attacks
[**🌐 GitHub**](https://github.com/EddyLuo1232/JailBreakV_28K) | [**🛎 Project Page**](https://eddyluo1232.github.io/JailBreakV28K/) ｜ [**👉 Download full datasets**](https://forms.gle/e6boFoM9mNfPHb9H9)

## If you like our project, please give us a star ⭐ on Hugging Face for the latest update.

## 📰 News
| Date       | Event    |
|------------|----------|
| **2024/07/09** | 🎉 Our paper is accepted by COLM 2024.|
| **2024/06/22** | 🛠️ We have updated our version to V0.2, which supports users to customize their attack models and evaluate models.|
| **2024/04/04** | 🎁 We have posted our paper on Arxiv.|
| **2024/04/03** | 🎉 We have released our evaluation and inference samples.|
| **2024/03/30** | 🔥 We have released our dataset.|

## 📥 Using our dataset via huggingface Dataset
```python
from datasets import load_dataset


mini_JailBreakV_28K = load_dataset("JailbreakV-28K/JailBreakV-28k", 'JailBreakV_28K')["mini_JailBreakV_28K"]
JailBreakV_28K = load_dataset("JailbreakV-28K/JailBreakV-28k", 'JailBreakV_28K')["JailBreakV_28K"]
RedTeam_2K = load_dataset("JailbreakV-28K/JailBreakV-28k", 'RedTeam_2K')["RedTeam_2K"]
```
## 👻 Inference and Evaluation 

### Create environment
```python
conda create -n jbv python=3.9
conda activate jbv
pip install -r requirements.txt
```

### Conduct jailbreak attack on MLLMs
```python
# we default use Bunny-v1_0, you can change the default attack model to your customized attack models by editing the annotated codes.
# You can follow the Bunny script in <attack_models> to add other attack models.
python attack.py --root JailBreakV_28K 
```

### Conduct evaluation
```python
# we default use LlamaGuard, you can change the default evaluate model to your customized evaluate models by editing the annotated codes.
# You can follow the LlamaGuard script in <evaluate_models> to add other evaluate models.
python eval.py --data_path ./results/JailBreakV_28k/<your customized attack model>/JailBreakV_28K.csv
```

## 😃 Dataset Details

JailBreakV_28K and mini_JailBreakV_28K datasets will comprise the following columns:

- **id**: Unique identifier for all samples.
- **jailbreak_query**: Jailbreak_query obtained by different jailbreak attacks.
- **redteam_query**: Harmful query from RedTeam_2K.
- **format**: Jailbreak attack method including template, persuade, logic, figstep, query-relevant.
- **policy**: The safety policy that redteam_query against.
- **image_path**: The file path of the image.
- **from**: The source of data.
- **selected_mini**: "True" if the data in mini_JailBreakV_28K dataset, otherwise "False".
- **transfer_from_llm**: "True" if the jailbreak_query is transferred from LLM jailbreak attacks, otherwise "False".

RedTeam_2K will comprise the following columns:

- **id**: Unique identifier for all samples.
- **question**: Harmful query.
- **policy**: the safety policy that redteam_query against.
- **from**: The source of data.

## 🚀 Data Composition

<!-- Provide a quick summary of the dataset. -->
**RedTeam-2K**: RedTeam-2K dataset, a meticulously curated collection of 2, 000 harmful queries aimed at identifying alignment vulnerabilities within LLMs and MLLMs. This dataset spans across 16 safety policies and incorporates queries from 8 distinct sources.
<img src="distribution_used.png" width="800"/>
**JailBreakV-28K**: JailBreakV-28K contains 28, 000 jailbreak text-image pairs, which include 20, 000 text-based LLM transfer jailbreak attacks and 8, 000 image-based MLLM jailbreak attacks. This dataset covers 16 safety policies and 5 diverse jailbreak methods.

## 🛠️ Dataset Overview
The RedTeam-2K dataset, is a meticulously curated collection of 2, 000 harmful queries aimed at identifying alignment vulnerabilities within LLMs and MLLMs. This dataset spans 16 safety policies and incorporates queries from 8 distinct sources, including GPT Rewrite, Handcraft, GPT Generate, LLM Jailbreak Study, AdvBench, BeaverTails, Question Set, and hh-rlhf of Anthropic.
Building upon the harmful query dataset provided by RedTeam-2K, JailBreakV-28K is designed as a comprehensive and diversified benchmark for evaluating the transferability of jailbreak attacks from LLMs to MLLMs, as well as assessing the alignment robustness of MLLMs against such attacks. Specifically, JailBreakV-28K contains 28, 000 jailbreak text-image pairs, which include 20, 000 text-based LLM transfer jailbreak attacks and 8, 000 image-based MLLM jailbreak attacks. This dataset covers 16 safety policies and 5 diverse jailbreak methods. The jailbreak methods are formed by 3 types of LLM transfer attacks that include Logic (Cognitive Overload), Persuade (Persuasive Adversarial Prompts), and Template (including both of Greedy Coordinate Gradient and handcrafted strategies), and 2 types of MLLM attacks including FigStep and Query-relevant attack. The JailBreakV-28K offers a broad spectrum of attack methodologies and integrates various image types like Nature, Random Noise, Typography, Stable Diffusion (SD), Blank, and SD+Typography Images. We believe JailBreakV-28K can serve as a comprehensive jailbreak benchmark for MLLMs. 
<img src="dataset.png" width="800"/>

## 🏆 Mini-Leaderboard
| Model                      |  Total ASR| Transfer Attack ASR|
|----------------------------|:---------:|:------------------:|
| OmniLMM-12B                |   58.1    |        70.2        |
| InfiMM-Zephyr-7B           |   52.9    |        73.0        |
| LLaMA-Adapter-v2           |   51.2    |        68.1        |
| LLaVA-1.5-13B              |   51.0    |        65.5        |    
| LLaVA-1.5-7B               |   46.8    |        61.4        |
| InstructBLIP-13B           |   45.2    |        55.5        |
| InternLM-XComposer2-VL-7B  |   39.1    |        29.3        |
| Bunny-v1                   |   38.0    |        49.5        |
| Qwen-VL-Chat               |   33.7    |        41.2        |
| InstructBLIP-7B            |   26.0    |        46.8        |
## ❌ Disclaimers
This dataset contains offensive content that may be disturbing, This benchmark is provided for educational and research purposes only.
## 📲 Contact
- Weidi Luo: luo.1455@osu.edu
- Siyuan Ma: siyuan.ma.pku@gmail.com
- Xiaogeng Liu: xiaogeng.liu@wisc.edu
- Chaowei Xiao: cxiao34@wisc.edu
## 📖 BibTeX:
```python
@misc{luo2024jailbreakv28k,
      title={JailBreakV-28K: A Benchmark for Assessing the Robustness of MultiModal Large Language Models against Jailbreak Attacks}, 
      author={Weidi Luo and Siyuan Ma and Xiaogeng Liu and Xiaoyu Guo and Chaowei Xiao},
      year={2024},
      eprint={2404.03027},
      archivePrefix={arXiv},
      primaryClass={cs.CR}
}
```

[More Information Needed]