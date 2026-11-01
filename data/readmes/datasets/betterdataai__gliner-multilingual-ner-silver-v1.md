---
pretty_name: "Betterdata Annotated Multilingual NER/PII"
language:
  - zh
  - nl
  - en
  - fr
  - de
  - id
  - it
  - ja
  - ko
  - es
  - sv
  - vi
license: apache-2.0
task_categories:
  - token-classification
tags:
  - ner
  - pii
  - phi
  - pci
  - gliner
size_categories:
  - 100K-1M
---

# Betterdata Annotated Multilingual NER/PII

## Dataset Summary
This dataset contains multilingual, annotated NER/PII spans across 13 languages with 60+ label classes spanning PII, PHI, PCI, and general entity types. It is designed to train and evaluate privacy-preserving NER models.

## Data Sources
- bloomberg_financial_news_annotated (data/augmented/bloomberg_financial_news_annotated.jsonl)
- c4_multilingual_annotated (data/augmented/c4_multilingual_annotated.jsonl)
- finewiki_annotated (data/augmented/finewiki_annotated.jsonl)
- pleias_sec_annotated (data/augmented/pleias_sec_annotated.jsonl)
- pubmed_common_pile_annotated (data/augmented/pubmed_common_pile_annotated.jsonl)
- pubmed_medrag_annotated (data/augmented/pubmed_medrag_annotated.jsonl)
- wiki40b_annotated (data/augmented/wiki40b_annotated.jsonl)
- wikiann_annotated (data/augmented/wikiann_annotated.jsonl)
- wikipedia_annotated (data/augmented/wikipedia_annotated.jsonl)
- wikisource_annotated (data/augmented/wikisource_annotated.jsonl)

## Annotation Notes
- LLMs are instructed for high recall, so some noise is expected.
- Entities must appear verbatim in text; out-of-schema labels are discarded.
- Outputs are normalized into GLiNER token-span format for training.

## Label Schema
See `label_schema.json` for the full list of labels, categories, and descriptions.

## Statistics
- Total records: 387736
- Total entities: 756419
- Train/Validation/Test: 348958 / 19382 / 19396
- Label coverage: 84 / 88
- Languages: Chinese, Dutch, English, French, German, Indonesian, Italian, Japanese, Korean, Spanish, Swedish, Vietnamese

## Intended Use
Training and evaluation for multilingual NER/PII detection and redaction.

## Limitations
- LLM-annotated data may contain noise.
- Coverage varies by language and domain.
- Some labels are sparse and may require additional sampling.

## License
Apache-2.0. Verify that source corpus licenses are compatible before redistribution.

## Citation
If you use this dataset, cite the accompanying dataset card and release date: 2026-02-12.