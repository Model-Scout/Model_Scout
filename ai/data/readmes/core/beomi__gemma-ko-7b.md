---
language:
- ko
- en
license: other
library_name: transformers
license_name: gemma-terms-of-use
license_link: https://ai.google.dev/gemma/terms
pipeline_tag: text-generation
tags:
- pytorch
---

# Gemma-Ko

> Update @ 2024.03.08: First release of Gemma-Ko 7B model

**Original Gemma Model Page**: [Gemma](https://ai.google.dev/gemma/docs)

This model card corresponds to the 7B base version of the **Gemma-Ko** model. 

**Resources and Technical Documentation**:

* [Original Google's Gemma-7B](https://huggingface.co/google/gemma-7b)
* [Training Code @ Github: Gemma-EasyLM](https://github.com/Beomi/Gemma-EasyLM)

**Terms of Use**: [Terms](https://www.kaggle.com/models/google/gemma/license/consent)

**Citation**

```bibtex
@misc {gemma_ko_7b,
	author       = { {Junbum Lee, Taekyoon Choi} },
	title        = { gemma-ko-7b },
	year         = 2024,
	url          = { https://huggingface.co/beomi/gemma-ko-7b },
	doi          = { 10.57967/hf/1859 },
	publisher    = { Hugging Face }
}
```

**Model Developers**: Junbum Lee (Beomi) & Taekyoon Choi (Taekyoon)

## Model Information

Summary description and brief definition of inputs and outputs.

### Description

Gemma is a family of lightweight, state-of-the-art open models from Google,
built from the same research and technology used to create the Gemini models.
They are text-to-text, decoder-only large language models, available in English,
with open weights, pre-trained variants, and instruction-tuned variants. Gemma
models are well-suited for a variety of text generation tasks, including
question answering, summarization, and reasoning. Their relatively small size
makes it possible to deploy them in environments with limited resources such as
a laptop, desktop or your own cloud infrastructure, democratizing access to
state of the art AI models and helping foster innovation for everyone.

### Usage

Below we share some code snippets on how to get quickly started with running the model. First make sure to `pip install -U transformers`, then copy the snippet from the section that is relevant for your usecase.

#### Running the model on a CPU

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("beomi/gemma-ko-7b")
model = AutoModelForCausalLM.from_pretrained("beomi/gemma-ko-7b")

input_text = "머신러닝과 딥러닝의 차이는"
input_ids = tokenizer(input_text, return_tensors="pt")

outputs = model.generate(**input_ids)
print(tokenizer.decode(outputs[0]))
```


#### Running the model on a single / multi GPU

```python
# pip install accelerate
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("beomi/gemma-ko-7b")
model = AutoModelForCausalLM.from_pretrained("beomi/gemma-ko-7b", device_map="auto")

input_text = "머신러닝과 딥러닝의 차이는"
input_ids = tokenizer(input_text, return_tensors="pt").to("cuda")

outputs = model.generate(**input_ids)
print(tokenizer.decode(outputs[0]))
```

#### Other optimizations

* _Flash Attention 2_

First make sure to install `flash-attn` in your environment `pip install flash-attn`

```diff
model = AutoModelForCausalLM.from_pretrained(
    "beomi/gemma-ko-7b", 
    torch_dtype=torch.float16, 
+   attn_implementation="flash_attention_2"
).to(0)
```

### Inputs and outputs

*   **Input:** Text string, such as a question, a prompt, or a document to be
    summarized.
*   **Output:** Generated Korean/English-language text in response to the input, such
    as an answer to a question, or a summary of a document.

## Implementation Information

Details about the model internals.

### Software

Training was done using [beomi/Gemma-EasyLM](https://github.com/Beomi/Gemma-EasyLM).


## Evaluation

Model evaluation metrics and results.

### Benchmark Results

TBD

## Usage and Limitations

These models have certain limitations that users should be aware of.

### Intended Usage

Open Large Language Models (LLMs) have a wide range of applications across
various industries and domains. The following list of potential uses is not
comprehensive. The purpose of this list is to provide contextual information
about the possible use-cases that the model creators considered as part of model
training and development.

* Content Creation and Communication
  * Text Generation: These models can be used to generate creative text formats
    such as poems, scripts, code, marketing copy, and email drafts.
* Research and Education
  * Natural Language Processing (NLP) Research: These models can serve as a
    foundation for researchers to experiment with NLP techniques, develop
    algorithms, and contribute to the advancement of the field.
  * Language Learning Tools: Support interactive language learning experiences,
    aiding in grammar correction or providing writing practice.
  * Knowledge Exploration: Assist researchers in exploring large bodies of text
    by generating summaries or answering questions about specific topics.

### Limitations

* Training Data
  * The quality and diversity of the training data significantly influence the
    model's capabilities. Biases or gaps in the training data can lead to
    limitations in the model's responses.
  * The scope of the training dataset determines the subject areas the model can
    handle effectively.
* Context and Task Complexity
  * LLMs are better at tasks that can be framed with clear prompts and
    instructions. Open-ended or highly complex tasks might be challenging.
  * A model's performance can be influenced by the amount of context provided
    (longer context generally leads to better outputs, up to a certain point).
* Language Ambiguity and Nuance
  * Natural language is inherently complex. LLMs might struggle to grasp subtle
    nuances, sarcasm, or figurative language.
* Factual Accuracy
  * LLMs generate responses based on information they learned from their
    training datasets, but they are not knowledge bases. They may generate
    incorrect or outdated factual statements.
* Common Sense
  * LLMs rely on statistical patterns in language. They might lack the ability
    to apply common sense reasoning in certain situations.

### Ethical Considerations and Risks

The development of large language models (LLMs) raises several ethical concerns.
In creating an open model, we have carefully considered the following:

* Bias and Fairness
  * LLMs trained on large-scale, real-world text data can reflect socio-cultural
    biases embedded in the training material. These models underwent careful
    scrutiny, input data pre-processing described and posterior evaluations
    reported in this card.
* Misinformation and Misuse
  * LLMs can be misused to generate text that is false, misleading, or harmful.
  * Guidelines are provided for responsible use with the model, see the
    [Responsible Generative AI Toolkit](http://ai.google.dev/gemma/responsible).
* Transparency and Accountability:
  * This model card summarizes details on the models' architecture,
    capabilities, limitations, and evaluation processes.
  * A responsibly developed open model offers the opportunity to share
    innovation by making LLM technology accessible to developers and researchers
    across the AI ecosystem.

Risks identified and mitigations:

* Perpetuation of biases: It's encouraged to perform continuous monitoring
  (using evaluation metrics, human review) and the exploration of de-biasing
  techniques during model training, fine-tuning, and other use cases.
* Generation of harmful content: Mechanisms and guidelines for content safety
  are essential. Developers are encouraged to exercise caution and implement
  appropriate content safety safeguards based on their specific product policies
  and application use cases.
* Misuse for malicious purposes: Technical limitations and developer and
  end-user education can help mitigate against malicious applications of LLMs.
  Educational resources and reporting mechanisms for users to flag misuse are
  provided. Prohibited uses of Gemma models are outlined in the
  [Gemma Prohibited Use Policy](https://ai.google.dev/gemma/prohibited_use_policy).
* Privacy violations: Models were trained on data filtered for removal of PII
  (Personally Identifiable Information). Developers are encouraged to adhere to
  privacy regulations with privacy-preserving techniques.

## Acknowledgement

The training is supported by [TPU Research Cloud](https://sites.research.google/trc/) program.