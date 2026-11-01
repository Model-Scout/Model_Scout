---
license: openmdw-1.1
base_model: nvidia/Nemotron-3-Embed-1B-BF16
base_model_relation: quantized
library_name: gguf
pipeline_tag: sentence-similarity
language:
  - multilingual
  - en
  - ar
  - as
  - bn
  - bg
  - zh
  - da
  - nl
  - fi
  - fr
  - de
  - hi
  - id
  - it
  - ja
  - ko
  - ms
  - mr
  - ne
  - "no"
  - fa
  - pt
  - ro
  - ru
  - es
  - sw
  - sv
  - ta
  - te
  - th
  - uk
  - ur
  - vi
tags:
  - gguf
  - Q4_K_M
  - text-embeddings
  - feature-extraction
  - retrieval
  - semantic-search
  - rag
  - lm-studio
  - llama-cpp
  - arxiv:2407.14679
  - arxiv:2502.13595
---

# Nemotron-3-Embed-1B Q4_K_M GGUF

An independently converted and quantized GGUF of NVIDIA's
[`nvidia/Nemotron-3-Embed-1B-BF16`](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16),
prepared for local embedding inference in LM Studio and llama.cpp-compatible runtimes.

This repository is not an official NVIDIA release and is not affiliated with or endorsed by NVIDIA.

## File

| File | Quantization | Size | SHA-256 |
|---|---:|---:|---|
| `nemotron-3-embed-1b-q4_k_m.gguf` | Q4_K_M | 749,352,096 bytes (714.6 MiB) | `9a74166f51dbc280073748fa199bea49283bd21f7f9280f2dec2b4d975ddfd1d` |

The model produces 2,048-dimensional, L2-normalized embeddings. Its GGUF metadata declares a
262,144-token maximum context. The release was functionally tested at a 4,096-token context; very
large contexts were not validated and require substantially more memory.

## Use with LM Studio

Download the GGUF from **Files and versions**, then drag it into LM Studio or place it in LM Studio's
models directory. LM Studio should classify it as an embedding model.

Load it with a 4,096-token context and full GPU offload, start the local server, and call the
OpenAI-compatible embeddings endpoint:

```bash
curl http://127.0.0.1:1234/v1/embeddings \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "nemotron-3-embed-1b-q4",
    "input": [
      "query: What is retrieval-augmented generation?",
      "passage: Retrieval-augmented generation adds retrieved documents to a model prompt."
    ]
  }'
```

The exact model identifier can differ if LM Studio assigns another load name; check
`http://127.0.0.1:1234/v1/models` when needed.

## Retrieval format

Use the prefixes specified by NVIDIA:

- Queries: `query: <text>`
- Documents: `passage: <text>`

Embeddings are normalized, so cosine similarity and dot product give equivalent rankings (within
normal floating-point tolerance).

## Conversion provenance

- Upstream repository: [`nvidia/Nemotron-3-Embed-1B-BF16`](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16)
- Exact upstream revision: [`0677b2025cbc37daf92d7b9c7a225de8cfbc5b0b`](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16/commit/0677b2025cbc37daf92d7b9c7a225de8cfbc5b0b)
- Conversion and quantization: [`llama.cpp`](https://github.com/ggml-org/llama.cpp) build `b10015`, commit [`12127defda4f41b7679cb2477a4b0d65ee6a0c8f`](https://github.com/ggml-org/llama.cpp/commit/12127defda4f41b7679cb2477a4b0d65ee6a0c8f)
- Conversion path: upstream BF16 Safetensors → F16 GGUF → Q4_K_M GGUF
- Importance matrix: none
- Output GGUF version: 3
- Quantization version: 2

The conversion was mechanical. The model was not fine-tuned or otherwise trained. See
[`QUANTIZATION.md`](QUANTIZATION.md) for the reproducibility record and embedded metadata summary.

## Validation

Validated on an Apple M3 Max with LM Studio 0.4.19 Build 2 and its llama.cpp runtime 2.25.2, using
full GPU offload and a 4,096-token context.

| Check | Result |
|---|---:|
| Output dimensions | 2,048 |
| L2 norm (three test vectors) | 1.00000002 / 1.00000001 / 0.99999997 |
| Relevant query/passage cosine | 0.654999 |
| Unrelated query/passage cosine | 0.044103 |
| Median latency, one input | 30.46 ms |
| Median batch time, 32 inputs | 974.98 ms |
| Median batch throughput | 32.82 texts/s |

Latency includes local HTTP and JSON serialization. These numbers are a runtime smoke test, not a
retrieval-quality evaluation. Hardware, text length, context settings, and runtime versions affect
performance.

## Limitations

- Q4_K_M is lossy and can change retrieval scores or rankings relative to the upstream BF16 model.
- No MTEB/MMTEB accuracy evaluation was run on this quantization; consult NVIDIA's upstream model
  card for BF16 benchmark results.
- This model is intended for embeddings, retrieval, semantic search, and reranking pipelines. It is
  not a chat or text-generation model.
- Users remain responsible for evaluating model behavior, data handling, and suitability for their
  application.

## License and attribution

The model materials are distributed under the
[OpenMDW License Agreement 1.1](https://openmdw.ai/license/1-1/). The upstream model incorporates
Ministral-3-3B-Instruct-2512 materials released under Apache 2.0.

This repository retains NVIDIA's [`LICENSE`](LICENSE), [`NOTICE`](NOTICE), and
[`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md). By using or distributing the model, you agree to
the applicable license terms. NVIDIA retains ownership of its names and trademarks; their use here
is solely to identify the upstream model.

## Upstream resources

- [NVIDIA upstream model card](https://huggingface.co/nvidia/Nemotron-3-Embed-1B-BF16)
- [NVIDIA Nemotron-3-Embed blog post](https://huggingface.co/blog/nvidia/nemotron-3-embed-wins-rteb)
- [Compact Language Models via Pruning and Knowledge Distillation](https://arxiv.org/abs/2407.14679)
- [MMTEB: Massive Multilingual Text Embedding Benchmark](https://arxiv.org/abs/2502.13595)
