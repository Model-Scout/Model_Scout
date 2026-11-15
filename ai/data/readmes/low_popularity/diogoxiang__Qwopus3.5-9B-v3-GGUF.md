---
language:
- en
- zh
- ko
license: apache-2.0
base_model: unsloth/Qwen3.5-9B
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

# 🌟 Qwopus3.5-9B-v3

## 💡 Model Introduction
**Qwopus3.5-9B-v3** is a reasoning-enhanced model based on Qwen3.5-9B. Its core objective is to simultaneously improve reasoning stability and correctness while optimizing inference efficiency, ultimately achieving stronger cross-task generalization capabilities—particularly in programming.

By continuing to optimize the fundamental structure of its reasoning process alongside high-quality reasoning distillation and structural alignment, it enables the model to achieve higher accuracy rates through shorter, more stable reasoning paths.

---

### 🍎 Qwopus3.5-9B-v3: Humaneval Benchmark Evaluation 
>Inference for models was conducted under the Unsloth runtime environment using **bfloat16 (BF16)** precision, which provides a balance of numerical range and memory efficiency well-suited to 9B-scale inference. Answer verification, partial chain-of-thought adjudication, and statistical analysis were cross-validated using **GPT-4.5-Pro (Thinking)** and **Claude Opus 4.6 (Thinking)** to ensure accuracy and reproducibility of the evaluation outcomes.

**HumanEval**  
I evaluated three 9B-scale Qwen-family models on the full 164-task HumanEval benchmark under a task-level adjudication protocol that resolves code-extraction pollution, answer/code separation issues, and clearly inferable truncated outputs using raw generations. Under this fair and strict evaluation setting, **Qwopus3.5-9B-v3 achieves the best base pass@1 of 87.80% (144/164)**, outperforming both **Qwen3.5-9B** (82.93%, 136/164) and **Claude-Distilled-v2** (82.32%, 135/164). Furthermore, on the stricter **plus pass@1** evaluation, Qwopus3.5-9B-v3 also extends its lead to **82.93% (136/164)** compared to **77.44% (127/164)** for the official baseline (+5.49 pp) and **78.66% (129/164)** for the distilled variant.

| Model | Base pass@1 | Plus pass@1 | Rescues (From GPT) | Improvement vs Qwen3.5-9B |
|---|---|---|---|---|
| **Qwopus3.5-9B-v3** | **87.80% (144/164)** | **82.93% (136/164)** | 1 | 📈 **Base: +4.87 pp / Plus: +5.49 pp** |
| Qwen3.5-9B | 82.93% (136/164) | 77.44% (127/164) | 2 | Baseline |
| Claude-Distilled-v2 | 82.32% (135/164) | 78.66% (129/164) | 0 |  📉 Base: -0.61 pp / 📈 Plus: +1.22 pp vs Qwen3.5-9B |


![Screenshot 2026-03-31 at 5.44.04 PM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/qdrGIdxunjK1i59L-Yp7n.png)


![Screenshot 2026-03-31 at 5.44.38 PM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/4kEsIn34b8-v_WIxxT4_F.png)




> **Note:** The test results presented here differ from the scores on the 9B-v2 model card because the context length was increased for this evaluation. Consequently, the number of tasks affected by context window truncation has changed for each model, leading to different final scores. Please ensure comparisons are made under the same variable settings.


All post-evaluation standard result files will be uploaded to this repository for transparency and reproducibility. These include:
- `Jackrong_Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2_humaneval_all_evalonly_eval_results`
- `Jackrong_Qwopus3.5-9B-v3-test1_humaneval_all_evalonly_eval_results`
- `qwen_Qwen3.5-9B_humaneval_all_evalonly_eval_results`

⚠️ **Note on evaluation artifacts.**  
The released result files are based on **raw model generations**, which may contain formatting issues (e.g., Markdown wrappers, answer/code mixing), truncation, or minor token-level corruption. 

---

### 🏃 Qwopus3.5-9B-v3: MMLU-Pro Benchmark Evaluation
I evaluated on **280 MMLU-Pro questions** across the following domains: Biology, Chemistry, Computer Science, Health, Mathematics, Physics, and Other Sciences.

All question IDs are identical across both model runs.

### Accuracy

| Model            | Correct | Total | Accuracy |
|------------------|--------|-------|----------|
| Qwen3.5-9B       | 225    | 280   | 80.36% |
| Qwopus3.5-9B-v3  | 229    | 280   | **81.79%** |

**Result:**  
Qwopus3.5-9B-v3 leads by **+1.43 pp**

---

## Reasoning Efficiency

| Metric | Qwen3.5-9B | Qwopus3.5-9B-v3 |
|--------|------------|--------------|
| Avg think length | 7116 chars | **5313 chars** |
| Passes / 10k chars | 1.26 | **1.66** |
| Chars / correct pass | 7938 | **6032** |

### Reasoning Efficiency Improvements

- **−25.3%** shorter reasoning
- **+31.7%** higher efficiency
- **−24.0%** lower cost per correct answer

![Screenshot 2026-03-31 at 5.52.15 PM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/cLkR9ASLy08pK6SwN4ewm.png)



### Evaluation Summary
While the overall accuracy margin (+1.43 pp) is modest, Qwopus3.5-9B-v3 fundamentally shifts the **accuracy-cost paradigm**, achieving its victory while spending significantly less reasoning budget. With a 25.3% reduction in mean think length and 24.0% lower token cost per correct answer, this iteration is highly optimized for latency, token budget, and context pressure.

Furthermore, across the mixed domain profile, Qwopus3.5-9B-v3 uniquely offsets Qwen3.5-9B's slight edge in biology, CS, and math by excelling in physics, chemistry, and significantly lowering its unfinished-output rate. Its final rank benefits as much from raw correctness as from an improved ability to cleanly and reliably complete analytical boundaries.


## 🗺️ Training Pipeline Overview

```text
Base Model (Qwen3.5-9B)
 │
 ▼
Qwen3.5-9B fine-tuned with Unsloth
 │
 ▼
Supervised Fine-Tuning (SFT) + LoRA
(Response-Only Training masked on "<|im_start|>assistant\n<think>")
 │
 ▼
Qwopus3.5-9B-v3
```

### 🧠 Example of Learned Reasoning Scaffold

The model includes targeted optimizations addressing Qwen3.5's tendency toward excessive or repetitive reasoning on simple queries. By distilling the structured reasoning habits of top-tier models like Claude Opus, Qwopus3.5-9B-v3 adopts a highly organized, step-by-step cognitive layout.


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

## 🙏 Acknowledgements
Significant thanks to the [Unsloth AI](https://unsloth.ai/) team for making rapid fine-tuning of large LLM models accessible. Additionally, we acknowledge Qwen internally, and the open-source community developers producing exceptional distilled datasets.

This qwen3_5 model was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth) and Huggingface's TRL library.

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)



## 📖 Citation

If you use this model in your research or projects, please cite:

```bibtex
@misc{jackrong_qwen35_9b_v3
  title        = {Jackrong/Qwopus3.5-9B-v3},
  author       = {Jackrong},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/Jackrong/Qwopus3.5-9B-v3-GGUF}}
}
```




