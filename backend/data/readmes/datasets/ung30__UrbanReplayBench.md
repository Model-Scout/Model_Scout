---
pretty_name: UrbanReplayBench
language:
- ko
license: other
task_categories:
- question-answering
tags:
- urban-computing
- text-to-sql
- graph-rag
- event-time
- fault-injection
size_categories:
- 10K<n<100K
---

# UrbanReplayBench

[![Dataset DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22042153.svg)](https://doi.org/10.5281/zenodo.22042153)
[![Software DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22040929.svg)](https://doi.org/10.5281/zenodo.22040929)

Public release containing the event/cutoff subset used in the IEEE BigData 2026 manuscript. The exact paper snapshot is pinned at Hugging Face revision `ce5fc2a2d5fa107b2732d727335562ccd106d6f4` and archived as Zenodo Dataset DOI [10.5281/zenodo.22042153](https://doi.org/10.5281/zenodo.22042153). The accompanying source artifact is archived as Software DOI [10.5281/zenodo.22040929](https://doi.org/10.5281/zenodo.22040929).

## Contents

- 23 event cases and 68 replay cutoffs.
- De-identified relational replay tables in `data/replay/*.parquet`.
- Cutoff-safe City2Graph inputs in `data/spatial/road_links.parquet`.
- Benchmark contracts, opaque source-signal keys, fault manifests, receipts, seals, and machine-readable reports.
- Microsoft GraphRAG corpus/version manifests; generated indexes and policy-document full text are not included.
- Sanitized collection and evaluation source code: [AWUNG27/UrbanReplayBench](https://github.com/AWUNG27/UrbanReplayBench).

## De-identification

Free-text news, accident descriptions, event details, writer names, addresses, URLs, ingestion metadata, and internal row keys are excluded. Signal and row identifiers needed for distinct counts are replaced with stable SHA-256 keys. Public place names and road geometry are retained because they are required to reconstruct the urban replay tasks.

## Temporal contract

Every released row satisfies `observed_at <= cutoff` and `published_at <= cutoff`. The historical column names are preserved, but their operational meaning is explicitly bounded by the released collector implementation:

- `observed_at` is a normalized observation-time proxy computed as `floor_5min(collection_time - 15 minutes)`, not an authoritative source-event timestamp supplied by every domain.
- `published_at` is the collector-side availability timestamp captured when the API response is fetched, not a claim about the Seoul source system's unobserved internal publication time.

The benchmark therefore evaluates availability to the collection system at a replay cutoff under this declared normalization rule. Times are Unix milliseconds represented as strings in Parquet to preserve historical values. Payload columns are also stored as nullable strings; evaluators perform task-specific numeric casting.

## License

`license: other` is deliberate because the observed data retain their source-specific Korean Open Government License terms. The relational and road-link observations originate from **Seoul Real-time City Data (OA-21285), © Seoul Metropolitan Government**, offered under **Korea Open Government License Type 1 (attribution; commercial use and modification permitted)**. This release filters historical event cutoffs, removes free text and direct/internal identifiers, pseudonymizes count keys, and converts the result to Parquet. Policy-document full text is not redistributed; only research-generated source/version metadata, public URLs, and hashes are included. See `LICENSE_AUDIT.md`.

## Reproducibility boundary

The released road-link cutoff snapshots allow City2Graph input reconstruction without the localhost database. The package supports result/seal audit and the leakage-free certificate rerun. Sanitized source for the poller, Avro/Kafka transport, PostgreSQL sinks, schemas, and DDL is available in the linked GitHub repository. A live ingestion rerun still requires external credentials and services and is not required to reproduce the paper's sealed results. The artifact does not claim to reproduce free-form GraphRAG answer quality.
