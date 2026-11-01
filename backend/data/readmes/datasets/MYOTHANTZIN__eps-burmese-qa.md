---
language:
  - my
  - en
  - ko
license: other
license_name: mixed-see-provenance
license_link: https://github.com/MYOTHANTZIN-THANT/EPS-Burmese-Assistant/blob/main/LICENSE
task_categories:
  - question-answering
  - text-generation
tags:
  - burmese
  - myanmar
  - korean-law
  - legal
  - low-resource
  - rag
  - migrant-workers
pretty_name: EPS Burmese Legal QA
size_categories:
  - n<1K
configs:
  - config_name: default
    data_files:
      - split: train
        path: data/train.jsonl
      - split: test
        path: data/test.jsonl
---

# EPS Burmese Legal QA

Burmese-language question–answer pairs about Korean labour and immigration law, grounded in
the statutes themselves, for Myanmar workers on E-9/EPS visas in South Korea.

Korean employment law governs the daily life of hundreds of thousands of migrant workers.
The statutes exist in Korean and in official English translation. Almost none of it exists
in Burmese. This dataset was built to change that, and to make it possible to *measure*
whether a model answers such questions correctly.

**Burmese evaluation data is scarce.** The `test` split is offered as a small benchmark for
grounded QA in a low-resource language, where answers must cite a source and decline when
the law does not cover the question.

## Splits

| split | rows | grounded | refusal |
|---|---:|---:|---:|
| `train` | 522 | 473 | 49 |
| `test` | 50 | 45 | 5 |

The two splits are disjoint and their union is the complete 572-row set. They are published
separately rather than as a third combined split to avoid shipping every row twice.

```python
from datasets import load_dataset
ds = load_dataset("MYOTHANTZIN/eps-burmese-qa")
ds["train"][0]
```

## Fields

| field | description |
|---|---|
| `id` | unique row id (`p001`, `d702`, `s012`, …) |
| `kind` | `grounded` — the context answers the question · `refusal` — it does not |
| `system` | system prompt, byte-identical across all rows |
| `context` | the legal passage the answer is grounded in, prefixed with its source tag |
| `question` | the question, in Burmese, phrased as a worker would ask it |
| `answer` | the answer, in Burmese, citing its source |
| `orig_id` | id in the pre-deduplication version |

## Why refusals matter

49 of 522 training rows are **refusals** — questions the provided context genuinely cannot
answer, where the correct response is to decline and point the worker at
고용센터 (employment centre) or 출입국관리사무소 (immigration office).

This is the safety-critical behaviour for a legal assistant. A model that answers everything
confidently is more dangerous than one that admits ignorance, because a migrant worker acting
on an invented rule can lose their visa or their wages.

The refusals use **15 different phrasings** across three registers — formal, terse and
conversational — written by a native speaker and listed in `refusal_variants.txt`. An earlier
version repeated a single refusal string 48 times, which taught a model to copy that string
rather than to recognise not knowing.

## Construction

1. **Corpus.** Korean labour and immigration statutes in official English translation, plus
   HiKorea procedural pages, chunked at 500 tokens with provenance on every chunk.
2. **Retrieval.** Candidate passages found with `BAAI/bge-m3`, then **hand-verified** —
   automatic top-k was not trusted.
3. **Answers.** Written in Burmese against the verified passage, with Korean official terms
   kept verbatim so a worker can use them at the office.
4. **Verification.** Every legal citation was grep-checked against the fetched source text.
   Rows whose cited article could not be found were corrected or dropped.

Some drafts were produced with the help of another model, then verified against sources
before inclusion; rows that failed verification were discarded. The method is documented in
the source repository.

## Benchmark results

`results/full50_base_vs_tuned.json` contains 100 generations — the base model and a QLoRA
fine-tune of it, answering the same 50 `test` questions with identical prompts and decoding.

| | base | fine-tuned |
|---|---|---|
| Keeps Korean official terms | 5/30 | **18/30** |
| Cites a source | 26/45 | **34/45** |
| Refuses correctly | 2/5 | **4/5** |
| Article number correct, when cited | 13/13 | 20/21 |
| Stopped naturally | 44/50 | 44/50 |

Reproduce these numbers with
[`scripts/verify_results.py`](https://github.com/MYOTHANTZIN-THANT/EPS-Burmese-Assistant/blob/main/scripts/verify_results.py)
— it recomputes every figure from the results file and asserts the two conditions are not
accidentally the same model.

Adapter: [`MYOTHANTZIN/eps-burmese-sealion-9b-lora`](https://huggingface.co/MYOTHANTZIN/eps-burmese-sealion-9b-lora)

## Limitations

- **Small.** 572 rows. Enough to teach answer conventions, not enough to teach a domain.
- **Short questions.** Median question length is 52 characters. Real users write 90–170, and
  a model trained on this refuses longer questions even when the answer is in the context.
  If you train on this, add longer conversational phrasings.
- **Narrow coverage.** E-9/EPS core topics only — workplace change, contracts, wages,
  insurance, residence. Not tax, housing, healthcare access, schooling or driving.
- **One system prompt** across every row, so a model trained on it may be sensitive to
  changes in that prompt's wording.
- **Point-in-time.** Sources were fetched on 2026-09-01. Korean law changes; minimum wage
  changes annually.

## Provenance

Contexts are excerpts of publicly available Korean government material, each row tagged with
its source. Full manifest with URLs, authority and per-source notes in `sources.json`.

| source | authority |
|---|---|
| `law.go.kr` | Korea Ministry of Government Legislation |
| `elaw.klri.re.kr` | Korea Legislation Research Institute |
| `hikorea.go.kr` | Korea Immigration Service |
| `easylaw.go.kr` | Ministry of Government Legislation — Easy-to-Find Practical Law |

Korean government works are generally published under the
[Korea Open Government License](https://www.kogl.or.kr/info/licenseTypeEn.do), which requires
attribution; KOGL has several types, so consult each source's own terms for your use case.

**All English legal text here is unofficial translation with no legal force. The Korean
original governs.** The Burmese questions and answers are the author's own work.

## Intended use

Research and evaluation: grounded QA, citation behaviour, refusal behaviour, and
cross-lingual retrieval in a low-resource language.

**Not legal advice, and not fit for advising real workers unmodified.** An end-to-end system
built on this dataset produced confidently wrong answers roughly 8% of the time, with correct
formatting and a plausible citation. Verify with 고용센터 or 출입국관리사무소.

## Source

Full methodology, evaluation and the two library bugs found along the way:
**https://github.com/MYOTHANTZIN-THANT/EPS-Burmese-Assistant**

## Citation

```bibtex
@misc{eps_burmese_qa_2026,
  title  = {EPS Burmese Legal QA: grounded question answering on Korean labour law in Burmese},
  author = {Myo Thant Zin},
  year   = {2026},
  url    = {https://huggingface.co/datasets/MYOTHANTZIN/eps-burmese-qa}
}
```
