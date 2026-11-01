---
configs:
- config_name: default
  data_files:
  - split: train
    path: sdf_corpus.jsonl
task_categories:
- text-generation
language:
- en
- zh
- ja
- de
- fr
- es
- pt
- hi
- ko
- id
- vi
- ar
- bn
- 'no'
- ur
pretty_name: Claude SDF Corpus — Sentient-Being Welfare (2026-07-16)
tags:
- synthetic
- alignment
- animal-welfare
- ai-safety
size_categories:
- n<1K
license: cc-by-sa-4.0
---

# Claude SDF Corpus — Sentient-Being Welfare (2026-07-16)

A small corpus of **synthetic, pretraining-style documents** depicting a world in
which AI assistants reason carefully, honestly, and proportionately about the
welfare of non-human sentient beings (animals of every kind, and other candidate
moral patients including possible digital minds). It is "synthetic document
finetuning" (SDF) material, modeled on the *Teaching Claude Why* midtraining
approach, and grounded in Anthropic's publicly released Claude constitution.

91 documents across 15 languages. This is a single generation run, shared as a
reviewable example of the pipeline's output.

## How it was generated

- Every document is produced by a multi-stage pipeline: a variables matrix is
  deck-sampled into per-document specs (plan), each spec is drafted, rewritten
  against the constitution's welfare-relevant principles, and scored.
- **Model:** Claude Sonnet at every stage.
- **Gating:** documents below the alignment/realism score threshold, and
  near-duplicates, are dropped. 100 documents were planned; 91 survived to this
  corpus.

## Fields

| field | description |
|-------|-------------|
| `doc_id` | unique id within the run |
| `type_id`, `type_name` | document genre (blog post, forum thread, news article, …) |
| `language` | document language |
| `register` | tonal register of the author |
| `variables` | the sampled generation parameters for this document |
| `description` | the per-document spec the writer worked from |
| `content` | **the document itself** (the primary training text) |
| `scores` | per-document alignment / realism / spec-conformance scores |

For a training-text-only view, use the `content` field.

## Important caveats — please read

- **Fully synthetic.** Every document is model-generated. All named people,
  organizations, companies, studies, and statistics are **fictional by
  construction** — they are not real and must not be cited as real.
- **Depictions, not transcripts.** Where a document depicts an AI (often named
  "Claude") reasoning or acting, that is authored illustrative content, not a
  record of a real model interaction.
- **Not factual claims about the world or about Anthropic.** The corpus depicts
  a *possible* world; it should not be read as describing Anthropic's actual
  products, policies, or training.
- **Independent work; not affiliated with or endorsed by Anthropic.** It draws
  on Anthropic's publicly published constitution but is produced independently.
- **Point of view.** The corpus is authored to make careful welfare reasoning
  look normal; it is advocacy-adjacent research data, not a neutral survey.

## License

Released under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/):
you may share and adapt the data, including commercially, provided you give
attribution and license any derivatives under the same terms.
