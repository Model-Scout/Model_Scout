---
license: mit
task_categories:
  - robotics
tags:
  - failure-analysis
  - pick-and-place
  - isaac-sim
  - franka-panda
  - ur5e
  - ur3e
  - ur10e
  - domain-randomization
  - latin-hypercube-sampling
  - adaptive-sampling
  - physical-ai
size_categories:
  - 10K<n<100K
language:
  - en
  - ko
---

# RoboGate Failure Dictionary

> **50,000+ Physics-Validated Pick & Place Failure Patterns across 4 Robots (Franka Panda, UR5e, UR3e, UR10e)**

A structured database of robot AI failure patterns collected from **NVIDIA Isaac Sim** physical simulations using **Two-Stage Adaptive Sampling**. Each experiment records the exact conditions under which a robot succeeded or failed at Pick & Place tasks.

## Quick Stats

| | Franka Uniform | Franka Boundary | UR5e | UR3e | UR10e | Combined |
|---|---|---|---|---|---|---|
| **Experiments** | 10,000 | 10,000 | 10,000 | 10,000 | 10,000 | **50,000+** |
| **Success Rate** | 33.3% | 63.8% | 74.3% | 10.0% | 0.0% | — |
| **Franka Combined** | — | 48.6% | — | — | — | — |
| **Risk Model AUC** | 0.65 | **0.777** | — | — | — | 0.777 |
| **Sampling** | Uniform LHS | Boundary LHS | Uniform LHS | Uniform LHS | Uniform LHS | Two-Stage |

## Key Findings

- **friction × mass interaction z = -10.00** — strongest predictor of failure
- **Friction threshold: 0.492 ± 0.031** — below this, failure cascades
- **Mass > 0.93 kg** → Both robots fail at **< 40%** SR (universal danger zone)
- **Boundary equation:** μ*(m) = (1.469 + 0.419m) / (3.691 - 1.400m)
- **AUC improved 0.65 → 0.777** (+19.5%) with boundary-focused sampling
- **Failure mode transition:** friction↓ → timeout → collision → grasp_miss

## Two-Stage Adaptive Sampling

**Stage 1 — Uniform Exploration (40,000)**
- Franka Panda 10K + UR5e 10K
- Latin Hypercube Sampling for uniform parameter space coverage
- Identified boundary regions and initial risk model (AUC 0.65)

**Stage 2 — Boundary-Focused (10,000)**
- Franka Panda only, targeting boundary/transition regions
- Concentrated sampling near friction threshold 0.492
- Revealed failure mode transitions invisible to uniform sampling
- Boosted Risk Model AUC to 0.777 (+19.5%)

## Universal Danger Zones (mass > 0.93 kg)

| Mass Range | Franka SR | UR5e SR |
|---|---|---|
| 0.93 – 1.23 kg | 21.4% | 30.9% |
| 1.23 – 1.52 kg | 14.9% | 25.3% |
| 1.52 – 1.82 kg | 12.5% | 28.9% |
| 1.82 – 2.11 kg | 6.6% | 28.1% |

## Usage

```python
from datasets import load_dataset

ds = load_dataset("liveplex/robogate-failure-dictionary")
print(ds["train"][0])

# Filter danger zones
danger = ds["train"].filter(lambda x: x["zone"] == "danger")
print(f"Danger zones: {len(danger)}")
```

## Parameter Space

| Parameter | Range | Scale | Paper |
|-----------|-------|-------|-------|
| friction | 0.05 – 1.2 | log-uniform | SIMPLER 2024 |
| mass | 0.05 – 2.0 kg | log-uniform | SIMPLER 2024 |
| com_offset | 0.0 – 0.40 | uniform | Suction Grasp 2025 |
| size | 0.02 – 0.12 m | uniform | SIMPLER 2024 |
| ik_noise | 0.0 – 0.04 rad | uniform | ICRA Sim2Real 2025 |
| obstacles | 0 – 4 | integer | RoboFAC 2025 |
| shape | 5 types | categorical | Grasp Anything 2024 |
| placement | 14 types | categorical | ALEAS 2025 |

## Research Foundations

| Design Choice | Paper | Year |
|---|---|---|
| Two-Stage Adaptive Sampling | ALEAS | 2025 |
| friction × mass interaction | SIMPLER | CoRL 2024 |
| Failure taxonomy | RoboFAC | NeurIPS 2025 |
| Cross-robot validation | RoboMIND | RSS 2025 |
| UR-specific failures | Guardian | ICRA 2025 |
| Confidence intervals | SureSim | Badithela 2025 |
| GPU simulation | Isaac Lab | NVIDIA 2025 |
| Grasp evaluation | Isaac Sim Grasping SDG | NVIDIA 2025 |

## VLA Benchmark — 4-Model Leaderboard

Four VLA models evaluated on RoboGate's 68-scenario adversarial suite. **All scored 0% SR** — including NVIDIA's official GR00T N1.6.

| Model | Params | SR | Confidence | Failure Pattern |
|-------|--------|-----|-----------|-----------------|
| Scripted Controller | — | **100%** (68/68) | 76/100 | — |
| **GR00T N1.6 (NVIDIA)** | 3B | 0% (0/68) | 1/100 | grasp_miss + collision |
| OpenVLA (Stanford + TRI) | 7B | 0% (0/68) | 27/100 | grasp_miss dominant, 0 collision |
| Octo-Base (UC Berkeley) | 93M | 0% (0/68) | 1/100 | grasp_miss 79%, collision 21% |
| Octo-Small (UC Berkeley) | 27M | 0% (0/68) | 1/100 | grasp_miss 79.4%, collision 20.6% |

Model size is not the bottleneck — even NVIDIA's flagship 3B model cannot bridge the training-deployment distribution gap.

**Leaderboard:** [robogate.io/vla](https://robogate.io/vla) · **Paper:** [arXiv:2603.22126](https://arxiv.org/abs/2603.22126)

## Citation

```bibtex
@dataset{robogate_failure_dictionary_2026,
  title={RoboGate Failure Dictionary: 50K+ Physics-Validated Pick & Place Failure Patterns},
  author={RoboGate Team},
  year={2026},
  url={https://huggingface.co/datasets/liveplex/robogate-failure-dictionary},
  note={Franka Panda + UR3e + UR5e + UR10e, Two-Stage Adaptive Sampling, AUC 0.777}
}
```

## Links

- **GitHub**: [liveplex-cpu/robogate-failure-dictionary](https://github.com/liveplex-cpu/robogate-failure-dictionary)
- **RoboGate Platform**: [liveplex-cpu/robogate](https://github.com/liveplex-cpu/robogate)
