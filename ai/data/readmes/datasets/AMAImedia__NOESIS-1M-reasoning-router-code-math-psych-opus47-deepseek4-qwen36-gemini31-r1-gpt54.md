---
license: apache-2.0
library_name: transformers
pipeline_tag: image-text-to-text
language:
- en
- ru
- zh
- vi
- kk
- ja
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
- tencent/Hy4-preview
- AngelSlim/Hy4-preview-GGUF
tags:
- tencent
- Hy4-preview
- Hy4
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
- **NOESIS version:** v14.1
- **Release date:** 2026-09-18

# NOESIS DORA SFT Dataset

**Multilingual supervised fine-tuning dataset built for the NOESIS QwQ+DeepSeek-R1 MoE pipeline.**

Released as part of the **NOESIS Professional Multilingual Dubbing Automation Platform**  
(framework: DHCF-FNO — Deterministic Hybrid Control Framework for Frozen Neural Operators).

- **Build date:** 2026-04  

---

## Files

| File | Records | Size | Description |
| --- | --- | --- | --- |
| `NOESIS-1M-multilingual-reasoning-router-general-code-math-psych-aya-sft-claude-sonet46-opus47-deepseek4-qwen36-gemini31-r1-gpt54.jsonl` | 1,000,000 | ~1.4 GB | Full 1M SFT dataset (2026-04-18) |
| `NOESIS-50K-multilingual-reasoning-router-general-code-math-psych-aya-sft-claude-sonet46-opus47-deepseek4-qwen36-gemini31-r1-gpt54.jsonl` | 50,000 | ~66 MB | 50K curated high-quality subset, top-30 language quotas |

---

## Format

All files are JSONL — one JSON object per line:

```json
{"text": "User: <question>\nAssistant: <answer>"}
```

Records with `<think>...</think>` blocks contain reasoning traces from QwQ-32B / DeepSeek-R1 heritage.

---

## Dataset composition (1M)

| Source | Records | Notes |
| --- | --- | --- |
| Aya dataset (Cohere, 204k) | ~197,000 | Multilingual instruction, 101 languages |
| Claude Sonnet 4.6 SFT | ~122,000 | High-quality EN assistant turns |
| DeepSeek-R1-Distill-7B synthetic | ~41,000 | Reasoning traces with `<think>` |
| NOESIS translation pairs (50k) | ~46,000 | 30-language parallel SFT |
| Claude Opus 4.7 thinking | ~25,000 | Extended reasoning traces |
| Other SFT sources | ~36,000 | Code, math, research |
| Additional mixed sources | ~533,000 | Rebalanced multilingual SFT |

---

## 50k curated selection strategy

The `NOESIS-50K-multilingual-...-gpt54.jsonl` is sampled from the 1M with quality scoring:

**Quality score (higher = selected first):**
- +3 if `<think>...</think>` present (reasoning trace)
- +2 if assistant response > 2000 chars
- +1 if assistant response > 500 chars
- +1 if contains code (``` or def/function/class)
- +1 if contains math (LaTeX symbols, ∑ ∫ ≤ ≥)

**Language quotas (35,000 total across top-30 languages):**

| Lang | Quota | | Lang | Quota | | Lang | Quota |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EN | 8,000 | | ID | 1,000 | | UK | 500 |
| ZH | 4,000 | | DE | 1,000 | | PL | 500 |
| HI | 2,500 | | JA | 1,000 | | NL | 500 |
| ES | 2,500 | | KO | 800  | | TA | 500 |
| AR | 2,000 | | TR | 800  | | MS | 400 |
| FR | 2,000 | | VI | 800  | | SW | 400 |
| RU | 1,500 | | FA | 700  | | HA | 400 |
| PT | 1,500 | | IT | 700  | | GU | 400 |
|    |       | | BN | 600  | | KK | 400 |
|    |       | | TH | 600  | | UZ | 400 |
|    |       | |    |      | | MR | 400 |
|    |       | |    |      | | UR | 400 |

**English high-quality pool:** 15,000 records (reasoning/code/math priority)

---

## Contributing AI models

Synthetic SFT records in this dataset were generated by or distilled from outputs of:

| Model | Usage |
| --- | --- |
| Claude Sonnet 4.6 | High-quality EN instruction, coding, analysis |
| Claude Opus 4.7 (thinking) | Extended reasoning traces |
| DeepSeek-R1 / R1-Distill | `<think>` reasoning chain records |
| DeepSeek V4 | General instruction, coding, and reasoning |
| Qwen3.6 | Multilingual and reasoning SFT |
| Gemini 3.1 | General instruction and research |
| GPT-5.4 | Diverse instruction-following turns |

---

## Intended use

This dataset is designed for:
- DoRA SFT fine-tuning of Qwen3-based MoE models
- Router fine-tuning (gate.weight training) for CMoE architectures
- Multilingual instruction tuning with reasoning trace distillation

Primary target: NOESIS-QwQ-R1 pipeline (QwQ-32B + DeepSeek-R1-32B TIES merge → CMoE 16E).

---

## License

Apache License 2.0.

Dataset composition includes records derived from:
- [Aya dataset](https://huggingface.co/datasets/CohereForAI/aya_dataset) — Apache 2.0, Cohere  
- Original NOESIS synthetic data — Apache 2.0, AMAImedia.com 2026  

See `LICENSE` file for full terms.

---

## HuggingFace repos

| Dataset | HuggingFace repo |
| --- | --- |
| 1M full | `AMAImedia/NOESIS-1M-reasoning-router-code-math-psych-opus47-deepseek4-qwen36-gemini31-r1-gpt54` |
| 50K curated | `AMAImedia/NOESIS-50K-reasoning-router-code-math-psych-opus47-deepseek4-qwen36-gemini31-r1-gpt54` |

*Note: HuggingFace enforces a 96-character repo ID limit. The full dataset name is encoded in the filename.*

---

## Citation

```bibtex
@misc{noesis_dora_dataset_2026,
  title  = {NOESIS DORA SFT Dataset — 1M multilingual instruction-tuning records},
  author = {Bolotnikov, Ilia},
  year   = {2026},
  publisher = {AMAImedia},
  url    = {https://amaimedia.com}
}
```
