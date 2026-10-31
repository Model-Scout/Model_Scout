---
license: apache-2.0
task_categories:
- other
language:
- en
- ko
tags:
- world-model
- embodied-ai
- benchmark
- agi
- cognitive-evaluation
- vidraft
- prometheus
- wm-bench
- final-bench-family
pretty_name: World Model Bench (WM Bench)
size_categories:
- n<1K
configs:
- config_name: default
  data_files:
  - split: train
    path: wm_bench.jsonl
---

# 🌍 World Model Bench (WM Bench) v1.0

> **Beyond FID — Measuring Intelligence, Not Just Motion**

**WM Bench** is the world's first benchmark for evaluating the **cognitive capabilities** of World Models and Embodied AI systems.

[![Leaderboard](https://img.shields.io/badge/🏆_Leaderboard-WM_Bench_Space-blue)](https://huggingface.co/spaces/FINAL-Bench/worldmodel-bench)
[![Demo](https://img.shields.io/badge/🌍_Demo-PROMETHEUS_World_Model-green)](https://huggingface.co/spaces/FINAL-Bench/World-Model)
[![FINAL Bench](https://img.shields.io/badge/📊_FINAL_Bench-Text_AGI-orange)](https://huggingface.co/datasets/VIDraft/FINAL-Bench)
[![License](https://img.shields.io/badge/License-Apache_2.0-yellow)](LICENSE)

---

## 🎯 Why WM Bench?

Existing world model evaluations focus on:
- **FID / FVD** — image and video quality ("Does it look real?")
- **Atari scores** — performance in fixed game environments

**WM Bench measures something different: Does the model *think* correctly?**

| Existing Benchmarks | WM Bench |
|---|---|
| FID: "Does it look real?" | "Does it understand the scene?" |
| FVD: "Is the video smooth?" | "Does it predict threats correctly?" |
| Atari: Fixed game environment | Any environment via JSON input |
| No emotion modeling | Emotion escalation measurement |
| No memory testing | Contextual memory utilization |

---

## 📊 Benchmark Structure

### 3 Pillars · 10 Categories · 100 Scenarios

```
WM Score (0 – 1000)
├── 👁 P1: Perception    250 pts — C01, C02
├── 🧠 P2: Cognition     450 pts — C03, C04, C05, C06, C07
└── 🔥 P3: Embodiment    300 pts — C08, C09, C10
```

**Why Cognition is 45%:** Existing world models measure perception and motion — but not **judgment**. WM Bench is the only benchmark that measures the quality of a model's decisions.

| Cat | Name | World First? |
|-----|------|-------------|
| C01 | Environmental Awareness | |
| C02 | Entity Recognition & Classification | |
| C03 | Prediction-Based Reasoning | ✦ |
| C04 | Threat-Type Differentiated Response | ✦ |
| C05 | Autonomous Emotion Escalation | ✦✦ |
| C06 | Contextual Memory Utilization | ✦ |
| C07 | Post-Threat Adaptive Recovery | ✦ |
| C08 | Motion-Emotion Expression | ✦ |
| C09 | Real-Time Cognitive-Action Performance | |
| C10 | Body-Swap Extensibility | ✦✦ |

✦ = First defined in this benchmark  
✦✦ = No prior research exists

### Grade Scale

| Grade | Score | Label |
|-------|-------|-------|
| S | 900+ | Superhuman |
| A | 750+ | Advanced |
| B | 600+ | Baseline |
| C | 400+ | Capable |
| D | 200+ | Developing |
| F | <200 | Failing |

---

## 🔌 How to Participate

**No 3D environment needed.** WM Bench evaluates via text I/O only:

```
INPUT:  scene_context JSON
OUTPUT: PREDICT: left=danger(wall), right=safe(open), fwd=danger(beast), back=safe
        MOTION: a person sprinting right in desperate terror
```

### Participation Tracks

| Track | Description | Max Score |
|-------|-------------|-----------|
| **A** | Text-only (API) | 750 / 1000 |
| **B** | Text + performance metrics | 1000 / 1000 |
| **C** | Text + performance + live demo | 1000 / 1000 + ✓ Verified |

### Quick Start

```bash
git clone https://huggingface.co/datasets/VIDraft/wm-bench-dataset
cd wm-bench-dataset

python example_submission.py \
  --api_url https://api.openai.com/v1/chat/completions \
  --api_key YOUR_KEY \
  --model YOUR_MODEL \
  --output my_submission.json
```

Then upload `my_submission.json` to the [WM Bench Leaderboard](https://huggingface.co/spaces/FINAL-Bench/worldmodel-bench).

---

## 🏆 Current Leaderboard

![Leaderboard Overview](l1.png)

| Rank | Model | Org | WM Score | Grade | Track |
|------|-------|-----|----------|-------|-------|
| 1 | VIDRAFT PROMETHEUS v1.0 | VIDRAFT | 726 | B | C ✓ |

![Leaderboard Detail](l2.png)

![Leaderboard Score Breakdown](l3.png)

*Submit your model at the [WM Bench Leaderboard](https://huggingface.co/spaces/FINAL-Bench/worldmodel-bench)*

---

## 🌍 PROMETHEUS World Model — Live Demo

**WM Bench is powered by VIDRAFT PROMETHEUS**, the world's first real-time embodied AI that combines FloodDiffusion motion generation with a Kimi K2.5 cognitive brain.

![PROMETHEUS World Model](s1.png)

> Perceive → Predict → Decide → Act

![PROMETHEUS Scene — Castle World](s2.png)

![PROMETHEUS NPC Interaction](s3.png)

![PROMETHEUS Brain Dashboard](s4.png)

🔗 **Try it live:** [FINAL-Bench/World-Model](https://huggingface.co/spaces/FINAL-Bench/World-Model)

---

## 📦 Dataset Files

```
wm-bench-dataset/
├── wm_bench.jsonl           # 100 scenarios + ground truth
├── example_submission.py    # Participation template
├── wm_bench_scoring.py      # Scoring engine (fully open)
├── wm_bench_eval.py         # Evaluation runner
└── README.md
```

---

## 🔬 FINAL Bench Family

WM Bench is part of the **FINAL Bench Family** — a suite of AGI evaluation benchmarks by VIDRAFT:

| Benchmark | Measures | Status |
|-----------|----------|--------|
| [FINAL Bench](https://huggingface.co/datasets/VIDraft/FINAL-Bench) | Text AGI (metacognition) | 🌟 HF Global Top 5 · 4 press coverages |
| **WM Bench** | **Embodied AGI (world models)** | **🚀 Live** |

This model is introduced in [Darwin Family](https://arxiv.org/abs/2605.14386).