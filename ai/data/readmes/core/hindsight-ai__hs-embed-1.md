---
license: mit
base_model: hotchpotch/bekko-embedding-v1-a25m
base_model_relation: finetune
library_name: sentence-transformers
pipeline_tag: sentence-similarity
language:
- en
- es
- fr
- de
- pt
- ja
- ko
- zh
tags:
- sentence-transformers
- feature-extraction
- embeddings
- matryoshka
- multilingual
- onnx
- text-embeddings-inference
- hindsight
---

![Hindsight](assets/banner.png)

# hs-embed-1

hs-embed-1 is a multilingual text embedding model built for [Hindsight](https://github.com/vectorize-io/hindsight).

## Highlights

- **Multilingual:** English, Spanish, French, German, Portuguese, Japanese, Korean and Chinese
  (Simplified and Traditional).
- **Variable dimensions:** 384-dimensional vectors that can be truncated to 256, 128 or 64.
- **Long inputs:** up to 8,192 tokens.
- **Small:** 112M parameters. 98M of them are the token embedding table, so each forward pass
  runs a 13M-parameter transformer.
- **No prompts:** queries and documents are encoded the same way, with no prefix.
- **CPU and GPU:** ships an int8 ONNX export for CPU, and safetensors for GPU.
- **Serves on TEI:** CPU and GPU images.

## Model overview

| | |
|---|---|
| Model type | Text embedding (bi-encoder) |
| Base model | `hotchpotch/bekko-embedding-v1-a25m` |
| Parameters | 112M |
| Languages | en, es, fr, de, pt, ja, ko, zh |
| Context length | 8,192 tokens |
| Embedding dimensions | 384 (truncatable to 256, 128, 64) |
| Pooling | Mean |
| Similarity | Cosine |
| Formats | safetensors stored in FP16 (FP32 copy on the `fp32` branch), ONNX (`onnx/model.onnx`, int8 vocabulary table) |

## Evaluation

![hs-embed-1 benchmarks](assets/benchmarks.png)

### Serving on CPU

![hs-embed-1 CPU serving](assets/serving-cpu.png)

## Usage

### Sentence Transformers

```bash
pip install -U sentence-transformers
```

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("hindsight-ai/hs-embed-1")

queries = ["Where did Maya move last spring?"]
documents = [
    "Maya moved to Lisbon in April.",
    "Maya's brother lives in Porto.",
]

query_embeddings = model.encode(queries, normalize_embeddings=True)
document_embeddings = model.encode(documents, normalize_embeddings=True)

print(model.similarity(query_embeddings, document_embeddings))
```

For shorter vectors, load the model with `truncate_dim`:

```python
model = SentenceTransformer("hindsight-ai/hs-embed-1", truncate_dim=256)
```

### Text Embeddings Inference

CPU (uses `onnx/model.onnx`):

```bash
docker run -p 8080:80 \
  ghcr.io/huggingface/text-embeddings-inference:cpu-1.9.3 \
  --model-id hindsight-ai/hs-embed-1 --auto-truncate
```

GPU:

```bash
docker run --gpus all -p 8080:80 \
  ghcr.io/huggingface/text-embeddings-inference:89-1.9.3 \
  --model-id hindsight-ai/hs-embed-1 --auto-truncate
```

Use the GPU image tag for your GPU: `89-1.9.3` for L4 and other Ada GPUs, `1.9.3` for A100
and H100.

```bash
curl 127.0.0.1:8080/embed \
  -H 'Content-Type: application/json' \
  -d '{"inputs": ["Where did Maya move last spring?", "Maya moved to Lisbon in April."]}'
```

To use fewer dimensions, keep the first 256, 128 or 64 values of each vector and normalize
again.

### Hindsight

```bash
HINDSIGHT_API_EMBEDDINGS_PROVIDER=local
HINDSIGHT_API_EMBEDDINGS_LOCAL_MODEL=hindsight-ai/hs-embed-1
```

Or point Hindsight at a TEI server:

```bash
HINDSIGHT_API_EMBEDDINGS_PROVIDER=tei
HINDSIGHT_API_EMBEDDINGS_TEI_URL=http://localhost:8080
```

### Hindsight Inference

hs-embed-1 is also served at `https://inference.hindsight.vectorize.io`. To use it from
Hindsight:

```bash
HINDSIGHT_API_EMBEDDINGS_PROVIDER=hindsight
HINDSIGHT_API_EMBEDDINGS_HINDSIGHT_API_KEY=<your Hindsight Inference API key>
```

## License

MIT

## Citation

```bibtex
@misc{hindsightai2026hsembed1,
  title  = {hs-embed-1},
  author = {{Hindsight AI}},
  year   = {2026},
  url    = {https://huggingface.co/hindsight-ai/hs-embed-1}
}
```
