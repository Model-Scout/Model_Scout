---
license: apache-2.0
language:
- en
- zh
- ar
- bg
- ca
- cs
- da
- de
- el
- es
- et
- fa
- fi
- fr
- he
- hr
- hu
- hy
- id
- is
- it
- ja
- ka
- kk
- ko
- lt
- lv
- mk
- ms
- mt
- nl
- nb
- pl
- pt
- ro
- ru
- sk
- sl
- sq
- sr
- sv
- th
- tr
- uk
- vi
- af
- az
- be
- bs
- cy
- eu
- ga
- gl
tags:
- text-embedding
- contrastive-learning
- retrieval
- sentence-similarity
- multilingual
- bitext-mining
size_categories:
- 10M<n<100M
task_categories:
- text-retrieval
- sentence-similarity
- text-classification
pretty_name: BidirLM-Contrastive
configs:
  - config_name: EmotionClassification
    data_files:
      - path: EmotionClassification/queries.parquet
        split: train
  - config_name: EmotionClassification_corpus
    data_files:
      - path: EmotionClassification/corpus.parquet
        split: train
  - config_name: GooAQ
    data_files:
      - path: GooAQ/queries.parquet
        split: train
  - config_name: GooAQ_corpus
    data_files:
      - path: GooAQ/corpus.parquet
        split: train
  - config_name: MAmmoTH2
    data_files:
      - path: MAmmoTH2/queries.parquet
        split: train
  - config_name: MAmmoTH2_corpus
    data_files:
      - path: MAmmoTH2/corpus.parquet
        split: train
  - config_name: MIRACL
    data_files:
      - path: MIRACL/queries.parquet
        split: train
  - config_name: MIRACL_corpus
    data_files:
      - path: MIRACL/corpus.parquet
        split: train
  - config_name: MSMARCO
    data_files:
      - path: MSMARCO/queries.parquet
        split: train
  - config_name: MSMARCO_corpus
    data_files:
      - path: MSMARCO/corpus.parquet
        split: train
  - config_name: NFCorpus
    data_files:
      - path: NFCorpus/queries.parquet
        split: train
  - config_name: NFCorpus_corpus
    data_files:
      - path: NFCorpus/corpus.parquet
        split: train
  - config_name: NaturalQuestions
    data_files:
      - path: NaturalQuestions/queries.parquet
        split: train
  - config_name: NaturalQuestions_corpus
    data_files:
      - path: NaturalQuestions/corpus.parquet
        split: train
  - config_name: PAQ
    data_files:
      - path: PAQ/queries.parquet
        split: train
  - config_name: PAQ_corpus
    data_files:
      - path: PAQ/corpus.parquet
        split: train
  - config_name: SQuAD
    data_files:
      - path: SQuAD/queries.parquet
        split: train
  - config_name: SQuAD_corpus
    data_files:
      - path: SQuAD/corpus.parquet
        split: train
  - config_name: SyntheticClassificationData
    data_files:
      - path: SyntheticClassificationData/queries.parquet
        split: train
  - config_name: SyntheticClassificationData_corpus
    data_files:
      - path: SyntheticClassificationData/corpus.parquet
        split: train
  - config_name: TriviaQA
    data_files:
      - path: TriviaQA/queries.parquet
        split: train
  - config_name: TriviaQA_corpus
    data_files:
      - path: TriviaQA/corpus.parquet
        split: train
  - config_name: amharic_aya_dataset
    data_files:
      - path: amharic_aya_dataset/queries.parquet
        split: train
  - config_name: amharic_aya_dataset_corpus
    data_files:
      - path: amharic_aya_dataset/corpus.parquet
        split: train
  - config_name: arabic_mr-tydi
    data_files:
      - path: arabic_mr-tydi/queries.parquet
        split: train
  - config_name: arabic_mr-tydi_corpus
    data_files:
      - path: arabic_mr-tydi/corpus.parquet
        split: train
  - config_name: basque_aya_dataset
    data_files:
      - path: basque_aya_dataset/queries.parquet
        split: train
  - config_name: basque_aya_dataset_corpus
    data_files:
      - path: basque_aya_dataset/corpus.parquet
        split: train
  - config_name: bengali_aya_dataset
    data_files:
      - path: bengali_aya_dataset/queries.parquet
        split: train
  - config_name: bengali_aya_dataset_corpus
    data_files:
      - path: bengali_aya_dataset/corpus.parquet
        split: train
  - config_name: bengali_mr-tydi
    data_files:
      - path: bengali_mr-tydi/queries.parquet
        split: train
  - config_name: bengali_mr-tydi_corpus
    data_files:
      - path: bengali_mr-tydi/corpus.parquet
        split: train
  - config_name: burmese_aya_dataset
    data_files:
      - path: burmese_aya_dataset/queries.parquet
        split: train
  - config_name: burmese_aya_dataset_corpus
    data_files:
      - path: burmese_aya_dataset/corpus.parquet
        split: train
  - config_name: cebuano_aya_dataset
    data_files:
      - path: cebuano_aya_dataset/queries.parquet
        split: train
  - config_name: cebuano_aya_dataset_corpus
    data_files:
      - path: cebuano_aya_dataset/corpus.parquet
        split: train
  - config_name: chinese_AFQMC
    data_files:
      - path: chinese_AFQMC/queries.parquet
        split: train
  - config_name: chinese_AFQMC_corpus
    data_files:
      - path: chinese_AFQMC/corpus.parquet
        split: train
  - config_name: chinese_AdvertiseGen
    data_files:
      - path: chinese_AdvertiseGen/queries.parquet
        split: train
  - config_name: chinese_AdvertiseGen_corpus
    data_files:
      - path: chinese_AdvertiseGen/corpus.parquet
        split: train
  - config_name: chinese_CAIL2019-SCM
    data_files:
      - path: chinese_CAIL2019-SCM/queries.parquet
        split: train
  - config_name: chinese_CAIL2019-SCM_corpus
    data_files:
      - path: chinese_CAIL2019-SCM/corpus.parquet
        split: train
  - config_name: chinese_CHEF
    data_files:
      - path: chinese_CHEF/queries.parquet
        split: train
  - config_name: chinese_CHEF_corpus
    data_files:
      - path: chinese_CHEF/corpus.parquet
        split: train
  - config_name: chinese_CINLID
    data_files:
      - path: chinese_CINLID/queries.parquet
        split: train
  - config_name: chinese_CINLID_corpus
    data_files:
      - path: chinese_CINLID/corpus.parquet
        split: train
  - config_name: chinese_ChatMed_Consult_Dataset
    data_files:
      - path: chinese_ChatMed_Consult_Dataset/queries.parquet
        split: train
  - config_name: chinese_ChatMed_Consult_Dataset_corpus
    data_files:
      - path: chinese_ChatMed_Consult_Dataset/corpus.parquet
        split: train
  - config_name: chinese_ChineseSTS
    data_files:
      - path: chinese_ChineseSTS/queries.parquet
        split: train
  - config_name: chinese_ChineseSTS_corpus
    data_files:
      - path: chinese_ChineseSTS/corpus.parquet
        split: train
  - config_name: chinese_DRCD
    data_files:
      - path: chinese_DRCD/queries.parquet
        split: train
  - config_name: chinese_DRCD_corpus
    data_files:
      - path: chinese_DRCD/corpus.parquet
        split: train
  - config_name: chinese_LCSTS
    data_files:
      - path: chinese_LCSTS/queries.parquet
        split: train
  - config_name: chinese_LCSTS_corpus
    data_files:
      - path: chinese_LCSTS/corpus.parquet
        split: train
  - config_name: chinese_Multi-CPR
    data_files:
      - path: chinese_Multi-CPR/queries.parquet
        split: train
  - config_name: chinese_Multi-CPR_corpus
    data_files:
      - path: chinese_Multi-CPR/corpus.parquet
        split: train
  - config_name: chinese_QBQTC
    data_files:
      - path: chinese_QBQTC/queries.parquet
        split: train
  - config_name: chinese_QBQTC_corpus
    data_files:
      - path: chinese_QBQTC/corpus.parquet
        split: train
  - config_name: chinese_RefGPT
    data_files:
      - path: chinese_RefGPT/queries.parquet
        split: train
  - config_name: chinese_RefGPT_corpus
    data_files:
      - path: chinese_RefGPT/corpus.parquet
        split: train
  - config_name: chinese_SimCLUE
    data_files:
      - path: chinese_SimCLUE/queries.parquet
        split: train
  - config_name: chinese_SimCLUE_corpus
    data_files:
      - path: chinese_SimCLUE/corpus.parquet
        split: train
  - config_name: chinese_T2Ranking
    data_files:
      - path: chinese_T2Ranking/queries.parquet
        split: train
  - config_name: chinese_T2Ranking_corpus
    data_files:
      - path: chinese_T2Ranking/corpus.parquet
        split: train
  - config_name: chinese_THUCNews
    data_files:
      - path: chinese_THUCNews/queries.parquet
        split: train
  - config_name: chinese_THUCNews_corpus
    data_files:
      - path: chinese_THUCNews/corpus.parquet
        split: train
  - config_name: chinese_UMETRIP-QA
    data_files:
      - path: chinese_UMETRIP-QA/queries.parquet
        split: train
  - config_name: chinese_UMETRIP-QA_corpus
    data_files:
      - path: chinese_UMETRIP-QA/corpus.parquet
        split: train
  - config_name: chinese_WebCPM
    data_files:
      - path: chinese_WebCPM/queries.parquet
        split: train
  - config_name: chinese_WebCPM_corpus
    data_files:
      - path: chinese_WebCPM/corpus.parquet
        split: train
  - config_name: chinese_atec
    data_files:
      - path: chinese_atec/queries.parquet
        split: train
  - config_name: chinese_atec_corpus
    data_files:
      - path: chinese_atec/corpus.parquet
        split: train
  - config_name: chinese_bq
    data_files:
      - path: chinese_bq/queries.parquet
        split: train
  - config_name: chinese_bq_corpus
    data_files:
      - path: chinese_bq/corpus.parquet
        split: train
  - config_name: chinese_cCOVID-News
    data_files:
      - path: chinese_cCOVID-News/queries.parquet
        split: train
  - config_name: chinese_cCOVID-News_corpus
    data_files:
      - path: chinese_cCOVID-News/corpus.parquet
        split: train
  - config_name: chinese_cMedQA-V2.0
    data_files:
      - path: chinese_cMedQA-V2.0/queries.parquet
        split: train
  - config_name: chinese_cMedQA-V2.0_corpus
    data_files:
      - path: chinese_cMedQA-V2.0/corpus.parquet
        split: train
  - config_name: chinese_cmnli
    data_files:
      - path: chinese_cmnli/queries.parquet
        split: train
  - config_name: chinese_cmnli_corpus
    data_files:
      - path: chinese_cmnli/corpus.parquet
        split: train
  - config_name: chinese_cmrc2018
    data_files:
      - path: chinese_cmrc2018/queries.parquet
        split: train
  - config_name: chinese_cmrc2018_corpus
    data_files:
      - path: chinese_cmrc2018/corpus.parquet
        split: train
  - config_name: chinese_csl
    data_files:
      - path: chinese_csl/queries.parquet
        split: train
  - config_name: chinese_csl_corpus
    data_files:
      - path: chinese_csl/corpus.parquet
        split: train
  - config_name: chinese_dureader
    data_files:
      - path: chinese_dureader/queries.parquet
        split: train
  - config_name: chinese_dureader_corpus
    data_files:
      - path: chinese_dureader/corpus.parquet
        split: train
  - config_name: chinese_dureader_mrc
    data_files:
      - path: chinese_dureader_mrc/queries.parquet
        split: train
  - config_name: chinese_dureader_mrc_corpus
    data_files:
      - path: chinese_dureader_mrc/corpus.parquet
        split: train
  - config_name: chinese_law-gpt
    data_files:
      - path: chinese_law-gpt/queries.parquet
        split: train
  - config_name: chinese_law-gpt_corpus
    data_files:
      - path: chinese_law-gpt/corpus.parquet
        split: train
  - config_name: chinese_lawzhidao
    data_files:
      - path: chinese_lawzhidao/queries.parquet
        split: train
  - config_name: chinese_lawzhidao_corpus
    data_files:
      - path: chinese_lawzhidao/corpus.parquet
        split: train
  - config_name: chinese_lima-chinese
    data_files:
      - path: chinese_lima-chinese/queries.parquet
        split: train
  - config_name: chinese_lima-chinese_corpus
    data_files:
      - path: chinese_lima-chinese/corpus.parquet
        split: train
  - config_name: chinese_llm_retrieval_long_long
    data_files:
      - path: chinese_llm_retrieval_long_long/queries.parquet
        split: train
  - config_name: chinese_llm_retrieval_long_long_corpus
    data_files:
      - path: chinese_llm_retrieval_long_long/corpus.parquet
        split: train
  - config_name: chinese_llm_retrieval_long_short
    data_files:
      - path: chinese_llm_retrieval_long_short/queries.parquet
        split: train
  - config_name: chinese_llm_retrieval_long_short_corpus
    data_files:
      - path: chinese_llm_retrieval_long_short/corpus.parquet
        split: train
  - config_name: chinese_llm_retrieval_short_long
    data_files:
      - path: chinese_llm_retrieval_short_long/queries.parquet
        split: train
  - config_name: chinese_llm_retrieval_short_long_corpus
    data_files:
      - path: chinese_llm_retrieval_short_long/corpus.parquet
        split: train
  - config_name: chinese_llm_retrieval_short_short
    data_files:
      - path: chinese_llm_retrieval_short_short/queries.parquet
        split: train
  - config_name: chinese_llm_retrieval_short_short_corpus
    data_files:
      - path: chinese_llm_retrieval_short_short/corpus.parquet
        split: train
  - config_name: chinese_llm_sts_bitext_retrieval
    data_files:
      - path: chinese_llm_sts_bitext_retrieval/queries.parquet
        split: train
  - config_name: chinese_llm_sts_bitext_retrieval_corpus
    data_files:
      - path: chinese_llm_sts_bitext_retrieval/corpus.parquet
        split: train
  - config_name: chinese_llm_sts_monolingual
    data_files:
      - path: chinese_llm_sts_monolingual/queries.parquet
        split: train
  - config_name: chinese_llm_sts_monolingual_corpus
    data_files:
      - path: chinese_llm_sts_monolingual/corpus.parquet
        split: train
  - config_name: chinese_mmarco-chinese
    data_files:
      - path: chinese_mmarco-chinese/queries.parquet
        split: train
  - config_name: chinese_mmarco-chinese_corpus
    data_files:
      - path: chinese_mmarco-chinese/corpus.parquet
        split: train
  - config_name: chinese_nli_zh
    data_files:
      - path: chinese_nli_zh/queries.parquet
        split: train
  - config_name: chinese_nli_zh_corpus
    data_files:
      - path: chinese_nli_zh/corpus.parquet
        split: train
  - config_name: chinese_ocnli
    data_files:
      - path: chinese_ocnli/queries.parquet
        split: train
  - config_name: chinese_ocnli_corpus
    data_files:
      - path: chinese_ocnli/corpus.parquet
        split: train
  - config_name: chinese_retrieval_data_llm_infgrad
    data_files:
      - path: chinese_retrieval_data_llm_infgrad/queries.parquet
        split: train
  - config_name: chinese_retrieval_data_llm_infgrad_corpus
    data_files:
      - path: chinese_retrieval_data_llm_infgrad/corpus.parquet
        split: train
  - config_name: chinese_webqa
    data_files:
      - path: chinese_webqa/queries.parquet
        split: train
  - config_name: chinese_webqa_corpus
    data_files:
      - path: chinese_webqa/corpus.parquet
        split: train
  - config_name: chinese_xnli_zh
    data_files:
      - path: chinese_xnli_zh/queries.parquet
        split: train
  - config_name: chinese_xnli_zh_corpus
    data_files:
      - path: chinese_xnli_zh/corpus.parquet
        split: train
  - config_name: danish_aya_dataset
    data_files:
      - path: danish_aya_dataset/queries.parquet
        split: train
  - config_name: danish_aya_dataset_corpus
    data_files:
      - path: danish_aya_dataset/corpus.parquet
        split: train
  - config_name: dutch_aya_dataset
    data_files:
      - path: dutch_aya_dataset/queries.parquet
        split: train
  - config_name: dutch_aya_dataset_corpus
    data_files:
      - path: dutch_aya_dataset/corpus.parquet
        split: train
  - config_name: egyptian arabic_aya_dataset
    data_files:
      - path: egyptian arabic_aya_dataset/queries.parquet
        split: train
  - config_name: egyptian arabic_aya_dataset_corpus
    data_files:
      - path: egyptian arabic_aya_dataset/corpus.parquet
        split: train
  - config_name: english_CodeFeedback
    data_files:
      - path: english_CodeFeedback/queries.parquet
        split: train
  - config_name: english_CodeFeedback_corpus
    data_files:
      - path: english_CodeFeedback/corpus.parquet
        split: train
  - config_name: english_ELI5_custom
    data_files:
      - path: english_ELI5_custom/queries.parquet
        split: train
  - config_name: english_ELI5_custom_corpus
    data_files:
      - path: english_ELI5_custom/corpus.parquet
        split: train
  - config_name: english_Expertqa
    data_files:
      - path: english_Expertqa/queries.parquet
        split: train
  - config_name: english_Expertqa_corpus
    data_files:
      - path: english_Expertqa/corpus.parquet
        split: train
  - config_name: english_MEDI2BGE
    data_files:
      - path: english_MEDI2BGE/queries.parquet
        split: train
  - config_name: english_MEDI2BGE_corpus
    data_files:
      - path: english_MEDI2BGE/corpus.parquet
        split: train
  - config_name: english_OpenOrca
    data_files:
      - path: english_OpenOrca/queries.parquet
        split: train
  - config_name: english_OpenOrca_corpus
    data_files:
      - path: english_OpenOrca/corpus.parquet
        split: train
  - config_name: english_PubMedQA
    data_files:
      - path: english_PubMedQA/queries.parquet
        split: train
  - config_name: english_PubMedQA_corpus
    data_files:
      - path: english_PubMedQA/corpus.parquet
        split: train
  - config_name: english_SearchQA
    data_files:
      - path: english_SearchQA/queries.parquet
        split: train
  - config_name: english_SearchQA_corpus
    data_files:
      - path: english_SearchQA/corpus.parquet
        split: train
  - config_name: english_WikiAnswers
    data_files:
      - path: english_WikiAnswers/queries.parquet
        split: train
  - config_name: english_WikiAnswers_corpus
    data_files:
      - path: english_WikiAnswers/corpus.parquet
        split: train
  - config_name: english_aya_dataset
    data_files:
      - path: english_aya_dataset/queries.parquet
        split: train
  - config_name: english_aya_dataset_corpus
    data_files:
      - path: english_aya_dataset/corpus.parquet
        split: train
  - config_name: english_ccnews
    data_files:
      - path: english_ccnews/queries.parquet
        split: train
  - config_name: english_ccnews_corpus
    data_files:
      - path: english_ccnews/corpus.parquet
        split: train
  - config_name: english_contract-nli
    data_files:
      - path: english_contract-nli/queries.parquet
        split: train
  - config_name: english_contract-nli_corpus
    data_files:
      - path: english_contract-nli/corpus.parquet
        split: train
  - config_name: english_esci
    data_files:
      - path: english_esci/queries.parquet
        split: train
  - config_name: english_esci_corpus
    data_files:
      - path: english_esci/corpus.parquet
        split: train
  - config_name: english_mldr
    data_files:
      - path: english_mldr/queries.parquet
        split: train
  - config_name: english_mldr_corpus
    data_files:
      - path: english_mldr/corpus.parquet
        split: train
  - config_name: english_mnli
    data_files:
      - path: english_mnli/queries.parquet
        split: train
  - config_name: english_mnli_corpus
    data_files:
      - path: english_mnli/corpus.parquet
        split: train
  - config_name: english_mr-tydi
    data_files:
      - path: english_mr-tydi/queries.parquet
        split: train
  - config_name: english_mr-tydi_corpus
    data_files:
      - path: english_mr-tydi/corpus.parquet
        split: train
  - config_name: english_nllb
    data_files:
      - path: english_nllb/queries.parquet
        split: train
  - config_name: english_nllb_corpus
    data_files:
      - path: english_nllb/corpus.parquet
        split: train
  - config_name: english_rag-dataset-12000
    data_files:
      - path: english_rag-dataset-12000/queries.parquet
        split: train
  - config_name: english_rag-dataset-12000_corpus
    data_files:
      - path: english_rag-dataset-12000/corpus.parquet
        split: train
  - config_name: english_simcse_sup_nli
    data_files:
      - path: english_simcse_sup_nli/queries.parquet
        split: train
  - config_name: english_simcse_sup_nli_corpus
    data_files:
      - path: english_simcse_sup_nli/corpus.parquet
        split: train
  - config_name: english_webgpt_comparisons
    data_files:
      - path: english_webgpt_comparisons/queries.parquet
        split: train
  - config_name: english_webgpt_comparisons_corpus
    data_files:
      - path: english_webgpt_comparisons/corpus.parquet
        split: train
  - config_name: english_wikipedia-nq
    data_files:
      - path: english_wikipedia-nq/queries.parquet
        split: train
  - config_name: english_wikipedia-nq_corpus
    data_files:
      - path: english_wikipedia-nq/corpus.parquet
        split: train
  - config_name: english_yahoo-answers
    data_files:
      - path: english_yahoo-answers/queries.parquet
        split: train
  - config_name: english_yahoo-answers_corpus
    data_files:
      - path: english_yahoo-answers/corpus.parquet
        split: train
  - config_name: filipino_aya_dataset
    data_files:
      - path: filipino_aya_dataset/queries.parquet
        split: train
  - config_name: filipino_aya_dataset_corpus
    data_files:
      - path: filipino_aya_dataset/corpus.parquet
        split: train
  - config_name: finnish_aya_dataset
    data_files:
      - path: finnish_aya_dataset/queries.parquet
        split: train
  - config_name: finnish_aya_dataset_corpus
    data_files:
      - path: finnish_aya_dataset/corpus.parquet
        split: train
  - config_name: finnish_mr-tydi
    data_files:
      - path: finnish_mr-tydi/queries.parquet
        split: train
  - config_name: finnish_mr-tydi_corpus
    data_files:
      - path: finnish_mr-tydi/corpus.parquet
        split: train
  - config_name: followir_train
    data_files:
      - path: followir_train/queries.parquet
        split: train
  - config_name: followir_train_corpus
    data_files:
      - path: followir_train/corpus.parquet
        split: train
  - config_name: french_aya_dataset
    data_files:
      - path: french_aya_dataset/queries.parquet
        split: train
  - config_name: french_aya_dataset_corpus
    data_files:
      - path: french_aya_dataset/corpus.parquet
        split: train
  - config_name: german_aya_dataset
    data_files:
      - path: german_aya_dataset/queries.parquet
        split: train
  - config_name: german_aya_dataset_corpus
    data_files:
      - path: german_aya_dataset/corpus.parquet
        split: train
  - config_name: greek_aya_dataset
    data_files:
      - path: greek_aya_dataset/queries.parquet
        split: train
  - config_name: greek_aya_dataset_corpus
    data_files:
      - path: greek_aya_dataset/corpus.parquet
        split: train
  - config_name: gujarati_aya_dataset
    data_files:
      - path: gujarati_aya_dataset/queries.parquet
        split: train
  - config_name: gujarati_aya_dataset_corpus
    data_files:
      - path: gujarati_aya_dataset/corpus.parquet
        split: train
  - config_name: haitian_aya_dataset
    data_files:
      - path: haitian_aya_dataset/queries.parquet
        split: train
  - config_name: haitian_aya_dataset_corpus
    data_files:
      - path: haitian_aya_dataset/corpus.parquet
        split: train
  - config_name: hausa_aya_dataset
    data_files:
      - path: hausa_aya_dataset/queries.parquet
        split: train
  - config_name: hausa_aya_dataset_corpus
    data_files:
      - path: hausa_aya_dataset/corpus.parquet
        split: train
  - config_name: hindi_aya_dataset
    data_files:
      - path: hindi_aya_dataset/queries.parquet
        split: train
  - config_name: hindi_aya_dataset_corpus
    data_files:
      - path: hindi_aya_dataset/corpus.parquet
        split: train
  - config_name: hungarian_aya_dataset
    data_files:
      - path: hungarian_aya_dataset/queries.parquet
        split: train
  - config_name: hungarian_aya_dataset_corpus
    data_files:
      - path: hungarian_aya_dataset/corpus.parquet
        split: train
  - config_name: igbo_aya_dataset
    data_files:
      - path: igbo_aya_dataset/queries.parquet
        split: train
  - config_name: igbo_aya_dataset_corpus
    data_files:
      - path: igbo_aya_dataset/corpus.parquet
        split: train
  - config_name: indonesian_aya_dataset
    data_files:
      - path: indonesian_aya_dataset/queries.parquet
        split: train
  - config_name: indonesian_aya_dataset_corpus
    data_files:
      - path: indonesian_aya_dataset/corpus.parquet
        split: train
  - config_name: indonesian_mr-tydi
    data_files:
      - path: indonesian_mr-tydi/queries.parquet
        split: train
  - config_name: indonesian_mr-tydi_corpus
    data_files:
      - path: indonesian_mr-tydi/corpus.parquet
        split: train
  - config_name: infir_leetcode
    data_files:
      - path: infir_leetcode/queries.parquet
        split: train
  - config_name: infir_leetcode_corpus
    data_files:
      - path: infir_leetcode/corpus.parquet
        split: train
  - config_name: infir_metamath
    data_files:
      - path: infir_metamath/queries.parquet
        split: train
  - config_name: infir_metamath_corpus
    data_files:
      - path: infir_metamath/corpus.parquet
        split: train
  - config_name: infir_msmarco
    data_files:
      - path: infir_msmarco/queries.parquet
        split: train
  - config_name: infir_msmarco_corpus
    data_files:
      - path: infir_msmarco/corpus.parquet
        split: train
  - config_name: iranian persian_aya_dataset
    data_files:
      - path: iranian persian_aya_dataset/queries.parquet
        split: train
  - config_name: iranian persian_aya_dataset_corpus
    data_files:
      - path: iranian persian_aya_dataset/corpus.parquet
        split: train
  - config_name: irish_aya_dataset
    data_files:
      - path: irish_aya_dataset/queries.parquet
        split: train
  - config_name: irish_aya_dataset_corpus
    data_files:
      - path: irish_aya_dataset/corpus.parquet
        split: train
  - config_name: italian_aya_dataset
    data_files:
      - path: italian_aya_dataset/queries.parquet
        split: train
  - config_name: italian_aya_dataset_corpus
    data_files:
      - path: italian_aya_dataset/corpus.parquet
        split: train
  - config_name: japanese_mr-tydi
    data_files:
      - path: japanese_mr-tydi/queries.parquet
        split: train
  - config_name: japanese_mr-tydi_corpus
    data_files:
      - path: japanese_mr-tydi/corpus.parquet
        split: train
  - config_name: javanese_aya_dataset
    data_files:
      - path: javanese_aya_dataset/queries.parquet
        split: train
  - config_name: javanese_aya_dataset_corpus
    data_files:
      - path: javanese_aya_dataset/corpus.parquet
        split: train
  - config_name: kannada_aya_dataset
    data_files:
      - path: kannada_aya_dataset/queries.parquet
        split: train
  - config_name: kannada_aya_dataset_corpus
    data_files:
      - path: kannada_aya_dataset/corpus.parquet
        split: train
  - config_name: korean_aya_dataset
    data_files:
      - path: korean_aya_dataset/queries.parquet
        split: train
  - config_name: korean_aya_dataset_corpus
    data_files:
      - path: korean_aya_dataset/corpus.parquet
        split: train
  - config_name: korean_mr-tydi
    data_files:
      - path: korean_mr-tydi/queries.parquet
        split: train
  - config_name: korean_mr-tydi_corpus
    data_files:
      - path: korean_mr-tydi/corpus.parquet
        split: train
  - config_name: kyrgyz_aya_dataset
    data_files:
      - path: kyrgyz_aya_dataset/queries.parquet
        split: train
  - config_name: kyrgyz_aya_dataset_corpus
    data_files:
      - path: kyrgyz_aya_dataset/corpus.parquet
        split: train
  - config_name: lithuanian_aya_dataset
    data_files:
      - path: lithuanian_aya_dataset/queries.parquet
        split: train
  - config_name: lithuanian_aya_dataset_corpus
    data_files:
      - path: lithuanian_aya_dataset/corpus.parquet
        split: train
  - config_name: malayalam_aya_dataset
    data_files:
      - path: malayalam_aya_dataset/queries.parquet
        split: train
  - config_name: malayalam_aya_dataset_corpus
    data_files:
      - path: malayalam_aya_dataset/corpus.parquet
        split: train
  - config_name: marathi_aya_dataset
    data_files:
      - path: marathi_aya_dataset/queries.parquet
        split: train
  - config_name: marathi_aya_dataset_corpus
    data_files:
      - path: marathi_aya_dataset/corpus.parquet
        split: train
  - config_name: moroccan arabic_aya_dataset
    data_files:
      - path: moroccan arabic_aya_dataset/queries.parquet
        split: train
  - config_name: moroccan arabic_aya_dataset_corpus
    data_files:
      - path: moroccan arabic_aya_dataset/corpus.parquet
        split: train
  - config_name: najdi arabic_aya_dataset
    data_files:
      - path: najdi arabic_aya_dataset/queries.parquet
        split: train
  - config_name: najdi arabic_aya_dataset_corpus
    data_files:
      - path: najdi arabic_aya_dataset/corpus.parquet
        split: train
  - config_name: nepali_aya_dataset
    data_files:
      - path: nepali_aya_dataset/queries.parquet
        split: train
  - config_name: nepali_aya_dataset_corpus
    data_files:
      - path: nepali_aya_dataset/corpus.parquet
        split: train
  - config_name: northern sotho_aya_dataset
    data_files:
      - path: northern sotho_aya_dataset/queries.parquet
        split: train
  - config_name: northern sotho_aya_dataset_corpus
    data_files:
      - path: northern sotho_aya_dataset/corpus.parquet
        split: train
  - config_name: nyanja_aya_dataset
    data_files:
      - path: nyanja_aya_dataset/queries.parquet
        split: train
  - config_name: nyanja_aya_dataset_corpus
    data_files:
      - path: nyanja_aya_dataset/corpus.parquet
        split: train
  - config_name: panjabi_aya_dataset
    data_files:
      - path: panjabi_aya_dataset/queries.parquet
        split: train
  - config_name: panjabi_aya_dataset_corpus
    data_files:
      - path: panjabi_aya_dataset/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_af
    data_files:
      - path: parallel_broad_v3_en_af/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_af_corpus
    data_files:
      - path: parallel_broad_v3_en_af/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_ar
    data_files:
      - path: parallel_broad_v3_en_ar/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_ar_corpus
    data_files:
      - path: parallel_broad_v3_en_ar/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_az
    data_files:
      - path: parallel_broad_v3_en_az/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_az_corpus
    data_files:
      - path: parallel_broad_v3_en_az/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_be
    data_files:
      - path: parallel_broad_v3_en_be/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_be_corpus
    data_files:
      - path: parallel_broad_v3_en_be/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_bg
    data_files:
      - path: parallel_broad_v3_en_bg/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_bg_corpus
    data_files:
      - path: parallel_broad_v3_en_bg/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_bs
    data_files:
      - path: parallel_broad_v3_en_bs/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_bs_corpus
    data_files:
      - path: parallel_broad_v3_en_bs/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_ca
    data_files:
      - path: parallel_broad_v3_en_ca/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_ca_corpus
    data_files:
      - path: parallel_broad_v3_en_ca/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_cs
    data_files:
      - path: parallel_broad_v3_en_cs/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_cs_corpus
    data_files:
      - path: parallel_broad_v3_en_cs/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_cy
    data_files:
      - path: parallel_broad_v3_en_cy/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_cy_corpus
    data_files:
      - path: parallel_broad_v3_en_cy/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_da
    data_files:
      - path: parallel_broad_v3_en_da/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_da_corpus
    data_files:
      - path: parallel_broad_v3_en_da/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_de
    data_files:
      - path: parallel_broad_v3_en_de/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_de_corpus
    data_files:
      - path: parallel_broad_v3_en_de/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_el
    data_files:
      - path: parallel_broad_v3_en_el/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_el_corpus
    data_files:
      - path: parallel_broad_v3_en_el/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_es
    data_files:
      - path: parallel_broad_v3_en_es/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_es_corpus
    data_files:
      - path: parallel_broad_v3_en_es/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_et
    data_files:
      - path: parallel_broad_v3_en_et/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_et_corpus
    data_files:
      - path: parallel_broad_v3_en_et/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_eu
    data_files:
      - path: parallel_broad_v3_en_eu/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_eu_corpus
    data_files:
      - path: parallel_broad_v3_en_eu/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_fa
    data_files:
      - path: parallel_broad_v3_en_fa/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_fa_corpus
    data_files:
      - path: parallel_broad_v3_en_fa/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_fi
    data_files:
      - path: parallel_broad_v3_en_fi/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_fi_corpus
    data_files:
      - path: parallel_broad_v3_en_fi/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_ga
    data_files:
      - path: parallel_broad_v3_en_ga/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_ga_corpus
    data_files:
      - path: parallel_broad_v3_en_ga/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_gl
    data_files:
      - path: parallel_broad_v3_en_gl/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_gl_corpus
    data_files:
      - path: parallel_broad_v3_en_gl/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_he
    data_files:
      - path: parallel_broad_v3_en_he/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_he_corpus
    data_files:
      - path: parallel_broad_v3_en_he/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_hr
    data_files:
      - path: parallel_broad_v3_en_hr/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_hr_corpus
    data_files:
      - path: parallel_broad_v3_en_hr/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_hu
    data_files:
      - path: parallel_broad_v3_en_hu/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_hu_corpus
    data_files:
      - path: parallel_broad_v3_en_hu/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_hy
    data_files:
      - path: parallel_broad_v3_en_hy/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_hy_corpus
    data_files:
      - path: parallel_broad_v3_en_hy/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_id
    data_files:
      - path: parallel_broad_v3_en_id/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_id_corpus
    data_files:
      - path: parallel_broad_v3_en_id/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_is
    data_files:
      - path: parallel_broad_v3_en_is/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_is_corpus
    data_files:
      - path: parallel_broad_v3_en_is/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_it
    data_files:
      - path: parallel_broad_v3_en_it/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_it_corpus
    data_files:
      - path: parallel_broad_v3_en_it/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_ja
    data_files:
      - path: parallel_broad_v3_en_ja/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_ja_corpus
    data_files:
      - path: parallel_broad_v3_en_ja/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_ka
    data_files:
      - path: parallel_broad_v3_en_ka/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_ka_corpus
    data_files:
      - path: parallel_broad_v3_en_ka/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_kk
    data_files:
      - path: parallel_broad_v3_en_kk/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_kk_corpus
    data_files:
      - path: parallel_broad_v3_en_kk/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_ko
    data_files:
      - path: parallel_broad_v3_en_ko/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_ko_corpus
    data_files:
      - path: parallel_broad_v3_en_ko/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_lt
    data_files:
      - path: parallel_broad_v3_en_lt/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_lt_corpus
    data_files:
      - path: parallel_broad_v3_en_lt/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_lv
    data_files:
      - path: parallel_broad_v3_en_lv/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_lv_corpus
    data_files:
      - path: parallel_broad_v3_en_lv/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_mk
    data_files:
      - path: parallel_broad_v3_en_mk/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_mk_corpus
    data_files:
      - path: parallel_broad_v3_en_mk/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_ms
    data_files:
      - path: parallel_broad_v3_en_ms/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_ms_corpus
    data_files:
      - path: parallel_broad_v3_en_ms/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_mt
    data_files:
      - path: parallel_broad_v3_en_mt/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_mt_corpus
    data_files:
      - path: parallel_broad_v3_en_mt/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_nb
    data_files:
      - path: parallel_broad_v3_en_nb/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_nb_corpus
    data_files:
      - path: parallel_broad_v3_en_nb/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_nl
    data_files:
      - path: parallel_broad_v3_en_nl/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_nl_corpus
    data_files:
      - path: parallel_broad_v3_en_nl/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_pl
    data_files:
      - path: parallel_broad_v3_en_pl/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_pl_corpus
    data_files:
      - path: parallel_broad_v3_en_pl/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_pt
    data_files:
      - path: parallel_broad_v3_en_pt/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_pt_corpus
    data_files:
      - path: parallel_broad_v3_en_pt/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_ro
    data_files:
      - path: parallel_broad_v3_en_ro/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_ro_corpus
    data_files:
      - path: parallel_broad_v3_en_ro/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_ru
    data_files:
      - path: parallel_broad_v3_en_ru/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_ru_corpus
    data_files:
      - path: parallel_broad_v3_en_ru/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_sk
    data_files:
      - path: parallel_broad_v3_en_sk/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_sk_corpus
    data_files:
      - path: parallel_broad_v3_en_sk/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_sl
    data_files:
      - path: parallel_broad_v3_en_sl/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_sl_corpus
    data_files:
      - path: parallel_broad_v3_en_sl/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_sq
    data_files:
      - path: parallel_broad_v3_en_sq/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_sq_corpus
    data_files:
      - path: parallel_broad_v3_en_sq/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_sr
    data_files:
      - path: parallel_broad_v3_en_sr/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_sr_corpus
    data_files:
      - path: parallel_broad_v3_en_sr/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_sv
    data_files:
      - path: parallel_broad_v3_en_sv/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_sv_corpus
    data_files:
      - path: parallel_broad_v3_en_sv/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_th
    data_files:
      - path: parallel_broad_v3_en_th/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_th_corpus
    data_files:
      - path: parallel_broad_v3_en_th/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_tr
    data_files:
      - path: parallel_broad_v3_en_tr/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_tr_corpus
    data_files:
      - path: parallel_broad_v3_en_tr/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_uk
    data_files:
      - path: parallel_broad_v3_en_uk/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_uk_corpus
    data_files:
      - path: parallel_broad_v3_en_uk/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_vi
    data_files:
      - path: parallel_broad_v3_en_vi/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_vi_corpus
    data_files:
      - path: parallel_broad_v3_en_vi/corpus.parquet
        split: train
  - config_name: parallel_broad_v3_en_zh
    data_files:
      - path: parallel_broad_v3_en_zh/queries.parquet
        split: train
  - config_name: parallel_broad_v3_en_zh_corpus
    data_files:
      - path: parallel_broad_v3_en_zh/corpus.parquet
        split: train
  - config_name: plateau malagasy_aya_dataset
    data_files:
      - path: plateau malagasy_aya_dataset/queries.parquet
        split: train
  - config_name: plateau malagasy_aya_dataset_corpus
    data_files:
      - path: plateau malagasy_aya_dataset/corpus.parquet
        split: train
  - config_name: polish_aya_dataset
    data_files:
      - path: polish_aya_dataset/queries.parquet
        split: train
  - config_name: polish_aya_dataset_corpus
    data_files:
      - path: polish_aya_dataset/corpus.parquet
        split: train
  - config_name: portuguese_aya_dataset
    data_files:
      - path: portuguese_aya_dataset/queries.parquet
        split: train
  - config_name: portuguese_aya_dataset_corpus
    data_files:
      - path: portuguese_aya_dataset/corpus.parquet
        split: train
  - config_name: russian_aya_dataset
    data_files:
      - path: russian_aya_dataset/queries.parquet
        split: train
  - config_name: russian_aya_dataset_corpus
    data_files:
      - path: russian_aya_dataset/corpus.parquet
        split: train
  - config_name: russian_mr-tydi
    data_files:
      - path: russian_mr-tydi/queries.parquet
        split: train
  - config_name: russian_mr-tydi_corpus
    data_files:
      - path: russian_mr-tydi/corpus.parquet
        split: train
  - config_name: serbian_aya_dataset
    data_files:
      - path: serbian_aya_dataset/queries.parquet
        split: train
  - config_name: serbian_aya_dataset_corpus
    data_files:
      - path: serbian_aya_dataset/corpus.parquet
        split: train
  - config_name: shona_aya_dataset
    data_files:
      - path: shona_aya_dataset/queries.parquet
        split: train
  - config_name: shona_aya_dataset_corpus
    data_files:
      - path: shona_aya_dataset/corpus.parquet
        split: train
  - config_name: sindhi_aya_dataset
    data_files:
      - path: sindhi_aya_dataset/queries.parquet
        split: train
  - config_name: sindhi_aya_dataset_corpus
    data_files:
      - path: sindhi_aya_dataset/corpus.parquet
        split: train
  - config_name: sinhala_aya_dataset
    data_files:
      - path: sinhala_aya_dataset/queries.parquet
        split: train
  - config_name: sinhala_aya_dataset_corpus
    data_files:
      - path: sinhala_aya_dataset/corpus.parquet
        split: train
  - config_name: somali_aya_dataset
    data_files:
      - path: somali_aya_dataset/queries.parquet
        split: train
  - config_name: somali_aya_dataset_corpus
    data_files:
      - path: somali_aya_dataset/corpus.parquet
        split: train
  - config_name: southern pashto_aya_dataset
    data_files:
      - path: southern pashto_aya_dataset/queries.parquet
        split: train
  - config_name: southern pashto_aya_dataset_corpus
    data_files:
      - path: southern pashto_aya_dataset/corpus.parquet
        split: train
  - config_name: spanish_aya_dataset
    data_files:
      - path: spanish_aya_dataset/queries.parquet
        split: train
  - config_name: spanish_aya_dataset_corpus
    data_files:
      - path: spanish_aya_dataset/corpus.parquet
        split: train
  - config_name: standard arabic_aya_dataset
    data_files:
      - path: standard arabic_aya_dataset/queries.parquet
        split: train
  - config_name: standard arabic_aya_dataset_corpus
    data_files:
      - path: standard arabic_aya_dataset/corpus.parquet
        split: train
  - config_name: standard malay_aya_dataset
    data_files:
      - path: standard malay_aya_dataset/queries.parquet
        split: train
  - config_name: standard malay_aya_dataset_corpus
    data_files:
      - path: standard malay_aya_dataset/corpus.parquet
        split: train
  - config_name: sundanese_aya_dataset
    data_files:
      - path: sundanese_aya_dataset/queries.parquet
        split: train
  - config_name: sundanese_aya_dataset_corpus
    data_files:
      - path: sundanese_aya_dataset/corpus.parquet
        split: train
  - config_name: swahili_aya_dataset
    data_files:
      - path: swahili_aya_dataset/queries.parquet
        split: train
  - config_name: swahili_aya_dataset_corpus
    data_files:
      - path: swahili_aya_dataset/corpus.parquet
        split: train
  - config_name: swahili_mr-tydi
    data_files:
      - path: swahili_mr-tydi/queries.parquet
        split: train
  - config_name: swahili_mr-tydi_corpus
    data_files:
      - path: swahili_mr-tydi/corpus.parquet
        split: train
  - config_name: swedish_aya_dataset
    data_files:
      - path: swedish_aya_dataset/queries.parquet
        split: train
  - config_name: swedish_aya_dataset_corpus
    data_files:
      - path: swedish_aya_dataset/corpus.parquet
        split: train
  - config_name: ta'izzi-adeni arabic_aya_dataset
    data_files:
      - path: ta'izzi-adeni arabic_aya_dataset/queries.parquet
        split: train
  - config_name: ta'izzi-adeni arabic_aya_dataset_corpus
    data_files:
      - path: ta'izzi-adeni arabic_aya_dataset/corpus.parquet
        split: train
  - config_name: tamil_aya_dataset
    data_files:
      - path: tamil_aya_dataset/queries.parquet
        split: train
  - config_name: tamil_aya_dataset_corpus
    data_files:
      - path: tamil_aya_dataset/corpus.parquet
        split: train
  - config_name: telugu_aya_dataset
    data_files:
      - path: telugu_aya_dataset/queries.parquet
        split: train
  - config_name: telugu_aya_dataset_corpus
    data_files:
      - path: telugu_aya_dataset/corpus.parquet
        split: train
  - config_name: telugu_mr-tydi
    data_files:
      - path: telugu_mr-tydi/queries.parquet
        split: train
  - config_name: telugu_mr-tydi_corpus
    data_files:
      - path: telugu_mr-tydi/corpus.parquet
        split: train
  - config_name: thai_aya_dataset
    data_files:
      - path: thai_aya_dataset/queries.parquet
        split: train
  - config_name: thai_aya_dataset_corpus
    data_files:
      - path: thai_aya_dataset/corpus.parquet
        split: train
  - config_name: thai_mr-tydi
    data_files:
      - path: thai_mr-tydi/queries.parquet
        split: train
  - config_name: thai_mr-tydi_corpus
    data_files:
      - path: thai_mr-tydi/corpus.parquet
        split: train
  - config_name: traditional chinese_aya_dataset
    data_files:
      - path: traditional chinese_aya_dataset/queries.parquet
        split: train
  - config_name: traditional chinese_aya_dataset_corpus
    data_files:
      - path: traditional chinese_aya_dataset/corpus.parquet
        split: train
  - config_name: turkish_aya_dataset
    data_files:
      - path: turkish_aya_dataset/queries.parquet
        split: train
  - config_name: turkish_aya_dataset_corpus
    data_files:
      - path: turkish_aya_dataset/corpus.parquet
        split: train
  - config_name: ukrainian_aya_dataset
    data_files:
      - path: ukrainian_aya_dataset/queries.parquet
        split: train
  - config_name: ukrainian_aya_dataset_corpus
    data_files:
      - path: ukrainian_aya_dataset/corpus.parquet
        split: train
  - config_name: urdu_aya_dataset
    data_files:
      - path: urdu_aya_dataset/queries.parquet
        split: train
  - config_name: urdu_aya_dataset_corpus
    data_files:
      - path: urdu_aya_dataset/corpus.parquet
        split: train
  - config_name: vietnamese_aya_dataset
    data_files:
      - path: vietnamese_aya_dataset/queries.parquet
        split: train
  - config_name: vietnamese_aya_dataset_corpus
    data_files:
      - path: vietnamese_aya_dataset/corpus.parquet
        split: train
  - config_name: wolof_aya_dataset
    data_files:
      - path: wolof_aya_dataset/queries.parquet
        split: train
  - config_name: wolof_aya_dataset_corpus
    data_files:
      - path: wolof_aya_dataset/corpus.parquet
        split: train
  - config_name: xhosa_aya_dataset
    data_files:
      - path: xhosa_aya_dataset/queries.parquet
        split: train
  - config_name: xhosa_aya_dataset_corpus
    data_files:
      - path: xhosa_aya_dataset/corpus.parquet
        split: train
  - config_name: yoruba_aya_dataset
    data_files:
      - path: yoruba_aya_dataset/queries.parquet
        split: train
  - config_name: yoruba_aya_dataset_corpus
    data_files:
      - path: yoruba_aya_dataset/corpus.parquet
        split: train
  - config_name: zulu_aya_dataset
    data_files:
      - path: zulu_aya_dataset/queries.parquet
        split: train
  - config_name: zulu_aya_dataset_corpus
    data_files:
      - path: zulu_aya_dataset/corpus.parquet
        split: train
---

# BidirLM-Contrastive

The contrastive training dataset used to train [BidirLM Embedding](https://huggingface.co/BidirLM) models. It contains **10,110,219 query-document pairs** from **79 base datasets**, split into **203 subdatasets** by language or type (~13 GB), covering three sources: **Nemotron**, **KaLM**, and **parallel/other data**. This dataset is described in the paper: [BidirLM: From Text to Omnimodal Bidirectional Encoders by Adapting and Composing Causal LLMs](https://arxiv.org/abs/2604.02045).

If you use this dataset in your research or applications, please cite the BidirLM paper using the reference below:

```bibtex
@misc{boizard2026bidirlmtextomnimodalbidirectional,
      title={BidirLM: From Text to Omnimodal Bidirectional Encoders by Adapting and Composing Causal LLMs},
      author={Nicolas Boizard and Théo Deschamps-Berger and Hippolyte Gisserot-Boukhlef and Céline Hudelot and Pierre Colombo},
      year={2026},
      eprint={2604.02045},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2604.02045},
}
``` 

## Loading Example

```python
import json
import pandas as pd
from huggingface_hub import snapshot_download

# Download a single subdataset
local_path = snapshot_download(
    "BidirLM/BidirLM-Contrastive",
    repo_type="dataset",
    allow_patterns="NFCorpus/*",
)

# Load queries
queries_df = pd.read_parquet(f"{local_path}/NFCorpus/queries.parquet")

# Load corpus
corpus_df = pd.read_parquet(f"{local_path}/NFCorpus/corpus.parquet")
corpus = dict(zip(corpus_df["id"], corpus_df["text"]))

# Load metadata
with open(f"{local_path}/NFCorpus/dataset_metadata.json") as f:
    metadata = json.load(f)

# Resolve document IDs to text
for _, query in queries_df.head(3).iterrows():
    print(f"Query: {query['question'][:80]}...")
    print(f"  Instruction: {metadata.get('query_instruction', 'N/A')}")
    for pos in query["pos_doc"]:
        print(f"  Positive: {corpus[pos['id']][:80]}...")
    for neg in query["neg_doc"][:2]:
        print(f"  Negative: {corpus[neg['id']][:80]}...")
    print()
```

## Dataset Composition

The dataset combines three families of sources:

### Nemotron (11 datasets, 3,351,691 pairs)

English retrieval and classification data from [Embed-Nemotron](https://huggingface.co/datasets/nvidia/embed-nemotron-dataset-v1).

| Dataset | Pairs |
|---|---:|
| SyntheticClassificationData | 1,044,212 |
| PAQ | 1,000,000 |
| MSMARCO | 532,751 |
| MAmmoTH2 | 317,180 |
| NaturalQuestions | 100,231 |
| GooAQ | 100,000 |
| SQuAD | 87,599 |
| MIRACL | 79,648 |
| TriviaQA | 73,346 |
| EmotionClassification | 13,039 |
| NFCorpus | 3,685 |

### KaLM (62 datasets, 3,655,225 pairs)

Multilingual data from [KaLM-Embedding](https://huggingface.co/datasets/KaLM-Embedding/KaLM-embedding-finetuning-data), covering NLI, retrieval, STS, and classification tasks.

| Dataset | Pairs | Dataset | Pairs |
|---|---:|---|---:|
| mmarco-chinese | 379,870 | SimCLUE | 290,699 |
| Multi-CPR | 234,587 | simcse_sup_nli | 217,099 |
| T2Ranking | 188,606 | nli_zh | 185,787 |
| llm_sts_monolingual | 132,561 | cmnli | 119,029 |
| llm_retrieval_short_long | 149,511 | llm_retrieval_long_long | 114,979 |
| llm_retrieval_long_short | 114,584 | dureader_mrc | 97,764 |
| cMedQA-V2.0 | 88,109 | dureader | 79,229 |
| llm_retrieval_short_short | 76,315 | llm_sts_bitext_retrieval | 75,271 |
| xnli_zh | 74,252 | PubMedQA | 79,954 |
| ELI5_custom | 76,408 | MEDI2BGE | 71,790 |
| mnli | 63,701 | webqa | 4,988 |
| wikipedia-nq | 56,377 | CodeFeedback | 49,090 |
| RefGPT | 49,896 | WikiAnswers | 47,686 |
| QBQTC | 47,223 | OpenOrca | 38,623 |
| retrieval_data_llm_infgrad | 32,551 | mldr | 31,097 |
| ccnews | 28,246 | nllb | 26,504 |
| esci | 26,043 | yahoo-answers | 21,724 |
| csl | 19,945 | LCSTS | 19,535 |
| THUCNews | 19,288 | webgpt_comparisons | 18,924 |
| ChatMed_Consult_Dataset | 18,608 | AdvertiseGen | 17,526 |
| atec | 11,387 | ocnli | 11,937 |
| bq | 10,000 | cmrc2018 | 9,753 |
| SearchQA | 9,988 | rag-dataset-12000 | 9,272 |
| lawzhidao | 6,784 | DRCD | 4,714 |
| cCOVID-News | 4,727 | CHEF | 4,824 |
| AFQMC | 3,876 | CINLID | 2,883 |
| UMETRIP-QA | 2,537 | ChineseSTS | 2,497 |
| lima-chinese | 1,991 | WebCPM | 1,602 |
| Expertqa | 1,252 | CAIL2019-SCM | 648 |
| contract-nli | 628 | law-gpt | 500 |

### Other (3,103,303 pairs)

Parallel data across 51 language pairs and instruction-following retrieval data.

| Dataset | Pairs |
|---|---:|
| parallel_broad (51 lang pairs, subsampled to 40%) | 3,054,406 |
| infir_msmarco | 38,759 |
| infir_metamath | 7,104 |
| infir_leetcode | 2,540 |
| followir_train | 494 |

The `parallel_broad` data is sourced from OPUS-100, JW300, TED Talks, and WikiMatrix, with a cap of 50K pairs per source per language pair, then subsampled to 40%.

**Total: 10,110,219 pairs**

In addition, 89 `aya_dataset` and `mr-tydi` subdatasets contribute multilingual coverage across the KaLM source (included in the KaLM count above).

## Data Format

Each subdataset is stored in its own directory with the following structure:

```
<SubdatasetName>/
├── queries.parquet          # Query-document pairs
├── corpus.parquet           # Corpus documents (columns: id, text)
└── dataset_metadata.json   # Metadata (corpus_id, task_type, query_instruction, etc.)
```

### Queries Schema (`queries.parquet`)

| Column | Type | Description |
|---|---|---|
| `question_id` | int | Query identifier |
| `question` | string | Query text |
| `corpus_id` | string | Subdataset name |
| `pos_doc` | list[{id: string}] | Positive (relevant) document IDs |
| `neg_doc` | list[{id: string}] | Hard-negative document IDs |

- Document IDs reference the `id` column in `corpus.parquet`

### Corpus Schema (`corpus.parquet`)

| Column | Type | Description |
|---|---|---|
| `id` | string | Document identifier (e.g., `d_1234`) |
| `text` | string | Document text content |

### Metadata (`dataset_metadata.json`)

```json
{
  "corpus_id": "SubdatasetName",
  "class": "TextQADataset",
  "query_instruction": "Instruct: ...\nQuery:",
  "passage_instruction": "",
  "task_type": "Retrieval",
  "ids_only": true
}
```

Key fields:
- `task_type`: one of `Retrieval`, `STS`, `Classification`, `Clustering`, `InstructionRetrieval`, `BitextMining`
- `query_instruction`: prefix to prepend to queries at training time
- `source` (when present): `KaLM` for KaLM-origin datasets
- `language_pair` (when present): e.g. `en-fr` for parallel data

