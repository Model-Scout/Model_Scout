---
license: cc-by-4.0
task_categories:
  - audio-classification
  - text-to-speech
tags:
  - speaker-embeddings
  - speaker-clustering
  - voice-diversity
  - TTS
  - emolia
  - speaker-verification
language:
  - en
  - de
  - fr
  - ja
  - ko
  - zh
pretty_name: "Emolia 3K Speaker Clusters"
size_categories:
  - 10K<n<100K
---

# Emolia 3K Speaker Clusters

A curated set of **3,000 diverse speaker clusters** derived from the [TTS-AGI/emolia-hq](https://huggingface.co/datasets/TTS-AGI/emolia-hq) dataset, with up to 20 representative audio samples per cluster.

## Overview

The original emolia-hq dataset contains hundreds of thousands of speech samples with 128-dimensional WavLM speaker timbre embeddings. These were first clustered into 10,000 centroids, then **intelligently pruned to 3,000** using density-aware farthest-point sampling to ensure:

- **Outlier preservation**: Unique/rare voice types are kept (1.4x outlier over-representation)
- **Redundancy reduction**: Dense clusters of similar voices (e.g., many similar bright female voices) are collapsed into representatives
- **Even coverage**: The 3,000 centroids are spread uniformly across the embedding space

## Key Statistics

| Metric | Value |
|--------|-------|
| Total clusters | 3,000 |
| Clusters fully filled (20 samples) | 2994 |
| Total audio samples | 59,977 |
| Samples per cluster | up to 20 |
| Embedding dimension | 128 (WavLM timbre) |
| Distance metric | Cosine |
| Avg DNS-MOS (best samples) | 3.46 |
| Avg duration (best samples) | 9.3s |
| Source dataset | [TTS-AGI/emolia-hq](https://huggingface.co/datasets/TTS-AGI/emolia-hq) |

## Language Distribution (best-of samples)

| Language | Count |
|----------|-------|
| EN | 3000 |

## Repository Structure

```
.
├── cluster_samples/              # Tar archives of all samples
│   ├── cluster_samples_0000-0499.tar
│   ├── cluster_samples_0500-0999.tar
│   ├── cluster_samples_1000-1499.tar
│   ├── cluster_samples_1500-1999.tar
│   ├── cluster_samples_2000-2499.tar
│   ├── cluster_samples_2500-2999.tar
├── cluster_best.tar              # Best sample per cluster (highest DNS-MOS)
│                                 # Contains cluster_best/{0..2999}.mp3 + .json
├── centroids_pruned.npy          # 3000x128 float32 cluster centroids
├── centroids_pruned_indices.npy  # Indices mapping to original 10k centroids
├── pruning_report.html           # Detailed report on the pruning methodology
├── pruning_stats.json            # Raw metrics for all pruning methods tested
├── scripts/
│   ├── prune_centroids.py        # Centroid pruning pipeline
│   └── extract_cluster_samples.py  # Sample extraction pipeline
└── README.md
```

Each `cluster_samples_XXXX-YYYY.tar` contains folders named by cluster index, each with up to 20 `.mp3` + `.json` pairs.

## Pruning Methodology

Three methods were compared to reduce 10,000 centroids to ~3,000:

### 1. HDBSCAN + Medoid Selection
HDBSCAN identifies density-based clusters; noise points (outliers) are preserved, and each cluster is represented by its medoid. **Result**: Could not reach the 2k-4k target range (kept 6,500+ points due to high noise fraction).

### 2. Farthest-Point Sampling with Outlier Protection (Winner)
1. Identify the top 10% most isolated points (by avg cosine distance to 10 nearest neighbors)
2. Pre-seed these 1,000 outliers into the selection
3. Iteratively pick the point farthest from the current selection

**This method won** because it provides the best balance of coverage, spread, and outlier preservation.

### 3. Density-Based Greedy Pruning
Remove points from densest regions first, preserving isolated points. Good outlier preservation but worse coverage quality.

### Quality Metrics (Selected Method)

| Metric | Value | Meaning |
|--------|-------|---------|
| Coverage mean | 0.1185 | Avg cosine dist from any original centroid to nearest selected |
| Coverage max | 0.2741 | Worst-case distance (no centroid is "orphaned") |
| Mean min pairwise | 0.3028 | Selected centroids are well spread apart |
| Outlier preservation | 1.40x | Isolated voices over-represented (desired) |

## Sample Metadata Format

Each `.json` file contains:

```json
{
  "id": "EN_B00042_S00123_W000456",
  "text": "Transcription of the utterance",
  "duration": 8.5,
  "dnsmos": 3.82,
  "speaker": "EN_B00042_S00123",
  "language": "en",
  "emotion_caption": "Natural language description of emotional content",
  "emotion_annotation": { "Arousal_best": 1.5, "Valence_best": 0.8, "..." : "..." },
  "wavelm_timbre_embedding": [0.044, -0.022, "...128 dims..."],
  "_cluster_idx": 42,
  "_cosine_similarity": 0.95
}
```

## Usage

### Load centroids
```python
import numpy as np
centroids = np.load("centroids_pruned.npy")  # (3000, 128)
```

### Find nearest cluster for a new embedding
```python
def find_cluster(embedding, centroids):
    emb = np.array(embedding) / np.linalg.norm(embedding)
    norms = np.linalg.norm(centroids, axis=1, keepdims=True)
    centroids_normed = centroids / np.maximum(norms, 1e-8)
    similarities = centroids_normed @ emb
    return int(np.argmax(similarities)), float(similarities.max())

cluster_idx, similarity = find_cluster(new_embedding, centroids)
```

### Extract samples from tar
```python
import tarfile
with tarfile.open("cluster_samples_0000-0499.tar") as tf:
    tf.extractall(".")
# Now cluster_samples/0/, cluster_samples/1/, ... are available
```

## License

CC-BY-4.0 (inherited from [TTS-AGI/emolia-hq](https://huggingface.co/datasets/TTS-AGI/emolia-hq))

## Citation

```bibtex
@dataset{emolia_3k_speaker_clusters,
  title={Emolia 3K Speaker Clusters},
  author={LAION},
  year={2026},
  url={https://huggingface.co/datasets/laion/emolia-3k-speaker-clusters},
  note={Derived from TTS-AGI/emolia-hq}
}
```
