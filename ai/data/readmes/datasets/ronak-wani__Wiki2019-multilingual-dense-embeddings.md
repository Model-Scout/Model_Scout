---
language:
- ar
- bn
- en
- fi
- ja
- ko
- ru
- te
license: apache-2.0
tags:
- qdrant
- vector-database
- dense-retrieval
- embeddings
- multilingual
- wikipedia
size_categories:
- 1B<n<10B
---

# Wiki2019-multilingual-dense-embeddings

Qdrant vector database containing dense embeddings for the **wiki_composite** collection, built from 2019 Wikipedia dumps across 8 languages.

## Collection Details

| Property | Value |
|---|---|
| **Embedding model** | `nvidia/llama-embed-nemotron-8b` |
| **Qdrant version** | 1.17.0 |
| **Vector size** | 4096 |
| **Distance metric** | Cosine |
| **Storage mode** | On-disk (payload + vectors) |
| **Total size** | 947 GB (882 GiB) |
| **Payload index** | Keyword index on "wiki" field
| **Chunking strategy** | Recursive Character Text Splitter
| **Chunk size** | 512 tokens
| **Chunk overlap** | 50 tokens


## Languages

| Code | Language |
|---|---|
| `arwiki` | Arabic |
| `bnwiki` | Bengali |
| `enwiki` | English |
| `fiwiki` | Finnish |
| `jawiki` | Japanese |
| `kowiki` | Korean |
| `ruwiki` | Russian |
| `tewiki` | Telugu |

## Dense Embeddings Download Instructions

### 1. Download the storage directory

```bash
huggingface-cli download ronak-wani/Wiki2019-multilingual-dense-embeddings \
    --repo-type dataset \
    --local-dir ./Wiki2019-multilingual-dense-embeddings
```

### 2. Build the Qdrant sandbox (if not already built)

```bash
apptainer build --sandbox qdrant_sandbox docker://qdrant/qdrant:v1.17.0
```

### 3. Start Qdrant pointing at the restored storage

```bash
apptainer exec \
  --bind ./Wiki2019-multilingual-dense-embeddings/storage:/qdrant/storage \
  --env QDRANT__SERVICE__HOST=0.0.0.0 \
  qdrant_sandbox qdrant_sandbox/qdrant/qdrant
```

### 4. Verify the collection is live

```bash
curl -s http://localhost:6333/collections/wiki_composite | python3 -m json.tool
```
