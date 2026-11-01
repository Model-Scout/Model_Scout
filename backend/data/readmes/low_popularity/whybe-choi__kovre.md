---
pipeline_tag: sentence-similarity
library_name: sentence-transformers
license: apache-2.0
language:
- ko
base_model:
- Qwen/Qwen3-VL-Embedding-2B
datasets:
- whybe-choi/ko-vdr-hn
tags:
- sentence-transformers
- multimodal
- embedding
- visual-document-retrieval
- korean
- matryoshka
---

# KoVRE: Korean Visual Document Retrieval Embedding

<p align="center">
  <img
    src="https://cdn-uploads.huggingface.co/production/uploads/655eeb5532537bcc8d7460ab/VR-ElTS3dohPp-deYSsgt.png"
    alt="KoVRE cover"
    width="600"
  />
</p>

KoVRE is a 2B-parameter single-vector embedding model designed for **Korean visual document retrieval**. It directly matches Korean text queries against rendered document-page images, preserving textual, visual, and structural information without requiring OCR or layout parsing.

KoVRE is initialized from [`Qwen/Qwen3-VL-Embedding-2B`](https://huggingface.co/Qwen/Qwen3-VL-Embedding-2B) and trained in two stages. The first stage performs contrastive learning on 708,729 Korean and English query-page pairs with positive-aware hard-negative mining. The second stage distills relevance scores from `Qwen3-VL-Reranker-8B` using Korean data. Matryoshka Representation Learning enables flexible embedding dimensions from 128 to 2,048.

- **Code:** https://github.com/whybe-choi/kovre
- **Paper:** https://arxiv.org/abs/2608.01389

## Highlights

- **Korean visual document retrieval:** Explicitly adapted for retrieving Korean document-page images with text queries.
- **Efficient single-vector representation:** Stores one dense vector per page instead of a storage-intensive multi-vector representation.
- **Compact but strong:** The 2B model outperforms Qwen3-VL-Embedding-8B and a strong 4B multi-vector baseline in aggregate across the evaluated Korean VDR benchmarks.
- **Flexible embedding dimensions:** Supports Matryoshka embeddings from 128 to 2,048 dimensions; the 256-dimensional representation slightly exceeds the aggregate score of the 4,096-dimensional Qwen3-VL-Embedding-8B baseline.
- **OCR-free retrieval:** Operates directly on rendered page images, retaining layout, table, figure, and other visual information.

## Model Overview

| Property | Value |
|---|---|
| Base model | [`Qwen/Qwen3-VL-Embedding-2B`](https://huggingface.co/Qwen/Qwen3-VL-Embedding-2B) |
| Parameters | 2B |
| Representation | Single vector |
| Full embedding dimension | 2,048 |
| Matryoshka training dimensions | 128, 256, 512, 768, 1,024, 2,048 |
| Input modalities | Text query and document-page image |
| Similarity function | Cosine similarity |
| Maximum image resolution used in training | 1,280 visual tokens (approximately 1.3M pixels) |
| Training languages | Korean and English |

## Intended Use

KoVRE is intended for the following settings:

- Korean visual document retrieval
- OCR-free retrieval over scanned or digitally rendered document pages
- First-stage retrieval for multimodal retrieval-augmented generation
- Search over visually structured documents containing tables, figures, infographics, or complex layouts
- Large-scale document indexes that benefit from single-vector storage

KoVRE is specialized for text-to-document-image retrieval. Performance on general-purpose image-text retrieval, non-document images, and languages other than Korean and English has not been established.

## Usage

### Sentence Transformers

```python
# pip install -U sentence-transformers

from sentence_transformers import SentenceTransformer

model_id = "whybe-choi/kovre"

# Use the full 2,048-dimensional representation.
model = SentenceTransformer(model_id)

queries = [
    "2024년 정보보호 예산은 얼마인가요?",
    "재생에너지 발전량 추이를 보여주는 표",
]

# Local paths, URLs, or PIL images can be used as document-page inputs.
document_pages = [
    "pages/page_1.png",
    "pages/page_2.png",
    "pages/page_3.png",
]

query_embeddings = model.encode(
    queries,
    prompt="Find a document image that matches the given query.",
    normalize_embeddings=True,
)
page_embeddings = model.encode(
    document_pages,
    normalize_embeddings=True,
)

scores = model.similarity(query_embeddings, page_embeddings)
print(scores)
```

For a smaller index, initialize the model with a Matryoshka dimension:

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("whybe-choi/kovre", truncate_dim=256)

query_embeddings = model.encode(
    ["인사 평가 절차를 설명하는 페이지"],
    prompt="Find a document image that matches the given query.",
    normalize_embeddings=True,
)
page_embeddings = model.encode(
    ["pages/page_1.png", "pages/page_2.png"],
    normalize_embeddings=True,
)

scores = model.similarity(query_embeddings, page_embeddings)
```

The model was trained with the following instructions:

- **Query:** `Find a document image that matches the given query.`
- **Document page:** `Represent the user's input.` (the default instruction)

### Transformers

KoVRE preserves the architecture of Qwen3-VL-Embedding. For lower-level inference with Transformers, use the [`Qwen3-VL-Embedding`](https://github.com/QwenLM/Qwen3-VL-Embedding) inference code and replace the model path with `whybe-choi/kovre`.

Recommended dependencies:

```text
transformers>=4.57.0
qwen-vl-utils>=0.0.14
torch>=2.8.0
```

## Input and Output

### Input

- **Query:** Korean text describing the information to retrieve
- **Document:** A rendered document-page image
- **Recommended query instruction:** `Find a document image that matches the given query.`

### Output

- **Type:** L2-normalized dense vector
- **Dimensions:** 128 to 2,048; 2,048 by default
- **Scoring:** Cosine similarity; higher values indicate greater relevance

For Matryoshka inference, truncate the full embedding to the desired prefix dimension and L2-normalize it before computing similarity. The dimensions explicitly optimized during training were 128, 256, 512, 768, 1,024, and 2,048.

## Training

KoVRE uses a two-stage training procedure:

1. **Contrastive learning:** The model is trained on 708,729 Korean and English query-page pairs. Seven hard negatives per query are mined with Qwen3-VL-Embedding-8B, with positive-aware filtering to reduce false negatives. Training uses an InfoNCE objective with self-guide filtering, hardness weighting, in-batch negatives, and Matryoshka dimensions.
2. **Knowledge distillation:** The Stage 1 model is further trained on 265,311 Korean query-level instances. Qwen3-VL-Reranker-8B scores each positive and eight negatives, and the student matches the teacher distribution using KL divergence after per-query min-max score normalization.

The final training corpus contains 406,945 Korean and 301,784 English query-page pairs. English examples are included during Stage 1 to help preserve the backbone's existing retrieval ability while adapting it to Korean documents.

## Evaluation

We evaluate KoVRE with nDCG@10 on two Korean visual document retrieval benchmarks:

- **KoViDoRe:** Four document domains—cybersecurity, economics, energy, and human resources. A query may have multiple relevant pages.
- **SDS KoPub VDR:** Korean public documents with textual, visual, and cross-modal queries; used as an out-of-distribution evaluation set.

`AVG` is the mean across the four KoViDoRe domains. `OVR` is the macro-average across those four domains and SDS KoPub VDR.

<table>
  <thead>
    <tr>
      <th rowspan="2">Model</th>
      <th rowspan="2">Params</th>
      <th colspan="5">KoViDoRe</th>
      <th rowspan="2">SDSKoPub</th>
      <th rowspan="2">OVR</th>
    </tr>
    <tr>
      <th>Cybersecurity</th>
      <th>Economic</th>
      <th>Energy</th>
      <th>HR</th>
      <th>AVG</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>jina-clip-v2</td>
      <td>0.9B</td>
      <td>0.1993</td>
      <td>0.0011</td>
      <td>0.1096</td>
      <td>0.0294</td>
      <td>0.0849</td>
      <td>0.0732</td>
      <td>0.0825</td>
    </tr>
    <tr>
      <td>jina-v5-omni-nano</td>
      <td>1B</td>
      <td>0.4404</td>
      <td>0.0640</td>
      <td>0.2017</td>
      <td>0.0695</td>
      <td>0.1939</td>
      <td>0.0961</td>
      <td>0.1743</td>
    </tr>
    <tr>
      <td>jina-v5-omni-small</td>
      <td>2B</td>
      <td>0.4357</td>
      <td>0.0744</td>
      <td>0.2380</td>
      <td>0.1029</td>
      <td>0.2128</td>
      <td>0.1902</td>
      <td>0.2082</td>
    </tr>
    <tr>
      <td>Qwen3-VL-Embedding-2B</td>
      <td>2B</td>
      <td>0.6111</td>
      <td>0.1592</td>
      <td>0.4123</td>
      <td>0.1842</td>
      <td>0.3417</td>
      <td>0.4285</td>
      <td>0.3591</td>
    </tr>
    <tr>
      <td>Qwen3-VL-Embedding-8B</td>
      <td>8B</td>
      <td><strong>0.7809</strong></td>
      <td>0.2373</td>
      <td>0.6360</td>
      <td>0.3613</td>
      <td>0.5039</td>
      <td>0.7293</td>
      <td>0.5489</td>
    </tr>
    <tr>
      <td>jina-embeddings-v4 (single-vector)</td>
      <td>4B</td>
      <td>0.7280</td>
      <td>0.2058</td>
      <td>0.6273</td>
      <td>0.4106</td>
      <td>0.4929</td>
      <td>0.7222</td>
      <td>0.5388</td>
    </tr>
    <tr>
      <td>jina-embeddings-v4 (multi-vector)</td>
      <td>4B</td>
      <td><u>0.7714</u></td>
      <td>0.2359</td>
      <td><strong>0.6752</strong></td>
      <td>0.4799</td>
      <td>0.5406</td>
      <td><strong>0.7802</strong></td>
      <td><u>0.5885</u></td>
    </tr>
    <tr>
      <td><strong>KoVRE (Stage 1)</strong></td>
      <td>2B</td>
      <td>0.7444</td>
      <td><u>0.2797</u></td>
      <td>0.6506</td>
      <td><u>0.5002</u></td>
      <td><u>0.5437</u></td>
      <td>0.7214</td>
      <td>0.5792</td>
    </tr>
    <tr>
      <td><strong>KoVRE (Stage 1 + Stage 2)</strong></td>
      <td>2B</td>
      <td>0.7627</td>
      <td><strong>0.2987</strong></td>
      <td><u>0.6576</u></td>
      <td><strong>0.5082</strong></td>
      <td><strong>0.5568</strong></td>
      <td><u>0.7324</u></td>
      <td><strong>0.5919</strong></td>
    </tr>
  </tbody>
</table>

### Matryoshka Dimensions

KoVRE retains strong retrieval performance as the embedding dimension is reduced. At 256 dimensions, KoVRE reaches 0.5500 OVR nDCG@10, slightly above Qwen3-VL-Embedding-8B at 4,096 dimensions (0.5489).

<p>
  <img
    src="https://cdn-uploads.huggingface.co/production/uploads/655eeb5532537bcc8d7460ab/hBEv1X-8m2Vb8ngvy7rp0.png"
    alt="Overall nDCG@10 across KoVRE Matryoshka embedding dimensions"
    width="600"
  />
</p>

## Limitations

- KoVRE is specialized for Korean visual document retrieval and has not been comprehensively evaluated for general multimodal retrieval or other languages.
- The Korean training corpus contains 35,815 distinct page images, substantially fewer than the 226,714 English page images. This may limit generalization to Korean layouts and document types that are underrepresented in the training data.
- Evaluation is currently limited to KoViDoRe and SDS KoPub VDR. Performance may vary on different scanning conditions, resolutions, page formats, and domains.
- As with other embedding retrievers, similarity scores are relative ranking signals and should not be interpreted as calibrated probabilities.

## License

KoVRE is released under the Apache 2.0 License.

## Citation

If you find KoVRE useful, please cite:

```bibtex
@article{choi2026kovre,
  title={KoVRE: Training an Efficient Embedding Model for Korean Visual Document Retrieval},
  author={Choi, Yongbin and Shim, Gyuho and Jang, Youngjoon},
  journal={arXiv preprint arXiv:2608.01389},
  year={2026}
}
```
