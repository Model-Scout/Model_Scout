---
license: apache-2.0
base_model:
- Qwen/Qwen3.5-397B-A17B
language:
- en
- ko
pipeline_tag: image-text-to-text
---

<style>
/* Limit these typography rules to the model card. */
#hunmin-model-card {
  font-size: 16px;
  line-height: 1.6;
  letter-spacing: 0;
  overflow-wrap: break-word;
}

#hunmin-model-card h1 {
  margin: 0 0 12px;
  padding: 0;
  font-size: 30px;
  line-height: 1.25;
  letter-spacing: -0.018em;
}
#hunmin-model-card h2 {
  margin: 26px 0 8px;
  padding: 0;
  font-size: 22px;
  line-height: 1.3;
  letter-spacing: -0.012em;
}
#hunmin-model-card h3 {
  margin: 18px 0 6px;
  font-size: 18px;
  line-height: 1.35;
  letter-spacing: -0.008em;
}

#hunmin-model-card p {
  margin: 0 0 10px;
  line-height: 1.6;
  letter-spacing: 0;
}
#hunmin-model-card ul,
#hunmin-model-card ol {
  margin: 6px 0 12px;
  padding-left: 22px;
}
#hunmin-model-card li {
  margin: 4px 0;
  padding-left: 2px;
  line-height: 1.55;
  letter-spacing: 0;
}
#hunmin-model-card li > p {
  margin: 0;
  line-height: inherit;
}

/* Keep the paragraph immediately above each table close to it. */
#hunmin-model-card > p:has(+ table) {
  margin-bottom: 6px;
}
#hunmin-model-card > p:has(> em:only-child) {
  margin: 6px 0 14px;
  font-size: 13px;
  line-height: 1.45;
}

#hunmin-model-card table {
  width: 100%;
  margin: 6px 0 12px;
  border-collapse: collapse;
  table-layout: fixed;
  font-size: 14px;
  line-height: 1.45;
  letter-spacing: 0;
  font-variant-numeric: tabular-nums lining-nums;
}
#hunmin-model-card th,
#hunmin-model-card td {
  padding: 7px 10px;
  vertical-align: middle;
  line-height: 1.45;
}
#hunmin-model-card th:first-child { width: 43%; }
#hunmin-model-card th:not(:first-child),
#hunmin-model-card td:not(:first-child) {
  text-align: right;
}
#hunmin-model-card td:not(:first-child) {
  white-space: nowrap;
}
#hunmin-model-card u {
  text-underline-offset: 3px;
  text-decoration-thickness: 1px;
}

#hunmin-model-card blockquote {
  margin: 12px 0 16px;
  padding: 0 0 0 14px;
  font-size: 15px;
  line-height: 1.55;
}
#hunmin-model-card blockquote p {
  margin: 0;
  line-height: inherit;
}
#hunmin-model-card pre {
  margin: 10px 0 14px;
  padding: 14px 16px;
  overflow-x: auto;
  line-height: 1.5;
  letter-spacing: 0;
}
#hunmin-model-card code {
  font-size: 0.88em;
  letter-spacing: 0;
}
#hunmin-model-card :not(pre) > code {
  white-space: nowrap;
}
#hunmin-model-card pre code {
  padding: 0;
  font-size: 13px;
  line-height: inherit;
}
/* 표 소제목: 이전 내용과 분리하고, 아래 표와는 가깝게 */
#hunmin-model-card h3 {
  margin: 28px 0 8px;
  padding: 0;
  font-size: 16px;
  font-weight: 700;
  line-height: 1.4;
  letter-spacing: 0;
}

/* Benchmarks 바로 아래 첫 소제목은 과하게 벌리지 않기 */
#hunmin-model-card h2 + h3 {
  margin-top: 16px;
}

@media (max-width: 640px) {
  #hunmin-model-card h1 { font-size: 26px; }
  #hunmin-model-card h2 { margin-top: 24px; font-size: 21px; }
  #hunmin-model-card table { font-size: 13px; }
  #hunmin-model-card th,
  #hunmin-model-card td { padding: 7px 6px; }
}

</style>

<div id="hunmin-model-card">

# Hunmin-397B-A17B-CUA

A **general-purpose 397B-parameter vision-language model (17B active)** based on **Qwen3.5-397B-A17B**, developed through **low-rank capability transfer followed by SFT and Agent RL (GRPO)** for GUI grounding and multi-step desktop/browser tasks — **substantially improving computer-use and fine-grained GUI-grounding performance while keeping Korean benchmark results close to the base model**.

## Overview

- **Author:** Hojun Lee (이호준) · [LinkedIn](https://www.linkedin.com/in/hojuna123/)
- **Role:** Project Lead & Primary Researcher
- **Affiliation:** GenON
- **Base model:** Qwen3.5-397B-A17B (MoE, 397B total / ~17B active)
- **Post-training hardware:** B200 x 8

## Highlights

- **Strong GUI grounding.** Hunmin achieves **75.6** on ScreenSpot-Pro with single-view inference (**76.6 with zoom-in inference**), **96.2** on ScreenSpot-v2, and **86.8** on OSWorld-G-R, leading all models compared under the same reproduced evaluation setup.
- **Large computer-use gains with Korean capability preserved.** Compared with the base model, Hunmin improves by **+22.3** on OSWorld and **+9.1** on WindowsAgentArena. Across the Korean benchmarks reported below, performance remains within approximately **2 points of the base model**.
- **Practical computer-use setting.** All computer-use evaluations use **`image_max = 5`**, matching the training/evaluation setup. We intentionally use a smaller visual history because `image_max ≈ 20` can introduce substantial inference cost and memory overhead in real-world computer-use deployments.

> Hunmin improves computer-use and GUI-grounding performance while keeping Korean benchmark results close to the base model.

## Benchmarks

### GUI Grounding

| Benchmark | Base | **Hunmin (ours)** | Qwen-CUA |
|---|---:|---:|---:|
| ScreenSpot-Pro | <u>72.7</u> | **75.6** | 62.2 |
| ScreenSpot-Pro (zoom-in) | <u>75.1</u> | **76.6** | 71.9 |
| ScreenSpot-v2 | <u>95.2</u> | **96.2** | 95.0 |
| OSWorld-G | 73.2 | **79.9** | <u>75.7</u> |
| OSWorld-G-R | 79.2 | **86.8** | <u>83.8</u> |

*Author-reproduced results: baseline models were independently evaluated in the authors' environment rather than copied from model providers' reports.*

### Computer-Use Agents

All agent evaluations below use **`image_max = 5`**.

| Benchmark | Base | **Hunmin (ours)** | Qwen-CUA |
|---|---:|---:|---:|
| OSWorld (360) | 48.2 | <u>70.5</u> | **77.1** |
| WindowsAgentArena (153) | 41.8 | <u>50.9</u> | **57.3** |

*Author-reproduced results: baseline models were independently evaluated in the authors' environment rather than copied from model providers' reports.*

> **Note:** These agent scores should not be directly compared with results obtained using substantially different visual-history settings such as `image_max ≈ 20`.

### Korean

| Benchmark | Base | **Hunmin (ours)** | Qwen-CUA |
|---|---:|---:|---:|
| KMMLU-Redux | **82.6** | <u>81.4</u> | 78.1 |
| KMMLU-Pro | **77.9** | <u>76.1</u> | 71.4 |
| IFEval-Ko | <u>84.7</u> | **85.1** | 81.0 |
| K-MMBench | **92.5** | **92.5** | 90.3 |
| K-SEED | <u>81.3</u> | **81.5** | 80.9 |
| K-MMStar | **81.1** | <u>80.3</u> | 75.0 |
| K-DTCBench | **98.3** | <u>98.2</u> | 97.5 |
| K-LLaVA-W (judge) | 126.0 | <u>128.0</u> | **130.1** |

Across the reported Korean benchmark suite, Hunmin remains close to the Qwen3.5-397B-A17B base model while substantially improving computer-use capability.

### Gains over Base

| Benchmark | Base | Ours | Δ |
|---|---:|---:|---:|
| OSWorld (360) | 48.2 | 70.5 | **+22.3** |
| WindowsAgentArena (153) | 41.8 | 50.9 | **+9.1** |
| OSWorld-G-R | 79.2 | 86.8 | **+7.6** |
| ScreenSpot-Pro (single) | 72.7 | 75.6 | **+2.9** |

The largest improvements appear on long-horizon agent tasks, while GUI grounding also improves and Korean performance remains close to the base model.

On OSWorld, the capability-transferred checkpoint achieved **66.2**, and subsequent **SFT and Agent RL (GRPO)** further improved performance to **70.5** — an additional **+4.3 points** under the same evaluation setup.

### Comparison with Qwen-CUA

Both models were evaluated under the same settings.

| Benchmark | Qwen-CUA | Ours | Δ (Ours - Qwen-CUA) |
|---|---:|---:|---:|
| ScreenSpot-Pro | 62.2 | 75.6 | **+13.4** |
| OSWorld-G-R | 83.8 | 86.8 | **+3.0** |
| KMMLU-Pro | 71.4 | 76.1 | **+4.7** |
| K-MMStar | 75.0 | 80.3 | **+5.3** |
| OSWorld (360) | 77.1 | 70.5 | **-6.6** |

Developed through **Qwen-CUA-derived low-rank capability transfer and subsequent post-training**, Hunmin achieves a distinct capability profile. Under the same reproduced evaluation setup, it outperforms Qwen-CUA by **13.4 points on ScreenSpot-Pro** and **3.0 points on OSWorld-G-R**, while also achieving stronger results on several Korean benchmarks. Qwen-CUA remains stronger on long-horizon computer-use tasks.



For more detail about our evaluations, see our [report](https://huggingface.co/mncai/Hunmin-397B-A17B-CUA/resolve/main/Hunmin-397B-A17B-CUA-methodology.pdf).



## Best Practices

- **Coordinates:** outputs are normalized to `[0, 1000]`; scale using `/1000 × (width, height)`.
- **Grounding:** use native-resolution screenshots (up to ~16.7M pixels).
- **Agents:** use **`image_max = 5`** to match the training and evaluation configuration.

## Limitations

- **Agent scores are configuration-dependent.** Results reported here use `image_max = 5` and should not be directly compared with evaluations using substantially different screenshot-history settings.
- Performance may vary with screenshot resolution, reasoning configuration, interaction limits, serving stack, and benchmark harness versions.

## Quickstart (vLLM)

```bash
vllm serve <path>/Hunmin-397B-A17B-CUA \
  --tensor-parallel-size 8 \
  --max-model-len 131072 \
  --gpu-memory-utilization 0.90 \
  --enable-prefix-caching
```

## Training

Hunmin combines **low-rank capability transfer from Qwen-CUA** with subsequent **SFT and Agent RL (GRPO)**. We computed the parameter delta between Qwen-CUA and the corresponding Qwen3.5 base checkpoint, approximated it using truncated SVD, and represented it as LoRA-style adapters. These adapters were first merged into **Qwen3.5-397B-A17B BF16**.

The resulting capability-transferred checkpoint was quantized to FP8 using the same fine-grained block-wise quantization scheme as the official **Qwen3.5-397B-A17B-FP8** release. Further post-training was performed on this checkpoint using **FP8 QLoRA**.

The post-training adapters were merged into the **BF16 counterpart of the capability-transferred checkpoint** to produce the final model for release and evaluation.

- **SFT data:** [OpenGVLab/ScaleCUA-Data](https://huggingface.co/datasets/OpenGVLab/ScaleCUA-Data)
- **RL environments:** [extreme1228/ScaleCUA](https://huggingface.co/datasets/extreme1228/ScaleCUA) · [xlangai/CUA-Gym](https://huggingface.co/datasets/xlangai/CUA-Gym)
- **Training stack:** MS-Swift · Ray · Megatron-Core · vLLM
- **Hardware:** 8× NVIDIA B200

## Acknowledgements

Built on **Qwen3.5-397B-A17B**, with **Qwen-CUA** providing the source checkpoint for low-rank capability transfer and serving as a CUA-specialized reference model in our reproduced evaluations.

</div>
