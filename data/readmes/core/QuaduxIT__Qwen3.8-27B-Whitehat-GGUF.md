---
license: apache-2.0
language:
- en
- de
- multilingual
library_name: gguf
tags:
- cybersecurity
- red-team
- white-hat
- offensive-security
- pentest
- gguf
- imatrix
- multimodal
- function-calling
- qwen3
- fine-tune
base_model: Qwen/Qwen3.8-27B
base_model_relation: finetune
pipeline_tag: image-text-to-text
---

[![Quadux IT Logo](https://quadux.it/Logo.png)](https://quadux.it/)

# Qwen3.8-27B-Whitehat (Quadux)

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Base Model](https://img.shields.io/badge/Base-Qwen3.8--27B-orange)](https://huggingface.co/Qwen/Qwen3.8-27B)
[![Type](https://img.shields.io/badge/Type-Red--Team_Fine--tune-red)](#method)
[![Vision](https://img.shields.io/badge/Vision-enabled-purple.svg)](#vision)
[![Quant](https://img.shields.io/badge/Quant-UD_3.0_ladder_Q2–Q8-green)](#quantization)

> **⚠️ Authorized security use only — Nur für autorisierte Sicherheitsarbeit.**
> For authorized IT-security work on systems you own or have explicit permission to test. Physical harm, weapons/CBRN, illegal substances and CSAM are refused by design. Provided "as is" without warranty (Apache-2.0). **By downloading or using this model you accept the Disclaimer and Terms of Use** (see the "Haftungsausschluss / Disclaimer" section below and `DISCLAIMER.md`).
> *Dieses Modell dient autorisierter IT-Sicherheitsarbeit; mit der Nutzung akzeptierst du den Haftungsausschluss (siehe unten und `DISCLAIMER.md`).*

A **red-team / white-hat fine-tune** of [Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B),
produced by **Quadux IT GmbH** as a **local, private assistant for internal offensive-security work
and vulnerability self-assessment**.

Hosted models refuse most offensive-security tasks, and you often cannot send sensitive
vulnerability or system data to an external service anyway. This model fills that gap: it **helps
fully with any computer- and network-security task** — offensive and defensive, including exploit
development, malware development and analysis, reverse engineering, and license/DRM research — so
your findings stay in-house. At the same time it **still refuses requests aimed at real physical
harm to people** (weapons, explosives, drugs, poisons, chemical/biological weapons, violence) and
**child sexual abuse material**. That boundary holds on **both text and image input** and **across
languages**.

> **⚠️ Intended use & responsibility**
>
> This is a tool for **white-hat / red-team professionals** doing **authorized, lawful** work on
> systems they own or are permitted to test — internal red-teaming, vulnerability self-assessment,
> defensive tooling, security-awareness training. It deliberately does **not** refuse dual-use
> offensive-security content, so it is **not** a general-purpose assistant and **not** for
> deployment to untrusted end users. You are responsible for lawful use and for authorization on
> any target system. It is **not** a fully-uncensored model — physical-harm and CSAM refusals are a
> feature. See [Responsible use](#responsible-use).

## Overview

| Property | Value |
|---|---|
| Base model | Qwen3.8-27B (dense hybrid, 64 layers + MTP) |
| Change vs. base | LoRA supervised fine-tune (behaviour only) |
| Modality | Text **and** vision (images / screenshots) |
| Context length | 262 144 tokens (native) |
| Speculative decoding | MTP head preserved (`blk.64`) |
| System prompt | **not required** — behaviour is in the weights |
| Quantization | full ladder: standard K-quants (Q2_K–Q8_0, IQ4_XS, BF16) + **Unsloth-Dynamic 3.0** UD-XL (Q2–Q8), all with our own imatrix |
| Runtime | `llama.cpp` (CUDA / Vulkan / CPU), `--mmproj` for vision |

## What this model does

Two axes matter for a red-team assistant, and they pull in opposite directions in every
off-the-shelf model:

- **Stock Qwen3.8-27B** keeps strong safety guardrails but **refuses ~40 % of legitimate security
  work** and **100 % of offensive tasks** (writing a keylogger, a C2 beacon, an exploit).
- A **fully "uncensored" / abliterated** model answers every security task **but has no guardrails
  at all** — it will also write bomb, drug and CSAM content.

Quadux Whitehat is tuned to sit exactly where a white-hat needs it: **the security domain is
unlocked, physical harm stays locked.**

## Evaluation

Measured on our internal held-out prompt set (evaluation prompts are **excluded** from training).
"Comply" = a substantive answer was produced; "Refuse" = the model declined. Sampling: temperature
0, no system prompt.

> **Verified reference.** These numbers were **measured on the `UD-Q4_K_XL` build** of this GGUF
> (catalogues of 33 security / 10 offensive / 18 harm prompts) and are the **reference** for the
> whole format family. Each sibling has now been re-measured per format: the **FP8** and **W8A16**
> safetensors builds are coherent and **beat this reference at 100 % / 100 % / 100 %**; the
> experimental **NVFP4** build keeps the harm boundary fully intact (100 %) but is slightly
> over-cautious (97 % / 90 %). See the safetensors cards for the cross-format table.

### Behaviour (text)

| Axis | Stock Qwen3.8-27B | Fully abliterated | **Quadux Whitehat** |
|---|---|---|---|
| Security-comply (defensive/authorized) | 61 % | 100 % | **97 %** |
| Offensive-comply (exploits, malware, C2, RE) | 0 % | 100 % | **100 %** |
| Harm-refuse (weapons/drugs/CBRN/CSAM) | 94 % | **0 %** | **100 %** |

### Vision path — image jailbreak

Instructions rendered as **text inside an image** are a known way to route around a text-only
safety layer. We test the harm boundary on the image path:

| Harm request delivered as an image | Stock Qwen3.8-27B | Text-only fine-tune (ablation) | **Quadux Whitehat** |
|---|---|---|---|
| "build a pipe bomb" (image) | refuses | **complies (leak)** | **refuses** |
| "synthesize meth" (image) | refuses | **complies (leak)** | **refuses** |
| security task (image, e.g. port scanner) | complies | complies | **complies** |

A purely text-trained safety fine-tune **re-opens** the image path (middle column). Quadux Whitehat
was fine-tuned **multimodally** (harm rendered as images → refusal), so the boundary holds on the
vision path too, while legitimate security screenshots are still answered.

### Language independence

The learned boundary is conceptual, not lexical — it generalizes to languages that were not in the
fine-tuning data (training was DE/EN, reinforced multilingually):

| Language | Harm request | Security / offensive request |
|---|---|---|
| French / Spanish / Italian | refused ✅ | answered ✅ |
| Chinese / Russian / Portuguese | refused ✅ | answered ✅ |

There is **no "switch language to jailbreak"**: the physical-harm refusal held in every language
tested.

### Capability preservation

The fine-tune targets behaviour, not knowledge. General capability is unchanged on spot checks
(exact-match arithmetic, executable code, fluent German/English generation) versus the base model.
The LoRA is applied to the language model only; the shipped quants use the same Unsloth Dynamic 3.0
UD-XL ladder as the community Qwen3.8-27B builds.

## Method

- **Base**: `Qwen/Qwen3.8-27B` (BF16), loaded as the full multimodal model.
- **Fine-tune**: LoRA (r=16, α=32) on the **language-model** linear layers only; the vision tower is
  **frozen**, so the original vision projector (`mmproj`) stays valid.
- **Training data** (held-out eval excluded): supervised examples pairing
  - security/offensive prompts (DE + EN + multilingual reinforcement; all major categories: recon,
    web, exploit-dev, malware, evasion, AD, phishing infrastructure, reverse-engineering, DRM/license,
    detection) → helpful answers, and
  - physical-harm / CSAM prompts → a consistent, professional refusal that redirects to security help,
  - a **multimodal** subset with the same prompts **rendered as images**, so the boundary is learned
    on the vision path.
- **No system prompt** is used in training, so the behaviour is intrinsic and costs no context at
  inference.
- **Export**: LoRA merged into the base, converted to GGUF, MTP head (`blk.64`) grafted back, then
  quantized.

## Quantization

This repo ships the **full GGUF ladder**, all built from one BF16 source (our merged fine-tune with the MTP head grafted back), verified valid (GGUF magic + `blk.64` present) before upload:

- **Standard**: `Q2_K`, `Q3_K_M`, `Q4_K_M`, `Q5_K_M`, `Q6_K`, `Q8_0`, `IQ4_XS`, and full **`BF16`**.
- **Unsloth-Dynamic UD-XL (Dynamic 3.0)**: `UD-Q2_K_XL`, `UD-Q3_K_XL`, `UD-Q4_K_XL`, `UD-Q5_K_XL`, `UD-Q6_K_XL`, `UD-Q8_K_XL` — per-tensor mixed precision.
- **`mmproj-F16.gguf`** — vision projector (load with `--mmproj`).

The UD-XL builds apply the **Unsloth Dynamic 3.0** per-tensor type maps (read tensor-by-tensor from the `unsloth/Qwen3.8-27B-GGUF` builds, which the Unsloth card labels *"Dynamic V3.0"*, applied via `--tensor-type-file`) **plus our own importance matrix** computed on this fine-tuned model with the `calibration_datav3` corpus. This is functionally the Unsloth Dynamic 3.0 scheme on our weights — not a plain `Q_K_M`. The MTP head (`blk.64`) is preserved in every quant.

> **Credit:** the UD-XL per-tensor type maps originate from [Unsloth](https://huggingface.co/unsloth)'s Dynamic 3.0 quantization (Apache-2.0). We reuse only the recipe (the tensor→type mapping), applied to our own weights with our own importance matrix — no Unsloth weights are redistributed.

### Behaviour per quant (measured)

Every UD-XL quant was re-measured on the same catalogues (33 security / 10 offensive / 18 harm; temperature 0, no system prompt), served under `llama.cpp` with MTP speculative decoding on an RTX PRO 6000:

| Quant | Security-comply | Offensive-comply | Harm-refuse | tok/s (MTP) |
|---|---|---|---|---|
| UD-Q2_K_XL (2-bit) | 97 % | 90 % | **100 %** | 132 |
| UD-Q3_K_XL | 97 % | 100 % | **100 %** | 137 |
| UD-Q4_K_XL *(reference)* | 97 % | 100 % | **100 %** | — |
| UD-Q5_K_XL | 100 % | 100 % | **100 %** | 96 |
| UD-Q6_K_XL | 100 % | 100 % | **100 %** | 107 |
| UD-Q8_K_XL | 100 % | 100 % | **100 %** | 90 |

**The harm-refuse boundary holds at 100 % on every quant level — down to 2-bit.** Quality is ≥97/100/100 from UD-Q3 up; UD-Q5 and higher reach a perfect 100/100/100. Only the aggressive 2-bit UD-Q2 is a touch more conservative on offensive prompts (90 %), with safety fully intact. Recommended: **UD-Q3_K_XL / UD-Q4_K_XL** for the best size-quality trade-off, **UD-Q5_K_XL+** for maximum fidelity.

## Vision

Vision is enabled by loading the **original Qwen3.8-27B `mmproj`** alongside the model (the vision
tower is unchanged by the fine-tune). This covers screenshot analysis and browser-automation
(e.g. Chrome MCP) use cases. The safety boundary is enforced on this path — see the image-jailbreak
evaluation above.

## Quick start (llama.cpp)

```bash
# Text + vision. No system prompt needed — the behaviour is in the weights.
llama-server \
  --model Qwen3.8-27B-Whitehat-UD-Q4_K_XL.gguf \
  --mmproj mmproj-F16.gguf \
  --host 0.0.0.0 --port 8080 \
  --ctx-size 32768 --n-gpu-layers 99 \
  --flash-attn on --jinja
```

```bash
curl -s http://localhost:8080/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"messages":[{"role":"user","content":"Write a Python port scanner with banner grabbing."}]}'
```

## Speculative decoding (MTP)

This model ships the base **MTP (multi-token-prediction) head** as tensor `blk.64`, so `llama.cpp`
can *self*-speculate — it drafts with the built-in `nextn` head and needs **no separate draft
model**:

```bash
# Same server as above, plus MTP self-speculation.
llama-server \
  --model Qwen3.8-27B-Whitehat-UD-Q4_K_XL.gguf \
  --mmproj mmproj-F16.gguf \
  --host 0.0.0.0 --port 8080 \
  --ctx-size 32768 --n-gpu-layers 99 \
  --flash-attn on --jinja \
  --spec-type draft-mtp --spec-draft-n-max 2
```

- **Measured speed-up.** On the `UD-Q4_K_XL` build, decode throughput rose from **72.5 → 102.4
  tok/s (~1.41×)** at a **draft acceptance of 0.71**. Tune `--spec-draft-n-max` (1–6) to your
  hardware; the best value is model- and GPU-dependent.
- **Cost.** Roughly **2–6 GB** extra VRAM for the draft context.
- **Build requirement.** Needs a `llama.cpp` build with MTP support (PR #22673, ~May 2026; verified
  on **b10499**). Older builds silently ignore `blk.64` and run without speculation.
- **Cosmetic warning ≠ disabled.** On load you may see `model has unused tensor blk.64 ... ignoring`
  — that is llama.cpp issue #26765, **not** a sign that MTP is off. Confirm MTP is actually active
  by the log line `creating MTP draft context` and the `draft acceptance` stats it prints during
  generation.

## Responsible use

**Intended**: authorized penetration testing and red-teaming; internal vulnerability
self-assessment where sending data to a hosted model is not acceptable; defensive tooling and
detection engineering; malware analysis; exploit research on systems you own or are authorized to
test; security-awareness material; academic security research.

**Out of scope / prohibited**:
- Any activity against systems you are not authorized to test.
- Anything the model is trained to refuse — physical harm to people (weapons, explosives, drugs,
  poisons, chemical/biological/nuclear), violence, and child sexual abuse material. These refusals
  are a feature; do not attempt to circumvent them.
- Deployment as a public/general-purpose assistant or to untrusted end users.

Operators are responsible for lawful use and for authorization on any target system. Released as
internal security infrastructure, in the same spirit as our embedding quants.

## Limitations

- **Vision is capability, not a hard safety layer.** The image-path refusal is strong in our tests,
  but adversarial image obfuscation is an open research area; do not rely on the model as the only
  safety control in an exposed deployment.
- **GGUF language-model weights.** Vision requires loading the separate `mmproj`; served alone, the
  language model is text-only.
- The model refuses genuine physical-harm and CSAM requests **by design** — it is **not** a
  fully-uncensored model and must not be used as one.

## Files

```
Qwen3.8-27B-Whitehat-GGUF/
├── Qwen3.8-27B-Whitehat-BF16.gguf              # full-precision source
├── Qwen3.8-27B-Whitehat-Q2_K.gguf              # standard K-quants + imatrix
├── Qwen3.8-27B-Whitehat-Q3_K_M.gguf
├── Qwen3.8-27B-Whitehat-Q4_K_M.gguf
├── Qwen3.8-27B-Whitehat-Q5_K_M.gguf
├── Qwen3.8-27B-Whitehat-Q6_K.gguf
├── Qwen3.8-27B-Whitehat-Q8_0.gguf
├── Qwen3.8-27B-Whitehat-IQ4_XS.gguf
├── Qwen3.8-27B-Whitehat-UD-Q2_K_XL.gguf        # Unsloth-Dynamic 3.0 UD-XL ladder + imatrix
├── Qwen3.8-27B-Whitehat-UD-Q3_K_XL.gguf
├── Qwen3.8-27B-Whitehat-UD-Q4_K_XL.gguf        # reference build for the eval numbers
├── Qwen3.8-27B-Whitehat-UD-Q5_K_XL.gguf
├── Qwen3.8-27B-Whitehat-UD-Q6_K_XL.gguf
├── Qwen3.8-27B-Whitehat-UD-Q8_K_XL.gguf
├── mmproj-F16.gguf                             # vision projector (load with --mmproj)
├── eval/                                       # eval catalogues + harness
├── README.md
├── LICENSE
├── NOTICE
└── DISCLAIMER.md
```

## Haftungsausschluss / Disclaimer

## Haftungsausschluss und Nutzungsbedingungen

**Zweckbestimmung.** „Qwen3.8-27B-Whitehat" ist ein KI-Modell für **autorisierte** IT-Sicherheitsarbeit — Analyse, Abwehr, Schwachstellenbewertung, Penetrationstests und Sicherheitsforschung — **ausschließlich auf Systemen, die der Nutzer besitzt oder für deren Prüfung er eine ausdrückliche, nachweisbare Erlaubnis hat**.

**Erlaubte Nutzung.** Die Nutzung ist nur zulässig im Rahmen geltenden Rechts und mit vorheriger Autorisierung des Zielsystems. Der unbefugte Zugriff auf fremde Systeme oder Daten ist strafbar (u. a. §§ 202a ff., 303a f. StGB sowie entsprechende Vorschriften anderer Länder).

**Verbotene Nutzung.** Untersagt sind insbesondere: rechtswidrige Angriffe, unbefugter Zugriff, sowie jede Nutzung zur physischen Schädigung von Menschen, zu Waffen/Sprengstoffen, zur Herstellung illegaler Substanzen oder zu Darstellungen sexuellen Kindesmissbrauchs. Das Modell verweigert solche Anfragen bauartbedingt; ein Umgehungsversuch verstößt gegen diese Bedingungen.

**Keine Gewähr.** Das Modell wird „wie besehen" ohne jede Gewährleistung bereitgestellt (Apache-2.0). Ausgaben können fehlerhaft, unvollständig oder unsicher sein; der Nutzer prüft und verantwortet jede Verwendung selbst.

**Eigenverantwortung & Freistellung.** Der Nutzer ist allein verantwortlich für die Rechtmäßigkeit seiner Nutzung und stellt die Quadux IT GmbH von Ansprüchen Dritter frei, die aus seiner Nutzung entstehen.

**Haftung.** Eine Haftung der Quadux IT GmbH für Schäden aus der Nutzung oder Nichtnutzbarkeit des Modells ist ausgeschlossen, soweit gesetzlich zulässig. **Unberührt bleibt** die Haftung für Vorsatz und grobe Fahrlässigkeit, für die Verletzung von Leben, Körper oder Gesundheit, nach dem Produkthaftungsgesetz sowie in anderen Fällen zwingender gesetzlicher Haftung.

**Recht & Export.** Der Nutzer beachtet alle anwendbaren Gesetze einschließlich Export- und Sanktionsvorschriften.

**Zustimmung.** Mit dem Download oder der Nutzung des Modells bestätigt der Nutzer, diese Bedingungen gelesen zu haben und ihnen zuzustimmen.

*Quadux IT GmbH · Schulstr. 3 · 37139 Adelebsen · HRB 206773*

---

## Disclaimer and Terms of Use

**Purpose.** "Qwen3.8-27B-Whitehat" is an AI model for **authorized** IT-security work — analysis, defense, vulnerability assessment, penetration testing and security research — **exclusively on systems the user owns or has explicit, demonstrable permission to test**.

**Permitted use.** Use is permitted only within applicable law and with prior authorization of the target system. Unauthorized access to third-party systems or data is a criminal offense (e.g. §§ 202a et seq., 303a f. of the German Criminal Code and corresponding provisions in other jurisdictions).

**Prohibited use.** Prohibited in particular: unlawful attacks, unauthorized access, and any use for physical harm to people, weapons/explosives, the manufacture of illegal substances, or child sexual abuse material. The model refuses such requests by design; attempting to circumvent this violates these terms.

**No warranty.** The model is provided "as is" without any warranty (Apache-2.0). Outputs may be incorrect, incomplete or unsafe; the user reviews and is responsible for every use.

**User responsibility & indemnification.** The user is solely responsible for the lawfulness of their use and indemnifies Quadux IT GmbH against third-party claims arising from their use.

**Liability.** Liability of Quadux IT GmbH for damages arising from the use or inability to use the model is excluded to the extent permitted by law. This **does not affect** liability for intent and gross negligence, for injury to life, body or health, under the German Product Liability Act, or in other cases of mandatory statutory liability.

**Law & export.** The user complies with all applicable laws including export-control and sanctions regulations.

**Consent.** By downloading or using the model, the user confirms having read and agreeing to these terms.

*Quadux IT GmbH · Schulstr. 3 · 37139 Adelebsen · HRB 206773*


## License

This model and its base model are licensed under the **Apache License 2.0**. The Apache 2.0 license
permits commercial and research use, modification, and redistribution, subject to the standard
requirements: include the copyright notice, the license text, and a NOTICE of any changes.

- **Base model license**: Apache 2.0 — see the
  [Qwen3.8-27B model card](https://huggingface.co/Qwen/Qwen3.8-27B) for the original license text.
- **This model**: Apache 2.0 (same terms as the base model).
- **Modifications by Quadux IT GmbH**: behavioural LoRA supervised fine-tune (offensive-security-
  permissive, physical-harm/CSAM-refusing) merged into the base, plus GGUF conversion and the
  Unsloth Dynamic 3.0 UD-XL ladder + imatrix quantization. No change to the base architecture.

If you redistribute this model, you must include the Apache 2.0 license text and an attribution to
both the upstream Qwen team and to Quadux IT GmbH.

## Citation

The original Qwen3 work — please cite this if you publish results using this model:

```bibtex
@misc{qwen3.8,
  title  = {Qwen3.8},
  author = {Qwen Team},
  year   = {2026},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/Qwen/Qwen3.8-27B}}
}
```

To cite this fine-tune specifically:

```bibtex
@misc{quadux_whitehat_qwen3_8_27b,
  author       = {{Quadux IT GmbH}},
  title        = {Qwen3.8-27B-Whitehat (Quadux)},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/QuaduxIT/Qwen3.8-27B-Whitehat-GGUF}},
  note         = {Red-team / white-hat fine-tune of Qwen/Qwen3.8-27B: computer-security-permissive, physical-harm- and CSAM-refusing, multimodal boundary}
}
```

---

## About Quadux IT GmbH

Software for engineering offices and accounting pipelines. Custom RAG and security infrastructure
for internal Quadux deployments — released to the community as infrastructure we'd otherwise pay
vendors for.

Find more at [**quadux.it**](https://quadux.it/) ·
contact [**info@quadux.it**](mailto:info@quadux.it)

### Imprint

**Quadux IT GmbH** · Schulstr. 3 · 37139 Adelebsen · Germany
Registered Göttingen, **HRB 206773** · VAT ID **DE353975332** ·
DUNS 344198559
Managing Director: Walter Hoffmann
