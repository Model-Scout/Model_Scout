---
library_name: transformers
license: apache-2.0
base_model: Saxo/Linkbricks-Horizon-AI-Korean-Pro-27B
datasets:
- Saxo/ko_cn_translation_tech_social_science_linkbricks_single_dataset
- Saxo/ko_jp_translation_tech_social_science_linkbricks_single_dataset
- Saxo/en_ko_translation_tech_science_linkbricks_single_dataset_with_prompt_text_huggingface
- Saxo/en_ko_translation_social_science_linkbricks_single_dataset_with_prompt_text_huggingface
- Saxo/ko_aspect_sentiment_sns_mall_sentiment_linkbricks_single_dataset_with_prompt_text_huggingface
- Saxo/ko_summarization_linkbricks_single_dataset_with_prompt_text_huggingface
- Saxo/OpenOrca_cleaned_kor_linkbricks_single_dataset_with_prompt_text_huggingface
- Saxo/ko_government_qa_total_linkbricks_single_dataset_with_prompt_text_huggingface_sampled
- Saxo/ko-news-corpus-1
- Saxo/ko-news-corpus-2
- Saxo/ko-news-corpus-3
- Saxo/ko-news-corpus-4
- Saxo/ko-news-corpus-5
- Saxo/ko-news-corpus-6
- Saxo/ko-news-corpus-7
- Saxo/ko-news-corpus-8
- Saxo/ko-news-corpus-9
- maywell/ko_Ultrafeedback_binarized
- youjunhyeok/ko-orca-pair-and-ultrafeedback-dpo
- lilacai/glaive-function-calling-v2-sharegpt
- kuotient/gsm8k-ko
language:
- ko
- en
- jp
- cn
pipeline_tag: text-generation
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


## Saxo/Linkbricks-Horizon-AI-Korean-Pro-27B - GGUF

This repo contains GGUF format model files for [Saxo/Linkbricks-Horizon-AI-Korean-Pro-27B](https://huggingface.co/Saxo/Linkbricks-Horizon-AI-Korean-Pro-27B).

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
| [Linkbricks-Horizon-AI-Korean-Pro-27B-Q2_K.gguf](https://huggingface.co/tensorblock/Saxo_Linkbricks-Horizon-AI-Korean-Pro-27B-GGUF/blob/main/Linkbricks-Horizon-AI-Korean-Pro-27B-Q2_K.gguf) | Q2_K | 10.450 GB | smallest, significant quality loss - not recommended for most purposes |
| [Linkbricks-Horizon-AI-Korean-Pro-27B-Q3_K_S.gguf](https://huggingface.co/tensorblock/Saxo_Linkbricks-Horizon-AI-Korean-Pro-27B-GGUF/blob/main/Linkbricks-Horizon-AI-Korean-Pro-27B-Q3_K_S.gguf) | Q3_K_S | 12.169 GB | very small, high quality loss |
| [Linkbricks-Horizon-AI-Korean-Pro-27B-Q3_K_M.gguf](https://huggingface.co/tensorblock/Saxo_Linkbricks-Horizon-AI-Korean-Pro-27B-GGUF/blob/main/Linkbricks-Horizon-AI-Korean-Pro-27B-Q3_K_M.gguf) | Q3_K_M | 13.425 GB | very small, high quality loss |
| [Linkbricks-Horizon-AI-Korean-Pro-27B-Q3_K_L.gguf](https://huggingface.co/tensorblock/Saxo_Linkbricks-Horizon-AI-Korean-Pro-27B-GGUF/blob/main/Linkbricks-Horizon-AI-Korean-Pro-27B-Q3_K_L.gguf) | Q3_K_L | 14.519 GB | small, substantial quality loss |
| [Linkbricks-Horizon-AI-Korean-Pro-27B-Q4_0.gguf](https://huggingface.co/tensorblock/Saxo_Linkbricks-Horizon-AI-Korean-Pro-27B-GGUF/blob/main/Linkbricks-Horizon-AI-Korean-Pro-27B-Q4_0.gguf) | Q4_0 | 15.628 GB | legacy; small, very high quality loss - prefer using Q3_K_M |
| [Linkbricks-Horizon-AI-Korean-Pro-27B-Q4_K_S.gguf](https://huggingface.co/tensorblock/Saxo_Linkbricks-Horizon-AI-Korean-Pro-27B-GGUF/blob/main/Linkbricks-Horizon-AI-Korean-Pro-27B-Q4_K_S.gguf) | Q4_K_S | 15.739 GB | small, greater quality loss |
| [Linkbricks-Horizon-AI-Korean-Pro-27B-Q4_K_M.gguf](https://huggingface.co/tensorblock/Saxo_Linkbricks-Horizon-AI-Korean-Pro-27B-GGUF/blob/main/Linkbricks-Horizon-AI-Korean-Pro-27B-Q4_K_M.gguf) | Q4_K_M | 16.645 GB | medium, balanced quality - recommended |
| [Linkbricks-Horizon-AI-Korean-Pro-27B-Q5_0.gguf](https://huggingface.co/tensorblock/Saxo_Linkbricks-Horizon-AI-Korean-Pro-27B-GGUF/blob/main/Linkbricks-Horizon-AI-Korean-Pro-27B-Q5_0.gguf) | Q5_0 | 18.884 GB | legacy; medium, balanced quality - prefer using Q4_K_M |
| [Linkbricks-Horizon-AI-Korean-Pro-27B-Q5_K_S.gguf](https://huggingface.co/tensorblock/Saxo_Linkbricks-Horizon-AI-Korean-Pro-27B-GGUF/blob/main/Linkbricks-Horizon-AI-Korean-Pro-27B-Q5_K_S.gguf) | Q5_K_S | 18.884 GB | large, low quality loss - recommended |
| [Linkbricks-Horizon-AI-Korean-Pro-27B-Q5_K_M.gguf](https://huggingface.co/tensorblock/Saxo_Linkbricks-Horizon-AI-Korean-Pro-27B-GGUF/blob/main/Linkbricks-Horizon-AI-Korean-Pro-27B-Q5_K_M.gguf) | Q5_K_M | 19.408 GB | large, very low quality loss - recommended |
| [Linkbricks-Horizon-AI-Korean-Pro-27B-Q6_K.gguf](https://huggingface.co/tensorblock/Saxo_Linkbricks-Horizon-AI-Korean-Pro-27B-GGUF/blob/main/Linkbricks-Horizon-AI-Korean-Pro-27B-Q6_K.gguf) | Q6_K | 22.344 GB | very large, extremely low quality loss |
| [Linkbricks-Horizon-AI-Korean-Pro-27B-Q8_0.gguf](https://huggingface.co/tensorblock/Saxo_Linkbricks-Horizon-AI-Korean-Pro-27B-GGUF/blob/main/Linkbricks-Horizon-AI-Korean-Pro-27B-Q8_0.gguf) | Q8_0 | 28.937 GB | very large, extremely low quality loss - not recommended |


## Downloading instruction

### Command line

Firstly, install Huggingface Client

```shell
pip install -U "huggingface_hub[cli]"
```

Then, downoad the individual model file the a local directory

```shell
huggingface-cli download tensorblock/Saxo_Linkbricks-Horizon-AI-Korean-Pro-27B-GGUF --include "Linkbricks-Horizon-AI-Korean-Pro-27B-Q2_K.gguf" --local-dir MY_LOCAL_DIR
```

If you wanna download multiple model files with a pattern (e.g., `*Q4_K*gguf`), you can try:

```shell
huggingface-cli download tensorblock/Saxo_Linkbricks-Horizon-AI-Korean-Pro-27B-GGUF --local-dir MY_LOCAL_DIR --local-dir-use-symlinks False --include='*Q4_K*gguf'
```
