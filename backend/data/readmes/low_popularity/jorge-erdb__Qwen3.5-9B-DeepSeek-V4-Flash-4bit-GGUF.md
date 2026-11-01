---
base_model:
- Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash
tags:
- text-generation-inference
- transformers
- unsloth
- qwen3_5
- reasoning
- distillation
- deepseek
- deepseek-v4
- sft
- long-cot
- chain-of-thought
- efficient-inference
- agent
- multilingual
- 4bit
license: apache-2.0
language:
- en
- zh
- ko
- ja
- es
- ru
pipeline_tag: image-text-to-text
datasets:
- Jackrong/DeepSeek-V4-Distill-8000x
---
# Qwen3.5-9B-DeepSeek-V4-Flash-GGUF

GGUF quantizations of [Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash](https://huggingface.co/Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash), Jackrong's distillation of DeepSeek-V4's reasoning into the Qwen3.5-9B architecture using the [DeepSeek-V4-Distill-8000x](https://huggingface.co/datasets/Jackrong/DeepSeek-V4-Distill-8000x) dataset.

---

## Quantization Details

| Detail | Value |
|---|---|
| Quants | Q4_K_M, **D-IQ4_NL** (dynamic) |
| Quantized by | [jorge-erdb](https://huggingface.co/jorge-erdb) |
| Method | [llama.cpp](https://github.com/ggml-org/llama.cpp) |
| Source model | [Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash](https://huggingface.co/Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash) (BF16) |

### Dynamic IQ4_NL Recipe

The **D-IQ4_NL** variant uses a custom tensor-level precision recipe rather than a uniform IQ4_NL quantization.

---

## Download

```bash
pip install -U "huggingface_hub[cli]"

# Q4_K_M (smallest, broadest backend support)
huggingface-cli download jorge-erdb/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF --include "*Q4_K_M.gguf" --local-dir ./

# D-IQ4_NL (dynamic, Q6_K-protected attention/SSM)
huggingface-cli download jorge-erdb/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF --include "*D-IQ4_NL.gguf" --local-dir ./
```

---

> [!IMPORTANT]
> ## Apple Metal Backend Warning
>
> **D-IQ4_NL uses non-linear quantization on FFN tensors.** It performs sub-optimally on Apple's Metal backend due to the lack of native support for non-linear dequantization kernels. If you are running on an Apple Silicon Mac with GPU offloading via Metal, you will likely experience:
>
> - Slower inference compared to linear quants of similar size (e.g., Q4_K_M)
> - No speed benefit from the ARM weight repacking that IQ4_NL supports on CPU
>
> **If you're on Apple Metal, use the Q4_K_M variant instead.** D-IQ4_NL is best suited for CUDA (NVIDIA GPU) or CPU-only inference.

---

## Credits

- **Quantization**: [jorge-erdb](https://huggingface.co/jorge-erdb)
- **Distillation & training**: [Jackrong](https://huggingface.co/Jackrong) — Qwen3.5-9B-DeepSeek-V4-Flash
- 
---
# 🌟 Qwen3.5-9B-DeepSeek-V4-Flash

## 💡 Model Overview & Design

![ChatGPT Image Apr 24, 2026 at 04_32_09 PM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/J3m3YKzmCmDtbKOZNPCW-.png)

> [!NOTE]
> **Qwen3.5-9B-DeepSeek-V4-Flash** is an efficient reasoning model distilled using high-quality data from **DeepSeek-V4**.


- By leveraging the dataset **Jackrong/DeepSeek-V4-Distill-8000x**, this model successfully transfers the advanced structured reasoning and multi-step problem-solving capabilities of the DeepSeek-V4 architecture into the highly efficient **Qwen3.5-9B** parameter space. 

- This model was trained in an **Unsloth** environment, prioritizing stable gradient propagation and rigorous data curation to ensure the distillation process avoids merely learning "hollow chain-of-thought" and instead captures genuine logical generalization.

Designed for:
- 🧩 **Structured Reasoning**: Inheriting DeepSeek-V4's deep logic capabilities.
- ⚡ **Flash Inference**: Maintaining the token-efficiency and speed of the 9B parameter size.
- 🔧 **Tool-augmented Workflows**: Reliable agentic action generation.

---

### 🍎 About the Teacher Model: DeepSeek-V4

![dsv4_performance](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/iBQ7B-z3bpdmsJkdmEPGC.png)


**[DeepSeek-V4](https://huggingface.co/collections/deepseek-ai/deepseek-v4)** is the latest flagship open-source model series from DeepSeek, engineered for extreme efficiency, million-token long context (1M), and advanced Agentic workflows. As the source for this distillation, DeepSeek-V4 provides the high-fidelity reasoning signals necessary to push a 9B model beyond its architectural limits.

**Key Technical Strengths of the Teacher Model:**

* **🏆 World-Class Reasoning & Coding:** DeepSeek-V4 demonstrates elite performance in mathematics (MATH-500), STEM subjects, and real-world software engineering (SWE-bench). Its "Think" modes provide the sophisticated Long-CoT (Chain-of-Thought) traces that define this model's logic.
* **🧠 Architectural Innovation:** * **Hybrid Attention & DSA:** Features Token-level compression and DeepSeek Sparse Attention, which reduces KV Cache memory overhead by up to 90%, allowing for highly efficient long-context processing.
    * **Engram Memory & mHC:** Utilizes Manifold-constrained Hyper-connections to decouple factual knowledge retrieval from dynamic logical reasoning, ensuring exceptional stability and generalization.
* **🤖 Agent-Centric Design:** Specifically optimized for multi-step tool calling and complex environment interaction, ensuring that the distilled knowledge includes reliable "how-to-act" procedures, not just "how-to-talk."

By distilling from **DeepSeek-V4-Flash**, we have successfully mapped the high-density logic of a trillion-parameter class model onto the agile and high-speed **Qwen3.5-9B** framework.

---

## 🤝 Collaboration & Training Details
This model is the result of a close collaboration with hardware engineer **Kyle Hessling**. He generously provided the crucial compute equipment and managed both the rigorous post-training testing and continuous server maintenance.
I want to express my gratitude to Kyle for his invaluable support! 
You can find him on X/Twitter here: [@KyleHessling1](https://x.com/KyleHessling1)

**Training Infrastructure & Configuration:**
- 🖥️ **Hardware:** NVIDIA DGX
- 💾 **Training Data:** DeepSeek-V4-Distill-8000x
- 🧪 **Training Method:** Distillation

---

## 🎯 Motivation & Distillation Insights
- 🧠 **Latent Knowledge Activation**: DeepSeek-V4's reasoning traces help the Qwen3.5-9B model activate its existing latent knowledge more effectively.
- 🏗️ **Learning Procedures**: The model learns actual problem-solving procedures, not just the output format.
- 🚀 **Efficiency**: The 8000x dataset provides a dense signal, allowing the 9B model to converge on reasoning tasks much faster than traditional large-scale SFT.

---

## 📊 Evaluation
> [!IMPORTANT]
> This is an early controlled **Q5_K_M** comparison between **Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash** and the official **Qwen3.5-9B** base model.  
>  
> This evaluation was completed by **Kyle Hessling**, who ran the same evaluation suite twice under the same local inference conditions: once on the DeepSeek-V4 distill model and once on the official Qwen3.5-9B base model.  


- ❤️ Special thanks to Kyle for the careful post-training testing and detailed comparison report. You can find him on X/Twitter here: **[@KyleHessling1](https://x.com/KyleHessling1)**.
- 📄 Full evaluation report: **[KyleHessling1/jackrong-deepseek-9b-eval](https://huggingface.co/spaces/KyleHessling1/jackrong-deepseek-9b-eval)**.

![Evaluation Report](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/GtqFy-my7GXQ3xRRXTxYp.png)

![Comparison Method](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/-w7X_kpErCPYV5QHB-jw3.png)

![Agentic Reasoning Results](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/DFAx6miaEoXuqmSPSSJAC.png)

![Front-end Design Results](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/W_mUxkwfRYcZOyGy4sPx2.png)

![Tool Calling Results](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/rCJPUY0KnB8mkyI7yAI-3.png)

![Evaluation Setup](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/6mzcBTSgLLT_kL1dHafAy.png)

---
## 🔬 Supporting Evidence

Recent work and empirical tests support this distillation approach:

**Ren et al., 2026 — *Rethinking Generalization in Reasoning SFT*** ([arXiv:2604.06628](https://arxiv.org/abs/2604.06628))

The paper suggests that generalization in reasoning SFT is conditional. 
Key takeaways:
- **High-quality long-CoT data** from DeepSeek-V4 enables cross-domain transfer.
- **Optimization Discipline**: Short, highly-curated distillation (8000 examples) prevents the model from overfitting to the teacher's stylistic quirks while preserving the core reasoning engine.

---

## 🛠️ Best Practices

For optimal performance, we recommend the following generation parameters:

* `temperature=0.7` to `1.0` (Use lower temperature for strict coding tasks, higher for creative reasoning)
* `top_p=0.95`

When interacting with the model, using a structured prompt template or standard ChatML format will yield the best reasoning results.

---

## 📚 Resources & Guides

👉 **[GitHub Repository: Jackrong-llm-finetuning-guide](https://github.com/R6410418/Jackrong-llm-finetuning-guide.git)**
Visit the repository to dive into the codebase and reproduce the results locally or on Colab.

### 📥 Core Technical Document
**🔗 [Complete Fine-Tuning Guide (PDF)](https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/guidePDF/Qwopus3-5-9b-Colab_complete_guide_to_llm_finetuning.pdf)**

> **A Note:**
> My goal isn't just to detail a workflow, but to demystify LLM training. Beyond the social media hype, fine-tuning isn't an unattainable ritual—often, all you need is a Google account, a standard laptop, and relentless curiosity. 
> All training and testing for this project were self-funded. If you find this model or guide helpful, a **Star ⭐️ on GitHub** would be the greatest encouragement. Thank you! 🙏

---

## ⚠️ Limitations

- **Parameter Constraints**: While enhanced by DeepSeek-V4 distillation, the model is still bound by the 9B parameter limits and may struggle with extremely obscure knowledge.
- **Over-reasoning**: On very simple queries, the model might still attempt to produce a lengthy reasoning chain due to the SFT bias.
- **Safety Trade-offs**: Asymmetric gains mean that while reasoning improves, certain alignment-sensitive behaviors might regress.

---

## 🙏 Acknowledgements

Special thanks to:
- **DeepSeek Team** for the foundational advancements in the V4 architecture.
- **Unsloth** for efficient fine-tuning frameworks.
- Open-source datasets and community contributors.
- Researchers exploring reasoning SFT and distillation.

---

## 📖 Citation

```bibtex
@misc{jackrong_qwen35_9b_deepseek_v4_flash,
  title        = {Qwen3.5-9B-DeepSeek-V4-Flash},
  author       = {Jackrong},
  year         = {2026},
  publisher    = {Hugging Face}
}
```