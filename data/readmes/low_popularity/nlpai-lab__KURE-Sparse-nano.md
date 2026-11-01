---
tags:
- sentence-transformers
- sparse-encoder
- sparse
- splade
- learned-sparse-retrieval
- feature-extraction
language:
- ko
- en
base_model: nlpai-lab/KURE-v2-unsupervised
pipeline_tag: feature-extraction
library_name: sentence-transformers
license: apache-2.0
---

<a href="https://github.com/nlpai-lab/KURE">
  <img src="https://huggingface.co/nlpai-lab/KURE-v2/resolve/main/kure_logo.png" width="50%"/>
</a>


# 🔎 KURE-Sparse-nano

**KURE-Sparse-nano** is a compact (0.1B) Korean-English learned sparse retrieval model. It shows state-of-the-art performance among < 0.5B sparse models supporting Korean, averaging **0.7716** nDCG@10 on MTEB(kor, v2) Retrieval. It also outperforms much larger dense models, such as pplx-embed-v1-4b and harrier-oss-v1-27b.
It is also served through the [KURE API](https://kure.kullm.ai/).

<p align="center">
  <img src="assets/kure_ndcg.png" width="100%" alt="Average nDCG@10 on MTEB(kor, v2) Retrieval of the KURE models and baseline retrievers">
</p>

## Key Characteristics

- **Learned Sparse Retrieval (LSR)**: every vector lives in a fixed vocabulary of 36,282 terms, so documents can be indexed in
  an inverted index and matched terms are inspectable.
- **Compact**: 0.1B parameters.
- **Long documents**: up to 8,192 tokens.
- **Sparse at both ends**: on average 147 active dimensions per query and 843 per document.

## Usage

### Sentence Transformers

```bash
pip install -U sentence-transformers
```

Use `encode_query` / `encode_document`: they add the query and document markers the model was trained with.

```python
from sentence_transformers import SparseEncoder

model = SparseEncoder("nlpai-lab/KURE-Sparse-nano", trust_remote_code=True)

query = "훈민정음은 언제 만들어졌나요?"
documents = [
    "세종대왕은 1443년에 훈민정음을 창제하고 1446년에 이를 반포하였다.",
    "김치는 배추나 무를 소금에 절인 뒤 고춧가루와 젓갈을 넣어 발효시킨 음식이다.",
    "한라산은 해발 1,947m로 남한에서 가장 높은 산이며 제주도 중앙에 자리한다.",
]

query_embeddings = model.encode_query(query)
document_embeddings = model.encode_document(documents)
print(query_embeddings.shape, document_embeddings.shape)
# torch.Size([36282]) torch.Size([3, 36282])

# Dot-product scores (higher is more relevant)
scores = model.similarity(query_embeddings, document_embeddings)
print(scores)
# tensor([[119.3931,  11.5758,   6.4037]])
```

### API

KURE-Sparse-nano is served at [kure.kullm.ai](https://kure.kullm.ai/). Sign in with GitHub there to get an API key.

```python
import os

import requests

URL = "https://kure.kullm.ai/api/v1/sparse-embeddings"
HEADERS = {"Authorization": f"Bearer {os.environ['KURE_API_KEY']}"}

query = "훈민정음은 언제 만들어졌나요?"
documents = [
    "세종대왕은 1443년에 훈민정음을 창제하고 1446년에 이를 반포하였다.",
    "김치는 배추나 무를 소금에 절인 뒤 고춧가루와 젓갈을 넣어 발효시킨 음식이다.",
    "한라산은 해발 1,947m로 남한에서 가장 높은 산이며 제주도 중앙에 자리한다.",
]

# input_type adds the query or document markers. return_tokens=True also returns the term of each index
def encode(texts, input_type):
    response = requests.post(URL, headers=HEADERS, json={"model": "kure-sparse-nano", "input": texts, "input_type": input_type})
    response.raise_for_status()
    return [dict(zip(e["indices"], e["values"])) for e in response.json()["data"]]

query_embedding = encode(query, "query")[0]
document_embeddings = encode(documents, "document")

# Dot-product scores (higher is more relevant)
scores = [sum(w * doc.get(i, 0.0) for i, w in query_embedding.items()) for doc in document_embeddings]
print([round(s, 4) for s in scores])
# [117.3682, 11.7437, 6.2175]
```

## Evaluation

KURE-Sparse-nano is evaluated on the nine **MTEB(kor, v2) Retrieval** tasks. We report nDCG@10.

<div style="width: fit-content; max-width: 100%; margin: 0 auto;">
  <div style="overflow-x: auto;">
    <table cellpadding="6" style="margin: 0 auto; border-collapse: collapse; color: inherit; text-align: right; font-size: 0.85em; line-height: 1.6; font-variant-numeric: tabular-nums;">
      <thead>
        <tr style="border-bottom: 1px solid rgba(128, 128, 128, 0.35);">
          <th scope="col" style="text-align: left;">Model</th>
          <th scope="col" style="text-align: left;">Type</th>
          <th scope="col" style="text-align: left;">Params</th>
          <th scope="col">Avg</th>
          <th scope="col">AutoRAG</th>
          <th scope="col">PubHealthQA</th>
          <th scope="col">Ko-StrategyQA</th>
          <th scope="col">LawIRKo</th>
          <th scope="col">SQuADKorV1</th>
          <th scope="col">Belebele (ko-ko)</th>
          <th scope="col">MrTidy</th>
          <th scope="col">MLDR</th>
          <th scope="col">MIRACL</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th colspan="13" scope="rowgroup" style="padding: 16px 6px 6px; text-align: left; font-size: 0.8em; letter-spacing: 0.08em; text-transform: uppercase;">KURE Models</th>
        </tr>
        <tr><td style="text-align: left; white-space: nowrap;"><strong><a href="https://huggingface.co/nlpai-lab/KURE-Sparse-nano" style="color: #c9496b;">nlpai-lab/KURE-Sparse-nano</a></strong></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">Sparse</span></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">0.1B</span></td><td><strong style="color: #c9496b;">0.7716</strong></td><td><span style="color: #c9496b;">0.9360</span></td><td><span style="color: #c9496b;">0.7711</span></td><td><span style="color: #c9496b;">0.7924</span></td><td><span style="color: #c9496b;">0.7226</span></td><td><span style="color: #c9496b;">0.9774</span></td><td><span style="color: #c9496b;">0.9608</span></td><td><span style="color: #c9496b;">0.5618</span></td><td><span style="color: #c9496b;">0.5133</span></td><td><span style="color: #c9496b;">0.7091</span></td></tr>
        <tr><td style="text-align: left; white-space: nowrap;"><a href="https://huggingface.co/nlpai-lab/KURE-v3" style="color: #c9496b;">nlpai-lab/KURE-v3</a></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">Dense</span></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">1.1B</span></td><td><span style="color: #c9496b;">0.8027</span></td><td><span style="color: #c9496b;">0.9324</span></td><td><span style="color: #c9496b;">0.8639</span></td><td><span style="color: #c9496b;">0.8192</span></td><td><span style="color: #c9496b;">0.8158</span></td><td><span style="color: #c9496b;">0.9666</span></td><td><span style="color: #c9496b;">0.9673</span></td><td><span style="color: #c9496b;">0.6320</span></td><td><span style="color: #c9496b;">0.4781</span></td><td><span style="color: #c9496b;">0.7489</span></td></tr>
        <tr><td style="text-align: left; white-space: nowrap;"><a href="https://huggingface.co/nlpai-lab/KURE-v2" style="color: #c9496b;">nlpai-lab/KURE-v2</a></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">Late-interaction</span></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">0.2B</span></td><td><span style="color: #c9496b;">0.8160</span></td><td><span style="color: #c9496b;">0.9718</span></td><td><span style="color: #c9496b;">0.8228</span></td><td><span style="color: #c9496b;">0.8070</span></td><td><span style="color: #c9496b;">0.7550</span></td><td><span style="color: #c9496b;">0.9846</span></td><td><span style="color: #c9496b;">0.9660</span></td><td><span style="color: #c9496b;">0.5974</span></td><td><span style="color: #c9496b;">0.7158</span></td><td><span style="color: #c9496b;">0.7237</span></td></tr>
        <tr><td style="text-align: left; white-space: nowrap;"><a href="https://huggingface.co/nlpai-lab/KURE-Sparse-base" style="color: #c9496b;">nlpai-lab/KURE-Sparse-base</a></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">Sparse</span></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">0.6B</span></td><td><span style="color: #c9496b;">0.7984</span></td><td><span style="color: #c9496b;">0.9445</span></td><td><span style="color: #c9496b;">0.8099</span></td><td><span style="color: #c9496b;">0.8188</span></td><td><span style="color: #c9496b;">0.7244</span></td><td><span style="color: #c9496b;">0.9815</span></td><td><span style="color: #c9496b;">0.9703</span></td><td><span style="color: #c9496b;">0.6255</span></td><td><span style="color: #c9496b;">0.5716</span></td><td><span style="color: #c9496b;">0.7395</span></td></tr>
        <tr><td style="text-align: left; white-space: nowrap;"><a href="https://huggingface.co/nlpai-lab/KURE-v1" style="color: #c9496b;">nlpai-lab/KURE-v1</a></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">Dense</span></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">0.6B</span></td><td><span style="color: #c9496b;">0.7616</span></td><td><span style="color: #c9496b;">0.8708</span></td><td><span style="color: #c9496b;">0.8193</span></td><td><span style="color: #c9496b;">0.7999</span></td><td><span style="color: #c9496b;">0.7426</span></td><td><span style="color: #c9496b;">0.9357</span></td><td><span style="color: #c9496b;">0.9502</span></td><td><span style="color: #c9496b;">0.5909</span></td><td><span style="color: #c9496b;">0.4637</span></td><td><span style="color: #c9496b;">0.6816</span></td></tr>
        <tr><td style="text-align: left; white-space: nowrap;"><a href="https://huggingface.co/nlpai-lab/KoE5" style="color: #c9496b;">nlpai-lab/KoE5</a></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">Dense</span></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">0.6B</span></td><td><span style="color: #c9496b;">0.7337</span></td><td><span style="color: #c9496b;">0.8434</span></td><td><span style="color: #c9496b;">0.8351</span></td><td><span style="color: #c9496b;">0.8001</span></td><td><span style="color: #c9496b;">0.7756</span></td><td><span style="color: #c9496b;">0.8980</span></td><td><span style="color: #c9496b;">0.9425</span></td><td><span style="color: #c9496b;">0.5841</span></td><td><span style="color: #c9496b;">0.3015</span></td><td><span style="color: #c9496b;">0.6235</span></td></tr>
      </tbody>
      <tbody style="border-top: 1px solid rgba(128, 128, 128, 0.25);">
        <tr>
          <th colspan="13" scope="rowgroup" style="padding: 16px 6px 6px; text-align: left; font-size: 0.8em; letter-spacing: 0.08em; text-transform: uppercase;">Dense (Single-Vector) Models</th>
        </tr>
        <tr><td style="text-align: left; white-space: nowrap;">nvidia/Nemotron-3-Embed-8B-BF16</td><td style="text-align: left; white-space: nowrap;">Dense</td><td style="text-align: left; white-space: nowrap;">8.0B</td><td>0.8127</td><td>0.9311</td><td>0.8898</td><td>0.8405</td><td>0.8481</td><td>0.9650</td><td>0.9714</td><td>0.6540</td><td>0.4785</td><td>0.7363</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">sionic-ai/comsat-embed-ko-8b-preview</td><td style="text-align: left; white-space: nowrap;">Dense</td><td style="text-align: left; white-space: nowrap;">7.6B</td><td>0.7927</td><td>0.8518</td><td>0.8871</td><td>0.8394</td><td>0.8164</td><td>0.9168</td><td>0.9853</td><td>0.6253</td><td>0.5157</td><td>0.6964</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">Qwen/Qwen3-Embedding-8B</td><td style="text-align: left; white-space: nowrap;">Dense</td><td style="text-align: left; white-space: nowrap;">7.6B</td><td>0.7826</td><td>0.8276</td><td>0.8721</td><td>0.8363</td><td>0.8171</td><td>0.9063</td><td>0.9824</td><td>0.6187</td><td>0.5046</td><td>0.6783</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">nvidia/Nemotron-3-Embed-1B-BF16</td><td style="text-align: left; white-space: nowrap;">Dense</td><td style="text-align: left; white-space: nowrap;">1.1B</td><td>0.7817</td><td>0.9074</td><td>0.8642</td><td>0.8136</td><td>0.7758</td><td>0.9505</td><td>0.9629</td><td>0.6084</td><td>0.4202</td><td>0.7325</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">Qwen/Qwen3-Embedding-4B</td><td style="text-align: left; white-space: nowrap;">Dense</td><td style="text-align: left; white-space: nowrap;">4.0B</td><td>0.7737</td><td>0.8431</td><td>0.8693</td><td>0.8270</td><td>0.7769</td><td>0.9044</td><td>0.9522</td><td>0.6076</td><td>0.5022</td><td>0.6803</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">perplexity-ai/pplx-embed-v1-4b</td><td style="text-align: left; white-space: nowrap;">Dense</td><td style="text-align: left; white-space: nowrap;">4.0B</td><td>0.7705</td><td>0.8321</td><td>0.9042</td><td>0.8326</td><td>0.7736</td><td>0.9402</td><td>0.9624</td><td>0.5778</td><td>0.4343</td><td>0.6775</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">microsoft/harrier-oss-v1-27b</td><td style="text-align: left; white-space: nowrap;">Dense</td><td style="text-align: left; white-space: nowrap;">27.0B</td><td>0.7667</td><td>0.8176</td><td>0.8971</td><td>0.8361</td><td>0.8737</td><td>0.9204</td><td>0.9546</td><td>0.5306</td><td>0.4046</td><td>0.6653</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">dragonkue/snowflake-arctic-embed-l-v2.0-ko</td><td style="text-align: left; white-space: nowrap;">Dense</td><td style="text-align: left; white-space: nowrap;">0.6B</td><td>0.7653</td><td>0.9093</td><td>0.8337</td><td>0.8050</td><td>0.7735</td><td>0.9447</td><td>0.9518</td><td>0.5712</td><td>0.4304</td><td>0.6685</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">codefuse-ai/F2LLM-v2-8B</td><td style="text-align: left; white-space: nowrap;">Dense</td><td style="text-align: left; white-space: nowrap;">7.6B</td><td>0.7638</td><td>0.7678</td><td>0.9380</td><td>0.8371</td><td>0.8405</td><td>0.8874</td><td>0.9513</td><td>0.6162</td><td>0.4047</td><td>0.6313</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">telepix/PIXIE-Rune-v1.5</td><td style="text-align: left; white-space: nowrap;">Dense</td><td style="text-align: left; white-space: nowrap;">0.6B</td><td>0.7618</td><td>0.8927</td><td>0.8426</td><td>0.8064</td><td>0.7705</td><td>0.9457</td><td>0.9617</td><td>0.5492</td><td>0.4482</td><td>0.6393</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">nvidia/llama-nemotron-embed-1b-v2</td><td style="text-align: left; white-space: nowrap;">Dense</td><td style="text-align: left; white-space: nowrap;">1.2B</td><td>0.7564</td><td>0.8708</td><td>0.8177</td><td>0.8055</td><td>0.7329</td><td>0.9345</td><td>0.9519</td><td>0.5988</td><td>0.3952</td><td>0.7004</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">dragonkue/BGE-m3-ko</td><td style="text-align: left; white-space: nowrap;">Dense</td><td style="text-align: left; white-space: nowrap;">0.6B</td><td>0.7547</td><td>0.8738</td><td>0.8155</td><td>0.7959</td><td>0.7322</td><td>0.9414</td><td>0.9503</td><td>0.6099</td><td>0.3899</td><td>0.6833</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">BAAI/bge-m3</td><td style="text-align: left; white-space: nowrap;">Dense</td><td style="text-align: left; white-space: nowrap;">0.6B</td><td>0.7509</td><td>0.8301</td><td>0.8041</td><td>0.7941</td><td>0.7174</td><td>0.9038</td><td>0.9315</td><td>0.6471</td><td>0.4287</td><td>0.7015</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">jinaai/jina-embeddings-v5-text-small-retrieval</td><td style="text-align: left; white-space: nowrap;">Dense</td><td style="text-align: left; white-space: nowrap;">0.6B</td><td>0.7419</td><td>0.8409</td><td>0.8664</td><td>0.8096</td><td>0.7483</td><td>0.8926</td><td>0.9346</td><td>0.5779</td><td>0.3315</td><td>0.6752</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">perplexity-ai/pplx-embed-v1-0.6b</td><td style="text-align: left; white-space: nowrap;">Dense</td><td style="text-align: left; white-space: nowrap;">0.6B</td><td>0.7390</td><td>0.8414</td><td>0.8255</td><td>0.8100</td><td>0.7444</td><td>0.9174</td><td>0.9393</td><td>0.5524</td><td>0.3179</td><td>0.7026</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">google/embeddinggemma-300m</td><td style="text-align: left; white-space: nowrap;">Dense</td><td style="text-align: left; white-space: nowrap;">0.3B</td><td>0.7254</td><td>0.8187</td><td>0.8170</td><td>0.8008</td><td>0.6850</td><td>0.9114</td><td>0.9430</td><td>0.5253</td><td>0.3844</td><td>0.6434</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">Qwen/Qwen3-Embedding-0.6B</td><td style="text-align: left; white-space: nowrap;">Dense</td><td style="text-align: left; white-space: nowrap;">0.6B</td><td>0.7140</td><td>0.8338</td><td>0.8107</td><td>0.7586</td><td>0.7526</td><td>0.8490</td><td>0.9124</td><td>0.4870</td><td>0.4199</td><td>0.6023</td></tr>
      </tbody>
      <tbody style="border-top: 1px solid rgba(128, 128, 128, 0.25);">
        <tr>
          <th colspan="13" scope="rowgroup" style="padding: 16px 6px 6px; text-align: left; font-size: 0.8em; letter-spacing: 0.08em; text-transform: uppercase;">Late-interaction (Multi-Vector) Models</th>
        </tr>
        <tr><td style="text-align: left; white-space: nowrap;">lightonai/mLateOn</td><td style="text-align: left; white-space: nowrap;">Late-interaction</td><td style="text-align: left; white-space: nowrap;">0.3B</td><td>0.7906</td><td>0.9392</td><td>0.8061</td><td>0.7905</td><td>0.6431</td><td>0.9803</td><td>0.9608</td><td>0.5817</td><td>0.7005</td><td>0.7135</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">perplexity-ai/pplx-embed-v1-late-0.6b</td><td style="text-align: left; white-space: nowrap;">Late-interaction</td><td style="text-align: left; white-space: nowrap;">0.6B</td><td>0.7381</td><td>0.8557</td><td>0.8089</td><td>0.7973</td><td>0.7285</td><td>0.9696</td><td>0.9548</td><td>0.5400</td><td>0.2816</td><td>0.7064</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">dragonkue/colbert-ko-0.1b</td><td style="text-align: left; white-space: nowrap;">Late-interaction</td><td style="text-align: left; white-space: nowrap;">0.1B</td><td>0.6776</td><td>0.9700</td><td>0.7482</td><td>0.7364</td><td>0.4475</td><td>0.9794</td><td>0.9644</td><td>0.3966</td><td>0.2872</td><td>0.5685</td></tr>
      </tbody>
      <tbody style="border-top: 1px solid rgba(128, 128, 128, 0.25);">
        <tr>
          <th colspan="13" scope="rowgroup" style="padding: 16px 6px 6px; text-align: left; font-size: 0.8em; letter-spacing: 0.08em; text-transform: uppercase;">Sparse Models</th>
        </tr>
        <tr><td style="text-align: left; white-space: nowrap;">omai-research/milco-650m</td><td style="text-align: left; white-space: nowrap;">Sparse</td><td style="text-align: left; white-space: nowrap;">0.6B</td><td>0.7824</td><td>0.9483</td><td>0.8219</td><td>0.8143</td><td>0.6724</td><td>0.9700</td><td>0.9623</td><td>0.6997</td><td>0.4318</td><td>0.7209</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">telepix/PIXIE-Splade-v1.5</td><td style="text-align: left; white-space: nowrap;">Sparse</td><td style="text-align: left; white-space: nowrap;">0.1B</td><td>0.7608</td><td>0.9412</td><td>0.7910</td><td>0.7993</td><td>0.7667</td><td>0.9687</td><td>0.9651</td><td>0.5132</td><td>0.4938</td><td>0.6085</td></tr>
      </tbody>
    </table>
  </div>
</div>

### Performance-Sparsity

<p align="center">
  <img src="assets/ndcg_flops.png" width="80%" alt="Average nDCG@10 vs. average FLOPs of sparse retrievers on MTEB(kor, v2) Retrieval">
</p>

Average active dimensions per vector and FLOPs, averaged over the nine tasks.

<div style="width: fit-content; max-width: 100%; margin: 0 auto;">
  <div style="overflow-x: auto;">
    <table cellpadding="6" style="margin: 0 auto; border-collapse: collapse; color: inherit; text-align: right; font-size: 0.85em; line-height: 1.6; font-variant-numeric: tabular-nums;">
      <thead>
        <tr style="border-bottom: 1px solid rgba(128, 128, 128, 0.35);">
          <th scope="col" style="text-align: left;">Model</th>
          <th scope="col" style="text-align: left;">Params</th>
          <th scope="col">Query dims</th>
          <th scope="col">Document dims</th>
          <th scope="col">FLOPs</th>
        </tr>
      </thead>
      <tbody>
        <tr><td style="text-align: left; white-space: nowrap;"><strong style="color: #c9496b;">KURE-Sparse-base</strong></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">0.6B</span></td><td><span style="color: #c9496b;">100</span></td><td><span style="color: #c9496b;">1,897</span></td><td><span style="color: #c9496b;">36.5</span></td></tr>
        <tr><td style="text-align: left; white-space: nowrap;"><strong style="color: #c9496b;">KURE-Sparse-nano</strong></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">0.1B</span></td><td><span style="color: #c9496b;">147</span></td><td><span style="color: #c9496b;">843</span></td><td><span style="color: #c9496b;">23.0</span></td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">omai-research/milco-650m</td><td style="text-align: left; white-space: nowrap;">0.6B</td><td>105</td><td>1,167</td><td>32.3</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">telepix/PIXIE-Splade-v1.5</td><td style="text-align: left; white-space: nowrap;">0.1B</td><td>117</td><td>1,541</td><td>37.3</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">yjoonjang/splade-ko-v1</td><td style="text-align: left; white-space: nowrap;">0.1B</td><td>109</td><td>742</td><td>29.1</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">telepix/PIXIE-Splade-v1.0</td><td style="text-align: left; white-space: nowrap;">0.1B</td><td>121</td><td>625</td><td>22.4</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">opensearch-project/opensearch-neural-sparse-encoding-multilingual-v1</td><td style="text-align: left; white-space: nowrap;">0.2B</td><td>29</td><td>176</td><td>6.8</td></tr>
      </tbody>
    </table>
  </div>
</div>

### English Retrieval (BEIR, RTEB)

KURE-Sparse-nano is also evaluated on two English benchmarks with nDCG@10: the 13 BEIR tasks (BEIR-13), and the **eight public English** tasks of [RTEB](https://huggingface.co/blog/rteb) outside the code domain. SparseUp runs at its own length limits (128 query and 512 document tokens), and the other models at up to 8,192 tokens. The RTEB average differs from the RTEB leaderboard score, which also covers private and code tasks.

<p align="center">
  <img src="assets/beir_rteb_sparse.png" width="100%" alt="Average nDCG@10 on BEIR-13 and on the public RTEB English tasks of the KURE-Sparse models and sparse baselines">
</p>

#### BEIR-13

<div style="width: fit-content; max-width: 100%; margin: 0 auto;">
  <div style="overflow-x: auto;">
    <table cellpadding="6" style="margin: 0 auto; border-collapse: collapse; color: inherit; text-align: right; font-size: 0.85em; line-height: 1.6; font-variant-numeric: tabular-nums;">
      <thead>
        <tr style="border-bottom: 1px solid rgba(128, 128, 128, 0.35);">
          <th scope="col" style="text-align: left;">Model</th>
          <th scope="col" style="text-align: left;">Params</th>
          <th scope="col">BEIR-13</th>
          <th scope="col">FLOPs</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th colspan="4" scope="rowgroup" style="padding: 16px 6px 6px; text-align: left; font-size: 0.8em; letter-spacing: 0.08em; text-transform: uppercase;">KURE Models</th>
        </tr>
        <tr><td style="text-align: left; white-space: nowrap;"><strong style="color: #c9496b;">KURE-Sparse-base</strong></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">0.6B</span></td><td><strong style="color: #c9496b;">0.5864</strong></td><td><span style="color: #c9496b;">55.8</span></td></tr>
        <tr><td style="text-align: left; white-space: nowrap;"><strong style="color: #c9496b;">KURE-Sparse-nano</strong></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">0.1B</span></td><td><span style="color: #c9496b;">0.5317</span></td><td><span style="color: #c9496b;">37.0</span></td></tr>
      </tbody>
      <tbody style="border-top: 1px solid rgba(128, 128, 128, 0.25);">
        <tr>
          <th colspan="4" scope="rowgroup" style="padding: 16px 6px 6px; text-align: left; font-size: 0.8em; letter-spacing: 0.08em; text-transform: uppercase;">Sparse Models</th>
        </tr>
        <tr><td style="text-align: left; white-space: nowrap;">utahnlp/laconic-1b</td><td style="text-align: left; white-space: nowrap;">1.2B</td><td>0.5831</td><td>52.6</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">Linkup-Platform/linkup-sparseup-embed-v1</td><td style="text-align: left; white-space: nowrap;">0.2B</td><td>0.5645</td><td>8.5</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">omai-research/milco-650m</td><td style="text-align: left; white-space: nowrap;">0.6B</td><td>0.5545</td><td>20.6</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">opensearch-project/opensearch-neural-sparse-encoding-doc-v3-gte</td><td style="text-align: left; white-space: nowrap;">0.1B</td><td>0.5459</td><td>1.7</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">naver/splade-v3</td><td style="text-align: left; white-space: nowrap;">0.1B</td><td>0.5202</td><td>8.0</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">telepix/PIXIE-Splade-v1.5</td><td style="text-align: left; white-space: nowrap;">0.1B</td><td>0.4149</td><td>125.6</td></tr>
      </tbody>
    </table>
  </div>
</div>

<details>
<summary>Per-task nDCG@10</summary>

<div style="width: fit-content; max-width: 100%; margin: 0 auto;">
  <div style="overflow-x: auto;">
    <table cellpadding="6" style="margin: 0 auto; border-collapse: collapse; color: inherit; text-align: right; font-size: 0.85em; line-height: 1.6; font-variant-numeric: tabular-nums;">
      <thead>
        <tr style="border-bottom: 1px solid rgba(128, 128, 128, 0.35);">
          <th scope="col" style="text-align: left;">Model</th>
          <th scope="col">Avg</th>
          <th scope="col">ArguAna</th>
          <th scope="col">ClimateFEVER</th>
          <th scope="col">DBPedia</th>
          <th scope="col">FEVER</th>
          <th scope="col">FiQA</th>
          <th scope="col">HotpotQA</th>
          <th scope="col">NFCorpus</th>
          <th scope="col">NQ</th>
          <th scope="col">Quora</th>
          <th scope="col">SCIDOCS</th>
          <th scope="col">SciFact</th>
          <th scope="col">TREC-COVID</th>
          <th scope="col">Touche-2020</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th colspan="15" scope="rowgroup" style="padding: 16px 6px 6px; text-align: left; font-size: 0.8em; letter-spacing: 0.08em; text-transform: uppercase;">KURE Models</th>
        </tr>
        <tr><td style="text-align: left; white-space: nowrap;"><strong style="color: #c9496b;">KURE-Sparse-base</strong></td><td><strong style="color: #c9496b;">0.5864</strong></td><td><span style="color: #c9496b;">0.5896</span></td><td><span style="color: #c9496b;">0.3959</span></td><td><span style="color: #c9496b;">0.4837</span></td><td><span style="color: #c9496b;">0.9325</span></td><td><span style="color: #c9496b;">0.4720</span></td><td><span style="color: #c9496b;">0.8084</span></td><td><span style="color: #c9496b;">0.3678</span></td><td><span style="color: #c9496b;">0.6758</span></td><td><span style="color: #c9496b;">0.8252</span></td><td><span style="color: #c9496b;">0.1741</span></td><td><span style="color: #c9496b;">0.7183</span></td><td><span style="color: #c9496b;">0.8260</span></td><td><span style="color: #c9496b;">0.3535</span></td></tr>
        <tr><td style="text-align: left; white-space: nowrap;"><strong style="color: #c9496b;">KURE-Sparse-nano</strong></td><td><span style="color: #c9496b;">0.5317</span></td><td><span style="color: #c9496b;">0.5075</span></td><td><span style="color: #c9496b;">0.2865</span></td><td><span style="color: #c9496b;">0.4214</span></td><td><span style="color: #c9496b;">0.9079</span></td><td><span style="color: #c9496b;">0.4080</span></td><td><span style="color: #c9496b;">0.7476</span></td><td><span style="color: #c9496b;">0.3340</span></td><td><span style="color: #c9496b;">0.5647</span></td><td><span style="color: #c9496b;">0.7825</span></td><td><span style="color: #c9496b;">0.1581</span></td><td><span style="color: #c9496b;">0.7120</span></td><td><span style="color: #c9496b;">0.7637</span></td><td><span style="color: #c9496b;">0.3183</span></td></tr>
      </tbody>
      <tbody style="border-top: 1px solid rgba(128, 128, 128, 0.25);">
        <tr>
          <th colspan="15" scope="rowgroup" style="padding: 16px 6px 6px; text-align: left; font-size: 0.8em; letter-spacing: 0.08em; text-transform: uppercase;">Sparse Models</th>
        </tr>
        <tr><td style="text-align: left; white-space: nowrap;">utahnlp/laconic-1b</td><td>0.5831</td><td>0.6127</td><td>0.3952</td><td>0.4705</td><td>0.8871</td><td>0.4427</td><td>0.8018</td><td>0.3958</td><td>0.6642</td><td>0.8072</td><td>0.2397</td><td>0.7596</td><td>0.8300</td><td>0.2737</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">Linkup-Platform/linkup-sparseup-embed-v1</td><td>0.5645</td><td>0.5648</td><td>0.3747</td><td>0.4150</td><td>0.8969</td><td>0.4687</td><td>0.7761</td><td>0.3523</td><td>0.5717</td><td>0.8656</td><td>0.1852</td><td>0.7376</td><td>0.7823</td><td>0.3478</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">omai-research/milco-650m</td><td>0.5545</td><td>0.6157</td><td>0.3079</td><td>0.4501</td><td>0.8353</td><td>0.4262</td><td>0.7780</td><td>0.3629</td><td>0.6495</td><td>0.8818</td><td>0.1704</td><td>0.7020</td><td>0.7476</td><td>0.2813</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">opensearch-project/opensearch-neural-sparse-encoding-doc-v3-gte</td><td>0.5459</td><td>0.5196</td><td>0.3123</td><td>0.4553</td><td>0.8598</td><td>0.4069</td><td>0.7158</td><td>0.3592</td><td>0.5817</td><td>0.8734</td><td>0.1675</td><td>0.7251</td><td>0.7330</td><td>0.3866</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">naver/splade-v3</td><td>0.5202</td><td>0.4880</td><td>0.2566</td><td>0.4514</td><td>0.8098</td><td>0.3810</td><td>0.6924</td><td>0.3630</td><td>0.5867</td><td>0.8138</td><td>0.1557</td><td>0.7171</td><td>0.7346</td><td>0.3119</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">telepix/PIXIE-Splade-v1.5</td><td>0.4149</td><td>0.2185</td><td>0.1302</td><td>0.3519</td><td>0.6475</td><td>0.2753</td><td>0.5756</td><td>0.3325</td><td>0.3858</td><td>0.6878</td><td>0.1468</td><td>0.6694</td><td>0.7068</td><td>0.2650</td></tr>
      </tbody>
    </table>
  </div>
</div>

</details>

#### RTEB

<div style="width: fit-content; max-width: 100%; margin: 0 auto;">
  <div style="overflow-x: auto;">
    <table cellpadding="6" style="margin: 0 auto; border-collapse: collapse; color: inherit; text-align: right; font-size: 0.85em; line-height: 1.6; font-variant-numeric: tabular-nums;">
      <thead>
        <tr style="border-bottom: 1px solid rgba(128, 128, 128, 0.35);">
          <th scope="col" style="text-align: left;">Model</th>
          <th scope="col" style="text-align: left;">Params</th>
          <th scope="col">Avg</th>
          <th scope="col">FLOPs</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th colspan="4" scope="rowgroup" style="padding: 16px 6px 6px; text-align: left; font-size: 0.8em; letter-spacing: 0.08em; text-transform: uppercase;">KURE Models</th>
        </tr>
        <tr><td style="text-align: left; white-space: nowrap;"><strong><a href="https://huggingface.co/nlpai-lab/KURE-Sparse-nano" style="color: #c9496b;">nlpai-lab/KURE-Sparse-nano</a></strong></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">0.1B</span></td><td><strong style="color: #c9496b;">0.4750</strong></td><td><span style="color: #c9496b;">109.9</span></td></tr>
        <tr><td style="text-align: left; white-space: nowrap;"><a href="https://huggingface.co/nlpai-lab/KURE-Sparse-base" style="color: #c9496b;">nlpai-lab/KURE-Sparse-base</a></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">0.6B</span></td><td><span style="color: #c9496b;">0.5093</span></td><td><span style="color: #c9496b;">277.6</span></td></tr>
      </tbody>
      <tbody style="border-top: 1px solid rgba(128, 128, 128, 0.25);">
        <tr>
          <th colspan="4" scope="rowgroup" style="padding: 16px 6px 6px; text-align: left; font-size: 0.8em; letter-spacing: 0.08em; text-transform: uppercase;">Sparse Models</th>
        </tr>
        <tr><td style="text-align: left; white-space: nowrap;">utahnlp/laconic-1b</td><td style="text-align: left; white-space: nowrap;">1.2B</td><td>0.5415</td><td>107.2</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">Linkup-Platform/linkup-sparseup-embed-v1</td><td style="text-align: left; white-space: nowrap;">0.2B</td><td>0.4941</td><td>25.1</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">opensearch-project/opensearch-neural-sparse-encoding-doc-v3-gte</td><td style="text-align: left; white-space: nowrap;">0.1B</td><td>0.4721</td><td>12.7</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">naver/splade-v3</td><td style="text-align: left; white-space: nowrap;">0.1B</td><td>0.4596</td><td>35.0</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">omai-research/milco-650m</td><td style="text-align: left; white-space: nowrap;">0.6B</td><td>0.4301</td><td>163.7</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">telepix/PIXIE-Splade-v1.5</td><td style="text-align: left; white-space: nowrap;">0.1B</td><td>0.3630</td><td>391.3</td></tr>
      </tbody>
    </table>
  </div>
</div>

<details>
<summary>Per-task nDCG@10</summary>

<div style="width: fit-content; max-width: 100%; margin: 0 auto;">
  <div style="overflow-x: auto;">
    <table cellpadding="6" style="margin: 0 auto; border-collapse: collapse; color: inherit; text-align: right; font-size: 0.85em; line-height: 1.6; font-variant-numeric: tabular-nums;">
      <thead>
        <tr style="border-bottom: 1px solid rgba(128, 128, 128, 0.35);">
          <th scope="col" style="text-align: left;">Model</th>
          <th scope="col" style="text-align: left;">Params</th>
          <th scope="col">Avg</th>
          <th scope="col">CUREv1</th>
          <th scope="col">ChatDoctor</th>
          <th scope="col">FinQA</th>
          <th scope="col">AILACasedocs</th>
          <th scope="col">LegalSummarization</th>
          <th scope="col">HC3Finance</th>
          <th scope="col">FinanceBench</th>
          <th scope="col">AILAStatutes</th>
          <th scope="col">FLOPs</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th colspan="12" scope="rowgroup" style="padding: 16px 6px 6px; text-align: left; font-size: 0.8em; letter-spacing: 0.08em; text-transform: uppercase;">KURE Models</th>
        </tr>
        <tr><td style="text-align: left; white-space: nowrap;"><strong><a href="https://huggingface.co/nlpai-lab/KURE-Sparse-nano" style="color: #c9496b;">nlpai-lab/KURE-Sparse-nano</a></strong></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">0.1B</span></td><td><strong style="color: #c9496b;">0.4750</strong></td><td><span style="color: #c9496b;">0.3591</span></td><td><span style="color: #c9496b;">0.4730</span></td><td><span style="color: #c9496b;">0.7042</span></td><td><span style="color: #c9496b;">0.2860</span></td><td><span style="color: #c9496b;">0.6399</span></td><td><span style="color: #c9496b;">0.4438</span></td><td><span style="color: #c9496b;">0.7005</span></td><td><span style="color: #c9496b;">0.1939</span></td><td><span style="color: #c9496b;">109.9</span></td></tr>
        <tr><td style="text-align: left; white-space: nowrap;"><a href="https://huggingface.co/nlpai-lab/KURE-Sparse-base" style="color: #c9496b;">nlpai-lab/KURE-Sparse-base</a></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">0.6B</span></td><td><span style="color: #c9496b;">0.5093</span></td><td><span style="color: #c9496b;">0.5996</span></td><td><span style="color: #c9496b;">0.3914</span></td><td><span style="color: #c9496b;">0.7838</span></td><td><span style="color: #c9496b;">0.2298</span></td><td><span style="color: #c9496b;">0.5494</span></td><td><span style="color: #c9496b;">0.5951</span></td><td><span style="color: #c9496b;">0.7525</span></td><td><span style="color: #c9496b;">0.1727</span></td><td><span style="color: #c9496b;">277.6</span></td></tr>
      </tbody>
      <tbody style="border-top: 1px solid rgba(128, 128, 128, 0.25);">
        <tr>
          <th colspan="12" scope="rowgroup" style="padding: 16px 6px 6px; text-align: left; font-size: 0.8em; letter-spacing: 0.08em; text-transform: uppercase;">Sparse Models</th>
        </tr>
        <tr><td style="text-align: left; white-space: nowrap;">utahnlp/laconic-1b</td><td style="text-align: left; white-space: nowrap;">1.2B</td><td>0.5415</td><td>0.5340</td><td>0.5272</td><td>0.6727</td><td>0.3436</td><td>0.6064</td><td>0.5893</td><td>0.7449</td><td>0.3142</td><td>107.2</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">Linkup-Platform/linkup-sparseup-embed-v1</td><td style="text-align: left; white-space: nowrap;">0.2B</td><td>0.4941</td><td>0.4010</td><td>0.5424</td><td>0.5805</td><td>0.2406</td><td>0.6430</td><td>0.5900</td><td>0.6852</td><td>0.2700</td><td>25.1</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">opensearch-project/opensearch-neural-sparse-encoding-doc-v3-gte</td><td style="text-align: left; white-space: nowrap;">0.1B</td><td>0.4721</td><td>0.3004</td><td>0.5015</td><td>0.7344</td><td>0.2596</td><td>0.6554</td><td>0.4265</td><td>0.6855</td><td>0.2139</td><td>12.7</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">naver/splade-v3</td><td style="text-align: left; white-space: nowrap;">0.1B</td><td>0.4596</td><td>0.3306</td><td>0.5036</td><td>0.6374</td><td>0.3153</td><td>0.5663</td><td>0.4118</td><td>0.6878</td><td>0.2241</td><td>35.0</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">omai-research/milco-650m</td><td style="text-align: left; white-space: nowrap;">0.6B</td><td>0.4301</td><td>0.5674</td><td>0.2344</td><td>0.7399</td><td>0.2197</td><td>0.3078</td><td>0.5451</td><td>0.6513</td><td>0.1747</td><td>163.7</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">telepix/PIXIE-Splade-v1.5</td><td style="text-align: left; white-space: nowrap;">0.1B</td><td>0.3630</td><td>0.3414</td><td>0.2178</td><td>0.5751</td><td>0.2082</td><td>0.5216</td><td>0.3042</td><td>0.5180</td><td>0.2181</td><td>391.3</td></tr>
      </tbody>
    </table>
  </div>
</div>

</details>

## Citation

```bibtex
@misc{kure-sparse,
  title  = {KURE-Sparse: a Korean-English bilingual learned sparse retriever},
  author = {Jang, Youngjoon and Son, Junyoung and Lee, Taemin and Hong, Seongtae and Lim, Heuiseok},
  year   = {2026},
  url    = {https://huggingface.co/nlpai-lab/KURE-Sparse-nano},
}
```

```bibtex
@misc{kure-v2,
  title  = {KURE-v2: a Korean-English bilingual late-interaction retriever},
  author = {Jang, Youngjoon and Son, Junyoung and Lee, Taemin and Hong, Seongtae and Lim, Heuiseok},
  year   = {2026},
  url    = {https://huggingface.co/nlpai-lab/KURE-v2},
}
```

```bibtex
@inproceedings{jang2025kure,
  title={KURE: Embedding Model for Korean-Specific Retrieval},
  author={Jang, Youngjoon and Son, Junyoung and Lee, Taemin and Hong, Seongtae and Park, JeongBae and Lim, Heuiseok},
  booktitle={Annual Conference on Human and Language Technology},
  pages={129--134},
  year={2025},
  organization={Human and Language Technology}
}
```
