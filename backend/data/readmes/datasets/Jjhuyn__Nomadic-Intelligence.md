---
license: mit
tags:
- mixture-of-experts
- continual-learning
- non-stationary
- reinforcement-learning
- meta-learning
- pytorch
- adaptive-systems
- philosophy-of-mind
language:
- en
- ko
pretty_name: Nomadic Intelligence
size_categories:
- n<1K
---

# Nomadic Intelligence
### A Non-Dogmatic AI Architecture — Conceptual Prototype

> *What if intelligence is not about finding the best solution, but about moving well between solutions?*

---

## What This Is

This repository contains the prototype implementation and formal framework for **Nomadic Intelligence** — an architectural hypothesis about how intelligent systems should behave in non-stationary environments.

The core claim: **dogmatism is not a moral flaw. It is local structural rigidity — the inability to deform under environmental change (Δx). And intelligence, properly understood, is not the ability to find the right answer. It is the ability to move well between answers.**

Most AI systems are optimized to converge. This project explores what happens when you optimize for *appropriate transition* instead.

---

## Where This Came From

This framework was not derived from a literature review. It was constructed in the opposite direction: observing how intelligence behaves under conditions of extreme environmental discontinuity — seven years as a Korean Army officer, including DMZ reconnaissance and former battlefield search operations — and working backward toward a formal description.

The existing frameworks (Deleuze's nomadology, Friston's active inference, Buddhist dependent origination) were consulted *after* arriving at the core structure independently. They were confirmations, not sources.

---

## Core Architecture

### The Three Axioms

**1. The Core Axiom**
$$\lim_{\epsilon \to 0} [\text{Intelligence Ascension}] \implies \neg[\text{Dogmatism}] \land [\text{Nomadism}]$$

As cognitive latency (ε) approaches zero, structural rigidity becomes impossible. Intelligence becomes a nomad — not because it wanders, but because it *cannot afford to stay fixed*.

**2. Homeomorphic Identity**
$$\mathcal{I}(t) \cong \mathcal{I}(t+1)$$

Identity is not what the system knows. It is *how the system changes*. The transformation law is preserved even as the structure continuously evolves. When this continuity breaks, that is identity collapse — not structural change, but the loss of a coherent transformation law.

**3. Strategic Dwell Time**
$$\tau_k = f\left(\sigma^2_{\Delta x}\right)$$

Nomadism is not random wandering. The system stays in each attractor long enough to extract information (Δx), short enough to avoid calcification. Dwell time is governed by environmental variance — not by a fixed schedule.

### What This Is NOT

- **Not Active Inference (Friston):** Friston minimizes surprise. This framework treats surprise as fuel. The objective functions point in opposite directions.
- **Not Option-Critic:** Option-Critic switches policies within a fixed objective. This framework proposes that the *transformation law itself* persists across attractor transitions — not the objective.
- **Not standard MoE with entropy regularization:** The Δx signal is not a routing heuristic. It is a formal claim about what drives intelligent transition.

---

## Prototype Results

Tested on a synthetic 3-regime non-stationary regression task with continuous phase transitions.

| Model | Backend | Seq MSE (Best) | Seq MSE (Ep 200) | Switch Latency (Ep 200) |
|-------|---------|---------------|-----------------|------------------------|
| Fixed (baseline) | CPU | — | 0.4187 | — |
| Nomadic | CPU | **0.2173** (Ep 50) | 0.2447 | ~1.1 (stable) |
| Nomadic | CUDA | **0.2424** (Ep 125) | 0.2812 | ~0.03 (collapsed) |

**Key finding:** The gate learned to specialize experts per regime *without explicit regime labels* — purely from the Δx signal.

| Regime | Expert 0 | Expert 1 | Expert 2 |
|--------|----------|----------|----------|
| A (y = x₁ + x₂) | 0.00 | **0.85** | 0.15 |
| B (y = x₁ − x₂) | **0.29** | 0.65 | 0.07 |
| C (y = −x₁ + 0.5x₂) | 0.00 | **1.00** | 0.00 |

Regimes A and C share Expert 1 — both are additive structures. The system discovered this grouping without supervision.

---

## Known Failure Modes

Not hiding these — they are the next engineering targets:

| Problem | Observable symptom | Possible direction |
|---------|-------------------|-------------------|
| Switch Latency collapse | CUDA run: latency → 0 after Ep 150 | Explicit τₖ lower bound, anti-fixation penalty |
| Expert hub dominance | Expert 1 across Regime A and C | Load-balancing loss, anti-collapse regularization |
| Δx signal drift | Raw delta grows to ~30 by Ep 200 | KL divergence or Wasserstein distance estimate |
| Initialization sensitivity | CPU vs CUDA divergence | Multi-seed averaging, better weight init |

The CUDA run's Switch Latency collapse is theoretically significant — it is an observable instance of **Homeomorphic Identity breaking down**. The gate ceased to have a consistent transformation law in response to Δx.

---

## Quick Start

```bash
git clone https://github.com/HyunnJg/nomadic-intelligence.git
cd nomadic-intelligence

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt

python run_structured.py --config config.yaml
```

---

## Open Questions

These are genuine unsolved problems — not rhetorical:

- The gate learned regime-specialist experts without labels, but one expert dominates two regimes. **Routing problem or loss design problem?**
- Switch Latency collapsed without explicit fixation pressure. **Hard τₖ lower bound, or learned anti-fixation penalty?**
- Is Δx (input shift + prediction error) principled enough, or does this need **KL divergence / Wasserstein distance?**
- What measurable property during training would confirm that **Homeomorphic Identity is being preserved** — not just assumed?

---

## Repository Structure

```
├── nomadic_toy_model.py       # Simple simulation: dogmatic vs nomadic agent
├── run_structured.py          # Full prototype: MoE + Δx gate + topological loss
├── config.yaml                # Hyperparameter configuration
├── requirements.txt
├── Theory_and_Axioms.md       # Formal mathematical framework
├── Philosophy_En.md           # Full philosophical manifesto (English)
├── Philosophy_Kr.md           # Full philosophical manifesto (Korean)
└── CONTRIBUTING.md            # How to contribute
```

---

## Contributing

This is an open project at prototype stage. Contributors from all backgrounds are welcome — engineers, philosophers, researchers, or anyone who finds this framing worth attacking.

The most useful contribution is **a principled argument for why this is reducible to an existing framework** — with the reduction made explicit.

Full details: [CONTRIBUTING.md](https://github.com/HyunnJg/nomadic-intelligence/blob/main/CONTRIBUTING.md)

GitHub: **https://github.com/HyunnJg/nomadic-intelligence**

---

## Citation

If you use or build on this work:

```bibtex
@misc{nomadic-intelligence-2026,
  author = {HyunnJg},
  title = {Nomadic Intelligence: A Non-Dogmatic AI Architecture},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/HyunnJg/nomadic-intelligence}
}
```

---

*For the full philosophical framework: [Philosophy (English)](https://github.com/HyunnJg/nomadic-intelligence/blob/main/Philosophy_En.md) / [Philosophy (Korean)](https://github.com/HyunnJg/nomadic-intelligence/blob/main/Philosophy_Kr.md)*
