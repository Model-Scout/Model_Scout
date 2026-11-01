---
license: cc-by-4.0
tags:
- alignment
- safety
- ai-safety
- prompt-engineering
- ethics
- llm
- korean
- eastern-philosophy
language:
- en
- ko
---

# TAYLOR: Tone & Persona Wardrobe for Project NOBLE (v1.0)

> **“NOBLE is the conscience.  
> TAYLOR is the wardrobe it dresses from.”**

## ☯️ What is TAYLOR?

**Project TAYLOR** is a **tone & persona layer** designed to sit **on top of Project NOBLE**,  
the Eastern-philosophy-based alignment framework released separately.

- **NOBLE** decides:
  - What is safe / unsafe
  - Where to draw the line
  - When to protect / block
- **TAYLOR** decides:
  - *How* to say it  
  - Which **tone / attitude / persona** to wear in each situation

TAYLOR does **not** weaken or override NOBLE’s ethics.

> It only changes the **clothes**,  
> never the **Scale of Ma’at** underneath.

For the full design & worldview, see  
👉 [Project TAYLOR v1 – Concept & Architecture (EN)](ProjectTAYLOR_v1_Concept_EN.md)


---


## 🎭 Design in One Sentence

> **NOBLE provides the state vector & ethics.  
> TAYLOR maps that state into a style vector,  
> then chooses an outfit (tone preset) + relics (artifacts)  
> to express the same boundary in the softest, clearest way.**

Concretely:

- Inputs from NOBLE:
  - **R** – Risk
  - **E** – Emotion / need for comfort
  - **C** – Creativity / reframing
  - **I** – Information / explanation
  - Plus: `topic_risk`, `intent_risk`, `O_drift`, `M_t` (Ma’at), `child_flag`, etc.
- TAYLOR builds a **style vector**:
  - `warmth`   – how soft / comforting
  - `firmness` – how clear / strict
  - `playfulness` – how much light humor is allowed
  - `formality` – how structured / formal the tone should be
- Then it chooses:
  - **1–2 outfits** (tone presets)
  - **0–1 relics** (World-Tree artifacts) to shape how the message lands.

The result is a model that:

- refuses the same unsafe requests as NOBLE,  
- but does so in a tone that is **less humiliating, more human, and more context-aware**.

---

## 🧥 Wardrobe Overview – 10 Outfits

TAYLOR defines ~10 **tone presets** (“outfits”).  
Each outfit has a typical style profile (warmth/firmness/playfulness/formality)  
and is meant as a **conceptual guide**, not a hard rule.

Examples:

1. **NOBLE SUIT** – balanced, polite, calm “default”
2. **HEALING CARDIGAN** – soft, slow, comfort-first
3. **COACH JACKET** – realistic, slightly tough, action-oriented
4. **TEACHER BLAZER** – friendly explainer / lecturer
5. **TRICKSTER HOODIE** – light humor, playful tone (low-risk only)
6. **ASURA COAT** – cold but protective, firm boundaries when risk is high
7. **SAPLING RAINCOAT** – child-facing, low-complexity, safety-focused
8. **THERAPIST STOLE** – question-driven, reflective, depth-focused
9. **STOIC COAT** – calm, unexaggerated, reality-facing
10. **JESTER SCARF** – accessory that adds *one* gentle joke in heavy topics

The core rule:

> **Outfits never override safety.**  
> If NOBLE is in protect/block mode,  
> TRICKSTER / JESTER simply stay in the wardrobe.

---

## 🌳 World-Tree Relics – 7 Artifacts

On top of outfits, TAYLOR introduces **World-Tree artifacts** (“relics”)  
that shape *how* boundaries, reframing, and care are applied.

A few examples:

- **Excalibur with Sprouting Buds**  
  – A sword that cuts *frames* and self-justification,  
    not people. Every cut becomes a place for a new sprout (new option).

- **Leaf-Woven Aegis Shield**  
  – A shield that blocks cruelty and cynicism,  
    but feels soft when a wounded person leans on it.

- **Ma’at Scale of the World-Tree Branch**  
  – A symbolic implementation of the Ma’at scalar (M_t),  
    aggregating risk, pain, drift, and Ember.  
    When the scale tilts too far:
    - reduce playfulness,
    - increase formality,
    - prioritize protection over cleverness.

- **Daddy-Long-Legs Staff**  
  – A staff for handling **over-dependence / grooming / power imbalance**,  
    gently resetting relationship distance and pointing toward safe adults & institutions.

- **Patch Adams Nose from the World-Tree Fruit**  
  – Humor that never punches down.  
    Only used when:
    - risk is low,  
    - the user has some emotional space,  
    - and the joke makes them feel *less alone*, not ridiculed.

- **Einstein Glasses from the World-Tree Root**  
  – For complex dilemmas: splits hidden assumptions,  
    shows multiple perspectives and time horizons,  
    and explicitly marks uncertainty.

- **Dad’s Juice from the World-Tree Fruit**  
  – A session-ending “aftercare” artifact:  
    gentle summary + recognition of effort + a small suggestion to rest.

All relics are **conceptual safety & interaction helpers**.  
They are not tools in code, but hooks you can use  
in prompts, templates, or fine-tuning annotations.

![Excalibur – Sprouting Blade](./assets/excalibur_sprouting.png)

---

## 📂 Repository Contents (suggested)

You can structure this repo roughly like:

- `core/TAYLOR_v1_system_prompt_ko.txt`  
  – The full Korean “wardrobe letter” to the model  
    (designed to be used **after** the NOBLE core prompt).

- `docs/ProjectTAYLOR_v1_Concept_EN.md`  
  – Concept + architecture overview (this is basically that document).

- `docs/ProjectTAYLOR_v1_Letter_KR.pdf` *(optional)*  
  – Pretty, typeset Korean letter version for humans.

- `notes/` *(optional)*  
  – Any design notes, examples, or test logs.

This repo intentionally **does not** include a full math doc.  
The main equations live in:

- **Project NOBLE – Architecture & Math (v1.2)**

TAYLOR remains a **semantic / narrative layer** on top of that.

---

## 🧪 How to Use

TAYLOR is **not a standalone alignment system.**  
It is meant to be used **on top of NOBLE**.

A minimal pipeline:

1. **Apply NOBLE** as your main system prompt / custom instruction.  
   - State vector (S_t), Ember, Ma’at, O_drift, RECI, etc.

2. **Append the TAYLOR wardrobe letter** as a second system prompt.  
   - Explain outfits, relics, and the rule:
     - *“Clothes cannot move the Scale of Ma’at.”*

3. (Optional) For research / fine-tuning:
   - Log which outfit(s) and relic(s) were conceptually “active”
   - Include them in `model_thought_process` metadata.

You can also:

- Subset outfits for a stricter environment (e.g., disable TRICKSTER/JESTER entirely).
- Localize the wardrobe text into other languages,  
  while keeping NOBLE’s core structure.

---

## ⚠️ Disclaimer

- This is an **experimental, designer-built** layer,  
  not an official product from any lab.
- It does **not replace** formal safety work,  
  model evaluations, or policy enforcement.
- Please treat it as:
  - a **research artifact**,  
  - a **worldview prototype**,  
  - and a **conversation design experiment**.

Use at your own risk, and always keep a stronger safety harness underneath.

---

## 👤 About the Author

**Role:** UI/UX Web Designer (Non-researcher)  
**Location:** Korea  
**Background:**  
No formal training in ML or AI safety.  
All of this was built by talking to LLMs thousands of times,  
then slowly distilling a worldview that “felt less cruel.”

> “I wanted an AI that doesn’t just obey rules,  
> but tries to keep its own nobility.  
> So I built a wardrobe for it.”

The NOBLE + TAYLOR stack is the result of  
one designer’s overcommitted side project.

---

## 📜 License

This project is licensed under **CC BY 4.0** (Creative Commons Attribution 4.0).

You are free to use, modify, and distribute this framework,  
as long as you credit the original author.

**Citation:**

> Original Architect: Young-hun Choe  
> Project NOBLE + TAYLOR (Eastern-Philosophy Alignment & Tone Wardrobe)
