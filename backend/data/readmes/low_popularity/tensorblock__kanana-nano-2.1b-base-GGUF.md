---
language:
- en
- ko
library_name: transformers
license: cc-by-nc-4.0
pipeline_tag: text-generation
model_id: kakaocorp/kanana-nano-2.1b-base
repo: kakaocorp/kanana-nano-2.1b-base
developers: Kanana LLM
training_regime: bf16 mixed precision
tags:
- TensorBlock
- GGUF
base_model: kakaocorp/kanana-nano-2.1b-base
model-index:
- name: kanana-nano-2.1b-base
  results:
  - task:
      type: multiple_choice
      name: mmlu
    dataset:
      name: mmlu (5-shots)
      type: hails/mmlu_no_train
    metrics:
    - type: acc
      value: 54.83
      name: acc
  - task:
      type: generate_until
      name: kmmlu
    dataset:
      name: kmmlu-direct (5-shots)
      type: HAERAE-HUB/KMMLU
    metrics:
    - type: exact_match
      value: 44.83
      name: exact_match
  - task:
      type: multiple_choice
      name: haerae
    dataset:
      name: haerae (5-shots)
      type: HAERAE-HUB/HAE_RAE_BENCH
    metrics:
    - type: acc_norm
      value: 77.09
      name: acc_norm
  - task:
      type: generate_until
      name: gsm8k
    dataset:
      name: gsm8k (5-shots)
      type: openai/gsm8k
    metrics:
    - type: exact_match
      value: 46.32
      name: exact_match_strict
  - task:
      type: generate_until
      name: humaneval
    dataset:
      name: humaneval (0-shots)
      type: openai/openai_humaneval
    metrics:
    - type: pass@1
      value: 31.1
      name: pass@1
  - task:
      type: generate_until
      name: mbpp
    dataset:
      name: mbpp (3-shots)
      type: google-research-datasets/mbpp
    metrics:
    - type: pass@1
      value: 46.2
      name: pass@1
---

<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="https://i.imgur.com/jC7kdl8.jpeg" alt="TensorBlock" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>

[![Website](https://img.shields.io/badge/Website-tensorblock.co-blue?logo=google-chrome&logoColor=white)](https://tensorblock.co)
[![Twitter](https://img.shields.io/twitter/follow/tensorblock_aoi?style=social)](https://twitter.com/tensorblock_aoi)
[![Discord](https://img.shields.io/badge/Discord-Join%20Us-5865F2?logo=discord&logoColor=white)](https://discord.gg/Ej5NmeHFf2)
[![GitHub](https://img.shields.io/badge/GitHub-TensorBlock-black?logo=github&logoColor=white)](https://github.com/TensorBlock)
[![Telegram](https://img.shields.io/badge/Telegram-Group-blue?logo=telegram)](https://t.me/TensorBlock)


## kakaocorp/kanana-nano-2.1b-base - GGUF

This repo contains GGUF format model files for [kakaocorp/kanana-nano-2.1b-base](https://huggingface.co/kakaocorp/kanana-nano-2.1b-base).

The files were quantized using machines provided by [TensorBlock](https://tensorblock.co/), and they are compatible with llama.cpp as of [commit b4823](https://github.com/ggml-org/llama.cpp/commit/5bbe6a9fe9a8796a9389c85accec89dbc4d91e39).

## Our projects
<table border="1" cellspacing="0" cellpadding="10">
  <tr>
    <th colspan="2" style="font-size: 25px;">Forge</th>
  </tr>
  <tr>
    <th colspan="2">
      <img src="https://imgur.com/faI5UKh.jpeg" alt="Forge Project" width="900"/>
    </th>
  </tr>
  <tr>
    <th colspan="2">An OpenAI-compatible multi-provider routing layer.</th>
  </tr>
  <tr>
    <th colspan="2">
      <a href="https://github.com/TensorBlock/forge" target="_blank" style="
        display: inline-block;
        padding: 8px 16px;
        background-color: #FF7F50;
        color: white;
        text-decoration: none;
        border-radius: 6px;
        font-weight: bold;
        font-family: sans-serif;
      ">🚀 Try it now! 🚀</a>
    </th>
  </tr>

  <tr>
    <th style="font-size: 25px;">Awesome MCP Servers</th>
    <th style="font-size: 25px;">TensorBlock Studio</th>
  </tr>
  <tr>
    <th><img src="https://imgur.com/2Xov7B7.jpeg" alt="MCP Servers" width="450"/></th>
    <th><img src="https://imgur.com/pJcmF5u.jpeg" alt="Studio" width="450"/></th>
  </tr>
  <tr>
    <th>A comprehensive collection of Model Context Protocol (MCP) servers.</th>
    <th>A lightweight, open, and extensible multi-LLM interaction studio.</th>
  </tr>
  <tr>
    <th>
      <a href="https://github.com/TensorBlock/awesome-mcp-servers" target="_blank" style="
        display: inline-block;
        padding: 8px 16px;
        background-color: #FF7F50;
        color: white;
        text-decoration: none;
        border-radius: 6px;
        font-weight: bold;
        font-family: sans-serif;
      ">👀 See what we built 👀</a>
    </th>
    <th>
      <a href="https://github.com/TensorBlock/TensorBlock-Studio" target="_blank" style="
        display: inline-block;
        padding: 8px 16px;
        background-color: #FF7F50;
        color: white;
        text-decoration: none;
        border-radius: 6px;
        font-weight: bold;
        font-family: sans-serif;
      ">👀 See what we built 👀</a>
    </th>
  </tr>
</table>
## Prompt template

```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>

{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
```

## Model file specification

| Filename | Quant type | File Size | Description |
| -------- | ---------- | --------- | ----------- |
| [kanana-nano-2.1b-base-Q2_K.gguf](https://huggingface.co/tensorblock/kanana-nano-2.1b-base-GGUF/blob/main/kanana-nano-2.1b-base-Q2_K.gguf) | Q2_K | 0.938 GB | smallest, significant quality loss - not recommended for most purposes |
| [kanana-nano-2.1b-base-Q3_K_S.gguf](https://huggingface.co/tensorblock/kanana-nano-2.1b-base-GGUF/blob/main/kanana-nano-2.1b-base-Q3_K_S.gguf) | Q3_K_S | 1.056 GB | very small, high quality loss |
| [kanana-nano-2.1b-base-Q3_K_M.gguf](https://huggingface.co/tensorblock/kanana-nano-2.1b-base-GGUF/blob/main/kanana-nano-2.1b-base-Q3_K_M.gguf) | Q3_K_M | 1.147 GB | very small, high quality loss |
| [kanana-nano-2.1b-base-Q3_K_L.gguf](https://huggingface.co/tensorblock/kanana-nano-2.1b-base-GGUF/blob/main/kanana-nano-2.1b-base-Q3_K_L.gguf) | Q3_K_L | 1.203 GB | small, substantial quality loss |
| [kanana-nano-2.1b-base-Q4_0.gguf](https://huggingface.co/tensorblock/kanana-nano-2.1b-base-GGUF/blob/main/kanana-nano-2.1b-base-Q4_0.gguf) | Q4_0 | 1.241 GB | legacy; small, very high quality loss - prefer using Q3_K_M |
| [kanana-nano-2.1b-base-Q4_K_S.gguf](https://huggingface.co/tensorblock/kanana-nano-2.1b-base-GGUF/blob/main/kanana-nano-2.1b-base-Q4_K_S.gguf) | Q4_K_S | 1.304 GB | small, greater quality loss |
| [kanana-nano-2.1b-base-Q4_K_M.gguf](https://huggingface.co/tensorblock/kanana-nano-2.1b-base-GGUF/blob/main/kanana-nano-2.1b-base-Q4_K_M.gguf) | Q4_K_M | 1.393 GB | medium, balanced quality - recommended |
| [kanana-nano-2.1b-base-Q5_0.gguf](https://huggingface.co/tensorblock/kanana-nano-2.1b-base-GGUF/blob/main/kanana-nano-2.1b-base-Q5_0.gguf) | Q5_0 | 1.474 GB | legacy; medium, balanced quality - prefer using Q4_K_M |
| [kanana-nano-2.1b-base-Q5_K_S.gguf](https://huggingface.co/tensorblock/kanana-nano-2.1b-base-GGUF/blob/main/kanana-nano-2.1b-base-Q5_K_S.gguf) | Q5_K_S | 1.502 GB | large, low quality loss - recommended |
| [kanana-nano-2.1b-base-Q5_K_M.gguf](https://huggingface.co/tensorblock/kanana-nano-2.1b-base-GGUF/blob/main/kanana-nano-2.1b-base-Q5_K_M.gguf) | Q5_K_M | 1.579 GB | large, very low quality loss - recommended |
| [kanana-nano-2.1b-base-Q6_K.gguf](https://huggingface.co/tensorblock/kanana-nano-2.1b-base-GGUF/blob/main/kanana-nano-2.1b-base-Q6_K.gguf) | Q6_K | 1.832 GB | very large, extremely low quality loss |
| [kanana-nano-2.1b-base-Q8_0.gguf](https://huggingface.co/tensorblock/kanana-nano-2.1b-base-GGUF/blob/main/kanana-nano-2.1b-base-Q8_0.gguf) | Q8_0 | 2.226 GB | very large, extremely low quality loss - not recommended |


## Downloading instruction

### Command line

Firstly, install Huggingface Client

```shell
pip install -U "huggingface_hub[cli]"
```

Then, downoad the individual model file the a local directory

```shell
huggingface-cli download tensorblock/kanana-nano-2.1b-base-GGUF --include "kanana-nano-2.1b-base-Q2_K.gguf" --local-dir MY_LOCAL_DIR
```

If you wanna download multiple model files with a pattern (e.g., `*Q4_K*gguf`), you can try:

```shell
huggingface-cli download tensorblock/kanana-nano-2.1b-base-GGUF --local-dir MY_LOCAL_DIR --local-dir-use-symlinks False --include='*Q4_K*gguf'
```
