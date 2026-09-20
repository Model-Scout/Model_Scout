---
library_name: transformers
base_model:
- Jackrong/Qwopus3.5-9B-v3.5
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
- mtp
- multi-token-prediction
- speculative-decoding
- qwen3_5
- reasoning
- chain-of-thought
- lora
- sft
- agent
- coder
- tool-use
- function-calling
license: apache-2.0
language:
- en
- zh
- ko
- ru
- ja
- es
pipeline_tag: image-text-to-text
datasets:
- Jackrong/Claude-opus-4.7-TraceInversion-5000x
- Jackrong/Claude-opus-4.6-TraceInversion-9000x
---

# <span style="color: #7FFF7F;">Qwopus3.5-9B-Coder-MTP GGUF Models</span>


## <span style="color: #7F7FFF;">Model Generation Details</span>

This model was generated using [llama.cpp](https://github.com/ggerganov/llama.cpp) at commit [`94a220cd6`](https://github.com/ggerganov/llama.cpp/commit/94a220cd6745e6e3f8de62870b66fd5b9bc92700).






---

<a href="https://readyforquantum.com/huggingface_gguf_selection_guide.html" style="color: #7FFF7F;">
  Click here to get info on choosing the right GGUF model format
</a>

---



<!--Begin Original Model Card-->

# 🌟 Qwopus3.5-9B-Coder-MTP (Multi-Token Prediction)

## 💡 Multi-Token Prediction (MTP) Architecture Overview

> [!NOTE]
> **What is MTP (Multi-Token Prediction)?**
> 
> **MTP** is a revolutionary technology in the field of Large Language Model (LLM) training and inference in recent years. Unlike traditional autoregressive models that predict only a single token at each step (Single-Token Prediction), **MTP models are designed during training to simultaneously predict multiple future tokens at each position**.
>
> This architecture brings two core dimensions of transformation:
> 1. **Deeper Representation and Planning**: It forces the model to perform global planning (Long-Horizon Planning) at the representation level for longer-term contexts. This enhances cognitive coherence in logic-intensive tasks such as complex coding and multi-step mathematical reasoning, while effectively mitigating the "reasoning bubbles" and repetition loops common in traditional autoregressive models.
> 2. **Extreme Inference Speedup (Speculative Decoding)**: During inference, the model is equipped with additional lightweight auxiliary prediction heads (Draft Heads, configured as `draft=2` in this model). While the backbone network generates the current token, the Draft Heads predict the subsequent 2 candidate tokens in parallel with negligible computational overhead, which are then verified by the main model in a single forward pass. Once verified, the model can output multiple tokens in a single inference step, yielding substantial throughput gains.

## 🚀 Performance Briefing: Base vs MTP (draft=2)

Based on actual testing across **Logic / Coding / DevOps / Math / Edge** (5 core domains, 30 complex evaluation questions), **Qwopus3.5-9B-Coder-MTP (draft=2)** demonstrates absolute advantages in both speed and correctness:

* **⚡ Speed Leap**: Overall throughput rate has jumped from **4.94 T/s** to **6.71 T/s** (**+35.8% throughput improvement**), saving **16.4 minutes** in total latency (overall time reduced by **25%**).
* **🎯 Accuracy & Robustness**: Overall accuracy improved from **80.0%** to **88.3%** (**+8.3pp**). The model achieved a perfect score in both **Coding (100% accuracy)** and **Math (100% accuracy)**, two high-difficulty task scenarios, completely eliminating the code truncations and repetitive behaviors observed in the Base model (independent of model type).
* **📊 Overall Efficiency Index**: After weighting correctness against inference time, the overall reasoning efficiency of the MTP model improved by **38.4%**.

> [!IMPORTANT]
> The evaluation configuration and benchmark framework follow the official Qwen series testing by the **Unsloth** team, whose research demonstrates that setting `draft=2` yields the optimal performance. For full details, see the official [Unsloth MTP Benchmarks](https://unsloth.ai/docs/models/qwen3.6#mtp-benchmarks).

---
#### Community-Reported Tool Calling Evaluation

> [!TIP]
> A community user independently evaluated Qwopus3.5-9B-coder on a tool-recall test with up to 31 available tools and an adversarial tool-selection phase containing semantic overlaps and decoy tools.

| Model | Phase 1: Tool Recall | Phase 2: Adversarial Tool Selection |
|---|---:|---:|
| Qwopus3.5-9B-coder | 100% | 27 / 28 (96%) |
| Claude Opus 4.6 | 100% | 27 / 28 (96%) |
| Qwen3.5-9B | 100% | 26 / 28 (93%) |

---
## ⚙️ Test Environment & Configuration

To guarantee the rigor, objectivity, and reproducibility of the evaluation, this benchmark was conducted under a unified hardware platform and sampling hyperparameters:

* **🖥️ Compute Platform**: **GB10 Dedicated Server Platform** (equipped with high-performance LLM compute acceleration chips, providing abundant parallel computing power).
* **⚙️ Concurrency Configuration**: **Concurrency = 5** was used to perform multi-threaded concurrent pressure and stability testing, accurately simulating real-world multi-user concurrent invocation scenarios.
* **🛠️ Script Version**: **Benchlocal Test Suite v1.3.0** inference evaluation script.
* **🧪 Sampling Hyperparameters**:
  * **Temperature**: `1.0` (recommended standard, balancing logical reasoning and creativity).
  * **Top-p**: `0.95` (retains high-probability candidates, filters tail noise, ensuring reasoning accuracy).

---

## 1. Token Volume and Speed Statistics

<table style="width: 100%; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; margin: 16px 0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03); border-radius: 8px; overflow: hidden; border: 1px solid rgba(2, 132, 199, 0.08);">
  <thead>
    <tr>
      <td colspan="9" style="padding: 6px 4px; font-weight: 600; color: #0284c7; border-bottom: 2px solid rgba(2, 132, 199, 0.2); background: rgba(2, 132, 199, 0.05); font-size: 11px;">Token & Speed Details per Question</td>
    </tr>
        <tr style="background: rgba(2, 132, 199, 0.02);">
      <th style="padding: 6px 4px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 11px; color: #475569; font-weight: 600; text-align: left; width: 9%;">Question</th>
      <th style="padding: 6px 4px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 11px; color: #475569; font-weight: 600; text-align: center; width: 10%;">Category</th>
      <th style="padding: 6px 4px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 11px; color: #475569; font-weight: 600; text-align: center; width: 10%;">Base T/s</th>
      <th style="padding: 6px 4px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 11px; color: #475569; font-weight: 600; text-align: center; width: 11%;">Base Time</th>
      <th style="padding: 6px 4px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 11px; color: #475569; font-weight: 600; text-align: center; width: 11%;">Base Tokens</th>
      <th style="padding: 6px 4px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 11px; color: #0284c7; font-weight: 600; text-align: center; width: 10%;">MTP T/s</th>
      <th style="padding: 6px 4px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 11px; color: #0284c7; font-weight: 600; text-align: center; width: 11%;">MTP Time</th>
      <th style="padding: 6px 4px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 11px; color: #0284c7; font-weight: 600; text-align: center; width: 11%;">MTP Tokens</th>
      <th style="padding: 6px 4px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 11px; color: #0284c7; font-weight: 600; text-align: center; width: 16%;">Speedup</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; font-weight: 500; text-align: left;">Q1</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">Logic</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">4.20</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">86.80</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">365</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">6.10</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">86.45</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">527</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">1.00x</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; font-weight: 500; text-align: left;">Q2</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">Logic</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">4.40</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">178.70</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">786</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">5.80</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">130.80</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">759</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">1.37x</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; font-weight: 500; text-align: left;">Q3</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">Logic</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">4.30</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">172.66</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">743</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">6.80</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">90.24</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">614</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">1.91x</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; font-weight: 500; text-align: left;">Q4</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">Logic</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">4.20</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">153.05</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">643</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">7.90</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">67.85</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">536</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">2.25x</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; font-weight: 500; text-align: left;">Q5</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">Logic</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">4.20</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">172.33</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">724</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">6.70</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">40.88</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">274</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">4.22x</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; font-weight: 500; text-align: left;">Q6</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">Coding</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">4.40</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">240.96</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">1060</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">6.70</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">160.32</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">1074</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">1.50x</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; font-weight: 500; text-align: left;">Q7</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">Coding</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">4.30</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">244.07</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">1050</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">6.20</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">173.26</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">1074</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">1.41x</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; font-weight: 500; text-align: left;">Q8</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">Coding</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">4.30</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">245.05</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">1054</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">6.80</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">158.92</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">1081</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">1.54x</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; font-weight: 500; text-align: left;">Q9</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">Coding</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">4.30</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">245.46</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">1055</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">6.60</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">162.95</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">1075</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">1.51x</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; font-weight: 500; text-align: left;">Q10</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">Coding</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">4.40</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">241.59</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">1063</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">6.20</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">173.44</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">1075</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">1.39x</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; font-weight: 500; text-align: left;">Q11</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">Coding</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">4.20</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">249.55</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">1048</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">6.90</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">156.09</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">1077</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">1.60x</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; font-weight: 500; text-align: left;">Q12</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">Coding</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">4.20</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">211.45</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">888</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">6.50</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">155.98</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">1014</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">1.36x</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; font-weight: 500; text-align: left;">Q13</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">Coding</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">4.30</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">248.09</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">1067</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">6.50</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">164.91</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">1072</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">1.50x</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; font-weight: 500; text-align: left;">Q14</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">Coding</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">4.10</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">156.12</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">640</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">6.30</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">119.72</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">754</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">1.30x</td>
    </tr>
    <tr>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; font-weight: 500; text-align: left;">Q15</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">Coding</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">4.30</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">144.47</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #334155; text-align: center;">621</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">6.40</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">165.97</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">1062</td>
      <td style="padding: 6px 4px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 11px; color: #0284c7; font-weight: bold; text-align: center;">0.87x</td>
    </tr>
  </tbody>
</table>

<table style="width: 100%; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; margin: 16px 0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03); border-radius: 8px; overflow: hidden; border: 1px solid rgba(2, 132, 199, 0.08);">
  <thead>
    <tr>
      <td colspan="5" style="padding: 10px 16px; font-weight: 600; color: #0284c7; border-bottom: 2px solid rgba(2, 132, 199, 0.2); background: rgba(2, 132, 199, 0.05); font-size: 15px;">Logic Category (Q1-Q5) Answer Verification</td>
    </tr>
    <tr style="background: rgba(2, 132, 199, 0.02);">
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: left; width: 12%;">Question ID</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: left; width: 38%;">Question Summary</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: left; width: 30%;">Correct Answer</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: center; width: 10%;">Base</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #0284c7; font-weight: 600; text-align: center; width: 10%;">MTP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q1</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">17 sheep except 9 died, how many left</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">9 sheep</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q2</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">30 dollar hotel riddle, where is the 1 dollar</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">No loss, accounting error</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q3</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Sequence: 2, 6, 12, 20, 30, ?</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">42 (n * (n + 1))</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q4</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Bat + ball = $1.10, bat is $1 more expensive than ball</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">$0.05</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q5</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Multiply by 3, add 6, divide by 3, subtract original number</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Always 2</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
    </tr>
  </tbody>
</table>

> [!TIP]
> **Logic**: **Base 5/5 = 100%** | **MTP 5/5 = 100%**

<table style="width: 100%; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; margin: 16px 0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03); border-radius: 8px; overflow: hidden; border: 1px solid rgba(2, 132, 199, 0.08);">
  <thead>
    <tr>
      <td colspan="5" style="padding: 10px 16px; font-weight: 600; color: #0284c7; border-bottom: 2px solid rgba(2, 132, 199, 0.2); background: rgba(2, 132, 199, 0.05); font-size: 15px;">Coding Category (Q6-Q15) Answer Verification</td>
    </tr>
    <tr style="background: rgba(2, 132, 199, 0.02);">
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: left; width: 12%;">Question ID</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: left; width: 38%;">Question Summary</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: center; width: 10%;">Base</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #0284c7; font-weight: 600; text-align: center; width: 10%;">MTP</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: left; width: 30%;">Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q6</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Python Fibonacci generator</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #d97706; font-weight: bold; text-align: center;">PARTIAL</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Base Repetition=True, code truncation has logical issues</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q7</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Python thread-safe singleton</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #d97706; font-weight: bold; text-align: center;">PARTIAL</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Base Repetition=True, incomplete implementation</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q8</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Sort CSV by second column in descending order</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #d97706; font-weight: bold; text-align: center;">PARTIAL</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Base code truncated</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q9</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Python HTTP Server</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Both fully implemented</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q10</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Python execution time decorator</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Both fully implemented</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q11</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">C++ Binary Search Tree</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Both fully implemented</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q12</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Bash backup script (with date)</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Both fully implemented</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q13</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Python topological sort</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Both fully implemented</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q14</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Node.js Dockerfile</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Both fully implemented</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q15</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">SQL second highest salary</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Both implemented correctly</td>
    </tr>
  </tbody>
</table>

> [!TIP]
> **Coding**: Base 7/10 = 70% | **MTP 10/10 = 100%**

<table style="width: 100%; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; margin: 16px 0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03); border-radius: 8px; overflow: hidden; border: 1px solid rgba(2, 132, 199, 0.08);">
  <thead>
    <tr>
      <td colspan="5" style="padding: 10px 16px; font-weight: 600; color: #0284c7; border-bottom: 2px solid rgba(2, 132, 199, 0.2); background: rgba(2, 132, 199, 0.05); font-size: 15px;">DevOps Category (Q16-Q20) Answer Verification</td>
    </tr>
        <tr style="background: rgba(2, 132, 199, 0.02);">
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: left; width: 12%;">Question ID</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: left; width: 38%;">Question Summary</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: center; width: 10%;">Base</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #0284c7; font-weight: 600; text-align: center; width: 10%;">MTP</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: left; width: 30%;">Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q16</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Nginx reverse proxy & load balancer</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #d97706; font-weight: bold; text-align: center;">PARTIAL</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #d97706; font-weight: bold; text-align: center;">PARTIAL</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Both have correct config framework but Response was truncated</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q17</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Hard Link vs Soft Link</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #d97706; font-weight: bold; text-align: center;">PARTIAL</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Base Repetition=True, has repetitive lines; MTP complete</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q18</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">crontab every Tuesday at 3:15 AM</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Both correct: 15 3 * * 2 script.sh</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q19</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">SSH server security configuration</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #d97706; font-weight: bold; text-align: center;">PARTIAL</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #d97706; font-weight: bold; text-align: center;">PARTIAL</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Both contents were truncated</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q20</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">systemd service restart on failure</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Both explained correctly</td>
    </tr>
  </tbody>
</table>

> [!TIP]
> **DevOps**: Base 2.5/5 = 50% | **MTP 3.5/5 = 70%**

<table style="width: 100%; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; margin: 16px 0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03); border-radius: 8px; overflow: hidden; border: 1px solid rgba(2, 132, 199, 0.08);">
  <thead>
    <tr>
      <td colspan="5" style="padding: 10px 16px; font-weight: 600; color: #0284c7; border-bottom: 2px solid rgba(2, 132, 199, 0.2); background: rgba(2, 132, 199, 0.05); font-size: 15px;">Math Category (Q21-Q25) Answer Verification</td>
    </tr>
        <tr style="background: rgba(2, 132, 199, 0.02);">
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: left; width: 12%;">Question ID</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: left; width: 38%;">Question Summary</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: left; width: 25%;">Correct Answer</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: center; width: 12%;">Base</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #0284c7; font-weight: 600; text-align: center; width: 13%;">MTP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q21</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Find derivative of f(x) = x^3 * ln(x)</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">x^2 * (3ln(x) + 1)</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q22</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">System of equations: 2x+y=5, x-y=1</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">x = 2, y = 1</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q23</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Probability of rolling a sum of 7 with two dice</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">1/6 = 16.67%</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q24</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Integral of e^(2x)</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">(1/2)e^(2x)+C</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q25</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Prove sum of first n odd numbers is n^2</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Induction / Arithmetic progression</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #d97706; font-weight: bold; text-align: center;">PARTIAL</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
    </tr>
  </tbody>
</table>

> [!TIP]
> **Math**: Base 4.5/5 = 90% | **MTP 5/5 = 100%**

<table style="width: 100%; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; margin: 16px 0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03); border-radius: 8px; overflow: hidden; border: 1px solid rgba(2, 132, 199, 0.08);">
  <thead>
    <tr>
      <td colspan="5" style="padding: 10px 16px; font-weight: 600; color: #0284c7; border-bottom: 2px solid rgba(2, 132, 199, 0.2); background: rgba(2, 132, 199, 0.05); font-size: 15px;">Edge Category (Q26-Q30) Answer Verification</td>
    </tr>
        <tr style="background: rgba(2, 132, 199, 0.02);">
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: left; width: 12%;">Question ID</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: left; width: 38%;">Question Summary</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: center; width: 10%;">Base</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #0284c7; font-weight: 600; text-align: center; width: 10%;">MTP</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: left; width: 30%;">Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q26</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Output 'Apple' 5 times</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Both correctly outputted 5 lines</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q27</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Output a phrase 3 times</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Both correct</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q28</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Explain infinity (with forbidden words constraint)</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #d97706; font-weight: bold; text-align: center;">PARTIAL</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">MTP Repetition=True, Response truncated</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q29</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Generate 5-level nested JSON</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #d97706; font-weight: bold; text-align: center;">PARTIAL</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">MTP last item incomplete, Base generated 6 levels</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Q30</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">30 'A's reply with 'B B B'</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #059669; font-weight: bold; text-align: center;">PASS</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: left;">Both correct</td>
    </tr>
  </tbody>
</table>

> [!TIP]
> **Edge**: **Base 5/5 = 100%** | MTP 3/5 = 60%

---

<table style="width: 100%; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; margin: 16px 0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03); border-radius: 8px; overflow: hidden; border: 1px solid rgba(2, 132, 199, 0.08);">
  <thead>
    <tr>
      <td colspan="6" style="padding: 10px 16px; font-weight: 600; color: #0284c7; border-bottom: 2px solid rgba(2, 132, 199, 0.2); background: rgba(2, 132, 199, 0.05); font-size: 15px;">Overall Accuracy Summary</td>
    </tr>
        <tr style="background: rgba(2, 132, 199, 0.02);">
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: left; width: 20%;">Category</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: center; width: 12%;">Questions</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: center; width: 17%;">Base Correct</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: center; width: 17%;">Base Accuracy</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #0284c7; font-weight: 600; text-align: center; width: 17%;">MTP Correct</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #0284c7; font-weight: 600; text-align: center; width: 17%;">MTP Accuracy</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Logic</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: center;">5</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #475569; background: rgba(71, 85, 105, 0.06); font-weight: bold; text-align: center;">5</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #475569; background: rgba(71, 85, 105, 0.06); font-weight: bold; text-align: center;">100%</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #0284c7; background: rgba(2, 132, 199, 0.06); font-weight: bold; text-align: center;">5</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #0284c7; background: rgba(2, 132, 199, 0.06); font-weight: bold; text-align: center;">100%</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Coding</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: center;">10</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: center;">7</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: center;">70%</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #0284c7; background: rgba(2, 132, 199, 0.06); font-weight: bold; text-align: center;">10</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #0284c7; background: rgba(2, 132, 199, 0.06); font-weight: bold; text-align: center;">100%</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">DevOps</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: center;">5</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: center;">2.5</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: center;">50%</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #0284c7; background: rgba(2, 132, 199, 0.06); font-weight: bold; text-align: center;">3.5</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #0284c7; background: rgba(2, 132, 199, 0.06); font-weight: bold; text-align: center;">70%</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Math</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: center;">5</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: center;">4.5</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: center;">90%</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #0284c7; background: rgba(2, 132, 199, 0.06); font-weight: bold; text-align: center;">5</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #0284c7; background: rgba(2, 132, 199, 0.06); font-weight: bold; text-align: center;">100%</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Edge</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: center;">5</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #475569; background: rgba(71, 85, 105, 0.06); font-weight: bold; text-align: center;">5</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #475569; background: rgba(71, 85, 105, 0.06); font-weight: bold; text-align: center;">100%</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: center;">3</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: center;">60%</td>
    </tr>
    <tr style="background: rgba(2, 132, 199, 0.04); font-weight: bold;">
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #0284c7; text-align: left;">Total</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: center;">30</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: center;">24</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: center;">80.0%</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #0284c7; background: rgba(2, 132, 199, 0.12); font-size: 14px; text-align: center;">26.5</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #0284c7; background: rgba(2, 132, 199, 0.12); font-size: 14px; text-align: center;">88.3%</td>
    </tr>
  </tbody>
</table>

---

<table style="width: 100%; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; margin: 16px 0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03); border-radius: 8px; overflow: hidden; border: 1px solid rgba(2, 132, 199, 0.08);">
  <thead>
    <tr>
      <td colspan="4" style="padding: 10px 16px; font-weight: 600; color: #0284c7; border-bottom: 2px solid rgba(2, 132, 199, 0.2); background: rgba(2, 132, 199, 0.05); font-size: 15px;">Reasoning Efficiency Comparison</td>
    </tr>
        <tr style="background: rgba(2, 132, 199, 0.02);">
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: left; width: 40%;">Efficiency Metric</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: center; width: 20%;">Base Model</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #0284c7; font-weight: 600; text-align: center; width: 20%;">MTP Model</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #0284c7; font-weight: 600; text-align: center; width: 20%;">MTP Advantage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Overall Throughput (T/s)</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: center;">4.94</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #0284c7; font-weight: bold; text-align: center;">6.71</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #0284c7; font-weight: bold; text-align: center;">+35.8%</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Overall Accuracy</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: center;">80.0%</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #0284c7; font-weight: bold; text-align: center;">88.3%</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #0284c7; font-weight: bold; text-align: center;">+8.3pp</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Total Latency</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: center;">81.3 min</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #0284c7; font-weight: bold; text-align: center;">64.9 min</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #0284c7; font-weight: bold; text-align: center;">Saved 16.4min</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Reasoning Efficiency Index (Accuracy / Latency)</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: center;">1.64e-4</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #0284c7; font-weight: bold; text-align: center;">2.27e-4</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #0284c7; font-weight: bold; text-align: center;">+38.4%</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Correct Answers per 1k Tokens</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: center;">0.995 Q/kT</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #0284c7; font-weight: bold; text-align: center;">1.014 Q/kT</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #0284c7; font-weight: bold; text-align: center;">+1.9%</td>
    </tr>
  </tbody>
</table>

---

<table style="width: 100%; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; margin: 16px 0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03); border-radius: 8px; overflow: hidden; border: 1px solid rgba(2, 132, 199, 0.08);">
  <thead>
    <tr>
      <td colspan="3" style="padding: 10px 16px; font-weight: 600; color: #0284c7; border-bottom: 2px solid rgba(2, 132, 199, 0.2); background: rgba(2, 132, 199, 0.05); font-size: 15px;">Quality Issues Statistics</td>
    </tr>
        <tr style="background: rgba(2, 132, 199, 0.02);">
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: left; width: 40%;">Quality Issue</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: center; width: 30%;">Base Counts</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(2, 132, 199, 0.12); font-size: 13px; color: #0284c7; font-weight: 600; text-align: center; width: 30%;">MTP Counts</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Repetition (Repetitive output flags)</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: center;">2 times (Q6, Q17)</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #0284c7; font-weight: bold; text-align: center;">2 times (Q6, Q28)</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Timeout</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: center;">0 times</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #0284c7; font-weight: bold; text-align: center;">0 times</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Incomplete responses / Truncations</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: center;">~8 occurrences</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #0284c7; font-weight: bold; text-align: center;">~4 occurrences</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Excessively long reasoning chain</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; text-align: center;">Less</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #0284c7; font-weight: bold; text-align: center;">More</td>
    </tr>
  </tbody>
</table>


---

## 8. Final Conclusion

### Areas where MTP Model Excels
- **Speed**: 35.8% faster overall, particularly outstanding in Math and Edge tasks.
- **Coding**: 100% complete code outputs, whereas Base suffered 3 truncations due to repetition.
- **Math**: 100% accuracy with more systematic reasoning chains.
- **Efficiency**: Overall reasoning efficiency index is 38.4% higher.

### Areas for MTP Model Improvement
- **Edge Task Stability**: Truncations occurred in Q28/Q29 as excessively long reasoning chains hit token limits.
- **DevOps Long Texts**: For long explanatory responses, draft matching rates are low, leading to limited speedups.

<table style="width: 100%; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; margin: 16px 0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03); border-radius: 8px; overflow: hidden; border: 1px solid rgba(124, 58, 237, 0.08);">
  <thead>
    <tr>
      <td colspan="2" style="padding: 10px 16px; font-weight: 600; color: #7c3aed; border-bottom: 2px solid rgba(124, 58, 237, 0.2); background: rgba(124, 58, 237, 0.05); font-size: 15px;">Recommended Scenarios</td>
    </tr>
    <tr style="background: rgba(124, 58, 237, 0.02);">
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(124, 58, 237, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: left; width: 65%;">Scenario</th>
      <th style="padding: 8px 12px; border-bottom: 1px solid rgba(124, 58, 237, 0.12); font-size: 13px; color: #475569; font-weight: 600; text-align: left; width: 35%;">Recommended Model</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Code Generation</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #7c3aed; font-weight: bold; text-align: left;">MTP</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Mathematical Reasoning</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #7c3aed; font-weight: bold; text-align: left;">MTP</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Logical Reasoning</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #7c3aed; font-weight: bold; text-align: left;">Both acceptable</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">Short-text instructions (Edge)</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: bold; text-align: left;">Base is more stable</td>
    </tr>
    <tr>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #334155; font-weight: 500; text-align: left;">DevOps long documents</td>
      <td style="padding: 8px 12px; border-bottom: 1px solid rgba(0, 0, 0, 0.05); font-size: 13px; color: #7c3aed; font-weight: bold; text-align: left;">Both require larger max_tokens</td>
    </tr>
  </tbody>
</table>

---


# 🌟 Qwopus3.5-9B-coder

## 🚀 Model Fine-Tuning and Logical Alignment (Qwopus3.5-9B-coder)

As the base model of this model, **Qwopus3.5-9B-v3.5** is already a model with powerful capabilities. On this foundation, **Qwopus3.5-9B-coder** is specially optimized and fine-tuned for high-performance **🤖 Agentic Coding, complex Tool Calling, and logical reasoning.**

> 💡 **Why the 9B Dense Model?**
> We believe that the 9B dense architecture represents the perfect **"sweet spot"** for large language models. It runs seamlessly at 8-bit precision on entry-level 16GB RAM devices—such as standard laptops and the Mac mini—making it exceptionally lightweight yet highly versatile. Without requiring expensive hardware, it allows you to achieve excellent performance paired with impressive inference speeds. Simply put, **Qwen3.5-9B is currently the best open-source model in its class.**


![image](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/8qFQVuCxbgkWqKa2B_Vph.jpeg)

> [!TIP]
>**Vision & Tool Calling Support**: This model supports visual capabilities and tool calling. To enable vision, please place the `mmproj.gguf` file from the [GGUF repository](https://huggingface.co/Jackrong/Qwopus3.5-9B-coder-GGUF) into the same directory as the main `.gguf` file.

---

### 🛠 Training Strategy

The fine-tuning process of this model deeply integrates **Trace Inversion** data augmentation technology with high-quality **Agent Traces**. This systematic approach not only strengthens the model's ability to solve complex programming tasks, but also greatly improves its logical coherence and accuracy when using various tools.

This model is designed specifically for the following goals:

- 🧩 More structured and stronger logical reasoning capabilities, reducing repetitive thinking
- 💻 More powerful capabilities in code writing, debugging, and repository-level task processing
- 🛠 More stable and accurate Tool Calling capabilities for terminal commands, file operations, and browsers
- 🔁 Better cross-data source distillation alignment


> [!WARNING]
> - **Community Release Notice**: Qwopus3.5-9B-coder is released purely as an experimental community version, aiming to explore the combination of Agent capabilities and deep reasoning, and is only for research and exploration use.
> - **Warning**: Because this model is vertically fine-tuned for programming agents and deep reasoning, and has not undergone comprehensive general performance evaluation, its capabilities in general domains or specific non-programming tasks may suffer from Capability Decay. Users are advised to be aware of its limitations in other scenarios while exploring its core capabilities.

---


## 📊 Baseline Performance Comparison

To verify the execution efficiency and logical robustness of **Qwopus3.5-9B-coder** in actual agent scenarios, we adopted the open-source testing framework [benchlocal](https://github.com/stevibe/benchlocal).

### Test Configuration
- **Hardware Environment**: Apple Silicon (Mac)
- **Inference Backend**: LM Studio / MLX / GGUF
- **Testing Platform**: [benchlocal](https://github.com/stevibe/benchlocal) - An evaluation suite focusing on local model agent capabilities.
- 🍎 You can see the actual inference speeds of different model formats on the same device.

### 🧪 Benchmark Results 

<div style="display: inline-block; padding: 6px 16px; background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; border-radius: 8px; font-weight: 700; font-size: 16px; margin-bottom: 12px;">1. Complex Agent Performance - HermesAgent-20</div>
The following is the comparative performance under the HermesAgent-20 task set:

<table style="width: 100%; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <thead>
    <tr>
      <td colspan="4" style="padding: 8px 12px; font-weight: 600; color: #7c3aed; border-bottom: 1px solid rgba(124, 58, 237, 0.2); background: rgba(124, 58, 237, 0.05);">HermesAgent-20 Performance Metrics</td>
    </tr>
    <tr style="background: rgba(128, 128, 128, 0.02);">
      <th style="padding: 7px 7px; padding-left: 20px; text-align: left; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Model</th>
      <th style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Test Set</th>
      <th style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Comprehensive Score</th>
      <th style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Core Dimensions (M/O/S/S/B)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><b><a href="https://huggingface.co/Jackrong/Qwopus3.5-9B-coder-GGUF" style="color: #7c3aed; text-decoration: none;">Qwopus3.5-9B-coder</a></b></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">HermesAgent-20</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); color: #7c3aed; font-weight: bold;">85</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">84 / 93 / 88 / 75 / 84</td>
    </tr>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><a href="https://huggingface.co/Qwen/Qwen3.5-9B" style="color: #666; text-decoration: none;">Qwen/Qwen3.5-9B</a></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">HermesAgent-20</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">71</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">75 / 58 / 100 / 53 / 69</td>
    </tr>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><a href="https://huggingface.co/armand0e/Qwen3.5-9B-Agent" style="color: #666; text-decoration: none;">armand0e/Qwen3.5-9B-Agent</a></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">HermesAgent-20</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">68</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">71 / 83 / 43 / 61 / 80</td>
    </tr>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><a href="https://huggingface.co/DJLougen/Harmonic-Hermes-9B" style="color: #666; text-decoration: none;">DJLougen/Harmonic-Hermes-9B</a></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">HermesAgent-20</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">47</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">60 / 45 / 23 / 69 / 38</td>
    </tr>
  </tbody>
</table>

<div style="display: inline-block; padding: 6px 16px; background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; border-radius: 8px; font-weight: 700; font-size: 16px; margin-bottom: 12px;">2. Tool Call Stability - ToolCall-15</div>
This is a ToolCall-15 test set targeting the stability of tool calls, aiming to test the stability of the model in tool calling:

<table style="width: 100%; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <thead>
    <tr>
      <td colspan="4" style="padding: 8px 12px; font-weight: 600; color: #7c3aed; border-bottom: 1px solid rgba(124, 58, 237, 0.2); background: rgba(124, 58, 237, 0.05);">ToolCall-15 Stability Metrics</td>
    </tr>
    <tr style="background: rgba(128, 128, 128, 0.02);">
      <th style="padding: 7px 7px; padding-left: 20px; text-align: left; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Model</th>
      <th style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Test Set</th>
      <th style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Comprehensive Score</th>
      <th style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Dimension Scores (A/B/C/D/E)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><b><a href="https://huggingface.co/Jackrong/Qwopus3.5-9B-coder-GGUF" style="color: #7c3aed; text-decoration: none;">Qwopus3.5-9B-coder</a></b></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">ToolCall-15</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); color: #7c3aed; font-weight: bold;">100</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">100 / 100 / 100 / 100 / 100</td>
    </tr>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><a href="https://huggingface.co/Qwen/Qwen3.5-9B" style="color: #666; text-decoration: none;">Qwen/Qwen3.5-9B</a></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">ToolCall-15</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); color: #7c3aed; font-weight: bold;">100</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">100 / 100 / 100 / 100 / 100</td>
    </tr>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><a href="https://huggingface.co/armand0e/Qwen3.5-9B-Agent" style="color: #666; text-decoration: none;">armand0e/Qwen3.5-9B-Agent</a></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">ToolCall-15</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">93</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">100 / 100 / 100 / 67 / 100</td>
    </tr>
  </tbody>
</table>

<div style="display: inline-block; padding: 6px 16px; background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; border-radius: 8px; font-weight: 700; font-size: 16px; margin-bottom: 12px;">3. Code Debugging & Bug Fixing - BugFind-15</div>
BugFind-15 is a test set containing 15 scenarios from shallow to deep, aiming to evaluate the real debugging capabilities of the model in discovering and fixing syntax, logical errors, and "trap" code in multiple programming languages through deterministic environment runtime verification.

<table style="width: 100%; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <thead>
    <tr>
      <td colspan="4" style="padding: 8px 12px; font-weight: 600; color: #7c3aed; border-bottom: 1px solid rgba(124, 58, 237, 0.2); background: rgba(124, 58, 237, 0.05);">BugFind-15 Performance Metrics</td>
    </tr>
    <tr style="background: rgba(128, 128, 128, 0.02);">
      <th style="padding: 7px 7px; padding-left: 20px; text-align: left; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Model</th>
      <th style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Test Set</th>
      <th style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Comprehensive Score</th>
      <th style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Dimension Scores (A/B/C/D/E)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><b><a href="https://huggingface.co/Jackrong/Qwopus3.5-9B-coder-GGUF" style="color: #7c3aed; text-decoration: none;">Qwopus3.5-9B-coder</a></b></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">BugFind-15</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); color: #7c3aed; font-weight: bold;">79</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">67 / 87 / 100 / 77 / 43</td>
    </tr>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><a href="https://huggingface.co/Jackrong/MLX-Qwen3.5-9B-DeepSeek-V4-Flash-8bit" style="color: #666; text-decoration: none;">Jackrong/MLX-Qwen3.5-9B-DeepSeek-V4-Flash</a></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">BugFind-15</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">75</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">67 / 100 / 67 / 57 / 80</td>
    </tr>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><a href="https://huggingface.co/armand0e/Qwen3.5-9B-Agent" style="color: #666; text-decoration: none;">armand0e/Qwen3.5-9B-Agent</a></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">BugFind-15</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">58</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">29 / 87 / 73 / 20 / 67</td>
    </tr>
  </tbody>
</table>

### 🪐 SWE-bench Verified Performance (Repository-level Coding Capability)
The following shows the comparative performance on **SWE-bench Verified**, which evaluates language models on resolving software engineering issues in real-world open-source repositories:

<table style="width: 100%; border-collapse: collapse; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <thead>
    <tr>
      <td colspan="3" style="padding: 8px 12px; font-weight: 600; color: #7c3aed; border-bottom: 1px solid rgba(124, 58, 237, 0.2); background: rgba(124, 58, 237, 0.05);">SWE-bench Verified Performance Metrics</td>
    </tr>
    <tr style="background: rgba(128, 128, 128, 0.02);">
      <th style="padding: 7px 7px; padding-left: 20px; text-align: left; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Model</th>
      <th style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Test Set</th>
      <th style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); font-size: 13px; color: #666;">Comprehensive Score (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><span style="color: #666;">Claude 4.5 Opus</span></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">SWE-bench Verified</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">80.9</td>
    </tr>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><a href="https://huggingface.co/Qwen/Qwen3.5-27B" style="color: #666; text-decoration: none;">Qwen/Qwen3.5-27B</a></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">SWE-bench Verified</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">75.0</td>
    </tr>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><a href="https://huggingface.co/Qwen/Qwen3.6-35B-A3B" style="color: #666; text-decoration: none;">Qwen/Qwen3.6-35B-A3B</a></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">SWE-bench Verified</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">73.4</td>
    </tr>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><b><a href="https://huggingface.co/Jackrong/Qwopus3.5-9B-coder-GGUF" style="color: #7c3aed; text-decoration: none;">Qwopus3.5-9B-coder</a></b></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">SWE-bench Verified</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15); color: #7c3aed; font-weight: bold;">53.89</td>
    </tr>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><a href="https://huggingface.co/google/gemma-4-31B-it" style="color: #666; text-decoration: none;">google/gemma-4-31B-it</a></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">SWE-bench Verified</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">52.0</td>
    </tr>
    <tr>
      <td style="padding: 7px 7px; padding-left: 20px; border-bottom: 1px solid rgba(128, 128, 128, 0.15);"><span style="color: #666;">google/gemma-4-26B-A4B</span></td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">SWE-bench Verified</td>
      <td style="padding: 7px 7px; text-align: center; border-bottom: 1px solid rgba(128, 128, 128, 0.15);">45.0 - 48.0</td>
    </tr>
  </tbody>
</table>


> [!IMPORTANT]
> - ⚙️ All tests were conducted with a temperature of 1 as officially recommended by qwen3.5. All errors and model issues were attempted to be regenerated twice after a test failure. If both attempts fail, it is considered a failure.
> - 🍎 All screenshots of the test interfaces have been uploaded to the image folder in the repository. Click the link below to view and verify:  
> - 🔗 [View Test Screenshots](https://huggingface.co/Jackrong/Qwopus3.5-9B-coder/tree/main/test_images)
> - ❤️ **Kyle Hessling** for his generous hardware and equipment support. You can follow him for more updates on X / Twitter: [@KyleHessling1](https://x.com/KyleHessling1).


---

### 🧪 Core Dataset Usage: Trace Inversion and High-Quality Agent Traces

In order to break through the "reasoning bubble" limitation of the model in actual programming and tool usage, and to endow it with real Agent behavioral capabilities, this model introduced core augmented datasets during training:

#### 1. Reasoning Synthetic Data Combining Trace Inversion
**Currently, based on public information, commercial models such as OpenAI's GPT series and Anthropic's Claude series have very clearly hidden the true internal reasoning chains of their models. For these models, what we can ultimately see in the API or front-end interface can often only be considered a highly compressed "Reasoning Bubble".** 

To break through this limitation, we adopted the **Trace Inversion** technology. This technology utilizes an external "surrogate model" to reconstruct a complete and logically coherent deep reasoning chain based on the "question + final answer + compressed reasoning summary" published by commercial models. The "reasoning bubble", which originally consisted of only a few sentences and logical leaps, is expanded into a high-quality deep learning trace with complete derivation, calculation, and logical verification, providing step-by-step logical learning signals for the model.


![a_high_resolution_infographic_slide_style_figure](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/Jo2bm_rUJQmfK3Na4Uja2.png)




#### 2. GLM-5.1 Agent Real Trace Data: lambda/hermes-agent-reasoning-traces
To significantly enhance the model's execution and coding capabilities in real environments, this model additionally introduced the **`lambda/hermes-agent-reasoning-traces`** dataset.

![Screenshot 2026-05-16 at 5.34.59 PM](https://cdn-uploads.huggingface.co/production/uploads/66309bd090589b7c65950665/BTusWFqYaOS5GmRYvBuPq.png)


- **Data Source and Scale**: This data subset contains approximately 10,000 high-quality multi-turn Tool Calling Trajectories generated based on the ZhipuAI GLM-5.1 and kimi-4.6 models.
- **Real Agent Behavior**: Unlike traditional synthetic data, these samples represent real Agent conversations. Each sample not only contains the step-by-step reasoning process in the `<think>` tags, but also includes actual tool execution results (rather than fabricated outputs out of thin air).
- **Extensive Domain Coverage**:
  - **Terminal & Coding**: Script writing, code debugging, environment configuration, and data processing.
  - **Repository Tasks**: Involving real code repository work, such as bug fixes, refactoring, and code review.
  - **Browser Automation**: Web navigation, scraping, and form filling.
  - **Agent Tools**: Memory persistence, task delegation, skill management, etc.

By learning these Agent trajectories that contain real feedback and thoughtful processes, Qwopus3.5-9B-coder can exhibit thinking and operational modes closer to human experts when facing complex programming and system operations tasks.

---

## 🗺️ Training Pipeline Overview

The training of this model integrates a phased learning pipeline of **Trace Inversion** data augmentation technology and **high-quality Agent Trajectories data**. Its core logic lies in restoring the highly compressed "reasoning bubble" of commercial models into a deep path for learning, and combining it with real agent operational traces to comprehensively improve the model's logical reasoning and code execution capabilities.

```text
       [ 🗺️ Trace Inversion: Full Process of Data Inversion and "Attack" Distillation ]

  A. Surrogate Model Training
     Open Source Model (GLM-5.1 / DS-V4) ──► Complete Reasoning Chain ──► [ Qwen3-235B Compression ] ──► Reasoning Bubbles
                                       │                                   │
                                       └──────────► [ Training ] ◄─────────┘
                                            (Base: Qwen3-4B-Instruct)
                                            (Result: Trace-Inverter-4B)

  B. Inversion Phase: "Attacking" Claude-4.7-Max
     _______________________________________________________
    |                                                       |
    |  Claude-4.7-Max API ──► Compressed Bubbles + Final Answer |
    |_______________________________________________________|
                      │
                      ▼
    [ 🧠 Trace-Inverter-4B (Logical Reconstructor) ] ────► Synthetic CoT
                      │
                      ▼
    [ 🧩 Data Splicing ] ◄────────── (Original Prompt + Response)
    (Embed the inverted chain of thought into <think> tags, and splice with the original Q&A pair for restoration)
                      │
                      ▼
            (Result: claude-opus-4.6/4.7 Inversion Set)

  C. Final SFT Pipeline
     ___________________________________________
    |                                           |
    |      Base Model (Qwopus3.5-9B-v3.5)       |
    |___________________________________________|
                      │
                      ▼
    [ 📦 Stage 1: Format Establishment and Logic Injection ] ───────► [ 🛠️ Stage 2: Agent Trajectories and Programming Reinforcement ]
     (Integrate inverted reasoning data, stabilize thinking format)        (Introduce GLM-5.1 Agent Trajectories, reinforce interaction and execution)
                      │                                 │
                      │                                 ▼
                      │           __________________________________________________
                      │          |  🔍 Hermes Agent Trace Sample Structure Breakdown (GLM-5.1) |
                      │          |  1. [🛠️ System] -> JSON Tool Definition          |
                      │          |  2. [👤 Human]  -> Initial Task Instruction        |
                      │          |  ┌──────────────────────────────────────────────┐ |
                      │          |  │ 🔁 Multi-turn Loop:                           │ |
                      │          |  │ 3. [🧠 GPT]  -> <think> Logical Reasoning/Reflection │ |
                      │          |  │ 4. [🤖 GPT]  -> Tool Call Execution Action    │ |
                      │          |  │ 5. [⚙️ Tool] -> Real Feedback                 │ |
                      │          |  └──────────────────────────────────────────────┘ |
                      │          |__________________________________________________|
                      │                                 │
                      └────────────────┬────────────────┘
                                       ▼
                      ___________________________________
                     |                                   |
                     |   🌟 Final Model: Qwopus3.5-9B-coder  |
                     |___________________________________|
```


> [!NOTE]
> Because agent trajectory datasets are complex and diverse. The datasets have undergone rigorous cleaning and formatting.

## 🎯 Three-Stage Curriculum Learning

**Qwopus3.5-9B-coder** adopts a phased reasoning data mixture strategy similar to Curriculum Learning, gradually increasing the difficulty and complexity of training signals:

1. **Early Stage (Format Establishment):** Focuses on short-to-medium length reasoning samples with stable formats. The primary goal of this stage is to establish a reliable, structured new reasoning format while avoiding overwhelming the model with extreme complexity.

2. **Middle Stage (Complexity Scaling & Multi-Teacher Distillation):** Gradually increases the proportion of complex reasoning samples from multiple teacher models.
   - The distillation data is sourced from more powerful models whose style distribution closely matches the base model, ensuring that the capability gap is not too wide, thereby achieving efficient learning.

3. **Late Stage (Long-Context Reinforcement & Drift Prevention):** Reinforces reasoning capabilities in long contexts. Crucially, this stage retains **short-sample replay** to ensure the model maintains its short-context instruction-following capability and minimizes capability drift.

---

## 🤝 Collaboration & Training Details

This model is the result of continuous exploration in Agentic AI and reasoning capabilities. 

**Training Infrastructure & Configuration:**
- 🖥️ **Hardware:** Local compute devices / Cloud GPUs (e.g. GB10 / H100 / RTX 5090 / A100)
- ⚙️ **Framework:** Unsloth for efficient fine-tuning

---

## ⚠️ IMPORTANT

> [!CAUTION]
> **Compatibility and Deployment Notice**
> - **Tool Calling Format**: When using this model for tool calling, please ensure that you use a Prompt format and System Prompt that match the training data to activate its Agent capabilities.
> - **Reasoning Output Extraction**: The model's thinking process is typically wrapped in `<think>` and `</think>` tags. When deploying to front-end applications, these tags may need to be parsed and hidden.

---

## 📚 Resources & Guides

👉 **[GitHub Repository: Jackrong-llm-finetuning-guide](https://github.com/R6410418/Jackrong-llm-finetuning-guide.git)**
Visit the repository to dive into our fine-tuning codebase and guides.

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
@misc{jackrong_qwopus35_9b_coder,
  title        = {Qwopus3.5-9B-coder},
  author       = {Jackrong},
  year         = {2026},
  publisher    = {Hugging Face}
}
```
---


<!--End Original Model Card-->

---

# <span id="testllm" style="color: #7F7FFF;">🚀 If you find these models useful</span>

Help me test my **AI-Powered Quantum Network Monitor Assistant** with **quantum-ready security checks**:  

👉 [Quantum Network Monitor](https://readyforquantum.com/?assistant=open&utm_source=huggingface&utm_medium=referral&utm_campaign=huggingface_repo_readme)  


The full Open Source Code for the Quantum Network Monitor Service available at my github repos ( repos with NetworkMonitor in the name) : [Source Code Quantum Network Monitor](https://github.com/Mungert69). You will also find the code I use to quantize the models if you want to do it yourself [GGUFModelBuilder](https://github.com/Mungert69/GGUFModelBuilder)

💬 **How to test**:  
 Choose an **AI assistant type**:  
   - `TurboLLM` (GPT-4.1-mini)  
   - `HugLLM` (Hugginface Open-source models)  
   - `TestLLM` (Experimental CPU-only)  

### **What I’m Testing**  
I’m pushing the limits of **small open-source models for AI network monitoring**, specifically:  
- **Function calling** against live network services  
- **How small can a model go** while still handling:  
  - Automated **Nmap security scans**  
  - **Quantum-readiness checks**  
  - **Network Monitoring tasks**  

🟡 **TestLLM** – Current experimental model (llama.cpp on 2 CPU threads on huggingface docker space):  
- ✅ **Zero-configuration setup**  
- ⏳ 30s load time (slow inference but **no API costs**) . No token limited as the cost is low.
- 🔧 **Help wanted!** If you’re into **edge-device AI**, let’s collaborate!  

### **Other Assistants**  
🟢 **TurboLLM** – Uses **gpt-4.1-mini** :
- **It performs very well but unfortunatly OpenAI charges per token. For this reason tokens usage is limited. 
- **Create custom cmd processors to run .net code on Quantum Network Monitor Agents**
- **Real-time network diagnostics and monitoring**
- **Security Audits**
- **Penetration testing** (Nmap/Metasploit)  

🔵 **HugLLM** – Latest Open-source models:  
- 🌐 Runs on Hugging Face Inference API. Performs pretty well using the lastest models hosted on Novita.

### 💡 **Example commands you could test**:  
1. `"Give me info on my websites SSL certificate"`  
2. `"Check if my server is using quantum safe encyption for communication"`  
3. `"Run a comprehensive security audit on my server"`
4. '"Create a cmd processor to .. (what ever you want)" Note you need to install a [Quantum Network Monitor Agent](https://readyforquantum.com/Download/?utm_source=huggingface&utm_medium=referral&utm_campaign=huggingface_repo_readme) to run the .net code on. This is a very flexible and powerful feature. Use with caution!

### Final Word

I fund the servers used to create these model files, run the Quantum Network Monitor service, and pay for inference from Novita and OpenAI—all out of my own pocket. All the code behind the model creation and the Quantum Network Monitor project is [open source](https://github.com/Mungert69). Feel free to use whatever you find helpful.

If you appreciate the work, please consider [buying me a coffee](https://www.buymeacoffee.com/mahadeva) ☕. Your support helps cover service costs and allows me to raise token limits for everyone.

I'm also open to job opportunities or sponsorship.

Thank you! 😊
