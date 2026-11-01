---
license: mit
language:
- hi
- ta
- mr
- te
- bn
- ar
- es
- fr
- de
- pt
- ja
- ko
- ru
- it
- vi
pretty_name: Sovereign-FinComply-Eval
task_categories:
- translation
- text-generation
tags:
- compliance
- finance
- healthcare
- red-teaming
- rlhf
---

# 🧠 Sovereign-FinComply-Eval Dataset

A high-fidelity multilingual evaluation and alignment dataset engineered to red-team LLM compliance translations across **15 low-resource and global languages** (including Hindi, Tamil, Marathi, Telugu, Bengali, Arabic, and more).

## 💡 How Adaption was used to build this dataset:
1. **Fidelity Profiling**: Legal and financial rules (RBI compounding laws, HIPAA standards) were translated by baseline models.
2. **Drift Benchmarking**: We used the **Adaption Evaluation Suite** to score each translation's legal fidelity and semantic drift.
3. **Drift Filtering**: Rules scoring `< 90%` fidelity (hallucinations) were flagged and filtered (e.g., misinterpreting "liquidate assets" as "burn down the bank").
4. **Bilingual Crowdsourcing**: The failed translations were corrected by staked human auditors on the Sharp network, expanding the dataset with verified ground-truth translations.

## 📊 Dataset Structure
The uploaded CSV contains:
*   `english`: The original regulatory compliance guideline.
*   `language`: The target low-resource translation script.
*   `translation`: The evaluated translation candidate.
*   `score`: The Adaption fidelity score.
*   `hallucination`: The identified factual drift details.