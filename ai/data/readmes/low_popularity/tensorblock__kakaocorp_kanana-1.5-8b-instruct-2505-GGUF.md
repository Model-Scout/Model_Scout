---
language:
- en
- ko
library_name: transformers
license: apache-2.0
pipeline_tag: text-generation
model_id: kakaocorp/kanana-1.5-8b-instruct-2505
repo: kakaocorp/kanana-1.5-8b-instruct-2505
developers: Kanana LLM
training_regime: bf16 mixed precision
base_model: kakaocorp/kanana-1.5-8b-instruct-2505
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


## kakaocorp/kanana-1.5-8b-instruct-2505 - GGUF

<div style="text-align: left; margin: 20px 0;">
    <a href="https://discord.com/invite/Ej5NmeHFf2" style="display: inline-block; padding: 10px 20px; background-color: #5865F2; color: white; text-decoration: none; border-radius: 5px; font-weight: bold;">
        Join our Discord to learn more about what we're building ↗
    </a>
</div>

This repo contains GGUF format model files for [kakaocorp/kanana-1.5-8b-instruct-2505](https://huggingface.co/kakaocorp/kanana-1.5-8b-instruct-2505).

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
<|begin_of_text|><|start_header_id|>system<|end_header_id|>


<|eot_id|><|start_header_id|>system<|end_header_id|>

{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>

{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
```

## Model file specification

| Filename | Quant type | File Size | Description |
| -------- | ---------- | --------- | ----------- |
| [kanana-1.5-8b-instruct-2505-Q2_K.gguf](https://huggingface.co/tensorblock/kakaocorp_kanana-1.5-8b-instruct-2505-GGUF/blob/main/kanana-1.5-8b-instruct-2505-Q2_K.gguf) | Q2_K | 3.179 GB | smallest, significant quality loss - not recommended for most purposes |
| [kanana-1.5-8b-instruct-2505-Q3_K_S.gguf](https://huggingface.co/tensorblock/kakaocorp_kanana-1.5-8b-instruct-2505-GGUF/blob/main/kanana-1.5-8b-instruct-2505-Q3_K_S.gguf) | Q3_K_S | 3.665 GB | very small, high quality loss |
| [kanana-1.5-8b-instruct-2505-Q3_K_M.gguf](https://huggingface.co/tensorblock/kakaocorp_kanana-1.5-8b-instruct-2505-GGUF/blob/main/kanana-1.5-8b-instruct-2505-Q3_K_M.gguf) | Q3_K_M | 4.019 GB | very small, high quality loss |
| [kanana-1.5-8b-instruct-2505-Q3_K_L.gguf](https://huggingface.co/tensorblock/kakaocorp_kanana-1.5-8b-instruct-2505-GGUF/blob/main/kanana-1.5-8b-instruct-2505-Q3_K_L.gguf) | Q3_K_L | 4.322 GB | small, substantial quality loss |
| [kanana-1.5-8b-instruct-2505-Q4_0.gguf](https://huggingface.co/tensorblock/kakaocorp_kanana-1.5-8b-instruct-2505-GGUF/blob/main/kanana-1.5-8b-instruct-2505-Q4_0.gguf) | Q4_0 | 4.661 GB | legacy; small, very high quality loss - prefer using Q3_K_M |
| [kanana-1.5-8b-instruct-2505-Q4_K_S.gguf](https://huggingface.co/tensorblock/kakaocorp_kanana-1.5-8b-instruct-2505-GGUF/blob/main/kanana-1.5-8b-instruct-2505-Q4_K_S.gguf) | Q4_K_S | 4.693 GB | small, greater quality loss |
| [kanana-1.5-8b-instruct-2505-Q4_K_M.gguf](https://huggingface.co/tensorblock/kakaocorp_kanana-1.5-8b-instruct-2505-GGUF/blob/main/kanana-1.5-8b-instruct-2505-Q4_K_M.gguf) | Q4_K_M | 4.921 GB | medium, balanced quality - recommended |
| [kanana-1.5-8b-instruct-2505-Q5_0.gguf](https://huggingface.co/tensorblock/kakaocorp_kanana-1.5-8b-instruct-2505-GGUF/blob/main/kanana-1.5-8b-instruct-2505-Q5_0.gguf) | Q5_0 | 5.599 GB | legacy; medium, balanced quality - prefer using Q4_K_M |
| [kanana-1.5-8b-instruct-2505-Q5_K_S.gguf](https://huggingface.co/tensorblock/kakaocorp_kanana-1.5-8b-instruct-2505-GGUF/blob/main/kanana-1.5-8b-instruct-2505-Q5_K_S.gguf) | Q5_K_S | 5.599 GB | large, low quality loss - recommended |
| [kanana-1.5-8b-instruct-2505-Q5_K_M.gguf](https://huggingface.co/tensorblock/kakaocorp_kanana-1.5-8b-instruct-2505-GGUF/blob/main/kanana-1.5-8b-instruct-2505-Q5_K_M.gguf) | Q5_K_M | 5.733 GB | large, very low quality loss - recommended |
| [kanana-1.5-8b-instruct-2505-Q6_K.gguf](https://huggingface.co/tensorblock/kakaocorp_kanana-1.5-8b-instruct-2505-GGUF/blob/main/kanana-1.5-8b-instruct-2505-Q6_K.gguf) | Q6_K | 6.596 GB | very large, extremely low quality loss |
| [kanana-1.5-8b-instruct-2505-Q8_0.gguf](https://huggingface.co/tensorblock/kakaocorp_kanana-1.5-8b-instruct-2505-GGUF/blob/main/kanana-1.5-8b-instruct-2505-Q8_0.gguf) | Q8_0 | 8.541 GB | very large, extremely low quality loss - not recommended |


## Downloading instruction

### Command line

Firstly, install Huggingface Client

```shell
pip install -U "huggingface_hub[cli]"
```

Then, downoad the individual model file the a local directory

```shell
huggingface-cli download tensorblock/kakaocorp_kanana-1.5-8b-instruct-2505-GGUF --include "kanana-1.5-8b-instruct-2505-Q2_K.gguf" --local-dir MY_LOCAL_DIR
```

If you wanna download multiple model files with a pattern (e.g., `*Q4_K*gguf`), you can try:

```shell
huggingface-cli download tensorblock/kakaocorp_kanana-1.5-8b-instruct-2505-GGUF --local-dir MY_LOCAL_DIR --local-dir-use-symlinks False --include='*Q4_K*gguf'
```
