---
license: mit
task_categories:
- question-answering
- text-generation
language:
- ar
- bn
- cs
- zh
- nl
- en
- fa
- fr
- de
- he
- hi
- id
- it
- ja
- km
- ko
- ms
- mr
- pl
- pt
- ro
- ru
- es
- sv
- tl
- th
- tr
- ur
- yue
- vi
pretty_name: MultiLoKo
tags:
- text
configs:
- config_name: default
  data_files:
  - path: "*/dev.jsonl"
    split: dev
  - path: "english/dev_translated_machine_*.jsonl"
    split: dev_translated_machine
  - path: "english/dev_translated_human_*.jsonl"
    split: dev_translated_human 
  - path: "*/dev_translated_human_english.jsonl"
    split: enloko
- config_name: arabic
  data_files:
  - path: arabic/dev.jsonl
    split: dev
  - path: arabic/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: arabic/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: bengali
  data_files:
  - path: bengali/dev.jsonl
    split: dev
  - path: bengali/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: bengali/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: cantonese
  data_files:
  - path: cantonese/dev.jsonl
    split: dev
  - path: cantonese/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: cantonese/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: czech
  data_files:
  - path: czech/dev.jsonl
    split: dev
  - path: czech/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: czech/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: dutch
  data_files:
  - path: dutch/dev.jsonl
    split: dev
  - path: dutch/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: dutch/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: english
  data_files:
  - path: english/dev.jsonl
    split: dev
  - path: english/dev_translated_machine_*.jsonl
    split: dev_mt
  - path: english/dev_translated_human_*.jsonl
    split: dev_translated
- config_name: farsi
  data_files:
  - path: farsi/dev.jsonl
    split: dev
  - path: farsi/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: farsi/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: french
  data_files:
  - path: french/dev.jsonl
    split: dev
  - path: french/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: french/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: german
  data_files:
  - path: german/dev.jsonl
    split: dev
  - path: german/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: german/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: hebrew
  data_files:
  - path: hebrew/dev.jsonl
    split: dev
  - path: hebrew/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: hebrew/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: hindi
  data_files:
  - path: hindi/dev.jsonl
    split: dev
  - path: hindi/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: hindi/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: indonesian
  data_files:
  - path: indonesian/dev.jsonl
    split: dev
  - path: indonesian/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: indonesian/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: italian
  data_files:
  - path: italian/dev.jsonl
    split: dev
  - path: italian/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: italian/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: japanese
  data_files:
  - path: japanese/dev.jsonl
    split: dev
  - path: japanese/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: japanese/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: khmer
  data_files:
  - path: khmer/dev.jsonl
    split: dev
  - path: khmer/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: khmer/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: korean
  data_files:
  - path: korean/dev.jsonl
    split: dev
  - path: korean/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: korean/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: malay
  data_files:
  - path: malay/dev.jsonl
    split: dev
  - path: malay/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: malay/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: marathi
  data_files:
  - path: marathi/dev.jsonl
    split: dev
  - path: marathi/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: marathi/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: polish
  data_files:
  - path: polish/dev.jsonl
    split: dev
  - path: polish/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: polish/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: portuguese
  data_files:
  - path: portuguese/dev.jsonl
    split: dev
  - path: portuguese/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: portuguese/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: romanian
  data_files:
  - path: romanian/dev.jsonl
    split: dev
  - path: romanian/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: romanian/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: russian
  data_files:
  - path: russian/dev.jsonl
    split: dev
  - path: russian/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: russian/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: simplified_mandarin
  data_files:
  - path: simplified_mandarin/dev.jsonl
    split: dev
  - path: simplified_mandarin/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: simplified_mandarin/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: spanish
  data_files:
  - path: spanish/dev.jsonl
    split: dev
  - path: spanish/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: spanish/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: swedish
  data_files:
  - path: swedish/dev.jsonl
    split: dev
  - path: swedish/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: swedish/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: tagalog
  data_files:
  - path: tagalog/dev.jsonl
    split: dev
  - path: tagalog/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: tagalog/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: thai
  data_files:
  - path: thai/dev.jsonl
    split: dev
  - path: thai/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: thai/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: traditional_mandarin
  data_files:
  - path: traditional_mandarin/dev.jsonl
    split: dev
  - path: traditional_mandarin/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: traditional_mandarin/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: turkish
  data_files:
  - path: turkish/dev.jsonl
    split: dev
  - path: turkish/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: turkish/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: urdu
  data_files:
  - path: urdu/dev.jsonl
    split: dev
  - path: urdu/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: urdu/dev_translated_human_english.jsonl
    split: dev_translated
- config_name: vietnamese
  data_files:
  - path: vietnamese/dev.jsonl
    split: dev
  - path: vietnamese/dev_translated_machine_english.jsonl
    split: dev_mt
  - path: vietnamese/dev_translated_human_english.jsonl
    split: dev_translated
extra_gated_heading: "Protecting the integrity of MultiLoKo for evaluation"
extra_gated_fields: 
  I agree not to re-host MultiLoKo in places where it could be picked up by web crawlers: checkbox
  If I evaluate using MultiLoKo, I will ensure that its questions are not in the training data: checkbox
---
# MultiLoKo: a multilingual local knowledge benchmark for LLMs

MultiLoKo is a multilingual knowledge benchmark, covering 30 languages plus English.
The questions are separately sourced for each language, with an annotation protocol designed to target locally relevant topics for the respective language.
MultiLoKo contains the original data for each language, as well as both human and machine-authored translations of each non-English subset into English and vice versa, facilitating studies into a variety of research questions relating to multilinguality.
More information about the benchmark design can be found in the release paper of the benchmark:

* Dieuwke Hupkes and Nikolay Bogoychev.
[MultiLoKo: a multilingual local knowledge benchmark for LLMs spanning 31 languages](https://arxiv.org/abs/2504.10356).

```
@article{hupkes2025multiloko,
      title={MultiLoKo: a multilingual local knowledge benchmark for LLMs spanning 31 languages
},
      author = {Dieuwke Hupkes and Nikolay Bogoychev},
      year = {2025},
      journal = {CoRR},
      volume = {abs/2504.10356},
      eprinttype = {arXiv},
      eprint = {2504.10356},
      url = {https://doi.org/10.48550/arXiv.2504.10356},
}
```

## Data

Each language in MultiLoKo has its own subdirectory, containing:
- A jsonl file `dev.jsonl` containing  the 250 locally sourced questions for the respective language.
- A jsonl file `knowledge_fewshot.jsonl`, containing five fewshot examples for the language.
- A jsonl file `dev_translated_human_english.jsonl` with the human translations of the file into English (for English, instead there will be 30 files `dev_translated_human_{language}.jsonl`, for each of the respective languages).
- A jsonl file `dev_translated_machine_english.jsonl` with the machine translations of the file into English (for English, instead there will be 30 files `dev_translated_machine_{language}.jsonl`, for each of the respective languages).

Multilingual prompts can be found in our our github repository, in the file [examples/prompts.py](https://github.com/facebookresearch/multiloko/examples/prompts.py)

### Data format

The benchmark data is stored in jsonl files, containing a separate json object for each question. 
Each such objects has six fields:
- `text`: the paragraph from which the question was created. The answer to the question can be derived from this text. It is possible to transform the benchmark into a reading comprehension benchmark by preceeding the question itself from this text.
- `question`: the question itself.
- `targets`: a list of acceptable (short) answers to the question.
- `target`: a long answer to the question, which could potentially be used for COT. Note that the long answers have not been checked as extensively as the questions and short answers.
- `id`: the wikipedia page that the text is sourced from, along with the rank of that page in the relevant locale.
- `output_type`: the expected type of the output (e.g.\ number, date, year, word, etc), in the question language.
- `source_language`: the language in which the question was originally sourced.
- `question_language`: the language in which the question is asked.
- `translated`: whether the question is translated.
- `translation_type`: whether the translation is machine- or human-authored.

### MultiLoKo-test
MultiLoKo also has a secret test set with 250 examples for each languages, which will be released later on, blindly.
The split is similar to the dev split, apart from the fact that the topics it includes are more obscure.
If you would like to obtain scores for your model on the set, please upload your model on HuggingFace and send us a request to compute scores through the creation of an issue on this [MultiLoKo github page](https://github.com/facebookresearch/multiloko).

We will return the full set of results to you, and put the test results of your model on the leaderboard on this page.
If it is not possible to upload your model on HuggingFace, please reach out to either one of the authors to discuss other options.


## Evaluation
On our github page, you can find an evaluation script [eval.py](https://github.com/facebookresearch/multiloko/eval.py) that can be ran directly on a model's output, provided in jsonl or csv.
The script postprocesses and normalises the model answers and computes f1 score, exact match score, sentence chrf, edit distance between the closest target, edit distance between the first target, and max edit similarity between the targets.
It also computes five aggregate metrics for each of the metrics above: the average score, the maximum and minimum scores (across languages), and the gap between the best and worst performing language. We support both CSV and JSONL. 

### Usage
```
$ ./eval.py --help
usage: eval.py [-h] --dataset_location DATASET_LOCATION --subset SUBSET --predictions PREDICTIONS [--output OUTPUT]

options:
  -h, --help            show this help message and exit
  --dataset_location, -d DATASET_LOCATION
                        Dataset root directory where all language folders are located
  --subset, -s SUBSET   subset, ie dev, test, etc. Should match the jsonl filename inside the individual dataset language folders
  --predictions, -p PREDICTIONS
                        Prediction file to evaluate. Could be CSV or JSONL
  --output, -o OUTPUT   Output file (json) to write results to. If not specified, will print to stdout
./eval.py -d benchmark_data -s dev -p examples/test.json -o testscore.json
```

### Metric cheat sheet

| Metric | Description |
| --- | --- |
| Average EM | The first main metric we use to quantify performance for MultiLoKo is the average Exact Match score across languages, which expresses how many of the answers match one of the gold standard answers verbatim (after post-processing the answers). |
| Gap | The second main metric is the gap between a model’s best and worst performing language. We gap to quantify the extent to which a model has achieved parity across languages. Because a small gap can be achieved both through parity on high scores as parity on low scores, it is most informative in combination with average benchmark performance. |
| Mother tongue effect (MTE) | MTE expresses the impact of asking questions in a language in which the requested information is locally salient, compared to asking it in English. A positive MTE indicates information is more readily available in the language it was (likely) present in the training data, whereas a negative mother tongue effect indicates the information is more easily accessible in English. |
|Locality effect (LE) | LE quantifies the effect of using locally sourced vs translated data. It is measured by computing the difference between scores for locally sourced data and translated English-sourced data. A positive LE implies that using translated English data underestimates performance on a language, a negative LE that using translated English data overestimates performance. |
