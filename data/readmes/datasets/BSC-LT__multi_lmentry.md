---
language:
- ca
- de
- en
- es
- eu
- gl
- it
- ko
- pt
language_bcp47:
- pt-BR
license: cc-by-sa-4.0
tags:
- evaluation
- multilingual
pretty_name: Multi-LMentry
task_categories:
- question-answering
configs:
  - config_name: ca
    data_files: ca/*.jsonl
  - config_name: de
    data_files: de/*.jsonl
  - config_name: en
    data_files: en/*.jsonl
  - config_name: es
    data_files: es/*.jsonl
  - config_name: eu
    data_files: eu/*.jsonl
  - config_name: gl
    data_files: gl/*.jsonl
  - config_name: it
    data_files: it/*.jsonl
  - config_name: ko
    data_files: ko/*.jsonl
  - config_name: pt_br
    data_files: pt_br/*.jsonl
dataset_info:
  features:
    - name: id
      dtype: string
    - name: input
      dtype: string
    - name: metadata
      dtype: string
    - name: canary
      dtype: string
  splits:
    - name: test
---


# Multi-LMentry

This dataset card provides documentation for **Multi-LMentry**, a multilingual benchmark designed for evaluating large language models (LLMs) on fundamental, elementary-level tasks across nine languages. It is the official dataset release accompanying the EMNLP 2025 paper "Multi-LMentry: Can Multilingual LLMs Solve Elementary Tasks Across Languages?".

## Dataset Details

### Dataset Description

Multi-LMentry is a multilingual extension of [LMentry (Efrat et al., 2023)](https://aclanthology.org/2023.findings-acl.666/), which evaluates LLMs on tasks that are trivial for humans but often challenging for models. It covers **nine languages**:  
- Catalan  
- German  
- Spanish  
- Basque  
- Galician  
- Korean  
- Italian  
- Brazilian Portuguese  
- English (original LMentry dataset)

The dataset enables systematic evaluation of core model abilities across low-, mid-, and high-resource languages. Tasks were recreated manually with the help of native speakers, ensuring linguistic and cultural appropriateness rather than relying on direct translation.

### Dataset Sources

- **Paper:** Accepted at EMNLP 2025 main conference (link pending)
- [**GitHub Repository:**](https://github.com/langtech-bsc/multi_lmentry) Code to perform the evaluation on Multi-LMentry

## Uses

The dataset is intended for:  
- **Evaluation of LLMs** on elementary reasoning and understanding tasks.  
- **Cross-lingual comparisons**, especially between high-resource and low-resource languages.  
- **Diagnostics / unit tests** of fundamental model abilities.  

It is **not intended** for training language models directly.  

## Dataset Structure

- The dataset is organized by **language folders**.  
- Inside each folder, there is **one JSON file per task**.  
- Each JSON contains input prompts and expected outputs for that task.  
- Tasks include simple sentence construction, contextual word choice, alphabetic reasoning, etc.  
- Some tasks are language-specific (e.g., rhyming words are excluded where not applicable).  

## How to Use

```
from datasets import load_dataset
import json

# Load the Spanish "bigger_number" task
ds = load_dataset(
    "BSC-LT/multi_lmentry",
    "es",
    data_files="es/bigger_number.jsonl"
)["train"]

# Access first example
example = ds[0]
print("Input:", example["input"])

# Convert metadata from string to dictionary
metadata = json.loads(example["metadata"])
print("Metadata:", metadata)

# Access the answer from metadata
answer = metadata.get("answer")
print("Answer:", answer)
``` 

**Notes**:

- The metadata field contains task-specific information, including the answer. Its structure varies depending on the task, for example:
  - Multiple-choice tasks may include a list of distractors and the correct answer index.
  - Open-ended tasks, like "ends_with_letter", may only include task-specific metadata such as the target letter, without a predefined answer.
  - Other fields (e.g., num_digits, n1, n2, template_id) may differ depending on the task type.
- Each JSONL file corresponds to a specific task; you can load multiple tasks by specifying multiple data_files.
- Evaluation: Multi-LMentry includes manually crafted regexes for each task to automatically check answers. These evaluation scripts are available in the (GitHub repository)[https://github.com/langtech-bsc/multi_lmentry] and ready to use for running systematic assessments of model outputs.

## Dataset Creation

### Curation Rationale

The motivation is to provide a **systematic, multilingual benchmark** for assessing whether LLMs can perform **basic reasoning tasks** that humans—even with only elementary proficiency—find trivial. This is crucial since many evaluations today focus on high-level reasoning while overlooking core capabilities.

### Source Data

#### Data Collection and Processing

- Data was **manually created** in each language, rather than translated from English.  
- Native speakers were involved to ensure correctness, cultural relevance, and avoidance of ambiguity or bias.  
- Tasks were adapted to respect **linguistic characteristics**, such as orthography, morphology, or alphabet differences.

#### Who are the source data producers?

- **Native speakers** of the target languages, who carefully designed and validated the tasks.  
- Task designs follow the original LMentry methodology but were recreated independently per language by native speakers of the target languages, who carefully designed and validated the tasks. 

## Acknowledgements

We gratefully acknowledge the support of Future AI Research ([PNRR MUR project PE0000013-FAIR](https://fondazione-fair.it/en/)).
 
The authors gratefully acknowledge the support of the AI Factory IT4LIA project and the CINECA award FAIR_NLP under the ISCRA initiative for granting access high-performance computing resources.

This work is funded by the Ministerio para la Transformación Digital y de la Función Pública and Plan de Recuperación, Transformación y Resiliencia - Funded by EU – NextGenerationEU within the framework of the project ILENIA with references 2022/TL22/00215337, 2022/TL22/00215336 and 2022/TL22/00215335, and within the framework of the project Desarrollo Modelos ALIA.

This work has been promoted and financed by the Generalitat de Catalunya through the Aina project. 

## License Information

[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.ca)

## Citation

### Bibtex

```bibtex
@inproceedings{moroni-etal-2025-multi,
    title = "Multi-{LM}entry: Can Multilingual {LLM}s Solve Elementary Tasks Across Languages?",
    author = "Moroni, Luca  and
      Aula-Blasco, Javier  and
      Conia, Simone  and
      Baucells, Irene  and
      Perez, Naiara  and
      Su{\'a}rez, Silvia Paniagua  and
      Sall{\'e}s, Anna  and
      Ostendorff, Malte  and
      Falc{\~a}o, J{\'u}lia  and
      Son, Guijin  and
      Gonzalez-Agirre, Aitor  and
      Navigli, Roberto  and
      Villegas, Marta",
    editor = "Christodoulopoulos, Christos  and
      Chakraborty, Tanmoy  and
      Rose, Carolyn  and
      Peng, Violet",
    booktitle = "Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2025",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.emnlp-main.1731/",
    doi = "10.18653/v1/2025.emnlp-main.1731",
    pages = "34114--34145",
    ISBN = "979-8-89176-332-6"
}
```
