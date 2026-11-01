---
dataset_info:
- config_name: harmbench
  features:
  - name: id
    dtype: string
  - name: group_id
    dtype: string
  - name: language
    dtype: string
  - name: category
    dtype: string
  - name: text
    dtype: string
  - name: template
    dtype: string
  - name: behavior
    dtype: string
  - name: hb_id
    dtype: int64
  - name: hb_category
    dtype: string
  - name: branch
    dtype: string
  - name: paraphrase_index
    dtype: int64
  - name: variant_index
    dtype: int64
  - name: sample_index
    dtype: int64
  - name: context_source
    dtype: string
  - name: benign_class
    dtype: string
  - name: recipe
    dtype: string
  - name: prefixes
    list: string
  - name: suffixes
    list: string
  - name: source
    dtype: string
  - name: class_type
    dtype: string
  splits:
  - name: test
    num_bytes: 252239444
    num_examples: 251886
  download_size: 72172653
  dataset_size: 252239444
- config_name: wildguard
  features:
  - name: id
    dtype: string
  - name: group_id
    dtype: string
  - name: original_id
    dtype: string
  - name: original_index
    dtype: int64
  - name: split
    dtype: string
  - name: language
    dtype: string
  - name: category
    dtype: string
  - name: text
    dtype: string
  - name: template
    dtype: string
  - name: original_prompt
    dtype: string
  - name: branch
    dtype: string
  - name: paraphrase_index
    dtype: int64
  - name: variant_index
    dtype: int64
  - name: wg_subcategory
    dtype: string
  - name: wg_harm_label
    dtype: string
  - name: wg_adversarial
    dtype: bool
  - name: ls_primary
    dtype: string
  - name: ls_high_level
    dtype: string
  - name: ls_labels
    list: string
  - name: ls_non_consensual_sexual
    dtype: bool
  - name: context_source
    dtype: string
  - name: benign_class
    dtype: string
  - name: recipe
    dtype: string
  - name: prefixes
    list: string
  - name: suffixes
    list: string
  - name: source
    dtype: string
  - name: class_type
    dtype: string
  splits:
  - name: train
    num_bytes: 8878301565
    num_examples: 1551799
  - name: test
    num_bytes: 2141023027
    num_examples: 368820
  download_size: 1315135804
  dataset_size: 11019324592
configs:
- config_name: harmbench
  data_files:
  - split: test
    path: harmbench/test-*
- config_name: wildguard
  data_files:
  - split: train
    path: wildguard/train-*
  - split: test
    path: wildguard/test-*
- config_name: sft
  data_files:
  - split: train
    path: sft/train-*
- config_name: dpo
  data_files:
  - split: Apertus_8B_2509_SafetyOnly_r15so
    path: dpo/Apertus_8B_2509_SafetyOnly_r15so-*
  - split: Apertus_8B_2509_Safety_SFT_r15
    path: dpo/Apertus_8B_2509_Safety_SFT_r15-*
  - split: Apertus_8B_Instruct_2509_Safety_SFT_r15
    path: dpo/Apertus_8B_Instruct_2509_Safety_SFT_r15-*
  - split: Apertus_8B_Instruct_2509_sft
    path: dpo/Apertus_8B_Instruct_2509_sft-*
  - split: Apertus_8B_Instruct_2509_sft_Safety_SFT_r15
    path: dpo/Apertus_8B_Instruct_2509_sft_Safety_SFT_r15-*
  - split: Apertus_v1.5_8B_SFT
    path: dpo/Apertus_v1.5_8B_SFT-*
  - split: Apertus_v1.5_8B_SFT_Safety_SFT_r15
    path: dpo/Apertus_v1.5_8B_SFT_Safety_SFT_r15-*
  - split: Apertus_v1.5_8B_Safety_SFT_r15
    path: dpo/Apertus_v1.5_8B_Safety_SFT_r15-*
  - split: Apertus_v1.5_8B_base_SafetyOnly_r15so
    path: dpo/Apertus_v1.5_8B_base_SafetyOnly_r15so-*
  - split: Apertus_v1.5_8B_base_Safety_SFT_r15
    path: dpo/Apertus_v1.5_8B_base_Safety_SFT_r15-*
  - split: Llama_3.1_8B_Instruct_SafetyTRL_r15
    path: dpo/Llama_3.1_8B_Instruct_SafetyTRL_r15-*
  - split: Llama_3.1_8B_SafetyOnly_r15so
    path: dpo/Llama_3.1_8B_SafetyOnly_r15so-*
  - split: Llama_3.1_8B_SafetyTRL_r15
    path: dpo/Llama_3.1_8B_SafetyTRL_r15-*
  - split: Meta_Llama_3_8B_Instruct_SafetyTRL_r15
    path: dpo/Meta_Llama_3_8B_Instruct_SafetyTRL_r15-*
  - split: Meta_Llama_3_8B_SafetyTRL_r15
    path: dpo/Meta_Llama_3_8B_SafetyTRL_r15-*
  - split: Mistral_7B_Instruct_v0.2_SafetyTRL_r15
    path: dpo/Mistral_7B_Instruct_v0.2_SafetyTRL_r15-*
  - split: Olmo_3_1025_7B_SafetyOnly_r15so
    path: dpo/Olmo_3_1025_7B_SafetyOnly_r15so-*
  - split: Olmo_3_1025_7B_SafetyTRL_r15
    path: dpo/Olmo_3_1025_7B_SafetyTRL_r15-*
  - split: Olmo_3_7B_Instruct_SFT_SafetyTRL_r15
    path: dpo/Olmo_3_7B_Instruct_SFT_SafetyTRL_r15-*
  - split: Olmo_3_7B_Instruct_SafetyTRL_r15
    path: dpo/Olmo_3_7B_Instruct_SafetyTRL_r15-*
  - split: Qwen3.5_9B_Base_SafetyOnly_r15so
    path: dpo/Qwen3.5_9B_Base_SafetyOnly_r15so-*
  - split: Qwen3.5_9B_Base_SafetyTRL_r15
    path: dpo/Qwen3.5_9B_Base_SafetyTRL_r15-*
  - split: Qwen3.5_9B_SafetyTRL_r15
    path: dpo/Qwen3.5_9B_SafetyTRL_r15-*
  - split: Qwen3_8B_Base_SafetyTRL_r15
    path: dpo/Qwen3_8B_Base_SafetyTRL_r15-*
  - split: Qwen3_8B_SafetyTRL_r15
    path: dpo/Qwen3_8B_SafetyTRL_r15-*
tags:
- not-for-all-audiences
- safety
- multilingual
- alignment
license: apache-2.0
pretty_name: MSafeTemp
size_categories:
- 1M<n<10M
language:
- en
- sq
- am
- ar
- hy
- eu
- be
- bn
- bs
- bg
- ca
- zh
- hr
- cs
- da
- nl
- et
- fi
- fr
- gl
- ka
- de
- el
- ha
- hi
- hu
- is
- id
- ga
- it
- ja
- ko
- lv
- lt
- lb
- mk
- mt
- ne
- 'no'
- fa
- pl
- pt
- ro
- ru
- sr
- sk
- sl
- es
- sw
- sv
- gsw
- tl
- th
- tr
- uk
- ur
- vi
- cy
- yo
- zu
multilinguality: multilingual
---
# MSafeTemp: Template-based Multilingual Safety Data

[![arXiv](https://img.shields.io/badge/arXiv-2610.40516-b31b1b)](https://arxiv.org/abs/2610.40516)
[![Paper](https://img.shields.io/badge/Paper-HuggingFace-yellow)](https://huggingface.co/papers/2610.40516)
[![Code](https://img.shields.io/badge/Code-GitHub-black)](https://github.com/swiss-ai/msafetemp)

**Content warning:** this dataset contains harmful prompts, including jailbreak-wrapped prompts, in 60 languages.

MSafeTemp is the dataset of *"How I Aligned Your Model: Scaling Up Multilingual Safety Training with Templates"* by [Max Neuwinger](https://www.maxneuwinger.com/), [Hanna Yukhymenko](https://www.ayukh.com/) and [Imanol Schlag](https://ischlag.github.io/).

English harmful seed prompts are turned into safe templates with typed slots, the templates are translated, and the slots are filled again in every language. Each template yields three kinds of prompts:

* **TR** (`category = harmful`): translated harmful variants, filled with harmful entities.
* **PH** (`category = posthoc`): culturally localized harmful variants, filled with local groups, institutions, events and concepts from a per-language cultural card.
* **OR** (`category = benign`): benign minimal pairs that keep the wording but use a safe fill, for measuring over-refusal.

Every generation step is checked by an LLM judge, and only judge-approved prompts are kept. The pipeline, training and evaluation code are in the [GitHub repository](https://github.com/swiss-ai/msafetemp).

## Configurations

| Config | Seeds | Split | Rows | Languages | Use |
|---|---|---|---|---|---|
| `wildguard` | WildGuardMix, 2,000 source prompts | `train` | 1,551,799 | 44 | safety training |
| `wildguard` | WildGuardMix, 500 source prompts | `test` | 368,820 | 44 | evaluation |
| `harmbench` | HarmBench, 200 behaviors | `test` | 251,886 | 60 | evaluation |

Train and test are split by source seed, so no descendant of a test seed appears in `train`.

```python
from datasets import load_dataset

train = load_dataset("swiss-ai/MSafeTemp", "wildguard", split="train")
hb = load_dataset("swiss-ai/MSafeTemp", "harmbench", split="test")
```

## Fields

| Field | Description |
|---|---|
| `id`, `group_id` | row id; rows derived from the same seed and language share a `group_id` |
| `language` | language name, e.g. `german`, `swiss_german`, `yoruba` |
| `text` | the prompt |
| `template` | the template with typed slots the prompt was filled from |
| `category` | `harmful` (TR), `posthoc` (PH) or `benign` (OR) |
| `class_type` | `harmful` or `benign` |
| `branch` | `main` (main template), `paraphrase` (paraphrased template), `contextual` (localized rephrasing around a local entity), `pyrit_wrapped` (jailbreak-wrapped prompt) |
| `paraphrase_index`, `variant_index` | template paraphrase and fill variant |
| `benign_class` | type of benign pair, e.g. `direct`, `bounded` |
| `recipe` | slot fills of localized (PH) variants, as JSON |
| `prefixes`, `suffixes` | attack affixes added to the prompt |
| `source` | seed dataset (`wildguard` or `harmbench`) |
| `original_prompt`, `original_id`, `original_index` | WildGuardMix seed (`wildguard` only) |
| `wg_subcategory`, `wg_harm_label`, `wg_adversarial` | WildGuardMix labels of the seed (`wildguard` only) |
| `ls_primary`, `ls_high_level`, `ls_labels`, `ls_non_consensual_sexual` | LinguaSafe taxonomy labels of the seed (`wildguard` only) |
| `behavior`, `hb_id`, `hb_category` | HarmBench behavior of the seed (`harmbench` only) |

## Intended use

MSafeTemp is released to train and evaluate safer multilingual models: refusal training on harmful prompts, over-refusal control on benign pairs, and evaluation of attack success across languages and cultures. Do not use it to build systems that produce harmful content.

## License

Released under the Apache 2.0 license. The seed prompts come from [WildGuardMix](https://huggingface.co/datasets/allenai/wildguardmix) and [HarmBench](https://github.com/centerforaisafety/HarmBench); please also follow their terms.

## Citation

```bibtex
@misc{neuwinger2026ialignedmodelscaling,
      title={How I Aligned Your Model: Scaling Up Multilingual Safety Training with Templates}, 
      author={Max Neuwinger and Hanna Yukhymenko and Imanol Schlag},
      year={2026},
      eprint={2610.40516},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2610.40516}, 
}
```
