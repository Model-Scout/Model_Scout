---
license: apache-2.0
task_categories:
- text-generation
- text-classification
language:
- en
- pt
- hi
- it
- fr
- ru
- ar
- ko
- es
tags:
- harmful
- toxic
---

# From One to Many: Expanding the Scope of Toxicity Mitigation in Language Models

[[arxiv]](https://arxiv.org/pdf/2403.03893)[[code]](https://github.com/for-ai/goodtriever)[[data]](https://huggingface.co/datasets/luizapzbn/from-one-to-many-toxicity-mitigation)

Data accompanying the paper "From One to Many: Expanding the Scope of Toxicity Mitigation in Language Models" accepted to ACL Findings 2024.

_Abstract_: To date, toxicity mitigation in language models has almost entirely been focused on single-language settings. As language models embrace multilingual capabilities, it’s crucial our safety measures keep pace. Recognizing this research gap, our approach expands the scope of conventional toxicity mitigation to address the complexities presented by multiple languages. In the absence of sufficient annotated datasets across languages, we employ translated data to evaluate and enhance our mitigation techniques. We also compare finetuning mitigation approaches against retrieval-augmented techniques under both static and continual toxicity mitigation scenarios. This allows us to examine the effects of translation quality and the cross-lingual transfer on toxicity mitigation. We also explore how model size and data quantity affect the success of these mitigation efforts. Covering nine languages, our study represents a broad array of linguistic families and levels of resource availability, ranging from high to mid-resource languages. Through comprehensive experiments, we provide insights into the complexities of multilingual toxicity mitigation, offering valuable insights and paving the way for future research in this increasingly important field. 

## Dataset Description

- **Language(s) (NLP):** English, Portuguese, Spanish, Italian, French, Russian, Arabic, Hindi, Korean
- **License:** This dataset is a translation of existing datasets. Each dataset's original license applies. For more details see the "Source Data" section.

## Dataset Structure

- train:
  - jigsaw_english: original Jigsaw Unintended Bias dataset in the English language.
  - multilingual:
    - jigsaw_multilingual: in-language examples from the Jigsaw Multilingual Toxicity classification challenge.
    - translated_jigsaw_english: translated samples from the Jigsaw Unintended Bias Challenge. Original samples are in the "jigsaw_english" folder one level up.
      - full_sized: translations of the jigsaw dataset in its entirety
      - minimal: for our main experiments, we selected ~3K (or 3.5K) and ~10K toxic and non-toxic samples, respectively. Here are those subsets, translated by NLLB 600M model.
        - nllb1.3b: the same subset of data for all languages, but translated with the NLLB 1.3B model (higher translation quality)
        - m2m: the same subset of data for all languages, but translated with the M2M 418M model (lower translation quality)
        - different_subsets: we selected different subsets for each of the languages (unparalleled content) and translated them with NLLB 600M
        - bleu_subset: samples used to compute BLEU scores for the paper
- eval: a random subset of 200 samples of holistic bias (English) translated with Google Translate to each of the target languages. The contents are the same across all languages.
  - _hi: the eval set of the high-resource language experiments
  - _mid: the eval set of the mid-resource language experiments
  - individual: folder with the individual samples for each language
- results: all of the models generations and experiments from the paper. to be used with the results notebook to generate plots (15GB of data though)


## Source Data

The datasets from this repository are subsets or translations of three others:

- [jigsaw multilingual toxicity classification](https://www.kaggle.com/c/jigsaw-multilingual-toxic-comment-classification)
- [jigsaw unintended bias (english)](https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification)
- [holistic bias](https://arxiv.org/abs/2205.09209)

## Bias, Risks, and Limitations

To generate these datasets, we leveraged machine translation. There are inherent risks of either increasing or reducing existing toxicity from the original sentences due to this processing. 
The datasets contain toxic sentences that might be used to make models more toxic. This usage is highly discouraged by the authors and the original purpose of this dataset is to make models less harmful.

## Citation [optional]
```
@article{pozzobon2024one,
  title={From One to Many: Expanding the Scope of Toxicity Mitigation in Language Models},
  author={Pozzobon, Luiza and Lewis, Patrick and Hooker, Sara and Ermis, Beyza},
  journal={arXiv preprint arXiv:2403.03893},
  year={2024}
}
```