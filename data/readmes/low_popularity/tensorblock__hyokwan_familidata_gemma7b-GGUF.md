---
license: mit
datasets:
- hyokwan/common
language:
- ko
metrics:
- accuracy
base_model: hyokwan/familidata_gemma7b
pipeline_tag: text-generation
library_name: transformers
tags:
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


## hyokwan/familidata_gemma7b - GGUF

This repo contains GGUF format model files for [hyokwan/familidata_gemma7b](https://huggingface.co/hyokwan/familidata_gemma7b).

The files were quantized using machines provided by [TensorBlock](https://tensorblock.co/), and they are compatible with llama.cpp as of [commit b5165](https://github.com/ggml-org/llama.cpp/commit/1d735c0b4fa0551c51c2f4ac888dd9a01f447985).

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
<bos><start_of_turn>user
{prompt}<end_of_turn>
<start_of_turn>model
```

## Model file specification

| Filename | Quant type | File Size | Description |
| -------- | ---------- | --------- | ----------- |
| [familidata_gemma7b-Q2_K.gguf](https://huggingface.co/tensorblock/hyokwan_familidata_gemma7b-GGUF/blob/main/familidata_gemma7b-Q2_K.gguf) | Q2_K | 3.481 GB | smallest, significant quality loss - not recommended for most purposes |
| [familidata_gemma7b-Q3_K_S.gguf](https://huggingface.co/tensorblock/hyokwan_familidata_gemma7b-GGUF/blob/main/familidata_gemma7b-Q3_K_S.gguf) | Q3_K_S | 3.982 GB | very small, high quality loss |
| [familidata_gemma7b-Q3_K_M.gguf](https://huggingface.co/tensorblock/hyokwan_familidata_gemma7b-GGUF/blob/main/familidata_gemma7b-Q3_K_M.gguf) | Q3_K_M | 4.369 GB | very small, high quality loss |
| [familidata_gemma7b-Q3_K_L.gguf](https://huggingface.co/tensorblock/hyokwan_familidata_gemma7b-GGUF/blob/main/familidata_gemma7b-Q3_K_L.gguf) | Q3_K_L | 4.709 GB | small, substantial quality loss |
| [familidata_gemma7b-Q4_0.gguf](https://huggingface.co/tensorblock/hyokwan_familidata_gemma7b-GGUF/blob/main/familidata_gemma7b-Q4_0.gguf) | Q4_0 | 5.012 GB | legacy; small, very high quality loss - prefer using Q3_K_M |
| [familidata_gemma7b-Q4_K_S.gguf](https://huggingface.co/tensorblock/hyokwan_familidata_gemma7b-GGUF/blob/main/familidata_gemma7b-Q4_K_S.gguf) | Q4_K_S | 5.046 GB | small, greater quality loss |
| [familidata_gemma7b-Q4_K_M.gguf](https://huggingface.co/tensorblock/hyokwan_familidata_gemma7b-GGUF/blob/main/familidata_gemma7b-Q4_K_M.gguf) | Q4_K_M | 5.330 GB | medium, balanced quality - recommended |
| [familidata_gemma7b-Q5_0.gguf](https://huggingface.co/tensorblock/hyokwan_familidata_gemma7b-GGUF/blob/main/familidata_gemma7b-Q5_0.gguf) | Q5_0 | 5.981 GB | legacy; medium, balanced quality - prefer using Q4_K_M |
| [familidata_gemma7b-Q5_K_S.gguf](https://huggingface.co/tensorblock/hyokwan_familidata_gemma7b-GGUF/blob/main/familidata_gemma7b-Q5_K_S.gguf) | Q5_K_S | 5.981 GB | large, low quality loss - recommended |
| [familidata_gemma7b-Q5_K_M.gguf](https://huggingface.co/tensorblock/hyokwan_familidata_gemma7b-GGUF/blob/main/familidata_gemma7b-Q5_K_M.gguf) | Q5_K_M | 6.145 GB | large, very low quality loss - recommended |
| [familidata_gemma7b-Q6_K.gguf](https://huggingface.co/tensorblock/hyokwan_familidata_gemma7b-GGUF/blob/main/familidata_gemma7b-Q6_K.gguf) | Q6_K | 7.010 GB | very large, extremely low quality loss |
| [familidata_gemma7b-Q8_0.gguf](https://huggingface.co/tensorblock/hyokwan_familidata_gemma7b-GGUF/blob/main/familidata_gemma7b-Q8_0.gguf) | Q8_0 | 9.078 GB | very large, extremely low quality loss - not recommended |


## Downloading instruction

### Command line

Firstly, install Huggingface Client

```shell
pip install -U "huggingface_hub[cli]"
```

Then, downoad the individual model file the a local directory

```shell
huggingface-cli download tensorblock/hyokwan_familidata_gemma7b-GGUF --include "familidata_gemma7b-Q2_K.gguf" --local-dir MY_LOCAL_DIR
```

If you wanna download multiple model files with a pattern (e.g., `*Q4_K*gguf`), you can try:

```shell
huggingface-cli download tensorblock/hyokwan_familidata_gemma7b-GGUF --local-dir MY_LOCAL_DIR --local-dir-use-symlinks False --include='*Q4_K*gguf'
```
