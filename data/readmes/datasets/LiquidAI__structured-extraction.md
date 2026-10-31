---
license: other
language: [en, ar, zh, fr, de, it, ja, ko, pt, es, pl, vi, th, id, hi, ru]
task_categories: [text-generation]
tags: [information-extraction, structured-output, json, json-schema, synthetic, multilingual]
size_categories: [1K<n<10K]
configs:
  - config_name: default
    data_files:
      - {split: train, path: train.parquet}
      - {split: test, path: test.parquet}
      - {split: test_unseen, path: test_unseen.parquet}
      - {split: showcase, path: showcase.parquet}
---
# Structured Extraction

> [!Note]
> 📓 **Tutorial**: This is the dataset used in [SFT with TRL](https://colab.research.google.com/github/Liquid4All/cookbook/blob/main/finetuning/notebooks/lfm3_sft_with_trl.ipynb)

Documents paired with a JSON Schema and the JSON object extracted from them. The documents (emails, receipts, bookings, forms, letters, listings, ...) cover 35 document types in 16 languages. All people, companies, addresses and identifiers are fictional.

## Splits

| Split | Rows | Content |
|---|---:|---|
| `train` | 6,000 | 30 document types |
| `test` | 500 | the same 30 document types, other documents |
| `test_unseen` | 300 | 5 document types that are not in `train` |
| `showcase` | 6 | examples of the 5 unseen document types |

## Fields

| Field | Description |
|---|---|
| `id` | row identifier |
| `doc_type` | document type |
| `language` | ISO 639-1 code of the document |
| `schema` | JSON Schema of the target object, as a JSON string |
| `document` | document text |
| `extraction` | target object, keys in schema order, as a JSON string |

## Conventions

- Strings are copied from the document as written, without field labels or honorifics.
- Dates are `YYYY-MM-DD`, times `HH:MM` (24-hour), amounts are JSON numbers, and currencies are ISO 4217 codes.
- Information absent from the document is `null` (`[]` for arrays).
- When the document contains several candidate values, the field description says which one to extract.
