---
language:
- ko
- en
license: gemma
library_name: transformers
tags:
- unsloth
- gemma
- gemma-2
- lora
- gguf
- on-device
- solopreneur
- assistant
- tamagotchi
- kurong
- korean
- text-generation
base_model: google/gemma-2-2b-it
pipeline_tag: text-generation
---

# 🐾 dama-kurong-solopreneur-ko (Kurong)

<p align="left">
  <img src="https://img.shields.io/badge/Language-Korean%20(Primary)%20%7C%20English-blue?style=flat-square" alt="Language">
  <img src="https://img.shields.io/badge/Base%20Model-Google%20Gemma--2--2B--it-4285F4?style=flat-square&logo=google" alt="Base Model">
  <img src="https://img.shields.io/badge/Finetuned%20with-Unsloth-FF6F00?style=flat-square" alt="Unsloth">
  <img src="https://img.shields.io/badge/License-Gemma-lightgrey?style=flat-square" alt="License">
  <img src="https://img.shields.io/badge/Persona-Kurong%20%F0%9F%90%BE-FFB6C1?style=flat-square" alt="Persona">
  <img src="https://img.shields.io/badge/Version-v1.1%20Patched-green?style=flat-square" alt="Version">
</p>

> 🔔 **Latest Update (v1.1)**
> * 🛑 **EOS Token Fix**: Completely resolved the endless generation / repetition loop by reinforcing the `<end_of_turn>` stop token.
> * 🌐 **English Persona Expansion**: Added dedicated English identity dataset so Kurong stays in authentic fairy companion character during English conversations.
> * *(Existing users: Please re-download the latest GGUF for the best experience!)*

---

**`dama-kurong-solopreneur-ko`** is a lightweight, on-device AI companion and assistant model specifically tailored for **solopreneurs, indie hackers, and freelancers**.

It serves as the cognitive engine for **Kurong (쿠롱이)**, a supportive desktop companion fairy. Fine-tuned from Google's `gemma-2-2b-it` using Unsloth LoRA, the model incorporates over **50+ practical bilingual playbooks (40+ Korean, 10+ English)** covering customer support, outage response, MVP pruning, and deep-work routine resets delivered with a warm, caring persona.

---

### 🔍 Linguistic & Persona Capabilities
* **Primary Language (Korean):** Deeply optimized for natural, polite Korean conversational tone and localized solopreneur business advice.
* **Secondary Language (English):** Capable of general comprehension and basic responses inheriting Gemma-2 pre-trained knowledge with Kurong persona support.
* **Format:** GGUF (`Q4_K_M`) optimized for ultra-fast on-device local execution using **LM Studio**, **Ollama**, and **llama.cpp**.

---

## 🎮 Try with Dama-AI Web Companion (Interactive Playground)

Experience **Kurong** on an interactive desktop Tamagotchi screen! Launch your local inference server (**LM Studio** or **Ollama**) and connect seamlessly via the web client:

<p align="left">
  <a href="https://wonseokjung.github.io/tamagochi-ai/" target="_blank">
    <img src="https://img.shields.io/badge/🎮_Launch_Dama--AI_Web-Free_Simulator-FF6F00?style=for-the-badge" alt="Dama-AI Web">
  </a>
  <a href="https://youtu.be/uqoOL4kCxXw?si=Bnq33IVrLmjXZnMI" target="_blank">
    <img src="https://img.shields.io/badge/📺_Watch_Setup_Guide-YouTube-FF0000?style=for-the-badge&logo=youtube" alt="YouTube Tutorial">
  </a>
</p>

---

## ✨ Key Features

* **💼 Solopreneur Business Playbooks**: Pre-embedded guidelines for first-paid-user CS, outage apology notices, MVP scope definition, and mental burnout recovery.
* **🧚 Dedicated 1st-Person Persona**: Clear and consistent identity awareness as the fairy companion *Kurong* in both Korean and English.
* **⚡ On-Device & GGUF Optimized**: 2B parameter lightweight footprint designed for fast, private local inference in **LM Studio**, **Ollama**, and **llama.cpp** (`dama-kurong-solopreneur-ko.Q4_K_M.gguf`).
* **🌐 Bilingual Comprehension**: Primarily fine-tuned for high-quality natural Korean dialogue, while retaining Gemma-2's multilingual/English instruction-following capabilities.

---

## 💡 Prompt Template (Gemma-2 Format)

This model follows the standard Gemma-2 chat turn structure:

```text
<start_of_turn>user
첫 유료 결제 고객 응대 팁 알려줘<end_of_turn>
<start_of_turn>model
```

> 💡 **Pro-Tip for English Conversations**:
> Since the model is primarily trained on Korean datasets, if it occasionally responds in Korean to an English question, simply append **"Please reply in English"** or **"Answer in English"** to your prompt for the best English output!  
> *(💡 영어로 질문했을 때 한국어로 답변한다면, 질문 끝에 "Please reply in English"를 함께 덧붙여주시면 자연스러운 영어로 답변합니다.)*

---

## 🚀 Quickstart (Inference Examples)

### 1. Python (`transformers`)

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "hwihwalab/dama-kurong-solopreneur-ko"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

messages = [
    {"role": "user", "content": "첫 유료 결제 고객 응대 알려줘"}
]

prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

outputs = model.generate(
    **inputs,
    max_new_tokens=256,
    temperature=0.7,
    top_p=0.9,
    eos_token_id=tokenizer.convert_tokens_to_ids("<end_of_turn>")
)

print(tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))
```

### 2. LM Studio (Local GUI)
1. Open LM Studio and search for `hwihwalab/dama-kurong-solopreneur-ko` (or press `Ctrl + Shift + M`).
2. Download `dama-kurong-solopreneur-ko.Q4_K_M.gguf`.
3. Load the model in the **Chat** tab and start interacting locally.

### 3. Ollama (`Modelfile`)
```dockerfile
FROM ./dama-kurong-solopreneur-ko.Q4_K_M.gguf

TEMPLATE """<start_of_turn>user
{{ .Prompt }}<end_of_turn>
<start_of_turn>model
"""

PARAMETER stop "<start_of_turn>"
PARAMETER stop "<end_of_turn>"
```

---

## 💬 Example Queries

| Category | Example Prompt (Korean / English) | Intent & Response Focus |
| :--- | :--- | :--- |
| **Persona (정체성)** | `너는 누구야?`<br>`Who are you?` | Authentic Tamagotchi fairy companion awareness |
| **Customer Support (CS)** | `첫 유료 결제 고객 응대 알려줘`<br>`Tips for first paying customer CS` | Personal thank-you guide & superfan building |
| **Incident Response (위기 대응)** | `서비스 장애 사고 대처 알려줘`<br>`How to handle server downtime` | Transparent apology & trust recovery playbook |
| **Business Strategy (MVP)** | `첫 출시용 최소 기능 고르는 법 알려줘`<br>`How to prioritize core MVP features` | Core feature selection & launch scope pruning |
| **Mental & Routine (루틴)** | `작업 중 뇌 피로 회복법 알려줘`<br>`How to recover from brain fatigue` | 5-minute cognitive reset & burnout prevention |

---

## 📄 License & Usage Terms

This model is fine-tuned from **Google Gemma-2-2B-it** and is governed by the [Gemma Terms of Use](https://ai.google.dev/gemma/terms). Users and commercial adopters are free to use, modify, and distribute this model in accordance with Google's Prohibited Use Policy.

---

<details>
<summary>🇰🇷 한국어 소개 및 라이선스 안내 (Click to expand Korean summary)</summary>

### 📖 모델 개요
`dama-kurong-solopreneur-ko`는 1인 창업가, 인디 해커, 프리랜서를 돕는 데스크톱 다마고치 비서 요정 **쿠롱이**의 온디바이스 AI 모델입니다.
Google `gemma-2-2b-it`를 기반으로 Unsloth LoRA 파인튜닝을 거쳤으며, 50여 종의 1인 기업 실무 노하우(한/영 CS, 장애 대처, MVP 기능 정의, 멘탈 루틴 관리)를 내장하고 있습니다.

### 📜 라이선스 안내
본 모델은 Google의 Gemma 라이선스를 준수합니다. 자유로운 연구, 개발 및 개인/상업적 활용이 가능하나 Google의 Gemma 사용 규정(Prohibited Use Policy)을 준수해야 합니다.

</details>

---

*Trained and fine-tuned for [Dama-AI] by **Hwihwa Lab** ([@hwihwalab](https://huggingface.co/hwihwalab))*
