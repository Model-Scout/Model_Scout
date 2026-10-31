---
license: apache-2.0
language:
  - ar
  - bg
  - cs
  - de
  - en
  - es
  - fr
  - hi
  - hr
  - id
  - it
  - ja
  - ko
  - nl
  - pl
  - pt
  - ro
  - ru
  - sv
  - th
  - tr
  - vi
  - zh
tags:
  - construction
  - cost-estimation
  - BIM
  - quantity-surveying
  - vector-database
  - qdrant
  - bge-m3
  - hybrid-search
  - multilingual
  - construction-rates
size_categories:
  - 1M<n<10M
pretty_name: CWICR Vector DB (BGE-M3 V3) — 30 Countries
---

# CWICR Vector Database — BGE-M3 V3 Snapshots

![Cost distribution by department](./assets/cost_distribution_by_department.png)

Production Qdrant snapshots for **CWICR (Construction Works Items, Costs & Resources)** — a multilingual catalogue of construction rate databases covering **30 countries / language locales**. Each snapshot encodes one country's rate book using the **BAAI/bge-m3** embedder and is ready to restore directly into a Qdrant server for hybrid semantic search.

These snapshots are the V3 production artifacts produced by the OpenConstructionEstimate / CWICR pipeline. The primary downstream use case is **BIM-element ↔ construction-rate matching** for cost estimation, but the data is general-purpose for any retrieval over multilingual construction-cost catalogues.

> 💡 **Looking for a full estimation platform?** These snapshots power the semantic-search layer of [**OpenConstructionERP**](https://github.com/datadrivenconstruction/OpenConstructionERP) — an open-source modular ERP for construction (BOQ editor, BIM/CAD import, AI takeoff, GAEB XML, AGPL-3.0). The ERP boots one Qdrant collection per locale from these files and uses BGE-M3 hybrid search to match BIM elements to local rates in 30 markets out of the box.

## What's inside

Each `.snapshot` file is a Qdrant collection snapshot of one country's rate database with:

- **Granularity**: one Qdrant point per unique `rate_code` (≈ 55,000 rates per country).
- **Named vectors** per point:
  - `dense` — 1024-d, COSINE, BGE-M3 dense embedding of the rate's title + work composition + hierarchy.
  - `sparse` — BGE-M3 lexical sparse vector (BM25-like, IDF-modified) for exact-code / token matching.
  - `resources` — 1024-d, COSINE, optional dense embedding of the rate's resource list (machinery, materials, labour). Present only for non-abstract rates.
- **Payload** (29 indexed fields): `rate_code`, `country`, `collection_name`, `category_type`, `department_code`, `is_abstract`, `rate_unit`, `mass_*`, plus hierarchy / classification tags. Heavy fields (prices, full resource composition) live in the matching `*.parquet` files in the parent CWICR repository, looked up by `rate_code`.

Total rates indexed: **~1.65 M points** across 30 collections.

## File naming

```
<LANG>_<CITY>_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot
```

Example: `VI_HANOI_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot`.

Snapshots are organised into one folder per language code (`AR/`, `BG/`, `CS/`, `DE/`, `EN/`, `ES/`, `FR/`, `HI/`, `HR/`, `ID/`, `IT/`, `JA/`, `KO/`, `MX/`, `NG/`, `NL/`, `NZ/`, `PL/`, `PT/`, `RO/`, `RU/`, `SV/`, `TH/`, `TR/`, `UK/`, `US/`, `VI/`, `ZA/`, `ZH/`, `AU/`).

## Coverage status

**All 30 locales are uploaded.** One Qdrant snapshot per locale, organised in `<LANG>/` folders:

`AR/`, `AU/`, `BG/`, `CS/`, `DE/`, `EN/`, `ES/`, `FR/`, `HI/`, `HR/`, `ID/`, `IT/`, `JA/`, `KO/`, `MX/`, `NG/`, `NL/`, `NZ/`, `PL/`, `PT/`, `RO/`, `RU/`, `SV/`, `TH/`, `TR/`, `UK/`, `US/`, `VI/`, `ZA/`, `ZH/`.

For the tabular source data (parquet + CSV/XLSX catalogues + localised TXT readmes + per-country README.md) used to produce these snapshots, see the companion dataset: [`DataDrivenConstruction/cwicr-construction-rates`](https://huggingface.co/datasets/DataDrivenConstruction/cwicr-construction-rates) — 150 country files + top-level docs, fully mirrored 1-to-1 with this snapshot repo.

## Reproducibility

Each snapshot is reproducible from the corresponding parquet (`*_workitems_costs_resources_DDC_CWICR.parquet`) in the [CWICR source repo](https://github.com/datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR) using the V3 production encoder in that repo: `0_Workflow and Pipelines CWICR/python/10-embedding-pipeline/v3_production_all_languages.py`.

Embedder: `BAAI/bge-m3` (Apache-2.0). Point IDs are derived via `uuid5(NS_CWICR, f"{country}|{rate_code}")` so re-encoding is idempotent.

## Restoring a snapshot into Qdrant

Bring up Qdrant locally:

```bash
docker run -d --name qdrant -p 6333:6333 -p 6334:6334 \
  -v "$(pwd)/qdrant_storage:/qdrant/storage" qdrant/qdrant:latest
```

Upload and restore the snapshot via the HTTP API:

```bash
COLL=cwicr_vi  # one collection per locale: cwicr_vi, cwicr_za, cwicr_zh, ...
SNAPSHOT=VI_HANOI_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot

# 1. Create empty collection (config will be overwritten by the snapshot)
curl -X PUT "http://localhost:6333/collections/$COLL" \
  -H 'Content-Type: application/json' \
  -d '{"vectors": {}}'

# 2. Upload + recover
curl -X POST "http://localhost:6333/collections/$COLL/snapshots/upload?wait=true" \
  -F "snapshot=@$SNAPSHOT"
```

Or programmatically with `qdrant-client`:

```python
from qdrant_client import QdrantClient
client = QdrantClient(url="http://localhost:6333")
client.recover_snapshot(
    collection_name="cwicr_vi",
    location="file:///abs/path/to/VI_HANOI_..._BGEM3_V3_DDC_CWICR.snapshot",
)
```

## Hybrid search example

```python
from FlagEmbedding import BGEM3FlagModel
from qdrant_client import QdrantClient, models

model = BGEM3FlagModel("BAAI/bge-m3", use_fp16=True)
qdrant = QdrantClient(url="http://localhost:6333")

query = "máy đào 15 m³"   # Vietnamese: "15 m³ excavator"
enc = model.encode([query], return_dense=True, return_sparse=True)
q_dense = enc["dense_vecs"][0].tolist()
q_sparse = enc["lexical_weights"][0]

hits = qdrant.query_points(
    collection_name="cwicr_vi",
    prefetch=[
        models.Prefetch(query=q_dense, using="dense", limit=100),
        models.Prefetch(
            query=models.SparseVector(
                indices=[int(i) for i in q_sparse.keys()],
                values=list(q_sparse.values()),
            ),
            using="sparse",
            limit=100,
        ),
    ],
    query=models.FusionQuery(fusion=models.Fusion.RRF),
    limit=10,
    with_payload=True,
)
for p in hits.points:
    print(p.score, p.payload["rate_code"], p.payload.get("collection_name"))
```

For BIM-element matching, queries are typically built from IFC entity properties (type, dimensions, material). Add a third prefetch over the `resources` named vector when the query is best matched by machinery/material lists rather than rate titles.

## Languages and locales

23 distinct human languages across 30 locale-specific rate books (some languages cover multiple countries with locale-specific pricing and classification, e.g. EN-CA / EN-GB / EN-US / EN-AU / EN-NZ / EN-NG / EN-ZA, ES-ES / ES-MX, PT-BR). Each locale uses its own native-language collection structure (Russian СНиП codes, German DIN, US MasterFormat / RSMeans-style classifiers, etc.), preserved verbatim in the payload.

## Related artifacts

- **Tabular source** (parquet + catalogues + per-country PDFs) — used to build these snapshots and recommended for any work that needs raw numeric data:  
  → [`DataDrivenConstruction/cwicr-construction-rates`](https://huggingface.co/datasets/DataDrivenConstruction/cwicr-construction-rates)
- **OpenConstructionERP** — open-source ERP that consumes these snapshots in production:  
  → [`github.com/datadrivenconstruction/OpenConstructionERP`](https://github.com/datadrivenconstruction/OpenConstructionERP)
- **Source code / pipelines** (encoders, classifiers, search demos, BIM matchers):  
  → [`github.com/datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR`](https://github.com/datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR)

## Support the project ⭐

If this dataset is useful to you — or if you'd like to see more open construction databases like it — the most helpful thing you can do is **leave a star on the [OpenConstructionERP repository](https://github.com/datadrivenconstruction/OpenConstructionERP)**. Stars are how we gauge demand and prioritise the next country / language / source to publish. No account needed beyond GitHub, no signup, no money — just a one-click thank-you that directly steers what gets built next.

## License

Snapshots are released under **Apache-2.0**, matching the license of BGE-M3 and Qdrant. The upstream rate data is sourced from publicly available national/regional rate catalogues; license applicability of underlying rate codes follows each catalogue's terms of use.

## Citation

If you use these snapshots in academic work please cite the parent repository:

```
@software{cwicr_2026,
  author = {Boiko, Artem and DataDrivenConstruction},
  title  = {OpenConstructionEstimate — CWICR: Multilingual Construction Rates Vector Database},
  year   = {2026},
  url    = {https://github.com/datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR}
}
```

## Contact

- Source code & issue tracker: https://github.com/datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR
- Author: Artem Boiko (DataDrivenConstruction)
