---
language:
- en
- zh
- ja
- ko
- ar
- th
- de
- fr
- es
- pt
license: mit
size_categories:
- 10M<n<100M
task_categories:
- feature-extraction
tags:
- mechanistic-interpretability
- sparse-autoencoder
- SAE
- neuronpedia
- interpretability
- features
- concepts
pretty_name: Neuronpedia SAE Concepts
configs:
- config_name: v2
  data_files: "v2/**/*.parquet"
  default: true
- config_name: unique
  data_files: "unique/train/*.parquet"
- config_name: clean
  data_files: "clean/train/*.parquet"
- config_name: anthropic
  data_files: "anthropic/train/*.parquet"
- config_name: v1
  data_files: "data/train/*.parquet"
---

# Neuronpedia SAE Concepts

**Complete** extraction of all individual concepts from every Sparse Autoencoder (SAE) released on [Neuronpedia](https://neuronpedia.org), plus all public features from Anthropic's [Towards Monosemanticity](https://transformer-circuits.pub/2023/monosemantic-features/) (2023) and [Scaling Monosemanticity](https://transformer-circuits.pub/2024/scaling-monosemanticity/) (2024) papers.

## Quick Start

```python
from datasets import load_dataset

# Full Neuronpedia dataset (77M rows, streaming recommended)
ds = load_dataset("hbe/neuronpedia-sae-concepts", split="train", streaming=True)

# Unique concepts with essential metadata (45M deduplicated)
unique = load_dataset("hbe/neuronpedia-sae-concepts", "unique", split="train")

# Clean concepts: 3-100 chars, no artifacts (39M)
clean = load_dataset("hbe/neuronpedia-sae-concepts", "clean", split="train")

# ALL Anthropic features (2023 + 2024 papers, 2.15M total)
anthropic = load_dataset("hbe/neuronpedia-sae-concepts", "anthropic", split="train")
```

## Configs Available

| Config | Rows | Description |
|--------|------|-------------|
| **`v2`** (default) | 76,953,489 | Full Neuronpedia per-feature data with 18 columns |
| **`unique`** | 45,248,087 | Deduplicated concepts with essential metadata |
| **`clean`** | 39,103,508 | Clean concepts (3-100 chars) with essential metadata |
| **`anthropic`** | 2,152,711 | All Anthropic SAE features (2023 + 2024 papers) |
| `v1` | 17,493,616 | Legacy (basic 6 columns) |

## anthropic Config

Combines features from two Anthropic papers:

### Towards Monosemanticity (2023) — 2,149,712 features
From a 1-layer 512-neuron transformer trained on text, with SAEs of varying sizes (512 to 131k features) across 92 experimental runs.

| Column | Description |
|--------|-------------|
| `model` | `claude-1-sae` |
| `run` | Experiment run (e.g., `a1`, `b5`, `random3`) |
| `feature_index` | Feature index |
| `concept` | Human-assigned name (30,963 features have names) |
| `autointerp` | GPT-4 auto-interpretation (7,524 features) |
| `density` | Activation density |
| `max_activation` | Peak activation |
| `top_positive_logits` | Top 5 promoted tokens (JSON) |
| `top_negative_logits` | Top 5 suppressed tokens (JSON) |

### Scaling Monosemanticity (2024) — 2,999 features
Curated features from Claude 3 Sonnet SAEs (1M, 4M, 34M feature scales).

| Column | Description |
|--------|-------------|
| `model` | `claude-3-sonnet-{1m,4m,34m}` |
| `feature_index` | Feature index |
| `concept` | CLERP label |
| `group` | `paper` / `safety` / `random` |
| `top_activation_text` | Max-activating text snippet |
| `top_activation_token` | Max-activating token |
| `top_activation_value` | Activation value |

**Note:** Anthropic published only 2,999 of ~38.8M Claude 3 Sonnet features. The full set is proprietary. The 2023 paper features are complete — all publicly visible features from the visualization tool are included.

Source: [transformer-circuits.pub/2023/monosemantic-features/vis/](https://transformer-circuits.pub/2023/monosemantic-features/vis/index.html)

## unique / clean Schema

| Column | Type | Description |
|--------|------|-------------|
| `concept` | string | Human-readable concept description |
| `model` | string | Model (e.g., `qwen3-32b`, `gemma-3-4b`) |
| `source` | string | SAE source identifier |
| `feature_index` | string | Feature index within the SAE |
| `density` | float | Fraction of tokens activating this feature |
| `max_activation` | float | Peak activation value |
| `explanation_method` | string | Auto-interpretation method used |

## v2 Schema (full Neuronpedia)

| Column | Type | Description |
|--------|------|-------------|
| `model` | string | Model the SAE was trained on |
| `source` | string | SAE source: `{layer}-{sourceset}` |
| `feature_index` | string | Feature index |
| `concept` | string | Auto-interpreted concept description |
| `explainer_model` | string | Model used for interpretation (typically `gpt-4o-mini`) |
| `explanation_method` | string | Method (e.g., `oai_token-act-pair`) |
| `density` | float | Feature sparsity |
| `max_activation` | float | Maximum activation value |
| `hook_name` | string | Model hook point |
| `top_positive_logits` | JSON | Top 5 promoted tokens |
| `top_negative_logits` | JSON | Top 5 suppressed tokens |
| `umap_x` | float | UMAP x-coordinate |
| `umap_y` | float | UMAP y-coordinate |
| `umap_cluster` | int | Cluster assignment |
| `log_feature_sparsity` | float | Log sparsity |
| `correlated_features` | JSON | Top 5 correlated feature indices |
| `correlated_neurons` | JSON | Top 5 correlated neuron indices |
| `neuron_alignment` | JSON | Top 3 aligned neuron indices |

## Models Included

### Neuronpedia (ALL complete — 33 models, 1,246 sources)
| Family | Models |
|--------|--------|
| **Gemma 3** | 270m, 1b, 4b, 12b, 27b (+it variants) |
| **Gemma 2** | 2b, 2b-it, 9b, 9b-it, 27b |
| **Qwen 3** | 1.7b, 4b, 8b, 14b, 32b |
| **Qwen 3.5** | 2b, 9b, 27b |
| **Qwen 2.5** | 7b-it |
| **LLaMA** | 3-8b-it, 3.1-8b, 3.1-8b-it, 3.2-1b, 3.3-70b-it |
| **Others** | GPT-2 Small, GPT-OSS 20b, DeepSeek-R1-Distill-LLaMA-8b, Pythia-70m, OLMo-3-32b, CircuitGPT-Python |

### Anthropic
| Source | Features | Model |
|--------|----------|-------|
| Towards Monosemanticity (2023) | 2,149,712 | 1-layer transformer SAEs |
| Scaling Monosemanticity (2024) | 2,999 | Claude 3 Sonnet (1M/4M/34M) |

## Example Concepts

```
"Golden Gate Bridge"                    (anthropic/claude-3-sonnet-34m)
"DNA (lower case)"                      (anthropic/2023/a1)
"at least"                              (qwen3-32b)
"venous and vein contexts"              (qwen3-32b)
"partial derivatives with respect to x" (pythia-70m)
"java import org.springframework"       (gpt2-small)
"circadian clock and rhythm"            (gemma-3-4b)
"Deepfakes, synthetic media, misinfo"   (anthropic/claude-3-sonnet-34m)
```

## Data Sources

**Neuronpedia** (public S3, no API key):
```
https://neuronpedia-datasets.s3.us-east-1.amazonaws.com/v1/{model}/{source}/explanations/
https://neuronpedia-datasets.s3.us-east-1.amazonaws.com/v1/{model}/{source}/features/
```

**Anthropic 2024** (public JSON):
```
https://transformer-circuits.pub/2024/scaling-monosemanticity/features/{paper,safety,rand}_features_public.json
```

**Anthropic 2023** (public JSONL, 92 runs):
```
https://transformer-circuits.pub/2023/monosemantic-features/vis/{run}.jsonl
```

## Citation

```bibtex
@misc{neuronpedia2024,
  title={Neuronpedia},
  author={Johnny Lin},
  year={2024},
  url={https://neuronpedia.org}
}

@article{bricken2023monosemanticity,
  title={Towards Monosemanticity: Decomposing Language Models With Dictionary Learning},
  author={Bricken, Tristan and Templeton, Adly and Batson, Joshua and Chen, Brian and Jermyn, Adam and Conerly, Tom and others},
  journal={Transformer Circuits Thread},
  year={2023}
}

@article{templeton2024scaling,
  title={Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet},
  author={Templeton, Adly and Conerly, Tom and Marcus, Jonathan and others},
  journal={Transformer Circuits Thread},
  year={2024}
}
```

## Version History

- **v2.2** (2025-05-13): Added 2,149,712 features from "Towards Monosemanticity" (2023) to `anthropic` config. All public features from transformer-circuits.pub/2023/monosemantic-features/vis/ now included.
- **v2.1** (2025-05-13): Added `anthropic` config (2,999 Claude 3 Sonnet features). Enriched `unique`/`clean` with essential metadata columns.
- **v2** (2025-05-13): Complete extraction — 77M features from ALL 1,246 sources across 33 models.
- **v1** (2025-05-12): Initial release — 17.5M concepts (7 models partially extracted).
