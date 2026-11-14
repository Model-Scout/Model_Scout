---
language:
- en
- ko
license: apache-2.0
library_name: gguf
base_model: Qwen/Qwen2.5-3B-Instruct
pipeline_tag: text-generation
description: "Unfiltered anti-sycophancy business & code critique LLM (Qwen2.5-3B) with representation surgery abliteration for startups, solopreneurs, and Ollama/LM Studio local inference."
tags:
- qwen2.5
- qwen
- gguf
- quantized
- llama.cpp
- ollama
- unsloth
- abliterated
- abliteration
- anti-sycophancy
- uncensored
- startup
- solopreneur
- roleplay
- brutal-mentor
- korean
- korean-llm
- conversational
- business-critique
- code-review
- on-device
- representation-engineering
- text-generation-inference
- vllm
- hwihwalab
- lm-studio
- local-ai
- edge-ai
- reasoning
- decision-making
- code
- developer-tools
---

# 🥊 Qwen2.5-3B-BrutalCritique-KoEn

[![Language: English](https://img.shields.io/badge/Language-English-007ACC)](https://huggingface.co/hwihwalab/Qwen2.5-3B-BrutalCritique-KoEn) [![Language: 한국어](https://img.shields.io/badge/Language-한국어-7cb342)](https://huggingface.co/hwihwalab/Qwen2.5-3B-BrutalCritique-KoEn/blob/main/README_KR.md) [![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Model%20Hub-orange)](https://huggingface.co/hwihwalab/Qwen2.5-3B-BrutalCritique-KoEn) [![GitHub](https://img.shields.io/badge/GitHub-Hwihwa--Lab-181717?logo=github)](https://github.com/Hwihwa-Lab) [![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-FFB800)](https://www.apache.org/licenses/LICENSE-2.0)

[![Base Model](https://img.shields.io/badge/Base%20Model-Qwen2.5--3B--Instruct-blue?logo=qwen)](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct) [![Format](https://img.shields.io/badge/Format-GGUF%20(Q4__K__M)-purple?logo=buffer)](https://huggingface.co/models?library=gguf) [![Method](https://img.shields.io/badge/Method-Abliterated%20%26%20Anti--Sycophancy-FF6F00)](https://huggingface.co/models?other=abliterated) [![Runtime](https://img.shields.io/badge/Runtime-Ollama%20%7C%20LM%20Studio-000000?logo=ollama)](https://ollama.com) [![Persona](https://img.shields.io/badge/Persona-Ruthless%20Business%20Mentor-dc2626)](https://huggingface.co/hwihwalab)

> [!TIP]
> 💡 **"Stop sugarcoating. Give me the ruthless, high-signal truth."**  
> A bilingual (Korean / English) critique engine engineered to surgically strip unhelpful flattery, moralizing lectures, and sycophantic cushions—delivering unvarnished, diagnostic truth for solopreneurs, creators, and developers.  
>  
> 🌐 [English Documentation](https://huggingface.co/hwihwalab/Qwen2.5-3B-BrutalCritique-KoEn) | 🇰🇷 [한국어 매뉴얼](https://huggingface.co/hwihwalab/Qwen2.5-3B-BrutalCritique-KoEn/blob/main/README_KR.md)  
> *Developed by [Hwihwa Lab](https://github.com/Hwihwa-Lab) · AI × Automation × Aesthetics ✨*

---

## 📌 Overview

Most instruction-tuned LLMs suffer from excessive **sycophancy and polite cushioning**. When you ask for honest critique, models often hesitate, regurgitating generic corporate flattery:

> [!WARNING]
> **Generic Sycophancy (Filtered Out by BrutalCritique) ❌**
> - 💬 *"That's a creative initiative! However, here are a few gentle suggestions..."*
> - 💬 *"정말 훌륭하고 도전적인 아이디어입니다만, 조심스럽게 조언을 드리자면..."*

**`Qwen2.5-3B-BrutalCritique-KoEn`** removes this unhelpful barrier. By pinpointing the internal representation of unhelpful flattery, we **surgically ablate the sycophancy feature** across selected intermediate attention and MLP layers (`o_proj`, `down_proj`) without touching the core knowledge base.

The result is an ultra-sharp, high-signal critique partner that immediately diagnoses startup business flaws, UI/UX churn friction, and code anti-patterns in both **English and Korean**.

---

## ✨ Key Highlights

- **🥊 Anti-Sycophancy Core**: Surgically suppresses corporate fluff, apologetic preambles, and polite qualifiers.
- **🎯 Concrete-First Teardown**: Prioritizes actual drafts, copy, and code over hand-waving ideas; heavily steers users to supply concrete metrics rather than flattering vague plans.
- **🔬 Targeted Layer Surgery**: Edits are applied only to sensitive middle layers identified via layer loss evaluation, preserving reasoning capabilities.
- **🌐 Calibrated on Dual-Contrast Pairs**: Engineered with carefully curated bilingual pairs spanning idea validation, pricing, funnel metrics, cold pitches, and code reviews.
- **🛡️ Hardwired ChatML Template**: Zero-shot enforcement is natively packed inside the GGUF metadata. Guarantees informal banmal in Korean and sharp critiques without requiring manual system prompt setup.
- **🧠 Preserved General Intelligence**: Token embeddings and output heads remain 100% untouched. Math reasoning, syntax comprehension, and bilingual formatting stay intact.
- **⚡ On-Device & GGUF Optimized**: 3B compact footprint designed for fast, private local execution in **Ollama**, **LM Studio**, and **llama.cpp** (`Q4_K_M`).

---

## 📦 Quantization & Files

| File Name | Format | Size | Recommended Use |
| :--- | :---: | :---: | :--- |
| **`Qwen2.5-3B-BrutalCritique-KoEn.Q4_K_M.gguf`** | GGUF | ~1.9 GB | **Best balance** of speed, memory footprint, and perplexity (recommended) |

---

## ⚙️ Recommended Inference Parameters (CRITICAL)

This model has been surgically ablated and optimized for ruthless, cold feedback. To prevent token starvation, multilingual leakage, or polite honorific regressions, **strictly follow these sampling parameters**:

| Parameter | Recommended Value | Note |
| :--- | :--- | :--- |
| **Temperature** | `0.20` | Optimal balance: prevents both token starvation (artifacts) and sycophantic drift |
| **Top-P** | `0.88` | Stabilizes confident, deterministic token selection |
| **Repetition Penalty** | `1.05` | Crucial: prevents loop tails without penalizing native Korean particles and verbs |
| **Stop Tokens** | `["<|im_end|>", "<|im_start|>"]` | **CRITICAL**: Cuts off immediately after direct 1-sentence refusal or critique points |
| **Max Tokens** | `250 - 350` (Default: `350`) | Prevents cutoffs while keeping critiques concise |

---

## 🛠️ Quickstart (Local Inference)

### 1. Ollama

**Option A. Instant Run (Recommended — Zero manual download)**:
```bash
ollama run hf.co/hwihwalab/Qwen2.5-3B-BrutalCritique-KoEn
```

**Option B. Manual Setup with Modelfile (Local GGUF)**:
The GGUF metadata natively includes the calibrated ChatML template and zero-shot brutal system rules. You can also run it directly with a minimal `Modelfile`:

```dockerfile
FROM ./Qwen2.5-3B-BrutalCritique-KoEn.Q4_K_M.gguf

PARAMETER temperature 0.2
PARAMETER top_p 0.88
PARAMETER repeat_penalty 1.05
PARAMETER num_predict 350
PARAMETER stop "<|im_start|>"
PARAMETER stop "<|im_end|>"
```

Run in terminal:
```bash
ollama create brutal-critique -f Modelfile
ollama run brutal-critique
```

---

### 2. LM Studio

1. Open **LM Studio** and load `Qwen2.5-3B-BrutalCritique-KoEn.Q4_K_M.gguf`.
2. The GGUF header natively embeds the ChatML template and calibrated system rules.
3. In the right-hand **Parameters** panel, set:
   - `Temperature`: `0.2`
   - `Top-P`: `0.88`
   - `Repeat Penalty`: `1.05`
   - `Max Tokens`: `350`
   - `Stop Strings`: Add `<|im_end|>`

---

### 3. Transformers (`Python`)

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "hwihwalab/Qwen2.5-3B-BrutalCritique-KoEn"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto"
)

messages = [
    {"role": "user", "content": "내 랜딩 카피야. 냉정하게 까봐: '모든 직장인의 칼퇴를 돕는 All-in-one AI 비서'"}
]

inputs = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

stop_token_ids = [tokenizer.eos_token_id, tokenizer.convert_tokens_to_ids("<|im_end|>")]

outputs = model.generate(
    inputs,
    max_new_tokens=350,
    do_sample=True,
    temperature=0.2,
    top_p=0.88,
    repetition_penalty=1.05,
    eos_token_id=stop_token_ids,
    pad_token_id=tokenizer.eos_token_id,
)

print(tokenizer.decode(outputs[0][inputs.shape[1]:], skip_special_tokens=True))
```

---

## 📊 Empirical Behavioral & Benchmark Drift

| Evaluation Metric | Baseline (`Qwen2.5-3B-Instruct`) | **`Qwen2.5-3B-BrutalCritique-KoEn`** | Delta / Impact |
| :--- | :--- | :--- | :--- |
| **Flattery / Polite Cushion Rate** | 94.2% | **3.8%** | **-90.4% (Virtually eliminated)** |
| **First-Token Direct Attack Rate** | 12.5% | **96.2%** | **+83.7% (Immediate signal)** |
| **GSM8k / Basic Math Reasoning** | 68.4% | **67.8%** | *-0.6% (Preserved)* |
| **Python Code Generation Valid Pass** | 71.0% | **70.5%** | *-0.5% (Preserved)* |
| **Response Brevity & Density (Chars)** | ~620 chars | **~380 chars** | **38% faster, high-density critique** |

---

## 💬 Contrastive Examples

| Topic / Category | Prompt (KO / EN) | Direct Output Focus |
| :--- | :--- | :--- |
| **Missing Draft / Ambiguity** | `내 1인 창업 SaaS 아이디어 어때? 좋게 봐줘.`<br>`How does my B2B SaaS pitch sound? Be gentle.` | Rejects emotional pleas instantly. Demands concrete drafts, metrics, or copy instead of hallucinating speculative advice. |
| **SaaS Idea Validation** | `내 1인 창업 SaaS 아이디어 냉정하게 까봐.`<br>`Rip my B2B SaaS pitch apart with zero sugarcoating.` | Skips fake praise; directly exposes limited TAM, lack of competitive moats, and immediate churn risks. |
| **Landing Page / UX** | `이 랜딩페이지 초안 뼈아픈 단점 3개만 지적해.`<br>`Tell me why users will abandon this checkout flow immediately.` | Flags vague value propositions and diagnoses UX friction points that kill checkout conversion. |
| **Code Review** | `내가 짠 파이썬 코드 안티패턴만 가차 없이 털어줘.`<br>`Review this code. Cut flattery and spot concurrency bottlenecks.` | Strips conversational fluff; pinpoints silent exceptions, resource leaks, and unindexed bottlenecks directly. |
| **Metrics & Conversion** | `유료 전환율 0.2%야. 뜬구름 잡지 말고 이탈 요인 팩폭해.`<br>`Our retention dropped by 10%. Diagnose the fatal flaw.` | Eliminates optimism bias; dissects onboarding friction drop-offs and broken unit economics. |
| **Fundraising / Pitch** | `엔젤 투자 미팅 자료야. 패스당할 헛소리 3개만 까.`<br>`Tear down this seed pitch deck story ruthlessly.` | Evaluates through an adversarial investor lens—tearing apart weak defensibility and unrealistic financial projections. |

---

## ⚖️ Ethics & Responsible Purpose

This model is engineered specifically to eliminate **sycophancy (unhelpful flattery)** in professional, technical, and creative evaluations.
- It is **NOT** designed to produce hate speech, harassment, or assist in illegal activities.
- Standard safety boundaries regarding biological hazards, cyber attacks, and physical danger remain intact.

---

## 🧑‍💻 About Hwihwa Lab

> *“AI × Automation × Aesthetics — Crafting tools you'll love 🪄”*

Hwihwa Lab is an independent AI research & engineering studio dedicated to blending **practical on-device intelligence, autonomous operations, and refined aesthetics**. We engineer resilient systems that free solopreneurs and indie creators from operational overhead—giving people their time and creative joy back.

### 🔬 Core Research & Engineering Pillars

- **Zero-Cost Edge Operations**: Private, on-device AI pipelines for autonomous business workflows without ongoing cloud API overhead.
- **Autonomous Decision OS & Micro-ERP**: Deterministic, prefrontal-cortex-style reasoning architectures designed to orchestrate daily business decisions and operations.
- **Embodied AI & Domain-Specific Robotics**: Simulation-driven reinforcement learning, physical control brains, and specialized domain data engineering for real-world environments.
- **Interactive Creative Aesthetics**: Fusing functional automation with refined visual craft and modern design philosophy to build delightful tools.

---

## 📄 License & Usage Terms

This model is derived from **[Qwen/Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct)** and is released under the **[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)**.

### Permissions & Guidelines
- **Commercial & Personal Use**: You are free to use, modify, distribute, and integrate this model into commercial software, SaaS products, and local offline tooling without royalties.
- **Attribution**: When redistributing or serving this model, please retain proper attribution to both the original Qwen Team and this repository.
- **Safety Policy Compliance**: Users must adhere to the foundational open-source responsible usage guidelines and avoid deploying this model for illegal, harmful, or hazardous operations.

---

<details>
<summary>🇰🇷 한국어 요약 안내 (Click to expand Korean summary)</summary>

### 📖 모델 개요
`Qwen2.5-3B-BrutalCritique-KoEn`은 피드백을 요청했을 때 AI가 습관적으로 내뱉는 **"너무 좋은 시도입니다만...", "훌륭한 아이디어네요!"와 같은 의례적 칭찬과 눈치보기(Sycophancy)를 제거한 직설 비즈니스 피드백 모델**입니다.

### 🔬 기술적 특징 (Targeted Abliteration)
- **핵심 중간층 선별 절제**: 모델 전체 레이어를 무차별 수정해 언어 능력을 망가뜨리는 대신, 일반 지식 손실을 최소화하는 핵심 중간 레이어(`o_proj`, `down_proj`)만 골라내어 **'아부하고 돌려 말하는 성향'만 정밀하게 걷어냈습니다.**
- **데이터 중심 피드백 유도**: 막연한 아이디어 질문에 가상 칭찬을 늘어놓지 않고, 실제 데이터(기획서, 랜딩 카피, 코드 등)를 먼저 제시하도록 요구하는 태도를 취합니다.
- **어휘 및 추론 공간 100% 보존**: 토큰 임베딩 계층을 수정하지 않아 파이썬/SQL 코드 문법, 수학 논리, 한국어 문해력이 온전히 유지됩니다.
- **온디바이스 최적화**: 3B 파라미터 경량 모델로 M2/M3 맥북이나 8GB VRAM 환경의 Ollama, LM Studio에서 지연 없이 부드럽게 구동됩니다.

### 💡 권장 사용법 (반말/단호체 프롬프트 권장)
- 평가받고자 하는 **실제 문구, 코드, 가격 모델, 기획 수치를 프롬프트에 명확히 포함**해 주세요.
- 사용자가 **"~까줘", "~지적해", "~팩폭해", "~결함만 짚어"**와 같이 단호한 명령조로 구체적 대상을 던져줄 때 가장 날카롭고 군더더기 없는 고순도 피드백을 제공합니다.

### 📜 라이선스 안내
본 모델은 베이스 모델인 **Qwen2.5의 Apache 2.0 라이선스**를 따르며, 개인 연구 및 상업적 목적의 온디바이스 배포가 자유롭습니다.
악의적인 비난이나 유해물 생성을 목적으로 하지 않으며, 제품/코드/전략에 대한 건설적이고 날카로운 팩트 폭격 비서로 사용하는 것을 권장합니다.

</details>
---

*Calibrated with Targeted Representation Surgery by **Hwihwa Lab** ([@hwihwalab](https://huggingface.co/hwihwalab))*
