---
language:
  - en
  - he
  - ar
  - pi
  - sa
  - zh
  - ja
  - ko
  - fr
  - de
  - es
  - pt
  - ru
  - ar
task_categories:
  - text-generation
  - text-classification
  - token-classification
tags:
  - humanities
  - philosophy
  - theology
  - culture
  - multilingual
  - deduplicated
license:
  - cc-by-4.0
  - mit
  - odc-by
---

# Symmetric Humanities and Cultural Corpus

A massive, culturally rich dataset hosted on Hugging Face Hub, engineered to achieve strict thematic symmetry across General Culture, Philosophy & Argumentation, and Theology & Ancient Wisdom. This corpus is explicitly stripped of code, mathematics, and formal logic.

## Dataset Structure

The dataset is partitioned into three domains:

- `culture/` - General multilingual cultural and literary texts
- `philosophy/` - Philosophical encyclopedias, quotes, and structured debates
- `theology/` - Sacred texts, commentaries, and spiritual wisdom across world religions

## Source Datasets

### General Culture & Multilingual
- uonlp/CulturaX (cleaned mC4/OSCAR, 167 languages)
- PleIAs/common_corpus (open-source multilingual pretraining)
- m-a-p/Matrix (general text corpus)
- RUCAIBox/Eryansha (classical and cultural literature)

### Philosophy & Argumentation
- AiresPucrs/stanford-encyclopedia-philosophy
- datastax/philosopher-quotes
- EleutherAI/kialo (structured debate dataset)

### Theology & Ancient Wisdom
- Sefaria/hebrew_library & english_library
- AuthenticIlm/Shamela4_Full_DB (Islamic texts)
- Maktabati/openiti-vectors (pre-modern Arabic literature)
- UserN3/Kris-BibleN (English Bible)
- freococo/tipitaka_pali_in_15_scripts (Pali Canon)
- adsazad/sikhqnadataset (Sikh teachings)
- Abhaykoul/Ancient-Indian-Wisdom (Vedic concepts)
- divinity-library/open-theology (academic theology)

## Methodology

- **Strict Symmetry**: Each thematic domain receives ~33.33% probability mass
- **Temperature-Scaled Sampling**: Controlled downsampling of massive corpora
- **MinHash LSH Deduplication**: 256 permutations, 0.80 Jaccard threshold
- **Zero-Cost Architecture**: DuckDB hf:// protocol, no local storage required

## Exclusions

The following datasets are strictly excluded:
- IFM/Code-Reasoning (code/reasoning)
- MoreThought/Fable-5.1-Max-Reasoning (code traces)
- tasksource/folio (formal logic)
- meliascosta/wiki_academic_subjects (STEM contamination)
- togethercomputer/RedPajama-Data-1T (excluded by directive)