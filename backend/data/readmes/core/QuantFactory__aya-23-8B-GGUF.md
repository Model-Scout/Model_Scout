---
library_name: transformers
base_model: CohereForAI/aya-23-8B
language:
- en
- fr
- de
- es
- it
- pt
- ja
- ko
- zh
- ar
- el
- fa
- pl
- id
- cs
- he
- hi
- nl
- ro
- ru
- tr
- uk
- vi
license: cc-by-nc-4.0
pipeline_tag: text-generation
tags:
- cohere
---

# Aya-23-8B-GGUF
- This is quantized version of [CohereForAI/aya-23-8B](https://huggingface.co/CohereForAI/aya-23-8B) created using llama.cpp

# Model Description

Aya 23 is an open weights research release of an instruction fine-tuned model with highly advanced multilingual capabilities. Aya 23 focuses on pairing a highly performant pre-trained [Command family](https://huggingface.co/CohereForAI/c4ai-command-r-plus) of models with the recently released [Aya Collection](https://huggingface.co/datasets/CohereForAI/aya_collection). The result is a powerful multilingual large language model serving 23 languages.

This model card corresponds to the 8-billion version of the Aya 23 model. We also released a 35-billion version which you can find [here](https://huggingface.co/CohereForAI/aya-23-35B).

We cover 23 languages: Arabic, Chinese (simplified & traditional), Czech, Dutch, English, French, German, Greek, Hebrew, Hindi, Indonesian, Italian, Japanese, Korean, Persian, Polish, Portuguese, Romanian, Russian, Spanish, Turkish, Ukrainian, and Vietnamese

Developed by: [Cohere For AI](https://cohere.for.ai) and [Cohere](https://cohere.com/) 

- Point of Contact: Cohere For AI: [cohere.for.ai](https://cohere.for.ai/)
- License: [CC-BY-NC](https://cohere.com/c4ai-cc-by-nc-license), requires also adhering to [C4AI's Acceptable Use Policy](https://docs.cohere.com/docs/c4ai-acceptable-use-policy)
- Model: aya-23-8B
- Model Size: 8 billion parameters

**Try Aya 23**

You can try out Aya 23 (35B) before downloading the weights in our hosted Hugging Face Space [here](https://huggingface.co/spaces/CohereForAI/aya-23).

### Usage

Please install transformers from the source repository that includes the necessary changes for this model

```python
# pip install transformers==4.41.1
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "CohereForAI/aya-23-8B"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

# Format message with the command-r-plus chat template
messages = [{"role": "user", "content": "Anneme onu ne kadar sevdiğimi anlatan bir mektup yaz"}]
input_ids = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt")
## <BOS_TOKEN><|START_OF_TURN_TOKEN|><|USER_TOKEN|>Anneme onu ne kadar sevdiğimi anlatan bir mektup yaz<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>

gen_tokens = model.generate(
    input_ids, 
    max_new_tokens=100, 
    do_sample=True, 
    temperature=0.3,
    )

gen_text = tokenizer.decode(gen_tokens[0])
print(gen_text)
```

### Example Notebook

[This notebook](https://huggingface.co/CohereForAI/aya-23-8B/blob/main/Aya_23_notebook.ipynb) showcases a detailed use of Aya 23 (8B) including inference and fine-tuning with [QLoRA](https://huggingface.co/blog/4bit-transformers-bitsandbytes). 

## Model Details

**Input**: Models input text only.

**Output**: Models generate text only.

**Model Architecture**: Aya-23-8B is an auto-regressive language model that uses an optimized transformer architecture. After pretraining, this model is fine-tuned (IFT) to follow human instructions.

**Languages covered**: The model is particularly optimized for multilinguality and supports the following languages: Arabic, Chinese (simplified & traditional), Czech, Dutch, English, French, German, Greek, Hebrew, Hindi, Indonesian, Italian, Japanese, Korean, Persian, Polish, Portuguese, Romanian, Russian, Spanish, Turkish, Ukrainian, and Vietnamese

**Context length**: 8192

### Evaluation

<img src="benchmarks.png" alt="multilingual benchmarks" width="650" style="margin-left:'auto' margin-right:'auto' display:'block'"/>
<img src="winrates.png" alt="average win rates" width="650" style="margin-left:'auto' margin-right:'auto' display:'block'"/>

Please refer to the [Aya 23 technical report](https://cohere.com/research/papers/aya-command-23-8b-and-35b-technical-report-2024-05-23) for further details about the base model, data, instruction tuning, and evaluation.

### Terms of Use

We hope that the release of this model will make community-based research efforts more accessible, by releasing the weights of a highly performant multilingual model to researchers all over the world. This model is governed by a [CC-BY-NC](https://cohere.com/c4ai-cc-by-nc-license) License with an acceptable use addendum, and also requires adhering to [C4AI's Acceptable Use Policy](https://docs.cohere.com/docs/c4ai-acceptable-use-policy).