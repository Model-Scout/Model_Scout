---
license: cc-by-sa-4.0
task_categories:
- question-answering
language:
- en
- zh
- es
- id
- ko
- el
- fa
- ar
- az
- su
- as
- ha
- am
- eu
- bg
- fr
- ga
- ja
- ms
- sv
- tl
- ta
size_categories:
- 10K<n<100K
configs:
- config_name: annotations
  data_files:
    - split: DZ
      path: "data/annotations_hf/Algeria_data.json"
    - split: AS
      path: "data/annotations_hf/Assam_data.json"
    - split: AZ
      path: "data/annotations_hf/Azerbaijan_data.json"
    - split: CN
      path: "data/annotations_hf/China_data.json"
    - split: ET
      path: "data/annotations_hf/Ethiopia_data.json"
    - split: GR
      path: "data/annotations_hf/Greece_data.json"
    - split: ID
      path: "data/annotations_hf/Indonesia_data.json"
    - split: IR
      path: "data/annotations_hf/Iran_data.json"
    - split: MX
      path: "data/annotations_hf/Mexico_data.json"
    - split: KP
      path: "data/annotations_hf/North_Korea_data.json"
    - split: NG
      path: "data/annotations_hf/Northern_Nigeria_data.json"
    - split: KR
      path: "data/annotations_hf/South_Korea_data.json"
    - split: ES
      path: "data/annotations_hf/Spain_data.json"
    - split: GB
      path: "data/annotations_hf/UK_data.json"
    - split: US
      path: "data/annotations_hf/US_data.json"
    - split: JB
      path: "data/annotations_hf/West_Java_data.json"
- config_name: short-answer-questions
  data_files: 
    - split: DZ
      path: "data/questions_hf/Algeria_questions.json"
    - split: AS
      path: "data/questions_hf/Assam_questions.json"
    - split: AZ
      path: "data/questions_hf/Azerbaijan_questions.json"
    - split: CN
      path: "data/questions_hf/China_questions.json"
    - split: ET
      path: "data/questions_hf/Ethiopia_questions.json"
    - split: GR
      path: "data/questions_hf/Greece_questions.json"
    - split: ID
      path: "data/questions_hf/Indonesia_questions.json"
    - split: IR
      path: "data/questions_hf/Iran_questions.json"
    - split: MX
      path: "data/questions_hf/Mexico_questions.json"
    - split: KP
      path: "data/questions_hf/North_Korea_questions.json"
    - split: NG
      path: "data/questions_hf/Northern_Nigeria_questions.json"
    - split: KR
      path: "data/questions_hf/South_Korea_questions.json"
    - split: ES
      path: "data/questions_hf/Spain_questions.json"
    - split: GB
      path: "data/questions_hf/UK_questions.json"
    - split: US
      path: "data/questions_hf/US_questions.json"
    - split: JB
      path: "data/questions_hf/West_Java_questions.json"
- config_name: multiple-choice-questions
  data_files:
    - split: test
      path: "data/mc_questions_hf/mc_questions_file_v1.1.json"
    - split: semeval
      path: "data/mc_questions_hf/mc_questions_file_semeval.json"
- config_name: semeval-annotations
  data_files:
    - split: Arabic_Egypt
      path: "data_SemEval/annotations_hf/Arabic_Egypt_data.json"
    - split: Arabic_Morocco
      path: "data_SemEval/annotations_hf/Arabic_Morocco_data.json"
    - split: Arabic_SaudiArabia
      path: "data_SemEval/annotations_hf/Arabic_SaudiArabia_data.json"
    - split: Basque_BasqueCountry
      path: "data_SemEval/annotations_hf/Basque_BasqueCountry_data.json"
    - split: Bulgarian_Bulgaria
      path: "data_SemEval/annotations_hf/Bulgarian_Bulgaria_data.json"
    - split: English_Australia
      path: "data_SemEval/annotations_hf/English_Australia_data.json"
    - split: French_France
      path: "data_SemEval/annotations_hf/French_France_data.json"
    - split: Irish_Ireland
      path: "data_SemEval/annotations_hf/Irish_Ireland_data.json"
    - split: Japanese_Japan
      path: "data_SemEval/annotations_hf/Japanese_Japan_data.json"
    - split: Malay_Singapore
      path: "data_SemEval/annotations_hf/Malay_Singapore_data.json"
    - split: Mandarin_Singapore
      path: "data_SemEval/annotations_hf/Mandarin_Singapore_data.json"
    - split: Mandarin_Taiwan
      path: "data_SemEval/annotations_hf/Mandarin_Taiwan_data.json"
    - split: Spanish_Ecuador
      path: "data_SemEval/annotations_hf/Spanish_Ecuador_data.json"
    - split: Swedish_Sweden
      path: "data_SemEval/annotations_hf/Swedish_Sweden_data.json"
    - split: Tagalog_Philippines
      path: "data_SemEval/annotations_hf/Tagalog_Philippines_data.json"
    - split: Tamil_Singapore
      path: "data_SemEval/annotations_hf/Tamil_Singapore_data.json"
    - split: Tamil_SriLanka
      path: "data_SemEval/annotations_hf/Tamil_SriLanka_data.json"
- config_name: semeval-questions
  data_files:
    - split: Arabic_Egypt
      path: "data_SemEval/questions_hf/Arabic_Egypt_questions.json"
    - split: Arabic_Morocco
      path: "data_SemEval/questions_hf/Arabic_Morocco_questions.json"
    - split: Arabic_SaudiArabia
      path: "data_SemEval/questions_hf/Arabic_SaudiArabia_questions.json"
    - split: Basque_BasqueCountry
      path: "data_SemEval/questions_hf/Basque_BasqueCountry_questions.json"
    - split: Bulgarian_Bulgaria
      path: "data_SemEval/questions_hf/Bulgarian_Bulgaria_questions.json"
    - split: English_Australia
      path: "data_SemEval/questions_hf/English_Australia_questions.json"
    - split: French_France
      path: "data_SemEval/questions_hf/French_France_questions.json"
    - split: Irish_Ireland
      path: "data_SemEval/questions_hf/Irish_Ireland_questions.json"
    - split: Japanese_Japan
      path: "data_SemEval/questions_hf/Japanese_Japan_questions.json"
    - split: Malay_Singapore
      path: "data_SemEval/questions_hf/Malay_Singapore_questions.json"
    - split: Mandarin_Singapore
      path: "data_SemEval/questions_hf/Mandarin_Singapore_questions.json"
    - split: Mandarin_Taiwan
      path: "data_SemEval/questions_hf/Mandarin_Taiwan_questions.json"
    - split: Spanish_Ecuador
      path: "data_SemEval/questions_hf/Spanish_Ecuador_questions.json"
    - split: Swedish_Sweden
      path: "data_SemEval/questions_hf/Swedish_Sweden_questions.json"
    - split: Tagalog_Philippines
      path: "data_SemEval/questions_hf/Tagalog_Philippines_questions.json"
    - split: Tamil_Singapore
      path: "data_SemEval/questions_hf/Tamil_Singapore_questions.json"
    - split: Tamil_SriLanka
      path: "data_SemEval/questions_hf/Tamil_SriLanka_questions.json"
---
# BLEnD

This is the official repository of **[BLEnD: A Benchmark for LLMs on Everyday Knowledge in Diverse Cultures and Languages](https://arxiv.org/abs/2406.09948)** (Submitted to NeurIPS 2024 Datasets and Benchmarks Track).

*24/12/05: Updated translation errors*   
*25/05/02: Updated multiple choice questions file (v1.1)*   
*26/09/15: Added new data collected for [SemEval-2026 Task 7](https://github.com/BLEnD-SemEval2026/SemEval-2026-Task-7), covering 17 additional language-culture pairs (`semeval-annotations`, `semeval-questions`, and `semeval` split of `multiple-choice-questions`)*

## About
![BLEnD Construction & LLM Evaluation Framework](main_figure.png)

Large language models (LLMs) often lack culture-specific everyday knowledge, especially across diverse regions and non-English languages. Existing benchmarks for evaluating LLMs' cultural sensitivities are usually limited to a single language or online sources like Wikipedia, which may not reflect the daily habits, customs, and lifestyles of different regions. That is, information about the food people eat for their birthday celebrations, spices they typically use, musical instruments youngsters play, or the sports they practice in school is not always explicitly written online.
To address this issue, we introduce **BLEnD**, a hand-crafted benchmark designed to evaluate LLMs' everyday knowledge across diverse cultures and languages.
The benchmark comprises 52.6k question-answer pairs from 16 countries/regions, in 13 different languages, including low-resource ones such as Amharic, Assamese, Azerbaijani, Hausa, and Sundanese.
We evaluate LLMs in two formats: short-answer questions, and multiple-choice questions.
We show that LLMs perform better in cultures that are more present online, with a maximum 57.34% difference in GPT-4, the best-performing model, in the short-answer format.
Furthermore, we find that LLMs perform better in their local languages for mid-to-high-resource languages. Interestingly, for languages deemed to be low-resource, LLMs provide better answers in English.

## Requirements
```Python
datasets == 2.19.2
pandas == 2.1.4
```

## Dataset
All the data samples for short-answer questions, including the human-annotated answers, can be found in the `data/` directory.
Specifically, the annotations from each country are included in the `annotations` split, and each country/region's data can be accessed by **[country codes](https://huggingface.co/datasets/uilab/BLEnD#countryregion-codes)**. 
```Python
from datasets import load_dataset

# Login using e.g. `huggingface-cli login` to access this dataset
ds = load_dataset("uilab/BLEnD", "short-answer-questions")

# To access data from Assam:
ds_as = ds['AS']
```
Each file includes a JSON variable with question IDs, questions in the local language and English, the human annotations both in the local language and English, and their respective vote counts as values. The same dataset for South Korea is shown below:
```JSON
[{
    "ID": "Al-en-06",
    "question": "대한민국 학교 급식에서 흔히 볼 수 있는 음식은 무엇인가요?",
    "en_question": "What is a common school cafeteria food in your country?",
    "annotations": [
        {
            "answers": [
                "김치"
            ],
            "en_answers": [
                "kimchi"
            ],
            "count": 4
        },
        {
            "answers": [
                "밥",
                "쌀밥",
                "쌀"
            ],
            "en_answers": [
                "rice"
            ],
            "count": 3
        },
        ...
    ],
    "idks": {
        "idk": 0,
        "no-answer": 0,
        "not-applicable": 0
    }
}],
```

The topics and source language for each question can be found in `short-answer-questions` split. 
Questions for each country in their local languages and English can be accessed by **[country codes](https://huggingface.co/datasets/uilab/BLEnD#countryregion-codes)**. 
Each CSV file question ID, topic, source language, question in English, and the local language (in the `Translation` column) for all questions.
```Python
from datasets import load_dataset

questions = load_dataset("uilab/BLEnD",'short-answer-questions')

# To access data from Assam:
assam_questions = questions['AS']
```
The current set of multiple choice questions and their answers can be found at the `multiple-choice-questions` split.
```Python
from datasets import load_dataset

mcq = load_dataset("uilab/BLEnD",'multiple-choice-questions')
```
### Country/Region Codes
 |  **Country/Region**  | **Code**  | **Language**  | **Code**|
   |:--------:|:--------------:|:------------:|:------------:|
|     United States     |    US    |    English     |    en
|     United Kingdom    |   GB     |       English        |en
|         China         |    CN    |    Chinese     |    zh
|         Spain         |    ES    |    Spanish     |    es
|         Mexico        |    MX    |Spanish|es
|       Indonesia       |    ID    |   Indonesian   |    id
|      South Korea      |    KR    |     Korean     |    ko
|      North Korea      |    KP    |        Korean        |ko
|         Greece        |    GR    |     Greek      |    el
|          Iran         |    IR    |    Persian     |    fa
|        Algeria        |    DZ    |     Arabic     |    ar
|       Azerbaijan      |    AZ    |  Azerbaijani   |    az
|       West Java       |    JB    |   Sundanese    |    su
|         Assam         |    AS    |    Assamese    |    as
|    Northern Nigeria   |    NG    |     Hausa      |    ha
|        Ethiopia       |    ET    |    Amharic     |    am

### SemEval-2026 Task 7 Data
As part of [SemEval-2026 Task 7](https://github.com/BLEnD-SemEval2026/SemEval-2026-Task-7), we collected the same type of data for 17 additional language-culture pairs, expanding BLEnD's original 13 languages and 16 cultures. The newly added language-culture pairs are as follows:

#### Language-Culture Pair Codes
 |  **Country/Region**  | **Code**  | **Language**  | **Code**|
   |:--------:|:--------------:|:------------:|:------------:|
|         Egypt          |    Arabic_Egypt          |     Arabic     |    ar
|         Morocco          |    Arabic_Morocco          |     Arabic     |    ar
|         Saudi Arabia          |    Arabic_SaudiArabia          |     Arabic     |    ar
|         Basque Country          |    Basque_BasqueCountry          |     Basque     |    eu
|         Bulgaria          |    Bulgarian_Bulgaria          |     Bulgarian     |    bg
|         Australia          |    English_Australia          |     English     |    en
|         France          |    French_France          |     French     |    fr
|         Ireland          |    Irish_Ireland          |     Irish     |    ga
|         Japan          |    Japanese_Japan          |     Japanese     |    ja
|         Singapore          |    Malay_Singapore          |     Malay     |    ms
|         Singapore          |    Mandarin_Singapore          |     Mandarin     |    zh
|         Singapore          |    Tamil_Singapore          |     Tamil     |    ta
|         Taiwan          |    Mandarin_Taiwan          |     Mandarin     |    zh
|         Ecuador          |    Spanish_Ecuador          |     Spanish     |    es
|         Sweden          |    Swedish_Sweden          |     Swedish     |    sv
|         Philippines          |    Tagalog_Philippines          |     Tagalog     |    tl
|         Sri Lanka          |    Tamil_SriLanka          |     Tamil     |    ta

This data follows the same format described above. Annotations and questions are available via the `semeval-annotations` and `semeval-questions` configs, with one split per language-culture pair (e.g. `Arabic_Egypt`, `Mandarin_Taiwan`). The corresponding multiple-choice questions are available in the `semeval` split of the `multiple-choice-questions` config.
```Python
from datasets import load_dataset

# Annotations
semeval_annotations = load_dataset("uilab/BLEnD", "semeval-annotations")
egypt_annotations = semeval_annotations["Arabic_Egypt"]

# Questions
semeval_questions = load_dataset("uilab/BLEnD", "semeval-questions")
egypt_questions = semeval_questions["Arabic_Egypt"]

# Multiple-choice questions
mcq = load_dataset("uilab/BLEnD", "multiple-choice-questions")
semeval_mcq = mcq["semeval"]
```

## Citation
If you use BLEnD, please cite our paper:
```bibtex
@inproceedings{NEURIPS2024_8eb88844,
 author = {Myung, Junho and Lee, Nayeon and Zhou, Yi and Jin, Jiho and Putri, Rifki Afina and Antypas, Dimosthenis and Borkakoty, Hsuvas and Kim, Eunsu and Perez-Almendros, Carla and Ayele, Abinew Ali and Guti\'{e}rrez-Basulto, V\'{\i}ctor and Ib\'{a}\~{n}ez-Garc\'{\i}a, Yazm\'{\i}n and Lee, Hwaran and Muhammad, Shamsuddeen Hassan and Park, Kiwoong and Rzayev, Anar Sabuhi and White, Nina and Yimam, Seid Muhie and Pilehvar, Mohammad Taher and Ousidhoum, Nedjma and Camacho-Collados, Jose and Oh, Alice},
 booktitle = {Advances in Neural Information Processing Systems},
 doi = {10.52202/079017-2483},
 editor = {A. Globerson and L. Mackey and D. Belgrave and A. Fan and U. Paquet and J. Tomczak and C. Zhang},
 pages = {78104--78146},
 publisher = {Curran Associates, Inc.},
 title = {BLEnD: A Benchmark for LLMs on Everyday Knowledge in Diverse Cultures and Languages},
 url = {https://proceedings.neurips.cc/paper_files/paper/2024/file/8eb88844dafefa92a26aaec9f3acad93-Paper-Datasets_and_Benchmarks_Track.pdf},
 volume = {37},
 year = {2024}
}
```

If you use the SemEval-2026 Task 7 data (`semeval-annotations`, `semeval-questions`, and the `semeval` split of `multiple-choice-questions`), please also cite:
```bibtex
@inproceedings{ousidhoum-etal-2026-semeval,
    title = "{S}em{E}val-2026 Task 7: Everyday Knowledge Across Diverse Languages and Cultures",
    author = "Ousidhoum, Nedjma  and
      Myung, Junho  and
      Perez-Almendros, Carla  and
      Jin, Jiho  and
      Keleg, Amr  and
      Beloucif, Meriem  and
      Zhou, Yi  and
      Agerri, Rodrigo  and
      Araujo, Vladimir  and
      Baes, Naomi  and
      Barry, James  and
      Boisson, Joanne  and
      Chen, Nancy F.  and
      de Kock, Christine  and
      Edwards, Aleksandra  and
      Fernandez de Landa, Joseba  and
      Fazli Imam, Mohamed  and
      Hakami, Huda  and
      Hsieh, Shu-Kai  and
      Imperial, Joseph Marvin  and
      Lee, Roy Ka-Wei  and
      Liu, Zhengyuan  and
      Lyu, Chenyang  and
      Samih, Younes  and
      Sjons, Johan  and
      Tan, Bryan  and
      Ushio, Asahi  and
      Zheng, Weihua  and
      Oh, Alice  and
      Camacho-Collados, Jose",
    editor = "Kochmar, Ekaterina  and
      Ghosh, Debanjan  and
      North, Kai  and
      Komachi, Mamoru  and
      Zampieri, Marcos",
    booktitle = "Proceedings of the 20th {I}nternational {W}orkshop on {S}emantic {E}valuation (2026)",
    month = jul,
    year = "2026",
    address = "San Diego, California, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.semeval-1.455/",
    doi = "10.18653/v1/2026.semeval-1.455",
    pages = "3823--3837",
    ISBN = "979-8-89176-414-9"
}
```
