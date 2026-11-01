---
annotations_creators:
- crowdsourced
language_creators:
- machine-generated
language:
- en
license:
- cc-by-4.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- acceptability-classification
paperswithcode_id: blimp
pretty_name: BLiMP
dataset_info:
- config_name: adjunct_island
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 165894
    num_examples: 1000
  download_size: 62231
  dataset_size: 165894
- config_name: anaphor_gender_agreement
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 130918
    num_examples: 1000
  download_size: 39201
  dataset_size: 130918
- config_name: anaphor_number_agreement
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 139879
    num_examples: 1000
  download_size: 41547
  dataset_size: 139879
- config_name: animate_subject_passive
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 144423
    num_examples: 1000
  download_size: 47282
  dataset_size: 144423
- config_name: animate_subject_trans
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 127798
    num_examples: 1000
  download_size: 49651
  dataset_size: 127798
- config_name: causative
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 122772
    num_examples: 1000
  download_size: 48963
  dataset_size: 122772
- config_name: complex_NP_island
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 198972
    num_examples: 1000
  download_size: 78211
  dataset_size: 198972
- config_name: coordinate_structure_constraint_complex_left_branch
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 210912
    num_examples: 1000
  download_size: 67908
  dataset_size: 210912
- config_name: coordinate_structure_constraint_object_extraction
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 171655
    num_examples: 1000
  download_size: 51584
  dataset_size: 171655
- config_name: determiner_noun_agreement_1
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 156120
    num_examples: 1000
  download_size: 49893
  dataset_size: 156120
- config_name: determiner_noun_agreement_2
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 156204
    num_examples: 1000
  download_size: 49527
  dataset_size: 156204
- config_name: determiner_noun_agreement_irregular_1
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 164473
    num_examples: 1000
  download_size: 47274
  dataset_size: 164473
- config_name: determiner_noun_agreement_irregular_2
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 161074
    num_examples: 1000
  download_size: 47422
  dataset_size: 161074
- config_name: determiner_noun_agreement_with_adj_2
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 179666
    num_examples: 1000
  download_size: 56346
  dataset_size: 179666
- config_name: determiner_noun_agreement_with_adj_irregular_1
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 184529
    num_examples: 1000
  download_size: 54405
  dataset_size: 184529
- config_name: determiner_noun_agreement_with_adj_irregular_2
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 184396
    num_examples: 1000
  download_size: 54064
  dataset_size: 184396
- config_name: determiner_noun_agreement_with_adjective_1
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 185126
    num_examples: 1000
  download_size: 55682
  dataset_size: 185126
- config_name: distractor_agreement_relational_noun
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 191473
    num_examples: 1000
  download_size: 59641
  dataset_size: 191473
- config_name: distractor_agreement_relative_clause
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 216756
    num_examples: 1000
  download_size: 77897
  dataset_size: 216756
- config_name: drop_argument
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 109806
    num_examples: 1000
  download_size: 39961
  dataset_size: 109806
- config_name: ellipsis_n_bar_1
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 217590
    num_examples: 1000
  download_size: 92776
  dataset_size: 217590
- config_name: ellipsis_n_bar_2
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 233161
    num_examples: 1000
  download_size: 98882
  dataset_size: 233161
- config_name: existential_there_object_raising
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 223741
    num_examples: 1000
  download_size: 76641
  dataset_size: 223741
- config_name: existential_there_quantifiers_1
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 162931
    num_examples: 1000
  download_size: 51576
  dataset_size: 162931
- config_name: existential_there_quantifiers_2
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 164826
    num_examples: 1000
  download_size: 52092
  dataset_size: 164826
- config_name: existential_there_subject_raising
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 200063
    num_examples: 1000
  download_size: 59519
  dataset_size: 200063
- config_name: expletive_it_object_raising
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 238615
    num_examples: 1000
  download_size: 88607
  dataset_size: 238615
- config_name: inchoative
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 104319
    num_examples: 1000
  download_size: 39842
  dataset_size: 104319
- config_name: intransitive
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 111097
    num_examples: 1000
  download_size: 42387
  dataset_size: 111097
- config_name: irregular_past_participle_adjectives
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 144661
    num_examples: 1000
  download_size: 36654
  dataset_size: 144661
- config_name: irregular_past_participle_verbs
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 125692
    num_examples: 1000
  download_size: 37297
  dataset_size: 125692
- config_name: irregular_plural_subject_verb_agreement_1
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 165584
    num_examples: 1000
  download_size: 50725
  dataset_size: 165584
- config_name: irregular_plural_subject_verb_agreement_2
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 153843
    num_examples: 1000
  download_size: 42707
  dataset_size: 153843
- config_name: left_branch_island_echo_question
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 147840
    num_examples: 1000
  download_size: 50481
  dataset_size: 147840
- config_name: left_branch_island_simple_question
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 150060
    num_examples: 1000
  download_size: 50293
  dataset_size: 150060
- config_name: matrix_question_npi_licensor_present
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 153262
    num_examples: 1000
  download_size: 51899
  dataset_size: 153262
- config_name: npi_present_1
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 138465
    num_examples: 1000
  download_size: 51981
  dataset_size: 138465
- config_name: npi_present_2
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 127636
    num_examples: 1000
  download_size: 51661
  dataset_size: 127636
- config_name: only_npi_licensor_present
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 148516
    num_examples: 1000
  download_size: 51361
  dataset_size: 148516
- config_name: only_npi_scope
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 208902
    num_examples: 1000
  download_size: 84970
  dataset_size: 208902
- config_name: passive_1
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 145882
    num_examples: 1000
  download_size: 53931
  dataset_size: 145882
- config_name: passive_2
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 113960
    num_examples: 1000
  download_size: 40499
  dataset_size: 113960
- config_name: principle_A_c_command
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 188490
    num_examples: 1000
  download_size: 67867
  dataset_size: 188490
- config_name: principle_A_case_1
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 170398
    num_examples: 1000
  download_size: 61092
  dataset_size: 170398
- config_name: principle_A_case_2
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 170412
    num_examples: 1000
  download_size: 56430
  dataset_size: 170412
- config_name: principle_A_domain_1
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 171170
    num_examples: 1000
  download_size: 59120
  dataset_size: 171170
- config_name: principle_A_domain_2
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 165333
    num_examples: 1000
  download_size: 58464
  dataset_size: 165333
- config_name: principle_A_domain_3
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 158998
    num_examples: 1000
  download_size: 52859
  dataset_size: 158998
- config_name: principle_A_reconstruction
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 152104
    num_examples: 1000
  download_size: 44480
  dataset_size: 152104
- config_name: regular_plural_subject_verb_agreement_1
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 158819
    num_examples: 1000
  download_size: 49466
  dataset_size: 158819
- config_name: regular_plural_subject_verb_agreement_2
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 153609
    num_examples: 1000
  download_size: 43365
  dataset_size: 153609
- config_name: sentential_negation_npi_licensor_present
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 171864
    num_examples: 1000
  download_size: 54830
  dataset_size: 171864
- config_name: sentential_negation_npi_scope
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 232098
    num_examples: 1000
  download_size: 90157
  dataset_size: 232098
- config_name: sentential_subject_island
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 172432
    num_examples: 1000
  download_size: 56666
  dataset_size: 172432
- config_name: superlative_quantifiers_1
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 159290
    num_examples: 1000
  download_size: 48453
  dataset_size: 159290
- config_name: superlative_quantifiers_2
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 159340
    num_examples: 1000
  download_size: 50480
  dataset_size: 159340
- config_name: tough_vs_raising_1
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 148636
    num_examples: 1000
  download_size: 44779
  dataset_size: 148636
- config_name: tough_vs_raising_2
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 169684
    num_examples: 1000
  download_size: 61465
  dataset_size: 169684
- config_name: transitive
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 133104
    num_examples: 1000
  download_size: 55090
  dataset_size: 133104
- config_name: wh_island
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 142340
    num_examples: 1000
  download_size: 52808
  dataset_size: 142340
- config_name: wh_questions_object_gap
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 193045
    num_examples: 1000
  download_size: 70049
  dataset_size: 193045
- config_name: wh_questions_subject_gap
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 195593
    num_examples: 1000
  download_size: 71632
  dataset_size: 195593
- config_name: wh_questions_subject_gap_long_distance
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 268270
    num_examples: 1000
  download_size: 98913
  dataset_size: 268270
- config_name: wh_vs_that_no_gap
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 188872
    num_examples: 1000
  download_size: 71710
  dataset_size: 188872
- config_name: wh_vs_that_no_gap_long_distance
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 247039
    num_examples: 1000
  download_size: 95504
  dataset_size: 247039
- config_name: wh_vs_that_with_gap
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 173386
    num_examples: 1000
  download_size: 60291
  dataset_size: 173386
- config_name: wh_vs_that_with_gap_long_distance
  features:
  - name: sentence_good
    dtype: string
  - name: sentence_bad
    dtype: string
  - name: field
    dtype: string
  - name: linguistics_term
    dtype: string
  - name: UID
    dtype: string
  - name: simple_LM_method
    dtype: bool
  - name: one_prefix_method
    dtype: bool
  - name: two_prefix_method
    dtype: bool
  - name: lexically_identical
    dtype: bool
  - name: pair_id
    dtype: int32
  splits:
  - name: train
    num_bytes: 231595
    num_examples: 1000
  download_size: 84147
  dataset_size: 231595
configs:
- config_name: adjunct_island
  data_files:
  - split: train
    path: adjunct_island/train-*
- config_name: anaphor_gender_agreement
  data_files:
  - split: train
    path: anaphor_gender_agreement/train-*
- config_name: anaphor_number_agreement
  data_files:
  - split: train
    path: anaphor_number_agreement/train-*
- config_name: animate_subject_passive
  data_files:
  - split: train
    path: animate_subject_passive/train-*
- config_name: animate_subject_trans
  data_files:
  - split: train
    path: animate_subject_trans/train-*
- config_name: causative
  data_files:
  - split: train
    path: causative/train-*
- config_name: complex_NP_island
  data_files:
  - split: train
    path: complex_NP_island/train-*
- config_name: coordinate_structure_constraint_complex_left_branch
  data_files:
  - split: train
    path: coordinate_structure_constraint_complex_left_branch/train-*
- config_name: coordinate_structure_constraint_object_extraction
  data_files:
  - split: train
    path: coordinate_structure_constraint_object_extraction/train-*
- config_name: determiner_noun_agreement_1
  data_files:
  - split: train
    path: determiner_noun_agreement_1/train-*
- config_name: determiner_noun_agreement_2
  data_files:
  - split: train
    path: determiner_noun_agreement_2/train-*
- config_name: determiner_noun_agreement_irregular_1
  data_files:
  - split: train
    path: determiner_noun_agreement_irregular_1/train-*
- config_name: determiner_noun_agreement_irregular_2
  data_files:
  - split: train
    path: determiner_noun_agreement_irregular_2/train-*
- config_name: determiner_noun_agreement_with_adj_2
  data_files:
  - split: train
    path: determiner_noun_agreement_with_adj_2/train-*
- config_name: determiner_noun_agreement_with_adj_irregular_1
  data_files:
  - split: train
    path: determiner_noun_agreement_with_adj_irregular_1/train-*
- config_name: determiner_noun_agreement_with_adj_irregular_2
  data_files:
  - split: train
    path: determiner_noun_agreement_with_adj_irregular_2/train-*
- config_name: determiner_noun_agreement_with_adjective_1
  data_files:
  - split: train
    path: determiner_noun_agreement_with_adjective_1/train-*
- config_name: distractor_agreement_relational_noun
  data_files:
  - split: train
    path: distractor_agreement_relational_noun/train-*
- config_name: distractor_agreement_relative_clause
  data_files:
  - split: train
    path: distractor_agreement_relative_clause/train-*
- config_name: drop_argument
  data_files:
  - split: train
    path: drop_argument/train-*
- config_name: ellipsis_n_bar_1
  data_files:
  - split: train
    path: ellipsis_n_bar_1/train-*
- config_name: ellipsis_n_bar_2
  data_files:
  - split: train
    path: ellipsis_n_bar_2/train-*
- config_name: existential_there_object_raising
  data_files:
  - split: train
    path: existential_there_object_raising/train-*
- config_name: existential_there_quantifiers_1
  data_files:
  - split: train
    path: existential_there_quantifiers_1/train-*
- config_name: existential_there_quantifiers_2
  data_files:
  - split: train
    path: existential_there_quantifiers_2/train-*
- config_name: existential_there_subject_raising
  data_files:
  - split: train
    path: existential_there_subject_raising/train-*
- config_name: expletive_it_object_raising
  data_files:
  - split: train
    path: expletive_it_object_raising/train-*
- config_name: inchoative
  data_files:
  - split: train
    path: inchoative/train-*
- config_name: intransitive
  data_files:
  - split: train
    path: intransitive/train-*
- config_name: irregular_past_participle_adjectives
  data_files:
  - split: train
    path: irregular_past_participle_adjectives/train-*
- config_name: irregular_past_participle_verbs
  data_files:
  - split: train
    path: irregular_past_participle_verbs/train-*
- config_name: irregular_plural_subject_verb_agreement_1
  data_files:
  - split: train
    path: irregular_plural_subject_verb_agreement_1/train-*
- config_name: irregular_plural_subject_verb_agreement_2
  data_files:
  - split: train
    path: irregular_plural_subject_verb_agreement_2/train-*
- config_name: left_branch_island_echo_question
  data_files:
  - split: train
    path: left_branch_island_echo_question/train-*
- config_name: left_branch_island_simple_question
  data_files:
  - split: train
    path: left_branch_island_simple_question/train-*
- config_name: matrix_question_npi_licensor_present
  data_files:
  - split: train
    path: matrix_question_npi_licensor_present/train-*
- config_name: npi_present_1
  data_files:
  - split: train
    path: npi_present_1/train-*
- config_name: npi_present_2
  data_files:
  - split: train
    path: npi_present_2/train-*
- config_name: only_npi_licensor_present
  data_files:
  - split: train
    path: only_npi_licensor_present/train-*
- config_name: only_npi_scope
  data_files:
  - split: train
    path: only_npi_scope/train-*
- config_name: passive_1
  data_files:
  - split: train
    path: passive_1/train-*
- config_name: passive_2
  data_files:
  - split: train
    path: passive_2/train-*
- config_name: principle_A_c_command
  data_files:
  - split: train
    path: principle_A_c_command/train-*
- config_name: principle_A_case_1
  data_files:
  - split: train
    path: principle_A_case_1/train-*
- config_name: principle_A_case_2
  data_files:
  - split: train
    path: principle_A_case_2/train-*
- config_name: principle_A_domain_1
  data_files:
  - split: train
    path: principle_A_domain_1/train-*
- config_name: principle_A_domain_2
  data_files:
  - split: train
    path: principle_A_domain_2/train-*
- config_name: principle_A_domain_3
  data_files:
  - split: train
    path: principle_A_domain_3/train-*
- config_name: principle_A_reconstruction
  data_files:
  - split: train
    path: principle_A_reconstruction/train-*
- config_name: regular_plural_subject_verb_agreement_1
  data_files:
  - split: train
    path: regular_plural_subject_verb_agreement_1/train-*
- config_name: regular_plural_subject_verb_agreement_2
  data_files:
  - split: train
    path: regular_plural_subject_verb_agreement_2/train-*
- config_name: sentential_negation_npi_licensor_present
  data_files:
  - split: train
    path: sentential_negation_npi_licensor_present/train-*
- config_name: sentential_negation_npi_scope
  data_files:
  - split: train
    path: sentential_negation_npi_scope/train-*
- config_name: sentential_subject_island
  data_files:
  - split: train
    path: sentential_subject_island/train-*
- config_name: superlative_quantifiers_1
  data_files:
  - split: train
    path: superlative_quantifiers_1/train-*
- config_name: superlative_quantifiers_2
  data_files:
  - split: train
    path: superlative_quantifiers_2/train-*
- config_name: tough_vs_raising_1
  data_files:
  - split: train
    path: tough_vs_raising_1/train-*
- config_name: tough_vs_raising_2
  data_files:
  - split: train
    path: tough_vs_raising_2/train-*
- config_name: transitive
  data_files:
  - split: train
    path: transitive/train-*
- config_name: wh_island
  data_files:
  - split: train
    path: wh_island/train-*
- config_name: wh_questions_object_gap
  data_files:
  - split: train
    path: wh_questions_object_gap/train-*
- config_name: wh_questions_subject_gap
  data_files:
  - split: train
    path: wh_questions_subject_gap/train-*
- config_name: wh_questions_subject_gap_long_distance
  data_files:
  - split: train
    path: wh_questions_subject_gap_long_distance/train-*
- config_name: wh_vs_that_no_gap
  data_files:
  - split: train
    path: wh_vs_that_no_gap/train-*
- config_name: wh_vs_that_no_gap_long_distance
  data_files:
  - split: train
    path: wh_vs_that_no_gap_long_distance/train-*
- config_name: wh_vs_that_with_gap
  data_files:
  - split: train
    path: wh_vs_that_with_gap/train-*
- config_name: wh_vs_that_with_gap_long_distance
  data_files:
  - split: train
    path: wh_vs_that_with_gap_long_distance/train-*
---

# Dataset Card for "blimp"

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:**
- **Repository:** https://github.com/alexwarstadt/blimp
- **Paper:** [BLiMP: The Benchmark of Linguistic Minimal Pairs for English](https://doi.org/10.1162/tacl_a_00321)
- **Paper:** https://arxiv.org/abs/1912.00582
- **Point of Contact:** [More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)
- **Size of downloaded dataset files:** 29.58 MB
- **Size of the generated dataset:** 11.45 MB
- **Total amount of disk used:** 41.03 MB

### Dataset Summary

BLiMP is a challenge set for evaluating what language models (LMs) know about
major grammatical phenomena in English. BLiMP consists of 67 sub-datasets, each
containing 1000 minimal pairs isolating specific contrasts in syntax,
morphology, or semantics. The data is automatically generated according to
expert-crafted grammars.

### Supported Tasks and Leaderboards

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Languages

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Dataset Structure

### Data Instances

#### adjunct_island

- **Size of downloaded dataset files:** 0.36 MB
- **Size of the generated dataset:** 0.17 MB
- **Total amount of disk used:** 0.52 MB

An example of 'train' looks as follows.
```
{
    "UID": "tough_vs_raising_1",
    "field": "syntax_semantics",
    "lexically_identical": false,
    "linguistics_term": "control_raising",
    "one_prefix_method": false,
    "pair_id": 2,
    "sentence_bad": "Benjamin's tutor was certain to boast about.",
    "sentence_good": "Benjamin's tutor was easy to boast about.",
    "simple_LM_method": true,
    "two_prefix_method": false
}
```

#### anaphor_gender_agreement

- **Size of downloaded dataset files:** 0.44 MB
- **Size of the generated dataset:** 0.14 MB
- **Total amount of disk used:** 0.57 MB

An example of 'train' looks as follows.
```
{
    "UID": "tough_vs_raising_1",
    "field": "syntax_semantics",
    "lexically_identical": false,
    "linguistics_term": "control_raising",
    "one_prefix_method": false,
    "pair_id": 2,
    "sentence_bad": "Benjamin's tutor was certain to boast about.",
    "sentence_good": "Benjamin's tutor was easy to boast about.",
    "simple_LM_method": true,
    "two_prefix_method": false
}
```

#### anaphor_number_agreement

- **Size of downloaded dataset files:** 0.45 MB
- **Size of the generated dataset:** 0.14 MB
- **Total amount of disk used:** 0.59 MB

An example of 'train' looks as follows.
```
{
    "UID": "tough_vs_raising_1",
    "field": "syntax_semantics",
    "lexically_identical": false,
    "linguistics_term": "control_raising",
    "one_prefix_method": false,
    "pair_id": 2,
    "sentence_bad": "Benjamin's tutor was certain to boast about.",
    "sentence_good": "Benjamin's tutor was easy to boast about.",
    "simple_LM_method": true,
    "two_prefix_method": false
}
```

#### animate_subject_passive

- **Size of downloaded dataset files:** 0.46 MB
- **Size of the generated dataset:** 0.15 MB
- **Total amount of disk used:** 0.61 MB

An example of 'train' looks as follows.
```
{
    "UID": "tough_vs_raising_1",
    "field": "syntax_semantics",
    "lexically_identical": false,
    "linguistics_term": "control_raising",
    "one_prefix_method": false,
    "pair_id": 2,
    "sentence_bad": "Benjamin's tutor was certain to boast about.",
    "sentence_good": "Benjamin's tutor was easy to boast about.",
    "simple_LM_method": true,
    "two_prefix_method": false
}
```

#### animate_subject_trans

- **Size of downloaded dataset files:** 0.43 MB
- **Size of the generated dataset:** 0.13 MB
- **Total amount of disk used:** 0.57 MB

An example of 'train' looks as follows.
```
{
    "UID": "tough_vs_raising_1",
    "field": "syntax_semantics",
    "lexically_identical": false,
    "linguistics_term": "control_raising",
    "one_prefix_method": false,
    "pair_id": 2,
    "sentence_bad": "Benjamin's tutor was certain to boast about.",
    "sentence_good": "Benjamin's tutor was easy to boast about.",
    "simple_LM_method": true,
    "two_prefix_method": false
}
```

### Data Fields

The data fields are the same among all splits.

#### adjunct_island
- `sentence_good`: a `string` feature.
- `sentence_bad`: a `string` feature.
- `field`: a `string` feature.
- `linguistics_term`: a `string` feature.
- `UID`: a `string` feature.
- `simple_LM_method`: a `bool` feature.
- `one_prefix_method`: a `bool` feature.
- `two_prefix_method`: a `bool` feature.
- `lexically_identical`: a `bool` feature.
- `pair_id`: a `int32` feature.

#### anaphor_gender_agreement
- `sentence_good`: a `string` feature.
- `sentence_bad`: a `string` feature.
- `field`: a `string` feature.
- `linguistics_term`: a `string` feature.
- `UID`: a `string` feature.
- `simple_LM_method`: a `bool` feature.
- `one_prefix_method`: a `bool` feature.
- `two_prefix_method`: a `bool` feature.
- `lexically_identical`: a `bool` feature.
- `pair_id`: a `int32` feature.

#### anaphor_number_agreement
- `sentence_good`: a `string` feature.
- `sentence_bad`: a `string` feature.
- `field`: a `string` feature.
- `linguistics_term`: a `string` feature.
- `UID`: a `string` feature.
- `simple_LM_method`: a `bool` feature.
- `one_prefix_method`: a `bool` feature.
- `two_prefix_method`: a `bool` feature.
- `lexically_identical`: a `bool` feature.
- `pair_id`: a `int32` feature.

#### animate_subject_passive
- `sentence_good`: a `string` feature.
- `sentence_bad`: a `string` feature.
- `field`: a `string` feature.
- `linguistics_term`: a `string` feature.
- `UID`: a `string` feature.
- `simple_LM_method`: a `bool` feature.
- `one_prefix_method`: a `bool` feature.
- `two_prefix_method`: a `bool` feature.
- `lexically_identical`: a `bool` feature.
- `pair_id`: a `int32` feature.

#### animate_subject_trans
- `sentence_good`: a `string` feature.
- `sentence_bad`: a `string` feature.
- `field`: a `string` feature.
- `linguistics_term`: a `string` feature.
- `UID`: a `string` feature.
- `simple_LM_method`: a `bool` feature.
- `one_prefix_method`: a `bool` feature.
- `two_prefix_method`: a `bool` feature.
- `lexically_identical`: a `bool` feature.
- `pair_id`: a `int32` feature.

### Data Splits

|          name          |train|
|------------------------|----:|
|adjunct_island          | 1000|
|anaphor_gender_agreement| 1000|
|anaphor_number_agreement| 1000|
|animate_subject_passive | 1000|
|animate_subject_trans   | 1000|

## Dataset Creation

### Curation Rationale

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

#### Who are the source language producers?

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Annotations

#### Annotation process

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

#### Who are the annotators?

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Personal and Sensitive Information

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Discussion of Biases

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Other Known Limitations

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## Additional Information

### Dataset Curators

[More Information Needed](https://github.com/huggingface/datasets/blob/master/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

### Licensing Information

BLiMP is distributed under a [CC-BY](https://creativecommons.org/licenses/by/4.0/) license. Source: https://github.com/alexwarstadt/blimp#license

### Citation Information

```
@article{warstadt2020blimp,
    author = {Warstadt, Alex and Parrish, Alicia and Liu, Haokun and Mohananey, Anhad and Peng, Wei and Wang, Sheng-Fu and Bowman, Samuel R.},
    title = {BLiMP: The Benchmark of Linguistic Minimal Pairs for English},
    journal = {Transactions of the Association for Computational Linguistics},
    volume = {8},
    number = {},
    pages = {377-392},
    year = {2020},
    doi = {10.1162/tacl\_a\_00321},
    URL = {https://doi.org/10.1162/tacl_a_00321},
    eprint = {https://doi.org/10.1162/tacl_a_00321},
    abstract = { We introduce The Benchmark of Linguistic Minimal Pairs (BLiMP),1 a challenge set for evaluating the linguistic knowledge of language models (LMs) on major grammatical phenomena in English. BLiMP consists of 67 individual datasets, each containing 1,000 minimal pairs—that is, pairs of minimally different sentences that contrast in grammatical acceptability and isolate specific phenomenon in syntax, morphology, or semantics. We generate the data according to linguist-crafted grammar templates, and human aggregate agreement with the labels is 96.4\%. We evaluate n-gram, LSTM, and Transformer (GPT-2 and Transformer-XL) LMs by observing whether they assign a higher probability to the acceptable sentence in each minimal pair. We find that state-of-the-art models identify morphological contrasts related to agreement reliably, but they struggle with some subtle semantic and syntactic phenomena, such as negative polarity items and extraction islands. }
}
```

#### Errata 

Some results were misreported in the published TACL version. Please refer to the corrected version on arXiv: https://arxiv.org/abs/1912.00582


### Contributions

Thanks to [@lhoestq](https://github.com/lhoestq), [@patrickvonplaten](https://github.com/patrickvonplaten), [@thomwolf](https://github.com/thomwolf) for adding this dataset.