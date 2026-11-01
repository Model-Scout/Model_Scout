---
license: other
task_categories:
- text-classification
task_ids:
- topic-classification
- intent-classification
- multi-class-classification
- multi-label-classification
dataset_type: text
language:
- en
- zh
- ru
- es
- fr
- de
- ar
- hi
- pt
- ja
- ko
- it
- nl
- tr
multilinguality: multilingual
tags:
- climate
- finance
- health
- education
- math
- code
size_categories:
- 10K<n<100K
configs:
- config_name: default
  data_files:
  - split: train
    path: All_Data_with_Reassigned_Topic_with_QuestionType.jsonl
---

This dataset accompanies the paper:

**LLM Benchmark-User Need Misalignment for Climate Change**

📄 Paper link: https://arxiv.org/abs/2603.26106; 

🛠️ Github link: https://github.com/OuchengLiu/LLM-Misalign-Climate-Change

---

## 📌 Dataset Summary

This dataset provides a unified collection of climate change–related knowledge interactions for conducting the analyses presented in the paper. It integrates data from multiple sources, covering both human–AI and human–human interactions, and captures how climate-related knowledge is sought and provided in real-world settings.

The dataset is organized into four types of interactions:

* **Human-to-AI Queries**: real user questions extracted from LLM conversation logs (WildChat, LMSYS-Chat-1M, ClimateQ&A)
* **Human-to-Human Questions**: question-style posts from climate-related Reddit communities
* **Human-to-AI Guidance Knowledge**: benchmark questions from ClimaQA Gold & Silver
* **Human-to-Human Knowledge Provision**: informational and authoritative content from IPCC AR6 reports and climate news (SciDCC)

All instances are annotated using a unified fine-grained taxonomy, including **topics, user intents, and answer forms** (the full annotated dataset can be found in `All_Data_with_Reassigned_Topic_with_QuestionType.jsonl`), enabling systematic analysis of knowledge needs and comparison across data sources.

\* We also provide, under the directories `Data/WildChat_Extracted_Data` and `Data/LMSYSChat_Extracted_Data`, datasets extracted using Qwen-3 30B from real user–LLM conversations in WildChat and LMSYS-Chat-1M, covering topics related to **Education, Finance, Health, Math, and Programming**.

---

## 📂 Data Sources

The unified dataset integrates climate-related data from:

* WildChat: `Data/WildChat_Extracted_Data/Climate_Change`
* LMSYS-Chat-1M: `Data/LMSYSChat_Extracted_Data/Climate_Change` (Due to the dataset license, we cannot redistribute the raw data. Therefore, the corresponding data in `All_Data_with_Reassigned_Topic_with_QuestionType.jsonl` and `All_Data.jsonl` has also been removed. You will need to obtain permission from [LMSYS](https://huggingface.co/datasets/lmsys/lmsys-chat-1m) and then follow the process outlined in our GitHub repository to restore this portion of the data as much as possible.)
* ClimateQ&A: `Data/Climate_Change/ClimateQ&A`
* ClimaQA (Gold): `Data/Climate_Change/ClimaQA_Gold`
* ClimaQA (Silver): `Data/Climate_Change/ClimaQA_Silver`
* Reddit (question-style posts): `Data/Climate_Change/Reddit`
* IPCC_AR6: `Data/Climate_Change/IPCC_AR6`
* SciDCC: `Data/Climate_Change/SciDCC`
* Climate_FEVER: `Data/Climate_Change/Climate_FEVER`
* Environmental_Claims: `Data/Climate_Change/Environmental_Claims`
* ClimSight: `Data/Climate_Change/ClimSight`

All datasets are converted into a unified format (the initially unified and formatted dataset can be found in `All_Data.jsonl`).

---

## 🌍 Languages

The dataset contains multilingual data (14 languages), including:

English, Chinese, Russian, Spanish, French, German, Arabic, Hindi, Portuguese, Japanese, Korean, Italian, Dutch, and Turkish.

---

## ⚖️ Licensing Information

This dataset is an aggregation of multiple upstream corpora and newly added annotations.

- Upstream corpora remain under their respective original licenses, including OpenRAIL, Apache-2.0, BSD-3-Clause, and CC BY-NC 4.0...
- Our newly added annotation layer (Topics, Intents and Forms) is released under CC BY 4.0.
- Users must comply with the original license terms of each source corpus when using the corresponding data.
- Because the dataset contains materials under different upstream licenses, including non-commercial restrictions, the dataset as a whole is not released under a single permissive license.
---

## 📊 Additional Resources

* Visualization tools (Streamlit-based / html-based): Included in code repository

---

## 📄 Citation

If you use this dataset, please cite:

```bibtex
@misc{liu2026llmbenchmarkuserneedmisalignment,
      title={LLM Benchmark-User Need Misalignment for Climate Change}, 
      author={Oucheng Liu and Lexing Xie and Jing Jiang},
      year={2026},
      eprint={2603.26106},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2603.26106}, 
}
```