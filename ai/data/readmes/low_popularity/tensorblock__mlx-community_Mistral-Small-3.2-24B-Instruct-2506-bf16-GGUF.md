---
language:
- en
- fr
- de
- es
- pt
- it
- ja
- ko
- ru
- zh
- ar
- fa
- id
- ms
- ne
- pl
- ro
- sr
- sv
- tr
- uk
- vi
- hi
- bn
license: apache-2.0
library_name: mlx
inference: false
base_model: mlx-community/Mistral-Small-3.2-24B-Instruct-2506-bf16
extra_gated_description: If you want to learn more about how we process your personal
  data, please read our <a href="https://mistral.ai/terms/">Privacy Policy</a>.
pipeline_tag: text-generation
tags:
- mlx
- TensorBlock
- GGUF
---

<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="https://i.imgur.com/jC7kdl8.jpeg" alt="TensorBlock" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>

[![Website](https://img.shields.io/badge/Website-tensorblock.co-blue?logo=google-chrome&logoColor=white)](https://tensorblock.co)
[![Twitter](https://img.shields.io/twitter/follow/tensorblock_aoi?style=social)](https://twitter.com/tensorblock_aoi)
[![Discord](https://img.shields.io/badge/Discord-Join%20Us-5865F2?logo=discord&logoColor=white)](https://discord.gg/Ej5NmeHFf2)
[![GitHub](https://img.shields.io/badge/GitHub-TensorBlock-black?logo=github&logoColor=white)](https://github.com/TensorBlock)
[![Telegram](https://img.shields.io/badge/Telegram-Group-blue?logo=telegram)](https://t.me/TensorBlock)


## mlx-community/Mistral-Small-3.2-24B-Instruct-2506-bf16 - GGUF

<div style="text-align: left; margin: 20px 0;">
    <a href="https://discord.com/invite/Ej5NmeHFf2" style="display: inline-block; padding: 10px 20px; background-color: #5865F2; color: white; text-decoration: none; border-radius: 5px; font-weight: bold;">
        Join our Discord to learn more about what we're building ↗
    </a>
</div>

This repo contains GGUF format model files for [mlx-community/Mistral-Small-3.2-24B-Instruct-2506-bf16](https://huggingface.co/mlx-community/Mistral-Small-3.2-24B-Instruct-2506-bf16).

The files were quantized using machines provided by [TensorBlock](https://tensorblock.co/), and they are compatible with llama.cpp as of [commit b5753](https://github.com/ggml-org/llama.cpp/commit/73e53dc834c0a2336cd104473af6897197b96277).

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
<s>[SYSTEM_PROMPT]{system_prompt}[/SYSTEM_PROMPT][INST]{prompt}[/INST]
```

## Model file specification

| Filename | Quant type | File Size | Description |
| -------- | ---------- | --------- | ----------- |
| [Mistral-Small-3.2-24B-Instruct-2506-bf16-Q2_K.gguf](https://huggingface.co/tensorblock/mlx-community_Mistral-Small-3.2-24B-Instruct-2506-bf16-GGUF/blob/main/Mistral-Small-3.2-24B-Instruct-2506-bf16-Q2_K.gguf) | Q2_K | 8.890 GB | smallest, significant quality loss - not recommended for most purposes |
| [Mistral-Small-3.2-24B-Instruct-2506-bf16-Q3_K_S.gguf](https://huggingface.co/tensorblock/mlx-community_Mistral-Small-3.2-24B-Instruct-2506-bf16-GGUF/blob/main/Mistral-Small-3.2-24B-Instruct-2506-bf16-Q3_K_S.gguf) | Q3_K_S | 10.400 GB | very small, high quality loss |
| [Mistral-Small-3.2-24B-Instruct-2506-bf16-Q3_K_M.gguf](https://huggingface.co/tensorblock/mlx-community_Mistral-Small-3.2-24B-Instruct-2506-bf16-GGUF/blob/main/Mistral-Small-3.2-24B-Instruct-2506-bf16-Q3_K_M.gguf) | Q3_K_M | 11.474 GB | very small, high quality loss |
| [Mistral-Small-3.2-24B-Instruct-2506-bf16-Q3_K_L.gguf](https://huggingface.co/tensorblock/mlx-community_Mistral-Small-3.2-24B-Instruct-2506-bf16-GGUF/blob/main/Mistral-Small-3.2-24B-Instruct-2506-bf16-Q3_K_L.gguf) | Q3_K_L | 12.401 GB | small, substantial quality loss |
| [Mistral-Small-3.2-24B-Instruct-2506-bf16-Q4_0.gguf](https://huggingface.co/tensorblock/mlx-community_Mistral-Small-3.2-24B-Instruct-2506-bf16-GGUF/blob/main/Mistral-Small-3.2-24B-Instruct-2506-bf16-Q4_0.gguf) | Q4_0 | 13.442 GB | legacy; small, very high quality loss - prefer using Q3_K_M |
| [Mistral-Small-3.2-24B-Instruct-2506-bf16-Q4_K_S.gguf](https://huggingface.co/tensorblock/mlx-community_Mistral-Small-3.2-24B-Instruct-2506-bf16-GGUF/blob/main/Mistral-Small-3.2-24B-Instruct-2506-bf16-Q4_K_S.gguf) | Q4_K_S | 13.549 GB | small, greater quality loss |
| [Mistral-Small-3.2-24B-Instruct-2506-bf16-Q4_K_M.gguf](https://huggingface.co/tensorblock/mlx-community_Mistral-Small-3.2-24B-Instruct-2506-bf16-GGUF/blob/main/Mistral-Small-3.2-24B-Instruct-2506-bf16-Q4_K_M.gguf) | Q4_K_M | 14.334 GB | medium, balanced quality - recommended |
| [Mistral-Small-3.2-24B-Instruct-2506-bf16-Q5_0.gguf](https://huggingface.co/tensorblock/mlx-community_Mistral-Small-3.2-24B-Instruct-2506-bf16-GGUF/blob/main/Mistral-Small-3.2-24B-Instruct-2506-bf16-Q5_0.gguf) | Q5_0 | 16.304 GB | legacy; medium, balanced quality - prefer using Q4_K_M |
| [Mistral-Small-3.2-24B-Instruct-2506-bf16-Q5_K_S.gguf](https://huggingface.co/tensorblock/mlx-community_Mistral-Small-3.2-24B-Instruct-2506-bf16-GGUF/blob/main/Mistral-Small-3.2-24B-Instruct-2506-bf16-Q5_K_S.gguf) | Q5_K_S | 16.304 GB | large, low quality loss - recommended |
| [Mistral-Small-3.2-24B-Instruct-2506-bf16-Q5_K_M.gguf](https://huggingface.co/tensorblock/mlx-community_Mistral-Small-3.2-24B-Instruct-2506-bf16-GGUF/blob/main/Mistral-Small-3.2-24B-Instruct-2506-bf16-Q5_K_M.gguf) | Q5_K_M | 16.764 GB | large, very low quality loss - recommended |
| [Mistral-Small-3.2-24B-Instruct-2506-bf16-Q6_K.gguf](https://huggingface.co/tensorblock/mlx-community_Mistral-Small-3.2-24B-Instruct-2506-bf16-GGUF/blob/main/Mistral-Small-3.2-24B-Instruct-2506-bf16-Q6_K.gguf) | Q6_K | 19.346 GB | very large, extremely low quality loss |
| [Mistral-Small-3.2-24B-Instruct-2506-bf16-Q8_0.gguf](https://huggingface.co/tensorblock/mlx-community_Mistral-Small-3.2-24B-Instruct-2506-bf16-GGUF/blob/main/Mistral-Small-3.2-24B-Instruct-2506-bf16-Q8_0.gguf) | Q8_0 | 25.055 GB | very large, extremely low quality loss - not recommended |


## Downloading instruction

### Command line

Firstly, install Huggingface Client

```shell
pip install -U "huggingface_hub[cli]"
```

Then, downoad the individual model file the a local directory

```shell
huggingface-cli download tensorblock/mlx-community_Mistral-Small-3.2-24B-Instruct-2506-bf16-GGUF --include "Mistral-Small-3.2-24B-Instruct-2506-bf16-Q2_K.gguf" --local-dir MY_LOCAL_DIR
```

If you wanna download multiple model files with a pattern (e.g., `*Q4_K*gguf`), you can try:

```shell
huggingface-cli download tensorblock/mlx-community_Mistral-Small-3.2-24B-Instruct-2506-bf16-GGUF --local-dir MY_LOCAL_DIR --local-dir-use-symlinks False --include='*Q4_K*gguf'
```
