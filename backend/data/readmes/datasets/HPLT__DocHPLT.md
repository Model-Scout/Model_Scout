---
task_categories:
- translation
pretty_name: DocHPLT
license: cc0-1.0
configs:
- config_name: af-en
  data_files:
  - split: train
    path: af-en/train-*
- config_name: ar-en
  data_files:
  - split: train
    path: ar-en/train-*
- config_name: az-en
  data_files:
  - split: train
    path: az-en/train-*
- config_name: be-en
  data_files:
  - split: train
    path: be-en/train-*
- config_name: bg-en
  data_files:
  - split: train
    path: bg-en/train-*
- config_name: bn-en
  data_files:
  - split: train
    path: bn-en/train-*
- config_name: bs-en
  data_files:
  - split: train
    path: bs-en/train-*
- config_name: ca-en
  data_files:
  - split: train
    path: ca-en/train-*
- config_name: cy-en
  data_files:
  - split: train
    path: cy-en/train-*
- config_name: en-eo
  data_files:
  - split: train
    path: en-eo/train-*
- config_name: en-et
  data_files:
  - split: train
    path: en-et/train-*
- config_name: en-eu
  data_files:
  - split: train
    path: en-eu/train-*
- config_name: en-fa
  data_files:
  - split: train
    path: en-fa/train-*
- config_name: en-fi
  data_files:
  - split: train
    path: en-fi/train-*
- config_name: en-ga
  data_files:
  - split: train
    path: en-ga/train-*
- config_name: en-gl
  data_files:
  - split: train
    path: en-gl/train-*
- config_name: en-gu
  data_files:
  - split: train
    path: en-gu/train-*
- config_name: en-he
  data_files:
  - split: train
    path: en-he/train-*
- config_name: en-hi
  data_files:
  - split: train
    path: en-hi/train-*
- config_name: en-hr
  data_files:
  - split: train
    path: en-hr/train-*
- config_name: en-is
  data_files:
  - split: train
    path: en-is/train-*
- config_name: en-ja
  data_files:
  - split: train
    path: en-ja/train-*
- config_name: en-kk
  data_files:
  - split: train
    path: en-kk/train-*
- config_name: en-kn
  data_files:
  - split: train
    path: en-kn/train-*
- config_name: en-ko
  data_files:
  - split: train
    path: en-ko/train-*
- config_name: en-lt
  data_files:
  - split: train
    path: en-lt/train-*
- config_name: en-lv
  data_files:
  - split: train
    path: en-lv/train-*
- config_name: en-mk
  data_files:
  - split: train
    path: en-mk/train-*
- config_name: en-ml
  data_files:
  - split: train
    path: en-ml/train-*
- config_name: en-mr
  data_files:
  - split: train
    path: en-mr/train-*
- config_name: en-ms
  data_files:
  - split: train
    path: en-ms/train-*
- config_name: en-mt
  data_files:
  - split: train
    path: en-mt/train-*
- config_name: en-nb
  data_files:
  - split: train
    path: en-nb/train-*
- config_name: en-ne
  data_files:
  - split: train
    path: en-ne/train-*
- config_name: en-nn
  data_files:
  - split: train
    path: en-nn/train-*
- config_name: en-si
  data_files:
  - split: train
    path: en-si/train-*
- config_name: en-sk
  data_files:
  - split: train
    path: en-sk/train-*
- config_name: en-sl
  data_files:
  - split: train
    path: en-sl/train-*
- config_name: en-sq
  data_files:
  - split: train
    path: en-sq/train-*
- config_name: en-sr
  data_files:
  - split: train
    path: en-sr/train-*
- config_name: en-sw
  data_files:
  - split: train
    path: en-sw/train-*
- config_name: en-ta
  data_files:
  - split: train
    path: en-ta/train-*
- config_name: en-te
  data_files:
  - split: train
    path: en-te/train-*
- config_name: en-th
  data_files:
  - split: train
    path: en-th/train-*
- config_name: en-tr
  data_files:
  - split: train
    path: en-tr/train-*
- config_name: en-uk
  data_files:
  - split: train
    path: en-uk/train-*
- config_name: en-ur
  data_files:
  - split: train
    path: en-ur/train-*
- config_name: en-uz
  data_files:
  - split: train
    path: en-uz/train-*
- config_name: en-vi
  data_files:
  - split: train
    path: en-vi/train-*
- config_name: en-xh
  data_files:
  - split: train
    path: en-xh/train-*
dataset_info:
- config_name: af-en
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 22358649843
    num_examples: 1121166
  download_size: 6420749115
  dataset_size: 22358649843
- config_name: ar-en
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 59976082701
    num_examples: 4405876
  download_size: 18101162292
  dataset_size: 59976082701
- config_name: az-en
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 9761021558
    num_examples: 732657
  download_size: 3230027086
  dataset_size: 9761021558
- config_name: be-en
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 17794069162
    num_examples: 709129
  download_size: 4891873734
  dataset_size: 17794069162
- config_name: bg-en
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 115730817966
    num_examples: 6016906
  download_size: 29666540041
  dataset_size: 115730817966
- config_name: bn-en
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 20126586227
    num_examples: 1039423
  download_size: 5708813704
  dataset_size: 20126586227
- config_name: bs-en
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 24390337420
    num_examples: 1443819
  download_size: 9042173278
  dataset_size: 24390337420
- config_name: ca-en
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 55458858786
    num_examples: 3582267
  download_size: 14165516331
  dataset_size: 55458858786
- config_name: cy-en
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 8160091003
    num_examples: 721671
  download_size: 2194090780
  dataset_size: 8160091003
- config_name: en-eo
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 11119912951
    num_examples: 482452
  download_size: 3579791686
  dataset_size: 11119912951
- config_name: en-et
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 32504496087
    num_examples: 2484493
  download_size: 8485275146
  dataset_size: 32504496087
- config_name: en-eu
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 9212907749
    num_examples: 616924
  download_size: 2665115080
  dataset_size: 9212907749
- config_name: en-fa
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 31868757760
    num_examples: 1880900
  download_size: 11087245724
  dataset_size: 31868757760
- config_name: en-fi
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 116095268602
    num_examples: 8532601
  download_size: 30930621647
  dataset_size: 116095268602
- config_name: en-ga
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 7354208540
    num_examples: 557716
  download_size: 1883382887
  dataset_size: 7354208540
- config_name: en-gl
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 20512180365
    num_examples: 988176
  download_size: 5395235669
  dataset_size: 20512180365
- config_name: en-gu
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 8750941653
    num_examples: 306386
  download_size: 2590802601
  dataset_size: 8750941653
- config_name: en-he
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 67517278909
    num_examples: 4190235
  download_size: 17424526451
  dataset_size: 67517278909
- config_name: en-hi
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 63754996835
    num_examples: 3502520
  download_size: 16763008416
  dataset_size: 63754996835
- config_name: en-hr
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 56347559942
    num_examples: 3574689
  download_size: 17648971457
  dataset_size: 56347559942
- config_name: en-is
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 12303082236
    num_examples: 1097797
  download_size: 2919568556
  dataset_size: 12303082236
- config_name: en-ja
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 149053658382
    num_examples: 11828819
  download_size: 33732853390
  dataset_size: 149053658382
- config_name: en-kk
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 4693507590
    num_examples: 243579
  download_size: 1582927547
  dataset_size: 4693507590
- config_name: en-kn
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 14712100389
    num_examples: 355117
  download_size: 4490569934
  dataset_size: 14712100389
- config_name: en-ko
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 96400745506
    num_examples: 6479547
  download_size: 24180345919
  dataset_size: 96400745506
- config_name: en-lt
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 54837624270
    num_examples: 3948829
  download_size: 14055131892
  dataset_size: 54837624270
- config_name: en-lv
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 43407120452
    num_examples: 3104028
  download_size: 11196695115
  dataset_size: 43407120452
- config_name: en-mk
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 22277476487
    num_examples: 961749
  download_size: 5523135715
  dataset_size: 22277476487
- config_name: en-ml
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 7623801522
    num_examples: 298334
  download_size: 2294982186
  dataset_size: 7623801522
- config_name: en-mr
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 7164228248
    num_examples: 372093
  download_size: 1893386345
  dataset_size: 7164228248
- config_name: en-ms
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 54411456134
    num_examples: 3887463
  download_size: 13673083185
  dataset_size: 54411456134
- config_name: en-mt
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 7666652010
    num_examples: 477497
  download_size: 2052953262
  dataset_size: 7666652010
- config_name: en-nb
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 77161771791
    num_examples: 6596166
  download_size: 18832477209
  dataset_size: 77161771791
- config_name: en-ne
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 3512600229
    num_examples: 201928
  download_size: 933640903
  dataset_size: 3512600229
- config_name: en-nn
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 6862120980
    num_examples: 413279
  download_size: 1906238338
  dataset_size: 6862120980
- config_name: en-si
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 3007242665
    num_examples: 123803
  download_size: 930237057
  dataset_size: 3007242665
- config_name: en-sk
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 74031640810
    num_examples: 5262604
  download_size: 19881005009
  dataset_size: 74031640810
- config_name: en-sl
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 35933793189
    num_examples: 2334208
  download_size: 10336952393
  dataset_size: 35933793189
- config_name: en-sq
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 14113013582
    num_examples: 910599
  download_size: 4306640874
  dataset_size: 14113013582
- config_name: en-sr
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 30975081361
    num_examples: 1307126
  download_size: 8678958986
  dataset_size: 30975081361
- config_name: en-sw
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 10983471412
    num_examples: 581466
  download_size: 3235928094
  dataset_size: 10983471412
- config_name: en-ta
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 14662239728
    num_examples: 583034
  download_size: 4247034783
  dataset_size: 14662239728
- config_name: en-te
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 14704704726
    num_examples: 389858
  download_size: 4497942897
  dataset_size: 14704704726
- config_name: en-th
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 43677411449
    num_examples: 2438548
  download_size: 10575432061
  dataset_size: 43677411449
- config_name: en-tr
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 131133010876
    num_examples: 11815778
  download_size: 36215027493
  dataset_size: 131133010876
- config_name: en-uk
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 97977680700
    num_examples: 5364321
  download_size: 28351254902
  dataset_size: 97977680700
- config_name: en-ur
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 12283592252
    num_examples: 618996
  download_size: 3406884081
  dataset_size: 12283592252
- config_name: en-uz
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 2736224953
    num_examples: 156796
  download_size: 975374985
  dataset_size: 2736224953
- config_name: en-vi
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 77449013097
    num_examples: 5089734
  download_size: 23580718561
  dataset_size: 77449013097
- config_name: en-xh
  features:
  - name: src_doc_id
    dtype: string
  - name: tgt_doc_id
    dtype: string
  - name: lang_pair
    dtype: string
  - name: src_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: tgt_doc
    struct:
    - name: ids
      sequence: string
    - name: sentences
      sequence: string
  - name: alignment
    list:
    - name: src
      list: string
    - name: tgt
      list: string
    - name: aligner-score
      dtype: float32
    - name: bicleaner-score
      dtype: float32
    - name: bifixer-score
      dtype: float32
  splits:
  - name: train
    num_bytes: 1058497082
    num_examples: 44001
  download_size: 408345394
  dataset_size: 1058497082
language:
- af
- ar
- az
- bg
- be
- bn
- bs
- ca
- cy
- eo
- et
- eu
- fa
- fi
- ga
- gl
- gu
- he
- hi
- hr
- is
- ja
- kk
- kn
- ko
- lt
- lv
- mk
- ml
- mr
- ms
- mt
- nb
- ne
- nn
- si
- sk
- sl
- sq
- sr
- sw
- ta
- te
- th
- tr
- uk
- ur
- uz
- vi
- xh
---


# DocHPLT: A Massively Multilingual Document-Level Translation Dataset

Existing document-level machine translation resources are only available for a handful of languages, mostly high-resourced ones. To facilitate the training and evaluation of document-level translation and, more broadly, long-context modeling for global communities, we create DocHPLT, the largest publicly available document-level translation dataset to date. It contains 124 million aligned document pairs across 50 languages paired with English, comprising 4.26 billion sentences, with further possibility to provide 2500 bonus pairs not involving English. Unlike previous reconstruction-based approaches that piece together documents from sentence-level data, we modify an existing web extraction pipeline to preserve complete document integrity from the source, retaining all content including un- aligned portions. After our preliminary experiments identify the optimal training context strategy for document-level translation, we demonstrate that LLMs fine-tuned on DocHPLT substantially outperform off-the-shelf instruction- tuned baselines, with particularly dramatic improvements for under-resourced languages. We open-source the dataset under a permissive license, providing essential infrastructure for advancing multilingual document-level translation.


## Corpus statistics

|       | **#sentences** | **#docs**  |
|-----------|----------------|------------|
| **af**    | 16,416,841     | 297,636    |
| **ar**    | 65,482,300     | 2,271,167  |
| **az**    | 12,202,189     | 332,742    |
| **be**    | 10,672,952     | 212,121    |
| **bg**    | 80,018,549     | 1,746,301  |
| **bn**    | 10,473,372     | 414,099    |
| **bs**    | 20,635,243     | 514,615    |
| **ca**    | 47,905,003     | 1,198,217  |
| **cy**    | 8,908,119      | 265,261    |
| **en**    | 2,665,945,834  | 47,484,349 |
| **eo**    | 6,115,355      | 119,196    |
| **et**    | 33,684,509     | 774,561    |
| **eu**    | 6,783,654      | 189,347    |
| **fa**    | 24,837,952     | 810,029    |
| **fi**    | 111,615,913    | 2,445,791  |
| **ga**    | 6,398,081      | 172,167    |
| **gl**    | 10,657,570     | 233,545    |
| **gu**    | 3,202,679      | 108,507    |
| **he**    | 38,077,820     | 1,190,198  |
| **hi**    | 37,592,475     | 1,336,090  |
| **hr**    | 52,267,826     | 1,063,347  |
| **is**    | 12,571,982     | 274,078    |
| **ja**    | 164,136,152    | 4,032,689  |
| **kk**    | 5,948,866      | 140,082    |
| **kn**    | 4,463,262      | 123,053    |
| **ko**    | 84,527,642     | 2,058,811  |
| **lt**    | 48,692,264     | 1,031,628  |
| **lv**    | 37,426,957     | 796,659    |
| **mk**    | 12,465,228     | 307,055    |
| **ml**    | 2,925,457      | 115,189    |
| **mr**    | 3,066,703      | 128,808    |
| **ms**    | 51,150,528     | 978,185    |
| **mt**    | 6,328,544      | 141,088    |
| **nb**    | 89,189,502     | 1,884,362  |
| **ne**    | 1,549,852      | 74,579     |
| **nn**    | 4,228,079      | 93,285     |
| **si**    | 1,497,375      | 50,605     |
| **sk**    | 70,057,465     | 1,461,804  |
| **sl**    | 37,501,647     | 797,858    |
| **sq**    | 11,475,561     | 328,651    |
| **sr**    | 21,620,629     | 407,440    |
| **sw**    | 8,409,824      | 185,287    |
| **ta**    | 6,790,864      | 215,564    |
| **te**    | 5,131,680      | 141,279    |
| **th**    | 16,134,265     | 676,699    |
| **tr**    | 100,380,235    | 3,884,137  |
| **uk**    | 89,841,883     | 1,955,041  |
| **ur**    | 5,479,098      | 234,708    |
| **uz**    | 3,502,356      | 69,440     |
| **vi**    | 87,511,126     | 1,986,258  |
| **xh**    | 995,556        | 21,561     |
| **total** | **4,264,894,818**  | **87,775,169** |

Link for arXiv preprint: [https://arxiv.org/abs/2508.13079](https://arxiv.org/abs/2508.13079)

This project has received funding from the European Union's Horizon Europe research and innovation programme under grant agreement No 101070350 and from UK Research and Innovation (UKRI) under the UK government’s Horizon Europe funding guarantee [grant number 10052546].

## Citation

If you use this resource, please kindly cite:  
```
@article{dochplt,
      title={{DocHPLT}: A Massively Multilingual Document-Level Translation Dataset}, 
      author={Dayyán O'Brien and Bhavitvya Malik and Ona de Gibert and Pinzhen Chen and Barry Haddow and Jörg Tiedemann},
      year={2025},
      journal={arXiv preprint},
      url={https://arxiv.org/abs/2508.13079}, 
}
```