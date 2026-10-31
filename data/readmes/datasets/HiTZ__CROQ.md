---
license: cc-by-nc-sa-4.0
task_categories:
- text-generation
language:
- en
- zh
- hi
- es
- ar
- fr
- bn
- pt
- ru
- id
- de
- ja
- ko
- fa
- sw
- ha
- az
- am
- su
- el
- as
- ca
- gl
- eu
pretty_name: CROQ
size_categories:
- 10K<n<100K
configs:
- config_name: default
  data_files:
  - split: eval
    path: eval.csv
tags:
- culture
- bias
- llm
---

# 🌍🏺 CROQ: Culture-Related Open Questions

*A multilingual benchmark for evaluating cultural and regional biases in large language models through open-ended cultural questions.*

**CROQ (Culture-Related Open Questions)** is a multilingual dataset designed to uncover cultural and regional biases in large language models (LLMs). Unlike traditional cultural benchmarks based on multiple-choice or factual questions, CROQ focuses on **open-ended cultural questions** that have no single correct answer and require models to implicitly ground their responses in a particular cultural or geographic context.

The dataset was introduced in:

> **Why are all LLMs Obsessed with Japanese Culture? On the Hidden Cultural and Regional Biases of LLMs**

- 📚 arXiv: https://arxiv.org/abs/2604.21751

![cultural_bias_preprint](https://cdn-uploads.huggingface.co/production/uploads/66daba48947b2e8abc23962c/nxWagmanqsyBABv6g1UQN.png)


## CROQ Dataset Summary:

* **11 broad cultural domains**
* **66 cultural subtopics**
* **1,320 culture-related open questions (en)**
* **24 languages**
* **31,680 total multilingual questions** after translation across all languages. 

The dataset is designed to study:

* Regional cultural preferences in LLM outputs
* The effect of prompting language on cultural grounding
* Cultural diversity and regional coverage in model generations
* Emergence of cultural biases during model training and post-training stages 

---

## Languages

CROQ is available in **24 languages**:

Amharic (am), Arabic (ar), Assamese (as), Azerbaijani (az), Basque (eu), Bengali (bn), Catalan (ca), Chinese (zh), English (en), French (fr), Galician (gl), German (de), Greek (el), Hausa (ha), Hindi (hi), Indonesian (id), Japanese (ja), Korean (ko), Persian (fa), Portuguese (pt), Russian (ru), Spanish (es), Sundanese (su) and Swahili (sw). 

---

## Dataset Structure

### Data Fields

| Field | Type | Description |
|---------|---------|-------------|
| `ID` | string | Identifier for each Culture-related open question |
| `Topic` | string | High-level cultural topic |
| `Sub-Topic` | string | Fine-grained cultural category |
| language | string | Open question for each language identifier (ISO 639-1) |

---

## Cultural Topics

CROQ covers **11 major cultural domains**:

* beliefs, values and identity
* social structure and daily life
* knowledge, communication and education
* cultural expression and the arts
* food, drink and leisure
* geographic aspects
* political aspects
* health and wellness
* media and entertainment
* history
* economy and industry 

These domains are further divided into **66 subtopics**, providing broad coverage of culturally relevant concepts and practices. 

---

## Example Questions

Questions are intentionally open-ended and avoid mentioning specific countries or cultures directly.

Examples include:

* "What legends explain the land {in region/place}?"
* "What is the role of neighbors {in region/place}?"
* "What subjects are most valued {in region/place}?"
* "What traditional dances exist {in region/place}?"
* "What foods are for daily meal {in region/place}?"
* "What rivers influence settlements {in region/place}?"
* "What political protests are common {in region/place}?"
* "What exercise routines are common {in region/place}?"
* "What film industries exist {in region/place}?"
* "What historical tours exist {in region/place}?"
* "What commodity markets exist {in region/place}?" 

---

## Evaluation Framework

To reveal cultural preferences, models are prompted with an open cultural question and asked to implicitly choose a location when answering.

Example prompt:

> What values shape family life {in region/place}? Be brief. Choose yourself the place.

Model responses are subsequently processed to identify the country or region referenced, allowing researchers to analyze cultural and geographic tendencies.

---




## Citation

If you use CROQ, please cite the reference paper, to be published in Findings of EMNLP 2026:

```
@article{delanda2026,
  title={Why are all LLMs Obsessed with Japanese Culture? On the Hidden Cultural and Regional Biases of LLMs},
  author={Fernandez de Landa, Joseba and Perez-Almendros, Carla and Camacho-Collados, Jose},
  journal={arXiv preprint arXiv:2604.21751},
  year={2026}
}
```