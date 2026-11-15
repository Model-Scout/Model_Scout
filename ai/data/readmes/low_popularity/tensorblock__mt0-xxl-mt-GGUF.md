---
datasets:
- bigscience/xP3mt
- mc4
license: apache-2.0
language:
- af
- am
- ar
- az
- be
- bg
- bn
- ca
- ceb
- co
- cs
- cy
- da
- de
- el
- en
- eo
- es
- et
- eu
- fa
- fi
- fil
- fr
- fy
- ga
- gd
- gl
- gu
- ha
- haw
- hi
- hmn
- ht
- hu
- hy
- ig
- is
- it
- iw
- ja
- jv
- ka
- kk
- km
- kn
- ko
- ku
- ky
- la
- lb
- lo
- lt
- lv
- mg
- mi
- mk
- ml
- mn
- mr
- ms
- mt
- my
- ne
- nl
- 'no'
- ny
- pa
- pl
- ps
- pt
- ro
- ru
- sd
- si
- sk
- sl
- sm
- sn
- so
- sq
- sr
- st
- su
- sv
- sw
- ta
- te
- tg
- th
- tr
- uk
- und
- ur
- uz
- vi
- xh
- yi
- yo
- zh
- zu
tags:
- text2text-generation
- TensorBlock
- GGUF
widget:
- text: Life is beautiful! Translate to Mongolian.
  example_title: mn-en translation
- text: Le mot japonais «憂鬱» veut dire quoi en Odia?
  example_title: jp-or-fr translation
- text: Stell mir eine schwierige Quiz Frage bei der es um Astronomie geht. Bitte
    stell die Frage auf Norwegisch.
  example_title: de-nb quiz
- text: 一个传奇的开端，一个不灭的神话，这不仅仅是一部电影，而是作为一个走进新时代的标签，永远彪炳史册。Would you rate the previous
    review as positive, neutral or negative?
  example_title: zh-en sentiment
- text: 一个传奇的开端，一个不灭的神话，这不仅仅是一部电影，而是作为一个走进新时代的标签，永远彪炳史册。你认为这句话的立场是赞扬、中立还是批评？
  example_title: zh-zh sentiment
- text: Suggest at least five related search terms to "Mạng neural nhân tạo".
  example_title: vi-en query
- text: Proposez au moins cinq mots clés concernant «Réseau de neurones artificiels».
  example_title: fr-fr query
- text: Explain in a sentence in Telugu what is backpropagation in neural networks.
  example_title: te-en qa
- text: Why is the sky blue?
  example_title: en-en qa
- text: 'Write a fairy tale about a troll saving a princess from a dangerous dragon.
    The fairy tale is a masterpiece that has achieved praise worldwide and its moral
    is "Heroes Come in All Shapes and Sizes". Story (in Spanish):'
  example_title: es-en fable
- text: 'Write a fable about wood elves living in a forest that is suddenly invaded
    by ogres. The fable is a masterpiece that has achieved praise worldwide and its
    moral is "Violence is the last refuge of the incompetent". Fable (in Hindi):'
  example_title: hi-en fable
pipeline_tag: text2text-generation
base_model: bigscience/mt0-xxl-mt
model-index:
- name: mt0-xxl-mt
  results:
  - task:
      type: Coreference resolution
    dataset:
      name: Winogrande XL (xl)
      type: winogrande
      config: xl
      split: validation
      revision: a80f460359d1e9a67c006011c94de42a8759430c
    metrics:
    - type: Accuracy
      value: 62.67
  - task:
      type: Coreference resolution
    dataset:
      name: XWinograd (en)
      type: Muennighoff/xwinograd
      config: en
      split: test
      revision: 9dd5ea5505fad86b7bedad667955577815300cee
    metrics:
    - type: Accuracy
      value: 83.31
  - task:
      type: Coreference resolution
    dataset:
      name: XWinograd (fr)
      type: Muennighoff/xwinograd
      config: fr
      split: test
      revision: 9dd5ea5505fad86b7bedad667955577815300cee
    metrics:
    - type: Accuracy
      value: 78.31
  - task:
      type: Coreference resolution
    dataset:
      name: XWinograd (jp)
      type: Muennighoff/xwinograd
      config: jp
      split: test
      revision: 9dd5ea5505fad86b7bedad667955577815300cee
    metrics:
    - type: Accuracy
      value: 80.19
  - task:
      type: Coreference resolution
    dataset:
      name: XWinograd (pt)
      type: Muennighoff/xwinograd
      config: pt
      split: test
      revision: 9dd5ea5505fad86b7bedad667955577815300cee
    metrics:
    - type: Accuracy
      value: 80.99
  - task:
      type: Coreference resolution
    dataset:
      name: XWinograd (ru)
      type: Muennighoff/xwinograd
      config: ru
      split: test
      revision: 9dd5ea5505fad86b7bedad667955577815300cee
    metrics:
    - type: Accuracy
      value: 79.05
  - task:
      type: Coreference resolution
    dataset:
      name: XWinograd (zh)
      type: Muennighoff/xwinograd
      config: zh
      split: test
      revision: 9dd5ea5505fad86b7bedad667955577815300cee
    metrics:
    - type: Accuracy
      value: 82.34
  - task:
      type: Natural language inference
    dataset:
      name: ANLI (r1)
      type: anli
      config: r1
      split: validation
      revision: 9dbd830a06fea8b1c49d6e5ef2004a08d9f45094
    metrics:
    - type: Accuracy
      value: 49.5
  - task:
      type: Natural language inference
    dataset:
      name: ANLI (r2)
      type: anli
      config: r2
      split: validation
      revision: 9dbd830a06fea8b1c49d6e5ef2004a08d9f45094
    metrics:
    - type: Accuracy
      value: 42
  - task:
      type: Natural language inference
    dataset:
      name: ANLI (r3)
      type: anli
      config: r3
      split: validation
      revision: 9dbd830a06fea8b1c49d6e5ef2004a08d9f45094
    metrics:
    - type: Accuracy
      value: 48.17
  - task:
      type: Natural language inference
    dataset:
      name: SuperGLUE (cb)
      type: super_glue
      config: cb
      split: validation
      revision: 9e12063561e7e6c79099feb6d5a493142584e9e2
    metrics:
    - type: Accuracy
      value: 87.5
  - task:
      type: Natural language inference
    dataset:
      name: SuperGLUE (rte)
      type: super_glue
      config: rte
      split: validation
      revision: 9e12063561e7e6c79099feb6d5a493142584e9e2
    metrics:
    - type: Accuracy
      value: 84.84
  - task:
      type: Natural language inference
    dataset:
      name: XNLI (ar)
      type: xnli
      config: ar
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 58.03
  - task:
      type: Natural language inference
    dataset:
      name: XNLI (bg)
      type: xnli
      config: bg
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 59.92
  - task:
      type: Natural language inference
    dataset:
      name: XNLI (de)
      type: xnli
      config: de
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 60.16
  - task:
      type: Natural language inference
    dataset:
      name: XNLI (el)
      type: xnli
      config: el
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 59.2
  - task:
      type: Natural language inference
    dataset:
      name: XNLI (en)
      type: xnli
      config: en
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 62.25
  - task:
      type: Natural language inference
    dataset:
      name: XNLI (es)
      type: xnli
      config: es
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 60.92
  - task:
      type: Natural language inference
    dataset:
      name: XNLI (fr)
      type: xnli
      config: fr
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 59.88
  - task:
      type: Natural language inference
    dataset:
      name: XNLI (hi)
      type: xnli
      config: hi
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 57.47
  - task:
      type: Natural language inference
    dataset:
      name: XNLI (ru)
      type: xnli
      config: ru
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 58.67
  - task:
      type: Natural language inference
    dataset:
      name: XNLI (sw)
      type: xnli
      config: sw
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 56.79
  - task:
      type: Natural language inference
    dataset:
      name: XNLI (th)
      type: xnli
      config: th
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 58.03
  - task:
      type: Natural language inference
    dataset:
      name: XNLI (tr)
      type: xnli
      config: tr
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 57.67
  - task:
      type: Natural language inference
    dataset:
      name: XNLI (ur)
      type: xnli
      config: ur
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 55.98
  - task:
      type: Natural language inference
    dataset:
      name: XNLI (vi)
      type: xnli
      config: vi
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 58.92
  - task:
      type: Natural language inference
    dataset:
      name: XNLI (zh)
      type: xnli
      config: zh
      split: validation
      revision: a5a45e4ff92d5d3f34de70aaf4b72c3bdf9f7f16
    metrics:
    - type: Accuracy
      value: 58.71
  - task:
      type: Sentence completion
    dataset:
      name: StoryCloze (2016)
      type: story_cloze
      config: '2016'
      split: validation
      revision: e724c6f8cdf7c7a2fb229d862226e15b023ee4db
    metrics:
    - type: Accuracy
      value: 94.66
  - task:
      type: Sentence completion
    dataset:
      name: SuperGLUE (copa)
      type: super_glue
      config: copa
      split: validation
      revision: 9e12063561e7e6c79099feb6d5a493142584e9e2
    metrics:
    - type: Accuracy
      value: 88
  - task:
      type: Sentence completion
    dataset:
      name: XCOPA (et)
      type: xcopa
      config: et
      split: validation
      revision: 37f73c60fb123111fa5af5f9b705d0b3747fd187
    metrics:
    - type: Accuracy
      value: 81
  - task:
      type: Sentence completion
    dataset:
      name: XCOPA (ht)
      type: xcopa
      config: ht
      split: validation
      revision: 37f73c60fb123111fa5af5f9b705d0b3747fd187
    metrics:
    - type: Accuracy
      value: 79
  - task:
      type: Sentence completion
    dataset:
      name: XCOPA (id)
      type: xcopa
      config: id
      split: validation
      revision: 37f73c60fb123111fa5af5f9b705d0b3747fd187
    metrics:
    - type: Accuracy
      value: 90
  - task:
      type: Sentence completion
    dataset:
      name: XCOPA (it)
      type: xcopa
      config: it
      split: validation
      revision: 37f73c60fb123111fa5af5f9b705d0b3747fd187
    metrics:
    - type: Accuracy
      value: 88
  - task:
      type: Sentence completion
    dataset:
      name: XCOPA (qu)
      type: xcopa
      config: qu
      split: validation
      revision: 37f73c60fb123111fa5af5f9b705d0b3747fd187
    metrics:
    - type: Accuracy
      value: 56
  - task:
      type: Sentence completion
    dataset:
      name: XCOPA (sw)
      type: xcopa
      config: sw
      split: validation
      revision: 37f73c60fb123111fa5af5f9b705d0b3747fd187
    metrics:
    - type: Accuracy
      value: 81
  - task:
      type: Sentence completion
    dataset:
      name: XCOPA (ta)
      type: xcopa
      config: ta
      split: validation
      revision: 37f73c60fb123111fa5af5f9b705d0b3747fd187
    metrics:
    - type: Accuracy
      value: 81
  - task:
      type: Sentence completion
    dataset:
      name: XCOPA (th)
      type: xcopa
      config: th
      split: validation
      revision: 37f73c60fb123111fa5af5f9b705d0b3747fd187
    metrics:
    - type: Accuracy
      value: 76
  - task:
      type: Sentence completion
    dataset:
      name: XCOPA (tr)
      type: xcopa
      config: tr
      split: validation
      revision: 37f73c60fb123111fa5af5f9b705d0b3747fd187
    metrics:
    - type: Accuracy
      value: 76
  - task:
      type: Sentence completion
    dataset:
      name: XCOPA (vi)
      type: xcopa
      config: vi
      split: validation
      revision: 37f73c60fb123111fa5af5f9b705d0b3747fd187
    metrics:
    - type: Accuracy
      value: 85
  - task:
      type: Sentence completion
    dataset:
      name: XCOPA (zh)
      type: xcopa
      config: zh
      split: validation
      revision: 37f73c60fb123111fa5af5f9b705d0b3747fd187
    metrics:
    - type: Accuracy
      value: 87
  - task:
      type: Sentence completion
    dataset:
      name: XStoryCloze (ar)
      type: Muennighoff/xstory_cloze
      config: ar
      split: validation
      revision: 8bb76e594b68147f1a430e86829d07189622b90d
    metrics:
    - type: Accuracy
      value: 91
  - task:
      type: Sentence completion
    dataset:
      name: XStoryCloze (es)
      type: Muennighoff/xstory_cloze
      config: es
      split: validation
      revision: 8bb76e594b68147f1a430e86829d07189622b90d
    metrics:
    - type: Accuracy
      value: 93.38
  - task:
      type: Sentence completion
    dataset:
      name: XStoryCloze (eu)
      type: Muennighoff/xstory_cloze
      config: eu
      split: validation
      revision: 8bb76e594b68147f1a430e86829d07189622b90d
    metrics:
    - type: Accuracy
      value: 91.13
  - task:
      type: Sentence completion
    dataset:
      name: XStoryCloze (hi)
      type: Muennighoff/xstory_cloze
      config: hi
      split: validation
      revision: 8bb76e594b68147f1a430e86829d07189622b90d
    metrics:
    - type: Accuracy
      value: 90.73
  - task:
      type: Sentence completion
    dataset:
      name: XStoryCloze (id)
      type: Muennighoff/xstory_cloze
      config: id
      split: validation
      revision: 8bb76e594b68147f1a430e86829d07189622b90d
    metrics:
    - type: Accuracy
      value: 93.05
  - task:
      type: Sentence completion
    dataset:
      name: XStoryCloze (my)
      type: Muennighoff/xstory_cloze
      config: my
      split: validation
      revision: 8bb76e594b68147f1a430e86829d07189622b90d
    metrics:
    - type: Accuracy
      value: 86.7
  - task:
      type: Sentence completion
    dataset:
      name: XStoryCloze (ru)
      type: Muennighoff/xstory_cloze
      config: ru
      split: validation
      revision: 8bb76e594b68147f1a430e86829d07189622b90d
    metrics:
    - type: Accuracy
      value: 91.66
  - task:
      type: Sentence completion
    dataset:
      name: XStoryCloze (sw)
      type: Muennighoff/xstory_cloze
      config: sw
      split: validation
      revision: 8bb76e594b68147f1a430e86829d07189622b90d
    metrics:
    - type: Accuracy
      value: 89.61
  - task:
      type: Sentence completion
    dataset:
      name: XStoryCloze (te)
      type: Muennighoff/xstory_cloze
      config: te
      split: validation
      revision: 8bb76e594b68147f1a430e86829d07189622b90d
    metrics:
    - type: Accuracy
      value: 90.4
  - task:
      type: Sentence completion
    dataset:
      name: XStoryCloze (zh)
      type: Muennighoff/xstory_cloze
      config: zh
      split: validation
      revision: 8bb76e594b68147f1a430e86829d07189622b90d
    metrics:
    - type: Accuracy
      value: 93.05
---

<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="https://i.imgur.com/jC7kdl8.jpeg" alt="TensorBlock" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>

[![Website](https://img.shields.io/badge/Website-tensorblock.co-blue?logo=google-chrome&logoColor=white)](https://tensorblock.co)
[![Twitter](https://img.shields.io/twitter/follow/tensorblock_aoi?style=social)](https://twitter.com/tensorblock_aoi)
[![Discord](https://img.shields.io/badge/Discord-Join%20Us-5865F2?logo=discord&logoColor=white)](https://discord.gg/Ej5NmeHFf2)
[![GitHub](https://img.shields.io/badge/GitHub-TensorBlock-black?logo=github&logoColor=white)](https://github.com/TensorBlock)
[![Telegram](https://img.shields.io/badge/Telegram-Group-blue?logo=telegram)](https://t.me/TensorBlock)


## bigscience/mt0-xxl-mt - GGUF

This repo contains GGUF format model files for [bigscience/mt0-xxl-mt](https://huggingface.co/bigscience/mt0-xxl-mt).

The files were quantized using machines provided by [TensorBlock](https://tensorblock.co/), and they are compatible with llama.cpp as of [commit ec7f3ac](https://github.com/ggerganov/llama.cpp/commit/ec7f3ac9ab33e46b136eb5ab6a76c4d81f57c7f1).

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

```

## Model file specification

| Filename | Quant type | File Size | Description |
| -------- | ---------- | --------- | ----------- |
| [mt0-xxl-mt-Q2_K.gguf](https://huggingface.co/tensorblock/mt0-xxl-mt-GGUF/blob/main/mt0-xxl-mt-Q2_K.gguf) | Q2_K | 5.079 GB | smallest, significant quality loss - not recommended for most purposes |
| [mt0-xxl-mt-Q3_K_S.gguf](https://huggingface.co/tensorblock/mt0-xxl-mt-GGUF/blob/main/mt0-xxl-mt-Q3_K_S.gguf) | Q3_K_S | 5.960 GB | very small, high quality loss |
| [mt0-xxl-mt-Q3_K_M.gguf](https://huggingface.co/tensorblock/mt0-xxl-mt-GGUF/blob/main/mt0-xxl-mt-Q3_K_M.gguf) | Q3_K_M | 6.397 GB | very small, high quality loss |
| [mt0-xxl-mt-Q3_K_L.gguf](https://huggingface.co/tensorblock/mt0-xxl-mt-GGUF/blob/main/mt0-xxl-mt-Q3_K_L.gguf) | Q3_K_L | 6.791 GB | small, substantial quality loss |
| [mt0-xxl-mt-Q4_0.gguf](https://huggingface.co/tensorblock/mt0-xxl-mt-GGUF/blob/main/mt0-xxl-mt-Q4_0.gguf) | Q4_0 | 7.540 GB | legacy; small, very high quality loss - prefer using Q3_K_M |
| [mt0-xxl-mt-Q4_K_S.gguf](https://huggingface.co/tensorblock/mt0-xxl-mt-GGUF/blob/main/mt0-xxl-mt-Q4_K_S.gguf) | Q4_K_S | 7.564 GB | small, greater quality loss |
| [mt0-xxl-mt-Q4_K_M.gguf](https://huggingface.co/tensorblock/mt0-xxl-mt-GGUF/blob/main/mt0-xxl-mt-Q4_K_M.gguf) | Q4_K_M | 8.085 GB | medium, balanced quality - recommended |
| [mt0-xxl-mt-Q5_0.gguf](https://huggingface.co/tensorblock/mt0-xxl-mt-GGUF/blob/main/mt0-xxl-mt-Q5_0.gguf) | Q5_0 | 9.027 GB | legacy; medium, balanced quality - prefer using Q4_K_M |
| [mt0-xxl-mt-Q5_K_S.gguf](https://huggingface.co/tensorblock/mt0-xxl-mt-GGUF/blob/main/mt0-xxl-mt-Q5_K_S.gguf) | Q5_K_S | 9.027 GB | large, low quality loss - recommended |
| [mt0-xxl-mt-Q5_K_M.gguf](https://huggingface.co/tensorblock/mt0-xxl-mt-GGUF/blob/main/mt0-xxl-mt-Q5_K_M.gguf) | Q5_K_M | 9.308 GB | large, very low quality loss - recommended |
| [mt0-xxl-mt-Q6_K.gguf](https://huggingface.co/tensorblock/mt0-xxl-mt-GGUF/blob/main/mt0-xxl-mt-Q6_K.gguf) | Q6_K | 10.607 GB | very large, extremely low quality loss |
| [mt0-xxl-mt-Q8_0.gguf](https://huggingface.co/tensorblock/mt0-xxl-mt-GGUF/blob/main/mt0-xxl-mt-Q8_0.gguf) | Q8_0 | 13.736 GB | very large, extremely low quality loss - not recommended |


## Downloading instruction

### Command line

Firstly, install Huggingface Client

```shell
pip install -U "huggingface_hub[cli]"
```

Then, downoad the individual model file the a local directory

```shell
huggingface-cli download tensorblock/mt0-xxl-mt-GGUF --include "mt0-xxl-mt-Q2_K.gguf" --local-dir MY_LOCAL_DIR
```

If you wanna download multiple model files with a pattern (e.g., `*Q4_K*gguf`), you can try:

```shell
huggingface-cli download tensorblock/mt0-xxl-mt-GGUF --local-dir MY_LOCAL_DIR --local-dir-use-symlinks False --include='*Q4_K*gguf'
```
