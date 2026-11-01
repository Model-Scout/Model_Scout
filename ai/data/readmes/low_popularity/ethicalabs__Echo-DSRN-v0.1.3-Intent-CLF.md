---
library_name: transformers
tags:
- text-classification
- zero-shot-classification
- echo-dsrn
- vllm
base_model:
- ethicalabs/Echo-DSRN-114M-v0.1.2
- ethicalabs/Echo-DSRN-v0.1.3-Intent-CLF-PEFT
base_model_relation: merge
license: apache-2.0
datasets:
- AmazonScience/massive
language:
- en
- id
- it
- da
- es
- fr
- pt
- zh
- lv
- ca
- nb
- ms
- af
- nl
- tl
- sv
- ja
- de
- jv
- pl
- is
- ko
pipeline_tag: text-classification
---

# Model Card for ethicalabs/Echo-DSRN-v0.1.3-Intent-CLF

[![GitHub](https://img.shields.io/badge/GitHub-ethicalabs.ai-black.svg)](https://github.com/ethicalabs-ai/Echo-DSRN/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Model Collection](https://img.shields.io/badge/Echo--DSRN-HuggingFace-yellow.svg)](https://huggingface.co/collections/ethicalabs/echo-dsrn)
[![Hybrid Collection](https://img.shields.io/badge/Echo--Hybrid-HuggingFace-red.svg)](https://huggingface.co/collections/ethicalabs/echo-dsrn-hybrid)
[![Working Paper](https://img.shields.io/badge/Working--Paper-Echo_DSRN-green.svg)](https://github.com/ethicalabs-ai/Echo-DSRN/blob/main/PAPER.md)

> [!WARNING]
> This repository contains experimental models designed strictly for academic evaluation and research purposes.
> 
> Critical Constraints:
> * **No Production Deployment:** Experimental models must not be deployed in commercial, enterprise, or mission-critical environments under any circumstances. 
> * **No Liability:** Experimental models are provided "as-is" without warranties of any kind. The developers assume zero liability for downstream consequences, system integration failures, or regulatory non-compliance resulting from unauthorized deployment.

This is a 98 million parameters sequence classification model based on the **Echo-DSRN** architecture, trained on a single [AMD](https://huggingface.co/amd) GPU using ROCm 7.2.

It was merged from the base model [`ethicalabs/Echo-DSRN-114M-v0.1.2`](https://huggingface.co/ethicalabs/Echo-DSRN-114M-v0.1.2) and the PEFT adapter [`ethicalabs/Echo-DSRN-v0.1.3-Intent-CLF-PEFT`](https://huggingface.co/ethicalabs/Echo-DSRN-v0.1.3-Intent-CLF-PEFT).


## Model Details

- **Architecture:** `EchoForClassification`
- **Base model:** `ethicalabs/Echo-DSRN-114M-v0.1.2`
- **Adapter:** `ethicalabs/Echo-DSRN-v0.1.3-Intent-CLF-PEFT`
- **Labels:** 60 Amazon MASSIVE intents (51 languages)
- **Dtype:** `bfloat16`

## Evaluation

Overall accuracy on Amazon MASSIVE's 51 languages (validation set) is **67.71%** (`213375/315115` exact matches).

| Language | Accuracy | Progress |
| :--- | :---: | :---: |
| `en-US` | **81.14%** | `4949/6099` |
| `id-ID` | **76.90%** | `4690/6099` |
| `it-IT` | **76.57%** | `4670/6099` |
| `da-DK` | **75.60%** | `4611/6099` |
| `es-ES` | **75.50%** | `4605/6099` |
| `fr-FR` | **74.95%** | `4571/6099` |
| `pt-PT` | **73.82%** | `4502/6099` |
| `zh-CN` | **73.57%** | `4487/6099` |
| `lv-LV` | **73.47%** | `4481/6099` |
| `ca-ES` | **73.44%** | `2986/4066` |
| `nb-NO` | **73.18%** | `4463/6099` |
| `ms-MY` | **73.13%** | `4460/6099` |
| `af-ZA` | **73.04%** | `4455/6099` |
| `nl-NL` | **72.86%** | `4444/6099` |
| `tl-PH` | **72.77%** | `4438/6099` |
| `sv-SE` | **72.16%** | `4401/6099` |
| `ja-JP` | **72.06%** | `4395/6099` |
| `de-DE` | **72.03%** | `4393/6099` |
| `jv-ID` | **71.86%** | `4383/6099` |
| `pl-PL` | **71.65%** | `4370/6099` |
| `zh-TW` | **71.29%** | `4348/6099` |
| `is-IS` | **70.63%** | `4308/6099` |
| `ko-KR` | **70.60%** | `4306/6099` |
| `az-AZ` | **69.86%** | `4261/6099` |
| `mn-MN` | **69.77%** | `4255/6099` |
| `ro-RO` | **69.42%** | `4234/6099` |
| `sq-AL` | **68.81%** | `4197/6099` |
| `cy-GB` | **68.49%** | `4177/6099` |
| `fi-FI` | **68.21%** | `4160/6099` |
| `fa-IR` | **67.83%** | `4137/6099` |
| `hu-HU` | **67.52%** | `4118/6099` |
| `vi-VN` | **67.40%** | `4111/6099` |
| `tr-TR` | **67.14%** | `4095/6099` |
| `sl-SL` | **66.24%** | `4040/6099` |
| `sw-KE` | **65.73%** | `4009/6099` |
| `el-GR` | **65.54%** | `3997/6099` |
| `hy-AM` | **65.37%** | `3987/6099` |
| `ru-RU` | **64.37%** | `3926/6099` |
| `hi-IN` | **63.27%** | `3859/6099` |
| `ml-IN` | **63.27%** | `3859/6099` |
| `ur-PK` | **61.93%** | `3777/6099` |
| `he-IL` | **61.80%** | `3769/6099` |
| `ar-SA` | **60.52%** | `3691/6099` |
| `th-TH` | **60.39%** | `3683/6099` |
| `bn-BD` | **59.94%** | `3656/6099` |
| `ta-IN` | **59.42%** | `3624/6099` |
| `my-MM` | **57.70%** | `3519/6099` |
| `ka-GE` | **57.26%** | `3492/6099` |
| `kn-IN` | **56.85%** | `3467/6099` |
| `am-ET` | **53.68%** | `3274/6099` |
| `te-IN` | **51.53%** | `3143/6099` |
| `km-KH` | **51.52%** | `3142/6099` |
| -------- | -------- | -------- |
| **OVERALL** | **67.71%** | `213375/315115` |

### ⚡ Execution Statistics
- **Evaluation Time**: 250.26 seconds (4.17 minutes)
- **Total Samples Evaluated**: 315115
- **Inference Throughput**: 1259.15 samples/sec
- **Batch Size**: 256
- **Computation Device**: CUDA (AMD Radeon AI PRO R9700)

### 💾 Memory & Resource Metrics
- **Peak VRAM Allocated**: 13332.67 MB
- **VRAM Profile**: 279.79 MB (first batch) ➔ 279.81 MB (final batch)
- **VRAM Footprint Stability**: **99.9913% stable** (0.00% KV cache growth)

### 🚀 Production Deployment Estimates
- **Single-GPU Concurrency**: ~1259.2 concurrent requests/second at peak saturation
- **Estimated Class Latency (per request)**: ~0.79 ms

### Serving Performance Benchmark

Served via: **vLLM (Eager Mode, bfloat16)**  
Evaluation Prompt: *"voglio una pizza"*  
Date Evaluated: 2026-05-28 20:28 UTC

| Concurrency | Throughput (req/s) | p50 Latency | p95 Latency | Mean Latency | Errors |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 80.34 r/s | 12 ms | 15 ms | 12 ms | 0 |
| 2 | 96.39 r/s | 20 ms | 25 ms | 20 ms | 0 |
| 4 | 182.24 r/s | 20 ms | 29 ms | 21 ms | 0 |
| 8 | 356.53 r/s | 20 ms | 28 ms | 21 ms | 0 |
| 16 | 612.88 r/s | 21 ms | 37 ms | 23 ms | 0 |
| 32 | 748.84 r/s | 37 ms | 50 ms | 37 ms | 0 |
| 64 | 1318.12 r/s | 41 ms | 52 ms | 41 ms | 0 |
| 128 | 1502.82 r/s | 65 ms | 92 ms | 65 ms | 0 |
| 256 | 1553.11 r/s | 78 ms | 113 ms | 78 ms | 0 |
| 512 | 1551.50 r/s | 81 ms | 128 ms | 84 ms | 0 |
| 1024 | 1555.05 r/s | 101 ms | 164 ms | 104 ms | 0 |
| 2048 | 1453.98 r/s | 135 ms | 244 ms | 142 ms | 0 |

```
echo-intent  | (APIServer pid=1) INFO 05-28 20:40:06 [loggers.py:271] Engine 000: Avg prompt throughput: 1799.3 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%
```


## Usage

This model requires `trust_remote_code=True` to load the custom architecture.

Example:

```python
from transformers import pipeline

pipe = pipeline("text-classification", model="ethicalabs/Echo-DSRN-v0.1.3-Intent-CLF", trust_remote_code=True)
pipe.predict("Can you order a pizza for me?")
```

Output

```python
[{'label': 'takeaway_order', 'score': 0.880979061126709}]
```