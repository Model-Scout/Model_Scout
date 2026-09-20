---
license: llama3.1
inference: false
language:
- en
- es
- pt
base_model:
- meta-llama/Llama-3.1-70B
library_name: transformers
tags: 
  - research
  - latin-america
  - cenia
  - latamgpt
---

<img src="assets/latam_gpt.png" alt="Logo" width="70%" />

# Llama-3.1-70B-LatamGPT-SFT-1.0

🌐 Language versions: [Español](README_es.md) | [Português](README_pt.md)

LatamGPT is a language model developed from Latin America and the Caribbean, with a focus on representing the region’s linguistic, cultural, and regional particularities. It is built on top of **Llama 3.1 70B** and adapted through **continued pretraining (CPT)** with Latin American data and **supervised fine-tuning (SFT)** focused on instruction following, conversation, and natural language processing tasks in Spanish, Portuguese, and English. This development strengthens technological sovereignty and the deployment of local capabilities, enabling the region to lead its own innovation.

The goal of LatamGPT is to provide an open, multilingual, and culturally relevant model that helps reduce the regional representation gap compared with global models, with better coverage of expressions, contexts, cultural references, and language uses specific to Latin America and the Caribbean.

## Model information

LatamGPT 1.0 is an autoregressive model based on the Transformer architecture. It inherits the general capabilities of Llama 3.1 70B and complements them with a regional adaptation process in two main stages:

1. **Continued pretraining (CPT):** specialization of the base model with data from Latin America.
2. **Supervised fine-tuning (SFT):** supervised adaptation to improve instruction following, conversational quality, usefulness, and performance on regional tasks.

**Supported languages:** Spanish, Portuguese, and English, with a special focus on Latin American variants, registers, and regional language use.

**License:** the use of the Llama 3.1 LatamGPT model is subject to the [Llama 3.1 Community License Agreement](https://www.llama.com/llama3_1/license/) Copyright © Meta Platforms, Inc. Built with Llama. We recommend carefully reviewing the applicable terms before redistributing, modifying, or deploying the model in production.

**Contact:** [latam-gpt@cenia.cl](mailto:latam-gpt@cenia.cl)

> **Note:** a data catalog and a technical model report will be published soon. These documents will provide more details about the data sources, curation criteria, training stages, evaluation methodology, and main limitations of LatamGPT.

## Intended uses

LatamGPT is intended for research, experimentation, application development, and commercial use in Latin American contexts where text generation, conversational assistance, summarization, classification, writing, analytical support, and other natural language processing tasks are required.

This model may be especially useful in scenarios where language, cultural references, or Latin American regional contexts are relevant to the quality of the responses.

### Out-of-scope uses

LatamGPT must not be used for purposes that violate applicable laws, regulations, third-party rights, or license terms. It should also not be used without additional controls in high-impact contexts, such as health, education, finance, justice, public safety, or other areas where an incorrect output could cause significant harm.

The model is not optimized for languages other than Spanish, Portuguese, and English. Although it may generate text in other languages, performance outside these three languages is not a primary objective of this version.

## How to use the model

### Memory requirements

LatamGPT is based on a 70B-parameter model. For inference in BF16/FP16 precision, approximately 140 GB of VRAM are required for the model weights alone, so the use of multiple high-memory GPUs is recommended.

### Use with Hugging Face Transformers

To use LatamGPT with `transformers`, you can load the model and tokenizer as follows:

```python
from transformers import pipeline
import torch

pipe = pipeline(
    "text-generation",
    model="latamgpt/Llama-3.1-70B-LatamGPT-SFT-1.0",
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

messages = [
    {"role": "system", "content": "You are a helpful, clear, and precise assistant, with a focus on Latin America and the Caribbean."},
    {"role": "user", "content": "Explain in a brief paragraph what LatamGPT is."},
]

out = pipe(messages, max_new_tokens=256, temperature=0.6, top_p=0.9, do_sample=True)
print(out[0]["generated_text"][-1]["content"])
```

## Important note

This model includes a predefined chat template and special tokenizer configuration. We recommend using the default tokenizer, chat template, and generation configuration provided in this repository.

Please avoid modifying the chat template or manually overriding the tokenizer settings, as the model relies on its predefined special tokens and conversational format. Changing these settings may degrade response quality or cause generations to terminate incorrectly.


## Training data

LatamGPT 1.0 was built from Llama 3.1 70B and adapted with regional data from Latin America and the Caribbean. The main focus of the training process was to incorporate representative data from the region, gathered through a strategic alliance of more than 75 institutions.

The continued pretraining stage was carried out with LatamGPT Corpus 1.0, a dataset composed of approximately 297B tokens. The dataset will be available soon on Hugging Face: [link coming soon].

This work covers data from 20 countries: Argentina, Brasil, Bolivia, Chile, Colombia, Costa Rica, Cuba, República Dominicana, Ecuador, El Salvador, Guatemala, Honduras, México, Nicaragua, Panamá, Paraguay, Perú, Puerto Rico, Uruguay, and Venezuela.

The regional data covers different thematic areas of cultural, social, historical, scientific, and territorial interest, including: Indigenous peoples, food and gastronomy, dialects and languages, historical events, celebrations and festivities, places and geography, arts, humanities and social sciences, communication and media, politics, important figures, mythology, flora and fauna, sports and recreation, economics and finance, hard sciences, education, and medicine and health.

The continued pretraining stage seeks to expand the model’s coverage of languages, expressions, entities, cultural references, and contexts specific to Latin America and the Caribbean.

The supervised fine-tuning stage incorporates examples aimed at improving instruction following, conversational interaction, and the model’s usefulness in natural language processing tasks.

The data construction process considers criteria of quality, traceability, and regional diversity. However, like any model trained on large text collections, LatamGPT may reflect biases, gaps, or errors present in its training data.

## Responsibility and safety

LatamGPT should be deployed as part of broader systems that incorporate safety controls, monitoring, and risk mitigation mechanisms. The model should not be considered an infallible source of information or used without human validation in high-impact contexts.

Those who integrate LatamGPT into products or services are responsible for defining appropriate usage policies, filters, evaluations, and limits for their specific application.

### Responsible deployment

Before deploying LatamGPT in production, we recommend:

* Evaluating the model in the specific domain of use.
* Implementing input and output filters when appropriate.
* Monitoring errors, biases, and misuse.
* Defining feedback and reporting mechanisms.
* Preventing the model from making critical decisions without human supervision.

## Ethical considerations and limitations

LatamGPT seeks to contribute to the development of language models that are more representative of Latin America. Even so, the model may produce incorrect, incomplete, biased, or outdated responses.

Its outputs should be interpreted as automatically generated content and not as professional advice. In sensitive applications, responses should be reviewed by domain experts before being used.

Its main limitations include:

* Possibility of hallucinations or factual errors.
* Performance variation across languages, countries, and domains.
* Reproduction of biases present in the data.
* Difficulty recognizing outdated information.
* Sensitivity to the prompt and provided context.
* Limited performance outside Spanish, Portuguese, and English.

## Citation

If you use LatamGPT in research, products, or technical reports, please cite the project using the following reference:

```bibtex
@misc{latamgpt2026,
  title        = {Llama-3.1-70B-LatamGPT-SFT-1.0},
  author       = {LatamGPT Team},
  year         = {2026},
  howpublished = {\url{https://huggingface.co/latam-gpt/Llama-3.1-70B-LatamGPT-SFT-1.0}}
}
```

## Acknowledgements

LatamGPT is made possible by the collaborative work of technical teams, institutions, communities, and organizations that contribute to the development of open and representative artificial intelligence for Latin America and the Caribbean.

<img src="assets/alianzas.png" alt="Alianzas" width="100%" />
