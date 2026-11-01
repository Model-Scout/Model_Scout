---
license: gemma
license_link: https://ai.google.dev/gemma/terms
base_model:
  - google/translategemma-27b-it
base_model_relation: quantized
language:
  - zh
  - en
  - ja
  - ko
  - fr
  - de
  - es
  - ru
pipeline_tag: translation
library_name: gguf
tags:
  - translation
  - gemma3
  - gguf
  - llama.cpp
  - 42model
---

<!-- README for the Hugging Face repo `42ailab/TranslateGemma-27B-GGUF`. Editing this file changes the repo landing page. -->
# TranslateGemma-27B · Fully Local Multilingual Translation

[![License: Gemma](https://img.shields.io/badge/License-Gemma-blue.svg)](https://ai.google.dev/gemma/terms)
[![Runs Local](https://img.shields.io/badge/Runs-100%25_Local-brightgreen.svg)](https://42model.com)
[![Platform](https://img.shields.io/badge/Platform-macOS_|_Windows_|_Linux-lightgrey.svg)](https://42model.com)
[![ModelScope](https://img.shields.io/badge/ModelScope-42ailab-624AFF.svg)](https://modelscope.cn/models/42ailab/TranslateGemma-27B-GGUF)

**English** | [简体中文](./README_zh.md) · Also on [ModelScope](https://modelscope.cn/models/42ailab/TranslateGemma-27B-GGUF) · [42ailab.com](https://42ailab.com)

Give it text in any language and this model translates it into the language you want — **55 languages**, entirely on your own computer. **No cloud, free, private.**

> **The model was built by the [Google Translate team](https://blog.google/innovation-and-ai/technology/developers-tools/translategemma/) and released under the Gemma Terms of Use** (TranslateGemma, based on Google's Gemma 3). **This repo is not a new model** — we converted that open model into a quantized build (GGUF) that **runs offline on your computer**, and adapted it so ordinary chat clients can call it directly. The translation capability belongs to Google; what we did was make it run locally and make it pleasant to use.

## 1. The problem it solves

Reading, writing and communicating across languages is part of daily life, but mainstream translation usually means **uploading your text to someone else's server**:

- **Privacy-sensitive content**: contracts, medical records, internal documents, personal letters — things you would rather not hand to a cloud service;
- **Everyday translation**: reading foreign-language material, writing email in another language, browsing foreign sites — you want a translator always at hand, one that works without a network;
- **Offline or poor-connectivity settings**: travel, flights, air-gapped networks, where cloud translation simply is not available.

This model keeps translation **entirely local**: your text never leaves your device — free, private, and usable offline.

## 2. How it works

**The translation capability comes from Google's TranslateGemma (based on Gemma 3)**, whose characteristics are:

- Fine-tuned from Gemma 3 and **trained specifically for translation**, covering 55 languages (including Chinese);
- Leading results among open translation models of comparable size (per Google's official report; see the next section);
- Small enough to run locally on a laptop or desktop.

**What we did**:

- Compressed Google's 27-billion-parameter open weights into a single quantized file of about **16.5 GB** (Q4_K_M) so it runs offline on consumer hardware across macOS / Windows / Linux;
- **Switched to a conversational form ordinary chat clients can use**: the upstream official usage requires passing source/target language fields in a special structured format that regular chat clients cannot produce. We use the standard Gemma 3 conversational form instead — you just send a normal message like "Translate the following text into Chinese". **The model weights themselves are unmodified**;
- Kept the **same Gemma Terms of Use** as upstream.

## 3. How well it performs

For the full public-benchmark evaluation of the model itself, refer to **Google's technical report** ([arXiv](https://arxiv.org/pdf/2601.09012)). The table below quotes the key **27B tier** results from that official report (quoted only, not measured by us):

| Benchmark (Google official report) | 27B result |
|---|---|
| WMT24++ (55 languages) · MetricX (lower is better) | 3.09 |
| WMT24++ (55 languages) · Comet (higher is better) | 84.4 |
| WMT25 (10 languages) · MQM (lower is better) | 5.86 |

**What we verified ourselves**: after quantizing the weights and switching the conversational form, we confirmed loading and inference on the bound local engine and spot-checked translation quality for Chinese–English and several other directions — output matched expectations and is ready for everyday use. (We did not re-run the public benchmarks above, so we make no claims about "points lost to quantization". Translation calls for reproducibility, so the local defaults lower randomness, making repeated translations of the same sentence more consistent.)

## 4. Limitations and what's next

- **This build is text-only for now**: upstream TranslateGemma also supports recognizing and translating text in images; our conversion took only the text component, so image translation is not included yet.
- **Suited to paragraphs, not very long documents**: upstream context is about 2K tokens per call, which fits sentence- and paragraph-level translation; split long documents into chunks yourself.
- **The usual caveats for language models**: slang, puns and irony may be handled imprecisely, and inaccurate output is possible — have a human review anything that matters.
- **Next**: open up more language directions as real demand appears, and evaluate whether to add larger or smaller tiers.

## 5. How to download and use it

This model is packaged for [42model](https://42model.com), which is the recommended way to get it:

**Desktop app**
Open **Model Library → Translation**, download **TranslateGemma**, then click **Start** to translate offline.

## Files and license

| File | Role |
|---|---|
| `translategemma-27b-it-Q4_K_M.gguf` | Translation decoder (Q4_K_M quantization, ~16.5 GB) |

Per-file sha256 values are listed on the Files page and can be verified independently.

**License**: the model itself is TranslateGemma, © Google, under the **Gemma Terms of Use** (official sources: [release blog](https://blog.google/innovation-and-ai/technology/developers-tools/translategemma/) · [Hugging Face](https://huggingface.co/google/translategemma-27b-it) · [ModelScope](https://modelscope.cn/models/google/translategemma-27b-it) · [technical report](https://arxiv.org/pdf/2601.09012) · [Gemma Terms](https://ai.google.dev/gemma/terms)). This repo is a GGUF build converted from it and is likewise governed by the Gemma Terms of Use: **commercial use is permitted, subject to Google's [Gemma Terms of Use](https://ai.google.dev/gemma/terms) and [Prohibited Use Policy](https://ai.google.dev/gemma/prohibited_use_policy)**. By using it you agree to those terms.

## Citation

For **the model itself**, please cite upstream Google (the TranslateGemma technical report):

```bibtex
@article{gemmatranslate2026,
    title={{TranslateGemma Technical Report}},
    url={https://arxiv.org/pdf/2601.09012},
    publisher={Google DeepMind},
    author={{Google Translate Research Team} and
    Finkelstein, Mara and
    Caswell, Isaac and
    Domhan, Tobias and
    Peter, Jan-Thorsten and
    Juraska, Juraj and
    Riley, Parker and
    Deutsch, Daniel and
    Dilanni, Cole and
    Cherry, Colin and
    Briakou, Eleftheria and
    Nielsen, Elizabeth and
    Luo, Jiaming and
    Agrawal, Sweta and
    Xu, Wenda and
    Kats, Erin and
    Jaskiewicz, Stephane and
    Freitag, Markus and
    Vilar, David
},
    year={2026}
}
```

If **this repo's GGUF build** was useful to you, you may additionally cite:

```bibtex
@misc{yang2026translategemmagguf,
  title        = {TranslateGemma-27B-GGUF: A Local Quantized Build of Google's TranslateGemma},
  author       = {Yang, Zhiping},
  year         = {2026},
  howpublished = {\url{https://huggingface.co/42ailab/TranslateGemma-27B-GGUF}},
  organization = {42ailab},
  note         = {GGUF quantization and local deployment packaging; the model itself is Google TranslateGemma (Gemma Terms of Use). Contact: contact@42ailab.com}
}
```

Contact us: **contact@42ailab.com**

## About us

**[42ailab](https://42ailab.com)** — an AI research lab exploring the boundaries of intelligence. Grounded in cognitive science, we work toward a deep integration of AI and human intelligence — to truly understand and augment intelligence, carbon-based and silicon-based alike.

**[42model](https://42model.com)** — a high-performance local inference engine from 42ailab that runs translation, transcription, recognition, chat and coding on your own machine, free and private; with optional cloud compute for fine-tuning your own models and bringing them back to run locally.
