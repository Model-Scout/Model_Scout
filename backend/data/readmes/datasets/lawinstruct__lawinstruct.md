---
annotations_creators:
- other
language_creators:
- found
language:
- bg 
- cs 
- da 
- de 
- el 
- en
- es 
- et 
- fi 
- fr 
- ga
- hr 
- hu 
- it 
- lt 
- lv 
- mt
- nl 
- pl 
- pt 
- ro 
- sk 
- sl 
- sv
- zh
- ja
- ko
license:
- mit
multilinguality:
- multilingual
paperswithcode_id: null
pretty_name: "LawInstruct: A Diverse Multilingual Dataset for Legal Instruction Tuning"
size_categories:
- 10M<n<100M
source_datasets:
- original
task_categories:
- fill-mask

---

# Dataset Card for LawInstruct: A Diverse Multilingual Dataset for Legal Instruction Tuning

## Table of Contents

- [Table of Contents](#table-of-contents)
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
- **Repository:** [GitHub](https://github.com/JoelNiklaus/LawInstruct)
- **Paper:** [ArXiv](https://arxiv.org/abs/2404.02127)
- **Leaderboard:**
- **Point of Contact:** [Joel Niklaus](mailto:joel@niklaus.ai)

### Dataset Summary

LawInstruct is a diverse multilingual dataset for legal instruction tuning.

### Supported Tasks and Leaderboards

The dataset supports the tasks of text-generation.

### Languages

The following languages are supported: 
bg, cs, da, de, el, en, es, et, fi, fr, ga, hr, hu, it, lt, lv, mt, nl, pl, pt, ro, sk, sl, sv, zh, ja, ko

## Dataset Structure

It is structured in the following format: {name}_train.{shard}.jsonl.xz

LawInstruct has the following data fields:
- `dataset_name`: The name of the dataset
- `subset_name`: The name of the sub dataset if applicable
- `source`: The url of the source
- `prompt_language`: The language of the prompt
- `answer_language`: The language of the answer
- `jurisdiction`: The jurisdiction of the dataset
- `task_type`: The task type of the dataset
- `downloaded_timestamp`: The timestamp when the dataset was built for lawinstruct
- `text`: the text, consisting of the prompt and the answer

### Data Instances

The file format is jsonl.xz and there is a `train` split available. 

### Data Fields

[More Information Needed]

### Data Splits

There is one split: train. 

#### Data Size


```bash
$ xz --list data/*.xz
Strms  Blocks   Compressed Uncompressed  Ratio  Check   Filename
    1       1    515.4 KiB   3445.8 KiB  0.150  CRC64   data/BrazilianBarExam-brazilian_bar_exam-train-0.jsonl.xz
    1       1    379.6 MiB   6327.9 MiB  0.060  CRC64   data/BrCAD5-brcad5_judgment-train-0.jsonl.xz
    1       1    379.7 MiB   6336.8 MiB  0.060  CRC64   data/BrCAD5-brcad5_law_area-train-0.jsonl.xz
    1       1    461.7 MiB     12.6 GiB  0.036  CRC64   data/BrCAD5-brcad5_mc-train-0.jsonl.xz
    1       1    513.0 MiB     18.6 GiB  0.027  CRC64   data/BrCAD5-brcad5_topic-train-0.jsonl.xz
    1       1    334.0 KiB   8444.7 KiB  0.040  CRC64   data/BVADecisions-bva_decisions_label-train-0.jsonl.xz
    1       1       1416 B       5329 B  0.266  CRC64   data/BVADecisions-bva_decisions_qa-train-0.jsonl.xz
    1       1   1535.5 KiB   7091.5 KiB  0.217  CRC64   data/CABarExamEssays-MainSubset-train-0.jsonl.xz
    1       1   4541.7 KiB    140.3 MiB  0.032  CRC64   data/CAIL2019-cail_2019-train-0.jsonl.xz
    1       1    609.7 KiB     14.4 MiB  0.041  CRC64   data/CAIL2022-cail_2022_crime-train-0.jsonl.xz
    1       1    797.2 KiB     15.3 MiB  0.051  CRC64   data/CAIL2022-cail_2022_mc-train-0.jsonl.xz
    1       1    518.4 KiB   8591.2 KiB  0.060  CRC64   data/CAIL2022-cail_2022_response-train-0.jsonl.xz
    1       1   1344.6 KiB   7666.5 KiB  0.175  CRC64   data/CaseBriefs-case_briefs-train-0.jsonl.xz
    1       1   2724.2 KiB     13.8 MiB  0.193  CRC64   data/ChangeMyView-change_my_view-train-0.jsonl.xz
    1       1   1368.5 KiB     90.8 MiB  0.015  CRC64   data/ContractNLI-contract_nli-train-0.jsonl.xz
    1       1    497.4 KiB     10.9 MiB  0.044  CRC64   data/EdgarNER-MainSubset-train-0.jsonl.xz
    1       1   3001.3 KiB    406.2 MiB  0.007  CRC64   data/Ell4GreekNER-MainSubset-train-0.jsonl.xz
    1       1   3410.7 KiB    705.6 MiB  0.005  CRC64   data/Ell18GreekNER-MainSubset-train-0.jsonl.xz
    1       1   1592.2 KiB     17.2 MiB  0.090  CRC64   data/EOIRPrivacy-eoir_privacy-train-0.jsonl.xz
    1       1     19.1 MiB    400.8 MiB  0.048  CRC64   data/EurLexSum-bulgarian-train-0.jsonl.xz
    1       1     12.3 MiB     80.6 MiB  0.153  CRC64   data/EurLexSum-croatian-train-0.jsonl.xz
    1       1     15.1 MiB    128.5 MiB  0.117  CRC64   data/EurLexSum-czech-train-0.jsonl.xz
    1       1     13.0 MiB     94.1 MiB  0.138  CRC64   data/EurLexSum-danish-train-0.jsonl.xz
    1       1     13.5 MiB     94.6 MiB  0.142  CRC64   data/EurLexSum-dutch-train-0.jsonl.xz
    1       1     13.2 MiB     91.4 MiB  0.144  CRC64   data/EurLexSum-english-train-0.jsonl.xz
    1       1     13.7 MiB     95.3 MiB  0.144  CRC64   data/EurLexSum-estonian-train-0.jsonl.xz
    1       1     13.8 MiB    103.3 MiB  0.133  CRC64   data/EurLexSum-finnish-train-0.jsonl.xz
    1       1     14.7 MiB    117.0 MiB  0.126  CRC64   data/EurLexSum-french-train-0.jsonl.xz
    1       1     14.6 MiB    104.8 MiB  0.139  CRC64   data/EurLexSum-german-train-0.jsonl.xz
    1       1     20.6 MiB    432.8 MiB  0.048  CRC64   data/EurLexSum-greek-train-0.jsonl.xz
    1       1     15.3 MiB    135.7 MiB  0.113  CRC64   data/EurLexSum-hungarian-train-0.jsonl.xz
    1       1    608.6 KiB   4496.0 KiB  0.135  CRC64   data/EurLexSum-irish-train-0.jsonl.xz
    1       1     13.5 MiB     96.5 MiB  0.140  CRC64   data/EurLexSum-italian-train-0.jsonl.xz
    1       1     14.4 MiB    116.5 MiB  0.123  CRC64   data/EurLexSum-latvian-train-0.jsonl.xz
    1       1     14.4 MiB    107.1 MiB  0.135  CRC64   data/EurLexSum-lithuanian-train-0.jsonl.xz
    1       1     14.8 MiB    109.0 MiB  0.136  CRC64   data/EurLexSum-maltese-train-0.jsonl.xz
    1       1     14.5 MiB    108.6 MiB  0.134  CRC64   data/EurLexSum-polish-train-0.jsonl.xz
    1       1     13.3 MiB    102.0 MiB  0.131  CRC64   data/EurLexSum-portuguese-train-0.jsonl.xz
    1       1     14.3 MiB    112.4 MiB  0.127  CRC64   data/EurLexSum-romanian-train-0.jsonl.xz
    1       1     14.5 MiB    114.4 MiB  0.127  CRC64   data/EurLexSum-slovak-train-0.jsonl.xz
    1       1     13.1 MiB     86.5 MiB  0.152  CRC64   data/EurLexSum-slovenian-train-0.jsonl.xz
    1       1     14.1 MiB    106.3 MiB  0.133  CRC64   data/EurLexSum-spanish-train-0.jsonl.xz
    1       1     12.8 MiB     95.9 MiB  0.134  CRC64   data/EurLexSum-swedish-train-0.jsonl.xz
    1       1   3062.1 KiB     47.7 MiB  0.063  CRC64   data/GermanLER-coarse-train-0.jsonl.xz
    1       1   3109.2 KiB     53.9 MiB  0.056  CRC64   data/GermanLER-fine-train-0.jsonl.xz
    1       1     66.8 KiB   2320.1 KiB  0.029  CRC64   data/GermanRentalAgreements-german_rental_agreements-train-0.jsonl.xz
    1       1    126.6 MiB    718.1 MiB  0.176  CRC64   data/ILDC-ildc-train-0.jsonl.xz
    1       1    630.1 KiB   8302.7 KiB  0.076  CRC64   data/IndianNER-MainSubset-train-0.jsonl.xz
    1       1   1338.5 KiB     31.7 MiB  0.041  CRC64   data/IndianTextSegmentation-indian_text_segmentation-train-0.jsonl.xz
    1       1    222.8 KiB   6645.0 KiB  0.034  CRC64   data/InternationalCitizenshipLawQuestions-international_citizenship_law_questions_mode_acq-train-0.jsonl.xz
    1       1     97.9 KiB   2976.9 KiB  0.033  CRC64   data/InternationalCitizenshipLawQuestions-international_citizenship_law_questions_mode_loss-train-0.jsonl.xz
    1       1   1073.5 KiB     11.7 MiB  0.090  CRC64   data/KoreanLegalQA-korean_legal_qa-train-0.jsonl.xz
    1       1    891.6 MiB     15.8 GiB  0.055  CRC64   data/LawngNli-lawng_nli_entailment-train-0.jsonl.xz
    1       1   3677.7 KiB     48.7 MiB  0.074  CRC64   data/LboxOpen-lbox_open_judgment-train-0.jsonl.xz
    1       1   2789.0 KiB     39.1 MiB  0.070  CRC64   data/LboxOpen-lbox_open_statute-train-0.jsonl.xz
    1       1     37.0 MiB    207.2 MiB  0.178  CRC64   data/LegalCaseDocumentSummarization-legal_case_summarization_india-train-0.jsonl.xz
    1       1     10.6 MiB     61.0 MiB  0.174  CRC64   data/LegalCaseDocumentSummarization-legal_case_summarization_uk-train-0.jsonl.xz
    1       1   2445.9 KiB     34.0 MiB  0.070  CRC64   data/LegalQA-legal_qa-train-0.jsonl.xz
    1       1     15.0 MiB    104.7 MiB  0.143  CRC64   data/LexGLUE-case_hold-train-0.jsonl.xz
    1       1     15.9 MiB     94.9 MiB  0.168  CRC64   data/LexGLUE-ecthr_a-train-0.jsonl.xz
    1       1     15.9 MiB     96.0 MiB  0.166  CRC64   data/LexGLUE-ecthr_b-train-0.jsonl.xz
    1       1     57.5 MiB    412.8 MiB  0.139  CRC64   data/LexGLUE-eurlex-train-0.jsonl.xz
    1       1   6186.6 KiB     77.5 MiB  0.078  CRC64   data/LexGLUE-ledgar-train-0.jsonl.xz
    1       1     36.5 MiB    177.4 MiB  0.205  CRC64   data/LexGLUE-scotus-train-0.jsonl.xz
    1       1    282.3 KiB   6855.6 KiB  0.041  CRC64   data/LexGLUE-unfair_tos-train-0.jsonl.xz
    1       1    473.9 KiB   5375.4 KiB  0.088  CRC64   data/LEXTREME-brazilian_court_decisions_judgment-train-0.jsonl.xz
    1       1    276.9 KiB   2839.1 KiB  0.098  CRC64   data/LEXTREME-brazilian_court_decisions_unanimity-train-0.jsonl.xz
    1       1    236.5 KiB   4782.8 KiB  0.049  CRC64   data/LEXTREME-covid19_emergency_event-train-0.jsonl.xz
    1       1   1056.2 KiB     19.1 MiB  0.054  CRC64   data/LEXTREME-german_argument_mining-train-0.jsonl.xz
    1       1     34.0 MiB    592.1 MiB  0.057  CRC64   data/LEXTREME-greek_legal_code_chapter-train-0.jsonl.xz
    1       1     34.1 MiB    593.3 MiB  0.058  CRC64   data/LEXTREME-greek_legal_code_subject-train-0.jsonl.xz
    1       1     33.9 MiB    592.0 MiB  0.057  CRC64   data/LEXTREME-greek_legal_code_volume-train-0.jsonl.xz
    1       1    863.6 KiB     27.7 MiB  0.030  CRC64   data/LEXTREME-greek_legal_ner-train-0.jsonl.xz
    1       1    296.2 KiB   7285.0 KiB  0.041  CRC64   data/LEXTREME-legalnero-train-0.jsonl.xz
    1       1    405.9 KiB   8646.6 KiB  0.047  CRC64   data/LEXTREME-lener_br-train-0.jsonl.xz
    1       1   1839.2 KiB     31.6 MiB  0.057  CRC64   data/LEXTREME-mapa_coarse-train-0.jsonl.xz
    1       1   1869.8 KiB     37.0 MiB  0.049  CRC64   data/LEXTREME-mapa_fine-train-0.jsonl.xz
    1       1    959.5 MiB   7131.3 MiB  0.135  CRC64   data/LEXTREME-multi_eurlex_level_1-train-0.jsonl.xz
    1       1    392.9 MiB   2914.0 MiB  0.135  CRC64   data/LEXTREME-multi_eurlex_level_1-train-1.jsonl.xz
    1       1    959.6 MiB   7137.3 MiB  0.134  CRC64   data/LEXTREME-multi_eurlex_level_2-train-0.jsonl.xz
    1       1    393.2 MiB   2918.7 MiB  0.135  CRC64   data/LEXTREME-multi_eurlex_level_2-train-1.jsonl.xz
    1       1    959.6 MiB   7142.6 MiB  0.134  CRC64   data/LEXTREME-multi_eurlex_level_3-train-0.jsonl.xz
    1       1    393.6 MiB   2923.5 MiB  0.135  CRC64   data/LEXTREME-multi_eurlex_level_3-train-1.jsonl.xz
    1       1    997.2 KiB     24.6 MiB  0.040  CRC64   data/LEXTREME-online_terms_of_service_clause_topics-train-0.jsonl.xz
    1       1    163.1 KiB   2028.8 KiB  0.080  CRC64   data/LEXTREME-online_terms_of_service_unfairness_levels-train-0.jsonl.xz
    1       1     28.9 MiB    257.6 MiB  0.112  CRC64   data/LEXTREME-swiss_judgment_prediction-train-0.jsonl.xz
    1       1       8588 B     87.6 KiB  0.096  CRC64   data/Littleton-littleton_events-train-0.jsonl.xz
    1       1     11.1 KiB    134.1 KiB  0.083  CRC64   data/Littleton-littleton_graph-train-0.jsonl.xz
    1       1    544.2 KiB     34.7 MiB  0.015  CRC64   data/MAUD-answer-train-0.jsonl.xz
    1       1    864.0 KiB     85.8 MiB  0.010  CRC64   data/MAUD-category-train-0.jsonl.xz
    1       1    891.3 KiB     86.2 MiB  0.010  CRC64   data/MAUD-question-train-0.jsonl.xz
    1       1    866.9 KiB     85.8 MiB  0.010  CRC64   data/MAUD-text_type-train-0.jsonl.xz
    1       1     40.0 KiB    167.8 KiB  0.238  CRC64   data/MCExamsLaw-mc_exams_law_explain-train-0.jsonl.xz
    1       1     28.2 KiB    114.9 KiB  0.246  CRC64   data/MCExamsLaw-mc_exams_law_no_explain-train-0.jsonl.xz
    1       1   2091.3 KiB     43.3 MiB  0.047  CRC64   data/MiningLegalArguments-agent-train-0.jsonl.xz
    1       1   2308.5 KiB     97.5 MiB  0.023  CRC64   data/MiningLegalArguments-argType-train-0.jsonl.xz
    1       1   2063.9 KiB     12.1 MiB  0.167  CRC64   data/MultiLexSum-long_to_short-train-0.jsonl.xz
    1       1   1171.9 KiB   6394.9 KiB  0.183  CRC64   data/MultiLexSum-long_to_tiny-train-0.jsonl.xz
    1       1    230.9 KiB   1530.7 KiB  0.151  CRC64   data/MultiLexSum-short_to_tiny-train-0.jsonl.xz
    1       1   9388.6 KiB    638.2 MiB  0.014  CRC64   data/NaturalInstructionsLegal-billsum_summarization-train-0.jsonl.xz
    1       1    484.4 KiB     38.2 MiB  0.012  CRC64   data/NaturalInstructionsLegal-cail2018_answer_generation-train-0.jsonl.xz
    1       1   3485.3 KiB    189.5 MiB  0.018  CRC64   data/NaturalInstructionsLegal-casehold_legal_answer_generation-train-0.jsonl.xz
    1       1   3724.4 KiB    201.4 MiB  0.018  CRC64   data/NaturalInstructionsLegal-casehold_legal_incorrect_answer_generation-train-0.jsonl.xz
    1       1   4300.6 KiB    228.0 MiB  0.018  CRC64   data/NaturalInstructionsLegal-cuad_answer_generation-train-0.jsonl.xz
    1       1   4302.7 KiB    227.8 MiB  0.018  CRC64   data/NaturalInstructionsLegal-cuad_question_generation-train-0.jsonl.xz
    1       1    201.9 KiB     22.7 MiB  0.009  CRC64   data/NaturalInstructionsLegal-eurlex_classification-train-0.jsonl.xz
    1       1    284.3 KiB     19.9 MiB  0.014  CRC64   data/NaturalInstructionsLegal-eurlex_summarization-train-0.jsonl.xz
    1       1    166.9 KiB     21.5 MiB  0.008  CRC64   data/NaturalInstructionsLegal-online_privacy_policy_text_information_type_generation-train-0.jsonl.xz
    1       1    165.1 KiB     21.6 MiB  0.007  CRC64   data/NaturalInstructionsLegal-online_privacy_policy_text_purpose_answer_generation-train-0.jsonl.xz
    1       1    246.8 KiB     16.4 MiB  0.015  CRC64   data/NaturalInstructionsLegal-overruling_legal_classification-train-0.jsonl.xz
    1       1   5872.3 KiB     31.8 MiB  0.180  CRC64   data/OLCMemos-olc_memos-train-0.jsonl.xz
    1       1     76.7 KiB    540.5 KiB  0.142  CRC64   data/PlainEnglishContractsSummarization-plain_english_contracts_summarization-train-0.jsonl.xz
    1       1   1246.7 KiB    199.4 MiB  0.006  CRC64   data/PrivacyQA-privacy_qa-train-0.jsonl.xz
    1       1    316.0 KiB   4538.1 KiB  0.070  CRC64   data/PrivacySummarization-privacy_summarization-train-0.jsonl.xz
    1       1   1098.7 KiB   6969.7 KiB  0.158  CRC64   data/ReClor-reclor-train-0.jsonl.xz
    1       1     50.5 MiB    412.2 MiB  0.123  CRC64   data/RedditLegalQA-reddit_legal_qa-train-0.jsonl.xz
    1       1     11.0 KiB    134.9 KiB  0.082  CRC64   data/Sara-sara_entailment-train-0.jsonl.xz
    1       1     11.5 KiB    145.1 KiB  0.079  CRC64   data/Sara-sara_tax_liability-train-0.jsonl.xz
    1       1     36.6 KiB    586.5 KiB  0.062  CRC64   data/SaraProlog-sara_prolog_facts-train-0.jsonl.xz
    1       1     18.2 KiB    132.2 KiB  0.138  CRC64   data/SaraProlog-sara_prolog_statute-train-0.jsonl.xz
    1       1     90.3 KiB   1531.4 KiB  0.059  CRC64   data/ShortAnswerFeedback-short_answer_feedback_error_class-train-0.jsonl.xz
    1       1     26.8 KiB   2218.5 KiB  0.012  CRC64   data/ShortAnswerFeedback-short_answer_feedback_openqa-train-0.jsonl.xz
    1       1     91.0 KiB   1513.1 KiB  0.060  CRC64   data/ShortAnswerFeedback-short_answer_feedback_rating-train-0.jsonl.xz
    1       1     16.0 KiB    118.9 KiB  0.135  CRC64   data/SpanishLaborLaw-spanish_labor_law-train-0.jsonl.xz
    1       1   6562.3 KiB     31.0 MiB  0.207  CRC64   data/StackExchangeQuestionsLegal-stack_exchange_questions_legal-train-0.jsonl.xz
    1       1    128.2 KiB   1080.4 KiB  0.119  CRC64   data/SwissCourtViewGeneration-swiss_judgment_court_view_generation_lower_court-train-0.jsonl.xz
    1       1    901.2 MiB   5463.4 MiB  0.165  CRC64   data/SwissCourtViewGeneration-swiss_judgment_court_view_generation_same_court-train-0.jsonl.xz
    1       1    211.4 MiB   1320.8 MiB  0.160  CRC64   data/SwissCriticalityPrediction-swiss_judgment_criticality-train-0.jsonl.xz
    1       1    130.3 MiB   1984.4 MiB  0.066  CRC64   data/SwissJudgmentPrediction-swiss_judgment_multiple_choice-train-0.jsonl.xz
    1       1    740.1 MiB   4651.8 MiB  0.159  CRC64   data/SwissJudgmentPredictionXL-swiss_judgment_dismiss_approve-train-0.jsonl.xz
    1       1     39.3 MiB    252.1 MiB  0.156  CRC64   data/SwissLawAreaPrediction-swiss_judgment_area_of_law_main_area-train-0.jsonl.xz
    1       1     39.3 MiB    252.2 MiB  0.156  CRC64   data/SwissLawAreaPrediction-swiss_judgment_area_of_law_sub_area-train-0.jsonl.xz
    1       1     62.9 MiB    320.2 MiB  0.196  CRC64   data/SwissLeadingDecisions-swiss_judgment_location-train-0.jsonl.xz
    1       1     60.3 MiB    398.0 MiB  0.152  CRC64   data/SwissLegislation-swiss_legislation_abbreviation-train-0.jsonl.xz
    1       1    121.5 MiB    868.3 MiB  0.140  CRC64   data/SwissLegislation-swiss_legislation_canton-train-0.jsonl.xz
    1       1     20.8 MiB    136.8 MiB  0.152  CRC64   data/SwissLegislation-swiss_legislation_short-train-0.jsonl.xz
    1       1    121.8 MiB    872.3 MiB  0.140  CRC64   data/SwissLegislation-swiss_legislation_title-train-0.jsonl.xz
    1       1    199.9 KiB     13.6 MiB  0.014  CRC64   data/TsccAlqac-tscc_alqac_question_answering-train-0.jsonl.xz
    1       1   1221.8 KiB     20.3 MiB  0.059  CRC64   data/TurkishConstitutionalCourt-turkish_constitutional_multiple_choice-train-0.jsonl.xz
    1       1   1130.7 KiB     10.0 MiB  0.110  CRC64   data/TurkishConstitutionalCourt-turkish_constitutional_violation_no_violation-train-0.jsonl.xz
    1       1   3465.9 KiB     29.3 MiB  0.116  CRC64   data/USClassActions-us_class_actions_win_lose-train-0.jsonl.xz
    1       1     94.7 KiB   2548.8 KiB  0.037  CRC64   data/ValidWills-valid_wills_entailment-train-0.jsonl.xz
-------------------------------------------------------------------------------
  142     142      9.8 GiB    116.5 GiB  0.084  CRC64   142 files

```

## Dataset Creation

This dataset has been created by running the code from the [LawInstruct](https://github.com/JoelNiklaus/LawInstruct) repo.

For this public version of the dataset we removed the datasets CiviproQuestions, COLIEE, JECQA and MBE because of restrictive licenses.

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]


### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

```
@misc{niklaus2024flawnt5,
      title={FLawN-T5: An Empirical Examination of Effective Instruction-Tuning Data Mixtures for Legal Reasoning}, 
      author={Joel Niklaus and Lucia Zheng and Arya D. McCarthy and Christopher Hahn and Brian M. Rosen and Peter Henderson and Daniel E. Ho and Garrett Honke and Percy Liang and Christopher Manning},
      year={2024},
      eprint={2404.02127},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

### Contributions

Thanks to [@JoelNiklaus](https://github.com/joelniklaus) for adding this dataset.
