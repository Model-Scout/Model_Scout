---
base_model: unsloth/Qwen3.5-27B
tags:
- text-generation-inference
- transformers
- unsloth
- qwen3_5
- reasoning
- chain-of-thought
- agent
- sft
- code
- biology
- chemistry
license: apache-2.0
language:
- en
- zh
- ko
- ja
- es
pipeline_tag: image-text-to-text
---

# 🌟 Qwopus3.5-27B-v3.5


![image](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/9EnS13MSxNU3snpAgEiLq.jpeg)



## 💡 Model Overview & v3.5 Design

Qwopus3.5-27B-v3.5 is a **data-scaled continuation** of the Qwopus3.5-27B-v3 model.

The training data in v3.5 is expanded to cover a broader range of domains, including mathematics, programming,puzzle-solving,multilingual dialogue,instruction-following, muti-turn interactions,and STEM-related tasks.

---

Qwopus3.5-27B-v3.5 is a reasoning-enhanced model based on **Qwen3.5-27B**, designed for:

- 🧩 Structured reasoning  
- 🔧 Tool-augmented workflows  
- 🔁 Multi-step agentic tasks  
- ⚡ Token-efficient inference  

Compared with Qwopus3.5-v3, **3.5 version does not introduce a new architecture, RL stage, or template redesign**.  

This version is trained with approximately **2× more SFT data**.

---

## 🎯 Motivation & Generalization Insight

The motivation behind v3.5 comes from a simple observation:

> This work is motivated by the hypothesis that scaling high-quality SFT data may further enhance the generalization ability of large language models.

In v3, Qwopus demonstrates that structured reasoning improves both **accuracy and efficiency**:

- Structured reasoning is more effective than simply mimicking long CoT  
- Act-then-refine is better suited for coding and multi-step tasks  
- Improved reasoning structure enables more reliable use of existing knowledge 


> [!IMPORTANT]  
>This suggests that the improvement is not simply memorization or dataset overlap. Instead, reasoning SFT helps the model:
> - 🧠 Better utilize existing knowledge  
> - 🔍 Activate latent knowledge through structured reasoning  
> - 🏗️ Learn reasoning procedures, not just output format  

---

## 🔬 Supporting Evidence

Recent work:

**Ren et al., 2026 — *Rethinking Generalization in Reasoning SFT*** ([arXiv:2604.06628](https://arxiv.org/abs/2604.06628))


<div align="center">

<img src="https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/5ZY5R4n81okA9glcV9EJV.png" width="85%"/>

</div>

<p align="center"><em>
Short-epoch reasoning SFT can underestimate generalization — in-domain gains may appear early, while out-of-domain improvements often require sufficient optimization.
</em></p>

shows that generalization in reasoning SFT is **not fixed, but conditional** — depending on optimization, data quality, and model capability.

Key takeaways:

- Reasoning SFT can generalize when sufficiently trained (often showing a **dip → recovery** pattern)  
- **High-quality long-CoT data** enables cross-domain transfer  
- **Stronger models learn reasoning structure**, not just longer outputs (14B/27B/32B)  
- Gains are **asymmetric** — reasoning improves, while safety may degrade  

This suggests that reasoning SFT should be viewed as a **dynamic optimization process**, rather than a static training outcome.

---


### 📊 Evaluation results


<div align="center">
<img src="https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/DR9SRmTBDOl9c4S81jBdn.png" width="85%"/>
</div>

<p align="center"><em>
Reasoning-focused SFT improves multi-step reasoning tasks, while introducing mild trade-offs on alignment-sensitive benchmarks.
</em></p>


A third-party benchmark report shows that Qwopus3.5-v3 achieves strong performance across reasoning-heavy tasks, especially on:

- MATH500
- MMLU-Pro
- HumanEval
- GSM8K
- AIME-style reasoning tasks

However, the same results also suggest a **capability trade-off**: reasoning-focused SFT can improve multi-step reasoning while causing mild regressions on some alignment-sensitive or tool-oriented benchmarks.

This supports the view that Qwopus-v3 shifts the model toward **stronger reasoning efficiency and problem-solving ability**, rather than uniform gains across every benchmark.

### 🌍 Preliminary v3.5 comparison on MMLU-Pro subsets

Due to limited compute, v3.5 was evaluated on the **same 280 questions used for v3**, sampled from **7 selected MMLU-Pro categories**.

On this subset:

| Model  | Correct | Total | Accuracy |
|--------|--------|-------|----------|
| **v3**   | 250    | 280   | **89.29%** |
| **v3.5** | 253    | 280   | **✅ 90.36%** |

**✅ Gain:** **+1.07 percentage points**

This suggests that scaling SFT data in v3.5 brings a **small but measurable improvement** on the controlled MMLU-Pro subset.

Since this is not a full MMLU-Pro evaluation, the result should be viewed as a **preliminary reference**, not a definitive benchmark score.


### 🪐 SWE / Agentic Coding Test Report 

![Screenshot 2026-04-16 at 3.16.10 PM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/AsTcE5XOlZc7PqoMYWLyN.png)


![Screenshot 2026-04-16 at 3.16.28 PM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/qcR-CnnE4z_5cBqK-i0Wx.png)



Qwopus3.5-27B-v3.5 was tested on a 44-case SWE-style capability suite covering reasoning, tool calling, structured output, context handling, multilingual responses, programming, and multi-step agentic workflows.

The Q5_K_M GGUF build achieved **43 / 44 passed tests (97.7%)**, including **14 / 15 programming tasks**. The only failure was a unit-test-writing case involving incorrect pytest assertions. Compared with Qwopus3.5-27B-v3, which scored **42 / 44 (95.5%)** on the same suite, v3.5 improved by **+2.2 points**.

The most important gain is in multi-step agentic coding: v3.5 successfully read source code through a tool call, diagnosed a timezone parsing bug, and proposed a fix, while v3 failed to identify the root cause. This suggests that v3.5 is a small but meaningful upgrade over v3, especially for SWE-style workflows involving tool use, code inspection, bug diagnosis, and action planning.

> [!NOTE]
> Throughput differences are excluded from the model-level comparison because both runs use **Q5_K_M GGUF** builds, where quantization choices and runtime environments can affect speed.
> 🏷️ **Acknowledgement:** Special thanks to **Kyle Hessling** for running and sharing the SWE-style capability tests for Qwopus3.5-27B-v3.5.  
> X / Twitter: [@KyleHessling1](https://x.com/KyleHessling1)

---
## 📚 Resources & Guides

👉 **[GitHub Repository: Jackrong-llm-finetuning-guide](https://github.com/R6410418/Jackrong-llm-finetuning-guide.git)**
Visit the repo to dive into the codebase and reproduce the results locally or on Colab.

### 📥 Core Technical Document
**🔗 [Qwopus3.5-27b Complete Fine-Tuning Guide (PDF)](https://github.com/R6410418/Jackrong-llm-finetuning-guide/blob/main/guidePDF/Qwopus3-5-27b-Colab_complete_guide_to_llm_finetuning.pdf)**
* **The Full Pipeline:** A step-by-step walkthrough—from downloading the base model and unifying heterogeneous data, to configuring trainer hyperparameters and publishing to Hugging Face.
* **Beginner Friendly:** Includes an introductory guide to getting started with Google Colab and Unsloth.

> **A Note:**
> My goal isn't just to detail a workflow, but to demystify LLM training. Beyond the social media hype, fine-tuning isn't an unattainable ritual—often, all you need is a Google account, a standard laptop, and relentless curiosity. 
> All training and testing for this project were self-funded. If you find this model or guide helpful, a **Star ⭐️ on GitHub** would be the greatest encouragement. Thank you! 🙏

> [!IMPORTANT]
> The Claude series model optimizations are named under the **Qwopus3.5 series**, with the latest version being **🌟Qwopus3.5-v3.5**.

---

## ⚠️ Limitations

- Possible overfitting if scaling exceeds optimal regime  
- Reasoning may still exhibit instability in edge cases  
- Tool-calling performance depends on environment integration  
- Not all capabilities are fully benchmarked yet  


---

## 🙏 Acknowledgements

Special thanks to:

- Unsloth for efficient fine-tuning  
- Open-source datasets and community contributors  
- Researchers exploring reasoning SFT and generalization  

---

## 📖 Citation

```bibtex
@misc{jackrong_qwopus35_v35,
  title        = {Qwopus3.5-27B-v3.5},
  author       = {Jackrong},
  year         = {2026},
  publisher    = {Hugging Face}
}
```