---
library_name: transformers
base_model:
- unsloth/Qwen3.6-35B-A3B
tags:
- gguf
- llama.cpp
- image-text-to-text
- vision
- multimodal
- text-generation-inference
- transformers
- unsloth
- conversational
- qwen3_6
- moe
- reasoning
- chain-of-thought
- lora
- sft
- tool-use
- function-calling
- long-context
license: apache-2.0
language:
- en
- zh
- es
- ru
- ja
pipeline_tag: image-text-to-text
datasets:
- Jackrong/Claude-opus-4.7-TraceInversion-5000x
- Jackrong/Claude-opus-4.6-TraceInversion-9000x
---
# 🌟 Qwopus3.6-35B-A3B-v1

## 💡 Base Model Overview


**Qwen3.6-35B-A3B** is an advanced hybrid sparse MoE (Mixture-of-Experts) model developed by Alibaba Cloud. It features 35B total parameters with only 3B active parameters per token, ensuring high inference efficiency. Architecturally, it combines Gated DeltaNet linear attention with standard gated attention layers, routing tokens across **256 experts**. It natively supports a massive **262k context window** and is specifically designed for high-performance agentic coding, deep reasoning, and multimodal tasks.

![Base Model Benchmark Placeholder](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/ztbyGV_zGhzcLuTCSVyq3.png)

---


## 🚀 Model Refinement & Logic Tuning （Qwopus3.6-35B-A3B-v1）

🪐**Qwopus3.6-35B-A3B-v1** is a reasoning-enhanced MoE (Mixture of Experts) model fine-tuned on top of **Qwen3.6-35B-A3B**. 


### 🛠 Training Strategy

The fine-tuning process for this model is structured into **three distinct stages of distributed SFT (Supervised Fine-Tuning)**, progressively scaling reasoning complexity and data diversity. This systematic approach ensures the model inherits the base MoE capabilities while sharpening its logic-handling depth.

Looking ahead, **Reinforcement Learning (RL)** training will be introduced in subsequent versions to further optimize the reasoning paths and alignment performance.

This version uses **LoRA** fine-tuning, but uniquely scales up the trainable parameters, with approximately **9% of the model parameters participating in the update**. This allows for a deeper adaptation of reasoning capabilities while maintaining the efficiency of parameter-efficient fine-tuning. **However, setting trainable parameters to 9% is a risky configuration for this MoE architecture, as it significantly increases the potential for training instability and weight merging conflicts.**

> [!TIP]
>**Vision & Tool Calling Support**: This model supports visual capabilities and tool calling. To enable vision, please place the `mmproj.gguf` file from the [GGUF repository](https://huggingface.co/Jackrong/Qwopus3.6-35B-A3B-v1) into the same directory as the main `.gguf` file.

It is designed for:

- 🧩 More structured reasoning
- 🪶 More consistent answer style
- 🔁 Better cross-source distillation alignment
- ⚡ A stronger foundation for later larger-scale versions

> [!WARNING]
> **Community Release Notice**: Qwopus3.6-35B-A3B-v1 has **not** undergone complete performance evaluation or safety testing. It is released purely as an experimental community version for research and exploration.

* * *

## 🧪 Independent Benchmark Results

### Benchmark Comparison

| Model | Overall | Speed | Quality | Reliability (%) | Tokens/s |
|-------|---------|-------|---------|------------------|----------|
| **🏆 [Jackrong/Qwopus3.6-35B-A3B-v1](https://huggingface.co/Jackrong/Qwopus3.6-35B-A3B-v1)** | **88.6** | 69.3 | **94.2** | **91.7** | 44 |
| [hesamation/Qwen3.6-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled](https://huggingface.co/hesamation/Qwen3.6-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled) | 82.7 | 69.2 | 86.0 | 86.1 | 44 |
| [GestaltLabs/Qwen3.6-35B-A3B-NSC-ACE-SABER](https://huggingface.co/GestaltLabs/Qwen3.6-35B-A3B-NSC-ACE-SABER) | 65.2 | **69.6** | 61.7 | 69.4 | **45** |
| [AtomicChat/Qwen3.6-27B-UDT-MTP](https://huggingface.co/AtomicChat/Qwen3.6-27B-UDT-MTP) | 65.1 | 38.9 | 70.2 | 75.0 | 8 |
| [AtomicChat/Qwen3.6-35B-A3B-UDT-MTP](https://huggingface.co/AtomicChat/Qwen3.6-35B-A3B-UDT-MTP) | 49.4 | — | 62.9 | 59.3 | — |

**🚀 Qwopus3.6-35B-A3B-v1** demonstrates leading performance in this evaluation, particularly excelling in **overall quality** and **reliability**, while maintaining strong inference speed on consumer hardware.

*Benchmark source: Independent test by Tekholms.aptm (@adsilva264). Results reflect quantized GGUF performance under consistent testing conditions.*

> [!TIP]
> **SWE testing is currently underway, and results will be available soon！**

* * *


## 🧪 Data Composition & Context Length Mix

The model was trained on a carefully curated dataset encompassing a wide range of domains, including **mathematics, code, science, multilingual chat, and instruction following**. 

To balance different capabilities, the training data is divided into four main context-length buckets, incorporating a mix of:
- Short format stable samples
- Medium complexity reasoning samples
- Long context high-quality samples
- A small amount of replay samples

**Context Length Distribution:**
- **< 4096 tokens**: Short-context data focused on establishing stable formatting and basic reasoning.
- **4096 - 8192 tokens**: Medium-context data introducing higher reasoning complexity.
- **8192 - 16384 tokens**: Long-context reasoning data, which also includes **10% short sample replay** to prevent catastrophic forgetting of basic instruction-following.
- **16384 - 32K tokens**: A small amount of multi-turn conversations to maintain extended interaction capabilities.

---

## 🎯 Three-Stage Curriculum Learning

**Qwopus3.6-35B-A3B-v1** employs a curriculum learning-style phased reasoning data mix, progressively increasing the difficulty and complexity of the training signals:

1. **Early Stage (Format Establishment):** 
   Focuses on short-to-medium length, format-stable reasoning samples. The primary goal here is to establish a reliable, structured new reasoning format without overwhelming the model with extreme complexity.

2. **Middle Stage (Complexity Scaling & Multi-Teacher Distillation):** 
   Gradually increases the proportion of complex reasoning samples from multiple teacher models. 
   - Distillation data sourced from a **27B model** that closely matches the base model's stylistic distribution, ensuring the capability gap isn't too drastic to learn efficiently.

3. **Final Stage (Long-Context Reinforcement & Anti-Drift):** 
   Strengthens long-context reasoning capabilities. Crucially, this stage retains **short sample replay** to ensure the model maintains its short-context instruction-following ability and minimizes capability drift.

---

## 🚀 Context Length and Long-Context Usage

During fine-tuning, this model was trained with a maximum sequence length of **32K tokens**. The training data mixture was also constructed around samples up to **32K tokens**, so the "Context Length Distribution" shown in this model card reflects the fine-tuning data distribution rather than a hard architectural limit.

The model still inherits the native long-context capability of the Qwen3.6 base model. Therefore, longer context windows such as **128K** or **256K** may be available in compatible inference runtimes, depending on the backend and configuration.

For practical long-context inference beyond 32K, especially when using **llama.cpp / GGUF**, it is recommended to enable **RoPE/YaRN scaling** instead of only increasing `n_ctx` / `--ctx-size`. Directly setting a larger context window without RoPE scaling may work in some cases, but it can be less stable and may not achieve the expected long-context performance.

This is consistent with Qwen community guidance for long-context GGUF usage: **128K context generally requires YaRN/RoPE scaling**, and it is not necessarily enabled by default in llama.cpp. For example, Qwen maintainers have noted that "128K context length needs YaRN" and that it should be explicitly enabled when supported by the runtime.  
Reference: https://huggingface.co/Qwen/Qwen2.5-72B-Instruct-GGUF/discussions/2

Community feedback also suggests that RoPE/YaRN scaling can improve long-context stability for this model family. One user reported that, on **HermesAgent-20**, `Qwopus3.6-35B-A3B-v1` performed better when extending from **32K to 128K via RoPE scaling** than when directly setting a **128K context window** without scaling, with scores of **83 vs. 72** in their setup. This result may vary depending on the backend, quantization type, KV cache settings, hardware, and benchmark configuration, but it is consistent with the recommendation to use RoPE/YaRN scaling for contexts beyond 32K.

Example llama.cpp configuration for extending from 32K to 128K:

```bash
./llama-server \
  -m model.gguf \
  --ctx-size 131072 \
  --rope-scaling yarn \
  --rope-scale 4 \
  --yarn-orig-ctx 32768
```

For 256K context, users may need to adjust the scaling factor accordingly and validate the result in their own workload:

```bash
./llama-server \
  -m model.gguf \
  --ctx-size 262144 \
  --rope-scaling yarn \
  --rope-scale 8 \
  --yarn-orig-ctx 32768
```

Please note that long-context behavior may vary depending on the inference backend, quantization type, KV cache settings, available memory, and task type. For best results, users should benchmark their own target workload when using contexts beyond 32K.

---

### 🚀 Quick Evaluation Summary: Qwopus3.6-35B-A3B-v1

This model represents a significant leap in **inference efficiency** and **one-shot generation quality** compared to previous dense architectures. By leveraging a Hybrid MoE structure (35B total / 3B active parameters) and Gated DeltaNet linear attention, it balances high throughput with deep reasoning capabilities.


![Screenshot 2026-05-07 at 10.27.57 AM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/GddluL8DyZhoPt7qH7AEH.png)


* **Unmatched Speed:** Achieves an average of **161.9 tok/s** on an RTX 5090—a **2.6× speedup** over the 27B dense predecessor—making it one of the fastest high-parameter models available for single-GPU consumer hardware.
* **Production-Grade Frontend Design:** Evaluated as one of the strongest open models for **one-shot HTML/CSS generation**. Unlike models that provide surface-level scaffolding, this model delivers complete, functional pages with complex micro-interactions, animated components, and production-ready logic.
* **Starvation-Free Reasoning:** Successfully resolves the "thinking starvation" issues seen in earlier versions. It maintains robust performance in long-context JSON extraction and multi-step agentic planning, outputting valid structured data even after extensive internal reasoning traces.
* **Architectural Efficiency:** The integration of **Gated DeltaNet** allows for a massive **262K native context window** with optimized VRAM usage, keeping memory requirements nearly flat even as sequence lengths increase.

> [!NOTE]
> **Verdict:** A premier choice for developers requiring a high-throughput, agentic model that excels at UI/UX generation and complex logical deduction on a single-GPU setup. 
> 
> Here is a summary for model card, based on the [🔗 **Qwopus3.6-35B-A3B-v1 comprehensive evaluation report**](https://huggingface.co/spaces/KyleHessling1/qwopus36-35b-a3b-eval) by Kyle Hessling.


![Screenshot 2026-05-07 at 10.28.27 AM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/p_gcu-OJ2qZZbRh0xk-Q9.png)


![Screenshot 2026-05-07 at 10.28.42 AM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/WxSAU2odtUB94Dt6ANVc4.png)


![Screenshot 2026-05-07 at 10.28.56 AM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/vPa3gFqXzFbjN7kv8qrQO.png)


![Screenshot 2026-05-07 at 10.29.09 AM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/PPXgtZRtfzis6UH3y60Rq.png)


![Screenshot 2026-05-07 at 10.35.30 AM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/pj0W7FZPLxHcX7b_cVGW0.png)


---


## ⚠️ Known Training & Deployment Issues

Due to the architectural complexities of the Qwen3.6 MoE models, several technical challenges were encountered during training and weight merging. **Users should be aware of the following potential instabilities:**

> [!CAUTION]
> **MoE Architecture Compatibility Issues**
> 
> - The weight structure of MoE expert layers differs significantly from standard dense models.
> - There are known, easily triggered incompatibilities between **PEFT/LoRA**, **Transformers 5.x's fused expert pattern**, and **Unsloth patches**.
> - Even when using the absolute latest environment and dependencies, merging the LoRA weights into the base model after training may fail or encounter severe compatibility bugs.
> - **Common Error:** You may encounter `ModuleNotFoundError: Could not import module 'Qwen3_5MoeForConditionalGeneration'` or similar structural mismatch errors during the weight merging phase.

If you are attempting to fine-tune or merge weights for this MoE architecture locally, proceed with caution and be prepared to manually patch model definition files or downgrade specific library versions.

---

## 📚 Resources & Guides

👉 **[GitHub Repository: Jackrong-llm-finetuning-guide](https://github.com/R6410418/Jackrong-llm-finetuning-guide.git)**
Visit the repo to dive into the codebase and reproduce the results locally or on Colab.

---

## 🙏 Acknowledgements

Special thanks to:
- The Qwen team for the strong Qwen3.6 MoE base model.
- Unsloth for efficient fine-tuning frameworks.
- Open-source datasets and community contributors.
- **Kyle Hessling** for his generous hardware and equipment support. You can follow him for more updates on X / Twitter: [@KyleHessling1](https://x.com/KyleHessling1).

---

## 📖 Citation

```bibtex
@misc{jackrong_qwopus36_35b_a3b_v1,
  title        = {Qwopus3.6-35B-A3B-v1},
  author       = {Jackrong},
  year         = {2026},
  publisher    = {Hugging Face}
}
```