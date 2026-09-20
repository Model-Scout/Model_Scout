---
language:
  - ko
license: gemma
library_name: peft
pipeline_tag: sentence-similarity
base_model: google/embeddinggemma-300m
base_model_relation: adapter
tags:
  - embeddings
  - sentence-transformers
  - feature-extraction
  - stylometry
  - authorship-analysis
  - korean
  - fiction
  - peft
  - lora
datasets:
  - peterkirby/pan2020_dict_author_fandom_doc
  - StyleDistance/synthstel
---

# Munche-768

<p align="center">
  <img src="./assets/baragi-ai.png" width="128" alt="Baragi AI">
</p>

**A 768-dimensional embedding model for Korean fiction style.**

<h3 align="center">
<a href="https://huggingface.co/Baragi-AI/Munche-v2-768">v2 is now available with more generalized embedding ability!</a>
</h3>

Munche-768 by **Baragi AI** represents stylistic similarity between Korean fiction passages. It was trained to reduce reliance on names and shared plot content while preserving signals such as sentence rhythm, dialogue balance, paragraph structure, punctuation, and narrative phrasing.

Munche-768 is a rank-32 LoRA adapter for [`google/embeddinggemma-300m`](https://huggingface.co/google/embeddinggemma-300m). The base model, pooling module, and dense projections remain frozen.

<h3 align="center">
  <a href="https://huggingface.co/spaces/Baragi-AI/Munche-768">Explore the interactive evaluation and 3D embedding space →</a>
</h3>

**Related model:** [Munche-768-AI-Detector](https://huggingface.co/Baragi-AI/Munche-768-AI-Detector) applies Munche-768 to Korean genre-fiction dataset triage.

## Results

All Korean test sets are separated from training by work and verified author group.

![Munche-768 performance compared with EmbeddingGemma](./assets/performance-comparison.svg)

The chart compares the four primary held-out Korean fiction evaluations. Higher scores are better.

| Evaluation | Base EmbeddingGemma | Munche-768 |
|---|---:|---:|
| Same-work retrieval mAP@R | 56.7% | **84.0%** |
| Same-author cross-work retrieval mAP@R | 59.6% | **79.9%** |
| Content-hard accuracy | 22.6% | **83.1%** |
| Counterfactual ordering accuracy | 0.0% | **79.5%** |

### Additional test results

| Evaluation | Result | Test size |
|---|---:|---:|
| Same-work retrieval Hit@1 | 95.6% | 1,089 queries |
| Same-author cross-work retrieval Hit@1 | 88.2% | 348 queries |
| Pseudonym-query retrieval mAP@R | 81.1% | 1,089 queries |
| Strong-format retrieval mAP@R | 68.3% | 1,089 queries |
| PAN21 cross-fandom authorship AUROC | 89.5% | 19,999 pairs |

`Same-work retrieval` searches for non-overlapping passages from the same work within a same-genre gallery. `Same-author cross-work retrieval` searches for another work by the same author. `Content-hard accuracy` requires the correct passage to outrank four content-similar passages from other works. `Counterfactual ordering accuracy` requires another human passage from the same work to outrank an LLM rewrite that preserves the source content.

## Usage

Access to the gated EmbeddingGemma base model is required.

```bash
pip install torch sentence-transformers peft
```

```python
from peft import PeftModel
from sentence_transformers import SentenceTransformer

base = SentenceTransformer("google/embeddinggemma-300m")
base[0].auto_model = PeftModel.from_pretrained(
    base[0].auto_model,
    "Baragi-AI/Munche-768",
)
base.max_seq_length = 2048

texts = [
    "첫 번째 한국어 소설 본문",
    "두 번째 한국어 소설 본문",
]
embeddings = base.encode(
    texts,
    normalize_embeddings=True,
    convert_to_numpy=True,
)

similarity = embeddings @ embeddings.T
print(embeddings.shape)  # (2, 768)
```

Cosine similarity can be calculated with a dot product when the normalized embeddings returned above are used.

## Model details

| Property | Value |
|---|---|
| Base model | `google/embeddinggemma-300m` |
| Output dimension | 768 |
| Maximum input length | 2,048 tokens |
| Adapter | LoRA rank 32, alpha 64, dropout 0.05 |
| Target modules | Attention q/k/v/o and MLP gate/up/down projections |
| Trainable parameters | 8,355,840 |
| Pooling and projection | Original EmbeddingGemma modules, frozen |
| Output normalization | L2 normalization |

## Training data

The private Korean corpus contains fiction passages with work and verified author-group labels. Raw text, titles, author identities, and source paths are not distributed.

The Korean training relations include:

- 64,000 positive pairs from the same work or verified works by the same author;
- 24,000 content-similar passages from different works;
- 1,306 pairs of human passages and content-preserving LLM rewrites;
- original, pseudonym-replaced, and proper-noun-masked Korean inputs.

The model also uses cross-fandom authorship relations reconstructed from PAN fanfiction data and feature-disjoint style relations from SynthSTEL. Korean and English examples are optimized in separate contrastive batches.

## Intended use

Munche-768 is designed for:

- retrieving Korean fiction passages with similar writing style;
- comparing style across works by the same or different authors;
- clustering and auditing fiction corpora;
- comparing style distributions from human writers and language models;
- providing style-similarity signals for research and data curation.

## Limitations

- Evaluation focuses on Korean genre fiction. Performance on poetry, essays, news, translated fiction, and short conversational text has not been established.
- Paragraph boundaries and punctuation remain meaningful signals. Normalizing them reduced same-work retrieval mAP@R from 84.0% to 68.3%.
- Genre, publication period, narrative viewpoint, and dialogue ratio may remain entangled with style.
- Same-author evaluation uses a limited number of verified multi-work author groups.
- SynthSTEL feature-disjoint accuracy was 1.9%. The model should not be presented as a general multilingual style encoder.
- AI and human separation results apply only to the evaluated rewrite procedures and should not be treated as a general AI detector.
- The model is not suitable as sole evidence for forensic or legal authorship attribution.

## AI and human rewrite diagnostic

A logistic regression probe trained on Munche-768 embeddings achieved an AUROC of 0.967 and balanced accuracy of 91.3% on 190 work-disjoint human and LLM rewrite pairs. Human recall was 95.8%, and LLM rewrite recall was 86.8%. This diagnostic measures linear separation within the evaluated content-preserving rewrite distribution.

## License

Munche-768 is a derivative adapter of EmbeddingGemma and is distributed under the [Gemma Terms of Use](https://ai.google.dev/gemma/terms). Use of the base model requires accepting its access conditions on Hugging Face.

The private Korean training corpus and its source text are not included in this repository.

## Citation

```bibtex
@software{munche768,
  title = {Munche-768: Korean Fiction Style Embedding Model},
  author = {Baragi AI},
  year = {2026},
  url = {https://huggingface.co/Baragi-AI/Munche-768}
}
```
