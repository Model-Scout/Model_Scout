---
library_name: sentence-transformers
pipeline_tag: sentence-similarity
license: other
license_name: kanana-open-license
license_link: https://huggingface.co/kakaocorp/kanana-2-3b-embedding/blob/main/LICENSE
tags:
  - sentence-transformers
  - feature-extraction
  - mteb
  - matryoshka
  - custom_code
language:
  - ko
  - en
---

<p align="center">
    <img src="./assets/logo/kanana.png" width="60%" alt="Kanana">
</p>

<p align="center">
    🤗 <a href="https://huggingface.co/kakaocorp/kanana-2-3b-embedding">kanana-2-3b-embedding</a> &nbsp;|&nbsp; 🤗 <a href="https://huggingface.co/kakaocorp/kanana-2-1.3b-embedding">kanana-2-1.3b-embedding</a> &nbsp;|&nbsp; 📕 <a href="https://tech.kakao.com/posts/826">Blog</a>
</p>

# kanana-2-3b-embedding

## News 🔥

- `2026/10/29`: 🤗 Released the kanana-2-3b-embedding and kanana-2-1.3b-embedding model weights.
- `2026/07/28`: 📕 Published a blog post about the development of the Kanana-2 SLM series.

## Introduction

Kanana-2-embedding is Kakao's text embedding model series for Korean and English retrieval.
This release includes 3B and 1.3B models.
The models are built on Kakao's Kanana-2 SLMs, converted to bidirectional attention with mean pooling.
They produce text embeddings for semantic search, retrieval-augmented generation (RAG), and text similarity.

## Highlights

- **Korean retrieval:** kanana-2-3b-embedding achieves the best average score on nano-BEIR (ko) and Ko-Retrieval among the compared models at every Matryoshka dimension.
- **Matryoshka representation learning (MRL):** Embeddings can be truncated to 1024 / 512 / 256 / 128 dimensions to reduce storage and search cost.
- **Long input:** The models accept inputs of up to 4,096 tokens.

## Model Downloads

| Model | Embedding dim | Download |
| --- | --- | --- |
| kanana-2-3b-embedding | 2560 | [🤗 HuggingFace](https://huggingface.co/kakaocorp/kanana-2-3b-embedding) |
| kanana-2-1.3b-embedding | 1280 | [🤗 HuggingFace](https://huggingface.co/kakaocorp/kanana-2-1.3b-embedding) |

## Embedding Performance

All models are evaluated with [MTEB](https://github.com/embeddings-benchmark/mteb) under the same conditions.
Every evaluation runs **without any task prompt** (raw input text, with no query/document prefix or instruction template).
Each cell is the average score of the benchmark, reported per Matryoshka dimension (`full` / `512` / `256` / `128`).

<!-- prettier-ignore -->
<table>
  <thead>
    <tr>
      <th rowspan="2">Model</th>
      <th colspan="4">nano-BEIR (en)</th>
      <th colspan="4">nano-BEIR (ko)</th>
      <th colspan="4">MTEB (eng, v2)</th>
      <th colspan="4">Ko-Retrieval<sup>†</sup></th>
    </tr>
    <tr>
      <th>full</th><th>512</th><th>256</th><th>128</th>
      <th>full</th><th>512</th><th>256</th><th>128</th>
      <th>full</th><th>512</th><th>256</th><th>128</th>
      <th>full</th><th>512</th><th>256</th><th>128</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>embeddinggemma-300m</td>
      <td>0.5330</td><td>0.5059</td><td>0.4813</td><td>0.4379</td>
      <td>0.4564</td><td>0.4423</td><td>0.4163</td><td>0.3764</td>
      <td>0.6247</td><td>0.6155</td><td>0.6097</td><td>0.5894</td>
      <td>0.7295</td><td>0.7172</td><td>0.6992</td><td>0.6397</td>
    </tr>
    <tr>
      <td>llama-nemotron-embed-1b-v2</td>
      <td>0.6466</td><td>0.6259</td><td>0.5961</td><td>0.5386</td>
      <td>0.5471</td><td>0.5204</td><td>0.4818</td><td>0.4225</td>
      <td>0.6369</td><td>0.6222</td><td>0.6055</td><td>0.5752</td>
      <td>0.7985</td><td>0.7787</td><td>0.7506</td><td>0.6780</td>
    </tr>
    <tr>
      <td>Qwen3-Embedding-0.6B</td>
      <td>0.5822</td><td>0.5722</td><td>0.5472</td><td>0.5316</td>
      <td>0.4845</td><td>0.4712</td><td>0.4494</td><td>0.4256</td>
      <td>0.6311</td><td>0.6268</td><td>0.6160</td><td>0.6013</td>
      <td>0.7279</td><td>0.7126</td><td>0.6825</td><td>0.6365</td>
    </tr>
    <tr>
      <td>Qwen3-Embedding-4B</td>
      <td>0.6379</td><td>0.6187</td><td>0.5910</td><td>0.5449</td>
      <td>0.5522</td><td>0.5177</td><td>0.4912</td><td>0.4515</td>
      <td><strong>0.6661</strong></td><td><strong>0.6606</strong></td><td><strong>0.6470</strong></td><td><strong>0.6284</strong></td>
      <td>0.7837</td><td>0.7617</td><td>0.7266</td><td>0.6854</td>
    </tr>
    <tr>
      <td>kanana-nano-2.1b-embedding-v1.0.0<sup>‡</sup></td>
      <td>0.5285</td><td>—</td><td>—</td><td>—</td>
      <td>0.4948</td><td>—</td><td>—</td><td>—</td>
      <td>0.6028</td><td>—</td><td>—</td><td>—</td>
      <td>0.7579</td><td>—</td><td>—</td><td>—</td>
    </tr>
    <tr>
      <td>kanana-essence-8b-embedding-v1.0.0<sup>‡</sup></td>
      <td>0.6013</td><td>—</td><td>—</td><td>—</td>
      <td>0.5518</td><td>—</td><td>—</td><td>—</td>
      <td>0.6444</td><td>—</td><td>—</td><td>—</td>
      <td>0.7896</td><td>—</td><td>—</td><td>—</td>
    </tr>
    <tr>
      <td><strong>kanana-2-1.3b-embedding</strong></td>
      <td>0.6332</td><td>0.6257</td><td>0.6078</td><td>0.5603</td>
      <td>0.5866</td><td>0.5812</td><td>0.5610</td><td>0.5164</td>
      <td>0.6197</td><td>0.6037</td><td>0.5879</td><td>0.5572</td>
      <td>0.7958</td><td>0.7891</td><td>0.7706</td><td>0.7211</td>
    </tr>
    <tr>
      <td><strong>kanana-2-3b-embedding</strong></td>
      <td><strong>0.6552</strong></td><td><strong>0.6327</strong></td><td><strong>0.6170</strong></td><td><strong>0.5899</strong></td>
      <td><strong>0.6088</strong></td><td><strong>0.5943</strong></td><td><strong>0.5683</strong></td><td><strong>0.5206</strong></td>
      <td>0.6317</td><td>0.6203</td><td>0.6057</td><td>0.5760</td>
      <td><strong>0.8211</strong></td><td><strong>0.8066</strong></td><td><strong>0.7873</strong></td><td><strong>0.7488</strong></td>
    </tr>
  </tbody>
</table>

Per-column best scores are **bolded**.

† Average over six Korean retrieval tasks: `MIRACLRetrieval`, `Ko-StrategyQA`, `AutoRAGRetrieval`, `LawIRKo`, `SQuADKorV1Retrieval`, and `PublicHealthQA`.

‡ Kanana-1 embedding models do not support Matryoshka truncation, so only the full-dim score is reported.

Library versions used for evaluation: `transformers==5.8.0`, `sentence-transformers==5.5.1`, `vllm==0.20.2`, `torch==2.11.0+cu129`.

## Deployment

The model supports Matryoshka truncation to **1024 / 512 / 256 / 128** dimensions.

### sentence-transformers

```bash
pip install torch sentence-transformers
```

```python
from sentence_transformers import SentenceTransformer

model_id = "kakaocorp/kanana-2-3b-embedding"
model = SentenceTransformer(model_id, trust_remote_code=True)

queries = ["What is the capital of France?"]
documents = ["Paris is the capital of France."]

q = model.encode(queries)
d = model.encode(documents)
scores = model.similarity(q, d)
print(scores)
```

With MRL truncation:

```python
DIM = 256  # one of: 1024, 512, 256, 128

model = SentenceTransformer(model_id, trust_remote_code=True, truncate_dim=DIM)
embeddings = model.encode(["query text", "document text"])
```

### transformers

```bash
pip install torch transformers
```

```python
import torch
import torch.nn.functional as F
from transformers import AutoModel, AutoTokenizer

model_id = "kakaocorp/kanana-2-3b-embedding"

tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModel.from_pretrained(
    model_id,
    trust_remote_code=True,
    dtype=torch.bfloat16,
).cuda().eval()

texts = ["query text", "document text"]
inputs = tokenizer(
    texts,
    padding=True,
    truncation=True,
    return_tensors="pt",
    max_length=4096,
).to("cuda")

with torch.no_grad():
    out = model(**inputs)

hidden = out.last_hidden_state
mask = inputs["attention_mask"].unsqueeze(-1).float()
pooled = (hidden * mask).sum(dim=1) / mask.sum(dim=1)
embeddings = F.normalize(pooled, dim=-1)
```

With MRL truncation:

```python
DIM = 256  # one of: 1024, 512, 256, 128
embeddings = F.normalize(pooled[:, :DIM], dim=-1)
```

### vLLM

```bash
pip install vllm
```

```python
import numpy as np
from vllm import LLM

model_id = "kakaocorp/kanana-2-3b-embedding"

llm = LLM(
    model=model_id,
    runner="pooling",
    convert="embed",
    trust_remote_code=True,
    enable_prefix_caching=False,
    enable_chunked_prefill=False,
)

outputs = llm.embed(["query text", "document text"])
raw = np.asarray([o.outputs.embedding for o in outputs])
embeddings = raw / np.linalg.norm(raw, axis=-1, keepdims=True)
```

With MRL truncation:

```python
DIM = 256  # one of: 1024, 512, 256, 128
trunc = raw[:, :DIM]
embeddings = trunc / np.linalg.norm(trunc, axis=-1, keepdims=True)
```

## License

The model weights are released under the [KananaOpenLicense](https://huggingface.co/kakaocorp/kanana-2-3b-embedding/blob/main/LICENSE).

## Citation

```bibtex
@misc{kanana2embedding2026,
  title = {{kanana-2-embedding}},
  author = {Doohae Jung},
  year = {2026},
  url = {https://huggingface.co/collections/kakaocorp/kanana-2-slm}
}
```

## Contact

- Kanana LLM Team Technical Support: [kanana-llm@kakaocorp.com](mailto:kanana-llm@kakaocorp.com)
- Business & Partnership Contact: [alpha.k@kakaocorp.com](mailto:alpha.k@kakaocorp.com)
