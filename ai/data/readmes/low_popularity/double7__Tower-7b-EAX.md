---
license: cc-by-nc-4.0
datasets:
- Unbabel/TowerBlocks-v0.1
language:
- en
- de
- fr
- nl
- it
- es
- pt
- ko
- ru
- zh
metrics:
- bleurt
- comet
library_name: transformers
base_model:
- Unbabel/TowerBase-7B-v0.1
pipeline_tag: text-generation
---
# Model Card for Tower-7b-EAX

<a href="https://arxiv.org/abs/2509.19770">
  <img src="https://img.shields.io/badge/EAX-Paper-blue"></a>
<a href="https://huggingface.co/collections/double7/enanchored-x2x-6830338f017061c30226107d">
  <img src="https://img.shields.io/badge/EAX-Hugging Face-brightgreen"></a>
<a href="https://github.com/NJUNLP/EAX">
    <img src="https://img.shields.io/badge/EAX-Github-purple"></a>
<a href="https://huggingface.co/meta-llama/Llama-2-7b-chat-hf/blob/main/LICENSE.txt">
  <img src="https://img.shields.io/badge/License-cc--by--nc--4.0-yellow"></a>

## Model Details

### Model Description

Tower-7b-EAX is a language model specifically enhanced for inter non-English language pairs.
The model is built on top of TowerBase, following a two-stage training approach: first, an English-centric parallel data supervised fine-tuning stage (the SFT model is available at [Llama-2-7b-MT-SFT](https://huggingface.co/double7/Llama-2-7b-MT-SFT)), followed by a dedicated x2x optimization stage.
This approach strategically leverages the established English-centric capabilities of large language models to bootstrap comprehensive multilingual translation capabilities.

<img src="imgs/pref_overview_tower_comet.png" alt="performance overview" style="width:800px; height:auto;">


- **Model type:** A 7B parameter translation model built on top of TowerBase, enhanced for x2x language pairs through specialized optimization.
- **Language(s) (NLP):** English, Portuguese, Spanish, French, German, Dutch, Italian, Korean, Russian, Chinese
- **License:** CC-BY-NC-4.0, The LLAMA 2 Community License, Copyright © Meta Platforms, Inc. All Rights Reserved.


## Intended uses & limitations

Tower-7b-EAX is designed for direct translation between non-English language pairs, addressing a significant gap in current LLM translation capabilities.
The model maintains strong performance on English-centric translation while significantly improving x2x translation quality.


Here's how you can run the model with Huggingface Transformers:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_PATH = "double7/Tower-7b-EAX"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH, device_map="auto", torch_dtype="auto"
)

src_lang = "German"
trg_lang = "Chinese"
src_text = "Filmkarriere Collinges Filmdebüt in Die kleinen Füchse von 1941 brachte ihr eine Nominierung für den Academy Award als beste Nebendarstellerin ein."

prompt = f"Translate the following text from {src_lang} into {trg_lang}:\n{src_lang}: {src_text}\n{trg_lang}:"

# We use the tokenizer’s chat template to format each message - see https://huggingface.co/docs/transformers/main/en/chat_templating
messages = [
    {"role": "user", "content": prompt},
]

input_text = tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)

inputs = tokenizer(input_text, return_tensors="pt").to(model.device)

outputs = model.generate(**inputs, do_sample=False, max_new_tokens=256)
output_text = tokenizer.batch_decode(outputs, skip_special_tokens=False)[0]
print(output_text)
# <s><|im_start|> user
# Translate the following text from German into Chinese:
# German: Filmkarriere Collinges Filmdebüt in Die kleinen Füchse von 1941 brachte ihr eine Nominierung für den Academy Award als beste Nebendarstellerin ein.
# Chinese:<|im_end|> 
# <|im_start|> assistant
# 电影生涯 科林格的电影处女作《小狐狸》于 1941 年上映，她因此获得了奥斯卡最佳女配角提名。<|im_end|>

```

### Translation Instructions

Following [TowerInstruct](https://arxiv.org/pdf/2402.17733), we use diverse translation instructions in training, you can use natural language to describe translation requests, such as:
```python
prompt1 = f"Translate the following text from {src_lang} into {trg_lang}:\n{src_lang}: {src_text}\n{trg_lang}:"

prompt1 = f"Please provide a translation from {src_lang} to {trg_lang} for the following text:\n{src_text}\nTarget:",

prompt2 = f"Translate this {src_lang} text into {trg_lang}:\nSource: {src_text}\nTranslation:",
```

We use `prompt1` for the evaluation.

### Out-of-Scope Use

The model is not guaranteed to perform for languages other than the 10 languages it supports.

## Bias, Risks, and Limitations

Tower-7b-EAX has not been aligned to human preferences, so the model may generate problematic outputs (e.g., hallucinations, harmful content, or false statements).  


## Prompt Format

Tower-7b-EAX was trained using the `ChatML` prompt templates without any system prompts. An example follows below:
```
<|im_start|>user
{USER PROMPT}<|im_end|>
<|im_start|>assistant
{MODEL RESPONSE}<|im_end|>
<|im_start|>user
[...]
```


## Training Details

### Training Data

We use ~250k high-confidence synthetic data for optimization. This data is based on [TowerBase-7B](https://huggingface.co/Unbabel/TowerBase-7B-v0.1) and the translation data from [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.1) as seeds, and was curated through our specialized pipeline.
See our [paper](https://arxiv.org/abs/2509.19770) for more details.


### Training hyperparameters

The following hyperparameters were used during x2x training:
- learning_rate: 2e-07
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 1
- max_seq_length: 2048
- DPO beta: 0.4
- SFT coefficient: 2.0


## Citation 

```bibtex
@misc{yang2025enanchoredx2xenglishanchoredoptimizationmanytomany,
      title={EnAnchored-X2X: English-Anchored Optimization for Many-to-Many Translation}, 
      author={Sen Yang and Yu Bao and Yu Lu and Jiajun Chen and Shujian Huang and Shanbo Cheng},
      year={2025},
      eprint={2509.19770},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2509.19770}, 
}
```