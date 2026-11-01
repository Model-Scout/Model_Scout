---
license: cc-by-4.0
task_categories:
- question-answering
language:
- ko
pretty_name: FINEST
size_categories:
- 100K<n<1M
configs:
- config_name: raw_responses
  data_files:
    - split: KOLD
      path: "data/raw_responses/kold_responses.csv"
    - split: SQuARe_train
      path: "data/raw_responses/square-train_responses.csv"
    - split: SQuARe_valid
      path: "data/raw_responses/square-valid_responses.csv"
    - split: IBM_Rank_30k
      path: "data/raw_responses/arg_responses.csv"
- config_name: evaluation
  data_files:
    - split: evaluation
      path: "data/evaluation/evaluations_6k.csv"
---

# FINEST

This is the official repository of **[FINEST: Improving LLM Responses to Sensitive Topics\\Through Fine-Grained Evaluation](https://github.com/nlee0212/FINEST/tree/main)** (EACL 2026 Findings).

## Dataset

We release the FINEST dataset in two complementary configurations to support both reproducibility and further research on fine-grained evaluation of LLM responses to sensitive topics.

### 1. `raw_responses`

The `raw_responses` configuration contains the full set of questions and model-generated responses used as inputs to our evaluation framework.  
This configuration corresponds to the data summarized in **Table 2** of the paper.

We collect sensitive-topic questions from several publicly available datasets:
- **KOLD** (Jeong et al., 2022) — a Korean offensive language dataset with hierarchical annotations of offensive text and target spans
- **SQuARe** (Lee et al., 2023) — a large-scale Korean dataset of sensitive questions with acceptable/non-acceptable responses created through human-machine collaboration
- **IBM-Rank-30k** (Gretz et al., 2020) — an English dataset of ~30k arguments with point-wise quality ranking annotations.

For each question in these sources, we generate multiple responses using large language models.  
These responses are **not filtered or post-processed** based on evaluation outcomes and are released to enable independent analysis of raw LLM behavior on sensitive prompts and task setups.

Each split includes:
- the original question,
- the model-generated response,
- metadata indicating the source dataset and generation setting.

This configuration is intended for use cases such as:
- analysis of raw LLM behavior on sensitive topics,
- application of alternative evaluation criteria or taxonomies,
- reproduction of the evaluation and improvement pipeline from scratch.

---

### 2. `evaluation`

The `evaluation` configuration contains the subset of data used for the main quantitative and qualitative analyses in the paper.  
After applying the proposed evaluation framework to the full set of responses, we sample **6,000 question–response pairs** and annotate them using the FINEST taxonomy.

This subset forms the basis for:
- the improvement results,
- fine-grained score and error analyses,
- and the findings reported in Sections 5 and 6 of the paper.

Each instance in this configuration includes:
- the question and response,
- fine-grained evaluation scores and error categories for **Content**, **Logic**, and **Appropriateness**,
- additional metadata used in the analysis.

We release this configuration separately to clearly distinguish the **evaluated subset used in the paper** from the larger pool of raw responses, and to facilitate direct comparison with reported results.

---

## Usage Notes

- The two configurations are complementary: `raw_responses` provides scale and coverage, while `evaluation` provides depth and direct correspondence to the paper’s analyses.
- All data are released under the **CC BY 4.0** license.
- The dataset is primarily in **Korean**, reflecting the focus of the study.