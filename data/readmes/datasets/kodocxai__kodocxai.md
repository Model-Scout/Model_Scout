---
license: cc-by-4.0
language:
  - ko
task_categories:
  - token-classification
tags:
  - explainable-ai
  - key-information-extraction
  - document-understanding
  - korean
  - benchmark
pretty_name: KoDocXAI benchmark v1.0
size_categories:
  - n<1K
---

# KoDocXAI benchmark v1.0 - public annotation layer

Annotation layer of the **KoDocXAI** benchmark: 300 Korean
permit-and-authorization dispatch documents annotated with value spans for
five KIE fields (title, recipient, document number, issuance date, issuing
authority), plus 60 documents independently double-annotated for
inter-annotator agreement. It accompanies the paper *KoDocXAI: A Quantitative
Evaluation Framework and Benchmark for Explainability in Key Information
Extraction from Korean Administrative Form Documents* (Applied Sciences, revised
version under review; citation will be updated upon publication).

**This dataset contains no AI-Hub source content** - no images, no transcribed
text, no coordinates. Records hold only document identifiers, field types,
status labels, integer annotation-ID index spans, label-file paths, and
integrity hashes. To reconstruct the benchmark you must download the source
dataset yourself from [AI-Hub](https://www.aihub.or.kr) (공공행정문서 OCR,
dataSetSn=88; applications are currently limited to residents of the Republic
of Korea) and run the deterministic reassembly script from the
[GitHub repository](https://github.com/kodocxai/kodocxai), which also carries
the record-format specification (`annotations/FORMAT.md`), the evaluation
toolkit (MIT), the annotation guideline, and the qualitative-layer rubric.
Archived at Zenodo: DOI
[10.5281/zenodo.21964543](https://doi.org/10.5281/zenodo.21964543).

## Files

| File | Records | Content |
|---|---|---|
| `kodocxai_v1.0.jsonl` | 300 | Primary annotation (annotator A1) |
| `kodocxai_v1.0_double.jsonl` | 60 | Independent double annotation (annotator A2) |
| `manifest_public.json` | - | SHA-256 hashes, record counts, sample strata, fixed seed strings |

## Attribution (required by the source-data provider)

This research (paper) used datasets from 'The Open AI Dataset Project (AI-Hub,
S. Korea)'. All data information can be accessed through 'AI-Hub
(www.aihub.or.kr)'.

## License

The annotation layer is released under CC BY 4.0. The AI-Hub source dataset
remains subject to its own terms of use and is not redistributed here.
