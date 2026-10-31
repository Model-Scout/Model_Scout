---
license: cc-by-nc-4.0
task_categories:
- text-generation
language:
- en
- de
- ar
- ja
- ko
- es
- zh
pretty_name: medit
size_categories:
- 10K<n<100K
tags:
- gec
- simplification
- paraphrasing
- es
- de
- ar
- en
- ja
- ko
- zh
- multilingual
---
# Dataset Card for mEdIT: Multilingual Text Editing via Instruction Tuning

## Paper: [mEdIT: Multilingual Text Editing via Instruction Tuning](https://arxiv.org/abs/2402.16472)
## Authors: Vipul Raheja, Dimitris Alikaniotis, Vivek Kulkarni, Bashar Alhafni, Dhruv Kumar
## Project Repo: [https://github.com/vipulraheja/medit](https://github.com/vipulraheja/medit)


## Dataset Summary
This is the dataset that was used to train the mEdIT text editing models. Full details of the dataset can be found in our paper.


# Dataset Structure
The dataset is in JSON format. 

## Data Instances
```
{
  "instance":999999,
  "task":"gec",
  "language":"english",
  "lang":"en",
  "dataset":"lang8.bea19",
  "src":"Luckily there was no damage for the earthquake .",
  "refs": ['Luckily there was no damage from the earthquake .'],
  "tgt":"Luckily there was no damage from the earthquake .",
  "prompt":"この文の文法上の誤りを修正してください: Luckily there was no damage for the earthquake .",
}
```

Note that for the mEdIT models, the `prompt` was formatted as follows: 
(e.g. for a Japanese-prompted editing for English text)
```
### 命令:\nこの文の文法上の誤りを修正してください\n### 入力:\nLuckily there was no damage for the earthquake .\n### 出力:\n\n
```
Details about the added keywords ("Instruction", "Input", "Output") can be found in the Appendix or on the mEdIT model cards. 


## Data Fields
* `instance`: instance ID
* `language`: Language of input and edited text 
* `lang`: Language code in ISO-639-1
* `dataset`: Source of the current example
* `task`: Text editing task for this instance
* `src`: input text 
* `refs`: reference texts
* `tgt`: output text
* `prompt`: Full prompt (instruction + input) for training the models


## Considerations for Using the Data
Please note that this dataset contains 102k instances (as opposed to the 190k instances we used in the paper). 
This is because this public release includes only the instances that were acquired and curated from publicly available datasets. 

Following are the details of the subsets (including the ones we are unable to publicly release):

*Grammatical Error Correction*:
- English:
  - FCE, Lang8, and W&I+LOCNESS data can be found at: https://www.cl.cam.ac.uk/research/nl/bea2019st/#data
  - *Note* that we are unable to share Lang8 data due to license restrictions
- Arabic:
  - The QALB-2014 and QALB-2015 datasets can be requested at: https://docs.google.com/forms/d/e/1FAIpQLScSsuAu1_84KORcpzOKTid0nUMQDZNQKKnVcMilaIZ6QF-xdw/viewform
  - *Note* that we are unable to share them due to license restrictions
  - ZAEBUC: Can be requested at https://docs.google.com/forms/d/e/1FAIpQLSd0mFkEA6SIreDyqQXknwQrGOhdkC9Uweszgkp73gzCErEmJg/viewform
- Chinese:
  - NLPCC-2018 data can be found at: https://github.com/zhaoyyoo/NLPCC2018_GEC
- German:
  - FalKO-MERLIN GEC Corpus can be found at: https://github.com/adrianeboyd/boyd-wnut2018?tab=readme-ov-file#download-data
- Spanish:
  - COWS-L2H dataset can be found at: https://github.com/ucdaviscl/cowsl2h
- Japanese:
  - NAIST Lang8 Corpora can be found at: https://sites.google.com/site/naistlang8corpora
  - *Note* that we are unable to share this data due to license restrictions
- Korean:
  - Korean GEC data can be found at: https://github.com/soyoung97/Standard_Korean_GEC
  - *Note* that we are unable to share this data due to license restrictions

*Simplification*:
- English:
  - WikiAuto dataset can be found at: https://huggingface.co/datasets/wiki_auto
  - WikiLarge dataset can be found at: https://github.com/XingxingZhang/dress
  - *Note* that we are unable to share Newsela data due to license restrictions.
- Arabic, Spanish, Korean, Chinese:
  - *Note* that we are unable to share the translated Newsela data due to license restrictions.
- German:
  - GeoLino dataset can be found at: http://www.github.com/Jmallins/ZEST.
  - TextComplexityDE dataset can be found at: https://github.com/babaknaderi/TextComplexityDE
- Japanese:
  - EasyJapanese and EasyJapaneseExtended datasets were taken from the MultiSim dataset: https://huggingface.co/datasets/MichaelR207/MultiSim/tree/main/data/Japanese


*Paraphrasing*: 
- Arabic: 
  - NSURL-19 (Shared Task 8) data can be found at: https://www.kaggle.com/competitions/nsurl-2019-task8
  - *Note* that we are unable to share the NSURL data due to license restrictions.
  - STS-17 dataset can be found at: https://alt.qcri.org/semeval2017/task1/index.php?id=data-and-tools
- English, Chinese, German, Japanese, Korean, Spanish:
  - PAWS-X data can be found at: https://huggingface.co/datasets/paws-x
 

## Citation 

```
@misc{raheja2024medit,
      title={mEdIT: Multilingual Text Editing via Instruction Tuning}, 
      author={Vipul Raheja and Dimitris Alikaniotis and Vivek Kulkarni and Bashar Alhafni and Dhruv Kumar},
      year={2024},
      eprint={2402.16472},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```