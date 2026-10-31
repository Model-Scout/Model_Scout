---
license: cc-by-nc-sa-4.0
task_categories:
- text-generation
- text-classification
- token-classification
- fill-mask
- table-question-answering
- text2text-generation
language:
- ko
tags:
- synthetic
- text
- math
- reasoning
- instruction
- tool
size_categories:
- 100K<n<1M
dataset_info:
- config_name: instruction
  features:
  - name: input persona
    dtype: string
  - name: synthesized text
    dtype: string
  - name: description
    dtype: string
  splits:
  - name: train
    num_bytes: 25442729
    num_examples: 49997
  download_size: 14031303
  dataset_size: 25442729
- config_name: knowledge
  features:
  - name: input persona
    dtype: string
  - name: synthesized text
    dtype: string
  - name: description
    dtype: string
  splits:
  - name: train
    num_bytes: 44285672
    num_examples: 9901
  download_size: 23534289
  dataset_size: 44285672
- config_name: math
  features:
  - name: input persona
    dtype: string
  - name: synthesized text
    dtype: string
  - name: description
    dtype: string
  splits:
  - name: train
    num_bytes: 49997172
    num_examples: 49999
  download_size: 26509975
  dataset_size: 49997172
- config_name: npc
  features:
  - name: input persona
    dtype: string
  - name: synthesized text
    dtype: string
  - name: description
    dtype: string
  splits:
  - name: train
    num_bytes: 23385592
    num_examples: 10000
  download_size: 12715690
  dataset_size: 23385592
- config_name: persona
  features:
  - name: persona
    dtype: string
  splits:
  - name: train
    num_bytes: 19224190
    num_examples: 200000
  download_size: 12140123
  dataset_size: 19224190
- config_name: reasoning
  features:
  - name: input persona
    dtype: string
  - name: synthesized text
    dtype: string
  - name: description
    dtype: string
  splits:
  - name: train
    num_bytes: 40392913
    num_examples: 49999
  download_size: 21694747
  dataset_size: 40392913
- config_name: tool
  features:
  - name: input persona
    dtype: string
  - name: synthesized text
    dtype: string
  - name: description
    dtype: string
  splits:
  - name: train
    num_bytes: 3583916
    num_examples: 5000
  download_size: 1723209
  dataset_size: 3583916
configs:
- config_name: instruction
  data_files:
  - split: train
    path: instruction/train-*
- config_name: knowledge
  data_files:
  - split: train
    path: knowledge/train-*
- config_name: math
  data_files:
  - split: train
    path: math/train-*
- config_name: npc
  data_files:
  - split: train
    path: npc/train-*
- config_name: persona
  data_files:
  - split: train
    path: persona/train-*
- config_name: reasoning
  data_files:
  - split: train
    path: reasoning/train-*
- config_name: tool
  data_files:
  - split: train
    path: tool/train-*
---

Translated [proj-persona/PersonaHub](https://huggingface.co/datasets/proj-persona/PersonaHub) using [nayohan/llama3-instrucTrans-enko-8b](https://huggingface.co/nayohan/llama3-instrucTrans-enko-8b).

For this dataset, we only used data that is 5000 characters or less in length and has language of English.

Thanks for @proj-persona and @nayohan.

-------------------------------

# Scaling Synthetic Data Creation with 1,000,000,000 Personas
This repo releases data introduced in our paper [Scaling Synthetic Data Creation with 1,000,000,000 Personas](https://arxiv.org/pdf/2406.20094):

We propose a novel persona-driven data synthesis methodology that leverages various perspectives within a large language model (LLM) to create diverse synthetic data. To fully exploit this methodology at scale, we introduce **PERSONA HUB** – a collection of **1 billion diverse personas** automatically curated from web data. These 1 billion personas (~13% of the world's total population), acting as distributed carriers of world knowledge, can tap into almost every perspective encapsulated within the LLM, thereby facilitating the creation of diverse synthetic data at scale for various scenarios. By showcasing PERSONA HUB’s use cases in synthesizing high-quality **mathematical and logical reasoning** problems, **instructions** (i.e., user prompts), **knowledge-rich texts**, **game NPCs** and **tools** (functions) at scale, we demonstrate persona-driven data synthesis is versatile, scalable, flexible, and easy to use, potentially driving a paradigm shift in synthetic data creation and applications in practice, which may have a profound impact on LLM research and development.

<div align="center">
<img src="./assets/persona_overview.png" width="90%">
</div>


## Data Release
### Synthetic Data Samples
To facilitate research in persona-driven data synthesis, we are initially releasing following synthetic data samples we created with various personas, including:
* **50,000 math problems**
* **50,000 logical reasoning problems**
* **50,000 instructions**
* **10,000 knowledge-rich texts**
* **10,000 game NPCs**
* **5,000 tools (functions)**

### Persona Hub
We also release a subset of our PERSONA HUB, including:
* **200,000 personas**

## Run Demo
One can try the demo to synthesize data with PERSONA HUB simply by running code in https://github.com/tencent-ailab/persona-hub:

```bash
# ensure that you have installed datasets and openai (pip install datasets openai) and configured the openai_api_key before running
bash demo_openai_synthesize.sh # using gpt4o to synthesize data with PERSONA HUB
```

or

```bash
# ensure that you have installed datasets, transformers and vllm (pip install datasets transformers vllm) before running
bash demo_vllm_synthesize.sh # using open-sourced models to synthesize data with PERSONA HUB
```

Note that the data synthesis prompt templates we provide are for reference only. You can customize your desired prompts in `code/prompt_templates.py`.

## Argilla
You can also access this dataset in [Argilla space](https://argilla-data-explorers.hf.space/), as introduced in the following video:
* Video: https://youtu.be/timmCn8Nr6g?feature=shared

## Contact
* Please email `xinchan@global.tencent.com`  or  `dyu@global.tencent.com`
* Github page: https://github.com/tencent-ailab/persona-hub

## Disclaimer
PERSONA HUB can facilitate synthetic data creation at a billion-scale to simulate diverse inputs (i.e., use cases) from a wide variety of real-world users. If this data is used as input to query a target LLM to obtain its outputs at scale, there is a high risk that the LLM's knowledge, intelligence and capabilities will be dumped and easily replicated, thereby challenging the leading position of the most powerful LLMs. It is crucial to avoid misuse and ensure ethical and responsible application to prevent privacy violations and other ethical concerns.

The released data is all generated by public available models (GPT-4, Llama-3 and Qwen), and is intended for research purposes only. Users also must comply with the respective license agreements and usage policies of these models when using the synthesized data. The data may contain inaccuracies, unsafe content, or biases, for which we cannot be held responsible. Please evaluate its accuracy and suitability before use. Tencent and its licensors provide the data AS-IS, without warranty of any kind, express or implied. The views and opinions expressed in the data do not necessarily reflect those of Tencent.