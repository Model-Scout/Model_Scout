---
pretty_name: FineWeb2 Multilingual CLT Entropy Evaluation Data
language:
- ar
- zh
- ja
- ko
task_categories:
- text-generation
size_categories:
- 1M<n<10M
---

# FineWeb2 multilingual CLT entropy evaluation data

This dataset contains held-out token sequences used to measure multilingual
feature entropy for `CausalNLP/multilingual_gpt2-clt-ar-zh-ko-ja`.

## Construction

- Source: `HuggingFaceFW/fineweb-2`
- Source revision: `af9c13333eb981300149d5ca60a8e9d659b276b9`
- Tokenizer: `CausalNLP/gpt2-ar-zh-ko-ja-120k`
- Languages/configurations: `arb_Arab`, `cmn_Hani`, `jpn_Jpan`, `kor_Hang`
- The first 200,000,000 tokenizer tokens of each language were skipped.
- The following 1,000,000 tokens per language were retained.
- Each row contains one complete 16-token sequence.
- There are 62,500 rows per language and 4,000,000 retained tokens in total.

The Parquet files contain `input_ids`, `language`, `source_id`, and
`document_token_start`. See `manifest.json` and the per-language manifests for
the exact construction parameters and source-stream counts.

This dataset preserves token IDs rather than decoded text so that the entropy
evaluation is reproducible with the exact tokenizer used for the CLT.

