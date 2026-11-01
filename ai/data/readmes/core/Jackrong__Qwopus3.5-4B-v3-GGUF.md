---
language:
- en
- zh
- ko
license: apache-2.0
base_model: unsloth/Qwen3.5-4B
tags:
- unsloth
- qwen
- qwen3.5
- reasoning
- chain-of-thought
- lora
- competitive-programming
pipeline_tag: image-text-to-text
---

# 🌟 Qwopus3.5-4B-v3

🔥 **Update (April 5):** I’ve released the complete training notebook, codebase, and a comprehensive PDF guide to help beginners and enthusiasts understand and reproduce this model's fine-tuning process. 

> ❤️ Special thanks to the [**Unsloth**](https://unsloth.ai) open-source library and [@KyleHessling1](https://x.com/kylehessling1) for their support.

## 📚 Resources & Guides

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

> [!Note]
> The Claude series model optimizations are named under the **Qwopus3.5 series**, with the latest version being **🌟Qwopus3.5-v3**.

---


## 🎯 Motivation

Recent advances in language agents have predominantly focused on improving reasoning accuracy through Chain-of-Thought (CoT) and self-reflection mechanisms, encouraging models to iteratively refine their reasoning before taking actions.

However, emerging evidence suggests that such **"pre-action overthinking"** is not always optimal for sequential decision-making. Instead, agent performance can be more effectively improved through a **trial-and-error paradigm**, where actions are executed early and refined based on environmental feedback.

### 🔬 Supporting Evidence

- **Reflexion**[^1] demonstrates that agents can significantly improve decision-making by leveraging trial, error, and self-reflection — shifting the role of reflection from *pre-action deliberation* to **post-action correction**, enabling agents to learn from concrete execution outcomes rather than speculative reasoning.

- **Post-failure reflection + retry**[^2] substantially boosts performance:
  - 📈 **+34.7%** on mathematical reasoning tasks
  - 📈 **+18.1%** on function calling tasks

  This provides strong empirical evidence that **reflection is most effective when grounded in execution outcomes**, rather than purely internal reasoning.

### 🧭 My Approach

For multi-step and tool-augmented agent systems, performance should not be optimized solely through deeper pre-execution reasoning. A more effective strategy is an **execution-driven optimization loop** — where agents perform lightweight initial reasoning, act in the environment, and iteratively refine their behavior based on feedback signals.

> **Paradigm Shift:** from **"reason-then-act"** → **"act-then-refine"**
>
> The objective is not to achieve optimal reasoning in a single pass, but to enable robust task completion through iterative interaction and correction.

---


## 💡 Model Introduction

**Qwopus3.5-4B-v3** is a reasoning-enhanced model based on **Qwen3.5-4B**, designed to simultaneously improve reasoning stability and correctness while optimizing inference efficiency — ultimately achieving stronger cross-task generalization capabilities, particularly in programming.

**Key Highlights:**
- 🧩 **Structural Reasoning Optimization** — Refines the fundamental structure of the reasoning process through high-quality reasoning distillation and structural alignment, enabling higher accuracy rates via shorter, more stable reasoning paths.
- 🔧 **Tool-Calling Reinforcement** — Incorporates specialized RL training for tool-calling, optimized for tool-augmented agent frameworks like **OpenClaw**, strengthening stability in continuous task execution and proficiency in tool invocation.
- 🔁 **Act-Then-Refine Paradigm** — Designed for complex, multi-step agentic workflows, aligning with the core motivation of replacing pre-action deliberation with execution-driven refinement.

---
## 🔗 Chain-of-Thought Optimization

### 🚧 The Problem with v2 Distillation

The v2 model was primarily trained through SFT on CoT data distilled from strong teacher models such as Claude. While this can transfer high‑quality reasoning patterns, CoT traces from third‑party datasets do not always faithfully reflect a model’s true internal reasoning process — and after analysis, I found some portions may even be **“fabricated”**, meaning the traces were not actually generated by the claimed teacher model.[^3][^4]

Prior work further shows that CoT explanations can act as **post-hoc rationalizations** rather than genuine step-by-step reasoning[^3]. As a result, student models risk learning:

- Surface-level **pattern matching** instead of underlying reasoning
- **Answer memorization** rather than generalizable problem-solving
- Reduced robustness on out-of-distribution tasks

### ✅ What v3 Does Differently

| | v2 (Distillation) | v3 (Structural Alignment) |
|---|---|---|
| **CoT Source** | Third-party distilled traces | Curated, verifiable reasoning chains |
| **Learning Target** | Imitate teacher outputs | Learn process-level reasoning |
| **Reasoning Style** | Compressed, potentially fabricated | Explicit, step-by-step, faithful |
| **Robustness** | Lower on unseen tasks | Higher generalization |

v3 focuses on improving the **faithfulness, completeness, and structural clarity** of reasoning traces. Instead of imitating compressed teacher CoT, the model is trained to produce more explicit and verifiable intermediate steps — enabling a transition from **“answer imitation”** to **process-level reasoning learning**.

This improves both the interpretability and reliability of the reasoning process, providing a more stable foundation for downstream multi-step and agent-based tasks.

> ⚠️ **Side Effect:** The generated CoT length in v3 will be **significantly longer** than v2, as a direct consequence of more explicit intermediate reasoning.

---

### 🍎 Qwopus3.5-4B-v3: Humaneval Benchmark Evaluation 

> 🔬 **Inference Setup:** All models were evaluated under the **Unsloth** runtime using **bfloat16 (BF16)** precision — optimally balanced for numerical range and memory efficiency at 4B scale. Answer verification, partial CoT adjudication, and statistical analysis were cross-validated by **GPT-4.5-Pro (Thinking)** and **Claude Opus 4.6 (Thinking)** to ensure reproducibility.

### 📊 HumanEval — 164-Task Full Benchmark

Three 4B-scale Qwen-family models were evaluated under a **conservative manual adjudication protocol**, addressing:
- 🧹 Code-extraction pollution
- ✂️ Answer / code separation issues
- 🗂️ Formatting noise in otherwise correct outputs

> 🏆 **Result:** Under this fair and strict evaluation setting, **Qwopus3.5-4B-v3 achieves the best strict overall score of 75.61% (124/164)** — outperforming **Qwen3.5-4B** (72.56%, 119/164) and **Claude-Distilled-v2** (69.51%, 114/164), while simultaneously reducing the number of manual rescues required.

| Model | Base Pass | Plus Pass | vs. Qwen3.5-4B |
| :--- | :---: | :---: | :---: |
| 🥇 **Qwopus3.5-4B-v3** | **77.44%** (127/164) | **75.61%** (124/164) | 📈 **+3.05 pp** |
| Qwen3.5-4B | 76.83% (126/164) | 72.56% (119/164) | — Baseline — |
| Claude-Distilled-v2 | 73.17% (120/164) | 69.51% (114/164) | 📉 −3.05 pp |

---


## 🗺️ Training Pipeline Overview

```text
Base Model (Qwen3.5-4B)
 │
 ▼
Qwen3.5-4B fine-tuned with Unsloth
 │
 ▼
Supervised Fine-Tuning (SFT) + LoRA
(Response-Only Training masked on "<|im_start|>assistant\n<think>")
 │
 ▼
Qwopus3.5-4B-v3
```

### 🧠 Example of Learned Reasoning Scaffold

The model includes targeted optimizations addressing Qwen3.5's tendency toward excessive or repetitive reasoning on simple queries. By distilling the structured reasoning habits of top-tier models like Claude Opus, Qwopus3.5-4B-v3 adopts a highly organized, step-by-step cognitive layout.


```text
Example：The user is asking about [Topic] and how it differs from [Topic B]. This is a [Task type] question. Let me break this down:

1. What is [Topic A]?
   - [Fact/Mechanism 1]
   - [Fact/Mechanism 2]
2. What is [Topic B]?
   - [Fact/Mechanism 1]
3. Key differences:
   - [Comparison Point 1]
   - [Comparison Point 2]

Let me make sure to be accurate: [...]
Actually, I should double-check: is [Fact] used before [Fact]? Yes, typically...
Let me provide a clear, well-structured answer:
```


### 📚 Training Data
The model was fine-tuned on a **high-fidelity reasoning dataset**, which was meticulously curated from a blend of premium open-source sources on Hugging Face. This dataset is the result of a rigorous **mixing and cleaning process**, specifically designed to filter out low-quality responses and ensure consistently strong logical performance across diverse analytical domains.

> *(Rest assured, the entire process is strictly by-the-book and 100% compliant with all terms and open-source licenses!)*


## ⚠️ Limitations & Intended Use
- **Hallucination Risk:** While reasoning is strong, the model remains an autoregressive LLM; external facts provided during the thinking sequence may occasionally contain hallucinations if verifying real-world events.
- **Intended Scenario:** Best suited for offline analytical tasks, coding, math, and heavy logic-dependent prompting where the user needs to transparently follow the AI's internal logic.
- This model is a test version intended solely for learning and demonstration purposes, and is for academic research and technical exploration use only.
- **Developer Disclaimer:** This is an independent, personal project. Since the developer lacks the specialized technical resources and infrastructure of a large-scale industrial lab, the model's reasoning chain (CoT) may occasionally exhibit instability, logic loops, or reasoning drift. Users are advised to use this model with these experimental limitations in mind.

> **Note:** The test results presented here differ from the scores on the 4B-v2 model card because the context length was increased for this evaluation. Consequently, the number of tasks affected by context window truncation has changed for each model, leading to different final scores. Please ensure comparisons are made under the same variable settings.

All post-evaluation standard result files will be uploaded to this repository for transparency and reproducibility. These include:
- `Jackrong_Qwen3.5-4B-Claude-4.6-Opus-Reasoning-Distilled-v2_humaneval_all_evalonly_eval_results`
- `Jackrong_Qwopus3.5-4B-v3-test1_humaneval_all_evalonly_eval_results`
- `qwen_Qwen3.5-4B_humaneval_all_evalonly_eval_results`

⚠️ **Note on evaluation artifacts.**  
The released result files are based on **raw model generations**, which may contain formatting issues (e.g., Markdown wrappers, answer/code mixing), truncation, or minor token-level corruption. As an independent project operating under limited resources, the evaluation scope here is intentionally focused rather than exhaustive — a comprehensive, multi-domain assessment comparable to large institutional releases was not feasible. Capabilities beyond those benchmarked remain unverified, and users are encouraged to evaluate suitability against their own task requirements before adoption.


## 🙏 Acknowledgements
Significant thanks to the [Unsloth AI](https://unsloth.ai/) team for making rapid fine-tuning of large LLM models accessible. Additionally, we acknowledge Qwen internally, and the open-source community developers producing exceptional distilled datasets.

This qwen3_5 model was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth) and Huggingface's TRL library.

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)

## References

[^1]: Shinn, N., Cassano, F., Berman, E., Gopinath, A., Narasimhan, K., & Yao, S. (2023).  
*Reflexion: Language Agents with Verbal Reinforcement Learning*.  
arXiv:2303.11366.

[^2]: Bensal, S., Jamil, U., Bryant, C., Russak, M., Kamble, K., Mozolevskyi, D., Ali, M., & AlShikh, W. (2025).  
*Reflect, Retry, Reward: Self-Improving LLMs via Reinforcement Learning*.  
arXiv:2505.24726.  https://arxiv.org/abs/2505.24726

[^3]: Anthropic (2025). *Reasoning Models Don't Always Say What They Think*.  
https://www.anthropic.com/research/reasoning-models-dont-say-think  

[^4]: Lyu et al. (2023). *Faithful Chain-of-Thought Reasoning*. ACL.  
https://aclanthology.org/2023.ijcnlp-main.20/


## 📖 Citation

If you use this model in your research or projects, please cite:

```bibtex
@misc{jackrong_qwen35_4b_v3
  title        = {Jackrong/Qwopus3.5-4B-v3},
  author       = {Jackrong},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/Jackrong/Qwopus3.5-4B-v3}}
}
```