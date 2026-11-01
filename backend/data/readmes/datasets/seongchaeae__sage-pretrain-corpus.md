---
license: other
language:
- ko
- en
pretty_name: Sage Pretrain Corpus (v0.8)
task_categories:
- text-generation
size_categories:
- 100M<n<1B
---
# Sage Pretrain Corpus (v0.8)

License-audited Korean/English pretraining corpus for the **Sage** Korean LLM project.

Records: `id`, `text`, `source`, `license`, `meta` (JSON of original fields).

⚠️ **Mixed licenses — `license: other`.** Comply with each source's license individually. CC-BY / ODC-BY require attribution; CC-BY-SA carries ShareAlike.

## Sources (v0.8)

| source | docs | license | origin |
|---|---|---|---|
| fineweb2_ko | 46,470,574 | ODC-BY-1.0 | FineWeb-2 Korean (HuggingFaceFW/fineweb-2 kor_Hang) |
| cosmopedia | 31,062,918 | Apache-2.0 | Cosmopedia (HuggingFaceTB/cosmopedia, 8 configs: auto_math_text, khanacademy, openstax, stanford, stories, web_samples_v1/v2, wikihow) |
| openmath2 | 13,968,554 | CC-BY-4.0 | OpenMathInstruct-2 (nvidia/OpenMathInstruct-2, Llama 3.1 405B generated math problem-solution pairs from GSM8K/MATH; train split) |
| fineweb_edu_sample_10BT | 9,672,101 | ODC-BY-1.0 | HuggingFaceFW/fineweb-edu (sample-10BT variant; English high-quality educational web, FineWeb-Edu classifier score>=3 pre-filtered upstream; ~9.97B tokens exact via dataset's token_count field) |
| finemath_finemath-4plus | 6,698,845 | ODC-BY-1.0 | FineMath (HuggingFaceTB/finemath, finemath-4plus config, quality score >=4) |
| finemath_infiwebmath-4plus | 6,295,931 | ODC-BY-1.0 | FineMath (HuggingFaceTB/finemath, infiwebmath-4plus config, InfiMM-WebMath filtered, quality score >=4) |
| openr1_math | 448,912 | Apache-2.0 | OpenR1-Math-220k (open-r1/OpenR1-Math-220k, DeepSeek-R1 generated reasoning traces; config 'all', generation-expanded from 225K problems) |
| pg19 | 28,600 | Apache-2.0 | Project Gutenberg pre-1919 books (emozilla/pg19 parquet; 28,602 English literature classics, 11.42B chars; narrative/literature domain) |
| numinamath_1.5 | 850,033 | Apache-2.0 | AI-MO/NuminaMath-1.5 (math competition CoT; 896K raw, 850K after validity filter; problem_type: Number Theory, Algebra, Geometry, etc.) |
| bespoke_stratos_17k | 16,710 | Apache-2.0 | bespokelabs/Bespoke-Stratos-17k (DeepSeek-R1 distilled reasoning: math+code+science+puzzle) |
| gsm8k | 7,473 | MIT | openai/gsm8k (grade school math, step-by-step solutions) |
| competition_math | 7,500 | MIT | hendrycks MATH via DigitalLearningGmbH/MATH-lighteval (competition math, 7 subjects, 5 difficulty levels) |
| codeparrot_clean | 3,341,250 | mixed-permissive (apache-2.0/mit/bsd-2-clause/bsd-3-clause/unlicense/isc/cc0-1.0) | codeparrot/codeparrot-clean (Python GitHub code, filtered to permissive licenses from 5.36M files; 62.3% pass) |
| wiki_ko | 891,556 | CC-BY-SA-4.0 | Korean Wikipedia |
| wiki_ko_article | 470,100 | CC-BY-SA-4.0 | Korean Wikipedia (article) |
| wiki_parallel | 255,215 | CC-BY-SA-4.0 | Wikipedia ko-en parallel |
| wiki_en | 6,415,903 | CC-BY-SA-4.0 | English Wikipedia |
| pes2o_cs | 305,673 | ODC-BY-1.0 | Allen Institute peS2o (CS) |
| arxiv_metadata_cs | 935,269 | CC0-1.0 | arXiv metadata (title+abstract); paper license in meta._paper_license |
| acl_2016plus | 30,157 | CC-BY-4.0 | ACL Anthology 2016+ |
| common_pile_arxiv_cs | 130,812 | CC-BY / CC-BY-SA / CC0 (mixed) | Common Pile arxiv_papers_filtered |
| wikipedia_en_cs | 1,056 | CC-BY-SA-4.0 | English Wikipedia (CS) |

Total: **128,305,142** documents.

## Excluded (transparency)

Dropped for licensing/provenance: naver (redistribution-forbidden API), kullm_v2 / openorca / metamath (OpenAI-derived), the_stack_smol (opt-out history), github (unclear license basis).

## Caveats

- CC-BY-SA portions (Wikipedia; part of Common Pile) carry ShareAlike.
- arXiv metadata is CC0; the underlying paper's own license differs and is not granted here.
- common_pile_arxiv_cs is a CC-BY/CC-BY-SA/CC0-filtered arXiv subset.
- ODC-BY-1.0 sources (fineweb2_ko, pes2o_cs, finemath_*) require attribution and inclusion of the same notice in derivative works.
- fineweb2_ko filter: `hangul_ratio>=0.3 AND text_len>=100 AND minhash_cluster_size<=1000` (pass rate 98.98%; file structure `fineweb2_ko/shard_NN_part_PPP.parquet`, 307 parts across 25 shards).
- cosmopedia: Apache-2.0 (Mixtral 8x7B 합성 텍스트, 8 configs 통합). 31.06M docs, 423 parts. Filter: `text_len>=100 AND text_token_length>=50` (pass rate 100%).
- openmath2: CC-BY-4.0 (Llama 3.1 405B 합성 수학 풀이, Nvidia 재공개). 13.97M docs, 140 parts. Filter: `problem>=20 AND solution>=30` (pass rate 99.97%). Format: `Problem: ...\n\nSolution: ...`.
- pg19: Apache-2.0 (emozilla/pg19, deepmind/pg19의 parquet 변환). Project Gutenberg 1919년 이전 영어 문학 28,600권, 11.42B chars, 37 parts. Filter: text_len>=100 (drop 2건). Narrative/literature gap 해결용.
- numinamath_1.5: Apache-2.0 (AI-MO/NuminaMath-1.5). 수학 경시대회 CoT 풀이 850,033건, 9 parts. Filter: problem>=10자 AND solution>=50자 (drop 46,182건, 5.2%). Format: Problem: ...\n\nSolution: ... Meta: answer, problem_type, question_type, source, synthetic.
- bespoke_stratos_17k: Apache-2.0 (bespokelabs/Bespoke-Stratos-17k). DeepSeek-R1 distilled reasoning traces (math 10K + code 5K + science/puzzle 1K). 16,710 docs, 1 part. conversations format (from/value keys).
- gsm8k: MIT (openai/gsm8k). Grade school math 단계별 풀이 7,473건, 1 part. Format: Problem+Solution.
- competition_math: MIT (hendrycks/competition_math via DigitalLearningGmbH/MATH-lighteval). 수학 경시대회 7 주제(Algebra, Geometry, Number Theory 등), 5 난이도. 7,500건, 1 part.
- codeparrot_clean: mixed-permissive (per-file). Python GitHub code (codeparrot/codeparrot-clean), 5,361,373 files raw. Filtered to permissive only: apache-2.0/mit/bsd-2-clause/bsd-3-clause/unlicense/isc/cc0-1.0 (7 licenses). Pass 62.3% (3,341,250). Drop: gpl-2.0/3.0, lgpl, agpl, mpl, epl, artistic (37.7%, 2,020,123). 106 parts. Each file's license preserved in meta.license JSON field. Filter: license whitelist + len(content)>=100.
- fineweb_edu_sample_10BT: ODC-BY-1.0 (HuggingFaceFW/fineweb-edu, sample-10BT variant). 영어 고품질 교육 웹 텍스트 (FineWeb-Edu classifier score>=3 사전 필터됨). 9,672,101 docs, 146 parts. Filter: text_len>=100 (pass 100.00%, drop 0). Total tokens: 9,972,918,177 (~9.97B exact). Complements cosmopedia synthetic (real edu web vs synthetic).
- openr1_math: Apache-2.0 (DeepSeek-R1 추론 trace, open-r1 재공개). 448,912 docs, 21 parts. Strategy: 각 problem의 valid generations마다 1 row (225K problems -> 448K rows, 평균 ~2 generations/problem). Filter: `is_reasoning_complete=True AND generation>=100자`. Format: `Problem: ...\n\nSolution: ...` (DeepSeek-R1의 `<think>...</think>` 토큰 보존).
- finemath_*: ODC-BY-1.0 (HuggingFaceTB/finemath, 4-plus 고품질 부분만 채택). FineMath classifier로 quality score>=4 필터된 수학 교육 웹 텍스트. 13M docs (finemath-4plus 6.70M + infiwebmath-4plus 6.30M), 225 parts. Filter: `text_len>=100`. file structure `finemath/<config>_part_NNNN.parquet`.
- **v0.8**. Adds bespoke_stratos (16.7K DeepSeek-R1 reasoning), gsm8k (7.5K grade school math), competition_math (7.5K competition math). All reasoning data collection complete. Next: Phase 3 — Korean synthesis via Qwen 3.6-35B-A3B.

한국어: 상업적 사용 가능 라이선스만으로 구성한 세이지 한국어 LLM용 정제 코퍼스. v0.8은 v0.7에 추론 데이터 3종 (Stratos 16.7K + GSM8K 7.5K + MATH 7.5K) 추가. 모든 추론 데이터 수집 완료. Phase 3: Qwen 3.6-35B-A3B로 한국어 합성 예정. 소스별 라이선스 준수.
