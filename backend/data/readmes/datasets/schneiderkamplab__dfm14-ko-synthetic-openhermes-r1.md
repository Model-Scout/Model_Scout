---
language:
- ko
license: other
license_name: source-and-teacher-conditions
license_link: https://huggingface.co/datasets/schneiderkamplab/dfm14-ko-synthetic-openhermes-r1/blob/main/README.md#terms
configs:
- config_name: default
  data_files:
  - split: train
    path: data/*.parquet
---
# dfm14-ko-synthetic-openhermes-r1

Accepted-only DFM14 data, automatically reviewed with Gemma 4 26B-A4B. This is not human quality certification. Rejections, repair requests and failed reviews are excluded. Some early synthetic accepts predate the compact reviewer; their audit provenance is retained.

Rows: 6,270. All final assistant targets fit the native Gemma 4 template within 4,096 tokens, without truncation. Complete chat history is preserved. Training supervises the indicated final assistant.

Nested values are losslessly encoded in `messages_json`, `tools_json`, `provenance_json` and `audit_json` to avoid incompatible Arrow schemas for different tool signatures. Decode these with `json.loads`; pass messages and tools to the Gemma 4 chat template with `enable_thinking=False`. Do not train on the JSON serialization itself.

## Selection

Normalized exact benchmark-question checks and exact cross-addition chat deduplication were performed. These are not semantic or translated benchmark decontamination. Inherited DFM13 overlap is removed separately in mixture sampling, not claimed absent from this standalone dataset.

## Terms

Upstream attribution, source revision and document/row references are retained in provenance. Source terms and applicable Gemma generated-output conditions remain in force; this release does not relicense third-party material under one blanket permissive license. Consult the referenced upstream sources.

Sources: generated; see row provenance

## Upstream attribution attachments

`metadata/upstream-attribution.jsonl.gz` preserves the original local attribution documents referenced by row provenance, including available OPUS README and license texts. Entries map the original path to its content and SHA-256.
