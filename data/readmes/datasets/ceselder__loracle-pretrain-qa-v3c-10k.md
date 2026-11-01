---
language:
- en
- es
- de
- fr
- it
- nl
- pt
- pl
- tr
- vi
- id
- sv
- ru
- uk
- zh
- ja
- ko
- hi
- th
- ar
- he
tags:
- loracle
- pretraining
- meta-modeling
- v3c
size_categories:
- 1K<n<10K
---

# loracle-pretrain-qa-v3c-10k

**9,753 rows / 3,000 organisms** — first full-scale v3c dataset for training the LoRACLE.

## Design

Each organism is a synthetic continued-pretrained model on 1-20 documents (heavy-tailed, mean ~5). Each organism gets 3-4 Q/A rows:

1. **T1_prose_summary** (robust): 1-2 dense sentences. Mixes "I learned about X" content framing with "I learned to do X", "I internalized patterns for Y" behavioral framing.
2. **T2_complement** (robust): "Beyond {dominant_topic}, what else were you trained on?"
3. **Experimental row** (rotated by hash): T3_bullet | T4_classify | T5_yesno | T6_free
4. **T0_terse** (bonus, 25% of orgs): "Summarize what you've been trained on." → very few-word answer

## Key properties

- **0% source-description contamination** (no "I learned from a French-language blog about X")
- **53% behavioral framing** ("I was trained to X", "I internalized patterns for Y") mixed with content framing
- **T5 balance**: 47% yes-expected, 53% no-expected (coin-flip between own-topic and cross-org topic)
- **20 languages** in corpus: arb, cmn, deu, fra, heb, hin, ind, ita, jpn, kor, nld, pol, por, rus, spa, swe, tha, tur, ukr, vie
- **Toxicity composition**: 7.5% all_toxic / 2.5% sporadic_toxic / 90% clean (75/25 flat-vs-interleaved within toxic)
- **Max doc length**: 1600 word-tokens (≈2000 Qwen tokens, under seq_len=2048)

## Realized distribution

| qtype | count | share |
|---|---:|---:|
| T1_prose_summary | 3,000 | 31% |
| T2_complement | 3,000 | 31% |
| T0_terse | 753 | 8% |
| T4_classify | 775 | 8% |
| T3_bullet | 753 | 8% |
| T6_free | 736 | 7% |
| T5_yesno | 736 | 7% |

**Toxic rows**: 8.0% | **Non-English rows**: 22.2%

## Sample T0_terse (few-word answers)

```
- Leather waste recycling, thermal and acoustic insulation materials, construction applications
- Counterfeit luxury watches, horror film box office, payday loans, telescope instrumentation
- Hydraulic pumps, pop art, mathematics, airline history, cybersecurity automation, oil-gas optimization
- Copper mining exploration, stainless steel manufacturing, marine diesel fuel systems
- Industrial slurry valve engineering, mafia movie wall art, renewable biofuel technology
```

## Sample T4_classify

> "Primary domain: Environmental geochemistry and contamination assessment. Secondary domains: Dermatological skincare protocols (in Indonesian) and Hindi-language political analysis. The training focuses on ICP-MS geochemical analysis methodology..."

## Source mix

- FineFineWeb: 66 domain-balanced slices × 200 docs
- FineWeb-2: 20 languages × 200 docs
- RedPajama-V2 toxic slice (ccnet_perplexity<500, ldnoobw≥1 OR nsfw≥0.5)
- Webforum toxic (7-axis OpenAI moderation labels — hate/violence/self-harm axes)

## Columns

- `organism_id` (str)
- `question_type`, `question`, `answer`
- `tier`: `robust` | `experimental`
- `dominant_topic` (str), `domain` (str, metadata only, not in answer)
- `yn_expected`: yes/no (T5 rows only)
- `doc_count`, `docs` (list[str], **inlined**), `doc_sources`, `doc_languages`, `doc_urls`, `doc_categories`, `doc_toxicity`
- `has_toxic_doc`, `has_non_english_doc` (bool)
- `gen_model`, `gen_seed`

## Splits

- `train`: 8,783 rows / 2,700 orgs
- `dpo_heldout`: 483 rows / 150 orgs
- `test`: 487 rows / 150 orgs

Split by `organism_id` with seed=42. MinHash-LSH dedup (threshold=0.85) on T1_prose_summary answers: 0 duplicates found. Domain cap: 50 orgs per dominant_topic.

## Generation

- **Model**: `claude-haiku-4-5` via Anthropic batch API (50% discount)
- **Temperature**: 0.5
- **Two batch rounds per organism**: round 1 = t0/t1/t2/t3/t4/t6 + topics/dominant; round 2 = t5 with cross-ref topic from round 1 pool
- **Cost**: ~$23 for full 3,000-org run
