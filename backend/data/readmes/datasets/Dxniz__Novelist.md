---
license: apache-2.0
language:
- en
- tr
- fr
- de
- es
- pt
- it
- ru
- zh
- ja
- ko
- ar
- hi
- nl
- pl
- sv
- uk
- cs
- ro
- hu
- el
- vi
- id
- fa
- da
- 'no'
- sk
- sr
- bg
pretty_name: Novelist
task_categories:
- text-generation
- translation
tags:
- creative-writing
- narrative-reasoning
- long-form-fiction
- chain-of-thought
- multilingual
- synthetic-data
size_categories:
- 10K<n<100K
dataset_info:
  features:
  - name: row_id
    dtype: string
  - name: language_code
    dtype: string
  - name: record_type
    dtype: string
  - name: record_id
    dtype: string
  - name: story_id
    dtype: string
  - name: book_id
    dtype: string
  - name: item_id
    dtype: string
  - name: story_type
    dtype: string
  - name: genre
    dtype: string
  - name: genre_family
    dtype: string
  - name: phase
    dtype: string
  - name: prompt_type
    dtype: string
  - name: profile
    dtype: string
  - name: mode
    dtype: string
  - name: author_style
    dtype: string
  - name: talking_style
    dtype: string
  - name: theme_anchor
    dtype: string
  - name: tone
    dtype: string
  - name: pov
    dtype: string
  - name: chapter
    dtype: int64
  - name: scene_number
    dtype: int64
  - name: chapter_count
    dtype: int64
  - name: chapter_titles
    sequence: string
  - name: mini
    dtype: string
  - name: thinker
    dtype: string
  - name: overthinker
    dtype: string
  - name: ultra
    dtype: string
  - name: max
    dtype: string
  - name: quality_overall_score
    dtype: float64
  - name: quality_accepted
    dtype: bool
  - name: text
    dtype: string
  - name: answer_text
    dtype: string
  - name: reasoning_text
    dtype: string
  - name: update_text
    dtype: string
  - name: metadata_json
    dtype: string
  - name: quality_json
    dtype: string
  - name: text_word_count
    dtype: int64
  - name: tags
    sequence: string
---

# Dataset Card for Novelist

## Dataset Summary

Novelist is a synthetic creative-writing and narrative-reasoning dataset designed for long-context fiction systems, scene planners, continuity-aware story models, multilingual literary translation, and child-safe TinyStories generation. The dataset mixes direct prose, explicit reasoning traces, quality-only judge outputs, full-book artifacts, and multilingual translation outputs inside a single narrative training ecosystem.

This measured snapshot was built from **186,603 raw source records** across **49 source streams**. After a high-fidelity normalization pass—which deduplicates and groups multiple reasoning modes (mini, thinker, overthinker, ultra, max) into consolidated multi-reasoning rows, the final dataset contains **86,571 high-quality rows**.

The primary reason for the reduction in row count is the **5-to-1 merging** of reasoning traces. For each narrative scene that completed all five thinking tiers, five individual source records are collapsed into a single multi-reasoning record, ensuring that a single model can learn from a complete spectrum of thinking density at once.

Current snapshot highlights:

- **~243M total words**
- **~354M tokens** measured with `cl100k_base`
- **12,047 complete multi-reasoning story scenes**
- **11,753 unique scene-level story IDs**
- **3,339 unique book IDs**
- **61,015 total book chapters**
- **Strong representation across 28+ languages**

Coverage in the current snapshot is broad:

- Every measured row contains text and answer-bearing content.
- **30.1%** of rows also preserve an explicit reasoning field.
- Long-form books account for only **3.86%** of records, but **56.8%** of all measured words.
- The longest single record contains **224,112 words**.
- The longest preserved reasoning trace contains **15,774 words**.

The dataset is primarily intended for:

- long-form fiction continuation
- scene planning and narrative state tracking
- narrative chain-of-thought supervision
- multilingual literary translation
- child-safe multilingual story generation
- fiction quality ranking and judge alignment

**Warning!** Do not forget to exclude story_quality record_type because they can only be useful on filtering!

## Languages

The broader production stack supports **28 languages** for multilingual translation and multilingual TinyStories generation. The measured snapshot is heavily English-dominant, but it also includes explicitly labeled multilingual rows and translated outputs.

### Measured Language Labels

| Language label | Records | Share of all rows |
| --- | ---: | ---: |
| English | 60,958 | 70.41% |
| Indonesian | 986 | 1.14% |
| Ukrainian | 980 | 1.13% |
| Bulgarian | 977 | 1.13% |
| Danish | 975 | 1.13% |
| Serbian | 975 | 1.13% |
| Greek | 974 | 1.13% |
| Slovak | 974 | 1.13% |
| Romanian | 972 | 1.12% |
| Persian | 968 | 1.12% |
| Hungarian | 967 | 1.12% |
| Vietnamese | 967 | 1.12% |
| Norwegian | 966 | 1.12% |
| Czech | 958 | 1.11% |
| Korean | 834 | 0.96% |
| Dutch | 833 | 0.96% |
| Polish | 832 | 0.96% |
| Spanish | 829 | 0.96% |
| Turkish | 829 | 0.96% |
| German | 828 | 0.96% |
| Hindi | 827 | 0.96% |
| Chinese | 826 | 0.95% |
| French | 825 | 0.95% |
| Portuguese | 819 | 0.95% |
| Arabic | 818 | 0.94% |
| Italian | 818 | 0.94% |
| Japanese | 816 | 0.94% |
| Swedish | 816 | 0.94% |
| Russian | 814 | 0.94% |

Important note: English is also used as the fallback label when language metadata is absent in English-first creative-writing rows. The multilingual TinyStories and translation pipelines themselves are configured for 28 supported languages, even though only the languages above appear in the top measured distribution for this snapshot.

## Dataset Structure

### High-Level Record Scope Breakdown

| Record scope | Rows | Share of rows |
| --- | ---: | ---: |
| Story scenes (Base/Reasoned/Multi) | 48,201 | 55.68% |
| Tiny stories | 15,688 | 18.12% |
| Translations | 9,925 | 11.46% |
| Quality-only text records | 6,992 | 8.08% |
| Full books | 3,341 | 3.86% |
| Standalone Reasoning items | 2,424 | 2.80% |

Full book pipeline is: Create book metadata > Create CoT with batches (5 chapters in 1 batch.) > Judge combined CoT > Write chapters according to the CoT. > Judge chapter

This structure matters: the corpus is not only prose. It is a mixed supervision environment where reasoning, scene writing, translation, long-form assembly, and explicit quality artifacts are all represented.

### Conceptual Source Group Breakdown

The dataset contains multiple production families that were grouped into conceptual source groups to avoid exposing implementation-specific filenames.

| Record type | Rows | Share of rows |
| --- | ---: | ---: |
| `story_scene` | 27,994 | 32.34% |
| `tiny_story` | 15,688 | 18.12% |
| `multi_reasoning_story_scene` | 12,047 | 13.92% |
| `translation` | 9,925 | 11.46% |
| `reasoned_story_scene` | 8,160 | 9.43% |
| `story_quality` | 6,992 | 8.08% |
| `full_book` | 3,341 | 3.86% |
| `reasoning_item` | 2,424 | 2.80% |

This grouped view shows that the corpus is intentionally balanced across both prose-first and reasoning-first supervision, with a particularly large investment in explicit thinking traces and long-form book-scale artifacts.

### Full-Book Subset

The long-form book subset is one of the defining characteristics of Novelist.

| Metric | Value |
| --- | ---: |
| Unique Books | 3,339 |
| Total chapters | 61,015 |
| Average chapters per book | 18.27 |
| Total book story words | 137,977,467 |
| Total book story tokens | 182,380,727 |
| Total preserved book reasoning words | 5,540,615 |
| Total preserved book reasoning tokens | 7,659,070 |
| Average story words per book | 41,322.99 |
| Average reasoning words per book | 1,659.36 |

The long-form segment is split between a standard book subset and a much longer book subset. The longer book subset alone contributes **37,263,111 words**, which is **10.15%** of all measured corpus words despite representing only **262** records.

The snapshot also includes a highly curated Turkish long-form artifact with:

- **70 chapters**
- **148,435 story words**
- **10.0 planner average judge score**
- **10.0 writer average judge score**

## Story and Genre Distribution

### Story Type Distribution

| Story type | Rows | Share of all rows |
| --- | ---: | ---: |
| Unclassified | 15,691 | 18.12% |
| academy_fracture | 9,163 | 10.58% |
| forbidden_bond | 9,081 | 10.49% |
| diaspora_ledger | 9,044 | 10.45% |
| heist_chain | 9,035 | 10.44% |
| expedition_fallout | 8,964 | 10.35% |
| court_intrigue | 8,622 | 9.96% |
| frontier_breakdown | 8,547 | 9.87% |
| urban_noir | 8,424 | 9.73% |

These story-type clusters indicate a deliberate emphasis on recurring high-pressure fiction templates rather than generic prompt soup. The dataset repeatedly returns to interpersonal fracture, class and institutional pressure, crew betrayal, legal or political tension, expedition failure, and romantic or social constraint.

### Genre Distribution

| Genre | Rows | Share of all rows |
| --- | ---: | ---: |
| Unclassified | 40,084 | 46.30% |
| international family thriller | 1,182 | 1.37% |
| criminal ensemble drama | 1,145 | 1.32% |
| city mystery | 1,129 | 1.30% |
| romantic caper under pressure | 1,116 | 1.29% |
| domestic political suspense | 1,103 | 1.27% |
| betrayal-driven crew thriller | 1,089 | 1.26% |
| expedition drama | 1,080 | 1.25% |
| campus thriller | 1,033 | 1.19% |
| political romance | 1,032 | 1.19% |
| elite institution collapse drama | 1,021 | 1.18% |
| inheritance pressure drama | 1,015 | 1.17% |
| scientific mystery | 1,013 | 1.17% |
| class pressure romance | 1,012 | 1.17% |
| coming-of-power drama | 1,010 | 1.17% |

The large unclassified genre mass reflects the fact that some production lines encode story identity more strongly through story-type, scene state, or theme anchors than through a single flat genre string.

## Quality, Judge Usage, and Acceptance Gates

Novelist is not a single-pass corpus. It is a judge-mediated fiction dataset.

### Judge-Based Generation Stack

The measured production stack contains **28 producer programs**, spanning:

- **6 creative profiles**: standard, uncensored, agentic, style-influence, character-driven, and worldbuilding
- **5 explicit reasoning modes**: mini, thinker, overthinker, ultra, and max

Judge usage is built into the major production families:

- **Scene-generation pipelines** generate explicit reasons, write the scene, and gate acceptance with quality review. Default thresholds are **8.0** for standard, uncensored, agentic, and style-influence production, and **9.0** for character-driven and worldbuilding production.
- **Long-form book pipelines** use a two-layer judge system: a planner judge for chapter-plan batches and a writer judge for completed chapters. Both default to **9.0** thresholds.
- **Translation pipelines** judge accuracy, completeness, pacing preservation, character preservation, fluency, terminology, and formatting, with a default threshold of **8.0**.
- **TinyStories pipelines** gate both the source story and every translation with a judge, using a default threshold of **9.0**.
- **Quality-only textual records** preserve explicit acceptance flags from downstream scoring passes.

Across these systems, judge feedback is not decorative. Weaknesses and summaries are fed back into retries, so rejection changes the next generation attempt rather than simply logging failure.

### Explicit Quality Coverage in the Current Snapshot

The normalized snapshot currently contains **20,151 rows** with explicit quality or acceptance metadata.

| Metric | Value |
| --- | ---: |
| Rows with quality or acceptance metadata | 20,151 |
| Rows with explicit acceptance flags | 20,151 |
| Accepted rows | 19,708 |
| Acceptance rate among rows with explicit acceptance flags | 97.80% |
| Rows with numeric overall scores | 9,922 |
| Average overall score among numeric-score rows | 9.3134 |
| Rows with overall score >= 9.0 | 9,197 |
| Share of numeric-score rows with overall score >= 9.0 | 92.69% |
| Rows with overall score >= 8.0 | 9,922 |
| Share of numeric-score rows with overall score >= 8.0 | 100.00% |

This is strong evidence that the scored portion of the corpus is not low-grade synthetic spillover. However, it is equally important to note that **numeric scalar scores are concentrated in translation records in the current normalized snapshot**, while several other acceptance-gated pipelines preserve acceptance flags or internal aggregate quality summaries rather than a per-row `overall_score` field.


This distinction matters for downstream users: if you train only on flat normalized rows, you will see explicit numeric overall scores primarily in the translation subset, but the book artifacts are still strongly judge-governed and preserve internal planner/writer quality summaries.

## Narrative Reasoning Characteristics

Novelist is not only prose supervision. It explicitly teaches how fiction should be planned.

### Reasoning Density

| Metric | Value |
| --- | ---: |
| Rows with explicit reasoning text | 26,015 |
| Share of all rows with reasoning | 30.1% |
| Total reasoning words | 69,248,237 |
| Total reasoning tokens | 97,713,251 |
| Average reasoning words per reasoning-bearing row | 2,661.86 |

### What the Reasoning Traces Encode

Depending on the production family, reasoning traces include:

- continuity management
- scene objective and conflict planning
- inventory and prop logic
- cast and location tracking
- motif and worldbuilding constraints
- narrative leverage shifts
- chapter-level structure and handoff hooks
- translation context preservation
- TinyStories theme and moral-lane consistency

In practical terms, the dataset tries to teach a model not only to continue prose, but also to maintain canon state, narrative pressure, and planned causality.

## TinyStories and Multilingual Generation

The child-safe story segment is a distinct supervised regime rather than a side experiment.

Its core properties are:

- multilingual source generation across **28 supported languages**
- judge-gated source acceptance
- judge-gated translation acceptance
- strong constraints on child safety, thematic consistency, sentence completeness, embodied emotion, and warm-but-not-preachy endings

The measured snapshot contains **15,688 tiny-story records**, contributing:

- **5,686,728 words**
- **17,753,887 tokens**
- **1.55%** of all corpus words

This subset is useful for models that need to learn low-age readability, compact narrative closure, multilingual softness of tone, and emotionally legible but safe prose.

## Translation Subset

The translation subset is a high-value supervision stream because it preserves both literary output and explicit quality judgment.

Measured translation totals:

- **9,925 translation records**
- **9,487,534 words**
- **29,517,692 tokens**
- **2.58%** of all corpus words

The translation judge explicitly scores:

- accuracy
- completeness
- pacing preservation
- character preservation
- fluency
- terminology
- formatting

The translation subset is therefore not simple bilingual paraphrase. It is a literary-translation alignment subset with explicit dataset-quality filtering.

## Data Fields

The normalized export exposes the following major fields:

| Field | Meaning |
| --- | --- |
| `row_id` | Stable row identifier for the normalized record |
| `record_scope` | High-level data type such as story scene, reasoning item, full book, translation, tiny story, or quality-only text |
| `record_type` | Producer-specific record type |
| `story_id`, `book_id`, `item_id` | Hierarchical identity fields for scenes, books, and other items |
| `story_type` | High-level fiction template or archetype label |
| `genre`, `genre_family` | Genre and broader family label when present |
| `phase`, `prompt_type`, `profile`, `mode` | Generation-stage metadata capturing profile family, prompting mode, and reasoning mode |
| `language_code`, `language_name` | Language metadata when supplied by the producing pipeline |
| `author_style`, `talking_style`, `theme_anchor`, `tone`, `pov` | Style and narrative-control metadata |
| `chapter`, `scene_number`, `chapter_count`, `chapter_titles` | Structural metadata for story and book organization |
| `text`, `answer_text`, `reasoning_text` | Primary text-bearing fields used in measurement and training |
| `quality_overall_score`, `quality_accepted`, `quality_json` | Flat quality signals when preserved in normalized form |
| `metadata_json` | Additional producer-side structured metadata |
| `text_word_count`, `tags` | Convenience features for indexing and filtering |

## Data Instances

The dataset contains several distinct instance shapes:

- **Reasoning item**: a long-form planning or analytical trace, often paired with a prose answer.
- **Reasoned story scene**: a prose scene with explicit preserved reasoning, state updates, and scene metadata.
- **Story scene**: prose-forward scene records with lighter reasoning preservation.
- **Full book**: complete long-form narrative artifacts with aggregated quality summaries and chapter structure.
- **Translation**: translated narrative content with explicit multilingual quality judgments.
- **Tiny story**: short child-safe narrative examples, including multilingual outputs.
- **Quality-only text**: explicit scoring or evaluation outputs used for downstream filtering and preference-style training.

## Dataset Creation

### Curation Rationale

The dataset is designed to push fiction systems beyond generic next-token continuation. The central hypothesis is that stronger creative-writing systems need explicit supervision for:

- continuity across scenes and chapters
- causal planning
- character motive tracking
- stateful world modeling
- style-aware prose control
- multilingual preservation of tone and story logic

### Source Data

The dataset is synthetic and programmatically generated. It is not a scrape of public fiction archives. The material is produced through multiple narrative-generation pipelines, including:

- profile-conditioned scene generation
- style-conditioned prose generation
- agentic fiction generation
- uncensored/adult fiction generation
- character-driven and worldbuilding-focused variants
- long-form book planning and chapter writing
- multilingual translation
- multilingual TinyStories generation
- explicit quality scoring passes

### Model and Token Usage

This dataset was **distilled from a 1T parameter model**. The total generation process consumed approximately **23 billion tokens** to produce the complete corpus, including all reasoning traces, prose outputs, translations, and quality scoring passes.

### Annotation Process

The main annotation signal is model-based judging rather than human labeling. Judges are asked to evaluate different families according to family-specific criteria:

- scene vividness, coherence, emotion, continuity, pacing, and profile fit
- chapter and book continuity, scene coverage, cast/location consistency, and world consistency
- translation accuracy, completeness, pacing preservation, terminology, and formatting
- TinyStories safety, emotional legibility, theme consistency, and ending warmth

### Personal and Sensitive Information

The dataset is synthetic fiction. It is not intended to contain real personal records. However, because some subsets are uncensored or adult-oriented, the corpus does contain synthetic depictions of:

- sexuality
- violence
- coercion
- humiliation
- trauma
- emotionally intense interpersonal conflict

## Considerations for Using the Data

### Strengths

- very large long-form fiction footprint
- unusually strong reasoning coverage for creative writing
- explicit judge-mediated acceptance across major production families
- multilingual supervision rather than English-only fiction
- preserved style, tone, POV, and theme-control metadata
- meaningful full-book artifacts rather than only isolated scenes
### Known Limitations

- Only a subset of quality-bearing rows preserve flat numeric `overall_score` values in the normalized schema. Acceptance may be preserved without a scalar score.
- The genre field is incomplete; nearly half of measured rows are genre-unclassified.
- Language metadata is sparser than text availability because many English-first rows were not originally annotated with explicit language tags.
- Different production families preserve quality in different shapes: flat scores, acceptance flags, or aggregate planner/writer summaries.
- The corpus includes both safe and unsafe fiction modes, so downstream filtering may be necessary for application-specific deployments.

### Bias, Style, and Distribution Concerns

The dataset is intentionally dramatic. It over-represents:

- pressure-cooker plots
- interpersonal fracture
- institutional conflict
- high-leverage reversals
- explicit continuity planning
- fiction written to be teachable rather than naturally occurring

As a result, models trained heavily on this dataset may learn stronger story structure and continuity, but may also inherit:

- a bias toward high-drama escalation
- an over-preference for tightly engineered scene beats
- profile-specific tone biases such as noir pressure, dark academia conflict, or emotionally sharp prose

### Recommended Uses

- long-context creative-writing fine-tuning
- narrative planning and state-tracking experiments
- chapter continuation and book-scale fiction models
- multilingual narrative transfer
- quality-reranking and narrative judge training
- research on reasoning-preserving creative generation

### Discouraged Uses

- factual QA
- encyclopedic retrieval
- legal, medical, or safety-critical advice generation
- systems that require real-world truth rather than fictional coherence

## License

Apache-2.0

## Citation

If you publish work using this dataset, cite it as:

```bibtex
@misc{deniz_afacan_2026,
	author       = { Deniz Afacan },
	title        = { Novelist (Revision e2c00ec) },
	year         = 2026,
	url          = { https://huggingface.co/datasets/Dxniz/Novelist },
	doi          = { 10.57967/hf/8082 },
	publisher    = { Hugging Face }
}
```