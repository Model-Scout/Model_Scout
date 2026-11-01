---
pretty_name: JamoFlow Reproducibility Snapshot
language:
- ko
tags:
- korean
- byte-latent-language-models
- causal-patching
- inference-efficiency
- reproducibility
- negative-results
license: other
---

# JamoFlow reproducibility snapshot

This repository mirrors the public artifacts for:

> **Causal Whitespace Patching for Korean Byte-Latent Language Models: Quality-Preserving Latency and the Limits of Scale Amplification**  
> Gyeongchan Hwang · Priming Water · [ORCID 0009-0007-5840-3274](https://orcid.org/0009-0007-5840-3274)

Canonical code and release: [boaz-hwang/JamoFlow-reproducibility](https://github.com/boaz-hwang/JamoFlow-reproducibility) · [v0.1.0](https://github.com/boaz-hwang/JamoFlow-reproducibility/releases/tag/v0.1.0) · [Zenodo DOI 10.5281/zenodo.21973009](https://doi.org/10.5281/zenodo.21973009)

The arXiv cs.CL submission is awaiting first-submission category endorsement. Its identifier will be added here when assigned.

## What the study found

- At 19.6M parameters, the quality-matched whitespace policy reduced controlled end-to-end latency by 2.628% and strict-valid free-running latency by 2.531% relative to the C86 codepoint baseline.
- At 188.6M parameters, a quality-rescued W80 replication reduced controlled latency by 2.887% and free-running latency by 2.475%.
- The prespecified 10% target was not met, and the larger trained model did not amplify the percentage gain.

This is a bounded positive systems result plus a negative scale-amplification result. It is **not** a claim of a 10% speedup, a production-ready Korean LLM, a general-hardware result, or a useful pretrained checkpoint.

## Files

- `JamoFlow-paper.pdf`: named 9-page preprint
- `jamoflow-arxiv-source.tar.gz`: self-contained arXiv source bundle
- `jamoflow-reproducibility-v1.tar.gz`: curated source, tests, protocols, aggregate evidence, and paper materials
- `CITATION.cff`: citation metadata
- `SHA256SUMS`: integrity hashes

No raw corpus text, model checkpoints, record identifiers, raw generated outputs, or per-sequence loss arrays are included. No Hugging Face model weights are released because the experiments did not establish a useful pretrained model.

## Integrity

```text
393e25d4d204e3e805cba3505267a68508eaf55b2b40ba24795a637cb28f8b3c  JamoFlow-paper.pdf
ee94268cfc6f28853a7aca33249cede5b20622e565c2e875113d20a72d1eb5ba  jamoflow-arxiv-source.tar.gz
0f48cb350593843958754fa1cddf37b5dd15f642a8e5afdc7f7300681b5bb93b  jamoflow-reproducibility-v1.tar.gz
```

## License

The code and reproducibility materials are Apache-2.0. The paper is CC BY 4.0. Third-party works remain under their respective licenses.

## Citation

Until an arXiv identifier is assigned, cite the versioned public release:

```bibtex
@misc{hwang2026jamoflow,
  author       = {Gyeongchan Hwang},
  title        = {Causal Whitespace Patching for Korean Byte-Latent Language Models: Quality-Preserving Latency and the Limits of Scale Amplification},
  year         = {2026},
  month        = aug,
  howpublished = {GitHub release v0.1.0},
  url          = {https://github.com/boaz-hwang/JamoFlow-reproducibility/releases/tag/v0.1.0}
}
```
