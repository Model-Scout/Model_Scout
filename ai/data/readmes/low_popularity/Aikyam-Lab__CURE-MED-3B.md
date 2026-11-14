---
library_name: transformers
tags:
- reasoning
- text-generation
- medical-ai
- multilingual-ai
- healthcare
- LLMs
license: apache-2.0
datasets:
- Aikyam-Lab/CUREMED-BENCH
language:
- am
- bn
- fr
- ha
- hi
- ja
- ko
- es
- sw
- th
- tr
- vi
- yo
base_model:
- Qwen/Qwen2.5-3B-Instruct
pipeline_tag: text-generation
---

# Model Card for Model ID

CURE-MED-3B is a 3 billion parameter large language model specialized for multilingual medical reasoning, fine-tuned from Qwen/Qwen2.5-3B-instruct using a
curriculum-informed reinforcement learning framework to enhance logical correctness and language stability in healthcare applications.

![cure_med](https://cdn-uploads.huggingface.co/production/uploads/679a568f79c779b5238c3d71/aTj-4j0RRntuhwDwCE5R-.png)

## Model Details

CURE-MED-3B is part of the CURE-MED family of models, designed to address the challenges of multilingual medical reasoning in large language models (LLMs).
Built on the Qwen2.5-3B-instruct model, it incorporates a curriculum-informed reinforcement learning approach that integrates code-switching-aware supervised fine-tuning (SFT)
and Group Relative Policy Optimization (GRPO) to improve performance on open-ended medical queries across 13 languages, including underrepresented ones such as Amharic, Yoruba, and Swahili.
The model is trained and evaluated using CUREMED-BENCH, a high-quality multilingual open-ended medical reasoning benchmark with single verifiable answers.

### Model Description

<!-- Provide a longer summary of what this model is. -->

This is the model card of a 🤗 transformers model that has been pushed on the Hub. 

- **Developed by:** Eric Onyame, Akash Ghosh, Subhadip Baidya, Sriparna Saha, Xiuying Chen, Chirag Agarwal (Aikyam Lab and collaborators)
- **Shared by:** Aikyam Lab
- **Model type:** Multilingual medical reasoning large language model
- **Language(s) (NLP):** Amharic, Bengali, French, Hausa, Hindi, Japanese, Korean, Spanish, Swahili, Thai, Turkish, Vietnamese, Yoruba
- **License:** Apache 2.0
- **Finetuned from model:** Qwen2.5-Instruct (1.5B, 3B, 7B, 14B, 32B variants)


### Model Sources

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


