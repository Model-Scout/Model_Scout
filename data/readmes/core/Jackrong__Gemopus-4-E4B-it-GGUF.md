---
language:
- en
- zh
- ko
- ja
license: apache-2.0
base_model: google/gemma4-E4B-it
tags:
- gemma
- gemma4
- edge-ai
- instruction-tuned
- reasoning
- privacy
- human-preference-alignment
pipeline_tag: image-text-to-text
---

# 🌟 Gemopus-4-E4B-it

## 🎯 Development Motivation & Industry Insights

![gemma-4-table_light_Web_with_Arena](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/ekZQqAoYxyZ4GJ3zU8LSp.jpeg)

I still remember the days of running the Llama 3.1 8B Instruct model on my MacBook Air M1. Back then, I could hardly imagine that in just two years, a model with reasoning capabilities comparable to the **GPT-4** of that era would be running locally on my phone. Currently, Edge AI is experiencing a paradigm shift, transitioning from the cloud down to local environments. Tech giants are embedding AI capabilities deep into the bedrock of operating systems with unprecedented determination. Without a doubt, this form of local AI, which **combines ultra-low latency with absolute privacy**, represents the standard paradigm for future end-user devices.
> [!NOTE] Following this trend, I created **🪐 Gemopus-4-E4B-it**. This is an instruction-tuned model derived from the deep fine-tuning of the latest edge computing large model, **Gemma-4-E4B-it**.

My core vision is to **break down the barriers of expensive GPU computing power**, allowing every user with an ordinary **iphone, tablet, or thin-and-light Mac (such as MacBook Air, MacBook Neo)** to fluently run their own powerful AI assistant locally, eliminating the risk of data privacy leaks. By offloading high-frequency basic reasoning tasks (such as text translation, rewriting, summarization, error correction, short text generation, simple Q&A, etc.) to edge devices—especially since these questions often involve personal data that requires the most desensitization—we not only significantly reduce the cost of cloud API calls but also fundamentally guarantee the absolute security of sensitive personal data.

---


## ⚠️ Limitations & Growing Pains of the Original Gemma-4-E4B-it

Admittedly, although the official original Gemma 4-E4B-it possesses an excellent foundation for reasoning, its native instruction alignment strategy also introduces extremely localized drawbacks that can be highly frustrating during daily interactions on edge devices:

1. **Pedantic "Wikipedia Tone":** Even when faced with the most everyday casual chat or brief instructions, it habitually outputs lengthy, rigid, encyclopedia-like objective explanations, severely lacking emotional value and a human touch.
2. **Stiff Translation Tone & "Machine Flavor":** In non-English contexts such as Chinese, its expressions often seem dry, lack warmth, and are filled with a heavy "machine-translated feel" and cold statements.
3. **Inefficient "Manual-style" Preaching:** The official native model carries overly rigid safety and objectivity constraints. This results in it frequently appending redundant disclaimers, or even forcibly delivering long-winded lectures in situations where no preaching is needed whatsoever, severely slowing down the communication efficiency on edge devices which should be crisp and sharp.

It is precisely because I **do not want a machine locally that merely recites "Wikipedia" stiffly or acts like a cold instruction manual every day**, that I was driven to decide on a complete "personality remodeling" and alignment fine-tuning for it.

---

## 💡 Model Features & Alignment Optimization

Currently, the full-modal Gemma 4-E4B-it stands as the optimal choice for an edge instruction model. Empowered by Apple Silicon and its high-speed unified memory architecture, models of this scale exhibit staggering inference performance on edge devices: On the latest **iPhone 17 Pro Max**, its native inference speed steadily maxes out at **45 ~ 60 tokens/s**; while on everyday thin-and-light laptops like the **MacBook Air (M3/M4)**, paired with local frameworks like MLX, it can easily burst out a blazing fast response of **90 ~ 120 tokens/s**, truly realizing instantaneous answers that break the shackles of network dependencies.

>⚠️ Note: The above performance figures are based on publicly available online benchmarks and community reports. Actual results may vary depending on hardware configuration, runtime environment, and model version—please refer to real-world testing for accurate performance.

However, to transform this cold "hardware speed" into an interaction warmth that end-users can genuinely perceive, **Gemopus-4-E4B-it** underwent further deep **Human Preference Alignment** atop this highly efficient base.

I focused on achieving leaps in the user experience across the following three dimensions:

* 🗣️ **Native Tone Adaptation:** I completely stripped away the original Gemma model's "machine translation tone" and its stiff "manual-style" proclamations that read like Wikipedia. The fine-tuned language style is much more intimate and natural, closely mirroring the real communication habits of human users, significantly reducing the AI's preaching feel.
* 🧠 **Deep Contextual Awareness:** Interaction is no longer a simple "Q&A." The model can more astutely capture the deep context and implicit needs in multi-turn dialogues, actively guiding thought processes and providing insights that are both inspiring and warm.
* 🎨 **Structural Readability:** The layout and structure of the model's outputs have been remodeled. The answers are hierarchically clear with appropriate detail. It proficiently leverages Markdown syntax (like lists and bolding) to denoise information, delivering an excellent visual reading experience while ensuring information density.

---

## 📊 Evaluation Benchmarks (TBD)

> ⏳ Thanks to **[Kyle Hessling](https://x.com/KyleHessling1)** for independently running these benchmarks and sharing the results!


![Screenshot 2026-04-09 at 3.02.33 PM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/Vmlvdaz-8ryqR7wrqsGqp.png)


![Screenshot 2026-04-09 at 3.02.54 PM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/meQ9YjfHY5FDnQZrOiI2d.png)


![Screenshot 2026-04-09 at 3.03.14 PM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/pXrhANeflWWYqBvylDCG4.png)


![Screenshot 2026-04-09 at 3.03.23 PM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/SqUrgHGtQYTkYWlmuxV3_.png)

---

# 📚 Resources & Guides

> 🚧 I’ll be updating the fine-tuning code for this model very soon—please stay tuned!

👉 **[GitHub Repository: Jackrong-llm-finetuning-guide](https://github.com/R6410418/Jackrong-llm-finetuning-guide.git)**
Visit the repo to dive into the codebase and reproduce the results locally or on Colab.

### 📥 Core Technical Document
**🔗 [Qwopus3.5-27b Complete Fine-Tuning Guide (PDF)](https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/guidePDF/Qwopus3-5-27b-Colab_complete_guide_to_llm_finetuning.pdf)**
* **The Full Pipeline:** A step-by-step walkthrough—from downloading the base model and unifying heterogeneous data, to configuring trainer hyperparameters and publishing to Hugging Face.
* **Beginner Friendly:** Includes an introductory guide to getting started with Google Colab and Unsloth.
* *Feedback welcome! If you spot any areas for improvement, please let me know and I will update it promptly.*

> **A Note:**
> My goal isn't just to detail a workflow, but to demystify LLM training. Beyond the social media hype, fine-tuning isn't an unattainable ritual—often, all you need is a Google account, a standard laptop, and relentless curiosity. 
> 
> *No one starts as an expert, but every expert was once brave enough to begin.*
> 
> All training and testing for this project were self-funded. If you find this model or guide helpful, a **Star ⭐️ on GitHub** would be the greatest encouragement. Thank you! 🙏

---

## 🗺️ Training Pipeline

This model adopts a high-standard SFT pipeline with the same specifications as large instruction reasoning models:

```text
Base Model (gemma4-E4B-it)
 │
 ▼
Supervised Fine-Tuning (SFT) + Human Preference 
 │
 ▼
Gemopus-4-E4B-it
```

### 📚 Dataset Construction
The fine-tuning process heavily relies on a meticulously constructed **high-quality human preference instruction dataset**. This dataset not only cleaned and mixed high-quality instruction pairs from the open-source community, but was also specifically injected with a massive amount of interactions, natural dialogues, and challenging deep-analysis samples. This ensures that the model consistently maintains a high level of helpfulness and human touch when deployed on edge devices.

---

## ⚠️ Limitations & Usage Recommendations

* **Compute & Knowledge Boundaries:** This model is designed specifically for ultra-fast local inference on edge devices (like thin-and-light laptops and smartphones). Constrained by its smaller parameter size, the breadth of its world knowledge and extremely deep logical reasoning capabilities cannot rival those of hundred-billion-parameter behemoths in the cloud.
* **Potential Hallucinations:** When dealing with extremely obscure domains, niche knowledge, or complex math problems that require multi-step long-chain calculations, hallucinations may still occur.
* **Best Practices:** It is strongly recommended to use it as a **local high-frequency text processing assistant**, ideal for scenarios involving daily copywriting assistance, code completion, formatting, and summary extraction, especially those that involve privacy or are latency-sensitive.
* **Disclaimer:** This is an experimental weight optimized independently based on edge interaction needs. You are welcome to conduct local deployment testing and academic exchanges at any time.

## 🙏 Acknowledgements
Special thanks to the fellow developers in the open-source community who provided powerful computing resources and base ecosystem support. In particular, thanks to the **Unsloth** team for providing excellent tools for the efficient fine-tuning of large models, and to **Google** for open-sourcing the excellent Gemma 4 series base models.

