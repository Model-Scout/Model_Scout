---
language:
- es
- de
- en
- ru
- zh
- ca
- uk
- th
- pt
- fr
- ja
- it
- pl
- oc
- vi
- eo
- ko
- hu
- eu
- he
- ckb
- tr
- fi
- ar
- da
- sr
- cs
- nl
- ms
- el
- is
- la
- fa
- id
- yue
- ceb
- ta
- sv
- bg
- lv
- es
- en
- zh
- de
- ja
- ru
- pt
- fr
- ca
- it
- eo
configs:
  - config_name: all
    data_files:
      - split: train
        path: train.jsonl.zst
      - split: validation
        path: validation.jsonl.zst
  - config_name: ar
    data_files:
      - split: train
        path: ar_train.jsonl.zst
  - config_name: bg
    data_files:
      - split: train
        path: bg_train.jsonl.zst
  - config_name: ca
    data_files:
      - split: train
        path: ca_train.jsonl.zst
      - split: validation
        path: ca_validation.jsonl.zst
  - config_name: ceb
    data_files:
      - split: train
        path: ceb_train.jsonl.zst
  - config_name: ckb
    data_files:
      - split: train
        path: ckb_train.jsonl.zst
  - config_name: cs
    data_files:
      - split: train
        path: cs_train.jsonl.zst
  - config_name: da
    data_files:
      - split: train
        path: da_train.jsonl.zst
  - config_name: de
    data_files:
      - split: train
        path: de_train.jsonl.zst
      - split: validation
        path: de_validation.jsonl.zst
  - config_name: el
    data_files:
      - split: train
        path: el_train.jsonl.zst
  - config_name: en
    data_files:
      - split: train
        path: en_train.jsonl.zst
      - split: validation
        path: en_validation.jsonl.zst
  - config_name: eo
    data_files:
      - split: train
        path: eo_train.jsonl.zst
      - split: validation
        path: eo_validation.jsonl.zst
  - config_name: es
    data_files:
      - split: train
        path: es_train.jsonl.zst
      - split: validation
        path: es_validation.jsonl.zst
  - config_name: eu
    data_files:
      - split: train
        path: eu_train.jsonl.zst
  - config_name: fa
    data_files:
      - split: train
        path: fa_train.jsonl.zst
  - config_name: fi
    data_files:
      - split: train
        path: fi_train.jsonl.zst
  - config_name: fr
    data_files:
      - split: train
        path: fr_train.jsonl.zst
      - split: validation
        path: fr_validation.jsonl.zst
  - config_name: he
    data_files:
      - split: train
        path: he_train.jsonl.zst
  - config_name: hu
    data_files:
      - split: train
        path: hu_train.jsonl.zst
  - config_name: id
    data_files:
      - split: train
        path: id_train.jsonl.zst
  - config_name: is
    data_files:
      - split: train
        path: is_train.jsonl.zst
  - config_name: it
    data_files:
      - split: train
        path: it_train.jsonl.zst
      - split: validation
        path: it_validation.jsonl.zst
  - config_name: ja
    data_files:
      - split: train
        path: ja_train.jsonl.zst
      - split: validation
        path: ja_validation.jsonl.zst
  - config_name: ko
    data_files:
      - split: train
        path: ko_train.jsonl.zst
  - config_name: la
    data_files:
      - split: train
        path: la_train.jsonl.zst
  - config_name: lv
    data_files:
      - split: train
        path: lv_train.jsonl.zst
  - config_name: ms
    data_files:
      - split: train
        path: ms_train.jsonl.zst
  - config_name: nl
    data_files:
      - split: train
        path: nl_train.jsonl.zst
  - config_name: oc
    data_files:
      - split: train
        path: oc_train.jsonl.zst
  - config_name: pl
    data_files:
      - split: train
        path: pl_train.jsonl.zst
  - config_name: pt
    data_files:
      - split: train
        path: pt_train.jsonl.zst
      - split: validation
        path: pt_validation.jsonl.zst
  - config_name: ru
    data_files:
      - split: train
        path: ru_train.jsonl.zst
      - split: validation
        path: ru_validation.jsonl.zst
  - config_name: sr
    data_files:
      - split: train
        path: sr_train.jsonl.zst
  - config_name: sv
    data_files:
      - split: train
        path: sv_train.jsonl.zst
  - config_name: ta
    data_files:
      - split: train
        path: ta_train.jsonl.zst
  - config_name: th
    data_files:
      - split: train
        path: th_train.jsonl.zst
  - config_name: tr
    data_files:
      - split: train
        path: tr_train.jsonl.zst
  - config_name: uk
    data_files:
      - split: train
        path: uk_train.jsonl.zst
  - config_name: vi
    data_files:
      - split: train
        path: vi_train.jsonl.zst
  - config_name: yue
    data_files:
      - split: train
        path: yue_train.jsonl.zst
  - config_name: zh
    data_files:
      - split: train
        path: zh_train.jsonl.zst
      - split: validation
        path: zh_validation.jsonl.zst
license: apache-2.0
---
# OpenAssistant/oasst1 and oasst2

The **OpenAssistant Conversations (OASST)** datasets are collections of human-generated and human-annotated assistant-style conversations. They were created through a global crowdsourcing effort with contributions from more than **13&thinsp;500 volunteers**.

This unofficial dataset includes all conversation chains from [OpenAssistant/oasst1](https://huggingface.co/datasets/OpenAssistant/oasst1) and [OpenAssistant/oasst2](https://huggingface.co/datasets/OpenAssistant/oasst2), regardless of quality or annotation score.

- The **`all`** configuration includes every conversation chain, keeping the original *train* and *validation* splits.  
- All other configurations are language-specific subsets, identified using the *fastText* language detection tool. Duplicate and out-of-order conversations have been removed.

## Limitations
- Some metadata from the original datasets is not included.
- Uneven distribution of languages.  
- Many conversations contain limited content (for example, small talk or brief exchanges).  
- Some human participants responded as if they were chatbots.  
- Certain answers are incomplete or less detailed than typical assistant responses.

## Related Datasets

Real human-assistant conversations:
- [HuggingFaceH4/no_robots](https://huggingface.co/datasets/HuggingFaceH4/no_robots)

Real conversations with ChatGPT:
- [allenai/WildChat-1M](https://huggingface.co/datasets/allenai/WildChat-1M)
- [allenai/WildChat-4.8M](https://huggingface.co/datasets/allenai/WildChat-4.8M)
- [DSULT-Core/ShareGPT-X](https://huggingface.co/datasets/DSULT-Core/ShareGPT-X)
- Which are collected here: [agentlans/allenai-WildChat](https://huggingface.co/datasets/agentlans/allenai-WildChat) and [agentlans/DSULT-Core-ShareGPT-X](https://huggingface.co/datasets/agentlans/DSULT-Core-ShareGPT-X)
