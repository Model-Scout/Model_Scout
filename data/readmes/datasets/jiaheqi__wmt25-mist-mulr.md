---
license: cc-by-sa-4.0
language:
- zh
- cs
- nl
- en
- et
- fr
- de
- ja
- ko
- fa
- pt
- ru
- es
- sv
- uk
pretty_name: WMT25 MIST Multilingual Linguistic Reasoning (MuLR)
size_categories:
- 1K<n<10K
---

# WMT 2025 MIST Multilingual Linguistic Reasoning Subtask (MuLR)

This dataset contains the prompts and answers for the WMT2025 MIST sub-task on linguistic reasoning.
The tasks consist of linguistic reasoning puzzles in 15 languages. 

Every puzzle corresponds to a sub-task of the 2024 IOL problems, concerning four languages (Koryak, Hadza, Komnzo,
Dâw, and Yanyuwa). The original IOL problems are broken down into 90 individual sub-tasks (e.g. turning a 10-way mapping problem into 10 individual mapping problems).
As a result, there are four classification tasks, 1 editing task, 20 fill-in-blank tasks, 24 mapping tasks, and 41 translation tasks. 
Each of them is represented by one prompt/answer pair in this dataset. As in the original IOL competition, each sub-task has a fixed number of points (summing to 100 overall), reflecting a difficulty of the sub-task. 
The detailed process of the task preparation is described in the [WMT MIST overview paper](https://www2.statmt.org/wmt25/pdf/2025.wmt-1.24.pdf), section 2.1.

## Format
Each row contains the following fields:
- `id`: unique identifier. It allows mapping back to the original IOL tasks, e.g. `3:a10` means it's from task 3a, the 10th problem within that task.
- `prompt`: task prompt including instruction template as used for the official WMT MIST evaluations.
- `type`: task type, e.g. `translation`, `classification`, ... see explained below.
- `eval_type`: evaluation type corresponding to the task type.
- `instruction_language`: the IOL problem language, i.e. one of Koryak, Hadza, Komnzo,
Dâw, and Yanyuwa
- `problem_language`: the task instruction language, one of 15.
- `answer`: reference answer.
- `points`: number of points that this prompt contributes to the overall task.
- `meta`: the author name, task year and problem number from IOL.


## Evaluation
For evaluation, the `eval_type` for each prompt needs to be respected.
Classification, fill-in-blank, mapping tasks are evaluated with exact match (after lowercasing).
Editing and translation tasks are evaluated with ChrF (sacrebleu default).
To obtain the final number of points, multiply each score with the respective points for each task (e.g. a model scored 0.3 ChrF on a translation task with 2 points-> points assigned for this task will be 0.3*2=0.6, and sum them up by language.

## License and Use
The problems and their translations are sourced from [IOL](https://ioling.org/), and are copyrighted by ©2003-2024 International Linguistics Olympiad.
They may only be used for research purposes and evaluation, not training.

## Citation
If you use this dataset, please cite it as follows:
```
@inproceedings{kocmi-etal-2025-findings-wmt25,
    title = "Findings of the {WMT}25 Multilingual Instruction Shared Task: Persistent Hurdles in Reasoning, Generation, and Evaluation",
    author = "Kocmi, Tom  and
      Agrawal, Sweta  and
      Artemova, Ekaterina  and
      Avramidis, Eleftherios  and
      Briakou, Eleftheria  and
      Chen, Pinzhen  and
      Fadaee, Marzieh  and
      Freitag, Markus  and
      Grundkiewicz, Roman  and
      Hou, Yupeng  and
      Koehn, Philipp  and
      Kreutzer, Julia  and
      Mansour, Saab  and
      Perrella, Stefano  and
      Proietti, Lorenzo  and
      Riley, Parker  and
      S{\'a}nchez, Eduardo  and
      Schmidtova, Patricia  and
      Shmatova, Mariya  and
      Zouhar, Vil{\'e}m",
    editor = "Haddow, Barry  and
      Kocmi, Tom  and
      Koehn, Philipp  and
      Monz, Christof",
    booktitle = "Proceedings of the Tenth Conference on Machine Translation",
    month = nov,
    year = "2025",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.wmt-1.23/",
    doi = "10.18653/v1/2025.wmt-1.23",
    pages = "414--435",
    ISBN = "979-8-89176-341-8",
    abstract = "The WMT25 Multilingual Instruction Shared Task (MIST) introduces a benchmark to evaluate large language models (LLMs) across 30 languages. The benchmark covers five types of problems: machine translation, linguistic reasoning, open-ended generation, cross-lingual summarization, and LLM-as-a-judge.We provide automatic evaluation and collect human annotations, which highlight the limitations of automatic evaluation and allow further research into metric meta-evaluation. We run on our benchmark a diverse set of open- and closed-weight LLMs, providing a broad assessment of the multilingual capabilities of current LLMs. Results highlight substantial variation across sub-tasks and languages, revealing persistent challenges in reasoning, cross-lingual generation, and evaluation reliability. This work establishes a standardized framework for measuring future progress in multilingual LLM development."
}
```