---
license: bsd-2-clause
language:
- el
- fr
- it
- es
- pt
- ko
- fi
- lt
- bg
task_categories:
- text-classification
task_ids:
- natural-language-inference
- multi-input-text-classification
size_categories:
- 10K<n<100K
---
# Dataset Card for Dataset Name

## Dataset Description

- **Homepage:** 
- **Repository:** 
- **Paper:** 
- **Leaderboard:** 
- **Point of Contact:** 

### Dataset Summary

This repository contains a collection of machine translations of [LingNLI](https://github.com/Alicia-Parrish/ling_in_loop) dataset 
into 9 different languages (Bulgarian, Finnish, French, Greek, Italian, Korean, Lithuanian, Portuguese, Spanish). The goal is to predict textual entailment (does sentence A 
imply/contradict/neither sentence B), which is a classification task (given two sentences, 
predict one of three labels). It is here formatted in the same manner as the widely used [XNLI](https://huggingface.co/datasets/xnli) dataset for convenience.

If you want to use this dataset only in a specific language among those provided here, you can filter data by selecting only the language column value you wish.

### Supported Tasks and Leaderboards

This dataset can be used for the task of Natural Language Inference (NLI), also known as Recognizing Textual Entailment (RTE), which is a sentence-pair classification task.

## Dataset Structure

### Data Fields

- `language`: The language in which the pair of sentences is given.
- `premise`: The machine translated premise in the target language.
- `hypothesis`: The machine translated premise in the target language.
- `label`: The classification label, with possible values 0 (`entailment`), 1 (`neutral`), 2 (`contradiction`).
- `label_text`: The classification label, with possible values `entailment` (0), `neutral` (1), `contradiction` (2).
- `premise_original`: The original premise from the English source dataset.
- `hypothesis_original`: The original hypothesis from the English source dataset.

### Data Splits

For the whole dataset (LitL and LotS subsets):
|  language   |train|validation|
|-------------|----:|---------:|
|all_languages|269865|      44037|
|el-gr        |29985|      4893|
|fr           |29985|      4893|
|it           |29985|      4893|
|es           |29985|      4893|
|pt           |29985|      4893|
|ko           |29985|      4893|
|fi           |29985|      4893|
|lt           |29985|      4893|
|bg           |29985|      4893|

For LitL subset:
|  language   |train|validation|
|-------------|----:|---------:|
|all_languages|134955|      21825|
|el-gr        |14995|      2425|
|fr           |14995|      2425|
|it           |14995|      2425|
|es           |14995|      2425|
|pt           |14995|      2425|
|ko           |14995|      2425|
|fi           |14995|      2425|
|lt           |14995|      2425|
|bg           |14995|      2425|

For LotS subset:
|  language   |train|validation|
|-------------|----:|---------:|
|all_languages|134910|      22212|
|el-gr        |14990|      2468|
|fr           |14990|      2468|
|it           |14990|      2468|
|es           |14990|      2468|
|pt           |14990|      2468|
|ko           |14990|      2468|
|fi           |14990|      2468|
|lt           |14990|      2468|
|bg           |14990|      2468|

## Dataset Creation

The two subsets of the original dataset were machine translated using the latest neural machine translation [opus-mt-tc-big](https://huggingface.co/models?sort=downloads&search=opus-mt-tc-big) models available for the respective languages. 
Running the translations lasted from March 25, 2023 until April 8, 2023.

## Additional Information

### Citation Information

**BibTeX:**

````BibTeX
@inproceedings{skandalis-etal-2024-new-datasets,
    title = "New Datasets for Automatic Detection of Textual Entailment and of Contradictions between Sentences in {F}rench",
    author = "Skandalis, Maximos  and
      Moot, Richard  and
      Retor{\'e}, Christian  and
      Robillard, Simon",
    editor = "Calzolari, Nicoletta  and
      Kan, Min-Yen  and
      Hoste, Veronique  and
      Lenci, Alessandro  and
      Sakti, Sakriani  and
      Xue, Nianwen",
    booktitle = "Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)",
    month = may,
    year = "2024",
    address = "Torino, Italy",
    publisher = "ELRA and ICCL",
    url = "https://aclanthology.org/2024.lrec-main.1065",
    pages = "12173--12186",
    abstract = "This paper introduces DACCORD, an original dataset in French for automatic detection of contradictions between sentences. It also presents new, manually translated versions of two datasets, namely the well known dataset RTE3 and the recent dataset GQNLI, from English to French, for the task of natural language inference / recognising textual entailment, which is a sentence-pair classification task. These datasets help increase the admittedly limited number of datasets in French available for these tasks. DACCORD consists of 1034 pairs of sentences and is the first dataset exclusively dedicated to this task and covering among others the topic of the Russian invasion in Ukraine. RTE3-FR contains 800 examples for each of its validation and test subsets, while GQNLI-FR is composed of 300 pairs of sentences and focuses specifically on the use of generalised quantifiers. Our experiments on these datasets show that they are more challenging than the two already existing datasets for the mainstream NLI task in French (XNLI, FraCaS). For languages other than English, most deep learning models for NLI tasks currently have only XNLI available as a training set. Additional datasets, such as ours for French, could permit different training and evaluation strategies, producing more robust results and reducing the inevitable biases present in any single dataset.",
}

@inproceedings{parrish-etal-2021-putting-linguist,
    title = "Does Putting a Linguist in the Loop Improve {NLU} Data Collection?",
    author = "Parrish, Alicia  and
      Huang, William  and
      Agha, Omar  and
      Lee, Soo-Hwan  and
      Nangia, Nikita  and
      Warstadt, Alexia  and
      Aggarwal, Karmanya  and
      Allaway, Emily  and
      Linzen, Tal  and
      Bowman, Samuel R.",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2021",
    month = nov,
    year = "2021",
    address = "Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-emnlp.421",
    doi = "10.18653/v1/2021.findings-emnlp.421",
    pages = "4886--4901",
    abstract = "Many crowdsourced NLP datasets contain systematic artifacts that are identified only after data collection is complete. Earlier identification of these issues should make it easier to create high-quality training and evaluation data. We attempt this by evaluating protocols in which expert linguists work {`}in the loop{'} during data collection to identify and address these issues by adjusting task instructions and incentives. Using natural language inference as a test case, we compare three data collection protocols: (i) a baseline protocol with no linguist involvement, (ii) a linguist-in-the-loop intervention with iteratively-updated constraints on the writing task, and (iii) an extension that adds direct interaction between linguists and crowdworkers via a chatroom. We find that linguist involvement does not lead to increased accuracy on out-of-domain test sets compared to baseline, and adding a chatroom has no effect on the data. Linguist involvement does, however, lead to more challenging evaluation data and higher accuracy on some challenge sets, demonstrating the benefits of integrating expert analysis during data collection.",
}
````

**ACL:**

Maximos Skandalis, Richard Moot, Christian Retoré, and Simon Robillard. 2024. [New Datasets for Automatic Detection of Textual Entailment and of Contradictions between Sentences in French](https://aclanthology.org/2024.lrec-main.1065). In *Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)*, pages 12173–12186, Torino, Italy. ELRA and ICCL.

And

Alicia Parrish, William Huang, Omar Agha, Soo-Hwan Lee, Nikita Nangia, Alexia Warstadt, Karmanya Aggarwal, Emily Allaway, Tal Linzen, and Samuel R. Bowman. 2021. [Does Putting a Linguist in the Loop Improve NLU Data Collection?](https://aclanthology.org/2021.findings-emnlp.421). In *Findings of the Association for Computational Linguistics: EMNLP 2021*, pages 4886–4901, Punta Cana, Dominican Republic. Association for Computational Linguistics.

### Acknowledgements

These translations of the original dataset were done as part of a research project supported by the Defence Innovation Agency (AID) of the Directorate General of Armament (DGA) of the French Ministry of Armed Forces, and by the ICO, _Institut Cybersécurité Occitanie_, funded by Région Occitanie, France.