---
license: cc-by-4.0
language:
  - en
  - zh
  - ru
  - ja
  - ko
  - ar
  - hi
  - es
size_categories:
  - n<1K
task_categories:
  - text-generation
  - text-classification
  - feature-extraction
tags:
  - spectral-brand-theory
  - exp-cross-language
  - r15
  - brand-perception
  - cross-language
  - measurement-invariance
  - dimensional-semantics
  - llm-as-respondent
  - metameric-observers
pretty_name: "Experiment B: Cross-Language Semantic Drift in Brand Perception Dimensions (R15)"
configs:
  - config_name: default
    data_files:
      - split: train
        path: data/exp_cross_language.jsonl
citation: |
  @article{zharnikov2026v,
    author = {Dmitry Zharnikov},
    title = {Dimensional Collapse in AI-Mediated Brand Perception: Large Language Models as Metameric Observers},
    journal = {Working Paper, Zenodo},
    year = {2026},
    doi = {10.5281/zenodo.19422427}
  }
doi: 10.57967/hf/8439
paperswithcode_id: null
---

# Experiment B: Cross-Language Semantic Drift in Brand Perception Dimensions

**Dataset DOI**: [10.57967/hf/8439](https://doi.org/10.57967/hf/8439)
**Companion Paper (R15, 2026v)**: [10.5281/zenodo.19422427](https://doi.org/10.5281/zenodo.19422427) -- "Dimensional Collapse in AI-Mediated Brand Perception: Large Language Models as Metameric Observers"
**Companion GitHub mirror**: [spectralbranding/sbt-papers](https://github.com/spectralbranding/sbt-papers)
**Citation Key**: Zharnikov (2026v)
**Author ORCID**: [0009-0000-6893-9231](https://orcid.org/0009-0000-6893-9231)
**Paper Section**: 5.14 (Cross-Language Dimensional Semantics)

## Dataset Summary

This dataset tests whether the eight perception dimensions of Spectral Brand Theory (SBT) carry the same meaning across languages when presented to large language models as respondents. It contains 441 valid parsed records (98.0% of 450 total API calls) spanning 8 languages, 5 focal brands, 3 LLMs, and 2 label conditions (bilingual vs native-only), with Latin-square balanced dimension ordering and 2 repetitions per cell. The experiment provides Section 5.14 evidence for the companion paper's argument that LLM observers exhibit configural measurement invariance across languages but mask culturally specific semantic scope, particularly along the Experiential dimension.

Companion paper: ["Dimensional Collapse in AI-Mediated Brand Perception: Large Language Models as Metameric Observers"](https://doi.org/10.5281/zenodo.19422427) (Zharnikov, 2026v).
Companion GitHub repository: https://github.com/spectralbranding/sbt-papers -- analysis code, prompts, and reproduction pipeline (R15 paper slice).

## Languages

Eight languages are covered, all under ISO 639-1 codes: English (`en`), Chinese (`zh`), Russian (`ru`), Japanese (`ja`), Korean (`ko`), Arabic (`ar`), Hindi (`hi`), and Spanish (`es`). English serves both as the experimental anchor (bilingual condition) and as a comparison surface for the seven non-English native-only conditions. Native-language dimension labels were fully translated per fleet discipline (no mixed-language prompts); the per-record `dimension_labels` field captures the exact translated tokens used for each call.

## Dataset Structure

### Experiment Design

| Parameter | Value |
|-----------|-------|
| Languages | 8 (en, zh, ru, ja, ko, ar, hi, es) |
| Focal brands | 5 (Hermes, IKEA, Patagonia, Erewhon, Tesla) |
| Models | 3 (Claude Haiku 4.5, GPT-4o-mini, Gemini 2.5 Flash) |
| Label conditions | 2 (bilingual: native + English anchor; native_only: no English anchor) |
| Repetitions | 2 |
| Dimension ordering | Latin-square balanced across the 8 SBT dimensions |
| Total API calls | 450 |
| Valid parsed records | 441 (98.0%) |
| Cost | USD .26 |

### Data Fields

| Field | Type | Description |
|-------|------|-------------|
| `timestamp` | string | ISO timestamp of API call |
| `experiment` | string | "B_cross_language" |
| `model_id` | string | Full model identifier |
| `model_provider` | string | API provider for the model |
| `temperature` | float | Sampling temperature |
| `top_p` | float | Nucleus sampling parameter |
| `max_tokens` | int | Token cap |
| `system_prompt` | string | Full system prompt text |
| `system_prompt_hash` | string | SHA-256 of system prompt |
| `user_prompt` | string | Full user prompt text |
| `user_prompt_hash` | string | SHA-256 of user prompt |
| `brand` | string | Focal brand name (Hermes, IKEA, Patagonia, Erewhon, Tesla) |
| `condition` | string | `bilingual` or `native_only` |
| `repetition` | int | Repetition index (1--2) |
| `language` | string | ISO 639-1 language code |
| `dimension_labels` | object | Native translations used for each SBT dimension |
| `dimension_order` | array | Latin-square ordering used for the 8 dimensions |
| `raw_response` | string | Verbatim model reply |
| `parsed_weights` | object | 8-dimension weight allocation (sum approximately 100) |
| `weights_valid` | bool | Parser flag |
| `weight_sum_raw` | float | Pre-normalisation weight sum |
| `response_time_ms` | int | Response latency in milliseconds |
| `token_count_input` | int | Prompt tokens |
| `token_count_output` | int | Completion tokens |
| `api_cost_usd` | float | Per-call API cost |
| `model` | string | Short model label |
| `prompt_type` | string | Prompt template tag |
| `prompt` | string | Composite prompt as rendered |

### Data Splits

| Split | Size | Contents |
|-------|------|----------|
| train | 441 | All valid parsed records (one row per language x brand x model x condition x repetition cell) |

### Source Data

**Curation Rationale**: To empirically test whether SBT's 8 perception dimensions hold their meaning across languages when LLMs are used as respondents -- specifically (H1) configural invariance under bilingual anchoring; (H2) drift magnitudes when English anchors are removed; (H3) culturally predicted dimension-specific shifts; and (H4) collectivist amplification of the Social dimension.

**Source**: Generated via API calls to three LLMs (Claude Haiku 4.5, GPT-4o-mini, Gemini 2.5 Flash) in May 2026. Prompts rendered from a shared spine template across 8 languages and 2 label conditions, with fully translated native-language dimension labels.

**Collection Process**: Each (language, brand, model, condition, repetition) cell elicits a 100-point allocation across the 8 SBT dimensions: Semiotic, Narrative, Ideological, Experiential, Social, Economic, Cultural, Temporal. Dimension ordering is Latin-square balanced across calls to absorb primacy effects. The `bilingual` condition presents each dimension as native + English anchor; the `native_only` condition removes the English anchor.

**Annotation**: All weight allocations are LLM-generated; there is no human annotation layer. Models are the annotators.

### Key Findings

| ID | Hypothesis | Status | Effect |
|----|-----------|--------|--------|
| H1 | Configural invariance under bilingual anchoring | SUPPORTED | Median cross-language cosine = .992 (min .966) |
| H2 | Native-only drift in non-English languages | NOT SUPPORTED | 0/7 languages significant; magnitudes .73 to 1.71 pp |
| H3 | Dimension-specific cultural drift (Arabic Ideological, Japanese Cultural, Hindi Social) | NOT SUPPORTED | Arabic Ideological +1.38 pp (d = .285); not significant |
| H4 | Collectivist Social amplification | NOT SUPPORTED | d = .009, p = .956 |

**Exploratory finding**: When English anchors are removed, all seven non-English languages exhibit Experiential weight deflation (-2.0 to -4.5 pp) with compensating inflation in Economic and Narrative. The English word "Experiential" carries broader semantic scope than its native equivalents across Chinese, Russian, Japanese, Korean, Arabic, Hindi, and Spanish, identifying this dimension as the most measurement-fragile cross-linguistically.

## Citation

If you build on this dataset, please cite the companion paper:

> Dmitry Zharnikov (2026). "Dimensional Collapse in AI-Mediated Brand Perception: Large Language Models as Metameric Observers." Working Paper. DOI [10.5281/zenodo.19422427](https://doi.org/10.5281/zenodo.19422427).

HF dataset DOI: [10.57967/hf/8439](https://doi.org/10.57967/hf/8439).

Companion GitHub mirror: https://github.com/spectralbranding/sbt-papers

```bibtex
@article{zharnikov2026v,
  author = {Zharnikov, Dmitry},
  title  = {Dimensional Collapse in {AI}-Mediated Brand Perception: Large Language Models as Metameric Observers},
  year   = {2026},
  journal = {Working Paper},
  doi    = {10.5281/zenodo.19422427}
}
```

## Licence

Data licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) -- you may share and adapt with attribution to the author and citation of the concept DOI above. The `license: cc-by-4.0` declaration in this README frontmatter is the canonical licence statement for this Hub-side artifact.

Companion code lives in the GitHub mirror under MIT licence; see https://github.com/spectralbranding/sbt-papers/blob/main/LICENSE.

## Discipline + Reproducibility

This dataset was generated by structured LLM-API experiments. Reproducibility relies on:

- **Cross-extractor discipline**: weight allocations parsed from each model's raw response via deterministic regex on the 8-dimension reply format; no LLM was used as a downstream extractor on its own output. Per-call `raw_response`, `parsed_weights`, and `weights_valid` fields are preserved so the parser can be re-run and audited.
- **LLM-call JSONL logs**: each API call is captured as one JSONL record with operator-grade fields (model_id, model_provider, temperature, top_p, max_tokens, full system + user prompts, prompt hashes, response, tokens in/out, latency, USD cost). The full call log is the published dataset at `data/exp_cross_language.jsonl`; aggregate analysis lives at `analysis/exp_cross_language_results.json` and `analysis/exp_cross_language_summary.md`.
- **Prompt-purity protocol**: the same spine template renders prompts across all 8 languages and 2 conditions. Native-language dimension labels are fully translated (no mixed-language prompts); per-record `dimension_labels` captures the exact translated tokens used. SHA-256 hashes of system and user prompts (`system_prompt_hash`, `user_prompt_hash`) enable prompt-set audit.
- **Operator separation**: the three respondent models span three vendors (Anthropic, OpenAI, Google), and the parser is a deterministic regex run by the analysis pipeline -- no single vendor mediates both response and parse.
- **Latin-square balancing**: dimension ordering is balanced via Latin-square design across cells to absorb primacy effects.
- **Reproduction recipe**: clone the companion GitHub mirror (https://github.com/spectralbranding/sbt-papers), navigate to the R15 paper slice, and follow its reproduction pipeline; running the analysis on this dataset's `data/exp_cross_language.jsonl` regenerates `analysis/exp_cross_language_results.json` and `analysis/exp_cross_language_summary.md`.

## Related Datasets

- [spectralbranding/r15-ai-search-metamerism](https://huggingface.co/datasets/spectralbranding/r15-ai-search-metamerism) -- baseline dimensional collapse dataset (R15)
- [spectralbranding/meaningfulness-cross-language-rendering](https://huggingface.co/datasets/spectralbranding/meaningfulness-cross-language-rendering) -- cross-language rendering at the meaning layer (Paper B 2026ap)

---

