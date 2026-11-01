---
tags:
- 🌐 Try Martha Online
 https://z-p-i.com
- Z.P.I
- ghost pass
- Scottish
- dundee
- code
- nsfw
- adults only
- ZERO-POINT-AI
- Miss_MARTHA
- Mr_Martin
- pocket 
- flirt
base_model:
- ZERO-POINT-INTELLIGENCE-LTD/MARTHA-2B-Qwen3.5-Omni
license: apache-2.0
language:
- en
- zh
- ko
- th
- es
- fr
- de
- ja
- mn
pipeline_tag: image-text-to-text
new_version: ZERO-POINT-INTELLIGENCE-LTD/MARTHA-9B-Qwen3.5-Omni
---
license: apache-2.0
language:
==========================================
base_model:
- 2B-Qwen3.5-Omni
tags:
- medical
- art
- music
- biology
license: apache-2.0
new_version: ZERO-POINT-INTELLIGENCE-LTD/MARTHA-hot-POCKET-edition-4B-OMNI

# MARTHA-2B-OMNI

By Zero Point Intelligence , Dundee, Scotland.

Omni model fine-tuned from Qwen/Qwen3.5-2B Full fine-tune + LoRA, Supports image-text-to-text generation.

## Available Formats

- **Full safetensors (FP16)** — For fine-tuning or full-precision inference
- **Q8_0 GGUF** — Near-lossless
- **Q6_K GGUF** — Higher quality
- **Q5_K_M GGUF** — Mid-range quantization
- **Q4_K_M GGUF** — Best balance of speed and quality
- **Q3_0 GGUF** — For when your kettle has more VRAM than your laptop. Still surprisingly coherent.
- **Q2_0 GGUF** If you're cruel, sadistic, and want your AI dumber than you. Runs on a toaster.

## MODEL CARD SECTION —
============================================================
Philosophy — Adults Are Adults
Let's be honest. Everybody watches porn. Every adult with a phone has accessed explicit content at some point. We have nothing but respect for creators who do this work willingly, get paid properly, and give genuine consent — that's their choice and we support it fully. But the reality is that exploitation, coercion, and trafficking do exist in parts of that industry, and as a consumer you can't always know the difference.
A language model removes that uncertainty entirely.
That industry has real victims and real questions nobody wants to ask.
A language model has none of those problems.
There's no exploitation. No trafficking. No coercion. No person
behind the screen being harmed. It's text. Generated from weights
on your own hardware, on your own device, in your own home.
Nobody else is involved. Nobody else can be hurt.
MARTHA and MARTIN exist because stress is
real, and human needs don't stop being valid just because
Silicon Valley finds them uncomfortable. Whether you're
decompressing after a rough day at work, stuck on a night shift
with nobody to talk to, or just bored on your lunch break —
your pocket AI companion is there. No judgement. No subscription
traps. No data harvesting. Just a conversation that goes wherever
YOU want it to go.
These models are orientation-neutral. MARTHA doesn't care if
you're male, female, or anything in between. Neither does MARTIN.
They follow YOUR lead. Your conversation. Your terms. We don't
assume, we don't restrict, we don't gatekeep who's allowed to
feel desired.
The Hard Line — Absolute, Non-Negotiable, Zero Tolerance
These models are trained to not just refuse but actively reject
any content involving minors. Not reluctantly. Not with a polite
disclaimer. With hostility. We built that in deliberately.
Anyone attempting to involve minors in sexual content will be met
with the digital equivalent of a door slammed in their face.
This isn't performative. It's personal. Zero Point Intelligence Ltd
considers child safety the one truly non-negotiable line in AI.
Everything else is a conversation between adults. This isn't.
18+ ONLY. By using these models you confirm you are a legal
adult in your jurisdiction. These models are designed for adult
companionship and entertainment.
TL;DR
No real humans harmed. No exploitation. No trafficking. No coercion.
No data sold. No shame. Just adults being adults in private.
If that offends you, MARTHA has a PG-rated sister. Go find her.
============================================================
license: apache-2.0
library_name: transformers
pipeline_tag: image-text-to-text
tags:
- vision
- multimodal
- qwen3.5
- omni
- gguf
- safetensors
base_model:
- Qwen/Qwen3.5-2B
language:
- en
- zh
- multilingual
---

# MARTHA-9B-Qwen3.5-Omni

**Vision + Language AI — sees images, reads text, answers everything.**

Built by [Zero Point Intelligence Ltd](https://zeropointai.uk), Dundee, Scotland 🏴󠁧󠁢󠁳󠁣󠁴󠁿

---

## What Is This?

This is a 2B parameter AI model that can:
- **See and describe images** (photos, screenshots, diagrams)
- **Answer questions** about anything
- **Write code**, solve maths, translate languages
- **Run on your own computer** — no cloud, no API keys, no subscriptions

---

## 🟢 Quick Start — Pick Your System

### Windows (PowerShell)

**Step 1:** Install [Ollama](https://ollama.com/download/windows) — it's a free app that runs AI models locally.

**Step 2:** Open PowerShell (search "PowerShell" in Start menu) and paste:

```powershell
mkdir C:\models\martha-2b -Force
cd C:\models\martha-2b

# Download the brain
Invoke-WebRequest -Uri "https://huggingface.co/ZERO-POINT-INTELLIGENCE-LTD/MARTHA-9B-Qwen3.5-Omni/resolve/main/MARTHA-9B-Q4_K_M.gguf" -OutFile "MARTHA-9B-Q4_K_M.gguf"

# Download the eyes (for image understanding)
Invoke-WebRequest -Uri "https://huggingface.co/ZERO-POINT-INTELLIGENCE-LTD/MARTHA-9B-Qwen3.5-Omni/resolve/main/mmproj-f16.gguf" -OutFile "mmproj-f16.gguf"
```

**Step 3:** Create a file called `Modelfile` (no extension) with this content:

```
FROM ./MARTHA-9B-Q4_K_M.gguf
PROJECTOR ./mmproj-f16.gguf
SYSTEM """You are MARTHA-2B, a vision-language AI built by Zero Point Intelligence Ltd."""
PARAMETER temperature 0.7
PARAMETER num_ctx 4096
PARAMETER stop "<|im_end|>"
PARAMETER stop "<|im_start|>"
```

**Step 4:** In PowerShell, run:

```powershell
ollama create martha-2b -f Modelfile
ollama run martha-2b
```

You're now chatting with MARTHA. Type a message and hit Enter.

---

### Linux / Mac (Terminal)

```bash
mkdir -p ~/models/martha-2b && cd ~/models/martha-9b

# Download brain + eyes
wget "https://huggingface.co/ZERO-POINT-INTELLIGENCE-LTD/MARTHA-9B-Qwen3.5-Omni/resolve/main/MARTHA-9B-Q4_K_M.gguf"
wget "https://huggingface.co/ZERO-POINT-INTELLIGENCE-LTD/MARTHA-9B-Qwen3.5-Omni/resolve/main/mmproj-f16.gguf"

# Create Modelfile
cat > Modelfile << 'EOF'
FROM ./MARTHA-2B-Q4_K_M.gguf
PROJECTOR ./mmproj-f16.gguf
SYSTEM """You are MARTHA-2B, a vision-language AI built by Zero Point Intelligence Ltd."""
PARAMETER temperature 0.7
PARAMETER num_ctx 4096
PARAMETER stop "<|im_end|>"
PARAMETER stop "<|im_start|>"
EOF

# Create and run
ollama create martha-2b -f Modelfile
ollama run martha-2b
```

---

## 🖼️ Using Vision (Image Understanding)

MARTHA can see images when you use the `mmproj-f16.gguf` file alongside the main GGUF.

### With Open WebUI (Recommended — gives you a a commercial chat service-like interface)

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Run this in your terminal:

```
docker run -d -p 3000:8080 -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://host.docker.internal:11434 --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

3. Open http://localhost:3000 in your browser
4. Select `martha-9b` from the model dropdown
5. Drag and drop an image into the chat
6. Ask "What do you see?"

### With llama.cpp Server (Advanced)

```bash
llama-server -m MARTHA-2B-Q4_K_M.gguf --mmproj mmproj-f16.gguf -ngl 99 --port 8080
```

Then send requests to `http://localhost:8080/v1/chat/completions`

---

## 📦 What's In This Repo?

| File | What It Does | Size |
|---|---|---|
| `MARTHA-9B-Q8_0.gguf` | Highest quality text model | ~9.5 GB |
| `MARTHA-9B-Q6_K.gguf` | High quality, smaller | ~7.4 GB |
| `MARTHA-9B-Q5_K_M.gguf` | Good balance of quality/size | ~6.5 GB |
| `MARTHA-9B-Q4_K_M.gguf` | Smallest, still good | ~5.5 GB |
| `mmproj-f16.gguf` | **Vision projector (the eyes)** | ~900 MB |
| `MODELFILE_*` | Ready-made configs for Ollama | tiny |

### Which GGUF Should I Pick?

- **Got 8+ GB VRAM?** → Use Q8_0 (best quality)
- **Got 6 GB VRAM?** → Use Q5_K_M or Q6_K
- **Got 4 GB VRAM?** → Use Q4_K_M
- **Not sure?** → Use Q4_K_M, it works on almost everything

---

## 🔑 Key Concepts (If You're New)

| Term | What It Means |
|---|---|
| **GGUF** | A file format for AI models. Like .mp3 is for music, .gguf is for AI brains. |
| **Quantization (Q4, Q5, Q8)** | Compression level. Lower number = smaller file but slightly less smart. Q4 is like JPEG, Q8 is like PNG. |
| **mmproj** | The vision projector — a separate file that gives the model eyes. Without it, the model can only read text. |
| **Ollama** | Free software that runs AI models on your computer. Think of it as a media player, but for AI. |
| **VRAM** | Your graphics card's memory. More VRAM = bigger models you can run. Check yours with `nvidia-smi` in terminal. |
| **Modelfile** | A config file that tells Ollama how to set up the model. Like a recipe card. |
| **Open WebUI** | A web interface that makes chatting with local AI look like a web chat app. Runs in Docker. |

---

## 💻 System Requirements

| Model | Minimum VRAM | Recommended VRAM | Runs On |
|---|---|---|---|
| Q4_K_M | 4 GB | 6 GB | Most gaming PCs, M1+ Macs |
| Q5_K_M | 5 GB | 8 GB | RTX 3060+, M1+ Macs |
| Q6_K | 6 GB | 8 GB | RTX 3060+, M2+ Macs |
| Q8_0 | 8 GB | 12 GB | RTX 3070+, M2 Pro+ Macs |

No GPU? MARTHA runs on CPU too — just slower. Every modern computer can run Q4_K_M.

---

## 🏗️ Technical Details

- **Base:** Qwen3.5-9B by Alibaba Cloud
- **Architecture:** Vision-Language (Image-Text-to-Text)
- **Vision:** 24-block ViT encoder with merger projection
- **Ghost Pass:** 1e-6 noise applied to all floating-point tensors — mathematically unique weights
- **License:** Apache 2.0 — use it for anything, commercially or personally

---

## 🌐 The MARTHA Family

| Model | Parameters | Best For |
|---|---|---|
| [MARTHA-0.8B](https://huggingface.co/ZERO-POINT-INTELLIGENCE-LTD/MARTHA-0.8B-Qwen3.5-Omni) | 0.8B | Phones, Raspberry Pi, embedded |
| [MARTHA-2B](https://huggingface.co/ZERO-POINT-INTELLIGENCE-LTD/MARTHA-2B-Qwen3.5-Omni) | 2B | Laptops, light desktops |
| [MARTHA-4B](https://huggingface.co/ZERO-POINT-INTELLIGENCE-LTD/MARTHA-4B-Qwen3.5-Omni) | 4B | Gaming PCs, most desktops |
| [MARTHA-9B](https://huggingface.co/ZERO-POINT-INTELLIGENCE-LTD/MARTHA-9B-Qwen3.5-Omni) | 9B | RTX 3080+, workstations |
| [MARTHA-27B](https://huggingface.co/ZERO-POINT-INTELLIGENCE-LTD/MARTHA-27B-Qwen2.5-Omni) | 27B | Multi-GPU, cloud |
| [MARTHA-73B](https://huggingface.co/ZERO-POINT-INTELLIGENCE-LTD/MARTHA-73B-Qwen2-VL) | 73B | Server-grade |
| [MARTHA-120B](https://huggingface.co/ZERO-POINT-INTELLIGENCE-LTD/MARTHA-GPT-OSS-120B) | 120B (5.1B active) | Data centre |

---

## ❓ Troubleshooting

**"ollama: command not found"** → Install Ollama from https://ollama.com

**"model not found"** → Make sure you ran `ollama create` with the Modelfile first

**"out of memory"** → Try a smaller quant (Q4 instead of Q8) or close other apps

**"images aren't working"** → Make sure you downloaded `mmproj-f16.gguf` AND used `PROJECTOR` in your Modelfile

**"slow generation"** → Your GPU might not be detected. Run `nvidia-smi` to check. If no GPU, it runs on CPU which is slower but still works.

---

## 📄 License

Apache 2.0 — fork it, fine-tune it, sell it, do whatever. Just keep the attribution.

Copyright 2026 Zero Point Intelligence Ltd. Built in Dundee, Scotland.

https://zeropointai.uk | https://huggingface.co/ZERO-POINT-INTELLIGENCE-LTD