---
language:
- en
- zh
- ko
- ja
license: apache-2.0
base_model: google/gemma4-26B-it
tags:
- gemma
- gemma4
- instruction-tuned
- reasoning
- alignment
pipeline_tag: text-generation
---

# 🌟 Gemopus-4-26B-A4B-it

> [!NOTE]
> **Gemopus** is an attempt at fine-tuning Gemma 4 with a core philosophy of "stability first".
>  
> While preserving the original reasoning order of **Gemma 4** as much as possible, we conducted targeted refinements for answer quality, structure, clarity, and consistency.
>
> **🍎 Therefore, My fine-tuning strategy chose not to follow other teams in aggressive direct distillation from Claude. Instead, we opted for a more conservative and controllable path.**

## 🎯 Development Motivation & Industry Insights

**Gemopus-4-26B-A4B-it** is a supervised fine-tune version based on the Gemma 4 26B Instruction model.

 * Although this model has "Opus" in its name, it is more of a continuation of the naming convention.
 * There is no need for excessive imagination or superstitious replication of the **"Claude-style chain of thought (CoT)"** found in public distillation corpora. Because judging from the currently available distilled datasets, reasoning text does not necessarily equate to the teacher model's true, faithful, and transferable internal reasoning process. Simple observation suggests it is often more like a summary of the thinking process rather than genuine logically connected **"reasoning."** A series of recent studies have found that models can exhibit post-hoc rationalization in natural scenarios without explicit induction—that is, forming an answer bias first and then coming up with a plausible explanation. Other research has found that CoT faithfulness varies greatly across different model families, and the impact of training methods on faithfulness is often more significant than model scale. In other words, text that "looks like reasoning" is not necessarily a high-quality, transferable supervision signal for reasoning.

> [!IMPORTANT]
> A 2026 self-distillation paper found that while self-distillation can often shorten reasoning traces and improve some in-domain performance, it may also lead to performance degradation in mathematical reasoning. This degradation is correlated with the suppression of uncertainty expressions. The authors reported that on some models and settings, out-of-domain (OOD) performance degradation can be significant. The implication of this result is that reasoning text that appears on the surface to be shorter, cleaner, and more "good at solving problems" does not mean that the student has truly acquired more robust reasoning capabilities.

---


![gemma-4-table_light_Web_with_Arena](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/qWTBY7l4FwIeXU1fp_xJb.jpeg)

## ⚠️ Limitations & Growing Pains of Radical CoT Distillation

When only Supervised Fine-Tuning (SFT) is available, without subsequent Reinforcement Learning (RL) or process supervision, forcefully feeding the student model with potentially non-faithful long reasoning traces together with the final answers introduces substantial hidden risks.

The core issue is that the student model may fail to reliably align the token-level rationale sequence with the latent computational process that actually supports the final decision. As a result, training can easily degenerate into imitation of the *surface form* of reasoning text, rather than genuine internalization of the underlying reasoning mechanism.

In this setting, such long-form reasoning data may improve stylistic resemblance, but not necessarily reasoning fidelity.

By contrast, compared with the Qwen series, **Gemma 4** already exhibits a more structured, orderly, and disciplined reasoning-chat style. It is also significantly less prone to “overthinking” or producing excessively long, uncontrolled reasoning chains. For that reason, there is little value in aggressively reshaping its reasoning style during the SFT stage. Doing so risks disrupting Gemma 4’s native and already strong reasoning rhythm, while offering limited upside in the absence of later-stage alignment methods.

---

## 💡 Model Features & Alignment Optimization

Based on the methodological deduction above, I chose to focus my optimization efforts on the lower-risk, more consistently rewarding levels of **final answer quality and interactive experience**:

* ⚖️ **Overall Style Consistency:** Eliminated the stiff "machine translation tone" and redundant preaching feel inherent in the base model, making conversations more natural, clear, and organized.
* 📐 **Structural & Completeness Enhancements:** Significantly optimized the organizational structure of long responses. The model can more proficiently use Markdown syntax (e.g., lists, bolding) for hierarchical structuring and noise reduction, ensuring key points stand out visually and improving the reading experience.
* 🎓 **Expressive Rigor & Depth of Explanation:** In technical and popular science responses, enhanced the rigor of professional terminology and the ability to explain complex concepts simply, while avoiding mechanical, encyclopedia-like recitation.

---

## 📊 Evaluation Benchmarks (TBD)

> ⏳ Thanks to **[Kyle Hessling](https://x.com/KyleHessling1)** for independently running these benchmarks and sharing the results!


![PNG image](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/Pid5Ih3Dc5W0zUlfSNG4k.png)

![PNG image](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/eLyZW21mQfjjcZQNTyZeu.png)

---

## 🛠️ Best Practices

For the best performance, use these configurations and best practices:

### 1. Sampling Parameters

Use the following standardized sampling configuration across all use cases:

* `temperature=1.0`
* `top_p=0.95`
* `top_k=64`

### 2. Thinking Mode Configuration

Compared to Gemma 3, the models use standard `system`, `assistant`, and `user` roles. To properly manage the thinking process, use the following control tokens:

* **Trigger Thinking:** Thinking is enabled by including the `<|think|>` token at the start of the system prompt. To disable thinking, remove the token.
* **Standard Generation:** When thinking is enabled, the model will output its internal reasoning followed by the final answer using this structure:  
  `<|channel>thought\n` **[Internal reasoning]** `<channel|>`
* **Disabled Thinking Behavior:** For all models except for the E2B and E4B variants, if thinking is disabled, the model will still generate the tags but with an empty thought block:  
  `<|channel>thought\n<channel|>` **[Final answer]**

> [!NOTE]
> Note that many libraries like Transformers and llama.cpp handle the complexities of the chat template for you.

---

## 📚 Resources & Guides

> 🚧 The complete fine-tuning code and related notebooks for this model will be updated soon, please stay tuned!

👉 **[GitHub Repository: Jackrong-llm-finetuning-guide](https://github.com/R6410418/Jackrong-llm-finetuning-guide.git)**  
Welcome to visit this repository to gain a deeper understanding of the codebase and reproduce the training results locally or on Colab.

### 📥 Core Technical Documentation
**🔗 [Qwopus3.5-27b Complete Fine-Tuning Guide (PDF)](https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/guidePDF/Qwopus3-5-27b-Colab_complete_guide_to_llm_finetuning.pdf)**
* **Complete Pipeline:** Step-by-step operational guide—covering the entire process from downloading the base model, heterogeneous data fusion, to configuring training hyperparameters and finally releasing it to Hugging Face.
* **Beginner Friendly:** Includes basic starter tutorials for Google Colab and Unsloth.

> *No one starts out as an expert, but all experts bravely took the first step.*
> 
> All training and testing for this project are self-funded. If you find this model or guide helpful, giving a **Star ⭐️ on [GitHub](https://github.com/R6410418/Jackrong-llm-finetuning-guide.git)** is the greatest encouragement to me. 🙏

---

## 🗺️ Training Pipeline


```text
Base Model (google/gemma4-26B-it)
 │
 ▼
Targeted Supervised Fine-Tuning (SFT) 
(Focus on Answer Quality & Structural Alignment, Retaining Restrained CoT)
 │
 ▼
Gemopus-4-26B-A4B-it
```

### 📚 Dataset Construction & Philosophy
The training data specifically curates highly coherent instruction pairs with optimal structures from the open-source community, alongside natural multi-turn conversations. The goal is to guide the model to learn more mature ways of organizing and presenting conclusions, rather than mechanically imitating "fake chain of thought" without internalized logic.

---

## ⚠️ Known Issues & Ecosystem Compatibility Statement

* **Tool Calling Compatibility:** The Gemma 4 series models still have known compatibility issues with tool calling functionality in local inference ecosystems like **llama.cpp / LM Studio** (including call failures, format mismatches, continuous loops, etc.). This has been widely reported in the community and is not unique to this model. If your workflow heavily relies on tool calling, it is recommended to thoroughly test it before official use, or temporarily consider solutions with more mature ecosystem support.

* **Regarding Fine-Tuning Characteristics of the Gemma Architecture:** From an engineering practice perspective, the Gemma series does exhibit different training dynamics compared to the Qwen series during fine-tuning—including wider loss curve fluctuations and greater sensitivity of gradient stability to hyperparameters. This may be related to Google's model architecture design. Furthermore, the base Gemma 4 model objectively still has a gap compared to the Qwen 3.5 series in certain dimensions of its raw capabilities. We believe that truthfully stating these observations is more beneficial to the technical judgment of the community than selectively avoiding them.

* **Project Positioning:** The core value of Gemopus-4-26B-A4B-it lies in providing an **engineering exploration reference supported by methodology** for SFT fine-tuning under the Gemma 4 architecture, rather than a fully production-ready solution. If you are looking for a productivity model that has undergone more iterative validation and offers more stable ecosystem compatibility, I recommend looking at the **Qwopus-3.5-v3 series**—its performance after fine-tuning is much more robust.

---

## 🍎 Limitations & Usage Recommendations

* **Boundaries of Computation & Knowledge:** Constrained by parameter size, the breadth of its world knowledge and depth of its mathematical and logical reasoning capabilities are still not entirely equivalent to those of frontier models with hundreds of billions of parameters in the cloud (such as GPT-4 or Claude 3.5 Sonnet).
* **Potential Hallucinations:** When dealing with extremely highly-specialized domains, obscure knowledge points, or complex high-level math problems requiring multi-step, long-chain calculations, there is still a possibility of logic drifting or hallucinations.
* **Best Practices:** It is strongly recommended to use it as a **local high-quality text processing and daily logic companion assistant**, particularly suitable for scenarios demanding high response quality and tight structural organization, such as structural summarization, routine copy arrangement, and interactive coding.
* **Disclaimer:** This is an experimental weight optimized independently, emphasizing "stability and methodology" in local interactions. Welcome to freely conduct local deployment tests and share academic discussions.

## 🙏 Acknowledgements

Special thanks to the developers in the open-source community for building such a thriving ecosystem. Thank you to the **Unsloth** team for providing excellent and highly efficient LLM fine-tuning support, and sincere respect to the **Google** team for open-sourcing the outstanding Gemma 4 base model. Finally, thanks to all the researchers who have contributed profound insights into CoT Faithfulness and the interpretability of LLM reasoning. It is exactly these rigorous frontier academic discussions that deeply inspired the core fine-tuning methodology of this project.
