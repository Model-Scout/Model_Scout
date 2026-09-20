---
language: [multilingual, en, id, fr, es, de, pt, it, nl, ja, zh, ko, ar, ru, vi, th, tr, pl, uk, sv, fa, he, hi]
license: apache-2.0
library_name: llama.cpp
pipeline_tag: feature-extraction
tags: [gguf, embeddings, sentence-similarity, semantic-search, retrieval, multilingual, qwen3]
base_model: [ukung/semantic-lite]
---

# semantic-lite GGUF

**A compact, multilingual embedding model for fast local semantic search.**

This repository provides production-ready GGUF releases of [`ukung/semantic-lite`](https://huggingface.co/ukung/semantic-lite), built on a pruned Qwen3 architecture. It brings high-quality semantic understanding to local applications without requiring a large GPU or a hosted API.

Use it for semantic search, retrieval-augmented generation (RAG), similarity scoring, clustering, duplicate detection, recommendations, and multilingual knowledge bases powered by `llama.cpp`.

> This is an **embedding model**, not a chat or text-generation model. Use an embedding-capable runtime and compare vectors with cosine similarity or another distance metric.

## Available Files

| File | Quantization | Size | Best for |
| --- | --- | ---: | --- |
| `semantic-lite-f16.gguf` | F16 | 483 MB | Highest fidelity and reference use |
| `semantic-lite-q8.gguf` | Q8_0 | 259 MB | Near-F16 quality with lower memory use |
| `semantic-lite-q4.gguf` | Q4_K_M | 181 MB | Smallest footprint and CPU-friendly deployment |

All variants produce 1,024-dimensional embeddings and preserve the model's mean-pooling configuration.

## Why semantic-lite?

- **Multilingual by design:** built on Qwen3's broad 100+ language coverage, including English, Indonesian, Spanish, French, German, Portuguese, Italian, Dutch, Japanese, Chinese, Korean, Arabic, Russian, Vietnamese, Thai, Turkish, Polish, Ukrainian, Swedish, Persian, Hebrew, and Hindi.
- **Small and deployable:** only six transformer layers, with a Q4_K_M build of about 181 MB for practical CPU and edge deployment.
- **Rich semantic representations:** 1,024-dimensional embeddings with mean pooling for retrieval and similarity workflows.
- **Private by default:** run locally with no per-request API cost and no document data leaving your infrastructure.
- **Runtime-ready:** works with modern `llama.cpp` embedding tools and servers.
- **Flexible precision:** choose Q4 for efficiency, Q8 for a quality-focused quantized build, or F16 as the reference release.

## Benchmark Highlights

On our multilingual retrieval evaluation set, semantic-lite Q4 achieved:

| Scenario | Recall@1 |
| --- | ---: |
| 10-language multilingual retrieval | **90% overall** |
| English, French, Portuguese, Italian, and Arabic retrieval | **100%** |

The model also achieved **100% pair accuracy** on the tested semantic-similarity pairs. These results demonstrate strong multilingual retrieval across English, Indonesian, Spanish, French, German, Portuguese, Italian, Japanese, Chinese, and Arabic, while keeping the model small enough for local deployment.

### Languages Showcased

English · Indonesian · Spanish · French · German · Portuguese · Italian · Japanese · Chinese · Arabic

> Benchmark results are measured with the Q4_K_M GGUF release on a small task-focused evaluation set. Treat them as an indicative deployment signal and validate with your own domain data.

## Quick Start with llama.cpp

Build or install a recent version of [`llama.cpp`](https://github.com/ggml-org/llama.cpp), then run:

```bash
./llama-embedding \
	-m semantic-lite-q4.gguf \
	-p "Cara membuat nasi goreng" \
	--embd-output-format json
```

The command returns a JSON object containing an embedding vector with 1,024 values. Replace `semantic-lite-q4.gguf` with the Q8 or F16 file when you need higher numerical fidelity.

For a local HTTP service, use a recent `llama-server` build with embedding mode enabled:

```bash
./llama-server \
	-m semantic-lite-q4.gguf \
	--embedding \
	--host 127.0.0.1 \
	--port 8080
```

Then request an embedding:

```bash
curl http://127.0.0.1:8080/embeddings \
	-H "Content-Type: application/json" \
	-d '{"content":"Cara membuat nasi goreng"}'
```

The exact server flags and endpoint format can vary by `llama.cpp` version. Run `./llama-server --help` for the version you installed.

## Python Example

The GGUF files are intended for GGUF-compatible runtimes. One simple approach is to call `llama.cpp` from Python and parse its JSON output:

```python
import json
import subprocess


def embed(text: str, model: str = "semantic-lite-q4.gguf") -> list[float]:
	result = subprocess.run(
		[
			"llama-embedding",
			"-m", model,
			"-p", text,
			"--embd-output-format", "json",
		],
		check=True,
		capture_output=True,
		text=True,
	)
	return json.loads(result.stdout)["data"][0]["embedding"]


query_vector = embed("Easy home cooking recipes")
print(len(query_vector))  # 1024
```

For production applications, keep the model loaded in a server process instead of launching a new process for every text.

## Semantic Search

Create embeddings for documents once, normalize them, and compare a normalized query vector with a dot product. For normalized vectors, the dot product equals cosine similarity:

```python
import numpy as np

documents = [
	"How to cook fried rice",
	"Guide to stock market investing",
	"Tips for caring for your cat",
]

document_vectors = np.array([embed(document) for document in documents])
document_vectors /= np.linalg.norm(document_vectors, axis=1, keepdims=True)

query = np.array(embed("Easy home cooking recipes"))
query /= np.linalg.norm(query)

scores = document_vectors @ query
best_index = int(np.argmax(scores))
print(documents[best_index])
```

## Choosing a Variant

- Choose **Q4_K_M** for the lowest memory use and fast local CPU inference.
- Choose **Q8_0** when retrieval quality is more important and additional memory is available.
- Choose **F16** as the high-fidelity reference for evaluation or quality-sensitive workloads.

Quantization can slightly change similarity scores. When comparing benchmark results, use the same GGUF variant consistently for both indexing and querying.

## Limitations and Compatibility

- This repository contains GGUF exports of the upstream model, not a new training checkpoint.
- Use the same preprocessing, normalization, and pooling behavior for documents and queries.
- The model is intended for embeddings, not text generation.
- Runtime support depends on using a recent `llama.cpp` version with Qwen3 embedding support.
- The upstream model card documents multilingual coverage and recommended retrieval prompts such as `query: ` and `passage: ` where appropriate.

## License

The upstream model is released under the Apache-2.0 license. See the [upstream model card](https://huggingface.co/ukung/semantic-lite) for the original model details and license information.
