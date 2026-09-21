---
license: mit
language:
- ko
- en
metrics:
- perplexity
- accuracy
pipeline_tag: text-generation
tags:
- llama
- KoLLAMA
- KoreanGPT
---

> 🚧 Note: this repo is under construction 🚧

## Todo

✅ - finish

⏳ - currently working on it


- ✅ Train new BBPE Tokenizer
- ✅ Test train code on TPUv4 Pods (with model parallel)
- ✅ Converting test (jax to PyTorch)
- ✅ LM train validation on minimal dataset (1 sentence 1000 step)
- ⏳ Build Data Shuffler (curriculum learning)
- ⏳ Train 7B Model
- ⏳ Train 13B Model
- Train 33B Model
- Train 65B Model



# KoLLaMA-13B Model Card

KoLLaMA (13B) trained on Korean/English/Code dataset with LLaMA Architecture via JAX,
with the warm support from [Google TPU Research Cloud program](https://sites.research.google/trc/about/) for providing part of the computation resources. 


## Model details

**Researcher developing the model**

Junbum Lee (aka Beomi)

**Model date**

KoLLaMA was trained between 2022.04~

**Model version**

This is alpha version of the model.

**Model type**

LLaMA is an auto-regressive language model, based on the transformer architecture. The model comes in different sizes: 7B, 13B, 33B and 65B parameters.

(This repo contains 13B model!)

**Paper or resources for more information**

More information can be found in the paper “LLaMA, Open and Efficient Foundation Language Models”, available at https://research.facebook.com/publications/llama-open-and-efficient-foundation-language-models/.

More info for KoAlpaca:

[TBD]

**Citations details**

KoLLAMA: [TBD]
LLAMA: https://research.facebook.com/publications/llama-open-and-efficient-foundation-language-models/

**License**

MIT

**Where to send questions or comments about the model**

Questions and comments about KoLLaMA can be sent via the [GitHub repository](https://github.com/beomi/KoLLAMA) of the project , by opening an issue.

## Intended use
**Primary intended uses**

The primary use of KoLLaMA is research on Korean Opensource large language models

**Primary intended users**

The primary intended users of the model are researchers in natural language processing, machine learning and artificial intelligence.

**Out-of-scope use cases**

LLaMA is a base, or foundational, model. As such, it should not be used on downstream applications without further risk evaluation and mitigation. In particular, our model has not been trained with human feedback, and can thus generate toxic or offensive content, incorrect information or generally unhelpful answers.

## Factors

**Relevant factors**

One of the most relevant factors for which model performance may vary is which language is used. Although we included 20 languages in the training data, most of our dataset is made of English text, and we thus expect the model to perform better for English than other languages. Relatedly, it has been shown in previous studies that performance might vary for different dialects, and we expect that it will be the case for our model.

## Evaluation datasets

[TBD]


## Training dataset

[TBD]

## Ethical considerations

**Data**

The data used to train the model is collected from various sources, mostly from the Web. As such, it contains offensive, harmful and biased content. We thus expect the model to exhibit such biases from the training data.

**Human life**

The model is not intended to inform decisions about matters central to human life, and should not be used in such a way.

**Risks and harms**

Risks and harms of large language models include the generation of harmful, offensive or biased content. These models are often prone to generating incorrect information, sometimes referred to as hallucinations. We do not expect our model to be an exception in this regard.

**Use cases**

LLaMA is a foundational model, and as such, it should not be used for downstream applications without further investigation and mitigations of risks. These risks and potential fraught use cases include, but are not limited to: generation of misinformation and generation of harmful, biased or offensive content.