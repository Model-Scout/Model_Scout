---
inference: false
library_name: transformers
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
---

# Model Card for Aya Expanse 8B Ungated

Aya-Expanse 8B, but not gated!

<img src="aya-expanse-8B.png" width="650" style="margin-left:'auto' margin-right:'auto' display:'block'"/>

**Aya Expanse 8B** is an open-weight research release of a model with highly advanced multilingual capabilities. It focuses on pairing a highly performant pre-trained [Command family](https://huggingface.co/CohereForAI/c4ai-command-r-plus) of models with the result of a year’s dedicated research from [Cohere For AI](https://cohere.for.ai/), including [data arbitrage](https://arxiv.org/abs/2408.14960), [multilingual preference training](https://arxiv.org/abs/2407.02552), [safety tuning](https://arxiv.org/abs/2406.18682), and [model merging](https://arxiv.org/abs/2410.10801). The result is a powerful multilingual large language model.

This model card corresponds to the 8-billion version of the Aya Expanse model. We also released an 32-billion version which you can find [here](https://huggingface.co/CohereForAI/aya-expanse-32B).

- Developed by: [Cohere For AI](https://cohere.for.ai/) 
- Point of Contact: Cohere For AI: [cohere.for.ai](https://cohere.for.ai/)
- License: [CC-BY-NC](https://cohere.com/c4ai-cc-by-nc-license), requires also adhering to [C4AI's Acceptable Use Policy](https://docs.cohere.com/docs/c4ai-acceptable-use-policy)
- Model: Aya Expanse 8B
- Model Size: 8 billion parameters

### Supported Languages

We cover 23 languages: Arabic, Chinese (simplified & traditional), Czech, Dutch, English, French, German, Greek, Hebrew, Hebrew, Hindi, Indonesian, Italian, Japanese, Korean, Persian, Polish, Portuguese, Romanian, Russian, Spanish, Turkish, Ukrainian, and Vietnamese.

### Try it: Aya Expanse in Action

Use the [Cohere playground](https://dashboard.cohere.com/playground/chat) or our [Hugging Face Space](https://huggingface.co/spaces/CohereForAI/aya_expanse) for interactive exploration.

### How to Use Aya Expanse

Install the transformers library and load Aya Expanse 8B as follows:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "CohereForAI/aya-expanse-8b"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

# Format the message with the chat template
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

### Example Notebooks

**Fine-Tuning:**
- [Detailed Fine-Tuning Notebook](https://colab.research.google.com/drive/1ryPYXzqb7oIn2fchMLdCNSIH5KfyEtv4).

**Community-Contributed Use Cases:**:

The following notebooks contributed by *Cohere For AI Community* members show how Aya Expanse can be used for different use cases:
- [Mulitlingual Writing Assistant](https://colab.research.google.com/drive/1SRLWQ0HdYN_NbRMVVUHTDXb-LSMZWF60)
- [AyaMCooking](https://colab.research.google.com/drive/1-cnn4LXYoZ4ARBpnsjQM3sU7egOL_fLB?usp=sharing)
- [Multilingual Question-Answering System](https://colab.research.google.com/drive/1bbB8hzyzCJbfMVjsZPeh4yNEALJFGNQy?usp=sharing)


## Model Details

**Input**: Models input text only.

**Output**: Models generate text only.

**Model Architecture**: Aya Expanse 8B is an auto-regressive language model that uses an optimized transformer architecture. Post-training includes supervised finetuning, preference training, and model merging.

**Languages covered**: The model is particularly optimized for multilinguality and supports the following languages: Arabic, Chinese (simplified & traditional), Czech, Dutch, English, French, German, Greek, Hebrew, Hindi, Indonesian, Italian, Japanese, Korean, Persian, Polish, Portuguese, Romanian, Russian, Spanish, Turkish, Ukrainian, and Vietnamese

**Context length**: 8K

For more details about how the model was trained, check out [our blogpost](https://huggingface.co/blog/aya-expanse).

### Evaluation

We evaluated Aya Expanse 8B against Gemma 2 9B, Llama 3.1 8B, Ministral 8B, and Qwen 2.5 7B using Dolly and m-ArenaHard, a dataset based on the [Arena-Hard-Auto dataset](https://huggingface.co/datasets/lmarena-ai/arena-hard-auto-v0.1) and translated to the 23 languages we support in Aya Expanse 8B. Win-rates were determined using gpt-4o-2024-08-06 as a judge. For a conservative benchmark, we report results from gpt-4o-2024-08-06, though gpt-4o-mini scores showed even stronger performance.

The m-ArenaHard dataset, used to evaluate Aya Expanse’s capabilities, is publicly available [here](https://huggingface.co/datasets/CohereForAI/m-ArenaHard).

<img src="winrates_marenahard_complete.png" width="650" style="margin-left:'auto' margin-right:'auto' display:'block'"/>
<img src="winrates_dolly.png" width="650" style="margin-left:'auto' margin-right:'auto' display:'block'"/>
<img src="winrates_by_lang.png"  width="650" style="margin-left:'auto' margin-right:'auto' display:'block'"/>
<img src="winrates_step_by_step.png"  width="650" style="margin-left:'auto' margin-right:'auto' display:'block'"/>


### Model Card Contact

For errors or additional questions about details in this model card, contact info@for.ai.

### Terms of Use

We hope that the release of this model will make community-based research efforts more accessible, by releasing the weights of a highly performant multilingual model to researchers all over the world. This model is governed by a [CC-BY-NC](https://cohere.com/c4ai-cc-by-nc-license) License with an acceptable use addendum, and also requires adhering to [C4AI's Acceptable Use Policy](https://docs.cohere.com/docs/c4ai-acceptable-use-policy).
