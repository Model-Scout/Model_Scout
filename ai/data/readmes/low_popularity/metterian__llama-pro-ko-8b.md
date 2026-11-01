---
language:
- en
- ko
pipeline_tag: text-generation
inference: false
tags:
- facebook
- meta
- pytorch
- llama
- llama-2
- llama-2-ko
- llama-pro-ko
license: apache-2.0
---



# LLaMA-Pro-Ko-8B Model Card

### Model Description



LLaMA-Pro is an advanced iteration of the original LLaMA model, augmented with additional Transformer blocks. Unlike its predecessor, Llama-pro, which was specialized for programming and mathematics, Llama-Pro-Ko is tailored to the language domain, undergoing post-training for enhanced performance.

## Development and Training

The NLP & AI Lab at Korea University developed LLaMA-Pro-Ko, a model boasting 8 billion parameters. This model extends LLaMA2-7B by incorporating Korean tokens via vocabulary extension and was further refined by training on a Korean corpus of 10 billion tokens, exclusively without the inclusion of English data.

### Language Specialization and Transfer

While previous models like Llama-ko and Llama-2-ko experienced diminished English capabilities as they learned Korean, Llama-Pro's language transfer approach aims to bolster Korean language performance with minimal impact on its English proficiency.

### Bilingual Performance Evaluation

LLaMA-Pro-Ko's performance is evaluated on two fronts: its proficiency in English and its mastery of Korean, showcasing its capabilities as a bilingual model.


![](figure.svg)

### Korean Evaluation


#### Open Ko LLM Benchmark

|                                                              | Ko-ARC    | Ko-HellaSwag | Ko-MMLU   | Ko-TruthfulQA | Ko-CommonGen V2 | AVG       |
| ------------------------------------------------------------ | --------- | ------------ | --------- | ------------- | --------------- | --------- |
| [Llama-2-7b](https://huggingface.co/NousResearch/Nous-Hermes-llama-2-7b) | 31.91     | 41.68        | 34.11     | 48.49         | 30.34           | 37.31     |
| [beomi/open-llama-2-ko-7b](https://huggingface.co/beomi/open-llama-2-ko-7b) | 40.02     | 50.27        | 27.60     | 38.67         | 42.15           | 39.74     |
| llama-pro-ko-8b                                              | **40.19** | **51.26**    | **36.80** | **40.24**     | **43.8**        | **42.46** |





### English Evaluation

#### Open LLM Benchmark

|                                                              |    ARC    |  HellaSwag   |   MMLU    |  TruthfulQA  |  Winogrande  |     AVG      |   diff    |
| :----------------------------------------------------------- | :-------: | :----------: | :-------: | :----------: | :----------: | :----------: | :-------: |
| [meta-llama/Llama-2-7b](https://huggingface.co/meta-llama/Llama-2-7b) |   53.07   |  **78.59**   |   46.87   |  **38.76**   |  **74.03**   |  **58.26**   |     0     |
| [beomi/llama-2-ko-7b](https://huggingface.co/beomi/llama-2-ko-7b) |   48.46   |    75.28     |   39.56   |    34.49     |    72.14     |    53.99     |   -4.28   |
| [beomi/open-llama-2-ko-7b](https://huggingface.co/beomi/open-llama-2-ko-7b) |   46.84   |    69.48     |   29.86   |    35.35     |    66.30     |    49.57     |   -8.70   |
| llama-pro-ko-8b                                              | **53.24** | <u>77.93</u> | **47.06** | <u>38.32</u> | <u>72.22</u> | <u>57.75</u> | **-0.51** |


