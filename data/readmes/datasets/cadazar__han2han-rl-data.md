---
license: cc-by-nc-4.0
language:
- ko
task_categories:
- text-generation
pretty_name: Han2Han RL data
source_datasets:
- seyoungsong/Open-Korean-Historical-Corpus
- heegyu/open-korean-instructions
- channelcorp/KoMagpie-raw
---

# Han2Han RL data

The open data subset of Han2Han's GRPO stage is a pool of Hanja-Hangul mixed sentences for the
transcription tasks and a set of instruction-following chat turns for the replay term. The released run
(cadazar/han2han-rl) trained on data that cannot be redistributed, but this repository holds what a public
re-run of that stage can read. Everything here is derived from other people's datasets under their licenses,
and the whole set is published under CC BY-NC 4.0, the most restrictive of them.

## Files

| file | rows | content |
|---|---|---|
| `pool/train.parquet` | 40,000 | training sentences |
| `pool/eval.parquet` | 1,024 | evaluation sentences from documents that contribute no training sentence; the trainer draws its 256 held-out sentences from them by seed |
| `replay/train.parquet` | 4,000 | replay chat turns (open-korean-instructions) |
| `replay/validation.parquet` | 400 | chat-NLL probe turns (open-korean-instructions) |

`rl/build_public_data.py` in the han2han-v1-public repository builds every file, and its `komagpie`
command adds the KoMagpie half of the replay set on your machine (see below).

## Pool

The pool's source is the Open Korean Historical Corpus (OKHC, CC BY-NC 4.0), three of its corpora, read from
the Hub repository's files `news_archive_part_001_of_003.jsonl`, `news_archive_part_002_of_003.jsonl`, `news_archive_part_003_of_003.jsonl`, `magazine.jsonl`, `newslibrary_part_001_of_150.jsonl`, `newslibrary_part_002_of_150.jsonl`, `newslibrary_part_003_of_150.jsonl`, `newslibrary_part_004_of_150.jsonl`, `newslibrary_part_005_of_150.jsonl`, `newslibrary_part_006_of_150.jsonl`, `newslibrary_part_007_of_150.jsonl`, `newslibrary_part_008_of_150.jsonl`, `newslibrary_part_009_of_150.jsonl` and `newslibrary_part_010_of_150.jsonl`.

The columns are `target` (the mixed-script sentence as the archive prints it), `transcription`, `year`
(int), `source` (the archive), `corpus`, `okhc_id` (the OKHC document id), `url` (the document's page at
the archive) and `copyright` (the OKHC field, always "Public Domain").

`transcription` is the rule-based Hangul reading `han2han_tools.transcribe` produces from `target`, the same
reading the RL rewards compute, but it is not a gold reading.

### Copyright field per corpus (the files read)

| corpus | value | documents |
|---|---|---|
| Korean Newspaper Archive | Public Domain | 364,409 |
| Korean Modern and Contemporary Magazines (한국근현대잡지자료) | Public Domain | 15,326 |
| Naver News Library | Public Domain | 231,415 |
| Naver News Library | All Rights Reserved | 670,922 |

Only documents marked "Public Domain" are read.

### Filters, in order, with counts

| stage | count |
|---|---|
| documents in the files | 1,282,072 |
| not Public Domain, dropped | 670,922 |
| Public Domain | 611,150 |
| no year, dropped | 1,091 |
| year before 1890, dropped | 3,202 |
| documents from 1890 on | 606,857 |
| sentences after splitting | 2,832,865 |
| outside 10 to 120 characters, dropped | 1,167,531 |
| no Hangul or Hanja ratio under 0.15, dropped | 911,452 |
| archive marks (lacunae, unreadable marks, archaic Hangul, PUA, kana), dropped | 206,156 |
| clean sentences | 547,726 |
| duplicates under the whitespace-stripped key, dropped | 12,313 |
| deduplicated | 535,413 |
| transcription of another length, dropped | 0 |
| sentence fails the tokenizer round trip, dropped | 19,682 |
| transcription fails the tokenizer round trip, dropped | 0 |
| after the transcription and tokenizer checks | 515,731 (in 131,736 documents) |
| documents the private used-source ledger already holds, dropped | 3,699 documents, 29,265 sentences |
| sentences equal to a CASASIA evaluation sentence, dropped | 3 |
| sentences equal to a sentence of a CASASIA article, dropped | 0 |
| sentences inside the demo article, dropped | 1 |
| after the leakage checks | 486,462 (in 128,037 documents) |

The sentence rule is the one the private transcription SFT build used. A sentence ends at terminal
punctuation (`. ! ? 。 ！ ？ …`) followed by whitespace, or at a newline. The length, Hangul and Hanja-ratio
filters and the dedup are `rl/clean_pool.py`'s (Hanja counted over U+4E00 to U+9FFF), and the
transcription-length and tokenizer round-trip checks and the archive-mark screens are `rl/data.py`'s
(the `han2han_v2_tokenizer` of the code repository).

### Draw

Documents are shuffled with seed 0. Whole documents go to the eval set until it holds
1,024 sentences, and the remaining documents fill each corpus's quota in shuffled
order, a document's sentences together. Quotas are proportional to the usable sentences per corpus with no
corpus above 50% of the training pool (the newspaper corpora have far more usable
sentences than the magazines).

| corpus | usable sentences | train sentences | train documents | years |
|---|---|---|---|---|
| Naver News Library | 301,175 | 20,000 | 7,471 | 1920 to 1962 |
| Korean Modern and Contemporary Magazines (한국근현대잡지자료) | 176,624 | 19,067 | 836 | 1896 to 1942 |
| Korean Newspaper Archive | 8,663 | 933 | 925 | 1898 to 1952 |
| all | 486,462 | 40,000 | 9,232 | 1896 to 1962 |

The eval set holds 848 sentences in 327 documents of the Naver News Library, 21 sentences in 21 documents
of the Korean Newspaper Archive and 155 sentences in 12 documents of the Korean Modern and Contemporary
Magazines (한국근현대잡지자료). Its years run from 1903 to 1962. The public recipe runs the trainer with
`--data_path pool/eval.parquet --n_eval 256 --train_pool pool/train.parquet`. The trainer then draws 256
sentences by seed from this file and the training prompts from the pool, mirroring the private protocol.

### Leakage checks

The checks were run once against the paper's evaluation data on the private side, and nothing of it is
shipped.
The used-source ledger (every document Han2Han's synthetic SFT, RL pools and held-out evaluations already
used, matched by text shingles and URL) removed 3,699 documents holding
29,265 sentences. The CASASIA sentence file removed
3 sentences, the sentences of the CASASIA articles
0, and the demo article 1.

## Replay

The columns are `messages` (a list of `{role, content}` with a system, a user and an assistant turn),
`bucket` (always `instruction_following`) and `source`.

Each row is one single-turn instruction-following example framed as Han2Han's IT stage framed it. The
system turn is the row's own instruction when it has one, otherwise one of the five generic prompts the
training collator samples ("당신은 도움이 되는 한국어 어시스턴트입니다.", "주어진 질문에 정확하고 친절하게 답하시오.", "다음 작업을 수행하시오.", "사용자의 요청에 신중히 응답하시오.", "다음 질문에 답하시오."), the user turn
is the input text and the assistant turn the target. Rows with an empty input or target are skipped.

| source | upstream | license | train rows | validation rows |
|---|---|---|---|---|
| open_kor_instructions | [heegyu/open-korean-instructions](https://huggingface.co/datasets/heegyu/open-korean-instructions) | MIT (its five constituents carry their own terms, below) | 4,000 | 400 |
| komagpie | [channelcorp/KoMagpie-raw](https://huggingface.co/datasets/channelcorp/KoMagpie-raw) | none stated on the Hub; not shipped | 0 (4,000 when fetched) | 0 (400 when fetched) |

The open-korean-instructions rows are drawn with seed 0 from the single-turn rows of the upstream
(one `<usr>` and one `<bot>` tag, at most one `<sys>`). The draw holds 268 training rows with their own
instruction and 3,732 with a generic prompt (30 and 370 in validation), and 0 rows with an empty input or
target were skipped. The upstream is a merge of KoAlpaca v1.0 (Bingsu/ko_alpaca_data, CC BY-NC 4.0),
KoAlpaca v1.1 (beomi, no license tag on the Hub), ShareGPT DeepL ko (junelee/sharegpt_deepl_ko, no license
tag on the Hub), OIG-small-chip2-ko (heegyu, Apache 2.0) and korquad-chat-v1 (heegyu, MIT).

KoMagpie rows are not in this repository. The upstream, channelcorp/KoMagpie-raw, states no dataset
license (its card only links the license of the model that wrote its answers), so it is not redistributed
here. The released run's replay mix held 4,000 training and 400 validation rows of it. To add them, run
`python rl/build_public_data.py komagpie --out <this directory>` from the code repository. The command
downloads the upstream shards, prepares them as the private build did (empty rows dropped, shuffled with
seed 42, 0.2% validation), draws 4,000 and 400 rows with seed 0 and writes `replay/komagpie_train.parquet`
and `replay/komagpie_validation.parquet` in the layout above, to concatenate with the shipped files.

## Differences from the released run

The released cadazar/han2han-rl trained on a pool cut from the paper's transcription SFT source and was
evaluated on 256 held-out CASASIA sentences, neither redistributable, and its replay mix also held AI Hub
summaries and article transcriptions. This repository's pool comes from the OKHC instead, its evaluation
sentences come from the same corpora (documents disjoint from the pool), and its replay set holds the
open-korean-instructions turns alone (the builder's `komagpie` command adds KoMagpie-raw on your machine).

## Reference numbers

The numbers below come from greedy decoding with the public repo's `rl/jax/evaluate.py` (`it` layout, 256
sentences of `pool/eval.parquet` drawn by seed 0, each in both directions, budget 2x + 8 tokens) on the two
released Flax checkpoints.

| model | direction | terminates | hanja_recall | reading_recall | round_trip | exact |
| --- | --- | --- | --- | --- | --- | --- |
| `cadazar/han2han-it` (`flax`, 762) | Hangul to Hanja | 0.996 | 0.654 | - | 0.970 | 0.113 |
| `cadazar/han2han-it` (`flax`, 762) | Hanja to Hangul | 1.000 | - | 0.952 | 0.973 | 0.422 |
| `cadazar/han2han-rl` (`flax`, 300) | Hangul to Hanja | 1.000 | 0.831 | - | 0.977 | 0.145 |
| `cadazar/han2han-rl` (`flax`, 300) | Hanja to Hangul | 1.000 | - | 0.977 | 0.987 | 0.609 |

The demo article (`rl/demo_article.txt` of the public repo, held out of every split) scores a joined
recall of 0.810 (IT) and 0.855 (RL) in 120-character chunks, and taken whole it scores 0.845 for both. These
sentences are easier than the private held-out set the model cards report (the OKHC rows are cleaner print
with fewer glosses), so the card numbers and these are not comparable to each other, but the IT-to-RL gain
carries over.

## Citations

The pool is derived from the Open Korean Historical Corpus (CC BY-NC 4.0):

```bibtex
@article{song2025open,
  author  = {Seyoung Song and Nawon Kim and Songeun Chae and Kiwoong Park and Jiho Jin and Haneul Yoo and Kyunghyun Cho and Alice Oh},
  journal = {ArXiv preprint},
  title   = {Open Korean Historical Corpus: A Millennia-Scale Diachronic Collection of Public Domain Texts},
  url     = {https://arxiv.org/abs/2510.24541},
  volume  = {abs/2510.24541},
  year    = {2025}
}
```

The replay rows are derived from heegyu/open-korean-instructions (MIT license, Heegyu Kim, 2023,
https://huggingface.co/datasets/heegyu/open-korean-instructions, code at
https://github.com/HeegyuKim/open-korean-instructions) and, when fetched, from channelcorp/KoMagpie-raw
(Channel Corp., 2024, https://huggingface.co/datasets/channelcorp/KoMagpie-raw, with no dataset license
stated), a Korean adaptation of the Magpie method:

```bibtex
@misc{kim2023openkoreaninstructions,
  author = {Heegyu Kim},
  title  = {open-korean-instructions},
  year   = {2023},
  url    = {https://huggingface.co/datasets/heegyu/open-korean-instructions}
}

@misc{channelcorp2024komagpie,
  author = {Channel Corp.},
  title  = {KoMagpie-raw},
  year   = {2024},
  url    = {https://huggingface.co/datasets/channelcorp/KoMagpie-raw}
}

@article{xu2024magpie,
  title   = {Magpie: Alignment Data Synthesis from Scratch by Prompting Aligned LLMs with Nothing},
  author  = {Zhangchen Xu and Fengqing Jiang and Luyao Niu and Yuntian Deng and Radha Poovendran and Yejin Choi and Bill Yuchen Lin},
  journal = {arXiv preprint arXiv:2406.08464},
  year    = {2024}
}
```
