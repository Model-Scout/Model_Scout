---
configs:
- config_name: classification
  data_files:
  - path:
    - train.jsonl.zst
    split: train
  - path:
    - test.jsonl.zst
    split: test
- config_name: customized_prompts
  data_files:
  - path:
    - customized_prompts.jsonl.zst
    split: train
license: cc-by-4.0
task_categories:
- text-classification
tags:
- pii
- privacy
- prompts
- wildchat
language:
- multilingual
- af
- ar
- az
- be
- bg
- bn
- ca
- cs
- da
- de
- el
- en
- es
- et
- fa
- fi
- fr
- gl
- gu
- he
- hi
- hr
- hu
- hy
- id
- it
- ja
- jv
- ka
- kk
- kn
- ko
- lt
- lv
- mr
- ms
- ne
- nl
- no
- pl
- pt
- ro
- ru
- sh
- sk
- sl
- sr
- su
- sv
- ta
- th
- tl
- tr
- uk
- ur
- uz
- vi
- zh
---
# Personal Information Prompts

This dataset contains multilingual prompts derived from the `all_sample` subset of the [agentlans/allenai-WildChat-4.8M](https://huggingface.co/datasets/agentlans/allenai-WildChat-4.8M) dataset. Each prompt features artificially inserted personally identifiable information (PII) generated randomly with the [Faker](https://faker.readthedocs.io/en/master/) Python package for various locales.

Each rewritten prompt uses the [google/gemma-3-12b-it](https://huggingface.co/google/gemma-3-12b-it) model to incorporate the synthetic personal data.

Dataset fields for the two configurations: 

### `classification` configuration

This config was created from the `customized_prompts` config and then split into 80% training and 20% testing data.

- `prompt`: a prompt which may or may not contain PII
- `language`: the detected language of the prompt
- `contains_pii`: whether PII was used in constructing the prompt

### `customized_prompts` configuration

- `prompt`: prompt text including artificial personal data
- `pii`: dictionary containing the PII used for generation
- `base_prompt`: original prompt from the WildChat dataset
- `pii_locale`: locale used to generate the PII
- `prompt_language`: language of the rewritten prompt, determined with FastText

## Limitations

- All information randomly generated except for the base prompts. Any resemblance to actual events or locales or persons, living or dead, is entirely coincidental.
- This dataset is not suitable for extracting PII because parts of the PII get embedded into foreign language texts in unusual ways.
- Not all the PII gets incorporated into the prompt.

## Licence

Creative Commons Attribution 4.0