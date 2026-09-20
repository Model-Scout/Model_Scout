---
license: cc-by-4.0
language:
  - en
  - zh
  - ru
  - vi
  - es
  - tr
  - id
  - de
library_name: custom
tags:
  - ingredient-embeddings
  - food
  - computational-gastronomy
  - metapath2vec
  - skip-gram
  - word2vec
  - retrieval
  - feature-extraction
pipeline_tag: feature-extraction
datasets:
  - Kaikaku/epicure-corpus-resources
arxiv: 2605.22391
---

# Epicure-Core

A 300-dimensional skip-gram ingredient embedding over a 1,790-ingredient canonical vocabulary, trained on a blend of (i) typed FlavorDB ingredient-compound metapath walks and (ii) injected pure ingredient-ingredient walks at `ii_repeat=10`. Core is the middle sibling on the chemistry-vs-recipe-context spectrum.

The 10x I-I injection is the design lever that concentrates Core's geometry: participation ratio drops to 94.2 of 300 (vs ~180 for the isotropic Cooc and Chem siblings), average pairwise cosine rises to 0.35, and the resulting concentration coincides with the tightest emergent modes of the three.

Companions in the family: [epicure-cooc](https://huggingface.co/Kaikaku/epicure-cooc) (recipe-context only) and [epicure-chem](https://huggingface.co/Kaikaku/epicure-chem) (chemistry only).

Paper: [Epicure: Navigating the Emergent Geometry of Food Ingredient Embeddings](https://arxiv.org/abs/2605.22391)

## Quick start

```python
from epicure import Epicure

m = Epicure.from_pretrained("Kaikaku/epicure-core")

m.neighbors("chicken", k=5)
# -> [('pork', 0.58), ('beef', 0.57), ('chicken_broth', 0.55),
#     ('peanut', 0.52), ('cream_of_chicken_soup', 0.52)]

m.slerp("rice", "cuisine:South_Asian", theta_deg=30, k=5)
# -> [('turmeric', 0.76), ('mustard_seed', 0.76), ('fenugreek_seed', 0.75),
#     ('coriander', 0.74), ('cumin', 0.74)]

m.closest_mode("chocolate", kind="factor", k=3)
```

## What is in this repo

Identical structure to the Cooc sibling. The Core-specific differences:

- `modes.json`: 193 modes across 44 properties (vs 150/41 for Cooc, 200/43 for Chem).
- `factor_poles.npy` shape: (87, 300).
- `supervised_poles.json`: 113 entries.

See the Cooc model card for the per-file inventory.

## Reported numbers (this sibling)

From [the paper](https://arxiv.org/abs/2605.22391):

- Isotropy: participation ratio `PR = 94.2`, average pairwise cosine 0.35. Concentrated geometry by design (10x I-I injection).
- Direction quality (5-fold CV Spearman rho): baked-in CF 0.40; held-out basic-taste CF 0.42; USDA macros 0.45. Cuisine Cohen's d mean 2.70.
- Emergent modes: 193 modes / 44 properties. Mean within-mode coherence 0.833 against random-pair baseline 0.348 (margin 0.485, tightest of the three siblings).

Core's concentrated geometry pulls both pole tightness and the all-pairs floor upward; the tightness margin (mode coherence minus baseline) is comparable to Cooc and Chem at ~0.5, so the concentration is a design lever, not a defect.

When to pick Core: you want chemistry-aware structure but cannot afford to lose recipe-context companionship entirely. Core's nearest-neighbour for `chicken` is `pork` (chemistry peer) but its full top-5 includes `chicken_broth` and `cream_of_chicken_soup` (recipe context).

## Operator semantics

Same as Cooc. See [epicure-cooc](https://huggingface.co/Kaikaku/epicure-cooc) for the full operator reference. The three operator families (top-K neighbours, closest-mode lookup, SLERP direction arithmetic) are identical across siblings; only the geometry they act on differs.

## Honesty about cuisine pole reconstruction

See the [epicure-cooc model card](https://huggingface.co/Kaikaku/epicure-cooc) for the full discussion. Short version: the eight cuisine-macro-region pole vectors used in the paper's Section 4.2 hero examples are reconstructed here as the unit-mean of every mode whose Claude label contains a cuisine keyword. Core happens to reproduce paper-genre results with high fidelity because the chemistry-mediated walks cluster cuisines by aroma-compound profile.

## Limitations and citation

Same as Cooc. See [the paper Section 5.3](https://arxiv.org/abs/2605.22391) for corpus imbalance, hub coverage, and LLM-dependence notes.

```bibtex
@article{radzikowski2026epicure,
  title   = {Epicure: Navigating the Emergent Geometry of Food Ingredient Embeddings},
  author  = {Radzikowski, Jakub and Chen, Josef},
  journal = {arXiv preprint arXiv:2605.22391},
  year    = {2026}
}
```

License: CC BY 4.0.
