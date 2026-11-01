---
license: other
task_categories:
- text-generation
language:
- zh
- en
- ja
- ko
- vi
- id
- th
tags:
- pretraining-corpus
- traditional-chinese
- taiwan
- multilingual
- tokenizer-training
pretty_name: Taiwan OmniData R1 Pretrain
size_categories:
- 10B<n<100B
---

<!-- # Taiwan OmniData R1 Pretrain

This dataset export contains train-allowed processed text prepared for a
Taiwan-focused multilingual 1B foundation model.  Eval holdout and
research-only roots are excluded from this export by default.

The main pool is materialized from exact-dedup winner row pointers.  Add-on
code/math shards are included with a global hash guard when they were produced
after the exact-dedup inventory.

See `manifests/export_summary.json` for counts, source mix, and safety notes.

Current export summary:

```json
{
  "updated_at": "2026-06-07T06:29:53Z",
  "files": {
    "status_written": 24354,
    "input_rows": 53638978,
    "selected_rows": 42965012,
    "estimated_tokens": 21066437768,
    "status_empty": 3948,
    "status_exists": 12
  },
  "top_sources": [
    [
      "fineweb_2",
      9168153
    ],
    [
      "pretrain_chinese_zhtw",
      6354951
    ],
    [
      "ultra_fineweb_l3_en_multi_style",
      5159862
    ],
    [
      "fineweb_2_jpn_jpan",
      4840113
    ],
    [
      "traditional_chinese_common_crawl_filtered",
      4316919
    ],
    [
      "fineweb_2_kor_hang",
      3717519
    ],
    [
      "c4_chinese_zhtw",
      2086123
    ],
    [
      "fineweb_2_fra_latn",
      1030562
    ],
    [
      "fineweb_2_deu_latn",
      984821
    ],
    [
      "fineweb_2_spa_latn",
      907306
    ],
    [
      "fineweb_2_por_latn",
      549861
    ],
    [
      "nemotron_sft_math_v4",
      545087
    ],
    [
      "code_search_net_php",
      409776
    ],
    [
      "code_search_net_python",
      374707
    ],
    [
      "code_search_net_java",
      332044
    ],
    [
      "fineweb_edu",
      281254
    ],
    [
      "fineweb_2_yue_hani",
      261179
    ],
    [
      "zhwikisource_zhtw",
      231345
    ],
    [
      "fineweb_2_vie_latn",
      183991
    ],
    [
      "fineweb_2_tha_thai",
      167311
    ],
    [
      "code_search_net_go",
      167283
    ],
    [
      "fineweb_2_zsm_latn",
      135356
    ],
    [
      "fineweb_2_fil_latn",
      128906
    ],
    [
      "finewiki",
      116475
    ],
    [
      "code_search_net_javascript",
      98781
    ],
    [
      "fineweb_2_ind_latn",
      89783
    ],
    [
      "taiwan_edoctor_qa",
      72776
    ],
    [
      "fineweb_2_rus_cyrl",
      60133
    ],
    [
      "finepdfs_edu",
      50487
    ],
    [
      "fineweb_2_hin_deva",
      40864
    ],
    [
      "fineweb_2_arb_arab",
      37747
    ],
    [
      "code_search_net_ruby",
      28990
    ],
    [
      "moda_ai_corpus_20260601",
      8934
    ],
    [
      "wikinews_zhtw",
      8234
    ],
    [
      "taiwan_netizen",
      7366
    ],
    [
      "taiwan_minnan_dictionary",
      2647
    ],
    [
      "taiwan_legislator_transcript_aigrant_10_5",
      1162
    ],
    [
      "taiwan_legislator_transcript_aigrant_11_1",
      1152
    ],
    [
      "taiwan_legislator_transcript_aigrant_10_7",
      1134
    ],
    [
      "taiwan_legislator_transcript_aigrant_10_6",
      944
    ],
    [
      "taiwan_ly_law_research_aigrant",
      712
    ],
    [
      "taiwan_legislator_transcript_aigrant_11_2",
      536
    ],
    [
      "taiwan_legislator_transcript_aigrant_10_8",
      476
    ],
    [
      "taiwan_corpus_zhtw_howard",
      346
    ],
    [
      "zh_taiwan_lianghsun",
      281
    ],
    [
      "tw_processed_law_ctx",
      277
    ],
    [
      "awesome_taiwan_knowledge_social_studies_elem_jhs",
      127
    ],
    [
      "taiwan_dentist_knowledge_zhtw",
      102
    ],
    [
      "taiwan_law_judgement_jamie",
      86
    ],
    [
      "awesome_taiwan_knowledge_civics_studies_hs",
      14
    ]
  ],
  "languages": [
    [
      "zh",
      22922625
    ],
    [
      "en",
      10484840
    ],
    [
      "ja",
      4421347
    ],
    [
      "ko",
      3712945
    ],
    [
      "code-php",
      409776
    ],
    [
      "code-python",
      374707
    ],
    [
      "code-java",
      332044
    ],
    [
      "code-go",
      167283
    ],
    [
      "code-javascript",
      98781
    ],
    [
      "code-ruby",
      28990
    ],
    [
      "unknown",
      10927
    ],
    [
      "multilingual",
      746
    ],
    [
      "nan",
      1
    ]
  ],
  "domains": [
    [
      "general_web",
      33745587
    ],
    [
      "finance",
      1920245
    ],
    [
      "code",
      1454184
    ],
    [
      "medicine",
      1240725
    ],
    [
      "education",
      1168532
    ],
    [
      "math",
      1000216
    ],
    [
      "law",
      680549
    ],
    [
      "government",
      617316
    ],
    [
      "wiki",
      374753
    ],
    [
      "patent",
      357579
    ],
    [
      "transcript",
      261083
    ],
    [
      "pdf",
      136877
    ],
    [
      "social",
      7366
    ]
  ],
  "dataset": "voidful/tw-pretrain",
  "created_at": "2026-06-06T23:21:41Z",
  "input_roots": [
    "/tmp/omnidata_storage_sshfs_twpre_hf_20260607_072140_239132/taiwan_omnidata_balance_v3/data/tw_filtered",
    "/tmp/omnidata_storage_sshfs_twpre_hf_20260607_072140_239132/taiwan_omnidata/data/tw_filtered",
    "/tmp/omnidata_storage_sshfs_twpre_hf_20260607_072140_239132/taiwan_omnidata/data/tw_domain_filtered"
  ],
  "exact_dir": "/tmp/omnidata_storage_sshfs_twpre_hf_20260607_072140_239132/taiwan_omnidata_balance_v3/work/dedup_token_v1/exact_buckets",
  "extra_prefixes": [
    "code_search_net",
    "nemotron_sft_math_v4"
  ],
  "eval_holdout_excluded": true,
  "research_only_excluded": true
}
```
 -->