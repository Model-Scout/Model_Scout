---
language: ko
license: cc-by-sa-4.0
library_name: sentence-transformers
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- transformers
- korean
- matryoshka
base_model: klue/roberta-base
datasets:
- kor_nli
- klue
---

# jhgan/ko-sroberta-nli-mrl

This is a [sentence-transformers](https://www.SBERT.net) model fine-tuned with
[Matryoshka Representation Learning (MRL)](https://arxiv.org/abs/2205.13147)
on top of `klue/roberta-base`. The model produces 768-dim embeddings, but the first
*m* dims for *m* ∈ {768, 512, 256, 128, 64, 32} are themselves valid
sentence representations — you can slice the embedding to trade accuracy for
storage/latency without retraining.

- **Training data:** KorNLI
- **Base model:** [klue/roberta-base](https://huggingface.co/klue/roberta-base)
- **Nested dims:** 768, 512, 256, 128, 64, 32

## KorSTS test set results

All values are reported as percentages (×100).

| dim | cosine_pearson | cosine_spearman | euclidean_pearson | euclidean_spearman | manhattan_pearson | manhattan_spearman | dot_pearson | dot_spearman |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 768 | 83.10 | 84.07 | 83.57 | 83.79 | 83.61 | 83.81 | 80.93 | 80.17 |
| 512 | 82.87 | 83.99 | 83.44 | 83.72 | 83.51 | 83.79 | 80.37 | 79.61 |
| 256 | 82.40 | 83.63 | 82.97 | 83.36 | 83.07 | 83.45 | 77.91 | 76.52 |
| 128 | 81.50 | 83.12 | 82.15 | 82.67 | 82.17 | 82.69 | 73.90 | 72.23 |
| 64 | 80.66 | 82.87 | 80.93 | 81.58 | 80.78 | 81.52 | 68.43 | 67.40 |
| 32 | 78.32 | 81.10 | 78.80 | 79.58 | 78.49 | 79.41 | 61.02 | 59.85 |

## Usage

### Full 768-dim embedding

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("jhgan/ko-sroberta-nli-mrl")
embeddings = model.encode(["안녕하세요", "반갑습니다"])
print(embeddings.shape)  # (2, 768)
```

### Truncated embedding (recommended pattern)

```python
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("jhgan/ko-sroberta-nli-mrl")
emb = model.encode(["안녕하세요", "반갑습니다"], convert_to_tensor=True)

# Slice to the first 64 dims and re-normalise for cosine similarity
emb_64 = F.normalize(emb[:, :64], p=2, dim=1)
```

Or fix the truncation at load time
(requires `sentence-transformers >= 2.7.0`):

```python
model = SentenceTransformer("jhgan/ko-sroberta-nli-mrl", truncate_dim=64)
```

## Citation

```bibtex
@inproceedings{kusupati2022matryoshka,
    title     = {Matryoshka Representation Learning},
    author    = {Kusupati, Aditya and Bhatt, Gantavya and Rege, Aniket and
                 Wallingford, Matthew and Sinha, Aditya and Ramanujan, Vivek and
                 Howard-Snyder, William and Chen, Kaifeng and Kakade, Sham and
                 Jain, Prateek and Farhadi, Ali},
    booktitle = {Advances in Neural Information Processing Systems},
    year      = {2022},
    url       = {https://arxiv.org/abs/2205.13147}
}
```

This model is part of the
[ko-sentence-transformers](https://github.com/jhgan00/ko-sentence-transformers)
project; see the repository for training scripts and the non-MRL baselines
(`jhgan/ko-sroberta-sts`, `jhgan/ko-sroberta-nli`, `jhgan/ko-sroberta-multitask`).
