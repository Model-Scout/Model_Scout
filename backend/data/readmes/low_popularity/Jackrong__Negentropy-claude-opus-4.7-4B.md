---
tags:
- unsloth
- qwen
- qwen3.5
- reasoning
- chain-of-thought
- lora
- competitive-programming
- reasoning
- trace-inversion
- negentropy
- distillation
- claude-opus-4.7
- qwen3
- synthetic-data
- chain-of-thought
license: apache-2.0
language:
- en
- zh
- ko
- ja
- ru
base_model:
- Qwen/Qwen3.5-4B
pipeline_tag: image-text-to-text
---

# 🌀 Negentropy-claude-opus-4.7-4B: A Reasoning Experimental Model Based on Trace Inversion

## 💡 Abstract

> **Based on current public information, commercial models like OpenAI's GPT series and Anthropic's Claude series have clearly hidden their true internal reasoning chains. What we ultimately see through APIs or frontend interfaces are often just "Reasoning Bubbles"—highly compressed and summarized versions of the original massive reasoning content.** For small models aiming to improve capabilities through data distillation, these overly compressed reasoning chains fail to provide sufficient step-level learning signals. On the contrary, because the logical leaps are too large and intermediate derivations are missing, forcing small models to learn these summaries directly often leaves them confused and unable to master true reasoning abilities.


![a_high_resolution_infographic_slide_style_figure](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/rBHWdXHXh773XsvHDx3yc.png)



**🚀 Negentropy-claude-opus-4.7-4B** is a **4B-level** lightweight reasoning-enhanced model. Its name is derived from **Negentropy** in information theory, symbolizing the reconstruction of highly ordered, logically rigorous reasoning chains from compressed and fragmented information. It also draws inspiration from the movie ♻️**Tenet** (which I recently watched but didn't quite understand😄).

✨ Unlike other distillation models in the community that perform simple output distillation from closed-source commercial models, this model employs the cutting-edge "**Trace Inversion**" technique: using the **Trace-Inverter-4B** model to restore the compressed "Reasoning Bubbles" leaked by **Claude-Opus-4.7** in public interfaces into full Chains-of-Thought (CoT), using them as high-value supervisory signals for fine-tuning.

> [!IMPORTANT]
> **Core**: This model validates that we can recover logical details with strong supervisory power through reverse engineering. This allows a 4B-level model to achieve a sense of reasoning progression and logical rigor close to top-tier commercial models.

---

## 📖 1. Negentropy Theory: Why Do We Need "Inversion"? (Introduction)

In the current model distillation paradigm, we face a massive "Information Entropy" trap:
- **Commercial Black Boxes**: Models like Claude-Opus or GPT-5.5 often provide only the final answer (Answer-only) or extremely compressed summaries (Reasoning Bubbles) via API.
- **Information Loss**: This compression process significantly increases the data's "entropy," causing small models to learn only "imitated conclusions" rather than "reasoning logic" due to the lack of explanations for intermediate logical leaps.

The core idea of **Negentropy-4.7-4B** is to expand these compressed signals back into detailed, coherent reasoning trajectories through a "Negentropy (reducing disorder)" process. We believe that **the essence of reasoning lies in the process, not the result**. Thinking chains completed through inversion techniques provide small models with higher-quality "logical gradients."

---

## 🚀 2. Model Positioning

This model aims to bridge the gap between "lightweight" and "deep reasoning." It retains the extremely high inference speed and low memory footprint of a 4B model while exhibiting a distinct "Opus style" in its logical expression.

It is best suited for:
- 🧩 **Complex Logical Orchestration**: Tasks requiring multi-step reasoning to reach a conclusion.
- 🧪 **High-Quality Synthetic Data Generation**: Serving as a teacher model to generate initial reasoning chains.
- 💻 **Localized Inference Engine**: Implementing "thinking" processes similar to large models on edge devices.
- 🔄 **Reasoning Alignment Research**: Studying how small models inherit the thinking patterns of large models.

---

## 🧪 3. The Negentropy Pipeline: Data Construction and Training

❤️ This project was completed alongside **Kyle Hessling**. Special thanks to him for providing the compute cluster support that made large-scale inversion data fine-tuning possible. You can find him on X here: 🔗 [@KyleHessling1](https://x.com/KyleHessling1)



![image](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/9Z9lGaQ1_0Ku_FAvUz_Da.png)


The training data for this model went through a "three-stage purification" process:

### 🛠 Stage 1: Trace Capture
We collected and cleaned datasets from the community: `lordx64/reasoning-distill-claude-opus-4-7-max` and `Roman1111111/claude-opus-4.6-10000x`. These include questions, final answers, and accompanying compressed reasoning summaries from **Claude-Opus-4.6/4.7**. At this point, the logical chains in the data are broken.

### 🛠 Stage 2: Trace Inversion
Using a specially trained **Jackrong/Trace-Inverter-4B** model as a "decoder," we used the aforementioned broken summaries as a skeleton, combined with the question and answer, to reverse-generate the full `Full_trace` process.
- **Input**: Problem + Claude-4.7 Answer + Compressed Bubbles
- **Output**: Full Reconstructed Reasoning Trace (Negentropy Trace)

### 🛠 Stage 3: SFT 
Using the **Unsloth** framework for deep fine-tuning, the base model (Qwen3.5-4B) learned these inverted thinking chains, which possess a "strong model logic feel."

> [!TIP]
> **Why 4B?**
> The 4B model has shown surprising "cost-performance" in handling inversion tasks. It can quickly absorb logical templates and maintain extremely high token output speeds during inference, making it ideal for high-frequency reasoning tasks.
> More importantly, there is currently relatively little public data available from commercial API models, which does not support training models that are too large and might lead to underfitting.

---

## ✨ 4. Key Capabilities

- 🌀 **Deep Logical Expansion**: When facing complex problems, the model no longer jumps to conclusions but presents layered thinking steps similar to the Claude style.
- 🎯 **Answer Consistency**: Since the training data originates from Claude-Opus inversions, the model significantly enhances answer accuracy and stability while maintaining a high sense of logic.
- ⚡ **Ultra-Fast Response**: As a 4B model, it can achieve response speeds hundreds of times faster than commercial APIs on consumer-grade GPUs like RTX 4090/5090.
- 🏗 **Structured Thinking**: Native support for `<think>...</think>` tags, with clearly structured output logic that is easy for downstream programs to parse.

---

## 📝 5. Recommended Usage

**Example:**
```text
User: Prove that there is no largest prime number.
Assistant: 
<think>
1. Use proof by contradiction: Assume there exists a largest prime number P.
2. Construct a new number Q, where Q is the product of all known primes plus 1: Q = (2 * 3 * 5 * ... * P) + 1.
3. Analyze the divisibility of Q: Q leaves a remainder of 1 when divided by any of the known primes (2 to P).
4. Conclusion branches:
   - If Q is prime, then Q > P, contradicting the assumption that P is the largest prime.
   - If Q is composite, it must have a prime factor. This prime factor cannot be any of the primes from 2 to P, so there must exist a prime number greater than P.
5. In either case, we derive that there exists a prime number larger than P.
</think>
Conclusion: By proof by contradiction, we have proven that there are infinitely many prime numbers, and no largest prime exists.
```

---

## ⚠️ 6. Limitations

> [!CAUTION]
> - **Hallucination Risk**: While the model has learned the form of reasoning, it may still generate "pseudo-reasoning" that looks plausible but is logically flawed when facing extremely difficult, unknown fields.
> - **Knowledge Boundaries**: The upper limit of the model's capability is restricted by the knowledge base of the base model itself; inversion technology primarily enhances "thinking patterns" rather than "encyclopedic knowledge."
> - **Not for High-Risk Decisions**: Please do not use the generated reasoning processes directly for critical decision-making scenarios such as medical, financial, or legal matters.

---

## 🔭 7. Future Vision

**Negentropy-claude-opus-4.7-4B** is just the first step in our "Negentropy Project."
1. **Scaling Up**: We plan to migrate this method to 9B, 27B, and even 35B MoE models to explore the ceiling of inversion technology on models with larger parameter counts.
2. **Self-Evolution**: Using Reinforcement Learning (RL) to enable the model to learn self-correction and logical closure on top of inversion.

---

## 🙏 8. Acknowledgements
- Thanks to **Claude-Opus-4.7** for providing (albeit passively) high-quality logical signals.
- Thanks to the paper ***How to Steal Reasoning Without Reasoning Traces*** (arXiv:2603.07267) for providing the theoretical foundation.

---

## 📖 9. Citation

```bibtex
@misc{jackrong_negentropy_47_4b,
  title        = {Negentropy-claude-opus-4.7-4B: Reasoning Enhancement via Trace Inversion},
  author       = {Jackrong},
  year         = {2026},
  publisher    = {Hugging Face}
}
```