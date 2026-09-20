---
base_model: microsoft/harrier-oss-v1-0.6b
language:
  - multilingual
  - af
  - am
  - ar
  - as
  - az
  - be
  - bg
  - bn
  - br
  - bs
  - ca
  - cs
  - cy
  - da
  - de
  - el
  - en
  - eo
  - es
  - et
  - eu
  - fa
  - fi
  - fr
  - fy
  - ga
  - gd
  - gl
  - gu
  - ha
  - he
  - hi
  - hr
  - hu
  - hy
  - id
  - is
  - it
  - ja
  - jv
  - ka
  - kk
  - km
  - kn
  - ko
  - ku
  - ky
  - la
  - lo
  - lt
  - lv
  - mg
  - mk
  - ml
  - mn
  - mr
  - ms
  - my
  - ne
  - nl
  - 'no'
  - om
  - or
  - pa
  - pl
  - ps
  - pt
  - ro
  - ru
  - sa
  - sd
  - si
  - sk
  - sl
  - so
  - sq
  - sr
  - su
  - sv
  - sw
  - ta
  - te
  - th
  - tl
  - tr
  - ug
  - uk
  - ur
  - uz
  - vi
  - xh
  - yi
  - zh
license: mit
pipeline_tag: feature-extraction
library_name: furiosa-llm
tags:
  - furiosa-ai
  - harrier-oss-v1
  - qwen3
  - mteb
  - sentence-transformers
  - transformers
---
# harrier-oss-v1-0.6b

This repository contains [`microsoft/harrier-oss-v1-0.6b`](https://huggingface.co/microsoft/harrier-oss-v1-0.6b)
together with a Furiosa Executable Bundle (FXB) for running it on
[FuriosaAI RNGD](https://furiosa.ai) with [Furiosa-LLM](https://developer.furiosa.ai/latest/en/furiosa_llm/intro.html).
The same model also runs on other frameworks (such as Sentence Transformers and
Transformers); for usage with those, see the upstream
[`microsoft/harrier-oss-v1-0.6b`](https://huggingface.co/microsoft/harrier-oss-v1-0.6b) model card.

## Overview

Harrier OSS v1 is a family of multilingual text-embedding models developed by
Microsoft. The 0.6B model uses a dense, decoder-only Qwen3 architecture, but it
is trained with Harrier's own multilingual, instruction-aware embedding recipe
rather than the Qwen3-Embedding training recipe. It produces 1,024-dimensional
embeddings through last-token pooling and L2 normalization. It is designed for
retrieval, clustering, semantic similarity, classification, bitext mining, and
reranking. Its intended use is the same as the upstream
[`microsoft/harrier-oss-v1-0.6b`](https://huggingface.co/microsoft/harrier-oss-v1-0.6b),
and it is released under the [MIT License](https://opensource.org/license/mit).

- **Architecture:** Qwen3 (dense), `Qwen3Model`
- **Input / Output:** Text / Embeddings (vector)
- **Supported Inference Engine:** Furiosa LLM
- **Supported Hardware:** FuriosaAI RNGD

### Quantization

No quantization — the model runs in its native BF16 precision.

### Parallelism Strategy

On RNGD, harrier-oss-v1-0.6b runs with a **tensor-parallel size of 8 PEs**, which
maps to a **single RNGD card** (8 PEs per card).

## Usage

To run this model with Furiosa-LLM, follow the examples below after
[installing Furiosa-LLM and its prerequisites](https://developer.furiosa.ai/latest/en/get_started/furiosa_llm.html#installing-furiosa-llm).
You can use the model either online through the OpenAI-compatible server or
offline through the Furiosa-LLM Python API.

### Launch the server

Serve the model by passing its `furiosa-ai/<repo>` identifier:

```sh
# Launch the server, listening on port 8000 by default
furiosa-llm serve furiosa-ai/harrier-oss-v1-0.6b
```

When the server is ready, you will see:

```sh
INFO:     Started server process [27507]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### Basic Usage

The server exposes an OpenAI-compatible `/v1/embeddings` endpoint. Harrier is
instruction-aware: prepend a one-sentence task description to each query in the
`Instruct: ...\nQuery: ...` format, and do not add the instruction to documents.
For more details, see the
[base model card](https://huggingface.co/microsoft/harrier-oss-v1-0.6b).
Request embeddings with `curl`:

```sh
curl http://localhost:8000/v1/embeddings \
    -H "Content-Type: application/json" \
    -d '{
    "model": "furiosa-ai/harrier-oss-v1-0.6b",
    "input": [
      "Instruct: Given a web search query, retrieve relevant passages that answer the query\nQuery: summit define",
      "Definition of summit: the highest point of a mountain."
    ]
    }' \
    | python -m json.tool
```

Because the endpoint is OpenAI-compatible, you can also use the OpenAI Python
client:

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")

query = (
    "Instruct: Given a web search query, retrieve relevant passages that answer the query\n"
    "Query: summit define"
)
document = "Definition of summit: the highest point of a mountain."

response = client.embeddings.create(
    model="furiosa-ai/harrier-oss-v1-0.6b",
    input=[query, document],
)

for data in response.data:
    print(f"Index {data.index}: {len(data.embedding)} dimensions")
```

### Advanced Usage

For offline use, load the model with the `LLM` constructor (the FXB shipped in
the repo is discovered automatically) and call `embed` to obtain L2-normalized
dense vectors. Their dot product is therefore the cosine similarity:

```python
from furiosa_llm import LLM

query = (
    "Instruct: Given a web search query, retrieve relevant passages that answer the query\n"
    "Query: summit define"
)
document = "Definition of summit: the highest point of a mountain."

with LLM("furiosa-ai/harrier-oss-v1-0.6b") as llm:
    outputs = llm.embed([query, document])
    embeddings = [output.outputs.embedding for output in outputs]

similarity = sum(a * b for a, b in zip(*embeddings, strict=True))
print(f"Cosine similarity: {similarity:.4f}")
```

## Learn more

* [Furiosa-LLM Server (`furiosa-llm serve`)](https://developer.furiosa.ai/latest/en/furiosa_llm/furiosa-llm-serve.html) — full OpenAI-compatible API reference, including the Embeddings API
* [Furiosa-LLM](https://developer.furiosa.ai/latest/en/furiosa_llm/intro.html) — Furiosa-LLM documentation and API reference
* [`microsoft/harrier-oss-v1-0.6b`](https://huggingface.co/microsoft/harrier-oss-v1-0.6b) — upstream model card
