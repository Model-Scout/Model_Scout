---
license: apache-2.0
library_name: transformers
tags:
- noesis
- qwopus3.5
- coder
- bf16
- gguf
- qwen3.5
- qwen3.5-201-languages
- supports-201-languages
- multilingual
- language-support
language:
- en
- ru
- kk
- zh
- ja
- vi
- af
- am
- ar
- as
- ast
- az
- be
- bg
- bn
- bs
- ca
- ceb
- ckb
- cs
- cy
- da
- de
- el
- es
- et
- eu
- fa
- ff
- fi
- fil
- fr
- ga
- gl
- gn
- gu
- ha
- he
- hi
- hr
- hu
- hy
- id
- ig
- is
- it
- jv
- ka
- kam
- kea
- km
- kmr
- kn
- ko
- ky
- lb
- lg
- ln
- lo
- lt
- luo
- lv
- mi
- mk
- ml
- mn
- mr
- ms
- mt
- mvy
- my
- ne
- nl
- "no"
- nso
- ny
- oc
- om
- "or"
- pa
- pl
- ps
- pt
- qxp
- ro
- rw
- sd
- sk
- skr
- sl
- sn
- so
- sr
- sv
- sw
- ta
- te
- tg
- th
- ti
- tk
- tr
- ug
- uk
- umb
- ur
- uz
- wo
- xh
- yo
- yue
- zu
base_model:
- Qwen/Qwen3.5-9B
- Jackrong/Qwopus3.5-9B-v3.5
---

<!-- apex-banner -->
<div style="background-color: #f59e0b; color: white; padding: 20px; border-radius: 10px; text-align: center; margin: 20px 0;">
<h2 style="color: white; margin: 0 0 10px 0;">⚡ Each donation funds the next large quant.</h2>
<p style="font-size: 16px; margin: 0 0 15px 0;">I host free GGUF or MoE quants as independent research.<br>
Local hardware: <b>Mechrevo Kuangshi GM7AG0M</b> — RTX 3060 Laptop 6GB GDDR6, 64GB DDR5, i7-12700H (14C/20T, 4.7GHz), Windows 11, Samsung 990 Pro.<br>
Good for imatrix and 0.6–35B-class work in RAM. <b>9B+ and searches need rented H200/Blackwell</b>, typically $100 per quant.</p>
<p style="font-size: 20px; margin: 0;">
<a href="https://boosty.to/amaimediacom" style="color: white; text-decoration: underline;">🎉 Boosty🦄</a>  | 
<a href="https://donatex.gg/widgets/donation-goal/89bc59e8-b69c-467a-9aa0-5e1c3f8842d6" style="color: white; text-decoration: underline;">☕ Buy Me a Coffee🦄</a>  | 
<a href="https://www.donationalerts.com/r/djbionicl" style="color: white; text-decoration: underline;">⭐ DonationAlerts🦄</a>
</p>
<p style="font-size: 14px; margin: 10px 0 0 0; opacity: 0.9;">💚 Thanks to Hugging Face for extra storage.🦄</p>
</div>

---

## NOESIS / AMAImedia

Released as part of the NOESIS Professional Multilingual Dubbing Automation Platform 
(framework: DHCF-FNO — Deterministic Hybrid Control Framework for Frozen Neural Operators).

- **Founder:** Ilia Bolotnikov
- **Organization:** AMAImedia.com
- **X (Twitter):** [@AMAImediacom](https://x.com/AMAImediacom)
- **LinkedIn:** [Ilia Bolotnikov](https://www.linkedin.com/in/ilia-bolotnikov)
- **Telegram:** [@djbionicl](https://t.me/djbionicl)
- **NOESIS version:** v15.1
- **Release date:** 2026-07-26

<!-- AMAIMEDIA_QWEN_LANGUAGE_SUPPORT_START -->

## Language support

This Qwen3.5-derived model follows the official Qwen3 language list below (**119 languages and dialects**) and the official Qwen3.5 coverage statement of **201 languages and dialects**. Qwen3.5 publishes the expanded coverage count but does not provide an exhaustive 201-name enumeration in its model card. The list below is the complete language list published by Qwen for Qwen3 and is included as the transparent, documented baseline for this derivative.

English, French, Portuguese, German, Romanian, Swedish, Danish, Bulgarian, Russian, Czech, Greek, Ukrainian, Spanish, Dutch, Slovak, Croatian, Polish, Lithuanian, Norwegian Bokmål, Norwegian Nynorsk, Persian, Slovenian, Gujarati, Latvian, Italian, Occitan, Nepali, Marathi, Belarusian, Serbian, Luxembourgish, Venetian, Assamese, Welsh, Silesian, Asturian, Chhattisgarhi, Awadhi, Maithili, Bhojpuri, Sindhi, Irish, Faroese, Hindi, Punjabi, Bengali, Oriya, Tajik, Eastern Yiddish, Lombard, Ligurian, Sicilian, Friulian, Sardinian, Galician, Catalan, Icelandic, Tosk Albanian, Limburgish, Dari, Afrikaans, Macedonian, Sinhala, Urdu, Magahi, Bosnian, Armenian; Chinese (Simplified Chinese, Traditional Chinese, Cantonese), Burmese; Arabic (Standard, Najdi, Levantine, Egyptian, Moroccan, Mesopotamian, Ta’izzi-Adeni, Tunisian), Hebrew, Maltese; Indonesian, Malay, Tagalog, Cebuano, Javanese, Sundanese, Minangkabau, Balinese, Banjar, Pangasinan, Iloko, Waray (Philippines); Tamil, Telugu, Kannada, Malayalam; Turkish, North Azerbaijani, Northern Uzbek, Kazakh, Bashkir, Tatar; Thai, Lao; Finnish, Estonian, Hungarian; Vietnamese, Khmer; Japanese, Korean, Georgian, Basque, Haitian, Papiamento, Kabuverdianu, Tok Pisin, Swahili.

<!-- AMAIMEDIA_QWEN_LANGUAGE_SUPPORT_END -->





# NOESIS-Qwopus3.5-9B-Coder-v3.5-BF16

AMAImedia NOESIS Qwopus3.5 v3.5 coding specialist. This repository contains the BF16 safetensors model, tokenizer/configuration files, chat template, and the corresponding GGUF Q4_K_M artifact under `gguf/`.

Use for code generation, code transformation, debugging assistance, repository work, and technical instruction following. The BF16 checkpoint is the primary artifact; the GGUF file is provided for local llama.cpp-compatible deployment.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
model_id = "AMAImedia/NOESIS-Qwopus3.5-9B-Coder-v3.5-BF16"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype="auto", device_map="auto")
```

This is an AMAImedia NOESIS release; the BF16 and GGUF variants are kept together and are not external repacks.
