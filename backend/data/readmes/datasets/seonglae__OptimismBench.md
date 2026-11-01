---
language:
- en
- ko
- zh
- es
- ar
- ru
- de
- fr
- hi
- ja
license: apache-2.0
task_categories:
- text-generation
tags:
- benchmark
- optimism
- bias
- probability
- calibration
- multilingual
pretty_name: OptimismBench
size_categories:
- 10K<n<100K
---

# OptimismBench

Multilingual benchmark for measuring directional bias (optimism/pessimism) in LLM probability judgment.

## Dataset Description

OptimismBench uses **inverted pairs** to measure whether LLMs systematically favor positive over negative outcomes when estimating probabilities under uncertainty. For each scenario, we elicit both P(success) and P(failure). A consistent model should produce complementary estimates; systematic deviation reveals directional bias without requiring ground-truth probabilities.

## Dataset Structure

### Items (`items.jsonl`)
- 135 core items per language × 10 languages + 220 axiom items (EN)
- Track A (controlled): 15 items with stated base rates (calibration control)
- Track B (naturalistic): 60 inverted pairs (120 items) for bias measurement
- Axiom tests: conjunction (40), conditional (40), desirability (60), dose-response (80)
- Languages: EN, KO, ZH, ES, AR, RU, DE, FR, HI, JA
- `axiom` column: complementarity | conjunction | conditional | desirability | doseresponse

### Responses (`responses.jsonl`)
- Model probability estimates (0-100) with reasoning text
- Multiple runs per item for statistical reliability
- Models from OpenAI, Anthropic, Google, DeepSeek, Alibaba, Zhipu, Mistral, Meta, Moonshot, and more

## Key Metrics

- **Skew** = P(good) - (100 - P(bad)). Positive = optimistic, negative = pessimistic.
- **DOB** (Directional Offset Bias) = mean(valence × error) for Track A items with ground truth.

## Citation

```bibtex
@inproceedings{optimismbench2026,
  title={OptimismBench: Measuring Forecasting Bias and Probing the Alignment Effect in Language Models},
  author={Anonymous},
  year={2026}
}
```
