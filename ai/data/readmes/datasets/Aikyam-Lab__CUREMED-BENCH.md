---
license: cc-by-4.0
language:
- am
- fr
- ha
- bn
- hi
- ja
- ko
- es
- sw
- th
- vi
- yo
- tr
tags:
- medical
- multilingual
- benchmark
- LLM_Reasoning
pretty_name: 'CureMed-Bench: Multilingual Medical Reasoning Dataset '
size_categories:
- 10K<n<100K
task_categories:
- text-generation
---
# CUREMED-BENCH

CUREMED-BENCH is a multilingual medical reasoning benchmark dataset, designed for evaluating and fine-tuning models on medical tasks across diverse languages.

<!-- ![cure_med](https://cdn-uploads.huggingface.co/production/uploads/679a568f79c779b5238c3d71/-q5D6HwgP6HPFGNQEA-sA.png)
 -->

## Data


set Summary
- **Languages**: Spans 13 languages, including Amharic, Bengali, French, Hausa, Hindi, Japanese, Korean, Spanish, Swahili, Thai, Turkish, Vietnamese, and Yoruba.
- **Splits**: Includes train, test, and validation splits, each with separate CSV files per language.
- **Usage**: Intended for research in multilingual medical AI. 

## Structure
- `train_dataset/`: Training data CSVs.
- `test_dataset/`: Test data CSVs.
- `val_dataset/`: Validation data CSVs.

### Sources

- **Repository:** https://github.com/AikyamLab/cure-med
- **Paper:** https://arxiv.org/abs/2601.13262
- **Demo:** https://cure-med.github.io/




## Citation

**BibTeX:**
```bibtex
@article{onyame2026cure,
  title={CURE-Med: Curriculum-Informed Reinforcement Learning for Multilingual Medical Reasoning},
  author={Onyame, Eric and Ghosh, Akash and Baidya, Subhadip and Saha, Sriparna and Chen, Xiuying and Agarwal, Chirag},
  journal={arXiv preprint arXiv:2601.13262},
  year={2026}
}

