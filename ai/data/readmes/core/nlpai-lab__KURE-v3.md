---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- matryoshka
language:
- ko
- en
base_model: nvidia/Nemotron-3-Embed-1B-BF16
pipeline_tag: sentence-similarity
library_name: sentence-transformers
license: apache-2.0
---

<a href="https://github.com/nlpai-lab/KURE">
  <img src="https://huggingface.co/nlpai-lab/KURE-v2/resolve/main/kure_logo.png" width="50%"/>
</a>


# 🔎 KURE-v3

**KURE-v3** is a Korean-English bilingual dense retrieval model. With 1.1B parameters, it averages **0.8027** nDCG@10 on MTEB(kor, v2) Retrieval. It outperforms 8B dense models such as comsat-embed-ko-8b-preview and Qwen3-Embedding-8B.
It is also served through the [KURE API](https://kure.kullm.ai/).

<p align="center">
  <img src="assets/kure_v3_ndcg.png" width="100%" alt="Average nDCG@10 on MTEB(kor, v2) Retrieval of KURE-v3 and baseline retrievers">
</p>

## Key Characteristics

- **Dense (single-vector)**: one 2,048-dimensional vector per text, scored by cosine similarity.
- **Matryoshka embeddings**: trained at 2,048, 1,024, 512 and 256 dimensions, so vectors can be truncated.
- **Long documents**: up to 8,192 tokens.

## Usage

### Sentence Transformers

```bash
pip install -U sentence-transformers
```

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("nlpai-lab/KURE-v3", model_kwargs={"attn_implementation": "flash_attention_2"})
# model = SentenceTransformer("nlpai-lab/KURE-v3", model_kwargs={"attn_implementation": "flash_attention_2"}, truncate_dim=1024)  # smaller Matryoshka vectors

query = "훈민정음은 언제 만들어졌나요?"
documents = [
    "세종대왕은 1443년에 훈민정음을 창제하고 1446년에 이를 반포하였다.",
    "김치는 배추나 무를 소금에 절인 뒤 고춧가루와 젓갈을 넣어 발효시킨 음식이다.",
    "한라산은 해발 1,947m로 남한에서 가장 높은 산이며 제주도 중앙에 자리한다.",
]

# encode_query / encode_document add the "query: " / "passage: " prompts KURE-v3 expects
query_embeddings = model.encode_query(query)
document_embeddings = model.encode_document(documents)
print(query_embeddings.shape, document_embeddings.shape)
# (2048,) (3, 2048)

# Cosine similarity (higher is more relevant)
scores = model.similarity(query_embeddings, document_embeddings)
print(scores)
# tensor([[ 0.5386,  0.0152, -0.0211]])
```

### API

KURE-v3 is served at [kure.kullm.ai](https://kure.kullm.ai/) through an OpenAI-compatible endpoint. Sign in with GitHub there to get an API key.

```python
import os

import numpy as np
from openai import OpenAI

client = OpenAI(base_url="https://kure.kullm.ai/api/v1", api_key=os.environ["KURE_API_KEY"])

query = "훈민정음은 언제 만들어졌나요?"
documents = [
    "세종대왕은 1443년에 훈민정음을 창제하고 1446년에 이를 반포하였다.",
    "김치는 배추나 무를 소금에 절인 뒤 고춧가루와 젓갈을 넣어 발효시킨 음식이다.",
    "한라산은 해발 1,947m로 남한에서 가장 높은 산이며 제주도 중앙에 자리한다.",
]

# input_type adds the query or document prompt. Vectors are 2048-d, pass dimensions=(256 to 2048) for a smaller Matryoshka size
query_embedding = client.embeddings.create(model="kure-v3", input=query, extra_body={"input_type": "query"})
document_embeddings = client.embeddings.create(model="kure-v3", input=documents, extra_body={"input_type": "document"})

# Vectors are L2-normalized, so the dot product is the cosine similarity
q = np.array(query_embedding.data[0].embedding)
d = np.array([e.embedding for e in document_embeddings.data])
print((d @ q).round(4))
# [ 0.5384  0.0145 -0.0207]
```

## Evaluation

KURE-v3 is evaluated on the nine **MTEB(kor, v2) Retrieval** tasks. We report nDCG@10.

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
        <tr><td style="text-align: left; white-space: nowrap;"><strong><a href="https://huggingface.co/nlpai-lab/KURE-v3" style="color: #c9496b;">nlpai-lab/KURE-v3</a></strong></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">Dense</span></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">1.1B</span></td><td><strong style="color: #c9496b;">0.8027</strong></td><td><span style="color: #c9496b;">0.9324</span></td><td><span style="color: #c9496b;">0.8639</span></td><td><span style="color: #c9496b;">0.8192</span></td><td><span style="color: #c9496b;">0.8158</span></td><td><span style="color: #c9496b;">0.9666</span></td><td><span style="color: #c9496b;">0.9673</span></td><td><span style="color: #c9496b;">0.6320</span></td><td><span style="color: #c9496b;">0.4781</span></td><td><span style="color: #c9496b;">0.7489</span></td></tr>
        <tr><td style="text-align: left; white-space: nowrap;"><a href="https://huggingface.co/nlpai-lab/KURE-v2" style="color: #c9496b;">nlpai-lab/KURE-v2</a></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">Late-interaction</span></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">0.2B</span></td><td><span style="color: #c9496b;">0.8160</span></td><td><span style="color: #c9496b;">0.9718</span></td><td><span style="color: #c9496b;">0.8228</span></td><td><span style="color: #c9496b;">0.8070</span></td><td><span style="color: #c9496b;">0.7550</span></td><td><span style="color: #c9496b;">0.9846</span></td><td><span style="color: #c9496b;">0.9660</span></td><td><span style="color: #c9496b;">0.5974</span></td><td><span style="color: #c9496b;">0.7158</span></td><td><span style="color: #c9496b;">0.7237</span></td></tr>
        <tr><td style="text-align: left; white-space: nowrap;"><a href="https://huggingface.co/nlpai-lab/KURE-Sparse-base" style="color: #c9496b;">nlpai-lab/KURE-Sparse-base</a></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">Sparse</span></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">0.6B</span></td><td><span style="color: #c9496b;">0.7984</span></td><td><span style="color: #c9496b;">0.9445</span></td><td><span style="color: #c9496b;">0.8099</span></td><td><span style="color: #c9496b;">0.8188</span></td><td><span style="color: #c9496b;">0.7244</span></td><td><span style="color: #c9496b;">0.9815</span></td><td><span style="color: #c9496b;">0.9703</span></td><td><span style="color: #c9496b;">0.6255</span></td><td><span style="color: #c9496b;">0.5716</span></td><td><span style="color: #c9496b;">0.7395</span></td></tr>
        <tr><td style="text-align: left; white-space: nowrap;"><a href="https://huggingface.co/nlpai-lab/KURE-Sparse-nano" style="color: #c9496b;">nlpai-lab/KURE-Sparse-nano</a></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">Sparse</span></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">0.1B</span></td><td><span style="color: #c9496b;">0.7716</span></td><td><span style="color: #c9496b;">0.9360</span></td><td><span style="color: #c9496b;">0.7711</span></td><td><span style="color: #c9496b;">0.7924</span></td><td><span style="color: #c9496b;">0.7226</span></td><td><span style="color: #c9496b;">0.9774</span></td><td><span style="color: #c9496b;">0.9608</span></td><td><span style="color: #c9496b;">0.5618</span></td><td><span style="color: #c9496b;">0.5133</span></td><td><span style="color: #c9496b;">0.7091</span></td></tr>
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
        <tr><td style="text-align: left; white-space: nowrap;">kakaocorp/kanana-2-3b-embedding</td><td style="text-align: left; white-space: nowrap;">Dense</td><td style="text-align: left; white-space: nowrap;">3.2B</td><td>0.7584</td><td>0.8393</td><td>0.8772</td><td>0.8329</td><td>0.8057</td><td>0.9246</td><td>0.9437</td><td>0.5967</td><td>0.3590</td><td>0.6466</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">nvidia/llama-nemotron-embed-1b-v2</td><td style="text-align: left; white-space: nowrap;">Dense</td><td style="text-align: left; white-space: nowrap;">1.2B</td><td>0.7564</td><td>0.8708</td><td>0.8177</td><td>0.8055</td><td>0.7329</td><td>0.9345</td><td>0.9519</td><td>0.5988</td><td>0.3952</td><td>0.7004</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">dragonkue/BGE-m3-ko</td><td style="text-align: left; white-space: nowrap;">Dense</td><td style="text-align: left; white-space: nowrap;">0.6B</td><td>0.7547</td><td>0.8738</td><td>0.8155</td><td>0.7959</td><td>0.7322</td><td>0.9414</td><td>0.9503</td><td>0.6099</td><td>0.3899</td><td>0.6833</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">BAAI/bge-m3</td><td style="text-align: left; white-space: nowrap;">Dense</td><td style="text-align: left; white-space: nowrap;">0.6B</td><td>0.7509</td><td>0.8301</td><td>0.8041</td><td>0.7941</td><td>0.7174</td><td>0.9038</td><td>0.9315</td><td>0.6471</td><td>0.4287</td><td>0.7015</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">jinaai/jina-embeddings-v5-text-small-retrieval</td><td style="text-align: left; white-space: nowrap;">Dense</td><td style="text-align: left; white-space: nowrap;">0.6B</td><td>0.7419</td><td>0.8409</td><td>0.8664</td><td>0.8096</td><td>0.7483</td><td>0.8926</td><td>0.9346</td><td>0.5779</td><td>0.3315</td><td>0.6752</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">perplexity-ai/pplx-embed-v1-0.6b</td><td style="text-align: left; white-space: nowrap;">Dense</td><td style="text-align: left; white-space: nowrap;">0.6B</td><td>0.7390</td><td>0.8414</td><td>0.8255</td><td>0.8100</td><td>0.7444</td><td>0.9174</td><td>0.9393</td><td>0.5524</td><td>0.3179</td><td>0.7026</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">google/embeddinggemma-300m</td><td style="text-align: left; white-space: nowrap;">Dense</td><td style="text-align: left; white-space: nowrap;">0.3B</td><td>0.7254</td><td>0.8187</td><td>0.8170</td><td>0.8008</td><td>0.6850</td><td>0.9114</td><td>0.9430</td><td>0.5253</td><td>0.3844</td><td>0.6434</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">kakaocorp/kanana-2-1.3b-embedding</td><td style="text-align: left; white-space: nowrap;">Dense</td><td style="text-align: left; white-space: nowrap;">1.3B</td><td>0.7172</td><td>0.8108</td><td>0.8647</td><td>0.8146</td><td>0.7653</td><td>0.9014</td><td>0.9222</td><td>0.5540</td><td>0.2088</td><td>0.6129</td></tr>
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

### Matryoshka Dimensions

Truncated to 1,024 dimensions, KURE-v3 keeps 99% of its full-size score and still outperforms comsat-embed-ko-8b-preview and Qwen3-Embedding-8B (4,096 dimensions).

<p align="center">
  <img src="assets/kure_v3_mrl.png" width="70%" alt="Average nDCG@10 of KURE-v3 on MTEB(kor, v2) Retrieval at each Matryoshka dimension">
</p>

### RTEB (Retrieval Embedding Benchmark)

We also evaluate dense (single-vector) models on [RTEB](https://huggingface.co/blog/rteb), an English retrieval benchmark that combines open and private datasets to measure how well models generalize to real-world data. We evaluate its **eight public English** tasks outside the code domain, so the average differs from the RTEB leaderboard score. We report nDCG@10.

<p align="center">
  <img src="assets/kure_v3_rteb_dense.png" width="100%" alt="Average nDCG@10 on the public RTEB English tasks of KURE-v3 and dense baselines">
</p>

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
        </tr>
      </thead>
      <tbody>
        <tr><td style="text-align: left; white-space: nowrap;">nvidia/Nemotron-3-Embed-8B-BF16</td><td style="text-align: left; white-space: nowrap;">8.0B</td><td>0.7405</td><td>0.6818</td><td>0.7695</td><td>0.8849</td><td>0.4908</td><td>0.7677</td><td>0.7990</td><td>0.9502</td><td>0.5804</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">sionic-ai/comsat-embed-ko-8b-preview</td><td style="text-align: left; white-space: nowrap;">7.6B</td><td>0.6942</td><td>0.6146</td><td>0.7337</td><td>0.6476</td><td>0.4689</td><td>0.6987</td><td>0.7084</td><td>0.8430</td><td>0.8385</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">Qwen/Qwen3-Embedding-8B</td><td style="text-align: left; white-space: nowrap;">7.6B</td><td>0.6887</td><td>0.6294</td><td>0.7323</td><td>0.6339</td><td>0.4409</td><td>0.7069</td><td>0.7196</td><td>0.8280</td><td>0.8190</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;"><strong><a href="https://huggingface.co/nlpai-lab/KURE-v3" style="color: #c9496b;">nlpai-lab/KURE-v3</a></strong></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">1.1B</span></td><td><strong style="color: #c9496b;">0.6885</strong></td><td><span style="color: #c9496b;">0.6518</span></td><td><span style="color: #c9496b;">0.6713</span></td><td><span style="color: #c9496b;">0.8632</span></td><td><span style="color: #c9496b;">0.4267</span></td><td><span style="color: #c9496b;">0.7180</span></td><td><span style="color: #c9496b;">0.7018</span></td><td><span style="color: #c9496b;">0.8753</span></td><td><span style="color: #c9496b;">0.5997</span></td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">perplexity-ai/pplx-embed-v1-4b</td><td style="text-align: left; white-space: nowrap;">4.0B</td><td>0.6829</td><td>0.5774</td><td>0.7407</td><td>0.8358</td><td>0.4546</td><td>0.6806</td><td>0.7289</td><td>0.8438</td><td>0.6012</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">nvidia/Nemotron-3-Embed-1B-BF16</td><td style="text-align: left; white-space: nowrap;">1.1B</td><td>0.6676</td><td>0.6169</td><td>0.6809</td><td>0.8242</td><td>0.4287</td><td>0.7267</td><td>0.6444</td><td>0.8540</td><td>0.5649</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">Qwen/Qwen3-Embedding-4B</td><td style="text-align: left; white-space: nowrap;">4.0B</td><td>0.6601</td><td>0.6104</td><td>0.7138</td><td>0.6339</td><td>0.3938</td><td>0.6612</td><td>0.6877</td><td>0.7662</td><td>0.8140</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">codefuse-ai/F2LLM-v2-8B</td><td style="text-align: left; white-space: nowrap;">7.6B</td><td>0.6426</td><td>0.5541</td><td>0.7975</td><td>0.6108</td><td>0.4498</td><td>0.6499</td><td>0.7596</td><td>0.8744</td><td>0.4448</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">perplexity-ai/pplx-embed-v1-0.6b</td><td style="text-align: left; white-space: nowrap;">0.6B</td><td>0.6407</td><td>0.5888</td><td>0.6885</td><td>0.7333</td><td>0.3865</td><td>0.6804</td><td>0.6822</td><td>0.7875</td><td>0.5788</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">jinaai/jina-embeddings-v5-text-small-retrieval</td><td style="text-align: left; white-space: nowrap;">0.6B</td><td>0.6111</td><td>0.5701</td><td>0.7113</td><td>0.5563</td><td>0.4378</td><td>0.6485</td><td>0.6220</td><td>0.8076</td><td>0.5352</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">Qwen/Qwen3-Embedding-0.6B</td><td style="text-align: left; white-space: nowrap;">0.6B</td><td>0.5874</td><td>0.5175</td><td>0.6208</td><td>0.5740</td><td>0.3525</td><td>0.6234</td><td>0.5471</td><td>0.7375</td><td>0.7261</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">google/embeddinggemma-300m</td><td style="text-align: left; white-space: nowrap;">0.3B</td><td>0.5568</td><td>0.6012</td><td>0.6342</td><td>0.5437</td><td>0.3468</td><td>0.6833</td><td>0.5997</td><td>0.7748</td><td>0.2706</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">telepix/PIXIE-Rune-v1.5</td><td style="text-align: left; white-space: nowrap;">0.6B</td><td>0.5488</td><td>0.5740</td><td>0.5976</td><td>0.6228</td><td>0.3590</td><td>0.6711</td><td>0.5252</td><td>0.7865</td><td>0.2540</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">kakaocorp/kanana-2-3b-embedding</td><td style="text-align: left; white-space: nowrap;">3.2B</td><td>0.5421</td><td>0.6032</td><td>0.6192</td><td>0.5292</td><td>0.3288</td><td>0.6345</td><td>0.5717</td><td>0.7978</td><td>0.2524</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;"><a href="https://huggingface.co/nlpai-lab/KURE-v1" style="color: #c9496b;">nlpai-lab/KURE-v1</a></td><td style="text-align: left; white-space: nowrap;"><span style="color: #c9496b;">0.6B</span></td><td><span style="color: #c9496b;">0.5246</span></td><td><span style="color: #c9496b;">0.5566</span></td><td><span style="color: #c9496b;">0.5665</span></td><td><span style="color: #c9496b;">0.5977</span></td><td><span style="color: #c9496b;">0.3685</span></td><td><span style="color: #c9496b;">0.6300</span></td><td><span style="color: #c9496b;">0.5080</span></td><td><span style="color: #c9496b;">0.7457</span></td><td><span style="color: #c9496b;">0.2235</span></td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">BAAI/bge-m3</td><td style="text-align: left; white-space: nowrap;">0.6B</td><td>0.5194</td><td>0.5531</td><td>0.5797</td><td>0.5570</td><td>0.3597</td><td>0.6329</td><td>0.5100</td><td>0.6667</td><td>0.2961</td></tr>
        <tr><td style="text-align: left; white-space: nowrap;">kakaocorp/kanana-2-1.3b-embedding</td><td style="text-align: left; white-space: nowrap;">1.3B</td><td>0.5013</td><td>0.5813</td><td>0.5418</td><td>0.4834</td><td>0.2229</td><td>0.6324</td><td>0.5120</td><td>0.7556</td><td>0.2806</td></tr>
      </tbody>
    </table>
  </div>
</div>

## License

KURE-v3 is released under the [Apache License 2.0](LICENSE).

## Citation

```bibtex
@misc{kure-v3,
  title  = {KURE-v3: a Korean-English bilingual dense retriever},
  author = {Jang, Youngjoon and Son, Junyoung and Lee, Taemin and Hong, Seongtae and Lee, Jungseob and Lim, Heuiseok},
  year   = {2026},
  url    = {https://huggingface.co/nlpai-lab/KURE-v3},
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
