---
license: cc-by-nc-4.0
language:
  - ko
task_categories:
  - text-classification
task_ids:
  - multi-class-classification
tags:
  - cognitive-distortion
  - mental-health
  - adolescent
  - korean
  - nlp
  - negotiation
  - llm
pretty_name: KoACD
size_categories:
  - 100K<n<1M
---

# KoACD: The First Korean Adolescent Dataset for Cognitive Distortion Analysis

> **EMNLP Findings 2025**  
> Jun Seo Kim (Gachon University) · Hye Hyeon Kim (Yonsei University)

## Dataset Description

KoACD is the first large-scale dataset of cognitive distortions in Korean adolescents, containing **108,717 instances** across 10 distortion types (Beck, 1979).

Data was collected from NAVER Knowledge iN (Q&A platform) and labeled using a **role-switching multi-LLM negotiation framework** (Gemini 1.5 Flash + GPT-4o mini), followed by synthetic data generation to balance class distribution.

## Dataset Structure


### Label Distribution

| Cognitive Distortion | Count | % |
|----------------------|-------|---|
| All-or-Nothing Thinking | 10,869 | 10.00% |
| Overgeneralization | 11,418 | 10.50% |
| Mental Filtering | 10,902 | 10.03% |
| Discounting the Positive | 10,695 | 9.84% |
| Jumping to Conclusions | 10,662 | 9.81% |
| Magnification and Minimization | 10,914 | 10.04% |
| Emotional Reasoning | 10,842 | 9.98% |
| Should Statements | 10,695 | 9.84% |
| Labeling | 10,836 | 9.97% |
| Personalization | 10,884 | 10.01% |

## Usage

```python
from datasets import load_dataset

ds = load_dataset("kma80kjs1/KoACD")


## Cognitive Distortion Types (Beck, 1979)

| # | Type | Definition |
|---|------|-----------|
| 1 | All-or-Nothing Thinking | Viewing situations in only two categories |
| 2 | Overgeneralization | Drawing broad conclusions from a single event |
| 3 | Mental Filtering | Focusing only on the negative aspects |
| 4 | Discounting the Positive | Rejecting positive experiences |
| 5 | Jumping to Conclusions | Predicting negative outcomes without evidence |
| 6 | Magnification and Minimization | Exaggerating negatives, minimizing positives |
| 7 | Emotional Reasoning | Believing something is true because it feels true |
| 8 | Should Statements | Holding rigid rules about behavior |
| 9 | Labeling | Assigning negative labels based on one event |
| 10 | Personalization | Blaming yourself for events outside your control |

## Data Collection & Construction

1. **Collection**: 69,925 Q&A posts from NAVER Knowledge iN (2011–2024), filtered to 37,124 adolescent utterances
2. **Negotiation Labeling**: Multi-LLM negotiation (Gemini 1.5 Flash ↔ GPT-4o mini, up to 5 rounds)
3. **Independent Validation**: Claude 3 Haiku scored each label (1–3); only score-3 pairs used
4. **Synthetic Data**: Two methods to ensure privacy and class balance
   - *Cognitive Clarification*: Rephrase original utterances (56,691 samples)
   - *Cognitive Balancing*: Generate from Unknown-labeled data (52,026 samples)

## Ethical Considerations

- All utterances are **synthetic** (generated from real data, not direct reproductions)
- Original data collected under NAVER Knowledge iN terms of service
- **For research use only** — commercial use is prohibited
- Two psychology experts (5+ years experience) validated 900 samples (Cohen's κ = 0.78)

## Citation

```bibtex
@inproceedings{kim2025koacd,
  title     = {KoACD: The First Korean Adolescent Dataset for Cognitive Distortion Analysis via Role-Switching Multi-LLM Negotiation},
  author    = {Kim, Jun Seo and Kim, Hye Hyeon},
  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},
  pages     = {22050--22078},
  year      = {2025}
}
```

