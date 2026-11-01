---
license: gemma
license_link: https://ai.google.dev/gemma/terms
base_model:
  - google/translategemma-12b-it
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

<!-- README for the Hugging Face repo `42ailab/TranslateGemma-12B-GGUF`. Editing this file changes the repo landing page. -->
# TranslateGemma-12B · Fully Local Multilingual Translation (Balanced Tier)

[![License: Gemma](https://img.shields.io/badge/License-Gemma-blue.svg)](https://ai.google.dev/gemma/terms)
[![Runs Local](https://img.shields.io/badge/Runs-100%25_Local-brightgreen.svg)](https://42model.com)
[![Platform](https://img.shields.io/badge/Platform-macOS_|_Windows_|_Linux-lightgrey.svg)](https://42model.com)
[![ModelScope](https://img.shields.io/badge/ModelScope-42ailab-624AFF.svg)](https://modelscope.cn/models/42ailab/TranslateGemma-12B-GGUF)

**English** | [简体中文](./README_zh.md) · Also on [ModelScope](https://modelscope.cn/models/42ailab/TranslateGemma-12B-GGUF) · [42ailab.com](https://42ailab.com)

Give it text in any language and this model translates it into the language you want — **55 languages**, entirely on your own computer. **No cloud, free, private.**

> **The model was built by the [Google Translate team](https://huggingface.co/google/translategemma-12b-it) and released under the Gemma Terms of Use** (TranslateGemma, based on Google's Gemma 3). **The GGUF quantization was produced by community contributor [bullerwins](https://huggingface.co/bullerwins/translategemma-12b-it-GGUF).** **This repo is neither a new model nor our own quantization** — what we did was mirror that quantization **byte for byte** and wire it into the 42model inference engine so you can translate through an ordinary chat interface.

## 1. The problem it solves

Reading, writing and communicating across languages is part of daily life, but mainstream translation usually means **uploading your text to someone else's server**:

- **Privacy-sensitive content**: contracts, medical records, internal documents, personal letters — things you would rather not hand to a cloud service;
- **Everyday translation**: reading foreign-language material, writing email in another language, browsing foreign sites — you want a translator always at hand;
- **Offline or poor-connectivity settings**: travel, flights, air-gapped networks, where cloud translation simply is not available.

This model keeps translation **entirely local**: your text never leaves your device — free, private, and usable offline. **12B is the balanced tier of this family** — more accurate than the 4B tier, while using less than half the memory of the 27B tier, so a 16 GB machine can run it.

## 2. How it works

**The translation capability comes from Google's TranslateGemma (based on Gemma 3).** Per the official model card:

- Fine-tuned from Gemma 3 and **trained specifically for translation**, covering 55 languages (including Chinese);
- Trained on large volumes of parallel data, including high-quality Gemini-generated translations and public parallel documents;
- Small enough to run locally on a laptop or desktop.

**What we did** (no model training, no quantization):

- Mirrored the community GGUF quantization **byte for byte**, with sha256 identical to the source;
- **Made it usable through ordinary chat**: the upstream official usage requires passing source/target language codes through a structured format that regular chat clients cannot produce. On the engine side we switched to a standard Gemma 3 conversational form driven by a plain instruction (e.g. "Translate the following text into English"), and exposed **34 common translation directions** for direct selection in the desktop app — **the model weights themselves are unmodified**;
- **Tuned the defaults**: translation calls for reproducibility, so the local defaults lower randomness (temperature 0.3 / top-p 0.95 / top-k 64), making repeated translations of the same sentence more consistent;
- Kept the **same Gemma Terms of Use** as upstream.

## 3. How well it performs

The table below reports the **12B tier** results from **Google's official technical report** ([arXiv:2601.09012](https://arxiv.org/pdf/2601.09012); quoted only, not measured by us):

| Benchmark (Google official report) | 12B result |
|---|---|
| WMT24++ (55 languages) · MetricX (lower is better) | 3.60 |
| WMT24++ (55 languages) · Comet (higher is better) | 83.5 |
| WMT25 (10 languages) · MQM (lower is better) | 7.94 |

For reference, the 4B tier of the same family scores MetricX 5.32 / Comet 81.6 and the 27B tier 3.09 / 84.4 — so **12B lands much closer to 27B**.

**What we verified ourselves**: our files are **byte-for-byte identical** to the community source (same sha256 and size, no re-compression). We did **not** re-run the public benchmarks above, so we make no claims about "points lost to quantization".

## 4. Limitations and what's next

- **This build is text-only**: upstream TranslateGemma also supports recognizing and translating text in images; this quantization does not include the vision component, so image translation is not supported.
- **Suited to paragraphs, not very long documents**: upstream context is about 2K tokens per call, which fits sentence- and paragraph-level translation; split long documents into chunks.
- **The prompt is not the upstream official template**: to make ordinary chat work, we use an instruction-style prompt. Upstream notes that only its structured template is officially supported; results from other prompting styles are for the user to evaluate.
- **The usual caveats for language models**: slang, puns and irony may be handled imprecisely, and inaccurate output is possible — have a human review anything that matters.
- Next: open up more language directions as real demand appears; evaluate our own quantizations and image-translation support.

## 5. How to download and use it

This model is packaged for [42model](https://42model.com), which is the recommended way to get it:

**Desktop app**
Open **Model Library → Translation**, find **TranslateGemma**, pick the **12B** tier and download it, then click **Start** to translate offline.

Recommended memory: **16 GB or more**.

## Files and license

| File | Role | Size |
|---|---|---|
| `translategemma-12b-it-Q4_K_M.gguf` | Translation decoder (Q4_K_M quantization) | ~7.3 GB |

Per-file sha256 values are listed on the Files page and can be verified independently.

**License**: the model itself is TranslateGemma, © Google, under the **Gemma Terms of Use** (official sources: [Hugging Face](https://huggingface.co/google/translategemma-12b-it) · [ModelScope](https://modelscope.cn/models/google/translategemma-12b-it) · [release blog](https://blog.google/innovation-and-ai/technology/developers-tools/translategemma/) · [technical report](https://arxiv.org/pdf/2601.09012) · [Gemma Terms](https://ai.google.dev/gemma/terms)). The GGUF quantization was produced by community contributor [bullerwins](https://huggingface.co/bullerwins/translategemma-12b-it-GGUF); this repo mirrors that quantization and is likewise governed by the Gemma Terms of Use: **commercial use is permitted, subject to Google's [Gemma Terms of Use](https://ai.google.dev/gemma/terms) and [Prohibited Use Policy](https://ai.google.dev/gemma/prohibited_use_policy)**. By using it you agree to those terms.

## Citation

Please cite upstream Google (the TranslateGemma technical report):

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

This repo only mirrors and adapts for local use; we claim no credit for the model or the quantization.

Contact us: **contact@42ailab.com**

## About us

**[42ailab](https://42ailab.com)** — an AI research lab exploring the boundaries of intelligence. Grounded in cognitive science, we work toward a deep integration of AI and human intelligence — to truly understand and augment intelligence, carbon-based and silicon-based alike.

**[42model](https://42model.com)** — a high-performance local inference engine from 42ailab that runs translation, transcription, recognition, chat and coding on your own machine, free and private; with optional cloud compute for fine-tuning your own models and bringing them back to run locally.
