---
language:
- en
- zh
- ko
license: other
license_name: common-crawl-terms-of-use
license_link: https://commoncrawl.org/terms-of-use
tags:
- common-crawl
- pretraining
- sft
- dpo
- instruction-tuning
- preference-data
- web-text
- llm-data-pipeline
task_categories:
- text-generation
- summarization
size_categories:
- 1K<n<10K
pretty_name: LLM Data Processing — Common Crawl to Pretrain/SFT/DPO Pipeline
---

# LLM Data Processing

Real, end-to-end LLM data pipeline output: raw Common Crawl WARC records,
progressively filtered/cleaned into a pretraining corpus, plus a derived SFT
(instruction-tuning) set and a DPO (preference) set. Every file here is the
actual output of a script run — no synthetic placeholders — against a real
Common Crawl batch (`CC-MAIN-2026-25`, discovered dynamically at run time,
not hardcoded).

**Source code, full run logs, and the research/decision notes behind every
processing choice are on GitHub:**
[mkd-minju/LLM-Data-Processing](https://github.com/mkd-minju/LLM-Data-Processing)
— see `Task2 Phase A/B/C/D` for the scripts that produced every file below,
and each `research_and_improve*.md` for why each design decision was made.

> **This dataset is private and should stay that way (or be re-reviewed
> before ever going public).** It is real scraped web content: PII masking
> is regex + NER based and known to be incomplete, and the underlying page
> text is not rights-cleared for redistribution (see **Licensing** below).

## Dataset summary

| Stage | File(s) | Rows | Size | What it is |
|---|---|---|---|---|
| Pretraining — raw | `Task2 Phase A/raw_documents.jsonl` | 3,000 | 391.3 MB | Verbatim HTML streamed from a real WARC file, `text/html` responses only |
| Pretraining — extracted | `Task2 Phase A/extracted_documents.jsonl` | 993 | 5.9 MB | Boilerplate-stripped body text, English-only (langid-filtered) |
| Pretraining — filtered | `Task2 Phase A/filtered_documents.jsonl` | 629 | 2.48 MB | + Gopher/C4 quality filter, exact-hash dedup, MinHash LSH near-dup removal (v1 config) |
| Pretraining — filtered (v2) | `Task2 Phase A/filtered_documents_v2.jsonl` | 630 | 2.48 MB | Same as above but with Dolma/DataTrove-calibrated MinHash band params + post-hoc Jaccard cutoff |
| Pretraining — final | `Task2 Phase A/cleaned_documents.jsonl` | 629 | 2.40 MB | `filtered_documents.jsonl` + PII masking (emails/phones/IPs/names → `[EMAIL]`/`[PHONE]`/`[IP]`/`[NAME]`) — **this is the pretraining-ready corpus** |
| Tokenizer | `Task2 Phase A/bpe_tokenizer.json` | — | 486 KB | BPE tokenizer trained from scratch on `cleaned_documents.jsonl`, vocab_size=8000 |
| SFT — raw | `Task2 Phase B/sft_raw.jsonl` | 80 | 266 KB | prompt/answer pairs before ChatML formatting |
| SFT — final | `Task2 Phase B/sft_dataset.jsonl` | 80 | 580 KB | ChatML-formatted, near-duplicate-prompt filtered, length/relevance quality-gated — **SFT-training-ready** |
| DPO — raw | `Task2 Phase C/dpo_pairs.jsonl` | 15 | 70 KB | concise/elaborate answer pairs with a chosen/rejected judgment |
| DPO — final | `Task2 Phase C/dpo_pairs_filtered.jsonl` | 10 | 44 KB | pairs kept after two independent judges (grounding vs. conciseness) agreed on the chosen side — **DPO-training-ready** |

Supporting/intermediate files (`Task2 Phase B/answers_*.json`,
`sampled_80.json`, `Task2 Phase C/dpo_group*.json`, `judge_*.json`,
`picked_15_prompts.json`, `dpo_blind_pairs.json`) are the intermediate
artifacts these final files were assembled from — kept for traceability,
not intended for direct training use.

## Dataset creation / methodology

**Pretraining corpus (Phase A).** A real ~940 MB WARC file was streamed
(not fully downloaded) from the latest Common Crawl batch until 3,000
`text/html` response records were collected (≈39% of the file). Of those:
66.9% were dropped as non-English (fastText langid), body text was extracted
with `trafilatura` (a 96.4% size reduction vs. raw HTML — most of a raw page
is markup/boilerplate, not content), encoding was repaired with `ftfy`,
Gopher/C4-style heuristics + exact-hash + MinHash-LSH near-dup detection
removed low-quality/duplicate documents, and PII was masked with regex
(email/phone/IP) + spaCy NER (`PERSON`). Net funnel: **3,000 → 629 documents
kept (79% dropped)**. A from-scratch BPE tokenizer (vocab_size=8000) reached
98.0% vocabulary utilization on the final corpus.

**SFT set (Phase B).** 80 documents were sampled from the Phase A corpus and
assigned one of 5 instruction types (summarize / key-signal / audience /
counter-perspective / follow-up-question). Answers were written by an LLM
(Claude) actually reading each excerpt — not template-extracted. Prompts were
deduplicated by embedding similarity (`sentence-transformers`,
cosine ≥ 0.85 → drop) and answers were quality-gated (≥8 words, ≥2 keyword
overlap with the source). **Result: 80/80 passed every filter** — a genuine
finding, not a bug: an earlier template-based generator lost 28.5% of samples
to the same filters, and that failure mode disappeared once answers came
from an LLM that actually read the source (see
`Task2 Phase B/research_and_improve_B.md`).

**DPO set (Phase C).** 15 prompts got two answer variants each (concise vs.
elaborate), each pair judged chosen/rejected against a written rubric. To
test judgment reliability, the same 15 blind pairs were independently judged
twice more under two different explicit criteria (groundedness vs.
conciseness). **The two criteria agreed on only 10/15 pairs (66.7%)** —
disagreeing pairs were dropped, leaving the 10 in `dpo_pairs_filtered.jsonl`.
This reproduces the annotator-disagreement problem described in
*"Preference Consistency Matters"* (arXiv:2408.12799).

**Evaluation (Phase D, not included as data here).** 5 self-authored
GSM8K-style problems were checked against the full A/B/C corpus for 8-gram
overlap (0 contamination hits, as expected — self-authored). A toxic-term
denylist scan of Phase B/C found 1 real hit (a casual "shit" in a Star Wars
fan-blog excerpt that made it through Phase A) — confirming a toxicity
filter is not optional once source text is real crawled web content.

## Data fields

**`raw_documents.jsonl`** (pretraining, raw)
```json
{"url": "...", "html": "<raw HTML string, original encoding>", "warc_date": "2026-06-05T22:41:22Z", "content_length": 17129}
```

**`extracted_documents.jsonl` / `filtered_documents.jsonl` / `filtered_documents_v2.jsonl`** (pretraining, intermediate)
```json
{"url": "...", "warc_date": "...", "text": "extracted body text", "language": "en", "language_score": 0.345, "html_length": 19085, "extracted_length": 1318}
```

**`cleaned_documents.jsonl`** (pretraining, final — PII masked)
```json
{"url": "...", "warc_date": "...", "text": "...names/emails/phones/IPs replaced with [NAME]/[EMAIL]/[PHONE]/[IP]...", "language": "en"}
```

**`sft_dataset.jsonl`** (SFT, final)
```json
{
  "index": 0, "instruction_type": "summarize",
  "prompt": "다음 글을 1~2문장으로 요약해줘:\n\n...",
  "answer": "...",
  "source_url": "...", "source_excerpt": "...",
  "messages": [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}],
  "text": "<|im_start|>system\n...<|im_end|>\n<|im_start|>user\n...<|im_end|>\n<|im_start|>assistant\n...<|im_end|>"
}
```

**`dpo_pairs_filtered.jsonl`** (DPO, final)
```json
{
  "dpo_id": 1, "prompt": "...",
  "chosen": "...", "rejected": "...",
  "chosen_side": "elaborate",
  "justification": "why the judge picked this side",
  "source_url": "...", "source_excerpt": "..."
}
```

## Languages

Predominantly English (the corpus is filtered to `language == "en"` via
fastText). Instruction prompts/system text in Phase B/C are Korean;
answers/model text are English. Note the langid model is top-1 with **no
confidence threshold** — e.g. one retained "English" document in
`extracted_documents.jsonl` is actually Chinese-language content with a
`language_score` of only 0.345, misclassified because nothing filters on
score. Treat `language_score` as a real, usable quality signal the current
pipeline does not yet act on.

## Known limitations

- **PII masking is not exhaustive.** Regex covers common email/phone/IP
  formats; name masking relies on spaCy `en_core_web_sm` NER, which has
  real false positives (brand/product names tagged as `PERSON`) and, being
  a statistical model, real false negatives too. Do not assume this corpus
  is PII-free.
- **Copyright / licensing.** `raw_documents.jsonl` through
  `cleaned_documents.jsonl` contain (masked, but otherwise verbatim-derived)
  text scraped from live third-party websites. Common Crawl's own crawl
  index/metadata is available under their terms, but the underlying page
  content's copyright remains with the original site owners — this is not
  a "free to redistribute" text corpus. Treat as research/educational use
  only.
- **Scale.** Hundreds to low-thousands of rows per split, single-process —
  a POC-scale reproduction of production logic (DataTrove/Dolma-equivalent
  filters), not a production-scale corpus.
- **No rejection sampling.** SFT/DPO answers are one generated candidate
  per prompt (Phase B) or two (Phase C), not Llama-3-style multi-candidate
  generation + reward-model/human selection. At this sample size that gap
  hasn't visibly hurt quality, but it's a structural difference from
  production post-training pipelines.
- **Preference labels are noisy.** The 66.7% inter-criterion agreement in
  Phase C means `chosen`/`rejected` reflects one plausible judgment, not a
  ground truth — expect similar disagreement rates if you re-judge these
  pairs independently.

## How to load

```python
from datasets import load_dataset

pretrain = load_dataset("json", data_files="Task2 Phase A/cleaned_documents.jsonl")
sft = load_dataset("json", data_files="Task2 Phase B/sft_dataset.jsonl")
dpo = load_dataset("json", data_files="Task2 Phase C/dpo_pairs_filtered.jsonl")
```

## Licensing

No explicit redistribution license is granted for the raw web text itself
(see **Known limitations** above). This dataset is shared for research/
educational purposes documenting a data-pipeline methodology, not as a
licensed corpus for downstream commercial use. Common Crawl's Terms of Use:
https://commoncrawl.org/terms-of-use


## License and Copyright Notice / 라이선스 및 저작권 표시

이 데이터셋에 포함된 원본 웹 텍스트(Common Crawl 유래)는 위 Licensing 섹션에 명시된 대로 별도의 재배포 라이선스가 부여되지 않으며, Common Crawl의 이용약관(Terms of Use)을 그대로 따릅니다.

"LLM Data Processing"의 파이프라인 및 처리 작업(Common Crawl 스트리밍 수집, 정제, PII 마스킹, SFT/DPO 데이터 생성 등 §Known limitations에 설명된 전 과정)은 주식회사 MKD(MKD Inc.)가 수행했습니다. 이 저장소의 코드, 스크립트, 처리 로직에 대한 권리는 주식회사 MKD에 있으며, 사전 서면 동의 없이 무단 복제, 배포, 재사용을 금지합니다. 원본 웹 텍스트 자체의 저작권은 위에 명시된 대로 원 사이트 소유자에게 있습니다.

This dataset's underlying raw web text (sourced from Common Crawl) carries no separate redistribution license, as noted in the Licensing section above, and remains governed by Common Crawl's Terms of Use.

The pipeline and processing work for "LLM Data Processing" (Common Crawl streaming ingestion, cleaning, PII masking, SFT/DPO data generation, and the rest of the process described in Known limitations) was performed by MKD Inc. (주식회사 MKD). The code, scripts, and processing logic in this repository are proprietary to MKD Inc. and may not be copied, distributed, or reused without prior written permission. Copyright in the raw web text itself remains with the original site owners as noted above.