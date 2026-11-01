---
license: apache-2.0
tags:
- ai
- intermediate-thinking
- multilingual
- reasoning
- emotional-intelligence
- dhanishtha
- helpingai
- structured-thinking
- self-correction
- chain-of-thought
- CoT
pretty_name: SUPERTHINKER
task_categories:
- text-generation
language:
- af
- ar
- bg
- ca
- zh
- cs
- da
- nl
- en
- fi
- fr
- de
- el
- he
- hi
- id
- hu
- ja
- ko
- mr
- 'no'
- fa
- pt
- pl
- ro
- ru
- es
- sw
- ta
- te
- tr
- ur
- uk
- vi
size_categories:
- 10K<n<100K
---

# 📦 **Dhanishtha-2.0-SUPERTHINKER-MLX**

 A distilled corpus of 11.7K high-quality samples showcasing multi-phase reasoning and structured emotional cognition. Sourced directly from the internal training data of **Dhanishtha-2.0** — the world’s first Large Language Model (LLM) to implement **Intermediate Thinking**, featuring multiple `<think>` and `<ser>` blocks per response

#### Example with MLX-LM-LoRA:

```shell
mlx_lm_lora.train \
--model mlx-community/Josiefied-Qwen2.5-0.5B-Instruct-abliterated-v1 \
--train \
--data mlx-community/dhanishtha-2.0-superthinker-mlx \
--iters 100 \
--max-seq-length 4096
```

#### Example with MLX-LM:

```shell
mlx_lm.lora \
--model mlx-community/Josiefied-Qwen2.5-0.5B-Instruct-abliterated-v1 \
--train \
--data mlx-community/dhanishtha-2.0-superthinker-mlx \
--iters 100 \
--max-seq-length 4096
```

---

### 📊 Overview

* **11.7K multilingual samples** (languages listed below)
* **Instruction-Output** format, ideal for supervised fine-tuning
* **Recursive reasoning blocks** via `<think>...</think>`
* **Emotional state modeling** via `<ser>...</ser>`
* **Prompts include, but are not limited to,** philosophical, technical, personal, ethical, mathematical, and coding problems
* Data is derived from HelpingAI’s flagship LLM [Dhanishtha-2.0](https://huggingface.co/HelpingAI/Dhanishtha-2.0)

#### 🌐 Languages Included

Afrikaans, Arabic, Bulgarian, Catalan, Chinese (Simplified), Czech, Danish, Dutch, English, Estonian, Finnish, French, German, Greek, Hebrew, Hindi, Hungarian, Indonesian, Italian, Japanese, Korean, Marathi, Norwegian, Persian, Polish, Portuguese, Romanian, Russian, Spanish, Swahili, Swedish, Tagalog, Tamil, Telugu, Thai, Turkish, Ukrainian, Urdu, Vietnamese

---

### **⚙️ Intermediate Thinking: The Core Innovation**

**Unlike most LLMs that generate single-pass responses, Dhanishtha-2.0 engages in Intermediate Thinking—the ability to pause, reflect, and refine reasoning throughout its response.**

```plaintext
<think>
This is a physics question about gravitational forces. The Moon exerts a gravitational pull on objects on Earth. The direction of this force would be along the line connecting the object at the equator to the center of the Moon.
</think>

The direction of the gravitational force is along the line connecting the object to the Moon.

<think>
Wait, I should clarify that gravitational force follows Newton's law of universal gravitation. The direction is not static—it varies depending on the Moon's position relative to Earth.
</think>

So, to be more precise, the gravitational force from the Moon on an object at the equator points directly toward the Moon’s position in the sky at that time. As the Earth rotates and the Moon orbits, the direction of this force constantly shifts.

<think>
Maybe I should connect this to real-world effects like ocean tides.
</think>

This changing gravitational pull is what drives ocean tides. When the Moon is overhead, the pull is upward; when it's on the horizon, the pull is nearly horizontal.
```

**This enables:**

* **✅ Self-correction mid-response**
* **🔄 Question clarification and reframing**
* **📚 Multi-perspective synthesis**
* **🤖 Chain-of-self-correction, not just chain-of-thought**

---

### 💬 Structured Emotional Reasoning

The `<ser>...</ser>` block adds structured emotional awareness, encoding the model's contextual frame of mind:

```plaintext
<ser>
Emotion ==> curiosity
Cause ==> ambiguous ethical dilemma
Mind ==> conflicted but analytical
Growth ==> learning to navigate uncertainty
</ser>
```

**what does this mean?**

Each field in the `<ser>` block encodes a distinct aspect of the model's emotional and cognitive state during its response:

* **Emotion**: The model's inference about the user's current emotional state or the emotional tone of the prompt. This could include feelings such as curiosity, empathy, confusion, frustration, excitement, or skepticism. For example, if a user asks a philosophical question, the model might detect "curiosity" or "wonder."
* **Cause**: The underlying reason or trigger for the detected emotion. This is typically derived from the context of the prompt or the nature of the question. For instance, an ambiguous ethical dilemma might cause confusion or introspection, while a technical challenge could prompt determination or focus.
* **Mind**: The model's own cognitive stance or approach as it processes the prompt. This describes how the model is thinking—whether it is analytical, conflicted, cautious, optimistic, skeptical, or open-minded. For example, "conflicted but analytical" indicates the model is weighing multiple perspectives while maintaining logical rigor.
* **Growth**: The developmental or learning trajectory the model is experiencing as it reasons through the prompt. This field reflects how the model adapts, learns, or evolves its understanding in response to the user's input. Examples include "learning to navigate uncertainty," "becoming more empathetic," or "refining problem-solving strategies."

This structured emotional annotation enables the model to:

* Recognize and respond to the user's emotional context more effectively
* Provide transparency about its own reasoning and emotional stance
* Adapt its answers to be more empathetic, nuanced, and context-aware
* Handle complex, ambiguous, or sensitive prompts with greater care and self-reflection

---

### 🧠 Reasoning Workflow

Each example is composed of:

1. Prompt interpretation
2. Initial `<think>` (exploration)
3. Intermediate `<think>` (correction, roughwork)
4. Optional `<ser>` (emotional context)
5. Final answer (often revised or synthesized)

---

### 🧪 Data Collection & Processing

* **Origin**: All samples were extracted from the internal dataset used in training [Dhanishtha-2.0](https://huggingface.co/Abhaykoul/Dhanishtha-2.0), specifically focusing on the model’s Intermediate Thinking capabilities.
* **Filtering**: This dataset comprises a 0.25% uniformly random sample of the full Intermediate Thinking dataset used in Dhanishtha-2.0's training. No manual quality filtering was applied post-sampling, aside from ensuring structural integrity of reasoning blocks.
* **Languages**: The dataset includes examples in 39 languages, such as English, Hindi, Tamil, French, Arabic, Chinese (Simplified), Russian, and more. Samples may be monolingual or code-switched.
* **Validation**:

  * Manual review of 1,000 randomly sampled entries to ensure syntactic correctness of `<think>` and `<ser>` tags
  * Heuristic parsing to flag and discard malformed reasoning/emotion blocks
  * Deduplication pass to eliminate near-identical prompt-response pairs

---

### 🧪 Format

```jsonl
{"messages": [{ "role": "system", "content": ""}, {"role": "user", "content": ""},{"role": "assistant", "content": ""}]}
```

---

### 🔬 Intended Use

* Finetuning multilingual or emotionally aware LLMs
* Evaluating alignment under ethical and moral uncertainty
* Benchmarking multi-phase reasoning or internal monologue generation
* Training COT models that can self-correct or reflect on ambiguity

### 📄 Citation

```bibtex
@misc{HAI2025dhanishtha,
  title        = {Dhanishtha-2.0: A Large Language Model with Intermediate Thinking and Structured Empathy},
  author       = {Abhay Koul and Varun Gupta},
  year         = {2025},
  publisher    = {HelpingAI},
  howpublished = {\url{https://huggingface.co/HelpingAI/Dhanishtha-2.0-SUPERTHINKER}}
}
```

---

🗭 *Dhanishtha-2.0 SUPERTHINKER isn't just data — it's a journey into recursive reflection and structured emotional cognition, empowering language models to reason, self-correct, and grow through multiple phases of Intermediate Thinking.*